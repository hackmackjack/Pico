import re

def fix_0400_standard():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. FIX HEADERS (Remove Emojis and standardise)
    # Map 1️⃣ -> 1., 2️⃣ -> 2., etc.
    # Also handle the generic "Project" headers if they have emojis.
    
    # List of specific replacements for headers
    header_map = {
        "## 1️⃣ Project": "## 1. Project",
        "### 2️⃣ Learning Objective": "### 2. Learning Objective",
        "### 3️⃣ Concepts Introduced": "### 3. Concepts Introduced",
        "### 4️⃣ Hardware Required": "### 4. Hardware Required",
        "### 5️⃣ Wiring / Interfaces": "### 5. Wiring / Interfaces",
        "### 8️⃣ Step-by-Step Guide": "### 8. Step-by-Step Guide",
        # Check if 6 and 7 have emojis in the source (Viewed 0401, 6 and 7 seemed to be normal text "6. Blocks Used")
        # But let's be safe.
        "### 6️⃣ Blocks Used": "### 6. Blocks Used",
        "### 7️⃣ Variables": "### 7. Variables",
        # 9, 10, 11, 12 might be standard numbers already based on 0401 view, but let's check.
        # In 0401 view: "### 9. Execution Flow", "### 10. Generated Code"... they seem clean.
    }
    
    print("Fixing Headers...")
    for bad, good in header_map.items():
        content = content.replace(bad, good)
        
    # Also generic emoji remover for headers just in case?
    # content = re.sub(r'# (1️⃣|2️⃣|3️⃣|4️⃣|5️⃣|6️⃣|7️⃣|8️⃣|9️⃣|🔟)', ...
    # But direct replace is safer.

    # 2. FIX CATEGORIES (Legacy -> Elite)
    # From **Pin Access** -> From **Smart IO**
    # From **Timing** -> From **Time**
    # From **Inputs** -> From **Smart IO**
    # From **Loops** (This is already standard)
    # From **Variables** (Standard)
    # From **Logic** (Standard)
    # From **Math** (Standard)
    # From **Text** (Standard -> But sometimes "Display" is used for text? No, Text is category)
    
    category_map = {
        "From **Pin Access**": "From **Smart IO**",
        "From **Timing**": "From **Time**",
        "From **Inputs**": "From **Smart IO**",
    }

    print("Fixing Categories...")
    for old, new in category_map.items():
        content = content.replace(old, new)
        
    # 3. FIX BLOCK NAMES (Legacy descriptive -> Elite explicit)
    # This is harder to verify without breaking things.
    # Ex: `Setup Pin:[16] as OUTPUT` vs `pico_gpio_write`.
    # Let's start with structural fixes first.

    # 4. FIX FORMATTING (Bullet style)
    # 0401 has:
    # *   **A. Initialization Phase**
    #     *   From ...
    # Elite standard is:
    # **A. Initialization Phase**
    # 1.  **Step Name**:
    #   *   From ...
    
    # This bullet fix is complex regex.
    # Let's try to remove the leading `*   **A.` and make it `**A.`
    content = re.sub(r'^\*\s+\*\*([A-Z])\. ', r'**\1. ', content, flags=re.MULTILINE)
    
    # Remove one level of indentation for the subsequent lines?
    # If content was:
    # *   **A. Init**
    #     *   From X
    # It becomes:
    # **A. Init**
    #     *   From X
    # Elite expectation:
    # **A. Init**
    # 1.  **Step**:
    #   *   From X
    
    # The legacy format lacks the "Step 1" wrapper often.
    # Or maybe it has it?
    # 0401 view:
    # *   **A. Initialization Phase**
    #     *   From **Pin Access**...
    # It jumps straight to instructions.
    
    # We might leave the structure as "bulleted list of instructions" for now,
    # as injecting "1. Step Name" requires inventing step names.
    # Unless strictly required, we'll keep the instruction list but fix the indentation if possible.
    # Let's just fix the Categories and Headers for now.
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Standardization Complete.")

if __name__ == "__main__":
    fix_0400_standard()
