import glob
import ast
import re

def verify_markdown_code_blocks():
    files = sorted(glob.glob("Pico_500_Batch_*.md"))
    error_count = 0

    print(f"Verifying {len(files)} files...")

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find python code blocks
        # Matches ```python ... ```
        code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)

        for i, code in enumerate(code_blocks):
            try:
                ast.parse(code)
            except SyntaxError as e:
                print(f"Syntax Error in {filename}, Block {i+1}:")
                print(f"  Line {e.lineno}: {e.msg}")
                # Print a snippet of the code
                lines = code.split('\n')
                if 0 <= e.lineno-1 < len(lines):
                    print(f"  Code: {lines[e.lineno-1].strip()}")
                error_count += 1
            except Exception as e:
                print(f"Error parsing {filename}, Block {i+1}: {e}")
                error_count += 1

    if error_count == 0:
        print("SUCCESS: All code blocks passed syntax check.")
    else:
        print(f"FAILURE: Found {error_count} syntax errors.")

if __name__ == "__main__":
    verify_markdown_code_blocks()
