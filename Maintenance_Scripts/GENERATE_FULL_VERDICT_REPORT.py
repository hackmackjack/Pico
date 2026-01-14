
import os
import re
import glob

def assess_guide(guide_text):
    has_snap = "**Snap**" in guide_text
    has_from = "From **" in guide_text
    
    if has_snap and has_from:
        return "PASS", "✅"
    elif has_snap and not has_from:
        return "NEEDS POLISH (Missing Source)", "⚠️"
    elif not has_snap:
        return "FAIL (No Snap)", "❌"
    return "UNKNOWN", "❓"

def check_function_consistency(guide, code):
    """
    Ensures that any function defined in the code (def func_name) 
    is explicitly mentioned in the Step-by-Step Guide.
    """
    # Find all python function definitions
    defined_funcs = re.findall(r'def\s+(\w+)\s*\(', code)
    
    missing = []
    for func in defined_funcs:
        # Check if function name appears in guide (case insensitive)
        if func.lower() not in guide.lower():
            missing.append(func)
            
    if missing:
        return False, f"Abstraction Gap: Code defines functions {missing} but Guide does not mention them."
    return True, ""

def validate_project(project_text):
    """
    Validates a single project block against Elite Standard v2.0.
    """
    issues = []
    
    # Extract Guide
    guide_match = re.search(r'### 8\. Step-by-Step Guide(.*?)### 9\.', project_text, re.DOTALL)
    code_match = re.search(r'### 10\. Generated Code(.*?)### 11\.', project_text, re.DOTALL)
    
    if not guide_match:
        return "Failed", ["Missing '### 8. Step-by-Step Guide' section."]
    
    guide_content = guide_match.group(1).strip()
    
    # 1. Check for 'From Category, drag Block' syntax
    if "from " not in guide_content.lower() or "drag " not in guide_content.lower():
         if "snap" not in guide_content.lower():
             issues.append("Guide missing explicit 'From [Category], drag [Block]' or 'Snap' instructions.")
             
    # 2. Check Loop instructions
    if "pico_forever" in project_text and "pico_forever" not in guide_content:
        issues.append("Code uses 'pico_forever' but Guide does not mention 'pico_forever' or 'forever loop'.")

    # NEW: Check Function Consistency
    if code_match:
        code_content = code_match.group(1).strip()
        consistent, message = check_function_consistency(guide_content, code_content)
        if not consistent:
            issues.append(message)

    if issues:
        return "Failed", issues
        
    return "Passed", []

def generate_full_report():
    docs_dir = r"d:\MFF\Pico\Documentation"
    output_path = r"d:\MFF\Pico\FULL_VERDICT_REPORT.md"
    
    # regex for Docs_XXXX_XXXX.md
    doc_files = glob.glob(os.path.join(docs_dir, "Docs_*.md"))
    
    # Sort files to be in order
    doc_files.sort()
    
    all_results = []
    
    print(f"Found {len(doc_files)} documentation files.")
    
    final_report = []
    final_report.append("# 📊 Comprehensive Verdict Report (All Stages)\n")
    final_report.append(f"**Generated on:** {os.popen('date /t').read().strip()}\n")
    
    total_pass = 0
    total_polish = 0
    total_fail = 0
    
    for file_path in doc_files:
        filename = os.path.basename(file_path)
        
        # Skip backup/temp files
        if "BACKUP" in filename or "NEW" in filename or "BEFORE" in filename or "ADVANCED" in filename:
            continue
            
        print(f"Processing {filename}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract Projects
        # Regex to capture "## X. Project <ID>:" or similar
        # Depending on file format consistency, this might need to vary.
        # Most follow "## [Num]. Project [ID]:"
        
        project_blocks = re.split(r'(?=## \d+\. Project \d+:)', content)
        if len(project_blocks) < 2:
            # Try alternative header format if standard one fails
             project_blocks = re.split(r'(?=## Project \d+:)', content)
             
        project_blocks = project_blocks[1:] # Skip preamble
        
        file_results = []
        
        for block in project_blocks:
            # Extract ID
            id_match = re.search(r'Project (\d+):', block)
            if not id_match: continue
            pid = id_match.group(1)
            
            # Use the new validation function
            verdict_status, issues = validate_project(block)
            
            if verdict_status == "Passed":
                verdict = "PASS"
                icon = "✅"
            else:
                # For now, if there are issues, mark as FAIL and list issues
                # This can be refined later to distinguish between "FAIL" and "NEEDS POLISH"
                verdict = f"FAIL ({'; '.join(issues)})"
                icon = "❌"

            file_results.append((pid, verdict, icon))
            
            if verdict_status == "Passed": total_pass += 1
            elif "POLISH" in verdict: total_polish += 1 # This logic might need adjustment based on how validate_project evolves
            else: total_fail += 1
            
        # Append to report
        if file_results:
            final_report.append(f"\n## 📂 {filename} ({len(file_results)} Projects)\n")
            final_report.append("| Project ID | Verdict | Status |")
            final_report.append("| :--- | :--- | :--- |")
            for pid, v, i in file_results:
                final_report.append(f"| {pid} | {v} | {i} |")
                
    # Summary Header
    summary = "\n## 📈 Global Summary\n"
    summary += f"*   **Total Projects Verified**: {total_pass + total_polish + total_fail}\n"
    summary += f"*   **✅ Passed**: {total_pass}\n"
    summary += f"*   **⚠️ Needs Polish**: {total_polish}\n"
    summary += f"*   **❌ Failed**: {total_fail}\n"
    
    final_report.insert(2, summary) # Insert after title
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(final_report))
        
    print(f"Assessment Complete. Report saved to {output_path}")

if __name__ == "__main__":
    generate_full_report()
