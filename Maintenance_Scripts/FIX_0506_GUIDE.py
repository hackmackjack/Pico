import os

def fix_0506_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # The Elite Compliant Guide for Project 0506 (Smart Digital Art Switch)
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16 Red). Snap into `start`.
  *   From **Smart IO**, drag `pico_pwm_write` (GP18 Blue). Snap below.
  *   From **Smart IO**, drag `pico_gpio_read` (GP15 Switch) to ensure it is available.

**B. Main Loop Phase**
1.  **Check Switch Mode**:
  *   From **Logic**, drag `if_else`.
  *   Condition: **Smart IO** `pico_gpio_read`(15) == HIGH.
  *   **Snap** into `pico_forever` loop.
2.  **Energy Mode (Red Flash)**:
  *   **Snap** into "DO" (True) section.
  *   From **Smart IO**, turn GP16 (Red) **HIGH**.
  *   From **Time**, wait 0.1 seconds.
  *   From **Smart IO**, turn GP16 (Red) **LOW**.
  *   From **Time**, wait 0.1 seconds.
3.  **Calm Mode (Blue Fade)**:
  *   **Snap** into "ELSE" (False) section.
  *   From **Loops**, drag `count_with` (i from 0 to 65000 by 1000).
      *   From **Smart IO**, set GP18 PWM to variable `i`.
      *   From **Time**, wait 0.01s.
      *   **Snap** inside the count loop.
  *   From **Loops**, drag `count_with` (i from 65000 to 0 by -1000).
      *   From **Smart IO**, set GP18 PWM to variable `i`.
      *   From **Time**, wait 0.01s.
      *   **Snap** inside the second count loop."""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate Project 0506
    start_marker = "## 6. Project 0506: Smart Digital Art Switch"
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
        
    print("Fixed Project 0506 Guide.")

if __name__ == "__main__":
    fix_0506_guide()
