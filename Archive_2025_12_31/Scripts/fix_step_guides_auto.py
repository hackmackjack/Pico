"""
Automated Step-by-Step Guide Fixer
Applies ultra-explicit format to all projects based on established patterns.
"""
import re

# Template patterns for common scenarios
TEMPLATES = {
    'button_check': """*   From **Logic**, drag `if [condition] then`.
    *   **Snap** it inside the forever loop.
    *   From **Pin Access**, drag `digital read pin [N]`.
    *   **Snap** the digital read block into the `[condition]` socket.""",
    
    'led_control': """*   From **Smart IO**, drag `Turn LED [GPN] [ON]`.
    *   **Snap** it inside/below the previous block.""",
    
    'wait_block': """*   From **Timing**, drag `sleep [1] seconds`.
    *   **Snap** it below the previous block.
    *   Change `[1]` to `[N]`.""",
    
    'variable_set': """*   From **Variables**, drag `set [var] to`.
    *   From **[Category]**, drag `[block name]`.
    *   **Snap** the [block name] into the socket of the set block.""",
    
    'forever_loop': """*   From **Loops**, drag `forever do`.
    *   **Snap** it into the workspace (this will be your main container)."""
}

def add_snap_instructions(guide_text):
    """Add 'Snap' instructions to guides that have 'drag' but missing 'Snap'."""
    
    lines = guide_text.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        
        # If line has 'drag' but next line doesn't have 'Snap', add it
        if 'drag' in line.lower() and i + 1 < len(lines):
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            
            if 'snap' not in next_line.lower():
                # Infer snap location based on context
                indent = len(line) - len(line.lstrip())
                
                if 'forever' in line or 'loop' in line.lower():
                    snap_text = " " * (indent + 4) + "*   **Snap** it into the workspace."
                elif 'if' in line.lower():
                    snap_text = " " * (indent + 4) + "*   **Snap** it inside the loop/parent block."
                elif 'set' in line or 'variable' in line.lower():
                    snap_text = " " * (indent + 4) + "*   **Snap** the value block into the socket."
                else:
                    snap_text = " " * (indent + 4) + "*   **Snap** it below the previous block."
                
                fixed_lines.append(snap_text)
    
    return '\n'.join(fixed_lines)

def convert_abstract_to_explicit(guide_text):
    """Convert abstract guides like '`var` = Read' to explicit drag/snap."""
    
    # Pattern: `variable` = expression
    guide_text = re.sub(
        r'`(\w+)` = (.*?)\.',
        lambda m: f"""*   From **Variables**, drag `set [{m.group(1)}] to`.
    *   From **[Category]**, drag the block for {m.group(2)}.
    *   **Snap** it into the socket.""",
        guide_text
    )
    
    return guide_text

# Main processing function
def fix_project_guide(project_text):
    """Fix a single project's Step-by-Step Guide."""
    
    guide_match = re.search(r'(### 8️⃣ Step-by-Step Guide\s*)(.*?)(###|\Z)', project_text, re.DOTALL)
    
    if not guide_match:
        return project_text  # No guide found
    
    guide_section = guide_match.group(2)
    
    # Apply fixes
    fixed_guide = add_snap_instructions(guide_section)
    fixed_guide = convert_abstract_to_explicit(fixed_guide)
    
    # Replace in original text
    new_text = project_text.replace(guide_match.group(0), guide_match.group(1) + fixed_guide + guide_match.group(3))
    
    return new_text

def process_file(filepath):
    """Process entire documentation file."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by projects
    projects = re.split(r'(## 1️⃣ Project \d+:)', content)
    
    fixed_projects = [projects[0]]  # Keep header
    
    for i in range(1, len(projects), 2):
        if i + 1 < len(projects):
            project_header = projects[i]
            project_content = projects[i + 1]
            
            fixed_content = fix_project_guide(project_content)
            fixed_projects.append(project_header)
            fixed_projects.append(fixed_content)
    
    return ''.join(fixed_projects)

# Process both files
print("Processing Docs_0001_0100.md...")
fixed_1_100 = process_file('d:/MFF/Pico/Documentation/Docs_0001_0100.md')
with open('d:/MFF/Pico/Documentation/Docs_0001_0100_FIXED.md', 'w', encoding='utf-8') as f:
    f.write(fixed_1_100)

print("Processing Docs_0101_0200.md...")
fixed_101_200 = process_file('d:/MFF/Pico/Documentation/Docs_0101_0200.md')
with open('d:/MFF/Pico/Documentation/Docs_0101_0200_FIXED.md', 'w', encoding='utf-8') as f:
    f.write(fixed_101_200)

print("✅ Done! Created _FIXED.md files. Review then replace originals.")
