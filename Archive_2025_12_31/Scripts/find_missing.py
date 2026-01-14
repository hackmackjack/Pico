import re

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

projects = re.findall(r'## 1\. Project (\d{4}):', content)
project_nums = sorted([int(p) for p in projects])

# Find missing
all_expected = set(range(501, 601))
found = set(project_nums)
missing = sorted(all_expected - found)

print(f"Total found: {len(projects)}")
print(f"Missing: {missing if missing else 'None'}")

# Find duplicates
from collections import Counter
counts = Counter(projects)
dups = [p for p, c in counts.items() if c > 1]
print(f"Duplicates: {dups if dups else 'None'}")
