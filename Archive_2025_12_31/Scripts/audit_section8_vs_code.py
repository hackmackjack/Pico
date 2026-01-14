"""
Section 8/10 Mismatch Audit Script
Detects projects where Step-by-Step Guide doesn't align with Generated Code
"""

import re

def extract_code_features(code_block):
    """Extract key features from Generated Code"""
    features = {
        'variables': set(),
        'has_for_loop': False,
        'has_while_loop': False,
        'has_if': False,
        'functions_called': set(),
        'imports': set(),
        'constants': set()
    }
    
    # Extract variable assignments
    var_pattern = r'(\w+)\s*='
    features['variables'] = set(re.findall(var_pattern, code_block))
    
    # Check for loops
    features['has_for_loop'] = 'for ' in code_block
    features['has_while_loop'] = 'while ' in code_block
    features['has_if'] = 'if ' in code_block
    
    # Extract function calls
    func_pattern = r'(\w+)\('
    features['functions_called'] = set(re.findall(func_pattern, code_block))
    
    # Extract imports
    import_pattern = r'import\s+(\w+)'
    features['imports'] = set(re.findall(import_pattern, code_block))
    
    # Extract constants (ALL_CAPS variables)
    const_pattern = r'([A-Z_]{2,})\s*='
    features['constants'] = set(re.findall(const_pattern, code_block))
    
    return features

def check_section8_issues(section8_text):
    """Check for red flags in Section 8"""
    issues = []
    
    # Check for placeholders
    if '[Category]' in section8_text or '[category]' in section8_text:
        issues.append("Contains placeholder [Category]")
    
    if 'appropriate' in section8_text.lower():
        issues.append("Vague: 'appropriate block'")
    
    if 'as needed' in section8_text.lower():
        issues.append("Vague: 'as needed'")
    
    # Check for old numbering
    if re.search(r'\*\*\s*[1-9]\.', section8_text) and not re.search(r'\*\*\s*[AB]\.', section8_text):
        issues.append("Uses numbered (1/2/3) instead of A/B structure")
    
    # Check for missing category syntax
    if 'From **' not in section8_text:
        issues.append("Missing 'From **Category**' syntax entirely")
    
    return issues

def validate_alignment(section8_text, code_features):
    """Check if Section 8 mentions key features from code"""
    mismatches = []
    
    # Check if code variables are mentioned
    for var in code_features['variables']:
        # Skip common system variables
        if var in ['machine', 'time', 'i', 'j', 'self']:
            continue
        if var not in section8_text:
            mismatches.append(f"Code defines variable '{var}' but Section 8 doesn't mention it")
    
    # Check if code constants are mentioned
    for const in code_features['constants']:
        if const not in section8_text:
            mismatches.append(f"Code defines constant '{const}' but Section 8 doesn't mention it")
    
    # Check loop alignment
    if code_features['has_for_loop'] and 'repeat' not in section8_text.lower() and 'count' not in section8_text.lower():
        mismatches.append("Code has 'for' loop but Section 8 doesn't mention repeat/count")
    
    if code_features['has_if'] and 'if' not in section8_text.lower():
        mismatches.append("Code has 'if' statement but Section 8 doesn't mention it")
    
    return mismatches

def audit_project(project_text, project_num):
    """Audit a single project for Section 8/10 alignment"""
    
    # Extract Section 8
    section8_match = re.search(r'### 8.*?Step-by-Step Guide\s*\n(.*?)(?=\n### 9)', project_text, re.DOTALL)
    if not section8_match:
        return {"project": project_num, "error": "No Section 8 found"}
    
    section8_text = section8_match.group(1)
    
    # Extract Section 10 (Generated Code)
    code_match = re.search(r'### .*?Generated Code.*?\n```python\s*\n(.*?)```', project_text, re.DOTALL)
    if not code_match:
        return {"project": project_num, "error": "No Generated Code found"}
    
    code_block = code_match.group(1)
    
    # Analyze
    section8_issues = check_section8_issues(section8_text)
    code_features = extract_code_features(code_block)
    alignment_issues = validate_alignment(section8_text, code_features)
    
    all_issues = section8_issues + alignment_issues
    
    if all_issues:
        return {
            "project": project_num,
            "issue_count": len(all_issues),
            "issues": all_issues,
            "section8_snippet": section8_text[:100] + "...",
            "code_snippet": code_block[:100] + "..."
        }
    
    return None

def audit_file(file_path):
    """Audit all projects in a file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all projects
    projects = re.finditer(r'(## .*?Project (\d+):.*?)(?=\n## .*?Project \d+:|$)', content, re.DOTALL)
    
    issues = []
    for match in projects:
        project_text = match.group(1)
        project_num = match.group(2)
        
        result = audit_project(project_text, project_num)
        if result and 'issues' in result:
            issues.append(result)
    
    return issues

if __name__ == "__main__":
    files = [
        (r"d:\MFF\Pico\Documentation\Docs_0001_0100.md", "0001-0100"),
        (r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md", "0101-0200")
    ]
    
    print("=== Section 8/10 Mismatch Audit ===\n")
    
    all_issues = []
    for file_path, proj_range in files:
        print(f"Auditing {proj_range}...")
        issues = audit_file(file_path)
        all_issues.extend(issues)
        print(f"  Found {len(issues)} projects with mismatches")
    
    print(f"\n=== Results ===")
    print(f"Total projects with issues: {len(all_issues)}\n")
    
    # Show top 10 worst offenders
    sorted_issues = sorted(all_issues, key=lambda x: x['issue_count'], reverse=True)
    
    print("Top 10 worst mismatches:")
    for i, issue in enumerate(sorted_issues[:10], 1):
        print(f"\n{i}. Project {issue['project']} ({issue['issue_count']} issues):")
        for j, iss in enumerate(issue['issues'][:3], 1):
            print(f"   - {iss}")
        if len(issue['issues']) > 3:
            print(f"   ... and {len(issue['issues']) - 3} more")
    
    # Save full report
    with open('section8_10_mismatch_report.txt', 'w') as f:
        f.write(f"Section 8/10 Mismatch Audit Report\n")
        f.write(f"Total projects with issues: {len(all_issues)}\n\n")
        for issue in sorted_issues:
            f.write(f"\nProject {issue['project']} ({issue['issue_count']} issues):\n")
            for iss in issue['issues']:
                f.write(f"  - {iss}\n")
    
    print("\nFull report saved to: section8_10_mismatch_report.txt")
