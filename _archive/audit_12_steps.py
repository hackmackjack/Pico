
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
REPORT_FILE = r"C:\Users\LocalAdmin\.gemini\antigravity\brain\cb0952c1-2c91-456d-a19a-36d44aa8a62d\final_12_step_audit.md"

REQUIRED_SECTIONS = [
    (1, r'## 1️⃣ Project'),
    (2, r'### 2️⃣ Learning Objective'),
    (3, r'### 3️⃣ Concepts Introduced'),
    (4, r'### 4️⃣ Hardware Required'),
    (5, r'### 5️⃣ Wiring / Interfaces'),
    (6, r'### 6️⃣ Blocks Used'),
    (7, r'### 7️⃣ Variables & State'),
    (8, r'### 8️⃣ Step-by-Step Guide'),
    (9, r'### 9️⃣ Execution Flow'),
    (10, r'### 🔟 Generated Code'),
    (11, r'### 1️⃣1️⃣ Common Mistakes'),
    (12, r'### 1️⃣2️⃣ Try This Next')
]

def audit_12_steps():
    try:
        with open(DOC_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Split by project (keep delimiters to know where P1 starts)
    # We split by '## 1️⃣ Project'
    # The first chunk is preamble. Subsequent chunks are projects (but we split on the header, so the header is consumed?)
    # Better: split by newline + '## 1️⃣ ' to avoid capturing the very first line if it starts there.
    
    projects = re.split(r'(?=\n## 1️⃣ Project )', content)
    
    # Filter out empty or preamble
    projects = [p for p in projects if '## 1️⃣ Project ' in p]
    
    report_lines = []
    report_lines.append("# Final 12-Step Documentation Audit (Projects 0001-0100)")
    report_lines.append("")
    report_lines.append("| Project | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | Status |")
    report_lines.append("| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |")
    
    total_projects = len(projects)
    perfect_projects = 0
    
    for p in projects:
        # Extract ID
        id_match = re.search(r'## 1️⃣ Project (\d+):', p)
        if not id_match:
            continue
        pid = id_match.group(1)
        
        row = [f"**{pid}**"]
        is_perfect = True
        
        for step_num, regex in REQUIRED_SECTIONS:
            if re.search(regex, p):
                row.append("✅")
            else:
                row.append("❌")
                is_perfect = False
        
        if is_perfect:
            row.append("PASS")
            perfect_projects += 1
        else:
            row.append("**FAIL**")
            
        report_lines.append("| " + " | ".join(row) + " |")

    report_lines.append("")
    report_lines.append(f"**Summary:** {perfect_projects}/{total_projects} Projects are 100% Compliant.")
    
    if perfect_projects == total_projects:
        report_lines.append("\n## 🎉 VERDICT: 100% GOOD")
    else:
        report_lines.append(f"\n## ⚠️ VERDICT: {total_projects - perfect_projects} Projects need attention.")

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"Audit Complete. Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    audit_12_steps()
