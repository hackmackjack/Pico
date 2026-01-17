import re

DOC_FILE = "Documentation/Docs_0101_0200.md"

def final_polish():
    with open(DOC_FILE, 'r') as f: content = f.read()

    # 1. Project 0198 - Update Names
    # From Smart IO, drag `pico_time_ms` -> From **Smart IO**, drag **`pico_ticks_ms`**
    content = content.replace("`pico_time_ms`", "**`pico_ticks_ms`**")

    # 2. Project 0200 - Update Modulo format
    # From Variables, set `a_hit` to (timer % 300 == 0) -> ... to **Math** Remainder of `timer` ÷ 300 == 0
    # Actually, let's keep it descriptive but use the block name "remainder of"

    content = content.replace("(timer % 300 == 0)", "**Math** remainder of **`timer`** ÷ 300 == 0")
    content = content.replace("(timer % 200 == 0)", "**Math** remainder of **`timer`** ÷ 200 == 0")

    # 3. Check for any "From" capitalization issues in S8 again (just in case)
    # The user said "From" must be lowercase in S6.
    # In S8, it is usually "From".
    # Ensure S6 is lowercase.

    # Re-running S6 fix on specific projects 0198/0200 just in case manual edit messed it up.
    # But I didn't touch S6 in manual edit.

    # 4. Remove any double bolding in S8
    content = content.replace("**from **", "From **")
    content = content.replace("**From **", "From **")

    # 5. Ensure Phase Headers have newlines
    content = re.sub(r"([^\n])(\*\*A\. Initialization Phase\*\*)", r"\1\n\n\2", content)
    content = re.sub(r"([^\n])(\*\*B\. Main Loop Phase\*\*)", r"\1\n\n\2", content)

    with open(DOC_FILE, 'w') as f: f.write(content)
    print("Documentation Polished.")

if __name__ == "__main__":
    final_polish()
