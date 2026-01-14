import re

def audit_final(filepath):
    """Final audit of fixed files."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    projects = re.findall(r'## 1️⃣ Project (\d+):(.*?)(?=## 1️⃣ Project \d+:|$)', content, re.DOTALL)
    
    issues = []
    compliant = []
    
    for proj_num, proj_content in projects:
        guide_match = re.search(r'### 8️⃣ Step-by-Step Guide\s*(.*?)(?=###|$)', proj_content, re.DOTALL)
        
        if not guide_match:
            issues.append(f"P{proj_num}: Missing guide section")
            continue
        
        guide = guide_match.group(1)
        
        has_from = 'From **' in guide
        has_drag = 'drag' in guide.lower()
        has_snap = '**Snap**' in guide or '**snap**' in guide.lower()
        
        if has_from and has_drag and has_snap:
            compliant.append(proj_num)
        elif not has_from and not has_drag:
            issues.append(f"P{proj_num}: Abstract (no From/drag)")
        elif has_drag and not has_snap:
            issues.append(f"P{proj_num}: Missing Snap")
        else:
            issues.append(f"P{proj_num}: Other issue")
    
    return compliant, issues

print("=" * 60)
print("FINAL AUDIT - COMPREHENSIVE FIX")
print("=" * 60)

comp1, iss1 = audit_final('d:/MFF/Pico/Documentation/Docs_0001_0100_FINAL.md')
comp2, iss2 = audit_final('d:/MFF/Pico/Documentation/Docs_0101_0200_FINAL.md')

total_compliant = len(comp1) + len(comp2)
total_issues = len(iss1) + len(iss2)

print(f"\n Projects 1-100:")
print(f"  Compliant: {len(comp1)}/100")
print(f"  Issues: {len(iss1)}")

print(f"\nProjects 101-200:")
print(f"  Compliant: {len(comp2)}/100")
print(f"  Issues: {len(iss2)}")

print(f"\n" + "=" * 60)
print(f"TOTAL COMPLIANCE: {total_compliant}/200 ({total_compliant/2:.1f}%)")
print("=" * 60)

if total_issues > 0:
    print(f"\nRemaining issues: {total_issues}")
    if iss1:
        print("\nP001-P100 issues:")
        for issue in iss1[:20]:
            print(f"  {issue}")
        if len(iss1) > 20:
            print(f"  ... and {len(iss1)-20} more")
    
    if iss2:
        print("\nP101-P200 issues:")
        for issue in iss2[:20]:
            print(f"  {issue}")
        if len(iss2) > 20:
            print(f"  ... and {len(iss2)-20} more")
else:
    print("\n[SUCCESS] ALL 200 PROJECTS ARE NOW COMPLIANT!")
