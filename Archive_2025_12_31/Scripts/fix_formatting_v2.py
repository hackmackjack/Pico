
import re

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def fix_whitespace():
    print(f"Reading {DOC_PATH}...")
    with open(DOC_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)
    
    # 1. Collapse 3+ newlines to 2 (Standard Paragraph gap)
    # This handles \n\n\n -> \n\n
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 2. Fix Tables: Remove ANY blank line between table rows
    # Pattern: | ... | \n \n | ... |
    # We want: | ... | \n | ... |
    # Regex lookbehind is tricky with variable length, so let's use a specific table pattern replacement
    # Iterate until stable? 
    # Or just replace `|\n\n|` with `|\n|` ? 
    # Tables rows start with `|`.
    # Let's try to match `(\|[^\n]+)\n\s*\n+(\|)` and replace with `\1\n\2`
    
    # Repeat a few times to handle multiple blank lines gap
    for _ in range(3):
        content = re.sub(r'(\|\s*[^\n]+\s*\|)\n\s*\n+(\|)', r'\1\n\2', content)

    # 3. Fix Code Blocks: Remove double spacing?
    # Determine if code blocks have `\n\n` between lines.
    # We don't want to destroy INTENTIONAL blank lines in code.
    # But if EVERY line has a blank, that's wrong.
    # Current view showed: `import machine\n\n\nimport time` -> This is caught by Step 1.
    # Step 1 fixes `\n\n\n` to `\n\n`.
    
    # Let's write it back.
    
    new_len = len(content)
    print(f"Reduced size from {original_len} to {new_len} chars.")
    
    with open(DOC_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    fix_whitespace()
