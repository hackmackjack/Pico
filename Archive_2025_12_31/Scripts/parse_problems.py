#!/usr/bin/env python3
"""
PROPER CUSTOM GENERATOR
Reads each problem statement and creates unique documentation
"""

import re

print("=" * 70)
print("🚀 CREATING TRULY CUSTOM DOCUMENTATION")
print("=" * 70)
print()

# Read problem statements
with open(r'd:\MFF\Pico\Problem_Statements\Projects_0501_0600.md', 'r', encoding='utf-8') as f:
    problems_content = f.read()

# Parse each project's specific details
# Pattern to extract: Project number, title, category, problem statement, hardware
pattern = r'### Project (\d{4}): ([^\n]+)\n\*\*Category:\*\* ([^\n]+)\n.*?\n\*\*Problem Statement:\*\*\s*\n([^\n]+)\n\n\*\*Hardware Requirements:\*\*\s*\n(.*?)(?=\n\n\*\*Expected Behavior:)'

matches = re.findall(pattern, problems_content, re.DOTALL)

print(f"Found {len(matches)} projects with detailed problem statements")
print()

# Store parsed data
projects = {}
for num, title, category, problem, hardware_raw in matches:
    # Clean up the problem statement (remove quotes)
    problem = problem.strip().strip('"').strip('"').strip()
    
    # Parse hardware list
    hardware_items = [h.strip().strip('*').strip() for h in hardware_raw.split('\n') if h.strip()]
    
    projects[int(num)] = {
        'title': title.strip(),
        'category': category.strip(),
        'problem': problem,
        'hardware': hardware_items
    }

# Show sample
print("Sample Projects:")
for i in [501, 502, 503]:
    if i in projects:
        p = projects[i]
        print(f"\nProject {i}: {p['title']}")
        print(f"  Problem: {p['problem'][:60]}...")
        print(f"  Hardware: {', '.join(p['hardware'])}")

print()
print(f"Total projects ready for custom generation: {len(projects)}")
print()
print("This data will be used to create UNIQUE documentation for each project")
print("=" * 70)

# Save parsed data for the generator
import json
with open(r'd:\MFF\Pico\projects_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(projects, f, indent=2)

print("✅ Parsed data saved to projects_parsed.json")
print("Ready to generate custom documentation!")
