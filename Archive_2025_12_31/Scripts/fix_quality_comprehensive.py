"""
Comprehensive Quality Fix Script
Fixes: backticks, category syntax, snap placement across all projects
"""

import re
import sys

def fix_backticks(line):
    """Add closing backticks to incomplete code references"""
    # Pattern: drag `something without closing backtick followed by period or newline
    if 'drag `' in line and line.count('`') % 2 != 0:
        # Add closing backtick before period or at end
        if line.rstrip().endswith('.'):
            line = line.rstrip()[:-1] + '`.'
        else:
            line = line.rstrip() + '`'
    
    # Pattern: sleep `0.2s without closing
    if re.search(r'`sleep\s+[\d.]+s(?!`)', line):
        line = re.sub(r'`(sleep\s+[\d.]+)s(?!`)', r'`\1 seconds`', line)
    
    return line

def add_category_syntax(line, indent_level):
    """Add 'From **Category**' to lines missing it"""
    
    # Skip if already has category or is a header/snap line
    if 'from **' in line.lower() or line.strip().startswith('**') or 'snap' in line.lower():
        return line
    
    # Skip if not a bullet point
    if not line.strip().startswith('*'):
        return line
    
    indent = ' ' * indent_level
    stripped = line.strip()[len('*   '):]
    
    # Mapping: instruction patterns to categories
    category_map = [
        (r'^(?:Show|Display).*(?:Char|Number|Text|LCD|TM1637|OLED)', 'Displays'),
        (r'^LCD\s+', 'Displays'),
        (r'^TM1637\s+', 'Displays'),
        (r'^OLED\s+', 'Displays'),
        (r'^Print\s+["\']', 'Logic'),
        (r'^(?:Wait|Sleep)\s+[\d.]+', 'Timing'),
        (r'^Change\s+', 'Variables'),
        (r'^Set\s+.*?\s+to', 'Variables'),
        (r'^Read\s+(?:Analog|Button|Sensor)', 'Inputs'),
        (r'^IF\s+', 'Logic'),
        (r'^Repeat\s+', 'Loops'),
        (r'^Clear\s+', 'Displays'),
    ]
    
    for pattern, category in category_map:
        if re.search(pattern, stripped, re.IGNORECASE):
            return indent + f'*   From **{category}**, drag `{stripped.rstrip(".")}`.\n'
    
    return line

def fix_drag_syntax(line):
    """Fix 'Drag another' to 'From **Category**, drag'"""
    if re.search(r'Drag\s+(?:another|a)\s+`', line, re.IGNORECASE):
        # Try to infer category from block name
        if 'Custom Char' in line or 'LCD' in line or 'Display' in line:
            line = re.sub(r'Drag\s+(?:another|a)\s+', 'From **Displays**, drag ', line, flags=re.IGNORECASE)
        elif 'Variable' in line:
            line = re.sub(r'Drag\s+(?:another|a)\s+', 'From **Variables**, drag ', line, flags=re.IGNORECASE)
        else:
            line = re.sub(r'Drag\s+(?:another|a)\s+', 'Drag ', line, flags=re.IGNORECASE)
    
    return line

def fix_section8(section8_content):
    """Apply all fixes to a Section 8"""
    lines = section8_content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Determine indentation level
        indent_level = len(line) - len(line.lstrip())
        
        # Apply fixes
        fixed = line
        fixed = fix_backticks(fixed)
        fixed = fix_drag_syntax(fixed)
        fixed = add_category_syntax(fixed, indent_level)
        
        fixed_lines.append(fixed)
    
    return '\n'.join(fixed_lines)

def process_file(file_path):
    """Process entire file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and fix all Section 8 blocks
    def fix_match(match):
        header = match.group(1)
        section8 = match.group(2)
        fixed_section8 = fix_section8(section8)
        return header + fixed_section8
    
    pattern = r'(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)'
    fixed_content = re.sub(pattern, fix_match, content, flags=re.DOTALL)
    
    # Count fixes
    fixes = fixed_content != content
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    return fixes

if __name__ == "__main__":
    files = [
        r"d:\MFF\Pico\Documentation\Docs_0001_0100.md",
        r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    ]
    
    print("=== Comprehensive Quality Fix ===\n")
    
    for file_path in files:
        filename = file_path.split('\\')[-1]
        print(f"Processing {filename}...")
        fixed = process_file(file_path)
        if fixed:
            print(f"  Applied fixes")
        else:
            print(f"  No changes needed")

    
    print("\n=== Complete ===")
    print("Re-run audit_quality.py to verify")
