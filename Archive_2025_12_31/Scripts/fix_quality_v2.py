"""
Enhanced Quality Fix Script v2
Handles complex multi-line formatting issues
"""

import re

def fix_double_periods(text):
    """Replace .. with ."""
    return re.sub(r'\.\.+', '.', text)

def fix_broken_multiline_drag(text):
    """Fix broken multi-line 'From **X**.\n    *   drag' format"""
    # Pattern: "From **Category**.\n    *   drag" should be "From **Category**, drag"
    text = re.sub(
        r'(From \*\*[^*]+\*\*)\.[\r\n]+\s+\*\s+drag\s+',
        r'\1, drag ',
        text,
        flags=re.MULTILINE
    )
    return text

def fix_sleep_format(text):
    """Standardize sleep statements"""
    # Fix: `sleep 0.2s` to `sleep [0.2] seconds`
    text = re.sub(
        r'`sleep\s+([\d.]+)s(?!econds)',
        r'`sleep [\1] seconds`',
        text
    )
    # Fix unclosed sleep: `sleep 0.2 seconds
    text = re.sub(
        r'`sleep\s+\[?([\d.]+)\]?\s+seconds(?!`)',
        r'`sleep [\1] seconds`',
        text
    )
    return text

def fix_led_toggle_format(text):
    """Fix LED ON/OFF toggle statements"""
    # Fix: `Turn LED [GP25] [ON]` format
    text = re.sub(
        r'`Turn LED \[([^\]]+)\] \[([^\]]+)\](?!`)',
        r'`Turn LED [\1] [\2]`',
        text
    )
    return text

def fix_variable_change_format(text):
    """Fix variable change statements"""
    # Fix: `Change `[value]` to `[value]`` (nested backticks)
    text = re.sub(
        r'`Change\s+`\[([^\]]+)\]`\s+to\s+`\[([^\]]+)\]`',
        r'change [\1] to [\2]',
        text
    )
    return text

def add_missing_category_comprehensive(line):
    """More comprehensive category addition"""
    # Skip if already has category
    if 'from **' in line.lower() or not line.strip().startswith('*'):
        return line
    
    # Get the instruction part
    stripped = line.strip()
    if not stripped.startswith('*'):
        return line
    
    # Remove leading bullet
    content = stripped[1:].strip()
    if not content:
        return line
    
    # Determine category based on content
    categories = [
        (r'^Turn LED', 'Smart IO'),
        (r'^Setup\s+(?:Button|Pin)', 'Inputs'),
        (r'^Setup\s+LCD', 'Displays'),
        (r'^LCD\s+(?:Print|Move|Clear)', 'Displays'),
        (r'^TM1637', 'Displays'),
        (r'^Show\s+(?:Char|Number)', 'Displays'),
        (r'^Display', 'Displays'),
        (r'^sleep\s+\[', 'Timing'),
       (r'^Wait', 'Timing'),
        (r'^IF\s+', 'Logic'),
        (r'^Check', 'Logic'),
        (r'^Read\s+(?:Analog|Pin)', 'Inputs'),
        (r'^digital\s+read', 'Pin Access'),
        (r'^set\s+Pin', 'Pin Access'),
        (r'^Change\s+', 'Variables'),
        (r'^Set\s+.*?\s+to', 'Variables'),
        (r'^Create\s+variable', 'Variables'),
        (r'^Repeat', 'Loops'),
        (r'^forever\s+do', 'Loops'),
    ]
    
    for pattern, category in categories:
        if re.search(pattern, content, re.IGNORECASE):
            indent = len(line) - len(line.lstrip())
            return ' ' * indent + f'*   From **{category}**, drag `{content.rstrip(".")}`.\n'
    
    return line

def comprehensive_section8_fix(section8_text):
    """Apply all fixes to Section 8"""
    
    # Fix 1: Double periods
    fixed = fix_double_periods(section8_text)
    
    # Fix 2: Broken multi-line drag statements
    fixed = fix_broken_multiline_drag(fixed)
    
    # Fix 3: Sleep format
    fixed = fix_sleep_format(fixed)
    
    # Fix 4: LED toggle format
    fixed = fix_led_toggle_format(fixed)
    
    # Fix 5: Variable change format
    fixed = fix_variable_change_format(fixed)
    
    # Fix 6: Add missing categories line by line
    lines = fixed.split('\n')
    enhanced_lines = []
    for line in lines:
        enhanced = add_missing_category_comprehensive(line)
        enhanced_lines.append(enhanced)
    
    return '\n'.join(enhanced_lines)

def process_file(file_path):
    """Process entire file with enhanced fixes"""
    
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix all Section 8 blocks
    def fix_match(match):
        header = match.group(1)
        section8 = match.group(2)
        fixed_section8 = comprehensive_section8_fix(section8)
        return header + fixed_section8
    
    pattern = r'(### 8.*?Step-by-Step Guide\s*\n)(.*?)(?=\n### 9)'
    fixed_content = re.sub(pattern, fix_match, content, flags=re.DOTALL)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"  Applied enhanced fixes")

if __name__ == "__main__":
    files = [
        r"d:\MFF\Pico\Documentation\Docs_0001_0100.md",
        r"d:\MFF\Pico\Documentation\Docs_0101_0200_FINAL.md"
    ]
    
    print("=== Enhanced Quality Fix v2 ===\n")
    
    for file_path in files:
        process_file(file_path)
    
    print("\n=== Complete ===")
    print("Re-run audit_quality.py to verify improvements")
