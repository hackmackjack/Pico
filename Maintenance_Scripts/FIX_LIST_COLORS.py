import os
import re

def fix_list_indentation():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    in_section_8 = False
    
    for line in lines:
        if line.strip().startswith("### 8. Step-by-Step Guide"):
            in_section_8 = True
            new_lines.append(line)
            continue
        if line.strip().startswith("### 9. Execution Flow"):
            in_section_8 = False
            new_lines.append(line)
            continue
            
        if in_section_8:
            # Check for bullet points
            s_line = line.lstrip()
            if s_line.startswith("* "):
                # It's a bullet. Force 2 spaces indent.
                new_lines.append("  " + s_line)
            elif s_line.startswith("1. ") or s_line.startswith("2. ") or s_line.startswith("3. ") or s_line.startswith("4. ") or s_line.startswith("5. "):
                # Numbered list. Force 0 indent.
                new_lines.append(s_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    fix_list_indentation()
