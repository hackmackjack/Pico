
lines = open('Docs_0001_0100.md', 'r', encoding='utf-8').readlines()
# Removing duplicates between Project 0007 (approx line 634) and Project 0008 (approx line 1278)
# We keep lines 0-633 (line 1 to 634)
# We keep lines 1277-end (line 1278 to end)
new_lines = lines[:634] + lines[1277:]
open('Docs_0001_0100.md', 'w', encoding='utf-8').writelines(new_lines)
print(f"Removed {1277-634} lines. New line count: {len(new_lines)}")
