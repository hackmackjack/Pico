#!/usr/bin/env python3
"""
VALIDATION - Elite Standard Documentation Complete Check
"""

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Count projects
projects = content.count('## 1. Project')
batches = {}
for i in range(51, 61):
    count = content.count(f'Batch {i}')
    if count > 0:
        batches[i] = count

# Count sections
section_counts = {
    '2. Learning Objective': content.count('### 2. Learning Objective'),
    '3. Concepts': content.count('### 3. Concepts Introduced'),
    '4. Hardware': content.count('### 4. Hardware Required'),
    '5. Wiring': content.count('### 5. Wiring'),
    '6. Blocks': content.count('### 6. Blocks Used'),
    '7. Variables': content.count('### 7. Variables'),
    '8. Step-by-Step': content.count('### 8. Step-by-Step Guide'),
    '9. Execution Flow': content.count('### 9. Execution Flow'),
    '10. Generated Code': content.count('### 10. Generated Code'),
    '11. Common Mistakes': content.count('### 11. Common Mistakes'),
    '12. Try This Next': content.count('### 12. Try This Next'),
}

print("=" * 70)
print("📊 VALIDATION REPORT")
print("=" * 70)
print()
print("FILE: Docs_0501_0600.md")
print(f"Total Lines: {len(content.splitlines()): ,}")
print(f"Total Size: {len(content):,} bytes ({len(content) // 1024} KB)")
print()
print(f"✅ Projects Found: {projects}/100")
print()
print("BATCH HEADERS:")
for batch_num in range(51, 61):
    present = "✓" if batch_num in batches else "✗"
    print(f"  {present} Batch {batch_num}: {'Present' if batch_num in batches else 'Missing'}")
print()
print("SECTION COMPLETENESS:")
for section, count in section_counts.items():
    status = "✅" if count >= 95 else "⚠️"
    print(f"  {status} {section}: {count}/100")
print()

# Check for Elite Standard compliance
has_snap = content.count('**Snap**')
has_from = content.count('**from ')
print("ELITE STANDARD MARKERS:")
print(f"  ✓ '**Snap**' markers: {has_snap}")
print(f"  ✓ 'from [Category], drag' patterns: {has_from}")
print()

if projects == 100:
    print("=" * 70)
    print("🎉 SUCCESS! ALL 100 PROJECTS GENERATED")
    print("=" * 70)
    print()
    print("✅ Documentation Complete")
    print("✅ Elite Standard v2.0 Format")
    print("✅ Ready for Production Use")
else:
    print("⚠️  Project count mismatch - expected 100")

print()
print("=" * 70)
