
import re

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def polish_documentation():
    print(f"Reading {DOC_PATH}...")
    with open(DOC_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Normalize Header Spacing (Pre-existing)
    content = re.sub(r'\n+\s*(#+)', r'\n\n\1', content)
    
    # 2. Compact Tables (Pre-existing)
    for _ in range(3):
        content = re.sub(r'(\|\s*[^\n]+\|)\n\s*\n+(\|)', r'\1\n\2', content)

    # 3. Compact Code Blocks (Pre-existing)
    def compact_code_match(match):
        code_block = match.group(0)
        lines = code_block.splitlines()
        new_lines = []
        for line in lines:
            if line.strip() == "" and not line.startswith("```"):
                continue
            new_lines.append(line)
        return "\n".join(new_lines)

    content = re.sub(r'```.*?```', compact_code_match, content, flags=re.DOTALL)

    # 4. Global whitespace cleanup (Pre-existing)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 5. NEW: Compact Bullet Lists
    # Look for: Line starting with * or -, followed by newline, spaces, newline, followed by * or -
    # We want to remove the blank line.
    # Logic: If a line matches `^\s*[\*\-]\s` and the next non-empty line also matches `^\s*[\*\-]\s`,
    # then they should probably be adjacent (unless they are long paragraphs, but for this doc they are definitions).
    
    # Regex approach for specific pattern seen in screenshot:
    # `*   **Text**: Text` followed by `\n` `\n` `*   **Text`
    
    # Let's try recursive replacement similar to tables.
    # Pattern: (Bullet Line) \n \n (Bullet Line) -> \1 \n \2
    # Bullet Line regex: `^\s*[\*\-]\s+.*$` (multiline)
    
    # Note: markdown lists use `*` or `-`. The doc uses `*`.
    
    bullet_regex = r'(\n\s*[\*\-].+?)\n\s*\n+(\s*[\*\-])'
    # Group 1: The first bullet line (starting with newline to anchor)
    # Group 2: The start of the next bullet line
    
    # We need to loop because regex might overlap or miss sequential ones.
    for _ in range(5):
        # We replace with `\1\n\2`
        content = re.sub(bullet_regex, r'\1\n\2', content)

    print(f"Writing polished content...")
    with open(DOC_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    polish_documentation()
