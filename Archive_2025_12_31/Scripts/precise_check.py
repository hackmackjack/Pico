import re

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all project headers
projects = re.findall(r'## 1\. Project (\d{4}):', content)
print(f"Projects Found: {len(projects)}")
print(f"Range: {min(projects)} to {max(projects)}" if projects else "None")
print()
if len(projects) == 100:
    print("✅ SUCCESS! All 100 projects present")
    print(f"   Projects {projects[0]} through {projects[-1]}")
else:
    print(f"⚠️  Found {len(projects)} projects (expected 100)")
    if len(projects) > 100:
        # Find duplicates
        from collections import Counter
        counts = Counter(projects)
        dups = [p for p, c in counts.items() if c > 1]
        if dups:
            print(f"   Duplicates: {dups}")
