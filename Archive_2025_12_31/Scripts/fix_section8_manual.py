"""
Manual targeted fix script for remaining 21 projects
Reads each project's Section 8 and adds missing snap instructions
"""

import re

# Projects with issues and what they need
PROJECTS_TO_FIX = {
    '0105': {'needs_snap': True, 'needs_category': True},
    '0106': {'needs_snap': True, 'needs_category': True},
    '0110': {'needs_snap': True, 'needs_category': True},
    '0113': {'needs_snap': True, 'needs_category': False},
    '0114': {'needs_snap': True, 'needs_category': True},
    '0115': {'needs_snap': True,'needs_category': False},
    '0117': {'needs_snap': True, 'needs_category': False},
    '0123': {'needs_snap': True, 'needs_category': False},
    '0126': {'needs_snap': True, 'needs_category': False},
    '0129': {'needs_snap': True, 'needs_category': False},
    '0136': {'needs_snap': True, 'needs_category': True},
    '0153': {'needs_snap': True, 'needs_category': True},
    '0156': {'needs_snap': True, 'needs_category': True},
    '0157': {'needs_snap': True, 'needs_category': True},
    '0158': {'needs_snap': True, 'needs_category': True},
    '0160': {'needs_snap': True, 'needs_category': True},
    '0163': {'needs_snap': True, 'needs_category': True},
    '0166': {'needs_snap': True, 'needs_category': False},
    '0169': {'needs_snap': True, 'needs_category': False},
    '0187': {'needs_snap': True, 'needs_category': True},
    '0193': {'needs_snap': True, 'needs_category': False},
}

def add_snap_after_each_step(content):
    """Add snap instruction after each instruction line"""
    lines = content.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        result.append(line)
        
        # Check if this is an instruction line (bullet point with action)
        is_instruction = (
            line.strip().startswith('*') and 
            len(line.strip()) > 2 and
            not line.strip().startswith('*   **A.') and
            not line.strip().startswith('*   **B.') and
            not line.strip().startswith('*   **C.') and
            'Inside' not in line
        )
        
        if is_instruction:
            # Check if next line is already a snap instruction
            next_is_snap = False
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if 'snap' in next_line.lower() or 'inside' in next_line.lower():
                    next_is_snap = True
            
            if not next_is_snap:
                # Determine indentation
                indent = len(line) - len(line.lstrip())
                snap_line = ' ' * indent + '        *   **Snap** it below the previous block.'
                result.append(snap_line)
    
    return '\n'.join(result)

def add_category_prefix(line):
    """Add 'From **Category**, drag' to a line if appropriate"""
    if 'from **' in line.lower():
        return line  # Already has it
    
    # Map keywords to categories
    if re.search(r'wait|sleep', line, re.IGNORECASE):
        return re.sub(r'(\s*\*\s+)(Wait|Sleep)', r'\1From **Timing**, drag `sleep', line, flags=re.IGNORECASE)
    elif re.search(r'tm1637.*show', line, re.IGNORECASE):
        return re.sub(r'(\s*\*\s+)(Show|TM1637)', r'\1From **Displays**, drag `TM1637 Show Number', line, flags=re.IGNORECASE)
    elif re.search(r'print', line, re.IGNORECASE):
        return re.sub(r'(\s*\*\s+)(Print)', r'\1From **Logic**, drag `print', line, flags=re.IGNORECASE)
    elif re.search(r'change.*by', line, re.IGNORECASE):
        return re.sub(r'(\s*\*\s+)(Change)', r'\1From **Variables**, drag `change', line, flags=re.IGNORECASE)
    elif re.search(r'set.*to', line, re.IGNORECASE):
        return re.sub(r'(\s*\*\s+)(Set)', r'\1From **Variables**, drag `set', line, flags=re.IGNORECASE)
    
    return line

def fix_project(content, proj_num):
    """Fix a specific project"""
    requirements = PROJECTS_TO_FIX.get(proj_num, {})
    
    # Find Section 8
    pattern = rf'(## .*?Project {proj_num}:.*?### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"  X Could not find Project {proj_num}")
        return content
    
    before_section8 = match.group(1)
    section8_content = match.group(2)
    original = before_section8 + section8_content
    
    fixed_section8 = section8_content
    
    # Add snap instructions if needed
    if requirements.get('needs_snap'):
        fixed_section8 = add_snap_after_each_step(fixed_section8)
    
    # Add category syntax if needed
    if requirements.get('needs_category'):
        lines = fixed_section8.split('\n')
        enhanced_lines = [add_category_prefix(line) for line in lines]
        fixed_section8 = '\n'.join(enhanced_lines)
    
    # Replace
    fixed = before_section8 + fixed_section8
    return content.replace(original, fixed)

def main():
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== Manual Fix for Remaining 21 Projects ===\n")
    
    fixed_content = content
    for proj_num in sorted(PROJECTS_TO_FIX.keys()):
        fixed_content = fix_project(fixed_content, proj_num)
        print(f"  Fixed Project {proj_num}")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"\n=== Complete ===")
    print(f"Fixed {len(PROJECTS_TO_FIX)} projects")

if __name__ == "__main__":
    main()
