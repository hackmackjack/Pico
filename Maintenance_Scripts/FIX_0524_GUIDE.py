import os

def fix_0524_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # The Elite Compliant Guide for Project 0524
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
  *   From **Smart IO**, drag `pico_gpio_write` blocks for GP16, 17, 18, 19, 20, and 21.
  *   **Snap** them into the `start` block.
2.  **Initialize Variables**:
  *   From **Variables**, set `pos` to 0 (Start Position).
  *   From **Variables**, set `dir` to 1 (Direction Right).
  *   **Snap** below the GPIO blocks.

**B. Main Loop Phase**
1.  **Clear All LEDs (Reset Frame)**:
  *   From **Smart IO**, set GP16-GP21 to **LOW**.
  *   **Snap** inside `pico_forever` loop.
2.  **Light Active LED**:
  *   From **Logic**, drag `if_else_if` (Expand to 6 checks).
  *   **Check 0**: If `pos` == 0, **Smart IO** write GP16 HIGH.
  *   **Check 1**: If `pos` == 1, **Smart IO** write GP17 HIGH.
  *   **Check 2**: If `pos` == 2, **Smart IO** write GP18 HIGH.
  *   **Check 3**: If `pos` == 3, **Smart IO** write GP19 HIGH.
  *   **Check 4**: If `pos` == 4, **Smart IO** write GP20 HIGH.
  *   **Check 5**: If `pos` == 5, **Smart IO** write GP21 HIGH.
  *   **Snap** below the clear block.
3.  **Update Position**:
  *   From **Variables**, `change pos by dir`.
  *   **Snap** after the big `if/else` block.
4.  **Bounce Logic (Right Edge)**:
  *   From **Logic**, drag `if_do`.
  *   Condition: `pos` == 5.
  *   **Action**: From **Variables**, set `dir` to -1.
  *   **Snap** below position update.
5.  **Bounce Logic (Left Edge)**:
  *   From **Logic**, drag `if_do`.
  *   Condition: `pos` == 0.
  *   **Action**: From **Variables**, set `dir` to 1.
  *   **Snap** below previous logic.
6.  **Animation Delay**:
  *   From **Time**, drag `pico_wait`.
  *   Set value to 0.1 seconds.
  *   **Snap** at the bottom of the loop."""

    # Same logic as before to find and replace
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "## 1. Project 0524: Binary Counter Sequences"
    end_marker = "### 9. Execution Flow"
    
    start_idx = content.find(start_marker)
    if start_idx == -1: return

    guide_header = "### 8. Step-by-Step Guide"
    guide_start = content.find(guide_header, start_idx)
    guide_end = content.find(end_marker, guide_start)
    
    pre = content[:guide_start]
    post = content[guide_end:]
    
    new_content = pre + new_guide + "\n\n" + post
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Fixed Project 0524 Guide.")

if __name__ == "__main__":
    fix_0524_guide()
