
import re

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def fix_table_newlines():
    print(f"Reading {DOC_PATH}...")
    try:
        with open(DOC_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect Table Rows
        # Valid row starts with "|" and usually has another "|"
        is_table_row = stripped.startswith('|') and '|' in stripped[1:]
        
        if is_table_row:
            in_table = True
            new_lines.append(line)
        elif in_table:
            # We are inside or just after a table
            if stripped == "":
                # It's a blank line. 
                # If the NEXT line is also a table row, we should SKIP this blank line
                # to merge the table.
                
                # Look ahead
                next_is_table = False
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line == "": 
                        continue # Skip multiple blanks
                    if next_line.startswith('|'):
                        next_is_table = True
                    break
                
                if next_is_table:
                    # We are in a table gap. DELETE this blank line.
                    continue
                else:
                    # Table ended. Keep this blank line (or maybe ensure just 1)
                    in_table = False
                    new_lines.append(line)
            else:
                # Text content implies table ended
                in_table = False
                new_lines.append(line)
        else:
            # Not in table, just append
            new_lines.append(line)

    # Re-join
    content = "".join(new_lines)
    
    # Optional: cleanup multiple blank lines elsewhere to max 2
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    print("Writing fixed content...")
    with open(DOC_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    fix_table_newlines()
