"""
Audit for mixed phase numbering in Section 8
Find projects using A, B, 3, 4 instead of A, B, C
"""

import re

def find_mixed_phase_numbering(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Find all Section 8 blocks
    projects = re.finditer(r'## .*?Project (\d+):.*?(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)', content, re.DOTALL)
    
    for match in projects:
        proj_num = match.group(1)
        section8 = match.group(3)
        
        # Check for mixed numbering pattern
        has_ab = bool(re.search(r'\*\*\s*[AB]\.', section8))
        has_numbers = bool(re.search(r'\*\*\s*[3-9]\.', section8))
        
        if has_ab and has_numbers:
            issues.append(proj_num)
    
    return issues

if __name__ == "__main__":
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    print("=== Auditing for Mixed Phase Numbering ===\n")
    issues = find_mixed_phase_numbering(file_path)
    
    print(f"Found {len(issues)} projects with mixed A/B/3/4 numbering:\n")
    for proj in issues:
        print(f"  - Project {proj}")
    
    print(f"\nTotal issues: {len(issues)}")
