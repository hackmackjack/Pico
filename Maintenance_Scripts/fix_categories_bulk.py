
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

def replace_category(match):
    prefix = match.group(1)
    suffix = match.group(3)
    return prefix + "Smart IO" + suffix

pattern = re.compile(r'(from \*\*|From \*\*|from |From )(Time)(\*\*, drag `pico_wait`|, drag `pico_wait`)', re.IGNORECASE)

for filename in files:
    file_path = os.path.join(dir_path, filename)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub(replace_category, content)
    new_content = re.sub(r'(?i)from \*\*Time\*\*', 'from **Smart IO**', new_content)
    new_content = re.sub(r'(?i)from Time', 'from Smart IO', new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")

print("Bulk replacement complete.")
