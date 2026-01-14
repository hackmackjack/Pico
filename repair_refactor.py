import os

REFACTOR_FILE = r"d:\MFF\Pico\refactor_task.md"
DASHBOARD_FILE = r"d:\MFF\Pico\final_dashboard.txt"

with open(REFACTOR_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 16 (index 15) is Batch 141.
# But wait, 139 is line 14. 140 is line 15.
# So Batch 141 to 250 are lines 16 to 125.
# Indices are 15 to 124.

# Let's rebuild the lines properly.
with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
    dashboard_lines = f.readlines()

# Correct any encoding issues in the EXISTING lines too if possible.
# Better yet, just replace the range.

new_lines = lines[:15] + dashboard_lines + lines[125:]

# Fix the COMPLETED checkmarks at lines 14, 15 (indices 13, 14)
new_lines[13] = new_lines[13].replace('âœ…', '✅').replace('ðŸ”„', '🔄')
new_lines[14] = new_lines[14].replace('âœ…', '✅').replace('ðŸ”„', '🔄')

with open(REFACTOR_FILE, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
