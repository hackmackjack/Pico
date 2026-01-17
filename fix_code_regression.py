import re

DOC_FILE = "Documentation/Docs_0101_0200.md"

def fix_code_regression():
    with open(DOC_FILE, 'r') as f: content = f.read()

    # Target Project 0200 Code Section
    start_marker = "### 10. Generated Code\n```python\nfrom machine import Pin"

    # We look for the corrupted lines in the code block context
    # Note: re.sub global was bad. We need specific fix.

    # The corrupted pattern:
    # a_hit = **Math** remainder of **`timer`** ÷ 300 == 0
    # b_hit = **Math** remainder of **`timer`** ÷ 200 == 0

    # The correct pattern:
    # a_hit = (timer % 300 == 0)
    # b_hit = (timer % 200 == 0)

    # Find the specific block for 0200
    p200_start = content.find("## Project 0200")
    if p200_start == -1:
        print("Error: Project 0200 not found")
        return

    # Extract the chunk for 0200 to work on
    p200_chunk = content[p200_start:]

    # Identify code block start
    code_start = p200_chunk.find("```python")
    if code_start == -1:
        print("Error: Code block not found in 0200")
        return

    # Replace specifically in this chunk
    new_chunk = p200_chunk.replace(
        "a_hit = **Math** remainder of **`timer`** ÷ 300 == 0",
        "a_hit = (timer % 300 == 0)"
    )
    new_chunk = new_chunk.replace(
        "b_hit = **Math** remainder of **`timer`** ÷ 200 == 0",
        "b_hit = (timer % 200 == 0)"
    )

    # Reassemble file
    new_content = content[:p200_start] + new_chunk

    with open(DOC_FILE, 'w') as f: f.write(new_content)
    print("Fixed code regression in Project 0200.")

if __name__ == "__main__":
    fix_code_regression()
