
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
REPORT_FILE = r"C:\Users\LocalAdmin\.gemini\antigravity\brain\cb0952c1-2c91-456d-a19a-36d44aa8a62d\guide_quality_audit.md"

def audit_guide_quality():
    with open(DOC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    projects = re.split(r'^## 1️⃣ Project ', content, flags=re.MULTILINE)[1:]
    report_lines = ["# Guide Quality Audit Report\n"]
    
    # We want to check if the new 'Step-by-Step Guide' sections are actually "step-by-step"
    # or if they are still using the old abstract style (e.g. "A. Initialization Phase").
    
    # Heuristics for "Good" Guides:
    # 1. Mentions specific actions: "Drag", "Click", "Snap", "From [Category]"
    # 2. Does NOT use abstract headers: "A. Initialization Phase", "B. Main Loop Phase"
    
    bad_projects = []
    
    for proj in projects:
        title_match = re.match(r'(\d+): (.+)', proj)
        if not title_match: continue
        p_id = title_match.group(1)
        p_title = title_match.group(2).strip()
        
        guide_match = re.search(r'### 8️⃣ Step-by-Step Guide\n(.*?)\n###', proj, re.DOTALL)
        if not guide_match:
            report_lines.append(f"## Project {p_id}: Missing Guide Section")
            continue
            
        guide_text = guide_match.group(1).strip()
        
        # Check for Old Abstract Headers
        if "*   **A. Initialization Phase**" in guide_text:
            bad_projects.append(f"{p_id}: Still uses Abstract Phases")
            continue
            
        # Check for Instructional Keywords
        keywords = ["drag", "click", "snap", "from"]
        score = sum(1 for k in keywords if k in guide_text.lower())
        
        if score < 1:
             bad_projects.append(f"{p_id}: Low instruction count - might be too abstract.")

    report_lines.append(f"Found {len(bad_projects)} projects with potentially poor quality guides:")
    for bp in bad_projects:
        report_lines.append(f"- {bp}")
        
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"Audit complete. Found {len(bad_projects)} potential issues.")

if __name__ == "__main__":
    audit_guide_quality()
