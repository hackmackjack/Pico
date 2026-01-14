
import os
import re

file_path = r'd:\MFF\Pico\Documentation\Docs_0001_0100.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for category name followed by the wait block
# Handles both bolded and non-bolded versions, and different casing.
def replace_category(match):
    prefix = match.group(1) # e.g., "from ", "From **"
    suffix = match.group(3) # e.g., "drag `pico_wait`"
    return prefix + "Smart IO" + suffix

# Regex to match: (from or From ** or From ) + (Time) + (**, drag `pico_wait` or , drag `pico_wait`)
pattern = re.compile(r'(from \*\*|From \*\*|from |From )(Time)(\*\*, drag `pico_wait`|, drag `pico_wait`)', re.IGNORECASE)
new_content = pattern.sub(replace_category, content)

# Check for other time-related category mismatches if any
# In picofile.html, there is no category named "Time". 
# Blocking blocks like pico_wait, pico_run_delay are in "Smart IO".
# So any "from Time" is likely a mistake.

# Let's also handle the simple case: From **Time**, drag `pico_wait`
new_content = re.sub(r'(?i)from \*\*Time\*\*', 'from **Smart IO**', new_content)
new_content = re.sub(r'(?i)from Time', 'from Smart IO', new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Regex replacement complete.")
