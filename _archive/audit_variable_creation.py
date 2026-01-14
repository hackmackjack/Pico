
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
REPORT_FILE = r"C:\Users\LocalAdmin\.gemini\antigravity\brain\cb0952c1-2c91-456d-a19a-36d44aa8a62d\variable_audit_report.md"

def audit_variables():
    try:
        with open(DOC_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    projects = re.split(r'^## 1️⃣ Project ', content, flags=re.MULTILINE)[1:]
    report_lines = ["# Variable Creation Audit Report\n"]
    total_issues = 0

    print(f"DEBUG: Found {len(projects)} projects.")
    for proj in projects:
        # Extract ID and Title
        title_match = re.match(r'(\d+): (.+)', proj)
        if not title_match:
            continue
        p_id = title_match.group(1)
        
        # Extract Variables Section
        vars_match = re.search(r'### 7️⃣ Variables & State\n(.*?)\n###', proj, re.DOTALL)
        if not vars_match:
            continue
            
        vars_text = vars_match.group(1).strip()
        variable_names = re.findall(r'\*\s+\*\*(.+?)\*\*', vars_text)
        if p_id == "0075":
            print(f"DEBUG 0075 vars_text: {vars_text!r}")
            print(f"DEBUG 0075 matches: {variable_names}")
            
        if not variable_names:
            continue

        # Extract Block Logic Section
        logic_match = re.search(r'### 8️⃣ Block Logic\n(.*?)\n###', proj, re.DOTALL)
        logic_text = logic_match.group(1).strip().lower() if logic_match else ""

        # Check for indicators of variable creation
        if "create variable" not in logic_text and "setup variables" not in logic_text:
             report_lines.append(f"## Project {p_id}")
             report_lines.append(f"Variables defined: {', '.join(variable_names)}")
             report_lines.append("Missing explicit variable setup.\n")
             total_issues += 1

    report_lines.append(f"\n**Total Projects Missing Variable Setup:** {total_issues}")

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    print(f"Audit complete. Found {total_issues} projects.")

if __name__ == "__main__":
    audit_variables()
