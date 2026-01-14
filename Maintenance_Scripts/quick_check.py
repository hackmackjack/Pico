import sys

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

projects = content.count('## 1. Project')
print(f"Total Projects: {projects}/100")
print(f"Status: {'SUCCESS' if projects == 100 else 'INCOMPLETE'}")
print(f"Total Lines: {len(content.splitlines())}")
print(f"File Size: {len(content) // 1024} KB")
