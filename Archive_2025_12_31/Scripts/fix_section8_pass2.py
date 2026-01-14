"""
Enhanced Fix Script - Second Pass
Specifically targets missing snap instructions and category syntax
"""

import re

def add_comprehensive_snap_instructions(content):
    """Add snap instructions more comprehensively"""
    lines = content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Check if this line needs a snap instruction
        should_add_snap = False
        
        # Pattern 1: "drag" keyword
        if 'drag' in line.lower() and 'snap' not in line.lower():
            should_add_snap = True
        
        # Pattern 2: Action words without snap following
        action_keywords = ['show', 'print', 'wait', 'sleep', 'read', 'change', 'if ', 'repeat', 'set to']
        if any(kw in line.lower() for kw in action_keywords):
            # Check if it's a block instruction (has indentation and *   )
            if line.strip().startswith('*') and len(line) - len(line.lstrip()) >= 4:
                # Check next line
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if 'snap' not in next_line.lower() and not next_line.strip().startswith('*   Inside'):
                        should_add_snap = True
        
        if should_add_snap:
            # Don't add if next line already has snap or is an "Inside" marker
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if 'snap' in next_line.lower() or 'inside' in next_line.lower():
                    should_add_snap = False
        
        if should_add_snap:
            indent = len(line) - len(line.lstrip())
            snap_line = ' ' * indent + '        *   **Snap** it below the previous block.'
            result.append(snap_line)
        
        i += 1
    
    return '\n'.join(result)

def add_category_syntax(content):
    """Add 'From **Category**' syntax to instructions"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        enhanced_line = line
        
        # Skip if already has category syntax
        if 'from **' in line.lower():
            result.append(line)
            continue
        
        # Only enhance bullet points with specific actions
        if not line.strip().startswith('*'):
            result.append(line)
            continue
        
        # Map actions to categories
        mappings = [
            (r'(wait|sleep)\s+[\d.]+\s*s', 'Timing', 'sleep'),
            (r'show.*tm1637', 'Displays', 'TM1637 Show Number'),
            (r'show.*lcd', 'Displays', 'LCD Print'),
            (r'show.*oled', 'Displays', 'OLED Show'),
            (r'print\s+["\']', 'Logic', 'print'),
            (r'change\s+`?\w+`?\s+by', 'Variables', 'change'),
            (r'set\s+`?\w+`?\s+to', 'Variables', 'set'),
            (r'read\s+(?:joystick|analog)', 'Inputs', 'Read Analog'),
            (r'if\s+', 'Logic', 'if'),
            (r'repeat\s+\d+', 'Loops', 'repeat'),
        ]
        
        for pattern, category, block_hint in mappings:
            if re.search(pattern, line, re.IGNORECASE):
                # Extract the action part
                indent = len(line) - len(line.lstrip())
                stripped = line.strip()[len('*   '):]  # Remove *   
                
                # Reconstruct with category
                enhanced_line = ' ' * indent + f'*   From **{category}**, drag `{stripped.rstrip(".")}`.'
                break
        
        result.append(enhanced_line)
    
    return '\n'.join(result)

def fix_project_section8(project_content, project_num):
    """Second pass fix for specific project"""
    
    # Find Section 8
    section_8_match = re.search(r'(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9|$)', project_content, re.DOTALL)
    
    if not section_8_match:
        return project_content
    
    header = section_8_match.group(1)
    section_8_content = section_8_match.group(2)
    
    # Apply enhancements
    enhanced = section_8_content
    
    # Add snap instructions if missing
    if 'snap' not in enhanced.lower() or enhanced.lower().count('snap') < 2:
        enhanced = add_comprehensive_snap_instructions(enhanced)
    
    # Add category syntax if sparse
    if enhanced.lower().count('from **') < 2:
        enhanced = add_category_syntax(enhanced)
    
    # Replace in original
    return project_content.replace(header + section_8_content, header + enhanced)

def fix_specific_projects(file_path, project_nums):
    """Fix specific projects by number"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_content = content
    fixes_made = 0
    
    for proj_num in project_nums:
        # Find the project
        pattern = rf'(## .*?Project 0{proj_num}:.*?)(?=\n## .*?Project \d+:|$)'
        match = re.search(pattern, fixed_content, re.DOTALL)
        
        if match:
            project_text = match.group(1)
            fixed_project = fix_project_section8(project_text, proj_num)
            
            if fixed_project != project_text:
                fixed_content = fixed_content.replace(project_text, fixed_project)
                fixes_made += 1
                print(f"  Enhanced Project {proj_num}")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    return fixes_made

if __name__ == "__main__":
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    # Projects that still have issues
    problem_projects = [105, 106, 110, 113, 114, 115, 117, 123, 126, 129, 
                        136, 153, 156, 157, 158, 160, 163, 166, 169, 187, 193]
    
    print(f"=== Second Pass Fix for {len(problem_projects)} Projects ===\n")
    fixes = fix_specific_projects(file_path, problem_projects)
    
    print(f"\n=== Fix Complete ===")
    print(f"Enhanced {fixes} projects")
    print("Re-run audit to verify")
