import re

file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200.md"

def check_projects():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    project_starts = []
    for i, line in enumerate(lines):
        if line.strip().startswith("## 1. Project"):
            project_starts.append(i)
    
    project_starts.append(len(lines)) # End sentinel

    print(f"{'Project':<10} | {'Status':<10} | {'Missing Sections'}")
    print("-" * 50)

    pass_count = 0
    fail_count = 0

    for i in range(len(project_starts) - 1):
        start_line = project_starts[i]
        end_line = project_starts[i+1]
        
        proj_content = "".join(lines[start_line:end_line])
        
        # Extract Project ID
        header = lines[start_line].strip()
        match = re.search(r'Project (\d+)', header)
        if match:
            proj_id = match.group(1)
        else:
            proj_id = "UNKNOWN"

        missing = []
        # Check for Sections 2-12 (Section 1 is the header itself)
        # We look for "### N. " pattern
        
        # Standard Headers as expected in "Enhanced Detail Standard v2.0"
        # 2. Learning Objective
        # 3. Concepts Introduced
        # 4. Hardware Required
        # 5. Wiring / Interfaces
        # 6. Blocks Used
        # 7. Variables
        # 8. Step-by-Step Guide
        # 9. Execution Flow
        # 10. Generated Code
        # 11. Common Mistakes
        # 12. Try This Next
        
        for sec_num in range(2, 13):
            # Regex to match "### N." or "### N "
            pattern = re.compile(rf'^### {sec_num}\.', re.MULTILINE)
            if not pattern.search(proj_content):
                missing.append(str(sec_num))
        
        if not missing:
            status = "PASS"
            pass_count += 1
            missing_str = "-"
        else:
            status = "FAIL"
            fail_count += 1
            missing_str = ",".join(missing)
        
        print(f"{proj_id:<10} | {status:<10} | {missing_str}")

    print("-" * 50)
    print(f"Total Projects: {len(project_starts)-1}")
    print(f"Passed: {pass_count}")
    print(f"Failed: {fail_count}")

if __name__ == "__main__":
    check_projects()
