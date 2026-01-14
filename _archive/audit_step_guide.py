import re

def audit_step_by_step_guides(filepath):
    """Audit Step-by-Step Guide sections for ultra-explicit format."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all projects
    projects = re.findall(r'## 1️⃣ Project (\d+):(.*?)(?=## 1️⃣ Project \d+:|$)', content, re.DOTALL)
    
    issues = []
    
    for proj_num, proj_content in projects:
        # Extract Step-by-Step Guide section
        guide_match = re.search(r'### 8️⃣ Step-by-Step Guide\s*(.*?)(?=###|$)', proj_content, re.DOTALL)
        
        if not guide_match:
            issues.append(f"P{proj_num}: Missing Step-by-Step Guide section")
            continue
        
        guide_text = guide_match.group(1)
        
        # Check for ultra-explicit indicators
        has_drag = 'drag' in guide_text.lower()
        has_from = 'From **' in guide_text
        has_snap = 'snap' in guide_text.lower() or 'Snap' in guide_text
        
        # Check for bad patterns (abstract logic)
        bad_patterns = [
            r'`\w+` = ',  # Assignment notation like `dist` = 
            r'\w+ = Read',  # Direct assignment
        ]
        
        has_bad_pattern = any(re.search(pattern, guide_text) for pattern in bad_patterns)
        
        # Quality scoring
        if not has_from and not has_drag:
            issues.append(f"P{proj_num}: Missing 'From' and 'drag' instructions (ABSTRACT)")
        elif not has_snap and has_drag:
            issues.append(f"P{proj_num}: Has 'drag' but missing 'Snap' instructions (INCOMPLETE)")
        elif has_bad_pattern:
            issues.append(f"P{proj_num}: Contains abstract assignment notation (NEEDS REWRITE)")
    
    return issues

# Audit both files
print("=== AUDITING DOCS_0001_0100.md ===")
issues_1_100 = audit_step_by_step_guides('d:/MFF/Pico/Documentation/Docs_0001_0100.md')
for issue in issues_1_100:
    print(issue)

print(f"\nTotal issues (P1-P100): {len(issues_1_100)}")

print("\n=== AUDITING DOCS_0101_0200.md ===")
issues_101_200 = audit_step_by_step_guides('d:/MFF/Pico/Documentation/Docs_0101_0200.md')
for issue in issues_101_200:
    print(issue)

print(f"\nTotal issues (P101-P200): {len(issues_101_200)}")

print(f"\n=== SUMMARY ===")
print(f"Total projects audited: 200")
print(f"Projects with issues: {len(issues_1_100) + len(issues_101_200)}")
print(f"Compliance rate: {((200 - len(issues_1_100) - len(issues_101_200)) / 200 * 100):.1f}%")
