"""
Hardware Section Sync Script
Extracts hardware from Problem Statements and syncs to Solution Section 4
"""

import re

def extract_problem_hardware(problem_file, project_num):
    """Extract hardware list from problem statement"""
    
    with open(problem_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the specific project
    pattern = f'### Project {project_num}:.*?\n(.*?)(?=\n### Project|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    project_text = match.group(1)
    
    # Extract hardware requirements section
    hw_match = re.search(r'\*\*Hardware Requirements:\*\*\s*\n(.*?)(?=\n\n\*\*Expected|$)', project_text, re.DOTALL)
    
    if not hw_match:
        return None
    
    hw_text = hw_match.group(1).strip()
    hw_lines = [line.strip('* \t') for line in hw_text.split('\n') if line.strip()]
    
    return hw_lines

def update_solution_hardware(solution_file, project_num, hardware_list):
    """Update Section 4 in solution file with hardware from problem"""
    
    with open(solution_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the project
    pattern = f'(## .*?Project {project_num}:.*?)(### 4.*?Hardware Required.*?\n)(.*?)((?=\n###))'
    
    def replace_hardware(match):
        header = match.group(1)
        section_header = match.group(2)
        old_hardware = match.group(3)
        next_section = match.group(4)
        
        # Build new hardware section
        new_hardware = ""
        for hw in hardware_list:
            # Clean and format
            hw_clean = hw.strip()
            # Extract main component name
            if ':' in hw_clean:
                hw_clean = hw_clean.split(':')[0].strip()
            
            # Check if it's already formatted with **
            if hw_clean.startswith('**'):
                new_hardware += f"*   {hw_clean}\n"
            else:
                new_hardware += f"*   **{hw_clean}**\n"
        
        new_hardware += "\n"
        
        return header + section_header + new_hardware + next_section
    
    new_content = re.sub(pattern, replace_hardware, content, flags=re.DOTALL)
    
    with open(solution_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return new_content != content

def sync_hardware_for_range(problem_file, solution_file, start_proj, end_proj):
    """Sync hardware for a range of projects"""
    
    updated_count = 0
    
    for proj_num in range(start_proj, end_proj + 1):
        proj_str = f"{proj_num:04d}"
        
        # Extract hardware from problem
        hardware = extract_problem_hardware(problem_file, proj_str)
        
        if not hardware:
            print(f"  Project {proj_str}: No hardware found in problem")
            continue
        
        # Update solution
        updated = update_solution_hardware(solution_file, proj_str, hardware)
        
        if updated:
            updated_count += 1
            print(f"  Project {proj_str}: Updated ({len(hardware)} items)")
        else:
            print(f"  Project {proj_str}: No changes needed")
    
    return updated_count

if __name__ == "__main__":
    print("=== Hardware Section Sync ===\n")
    
    # Priority 1: Projects 0101-0200
    print("Syncing Projects 0101-0200...")
    count1 = sync_hardware_for_range(
        r"d:\MFF\Pico\Problem_Statements\Projects_0101_0200.md",
        r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md",
        101, 200
    )
    print(f"  Updated {count1} projects\n")
    
    # Priority 2: Projects 0001-0100  
    print("Syncing Projects 0001-0100...")
    count2 = sync_hardware_for_range(
        r"d:\MFF\Pico\Problem_Statements\Projects_0001_0100.md",
        r"d:\MFF\Pico\Documentation\Docs_0001_0100.md",
        1, 100
    )
    print(f"  Updated {count2} projects\n")
    
    print(f"\n=== Complete ===")
    print(f"Total projects updated: {count1 + count2}")
    print("Re-run audit_problem_solution_cross.py to verify")
