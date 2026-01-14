import os

def fix_0523_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # The Elite Compliant Guide for Project 0523
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
  *   From **Smart IO**, configure GP14 and GP15 as **Input (Pull-Down)**.
  *   From **Smart IO**, configure GP16, GP17, GP18, GP19 as **Output**.
  *   **Snap** these into the `start` block.
2.  **Initialize Variables**:
  *   From **Variables**, set `count` to 0.
  *   **Snap** at the bottom of the Initialization stack.

**B. Main Loop Phase**
1.  **Increment Logic**:
  *   From **Logic**, drag `if_do`.
  *   Condition: From **Logic**, drag `and` block.
      *   Left: **Smart IO** `read_pin(14)` (Up Button) is High.
      *   Right: `count` < 15 (Max limit).
  *   **Snap** into `pico_forever` loop.
  *   **Action**: From **Variables**, `change count by 1`.
  *   **Wait**: From **Time**, drag `pico_wait(0.2)` (Debounce).
2.  **Decrement Logic**:
  *   From **Logic**, drag `if_do`.
  *   Condition: From **Logic**, drag `and` block.
      *   Left: **Smart IO** `read_pin(15)` (Down Button) is High.
      *   Right: `count` > 0 (Min limit).
  *   **Snap** below previous `if_do`.
  *   **Action**: From **Variables**, `change count by -1`.
  *   **Wait**: From **Time**, drag `pico_wait(0.2)`.
3.  **Bit 0 (Value 1) Display**:
  *   From **Logic**, drag `if_else`.
  *   Condition: (`count` & 1) > 0. (Use **Math** `bitwise_and`).
  *   **Snap** below decrement logic.
  *   **If True**: Set GP16 HIGH. **Else**: Set GP16 LOW.
4.  **Bit 1 (Value 2) Display**:
  *   From **Logic**, drag `if_else`.
  *   Condition: (`count` & 2) > 0.
  *   **Snap** below previous check.
  *   **If True**: Set GP17 HIGH. **Else**: Set GP17 LOW.
5.  **Bit 2 (Value 4) Display**:
  *   From **Logic**, drag `if_else`.
  *   Condition: (`count` & 4) > 0.
  *   **Snap** below previous check.
  *   **If True**: Set GP18 HIGH. **Else**: Set GP18 LOW.
6.  **Bit 3 (Value 8) Display**:
  *   From **Logic**, drag `if_else`.
  *   Condition: (`count` & 8) > 0.
  *   **Snap** below previous check.
  *   **If True**: Set GP19 HIGH. **Else**: Set GP19 LOW."""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Identify the block to replace
    # We look for the start of the guide and the start of the next section (Execution Flow)
    start_marker = "## 1. Project 0523: Manual Binary Counter Control"
    end_marker = "### 9. Execution Flow"
    
    # We need to target the SPECIFIC 0523 Section 8
    # Since regex is risky with duplicates, let's find the 0523 header index
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Project 0523 not found")
        return

    # Find Section 8 *after* the header
    guide_header = "### 8. Step-by-Step Guide"
    guide_start = content.find(guide_header, start_idx)
    
    # Find Section 9 *after* the guide
    guide_end = content.find(end_marker, guide_start)
    
    if guide_start == -1 or guide_end == -1:
        print("Could not delineate Guide section for 0523")
        return
        
    # Replace
    pre = content[:guide_start]
    post = content[guide_end:]
    
    new_content = pre + new_guide + "\n\n" + post
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Fixed Project 0523 Guide.")

if __name__ == "__main__":
    fix_0523_guide()
