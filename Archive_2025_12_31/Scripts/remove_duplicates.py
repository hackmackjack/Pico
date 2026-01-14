#!/usr/bin/env python3
"""
FIX DUPLICATES - Remove duplicate 0503 and 0504
"""

import re

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into projects
projects = re.split(r'(## 1\. Project \d{4}:)', content)

# Rebuild without duplicates
seen = set()
output = [projects[0]]  # Header

for i in range(1, len(projects), 2):
    if i+1 < len(projects):
        header = projects[i]
        body = projects[i+1]
        
        # Extract project number
        match = re.search(r'Project (\d{4}):', header)
        if match:
            proj_num = match.group(1)
            if proj_num not in seen:
                seen.add(proj_num)
                output.append(header)
                output.append(body)
            else:
                print(f"Skipping duplicate: Project {proj_num}")

final_content = ''.join(output)

# Write fixed version
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(final_content)

print()
print("✅ Duplicates removed")
print(f"Final project count: {len(seen)}")
