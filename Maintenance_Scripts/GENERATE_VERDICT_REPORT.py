import re

def generate_verdict():
    file_path = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into projects
    # Regex to capture "## X. Project <ID>:"
    project_blocks = re.split(r'(?=## \d+\. Project \d+:)', content)
    
    # Skip preamble
    project_blocks = project_blocks[1:]
    
    results = []
    
    print(f"Analyzing {len(project_blocks)} projects...")
    
    for block in project_blocks:
        # Get ID
        id_match = re.search(r'Project (\d+):', block)
        if not id_match: continue
        pid = id_match.group(1)
        
        # Get Guide
        guide_match = re.search(r'### 8\. Step-by-Step Guide(.*?)### 9\. Execution Flow', block, re.DOTALL)
        if not guide_match:
            results.append((pid, "FAIL - NO GUIDE"))
            continue
            
        guide = guide_match.group(1)
        
        # STRICT CRITERIA
        has_snap = "**Snap**" in guide
        has_from = "From **" in guide
        has_drag = "drag `" in guide or "drag *" in guide or "drag p" in guide # generic check
        
        verdict = ""
        
        if has_snap and has_from:
            verdict = "PASS"
        elif has_snap and not has_from:
             verdict = "NEEDS POLISH (Missing Source Category)"
        elif not has_snap:
            verdict = "FAIL (No Snap)"
            
        results.append((pid, verdict))

    # Write Report
    report_path = r'd:\MFF\Pico\VERDICT_REPORT_0400.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Final Verdict Report: Projects 0401-0500\n\n")
        f.write("| Project ID | Verdict | Status |\n")
        f.write("| :--- | :--- | :--- |\n")
        
        pass_count = 0
        polish_count = 0
        fail_count = 0
        
        for pid, v in results:
            icon = "✅" if v == "PASS" else ("⚠️" if "POLISH" in v else "❌")
            f.write(f"| {pid} | {v} | {icon} |\n")
            
            if v == "PASS": pass_count += 1
            elif "POLISH" in v: polish_count += 1
            else: fail_count += 1
            
        f.write(f"\n## Summary\n")
        f.write(f"*   **Passed (Elite Standard)**: {pass_count}\n")
        f.write(f"*   **Needs Polish (Acceptable)**: {polish_count}\n")
        f.write(f"*   **Failed (Non-Compliant)**: {fail_count}\n")
        
    print(f"Report generated at {report_path}")
    print(f"Passed: {pass_count}, Polish: {polish_count}, Failed: {fail_count}")

if __name__ == "__main__":
    generate_verdict()
