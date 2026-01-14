
import re

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def fix_code_blocks():
    print(f"Reading {DOC_PATH}...")
    try:
        with open(DOC_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    new_lines = []
    in_code_block = False
    
    # We want to remove blank lines INSIDE code blocks, 
    # BUT we want to keep them if they are separating distinct logical blocks (like imports vs code).
    # However, if *every* line is followed by a blank, that's just bad formatting.
    # Simple heuristic: Inside a code block, if line N is code and line N+1 is blank, and line N+2 is code... 
    # we can probably collapse it IF this pattern is pervasive.
    # EASIER APPROACH: Just strip all blank lines inside code blocks?
    # That might be too aggressive (merging imports with code).
    # Better: logic to `strip` blank lines if the previous line was non-blank?
    
    # Let's try to detect if it's "double spaced".
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Toggle code block state
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
            
        if in_code_block:
            # If line is blank
            if stripped == "":
                # Check previous line
                if i > 0 and lines[i-1].strip() != "":
                    # Logic: If we are in a code block, and we see a blank line, 
                    # check if the NEXT line is also blank?
                    # If the next line is NOT blank, this is a single gap.
                    # Standard python style uses gaps.
                    # BUT the user screenshot shows `import machine \n \n import time`.
                    # Our file view showed `import machine \n \n import time`.
                    # So there are TWO blank lines, or the view adds one?
                    # `view_file` output:
                    # 94: # Setup
                    # 95: 
                    # 96: led = ...
                    # That looks like ONE blank line.
                    # User complaint "Line breker for each lines" implies they want NO blank lines for simple sequences.
                    
                    # Refined Logic:
                    # If this line is blank, and the NEXT line is non-blank...
                    # we only keep it if it looks like a paragraph break?
                    # Let's try to just DELETE simple single blank lines inside code blocks
                    # to make it dense. Users usually prefer dense code in docs.
                    continue
            new_lines.append(line)
        else:
            new_lines.append(line)

    content = "".join(new_lines)
    
    print("Writing fixed content...")
    with open(DOC_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    fix_code_blocks()
