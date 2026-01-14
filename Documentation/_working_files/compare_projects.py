import re
from pathlib import Path

# Read files
ps_file = Path(r"d:\MFF\Pico\Problem_Statements\Projects_0101_0200.md").read_text(encoding='utf-8')
doc_file = Path(r"d:\MFF\Pico\Documentation\Docs_0101_0200_NEW.md").read_text(encoding='utf-8')

# Extract project titles
ps_projects = {}
for match in re.finditer(r'^### Project (\d{4}): (.+)$', ps_file, re.MULTILINE):
    proj_num = match.group(1)
    if proj_num.startswith('01'):
        ps_projects[proj_num] = match.group(2).strip()

doc_projects = {}
for match in re.finditer(r'^## \S+ Project (\d{4}): (.+)$', doc_file, re.MULTILINE):
    proj_num = match.group(1)
    if proj_num.startswith('01'):
        doc_projects[proj_num] = match.group(2).strip()

# Find mismatches
mismatches = []
missing = []

for proj_num in sorted(ps_projects.keys()):
    ps_title = ps_projects[proj_num]
    if proj_num in doc_projects:
        doc_title = doc_projects[proj_num]
        if ps_title != doc_title:
            mismatches.append((proj_num, ps_title, doc_title))
    else:
        missing.append((proj_num, ps_title))

# Report
print(f"=== MISMATCH ANALYSIS ===\n")
print(f"Total Projects in Problem Statements: {len(ps_projects)}")
print(f"Total Projects in Documentation: {len(doc_projects)}")
print(f"Mismatched Titles: {len(mismatches)}")
print(f"Missing from Documentation: {len(missing)}\n")

if mismatches:
    print("=== MISMATCHED PROJECTS ===")
    for proj, ps_t, doc_t in mismatches:
        print(f"\nProject {proj}:")
        print(f"  Problem Statement: \"{ps_t}\"")
        print(f"  Documentation:     \"{doc_t}\"")

if missing:
    print(f"\n=== MISSING FROM DOCUMENTATION ({len(missing)}) ===")
    for proj, title in missing[:10]:  # Show first 10
        print(f"  {proj}: {title}")
    if len(missing) > 10:
        print(f"  ... and {len(missing) - 10} more")

print("\n=== SUMMARY ===")
if len(mismatches) == 0 and len(missing) == 0:
    print("✅ PERFECT ALIGNMENT - All projects match!")
else:
    print(f"⚠️ Issues found: {len(mismatches)} mismatches, {len(missing)} missing")
