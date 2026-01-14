import re

file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200.md"
report_path = r"d:\MFF\Pico\report_utf8.txt"

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
    
    project_starts.append(len(lines))

    with open(report_path, 'w', encoding='utf-8') as out:
        out.write(f"{'Project':<10} | {'Status':<10} | {'Missing Sections'}\n")
        out.write("-" * 50 + "\n")

        pass_count = 0
        fail_count = 0

        for i in range(len(project_starts) - 1):
            start_line = project_starts[i]
            end_line = project_starts[i+1]
            
            proj_content = "".join(lines[start_line:end_line])
            header = lines[start_line].strip()
            # Strict Regex for project ID "0153" etc
            match = re.search(r'Project (\d+)', header)
            if match:
                proj_id = match.group(1)
            else:
                proj_id = "UNKNOWN"

            missing = []
            for sec_num in range(2, 13):
                # Search for "### 2." etc.
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
            
            out.write(f"{proj_id:<10} | {status:<10} | {missing_str}\n")

        out.write("-" * 50 + "\n")
        out.write(f"Total Projects: {len(project_starts)-1}\n")
        out.write(f"Passed: {pass_count}\n")
        out.write(f"Failed: {fail_count}\n")

if __name__ == "__main__":
    check_projects()
