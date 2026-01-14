"""
SMART Step-by-Step Guide Fixer v2.0
Fixes guides based on established patterns from P0001 and P0011.
"""
import re

def fix_guide_section(guide_text, project_num):
    """Fix a single guide section with smart pattern detection."""
    
    lines = guide_text.strip().split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # Skip empty lines and headers
        if not line.strip() or line.strip().startswith('###'):
            i += 1
            continue
        
        # Check if this line has "drag" but next line doesn't have "Snap"
        if 'drag' in line.lower():
            # Look ahead to see if next line has "Snap"
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            
            if 'snap' not in next_line.lower() and '**snap**' not in next_line.lower():
                # Determine indent level
                indent = len(line) - len(line.lstrip())
                snap_indent = " " * indent
                
                # Smart snap instruction based on context
                if 'forever' in line.lower() or 'workspace' in line.lower():
                    snap = f"{snap_indent}    *   **Snap** itinto the workspace."
                elif 'if' in line.lower() or 'logic' in line.lower():
                    snap = f"{snap_indent}    *   **Snap** it inside the loop."
                elif 'variable' in line.lower() or 'set' in line.lower():
                    snap = f"{snap_indent}    *   **Snap** the value block into the socket."
                else:
                    snap = f"{snap_indent}    *   **Snap** it below the previous block."
                
                fixed_lines.append(snap)
        
        i += 1
    
    return '\n'.join(fixed_lines)

def process_documentation(input_file, output_file):
    """Process entire documentation file."""
    
    print(f"Processing {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all Step-by-Step Guide sections
    pattern = r'(### 8️⃣ Step-by-Step Guide\s*\n)(.*?)(\n### )'
    
    def replace_guide(match):
        header = match.group(1)
        guide_content = match.group(2)
        next_section = match.group(3)
        
        # Extract project number from context
        before_text = content[:match.start()]
        proj_match = re.search(r'## 1️⃣ Project (\d+):', before_text[::-1])
        proj_num = proj_match.group(1)[::-1] if proj_match else "Unknown"
        
        fixed_guide = fix_guide_section(guide_content, proj_num)
        return header + fixed_guide + next_section
    
    fixed_content = re.sub(pattern, replace_guide, content, flags=re.DOTALL)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"[OK] Fixed file saved to {output_file}")

# Process both files
print("=" * 60)
print("SMART STEP-BY-STEP GUIDE FIXER")
print("=" * 60)

process_documentation(
    'd:/MFF/Pico/Documentation/Docs_0001_0100.md',
    'd:/MFF/Pico/Documentation/Docs_0001_0100_AUTOFIXED.md'
)

process_documentation(
    'd:/MFF/Pico/Documentation/Docs_0101_0200.md',
    'd:/MFF/Pico/Documentation/Docs_0101_0200_AUTOFIXED.md'
)

print("\n" + "=" * 60)
print("[OK] COMPLETE!")
print("=" * 60)
print("\nNext steps:")
print("1. Review _AUTOFIXED.md files")
print("2. Spot-check 10-20 projects for quality")
print("3. If satisfied, replace originals with:")
print("   mv Docs_0001_0100_AUTOFIXED.md Docs_0001_0100.md")
print("   mv Docs_0101_0200_AUTOFIXED.md Docs_0101_0200.md")
