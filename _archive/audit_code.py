
import re
import ast
import sys

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def audit_file(filepath):
    print(f"Auditing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    # Regex to find Project headers and Code blocks
    # Logic: Find "Project XXXX" then look ahead for the python block
    
    # Split by project to make context easier
    projects = re.split(r'^##\s+1️⃣\s+Project\s+', content, flags=re.MULTILINE)
    
    issues_found = 0
    
    for proj in projects:
        if not proj.strip(): continue
        
        # Extract ID
        lines = proj.split('\n')
        title_line = lines[0]
        project_id_match = re.match(r'(\d+):', title_line)
        if not project_id_match:
            continue
            
        project_id = project_id_match.group(1)
        
        # Find Python Code
        code_blocks = re.findall(r'```python(.*?)```', proj, re.DOTALL)
        
        if not code_blocks:
            print(f"[WARN] Project {project_id}: No Python code found.")
            issues_found += 1
            continue
            
        # Verify each block (usually only one per project)
        for i, code in enumerate(code_blocks):
            code = code.strip()
            
            # 1. Syntax Check
            try:
                ast.parse(code)
            except SyntaxError as e:
                print(f"[FAIL] Project {project_id} Code Block {i+1}: Syntax Error")
                print(f"       {e}")
                print(f"       Line {e.lineno}: {e.text.strip() if e.text else '?'}")
                issues_found += 1
                continue
                
            # 2. Logic Heuristics
            # Check for missing imports
            if "machine" in code and "import machine" not in code:
                 print(f"[WARN] Project {project_id}: Uses 'machine' but missing import.")
                 issues_found += 1
            if "sleep" in code and "import time" not in code and "from time" not in code:
                 print(f"[WARN] Project {project_id}: Uses 'sleep' but missing 'time' import.")
                 issues_found += 1
                 
            # Check for infinite loops without sleep (Crash risk)
            if "while True" in code and "sleep" not in code and "wait" not in code:
                # heuristic, might be false positive if they use other blocking calls
                print(f"[WARN] Project {project_id}: 'while True' loop possibly missing sleep (CPU Hog).")
                
            # Check for Pin placeholders
            if "[" in code and "]" in code:
                 # Regex to see if they are part of a list or placeholders
                 # Look for [0-9] as a single item which is usually fine (list index), but logic blocks often use [PIN] notation
                 pass

    if issues_found == 0:
        print("[OK] SUCCESS: No syntax errors or major issues found in code blocks.")
    else:
        print(f"[FAIL] COMPLETED: Found {issues_found} issues.")

if __name__ == "__main__":
    audit_file(DOC_PATH)
