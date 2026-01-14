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
        
        # Quality scoring
        if not has_from and not has_drag:
            issues.append(f"P{proj_num}: Missing 'From' and 'drag' instructions (ABSTRACT)")
        elif has_drag and not has_snap:
            issues.append(f"P{proj_num}: Has 'drag' but missing 'Snap' instructions (INCOMPLETE)")
    
    return issues

# Audit AUTOFIXED files
print("=== AUDITING AUTOFIXED FILES ===\n")

print("Checking Docs_0001_0100_AUTOFIXED.md...")
issues_1_100 = audit_step_by_step_guides('d:/MFF/Pico/Documentation/Docs_0001_0100_AUTOFIXED.md')

print("Checking Docs_0101_0200_AUTOFIXED.md...")
issues_101_200 = audit_step_by_step_guides('d:/MFF/Pico/Documentation/Docs_0101_0200_AUTOFIXED.md')

print("\n" + "=" * 60)
print("AUDIT RESULTS")
print("=" * 60)
print(f"Projects 1-100: {len(issues_1_100)} issues")
print(f"Projects 101-200: {len(issues_101_200)} issues")
print(f"\nTotal issues: {len(issues_1_100) + len(issues_101_200)}/200")
print(f"Compliance rate: {((200 - len(issues_1_100) - len(issues_101_200)) / 200 * 100):.1f}%")

if issues_1_100:
    print("\n--- Issues in P001-P100 ---")
    for issue in issues_1_100[:10]:  # Show first  10
        print(issue)
    if len(issues_1_100) > 10:
        print(f"... and {len(issues_1_100) - 10} more")

if issues_101_200:
    print("\n--- Issues in P101-P200 ---")
    for issue in issues_101_200[:10]:  # Show first 10
        print(issue)
    if len(issues_101_200) > 10:
        print(f"... and {len(issues_101_200) - 10} more")
