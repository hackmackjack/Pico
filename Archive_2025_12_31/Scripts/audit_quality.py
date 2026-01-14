"""
Comprehensive Audit for Documentation Quality Issues:
1. Missing closing backticks
2. Missing "From **Category**" syntax
3. Misplaced snap instructions
4. Inconsistent drag syntax
"""

import re

def audit_quality_issues(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = {}
    
    # Find all Section 8 blocks
    projects = re.finditer(r'## .*?Project (\d+):.*?(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)', content, re.DOTALL)
    
    for match in projects:
        proj_num = match.group(1)
        section8 = match.group(3)
        proj_issues = []
        
        # Check for missing back ticks on drag/sleep lines
        lines = section8.split('\n')
        for i, line in enumerate(lines):
            # Look for drag statements
            if 'drag `' in line.lower():
                # Count backticks
                backtick_count = line.count('`')
                if backtick_count % 2 != 0:
                    proj_issues.append(f"Line {i}: Unclosed backtick")
            
            # Look for instructions without "From **"
            if ('show ' in line.lower() or 'print ' in line.lower() or 
                'wait' in line.lower() or 'sleep' in line.lower() or
                'change ' in line.lower() or 'read ' in line.lower()):
                if line.strip().startswith('*') and 'from **' not in line.lower():
                    # Could be missing category
                    if '`' in line or 'LCD' in line or 'TM1637' in line:
                        proj_issues.append(f"Line {i}: Likely missing 'From **Category**'")
        
        # Check for "Drag" without "From"
        if re.search(r'drag.*`[^`]+`(?!\.)', section8, re.IGNORECASE):
            proj_issues.append("Missing closing backtick after drag")
        
        if re.search(r'^\s*\*\s+Drag\s+', section8, re.MULTILINE):
            proj_issues.append("Uses 'Drag' without 'From **Category**'")
        
        if proj_issues:
            issues[proj_num] = proj_issues
    
    return issues

if __name__ == "__main__":
    file1 = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    file2 = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
    
    print("=== Auditing Documentation Quality Issues ===\n")
    
    for file_path, file_name in [(file1, "Docs_0101_0200"), (file2, "Docs_0001_0100")]:
        try:
            print(f"\n{file_name}:")
            issues = audit_quality_issues(file_path)
            
            if issues:
                print(f"  Found issues in {len(issues)} projects")
                for proj, proj_issues in list(issues.items())[:10]:
                    print(f"    Project {proj}: {len(proj_issues)} issues")
            else:
                print(f"  No issues found")
        except FileNotFoundError:
            print(f"  File not found")
    
    print("\n=== Summary ===")
    print("Check complete")
