import os

def fix_batch_51_remaining():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # Project 0507 (Alarm System)
    g0507 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18) for Outputs.
  *   From **Smart IO**, configure GP14 and GP15 as **Input (Pull-Down)**.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Logic Check (Priority)**:
  *   From **Logic**, drag `if_else_if` (Expand to 3 conditions).
  *   **Snap** into `pico_forever` loop.
  *   **Cond 1 (Both)**: From **Logic**, drag `and` block. (GP14 AND GP15).
      *   Action: Set GP16 (Red) **HIGH**, GP18 (Blue) **HIGH** (Purple).
  *   **Cond 2 (A only)**: GP14 is HIGH.
      *   Action: Set GP16 (Red) **HIGH**, GP18 (Blue) **LOW**.
  *   **Cond 3 (B only)**: GP15 is HIGH.
      *   Action: Set GP16 (Red) **LOW**, GP18 (Blue) **HIGH**.
  *   **Else (None)**:
      *   Action: Set both **LOW**."""

    # Project 0508 (Game)
    g0508 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP15 (Button) and RGB Pins.

**B. Main Loop Phase**
1.  **Pick Color**:
  *   From **Variables**, set `color` to `random_integer(1, 3)`.
  *   **Snap** into `pico_forever`.
2.  **Display Color**:
  *   From **Logic**, drag `if_else_if`.
  *   If `color == 1`: Turn Red ON.
  *   If `color == 2`: Turn Green ON.
  *   If `color == 3`: Turn Blue ON.
  *   **Snap** below variable block.
3.  **Reaction Window**:
  *   From **Time**, wait 0.5s.
4.  **Check Condition**:
  *   From **Logic**, drag `if_do`.
  *   Condition: `pico_gpio_read(15)` (Button Pressed).
      *   Sub-Condition: `if color == 2` (Green).
          *   **Win**: Flash White.
      *   Else:
          *   **Lose**: Flash Red.
5.  **Reset**:
  *   Turn all LEDs OFF.
  *   From **Time**, wait 1s."""

    # Project 0509 (Day Cycle)
    g0509 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
  *   From **Smart IO**, set GP16, 17, 18 as PWM with Freq 1000.

**B. Main Loop Phase**
1.  **Sunrise (0-5s)**:
  *   From **Loops**, drag `count_with` (i from 0 to 65000 by 1000).
      *   Set Red PWM to `i`.
      *   Set Green PWM to `i / 2`.
      *   Wait 0.05s.
      *   **Snap** into `pico_forever`.
2.  **Noon (5-10s)**:
  *   From **Loops**, drag `count_with` (i from 0 to 65000 by 1000).
      *   Set Green PWM to `32000 + (i/2)`.
      *   Set Blue PWM to `i`.
      *   Wait 0.05s.
3.  **Sunset (10-15s)**:
  *   From **Loops**, drag `count_with` (i from 65000 to 0 by -1000).
      *   Set Blue PWM to `i`.
      *   Set Green PWM to `i`.
      *   Wait 0.05s.
4.  **Night (15-20s)**:
  *   From **Smart IO**, set Red/Green/Blue LOW.
  *   Wait 5s."""

    replacements = {
        "## 7. Project 0507": (g0507, "### 9. Execution Flow"),
        "## 8. Project 0508": (g0508, "### 9. Execution Flow"),
        "## 9. Project 0509": (g0509, "### 9. Execution Flow")
    }

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for header, (new_text, end_marker) in replacements.items():
        start_idx = content.find(header)
        if start_idx == -1: continue

        guide_header = "### 8. Step-by-Step Guide"
        guide_start = content.find(guide_header, start_idx)
        guide_end = content.find(end_marker, guide_start)
        
        pre = content[:guide_start]
        post = content[guide_end:]
        content = pre + new_text + "\n\n" + post

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Projects 0507, 0508, 0509.")

if __name__ == "__main__":
    fix_batch_51_remaining()
