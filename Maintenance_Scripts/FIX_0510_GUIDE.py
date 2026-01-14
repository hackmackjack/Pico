import os

def fix_0510_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # The Elite Compliant Guide for Project 0510 (Function-based Art)
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
  *   From **Smart IO**, drag `pico_pwm_write` blocks for GP16, 17, 18.
  *   **Snap** into `start`.
  *   Set initial values to 0.

**B. Function Definition Phase**
1.  **Create Function**:
  *   From **Functions**, drag `to_do_something` block.
  *   Rename it to `set_purple`.
  *   Click gear icon to add input `intensity`.
2.  **Function Logic**:
  *   From **Variables**, set `scaled_val` to `intensity * 655`. (Use **Math**).
  *   **Snap** inside function.
  *   From **Smart IO**, set GP16 (Red) PWM to `scaled_val`.
  *   From **Smart IO**, set GP18 (Blue) PWM to `scaled_val`.
  *   From **Smart IO**, set GP17 (Green) PWM to 0.

**C. Main Loop Phase**
1.  **Sweep Up**:
  *   From **Loops**, drag `count_with` (i from 0 to 100).
  *   **Snap** into `pico_forever`.
  *   From **Functions**, call `set_purple` with input `i`.
  *   From **Time**, wait 0.01s.
2.  **Sweep Down**:
  *   From **Loops**, drag `count_with` (i from 100 to 0 by -1).
  *   **Snap** below previous loop.
  *   From **Functions**, call `set_purple` with input `i`.
  *   From **Time**, wait 0.01s."""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate Project 0510
    start_marker = "## 10. Project 0510: Mastering Digital Art"
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
        
    print("Fixed Project 0510 Guide.")

if __name__ == "__main__":
    fix_0510_guide()
