
import re

DOC_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def fix_variables():
    with open(DOC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into projects to process safely
    # Using a capture group to keep the delimiter
    parts = re.split(r'(^## 1️⃣ Project .+$)', content, flags=re.MULTILINE)
    
    # parts[0] is preamble
    # parts[1] is header of proj 1, parts[2] is body of proj 1
    # parts[3] is header of proj 2, parts[4] is body of proj 2...
    
    new_content = parts[0]
    
    fixed_count = 0
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]
        
        # 1. Check for variables
        vars_match = re.search(r'### 7️⃣ Variables & State\n(.*?)\n###', body, re.DOTALL)
        if not vars_match:
            new_content += header + body
            continue
            
        vars_text = vars_match.group(1).strip()
        variable_names = re.findall(r'\*\s+\*\*(.+?)\*\*', vars_text)
        
        if not variable_names:
            new_content += header + body
            continue
            
        # 2. Check logic section
        logic_match = re.search(r'(### 8️⃣ Block Logic\n)(.*?)(?=\n###)', body, re.DOTALL)
        if not logic_match:
            new_content += header + body
            continue
            
        logic_header = logic_match.group(1) # ### 8️⃣ Block Logic\n
        logic_body = logic_match.group(2)
        
        if "create variable" in logic_body.lower() or "setup variables" in logic_body.lower():
            new_content += header + body
            continue
            
        # 3. Apply Fix
        # print(f"Fixing {header.strip()}...")
        
        # Prepare injection
        var_list_str = ", ".join([f"`{v}`" for v in variable_names])
        injection = (
            f"*   **1. Setup Variables**\n"
            f"    *   Click the **Variables** category.\n"
            f"    *   Click **Create variable...** and type the name.\n"
            f"    *   Repeat for: {var_list_str}.\n"
        )
        
        # Renumber existing steps
        # Look for *   **1. Step** ... *   **2. Step**
        # We need to increment them. It's safer to just replace them assuming they are in order.
        # Logic: Replace `*   **N.` with `*   **N+1.`
        # We do this in reverse order (9->10, 8->9) to avoid overwriting 1->2 then 2->3... wait, no.
        # String replacement is linear. But regex might overlap? 
        # Safer: Pass a callback function to re.sub that parses the number and adds 1.
        
        def increment_step(match):
            num = int(match.group(1))
            rest = match.group(2)
            return f"*   **{num + 1}. {rest}"

        new_logic_body = re.sub(r'\*   \*\*(\d+)\. (.+)', increment_step, logic_body)
        
        # Reconstruct Body
        # Replace the original logic section with the new logic section
        # We need to be careful with strings. 
        # logic_match.start() is relative to 'body' string.
        
        # Actually easier to just replace the logic_body text
        # But we need to insert the injection at the top of logic_body
        
        final_logic_body = injection + new_logic_body
        
        # Replace in body
        new_body = body.replace(logic_header + logic_body, logic_header + final_logic_body)
        
        new_content += header + new_body
        fixed_count += 1

    with open(DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Fixed {fixed_count} projects.")

if __name__ == "__main__":
    fix_variables()
