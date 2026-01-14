import os

def fix_0504_guide():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # The Elite Compliant Guide for Project 0504 (Campfire Simulation)
    new_guide = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP18).
  *   **Snap** into `start`.
  *   Set value to **LOW** (Turn Blue OFF).

**B. Main Loop Phase**
1.  **Generate Red Flicker**:
  *   From **Smart IO**, drag `pico_pwm_write`.
  *   **Snap** into `pico_forever` loop.
  *   Set Pin to **GP16** (Red).
  *   Set Value to: From **Math**, drag `random_integer`.
      *   Min: 40000.
      *   Max: 65535.
2.  **Generate Green Flicker**:
  *   From **Smart IO**, drag `pico_pwm_write`.
  *   **Snap** below Red logic.
  *   Set Pin to **GP17** (Green).
  *   Set Value to: From **Math**, drag `random_integer`.
      *   Min: 5000 (Very dim).
      *   Max: 20000 (Dim).
      *   *Note: Keeping Green < 30% ensures the flame looks orange, not yellow-green.*
3.  **Variable Timing**:
  *   From **Time**, drag `pico_wait`.
  *   **Snap** below Green logic.
  *   Set Value to: From **Math**, drag `arithmetic` (Division).
      *   Left: `random_integer` (50, 200).
      *   Right: `number` 1000.
      *   *Explanation: This creates a random wait between 0.05s and 0.2s.*"""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "## 4. Project 0504: Digital Art Sequences"
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
        
    print("Fixed Project 0504 Guide.")

if __name__ == "__main__":
    fix_0504_guide()
