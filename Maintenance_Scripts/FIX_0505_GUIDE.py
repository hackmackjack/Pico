import os

def fix_0505_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # The Elite Compliant Guide for Project 0505 (Interactive Digital Art)
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
  *   From **Smart IO**, drag `pico_gpio_write`.
  *   **Snap** into `start`.
  *   Set Pin to **GP16** (Red LED) and Value to **LOW**.
2.  **Configure Sensor**:
  *   The LDR on GP26 is essentially always ready for ADC reading.

**B. Main Loop Phase**
1.  **Read Sensor**:
  *   From **Variables**, set `light` to:
  *   From **Smart IO**, drag `pico_adc_read` (Pin GP26).
  *   **Snap** into `pico_forever`.
2.  **Threshold Logic**:
  *   From **Logic**, drag `if_else`.
  *   **Snap** below variables block.
  *   Condition: From **Logic**, drag comparison block (`<`).
      *   Left: `light` (Variable).
      *   Right: `number` 20000 (Adjust based on ambient room light).
3.  **Night Mode (Action)**:
  *   **Snap** into the "DO" (True) slot.
  *   From **Smart IO**, drag `pico_gpio_write` (GP16).
  *   Set Value to **HIGH** (Turn on Art).
  *   *Optional: You can add a `count_with` loop here to fade colors.*
4.  **Day Mode (Safety)**:
  *   **Snap** into the "ELSE" (False) slot.
  *   From **Smart IO**, drag `pico_gpio_write` (GP16).
  *   Set Value to **LOW** (Turn off).
5.  **Sampling Delay**:
  *   From **Time**, wait 0.5 seconds.
  *   **Snap** at the bottom of the loop."""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "## 5. Project 0505: Interactive Digital Art"
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
        
    print("Fixed Project 0505 Guide.")

if __name__ == "__main__":
    fix_0505_guide()
