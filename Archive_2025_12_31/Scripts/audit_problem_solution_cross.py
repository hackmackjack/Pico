"""
Cross-Validation Audit: Problem Statements vs Solutions
Checks if Problem files match Solution files across all 12 sections
"""

import re

def extract_problem_data(problem_text, project_num):
    """Extract problem statement details"""
    data = {
        'project': project_num,
        'category': None,
        'difficulty': None,
        'problem_statement': None,
        'hardware': [],
        'expected_behavior': []
    }
    
    # Extract category
    cat_match = re.search(r'\*\*Category:\*\*\s+(.+)', problem_text)
    if cat_match:
        data['category'] = cat_match.group(1).strip()
    
    # Extract difficulty
    diff_match = re.search(r'\*\*Difficulty:\*\*\s+(\d+)', problem_text)
    if diff_match:
        data['difficulty'] = int(diff_match.group(1))
    
    # Extract problem statement
    prob_match = re.search(r'\*\*Problem Statement:\*\*\s*\n(.+?)(?=\n\n|\*\*Hardware)', problem_text, re.DOTALL)
    if prob_match:
        data['problem_statement'] = prob_match.group(1).strip()
    
    # Extract hardware requirements
    hw_section = re.search(r'\*\*Hardware Requirements:\*\*\s*\n(.*?)(?=\n\n\*\*Expected|$)', problem_text, re.DOTALL)
    if hw_section:
        hw_lines = hw_section.group(1).strip().split('\n')
        data['hardware'] = [line.strip('* \t') for line in hw_lines if line.strip()]
    
    # Extract expected behavior
    exp_section = re.search(r'\*\*Expected Behavior:\*\*\s*\n(.*?)$', problem_text, re.DOTALL)
    if exp_section:
        exp_lines = exp_section.group(1).strip().split('\n')
        data['expected_behavior'] = [line.strip('* \t') for line in exp_lines if line.strip()]
    
    return data

def extract_solution_data(solution_text, project_num):
    """Extract documentation sections"""
    data = {
        'project': project_num,
        '2_learning_objective': None,
        '3_concepts': [],
        '4_hardware': [],
        '5_wiring': None,
        '6_blocks': [],
        '7_variables': [],
        '8_step_by_step': None,
        '9_execution_flow': None,
        '10_code': None,
        '11_debug_tips': [],
        '12_try_next': []
    }
    
    # Section 2: Learning Objective
    sec2 = re.search(r'### 2.*?Learning Objective.*?\n(.*?)(?=\n###)', solution_text, re.DOTALL)
    if sec2:
        data['2_learning_objective'] = sec2.group(1).strip()[:200]  # First 200 chars
    
    # Section 3: Concepts
    sec3 = re.search(r'### 3.*?Concepts.*?\n(.*?)(?=\n###)', solution_text, re.DOTALL)
    if sec3:
        concepts = re.findall(r'\*\*([^*]+)\*\*:', sec3.group(1))
        data['3_concepts'] = concepts
    
    # Section 4: Hardware
    sec4 = re.search(r'### 4.*?Hardware.*?\n(.*?)(?=\n###)', solution_text, re.DOTALL)
    if sec4:
        hw_items = re.findall(r'\*\*([^*]+)\*\*', sec4.group(1))
        data['4_hardware'] = hw_items
    
    # Section 8: Check if exists
    sec8 = re.search(r'### 8.*?Step-by-Step', solution_text)
    data['8_step_by_step'] = 'Present' if sec8 else 'Missing'
    
    # Section 10: Check if code exists
    sec10 = re.search(r'### .*?Generated Code.*?\n```', solution_text, re.DOTALL)
    data['10_code'] = 'Present' if sec10 else 'Missing'
    
    return data

