import re

file_path = r"d:\MFF\Pico\Documentation\Docs_0101_0200.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

projects = re.split(r'^## 1\. Project ', content, flags=re.MULTILINE)
results = []

print(f"Found {len(projects)-1} projects.")

for i, proj in enumerate(projects):
    if i == 0: continue # Skip preamble
    
    # Extract ID
    input_lines = proj.strip().split('\n')
    title_line = input_lines[0]
    proj_id = title_line.split(':')[0].strip()
    
    # Check sections
    has_exec = "### 9. Execution Flow" in proj
    has_code = "### 10. Generated Code" in proj
    has_mistakes = "### 11. Common Mistakes" in proj
    has_next = "### 12. Try This Next" in proj
    
    # Check headers
    headers = re.findall(r'^### \d+\.', proj, flags=re.MULTILINE)
    
    status = "OK"
    missing = []
    if not has_exec: missing.append("9")
    if not has_code: missing.append("10")
    if not has_mistakes: missing.append("11")
    if not has_next: missing.append("12")
    
    if missing:
        status = f"MISSING {','.join(missing)}"
        
    print(f"{proj_id}: {status}")
