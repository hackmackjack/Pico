
import re
import sys

# Path to the master documentation file
DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def parse_project(project_text, project_id):
    """Parses a single project text block into its components."""
    sections = {}
    
    # Simple regex to split by headers
    # Note: Headers are like "### 4️⃣ Hardware Required"
    # We will grab content between headers
    
    headers = [
        "1️⃣ Project", "2️⃣ Learning Objective", "3️⃣ Concepts Introduced", 
        "4️⃣ Hardware Required", "5️⃣ Wiring / Interfaces", "6️⃣ Blocks Used",
        "7️⃣ Variables & State", "8️⃣ Block Logic", "9️⃣ Execution Flow",
        "🔟 Generated Code", "1️⃣1️⃣ Common Mistakes", "1️⃣2️⃣ Try This Next"
    ]
    
    lines = project_text.split('\n')
    current_section = None
    buffer = []
    
    for line in lines:
        # Check if line works as a header start
        found_header = False
        for h in headers:
            if h in line:
                if current_section:
                    sections[current_section] = "\n".join(buffer).strip()
                current_section = h
                buffer = []
                found_header = True
                break
        
        if not found_header and current_section:
            buffer.append(line)
            
    if current_section:
        sections[current_section] = "\n".join(buffer).strip()
        
    return sections

def audit_consistency():
    print(f"Deep Auditing {DOC_PATH}...")
    try:
        with open(DOC_PATH, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    # Split by Project Header
    raw_projects = re.split(r'##\s+1️⃣\s+Project', content)
    # First split is usually empty or file header
    projects = raw_projects[1:]
    
    issues_found = 0
    
    for i, proj_text in enumerate(projects):
        # We need to reconstruct the header slightly or just look for the ID
        # The split consumed "## 1️⃣ Project"
        # So proj_text starts with "0001: Title..."
        
        # Get ID
        id_match = re.match(r'\s*(\d+):', proj_text)
        if not id_match:
            print(f"Skipping malformed block index {i}")
            continue
            
        pid = id_match.group(1)
        
        sections = parse_project(proj_text, pid)
        
        # --- Audit Checks ---
        
        errors = []
        
        # 1. Hardware vs Wiring
        hardware = sections.get("4️⃣ Hardware Required", "")
        wiring = sections.get("5️⃣ Wiring / Interfaces", "")
        
        hardware_items = [line.strip().replace('*', '').strip() for line in hardware.split('\n') if '*' in line]
        wiring_items = []
        # Parse markdown table logic roughly
        for line in wiring.split('\n'):
            if '|' in line and '---' not in line and 'Component' not in line:
                parts = line.split('|')
                if len(parts) > 2:
                    comp_name = parts[1].strip().replace('**', '')
                    wiring_items.append(comp_name)
        
        # Check coverage (Is every wired item in hardware list?)
        # Soft check because naming might differ slightly ("Red LED" vs "LED")
        # Skipping for now to focus on Code Alignment which is safer
        
        # 2. Wiring vs Code (CRITICAL)
        code_section = sections.get("🔟 Generated Code", "")
        
        # Extract Pins from Wiring Table
        # Look for "GP[0-9]+"
        wired_pins = set(re.findall(r'GP(\d+)', wiring))
        
        # Extract Pins from Code
        # machine.Pin(X, ...)
        code_pins = set(re.findall(r'Pin\(\s*(\d+)', code_section))
        
        # Also check for explicit references like "Pico W Onboard LED" which is "LED" or "GP25"
        if "LED" in wiring or "Onboard" in wiring:
             # GP25 is predominantly used for LED
             pass
             
        # Verification: Are all Code Pins in the Wiring Table?
        for pin in code_pins:
            if pin not in wired_pins:
                # Exception: Onboard LED (GP25) often omitted from simple wiring tables or called "Built-in"
                if pin == "25":
                    # Check if "Onboard" or "Built-in" or "LED" is in wiring text
                    if "On-board" in wiring or "Built-in" in wiring or "Icon" in wiring or "Start LED" in wiring:
                        continue
                
                # Check if the wiring table actually lists it but regex missed it (e.g., inside a range?)
                # Or maybe user defined it differently.
                errors.append(f"Code uses GP{pin} but Wiring Table does not explicitly list GP{pin}.")

        # 3. Variables vs Code
        vars_section = sections.get("7️⃣ Variables & State", "")
        # Extract bolded variables like **count**
        doc_vars = set(re.findall(r'\*\s*\*\*([a-zA-Z0-9_]+)\*\*', vars_section))
        
        # Check if these appear in code
        for var in doc_vars:
            if var not in code_section and var != "None":
                # Check for case sensitivity issues or partial matches
                if var.lower() not in code_section.lower():
                     errors.append(f"Variable '{var}' defined in docs but not found in code.")

        if errors:
            print(f"Project {pid} Issues:")
            for err in errors:
                print(f"  - {err}")
            issues_found += len(errors)

    if issues_found == 0:
        print("Consistency Audit Passed: Wiring and Code are aligned.")
    else:
        print(f"Found {issues_found} consistency issues.")

if __name__ == "__main__":
    audit_consistency()
