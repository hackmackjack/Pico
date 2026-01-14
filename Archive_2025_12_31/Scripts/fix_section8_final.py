"""
Final fix for last 8 projects
More aggressive category syntax injection
"""

import re

FINAL_PROJECTS = ['0106', '0110', '0114', '0157', '0160', '0163', '0187', '0188']

def aggressively_add_categories(content):
    """Add category syntax to every applicable line"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # Skip headers and already-categorized lines
        if line.strip().startswith('**') or 'from **' in line.lower():
            result.append(line)
            continue
        
        # Only process bullet points
        if not line.strip().startswith('*'):
            result.append(line)
            continue
        
        modified = line
        indent = ' ' * (len(line) - len(line.lstrip()))
        stripped = line.strip()[len('*   '):]  # Remove bullet
        
        # Aggressive pattern matching
        categories_map = [
            (r'(?:wait|sleep|delay)\s*[\d.]+', 'Timing', 'sleep'),
            (r'(?:show|display).*(?:number|value)', 'Displays', 'Show Number'),
            (r'print.*["\']', 'Logic', 'print'),
            (r'change\s+.*?\s+by', 'Variables', 'change variable'),
            (r'set\s+.*?\s+to', 'Variables', 'set variable'),
            (r'if\s+', 'Logic', 'if block'),
            (r'repeat\s+\d+', 'Loops', 'repeat block'),
            (r'measure|read\s+(?:dht|temp|sensor)', 'Inputs', 'read sensor'),
            (r'lcd.*(?:print|show|move)', 'Displays', 'LCD block'),
            (r'clear.*(?:lcd|display)', 'Displays', 'clear'),
        ]
        
        for pattern, category, block_name in categories_map:
            match_obj = re.search(pattern, stripped, re.IGNORECASE)
            if match_obj:
                modified = indent + f'*   From **{category}**, drag `{block_name}`.'
                break
        
        result.append(modified)
    
    return '\n'.join(result)

def final_fix_project(content, proj_num):
    """Final targeted fix"""
    # Find Section 8
    pattern = rf'(## .*?Project {proj_num}:.*?### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"  X Could not find Project{proj_num}")
        return content
    
    before = match.group(1)
    section8 = match.group(2)
    
    #Add categories
    fixed = aggressively_add_categories(section8)
    
    # Add snaps if needed for 0188
    if proj_num == '0188' and 'snap' not in fixed.lower():
        lines = fixed.split('\n')
        snap_added = []
        for i, line in enumerate(lines):
            snap_added.append(line)
            if line.strip().startswith('*') and 'drag' in line.lower():
                if i + 1 < len(lines) and 'snap' not in lines[i+1].lower():
                    indent = len(line) - len(line.lstrip())
                    snap_added.append(' ' * indent + '        *   **Snap** it below the previous block.')
        fixed = '\n'.join(snap_added)
    
    return content.replace(before + section8, before + fixed)

def main():
    file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== Final Fix for Last 8 Projects ===\n")
    
    fixed_content = content
    for proj_num in FINAL_PROJECTS:
        fixed_content = final_fix_project(fixed_content, proj_num)
        print(f"  Fixed Project {proj_num}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("\n=== Complete ===")

if __name__ == "__main__":
    main()
