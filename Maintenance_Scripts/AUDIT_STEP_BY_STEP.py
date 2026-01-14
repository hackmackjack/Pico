import re

def rigorous_audit():
    file_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into projects
    projects = re.split(r'(?=## \d+\. Project \d+:)', content)
    projects = projects[1:] # Skip preamble
    
    non_compliant_ids = []
    
    print(f"Auditing {len(projects)} projects for Elite Standard Step-by-Step compliance...")
    
    for proj_text in projects:
        # Extract ID
        match = re.search(r'Project (\d+):', proj_text)
        if not match: continue
        pid = match.group(1)
        
        # Extract Guide
        guide_match = re.search(r'### 8\. Step-by-Step Guide(.*?)### 9\. Execution Flow', proj_text, re.DOTALL)
        if not guide_match:
            print(f"[FAIL] Project {pid}: Missing Section 8 completely.")
            non_compliant_ids.append(pid)
            continue
            
        guide_text = guide_match.group(1)
        
        has_snap = "**Snap**" in guide_text
        has_category = "From **" in guide_text
        
        verdict = "PASS"
        if not has_snap or not has_category:
            verdict = "FAIL"
            non_compliant_ids.append(pid)
        
        print(f"Project {pid}: {verdict}")

    # Write report to file with correct encoding
    with open(r'd:\MFF\Pico\audit_report_final.txt', 'w', encoding='utf-8') as f:
        f.write("AUDIT REPORT FINAL\n")
        f.write(f"Total Projects: {len(projects)}\n")
        f.write(f"Failed Count: {len(non_compliant_ids)}\n")
        f.write(f"Failed IDs: {non_compliant_ids}\n")
        
    print(f"Audit Complete. Results saved to d:\\MFF\\Pico\\audit_report_final.txt")

if __name__ == "__main__":
    rigorous_audit()
