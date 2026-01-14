"""
Comprehensive Fix Script for Section 8 (Step-by-Step Guide)
Adds A/B/C structure, snap instructions, and proper category syntax
"""

import re
import sys

def add_snap_instructions(content):
    """Add snap instructions after block drag operations"""
    # Pattern: "drag" followed by block without snap
    lines = content.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        result.append(line)
        # If line contains "drag" and next line doesn't have "Snap"
        if 'drag' in line.lower() and i + 1 < len(lines):
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if 'snap' not in next_line.lower() and not next_line.strip().startswith('*   Inside'):
                indent = len(line) - len(line.lstrip())
                snap_line = ' ' * indent + '        *   **Snap** it below the previous block.'
                result.append(snap_line)
    
    return '\n'.join(result)

def fix_section_8(project_content, project_num):
    """Fix Section 8 for a single project"""
    
    # Find Section 8
    section_8_pattern = r'(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9|$)'
    match = re.search(section_8_pattern, project_content, re.DOTALL)
    
    if not match:
        return project_content
    
    header = match.group(1)
    section_8_content = match.group(2)
    
    # Check if already has proper structure
    if re.search(r'\*\*\s*[AB]\.', section_8_content):
        # Already has A/B structure, just add snap instructions if missing
        if 'snap' not in section_8_content.lower():
            enhanced = add_snap_instructions(section_8_content)
            return project_content.replace(header + section_8_content, header + enhanced)
        return project_content
    
    # Determine what phases are needed
    has_setup = any(keyword in section_8_content.lower() for keyword in ['setup', 'init', 'create variable', 'tm1637', 'servo', 'lcd', 'oled', 'neopixel'])
    has_events = any(keyword in section_8_content.lower() for keyword in ['button', 'if ', 'press', 'event'])
    
    # Build new structure
    new_content = []
    
    # Parse existing structure
    lines = section_8_content.strip().split('\n')
    
    # Group lines by phase markers
    setup_lines = []
    loop_lines = []
    event_lines = []
    current_phase = 'loop'
    
    for line in lines:
        if re.search(r'\*\*\s*1\.?\s*(?:Setup|Initialization)', line, re.IGNORECASE):
            current_phase = 'setup'
        elif re.search(r'\*\*\s*2\.?\s*(?:Loop|Main)', line, re.IGNORECASE):
            current_phase = 'loop'
        elif re.search(r'\*\*\s*3\.?\s*(?:Event|Condition)', line, re.IGNORECASE):
            current_phase = 'event'
        else:
            if current_phase == 'setup':
                setup_lines.append(line)
            elif current_phase == 'event':
                event_lines.append(line)
            else:
                loop_lines.append(line)
    
    # If no explicit phases found, treat all as loop content
    if not setup_lines and not event_lines:
        loop_lines = lines
    
    # Build structured output
    if setup_lines or has_setup:
        new_content.append('*   **A. Initialization Phase**')
        if setup_lines:
            new_content.extend(setup_lines)
        else:
            # Add placeholder based on project type
            if 'tm1637' in project_content.lower():
                new_content.append('    *   From **Displays**, drag `Setup TM1637 CLK:[14] DIO:[15]`.')
                new_content.append('        *   **Snap** into setup block.')
    
    if loop_lines:
        new_content.append('*   **B. Main Loop Phase**')
        # Enhance loop lines with "From **Category**" syntax if missing
        for line in loop_lines:
            if line.strip() and not line.strip().startswith('*'):
                continue
            # Check if needs enhancement
            if 'from **' not in line.lower() and any(word in line.lower() for word in ['show', 'print', 'wait', 'read', 'change']):
                # Try to add category
                enhanced_line = enhance_with_category(line)
                new_content.append(enhanced_line)
            else:
                new_content.append(line)
    
    if event_lines:
        new_content.append('*   **C. Event / Condition Handling**')
        new_content.extend(event_lines)
    
    # Add snap instructions
    final_content = '\n'.join(new_content)
    final_content = add_snap_instructions(final_content)
    
    # Replace in original
    return project_content.replace(header + section_8_content, header + final_content + '\n')

def enhance_with_category(line):
    """Add category syntax to a line if appropriate"""
    # Simple heuristics
    if 'wait' in line.lower() or 'sleep' in line.lower():
        if 'from **' not in line.lower():
            # Replace pattern
            line = re.sub(r'(\s*)(?:Wait|sleep)', r'\1From **Timing**, drag `sleep', line, flags=re.IGNORECASE)
            if '`' not in line:
                line = line.rstrip('.') + '`.'
    elif 'show' in line.lower() and 'tm1637' in line.lower():
        if 'from **' not in line.lower():
            line = re.sub(r'(\s*)Show', r'\1From **Displays**, drag `TM1637 Show Number', line, flags=re.IGNORECASE)
    elif 'change' in line.lower() and 'by' in line.lower():
        if 'from **' not in line.lower():
            line = re.sub(r'(\s*)Change', r'\1From **Variables**, drag `change', line, flags=re.IGNORECASE)
    
    return line

def fix_all_projects(file_path):
    """Fix all projects in the documentation file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by project headers
    project_pattern = r'(## .*?Project (\d+):.*?)(?=\n## .*?Project \d+:|$)'
    projects = list(re.finditer(project_pattern, content, re.DOTALL))
    
    print(f"Found {len(projects)} projects to process")
    
    fixed_content = content
    fixes_made = 0
    
    for match in projects:
        project_text = match.group(1)
        project_num = match.group(2)
        
        # Only fix if Section 8 has issues
        if '### 8' in project_text and 'Step-by-Step' in project_text:
            fixed_project = fix_section_8(project_text, project_num)
            if fixed_project != project_text:
                fixed_content = fixed_content.replace(project_text, fixed_project)
                fixes_made += 1
                print(f"  Fixed Project {project_num}")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"\n=== Fix Complete ===")
    print(f"Total fixes applied: {fixes_made}")
    return fixes_made

if __name__ == "__main__":
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    print("=== Starting Section 8 Fix Process ===\n")
    fixes = fix_all_projects(file_path)
    
    print(f"\nFixed {fixes} projects")
    print("Re-run audit_section8.py to verify")
