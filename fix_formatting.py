import re

def fix_formatting():
    filepath = "Documentation/Docs_0101_0200.md"
    with open(filepath, 'r') as f: content = f.read()

    # Fix S6 'From'
    # Pattern: *   From **Cat**, drag **`Block`**
    # Target: * **from Cat, drag `Block`**

    # 1. Lowercase From
    content = content.replace("*   From", "* **from")
    content = content.replace("* From", "* **from")

    # 2. Fix Bold/Space around Category
    # This regex is complex, refer to previous 'bulk_fix_s6' logic if needed.
    # Simple search/replace is safer for bulk:
    # We want: * **from Category, drag `block`**
    # Input might be: * From **Category**, drag `block`

    # Correcting the pattern to capture category and block
    # Note: The input file likely has "* From Category, drag `block`" or "* From **Category**, drag `block`"
    # We normalized "From" to "**from" above.

    # Fix clumping in S8
    content = re.sub(r"([^\n])\s+(B\. Main Loop Phase)", r"\1\n\n\2", content)
    content = re.sub(r"([^\n])\s+(\d+\.\s+\*\*)", r"\1\n\2", content)

    with open(filepath, 'w') as f: f.write(content)
    print("Formatting Fixed.")

if __name__ == "__main__":
    fix_formatting()
