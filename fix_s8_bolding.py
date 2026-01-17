import re

def fix_s8_bolding():
    filepath = "Documentation/Docs_0101_0200.md"
    with open(filepath, 'r') as f: content = f.read()

    # Fix the double bolding artifact caused by global replace
    # Pattern: * **from **Category** -> * From **Category**
    # We assume S8 instructions start with * From (Capital F for sentences)

    new_content = content.replace("* **from **", "* From **")

    # Also check if there are cases like "* **from Smart IO" (single bold) in S8
    # If we want S8 to be "From **Smart IO**", we need to fix those too if they exist.
    # But expand_s8_batch generated "From **Smart IO**".
    # fix_formatting changed it to "**from **Smart IO**".
    # So replacing "**from **" with "From " should fix it.
    # Wait, fix_formatting did: replace("* From", "* **from")
    # So "* From **Smart" -> "* **from **Smart"
    # So replace "* **from **" with "* From **" restores it.

    with open(filepath, 'w') as f: f.write(new_content)
    print("S8 Bolding Fixed.")

if __name__ == "__main__":
    fix_s8_bolding()
