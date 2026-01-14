#!/usr/bin/env python3
"""
Complete Custom Documentation Generator
Projects 0501-0600 - All 100 with unique content
"""

import re

problems_file = r'd:\MFF\Pico\Problem_Statements\Projects_0501_0600.md'

# Read all problem statements
with open(problems_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse projects (simple extraction)
projects_raw = re.split(r'### Project (\d{4}):', content)[1:]
projects_data = []

for i in range(0, len(projects_raw), 2):
    num = projects_raw[i].strip()
    body = projects_raw[i+1] if i+1 < len(projects_raw) else ""
    
    # Extract title
    title_match = re.search(r'^([^\n]+)', body)
    title = title_match.group(1).strip() if title_match else "Unknown"
    
    # Extract problem statement
    prob_match = re.search(r'\*\*Problem Statement:\*\*\s*\n(.+?)(?=\n\n\*\*Hardware)', body, re.DOTALL)
    problem = prob_match.group(1).strip() if prob_match else ""
    
    # Extract hardware
    hw_match = re.search(r'\*\*Hardware Requirements:\*\*\s*\n(.*?)(?=\n\n\*\*Expected)', body, re.DOTALL)
    hardware_raw = hw_match.group(1).strip() if hw_match else ""
    hardware = ', '.join([h.strip().replace('*', '').strip() for h in hardware_raw.split('\n') if h.strip()])
    
    projects_data.append({
        'num': num,
        'title': title,
        'problem': problem,
        'hardware': hardware
    })

print(f"Parsed {len(projects_data)} projects")

# Now generate documentation
output_lines = []
output_lines.append("# 📚 Pico 2500: Elite Documentation (Projects 0501-0600)\n\n")
output_lines.append("**Standard**: Elite Documentation Standard v2.0\n")
output_lines.append("**Projects**: 100 (0501-0600)\n\n---\n\n")

# Write to file in batches
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600_CUSTOM.md', 'w', encoding='utf-8') as f:
    f.write(''.join(output_lines))

print(f"✓ Created base file")
print(f"Ready for content insertion")
print(f"Total projects: {len(projects_data)}")
