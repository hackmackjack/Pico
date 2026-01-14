"""
Audit Script for Section 8 (Step-by-Step Guide) Compliance
Scans Docs_0101_0200_FINAL.md for projects missing:
1. A/B/C subsection structure (Initialization/Main Loop/Event Handling)
2. "Snap" instructions
3. Proper block category syntax (**Category** → Block Name)
"""

import re

def audit_section_8_compliance(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by projects
    projects = re.split(r'## .*?Project \d+:', content)
    
    issues = []
    
    for i, project in enumerate(projects[1:], start=1):  # Skip first empty split
        project_match = re.search(r'## .*?Project (\d+):', content.split(project)[0][-100:])
        if not project_match:
            continue
        
        project_num = project_match.group(1)
        
        # Find Section 8
        section_8_match = re.search(r'### 8.*?Step-by-Step Guide\s*\n(.*?)(?=\n### 9|$)', project, re.DOTALL)
        
        if not section_8_match:
            issues.append(f"Project {project_num}: Missing Section 8")
            continue
        
        section_8_content = section_8_match.group(1)
        
        # Check for A/B/C structure
        has_setup_phase = bool(re.search(r'\*\*\s*(?:1|A)\.?\s*(?:Setup|Initialization)', section_8_content, re.IGNORECASE))
        has_loop_phase = bool(re.search(r'\*\*\s*(?:2|B)\.?\s*(?:Loop|Main)', section_8_content, re.IGNORECASE))
        
        # Check for snap instructions
        has_snap = 'snap' in section_8_content.lower()
        
        # Check for category syntax
        has_category_syntax = bool(re.search(r'From \*\*[A-Z]', section_8_content))
        
        project_issues = []
        if not has_setup_phase and not has_loop_phase:
            project_issues.append("Missing A/B/C structure")
        if not has_snap:
            project_issues.append("Missing 'snap' instructions")
        if not has_category_syntax:
            project_issues.append("Missing category syntax (From **Category**)")
        
        if project_issues:
            issues.append(f"Project {project_num}: {', '.join(project_issues)}")
    
    return issues

if __name__ == "__main__":
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    print("=== Auditing Section 8 Compliance ===\n")
    issues = audit_section_8_compliance(file_path)
    
    print(f"Found {len(issues)} projects with issues:\n")
    for issue in issues[:20]:  # Show first 20
        print(f"  - {issue}")
    
    if len(issues) > 20:
        print(f"\n  ... and {len(issues) - 20} more")
    
    print(f"\nTotal projects scanned: ~100")
    print(f"Projects needing fixes: {len(issues)}")
