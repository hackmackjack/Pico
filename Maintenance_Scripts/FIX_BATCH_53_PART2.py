import os

def fix_batch_53_part2():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # Project 0525 (Binary Clock)
    g0525 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
  *   From **Smart IO**, drag `pico_gpio_write` blocks for GP16, 17, 18, 19, 20, 21. Snap into `start`.
2.  **Initialize Variables**:
  *   From **Variables**, set `seconds` to 0.

**B. Main Loop Phase**
1.  **Display Bit 0**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 1 > 0`.
  *   **Snap** into `pico_forever`.
  *   If True: `pico_gpio_write` (16) HIGH. Else: LOW.
2.  **Display Bit 1**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 2 > 0`.
  *   If True: `pico_gpio_write` (17) HIGH. Else: LOW.
3.  **Display Bit 2**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 4 > 0`.
  *   If True: `pico_gpio_write` (18) HIGH. Else: LOW.
4.  **Display Bit 3**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 8 > 0`.
  *   If True: `pico_gpio_write` (19) HIGH. Else: LOW.
5.  **Display Bit 4**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 16 > 0`.
  *   If True: `pico_gpio_write` (20) HIGH. Else: LOW.
6.  **Display Bit 5**:
  *   From **Logic**, drag `if_else`. Condition: `seconds & 32 > 0`.
  *   If True: `pico_gpio_write` (21) HIGH. Else: LOW.
7.  **Update Time**:
  *   From **Variables**, change `seconds` by 1.
  *   From **Logic**, if `seconds >= 60`:
      *   Set `seconds` to 0.
  *   From **Time**, wait 1s."""

    # Project 0526 (Parity)
    g0526 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
  *   From **Smart IO**, configure GP14, 15, 16 as Inputs (Pull-Down).
  *   From **Smart IO**, configure GP17 as Output.

**B. Main Loop Phase**
1.  **Sum Bits**:
  *   From **Variables**, set `total` to 0.
  *   **Snap** into `pico_forever`.
  *   From **Logic**, if `pico_gpio_read(14)`: Change `total` by 1.
  *   From **Logic**, if `pico_gpio_read(15)`: Change `total` by 1.
  *   From **Logic**, if `pico_gpio_read(16)`: Change `total` by 1.
2.  **Check Parity**:
  *   From **Logic**, drag `if_else`.
  *   Condition: From **Math**, `is_even(total)`.
  *   **Snap** below sums.
  *   **If True (Even)**:
      *   From **Smart IO**, set GP17 to **LOW**.
  *   **Else (Odd)**:
      *   From **Smart IO**, set GP17 to **HIGH**."""

    # Project 0527 (Overflow Alarm)
    g0527 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (Btn) In, GP15 (Bzr) Out, GP16-19 (LEDs) Out.
2.  **Init**: `count = 0`.

**B. Main Loop Phase**
1.  **Handle Button**:
  *   From **Logic**, if `pico_gpio_read(14)`:
      *   Change `count` by 1.
      *   From **Time**, wait 0.2s.
      *   **Snap** into `pico_forever`.
2.  **Check Overflow**:
  *   From **Logic**, if `count > 15`:
      *   From **Smart IO**, `pico_buzzer_beep` (GP15, Duration=1s).
      *   From **Variables**, set `count` to 0.
3.  **Update LEDs**:
  *   (Repeat the bitwise display logic for GP16-19 as seen in previous projects).
  *   **Snap** below overflow check."""

    # Project 0528 (Game)
    g0528 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16-19 Outputs.

**B. Main Loop Phase**
1.  **New Round**:
  *   From **Variables**, set `target` to `random_integer(1, 15)`.
  *   **Snap** into `pico_forever`.
2.  **Show Pattern**:
  *   Use Bitwise Logic (If `target & 1` -> GP16 On, etc) to display `target`.
3.  **Prompt**:
  *   From **Text**, print "Enter number logic not supported in blocks, use Terminal".
  *   *Note: This specific project relies heavily on Python input() which has no direct Block equivalent in standard lib, simulating visual logic instead.*
4.  **Wait**: 5 seconds."""

    # Project 0529 (BCD Counter)
    g0529 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP10-13 (Ones), GP16-19 (Tens) as Outputs.

**B. Main Loop Phase**
1.  **Count Loop**:
  *   From **Loops**, `count_with` (i from 0 to 99).
  *   **Snap** into `pico_forever`.
2.  **Calculate Digits**:
  *   Set `ones` to `i % 10`.
  *   Set `tens` to `math_floor(i / 10)`.
3.  **Display Ones**:
  *   Process `ones` bits 1,2,4,8 to GP10,11,12,13.
4.  **Display Tens**:
  *   Process `tens` bits 1,2,4,8 to GP16,17,18,19.
5.  **Wait**:
  *   From **Time**, wait 0.5s."""

    # Project 0530 (Mastering)
    g0530 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: All 8 LEDs.

**B. Main Loop Phase**
1.  **Larson Scanner**:
  *   From **Loops**, `count_with` (pos from 0 to 7).
  *   **Snap** into `pico_forever`.
  *   **Clear All**.
  *   **Set Bit**:
      *   If `pos < 4`: Turn ON GP(10+pos).
      *   Else: Turn ON GP(16 + (pos-4)).
  *   **Wait**: 0.1s.
2.  **Reverse**:
  *   Repeat loop from 7 down to 0."""

    replacements = {
        "## 1. Project 0525": (g0525, "### 9. Execution Flow"),
        "## 1. Project 0526": (g0526, "### 9. Execution Flow"), # Header fix needed maybe? Project 1 again?
        "## 1. Project 0527": (g0527, "### 9. Execution Flow"),
        "## 1. Project 0528": (g0528, "### 9. Execution Flow"),
        "## 1. Project 0529": (g0529, "### 9. Execution Flow"),
        "## 1. Project 0530": (g0530, "### 9. Execution Flow") # If exists
    }
    
    # Note: Previous verification showed headers matching "## 1. Project 0526". 
    # This indicates NUMBERING ISSUES in Batch 53 as well (They might all be labeled "1").
    # The `FINAL_ASSEMBLY.py` I ran earlier (Step 2018) claimed to fix numbering (## rel_index).
    # But if REGENERATE_BATCH_53 or BUILD_BATCH53 didn't have correct relative indices in the text, and I patched over it?
    
    # Let's assume the headers are correct (## 5. Project 0525) thanks to FINAL_ASSEMBLY processing of the raw text if I used it.
    # WAIT. I injected Step 8 *into* the file. 
    # But earlier I saw `## 1. Project 0521` in the Bridge Repair.
    
    # Let's search by Project ID to be safe.
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    import re
    
    for pid, (new_text, end_marker) in [
        ("0525", (g0525, "### 9. Execution Flow")),
        ("0526", (g0526, "### 9. Execution Flow")),
        ("0527", (g0527, "### 9. Execution Flow")),
        ("0528", (g0528, "### 9. Execution Flow")),
        ("0529", (g0529, "### 9. Execution Flow")),
        ("0530", (g0530, "### 9. Execution Flow"))
    ]:
        # Regex find the header: ## <Digit>. Project <PID>
        match = re.search(rf"## \d+\. Project {pid}", content)
        if not match:
            print(f"Project {pid} Not Found")
            continue
            
        header_idx = match.start()
        
        guide_header = "### 8. Step-by-Step Guide"
        guide_start = content.find(guide_header, header_idx)
        guide_end = content.find(end_marker, guide_start)
        
        if guide_start == -1 or guide_end == -1:
            print(f"Guide not found for {pid}")
            continue

        pre = content[:guide_start]
        post = content[guide_end:]
        content = pre + new_text + "\n\n" + post

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Batch 53 Part 2 (0525-0530).")

if __name__ == "__main__":
    fix_batch_53_part2()
