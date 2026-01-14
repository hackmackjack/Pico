import os

def fix_indentation():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    # Analysis suggests indentation issue is primarily in the first project (Batch 51 start)
    # The snippet showed lines 3 to 48 were indented by 4 spaces.
    # We will detect if line starts with 4 spaces and looks like a header or text that represents the structure.
    
    for i, line in enumerate(lines):
        # Limit the fix to the beginning of the file to avoid accidental damage elsewhere
        # until valid Phase B is seen.
        if i < 200: 
            # If line starts with 4 spaces and next char is non-whitespace, and it's not a list item inside a guide that needs indentation?
            # Actually, the snippet showed even headers indented: "    ## 1. Project..."
            # Headers should NEVER be indented in this standard.
            if line.startswith("    #"):
                new_lines.append(line[4:])
            elif line.startswith("    ---"):
                new_lines.append(line[4:])
            elif line.startswith("    **A. Init"):
                new_lines.append(line[4:])
            elif line.startswith("    1.  **Config"):
                new_lines.append(line[4:])
            # Also catch the intermediate lines which might be indented 4 spaces
            # Since the user diff showed EVERYTHING in that block indented...
            # We can aggressively unindent if we are in that specific block.
            elif line.startswith("    ") and not line.startswith("        ") and i < 60:
                # Remove exactly 4 spaces
                new_lines.append(line[4:])
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    fix_indentation()
