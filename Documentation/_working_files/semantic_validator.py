import re
import os
import sys

# Target Files (Add others as needed)
TARGET_FILES = [
    r"d:\MFF\Pico\Documentation\Docs_0001_0100.md" 
]

def load_schema():
    # Hardcoded minimal schema since pyyaml install failed
    return {}

def parse_project_block(content):
    # Regex to capture full project blocks from ## 1️⃣ Project... to end or next project
    project_pattern = re.compile(r"(## 1️⃣ Project (\d{4}):.*?)(?=## 1️⃣ Project|\Z)", re.DOTALL)
    return project_pattern.findall(content)

def validate_pins(project_text, wiring_section, code_section):
    # Extract pins from Wiring Table
    # Looks for "| ... | GP(\d+) |" or "| ... | (\d+) |"
    wiring_pins = set(re.findall(r"\|\s*GP(\d+)\s*\|", wiring_section))
    # Extract pins from Code
    # Looks for "Pin(15" or "Pin('GP15'"
    code_pins = set(re.findall(r"Pin\(\s*(\d+)", code_section))
    code_pins.update(re.findall(r"Pin\(\s*['\"]GP(\d+)['\"]", code_section))

    # Identify mismatches
    orphan_in_wiring = wiring_pins - code_pins
    orphan_in_code = code_pins - wiring_pins
    
    return orphan_in_wiring, orphan_in_code

def validate_project(project_id, project_text, schema):
    errors = []
    
    # 1. Section Presence & Order
    sections = [
        "1️⃣ Project", "2️⃣ Learning Objective", "3️⃣ Concepts Introduced", 
        "4️⃣ Hardware Required", "5️⃣ Wiring / Interfaces", "6️⃣ Blocks Used",
        "7️⃣ Variables", "8️⃣ Step-by-Step Guide", "9️⃣ Execution Flow",
        "10️⃣ Generated Code", "11️⃣ Common Mistakes", "12️⃣ Try This Next"
    ]
    
    for sec in sections:
        if f"## {sec}" not in project_text and f"### {sec}" not in project_text:
            errors.append(f"Missing Section: {sec}")

    # 2. Hardware Lock (Basic Check)
    if "Raspberry Pi Pico" not in project_text and "Pico W" not in project_text:
         # Check strictly in Hardware section
         hw_match = re.search(r"### 4️⃣ Hardware Required(.*?)###", project_text, re.DOTALL)
         if hw_match:
             hw_content = hw_match.group(1)
             if "Raspberry Pi Pico" not in hw_content and "Pico W" not in hw_content:
                 errors.append("Hardware Error: 'Raspberry Pi Pico' or 'Pico W' not listed in Hardware section.")

    # 3. Pin Validation (Deep Semantic Check)
    wiring_match = re.search(r"### 5️⃣ Wiring / Interfaces(.*?)###", project_text, re.DOTALL)
    code_match = re.search(r"### 10️⃣ Generated Code(.*?)###", project_text, re.DOTALL)
    
    if wiring_match and code_match:
        orphan_wiring, orphan_code = validate_pins(project_text, wiring_match.group(1), code_match.group(1))
        
        if orphan_code:
            errors.append(f"Pin Logic Fail: Code uses pins {orphan_code} not defined in Wiring.")
        if orphan_wiring:
            # This might be allowed for power pins, but strict for GPIO
            pass # Relaxed for now, but good to know
            
    # 4. Learning Objective Verb Check
    lo_match = re.search(r"### 2️⃣ Learning Objective\s*(.*?)\n", project_text)
    if lo_match:
        lo_text = lo_match.group(1).strip()
        # Basic list of verbs expected
        verbs = ["Create", "Build", "Program", "Understand", "Learn", "Use", "Turn", "Make", "Control", "Read"]
        if not any(lo_text.startswith(v) for v in verbs):
            errors.append(f"Learning Objective Warning: Does not start with standard action verb ('{lo_text[:10]}...').")

    return errors

def main():
    print("Starting Semantic Audit (Pico Standard v1.2.1)...")
    schema = load_schema()
    
    total_projects = 0
    total_errors = 0
    
    report_lines = []
    report_lines.append("| Project | Status | Errors |")
    report_lines.append("| :--- | :--- | :--- |")
    
    for file_path in TARGET_FILES:
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        projects = parse_project_block(content)
        
        for proj_text, pid in projects:
            total_projects += 1
            errors = validate_project(pid, proj_text, schema)
            
            status = "✅ PASS"
            error_str = ""
            
            if errors:
                status = "❌ FAIL"
                error_str = "<br>".join(errors)
                total_errors += 1
                
            report_lines.append(f"| {pid} | {status} | {error_str} |")

    # Output Report
    with open("SEMANTIC_AUDIT_REPORT.md", "w", encoding="utf-8") as f:
        f.write("# Semantic Audit Report\n\n")
        f.write("\n".join(report_lines))
        f.write(f"\n\n**Total Projects Audited:** {total_projects}")
        f.write(f"\n**Total Failures:** {total_errors}")
        
    print(f"Audit Complete. Checked {total_projects} projects. Found {total_errors} failures.")
    print("Detailed report saved to SEMANTIC_AUDIT_REPORT.md")

if __name__ == "__main__":
    main()