def cross_validate_project(problem_data, solution_data):
    """Compare problem vs solution and find mismatches"""
    issues = []
    
    # Check if hardware matches
    prob_hw = set([hw.lower() for hw in problem_data['hardware']])
    sol_hw = set([hw.lower() for hw in solution_data['4_hardware']])
    
    # Look for major hardware discrepancies
    for hw in prob_hw:
        # Check if this hardware is mentioned in solution
        found = any(ph_item in hw or hw in ph_item for ph_item in sol_hw)
        if not found and 'pico' not in hw.lower():
            issues.append(f"Problem requires '{hw}' but not found in Solution hardware list")
    
    # Check if Section 8 exists
    if solution_data['8_step_by_step'] == 'Missing':
        issues.append("Solution missing Section 8 (Step-by-Step Guide)")
    
    # Check if Section 10 exists
    if solution_data['10_code'] == 'Missing':
        issues.append("Solution missing Section 10 (Generated Code)")
    
    # Check if learning objective relates to problem
    if solution_data['2_learning_objective']:
        prob_keywords = set(problem_data['problem_statement'].lower().split())
        learn_keywords = set(solution_data['2_learning_objective'].lower().split())
        common = prob_keywords & learn_keywords
        if len(common) < 3:  # Very few common words
            issues.append("Learning Objective may not align with Problem Statement (< 3 common words)")
    
    return issues

def audit_projects(problem_file, solution_file):
    """Main audit function"""
    
    # Read files
    with open(problem_file, 'r', encoding='utf-8') as f:
        problem_content = f.read()
    
    with open(solution_file, 'r', encoding='utf-8') as f:
        solution_content = f.read()
    
    # Find all projects in problem file
    problem_projects = re.finditer(
        r'### Project (\d+):.*?\n(.*?)(?=\n### Project|\Z)',
        problem_content,
        re.DOTALL
    )
    
    problems = {}
    for match in problem_projects:
        proj_num = match.group(1)
        proj_text = match.group(2)
        problems[proj_num] = extract_problem_data(proj_text, proj_num)
    
    # Find all projects in solution file
    solution_projects = re.finditer(
        r'## .*?Project (\d+):.*?\n(.*?)(?=\n## .*?Project|\Z)',
        solution_content,
        re.DOTALL
    )
    
    solutions = {}
    for match in solution_projects:
        proj_num = match.group(1)
        proj_text = match.group(2)
        solutions[proj_num] = extract_solution_data(proj_text, proj_num)
    
    # Cross-validate
    all_issues = []
    
    for proj_num in problems:
        if proj_num not in solutions:
            all_issues.append({
                'project': proj_num,
                'issues': [f"Problem exists but no matching Solution found"]
            })
            continue
        
        issues = cross_validate_project(problems[proj_num], solutions[proj_num])
        if issues:
            all_issues.append({
                'project': proj_num,
                'issues': issues,
                'problem_data': problems[proj_num],
                'solution_data': solutions[proj_num]
            })
    
    # Check for solutions without problems
    for proj_num in solutions:
        if proj_num not in problems:
            all_issues.append({
                'project': proj_num,
                'issues': [f"Solution exists but no matching Problem found"]
            })
    
    return all_issues

if __name__ == "__main__":
    file_pairs = [
        (r"d:\MFF\Pico\Problem_Statements\Projects_0001_0100.md",
         r"d:\MFF\Pico\Documentation\Docs_0001_0100.md",
         "0001-0100"),
        (r"d:\MFF\Pico\Problem_Statements\Projects_0101_0200.md",
         r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md",
         "0101-0200")
    ]
    
    print("=== Problem-Solution Cross-Validation Audit ===\n")
    
    all_results = []
    for prob_file, sol_file, range_name in file_pairs:
        print(f"Auditing {range_name}...")
        issues = audit_projects(prob_file, sol_file)
        all_results.extend(issues)
        print(f"  Found {len(issues)} projects with mismatches")
    
    print(f"\n=== Results ===")
    print(f"Total projects with issues: {len(all_results)}\n")
    
    # Show first 15
    print("Projects with mismatches:")
    for i, result in enumerate(all_results[:15], 1):
        print(f"\n{i}. Project {result['project']} ({len(result['issues'])} issues):")
        for issue in result['issues']:
            print(f"   - {issue}")
    
    if len(all_results) > 15:
        print(f"\n... and {len(all_results) - 15} more projects")
    
    # Save full report
    with open('problem_solution_cross_validation.txt', 'w', encoding='utf-8') as f:
        f.write("Problem-Solution Cross-Validation Report\n")
        f.write(f"Total projects with issues: {len(all_results)}\n\n")
        for result in all_results:
            f.write(f"\nProject {result['project']} ({len(result['issues'])} issues):\n")
            for issue in result['issues']:
                f.write(f"  - {issue}\n")
    
    print("\nFull report saved to: problem_solution_cross_validation.txt")
