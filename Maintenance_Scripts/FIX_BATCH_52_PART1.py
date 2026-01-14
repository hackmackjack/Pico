import os

def fix_batch_52():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # 1. Project 0511: Countdown
    g0511 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Display**:
  *   From **Display**, drag `pico_oled_init`.
  *   **Snap** into `start`.
  *   Set SDA=8, SCL=9.

**B. Main Loop Phase**
1.  **Frame 1 (Three)**:
  *   From **Display**, drag `pico_oled_clear`. **Snap** into loop.
  *   From **Display**, drag `pico_oled_text`.
      *   Text: "3", X: 60, Y: 30.
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 1s.
2.  **Frame 2 (Two)**:
  *   **Snap** below previous blocks.
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_text`("2", 60, 30).
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 1s.
3.  **Frame 3 (One)**:
  *   **Snap** below.
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_text`("1", 60, 30).
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 1s."""

    # 2. Project 0512: Blinking Face
    g0512 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
  *   From **Display**, drag `pico_oled_init` (SDA=8, SCL=9).
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Draw Open Face**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_rect` (X=30, Y=10, W=68, H=44). (Face).
  *   From **Display**, drag `pico_oled_circle` (X=45, Y=25, R=5). (Left Eye).
  *   From **Display**, drag `pico_oled_circle` (X=80, Y=25, R=5). (Right Eye).
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 2s.
  *   **Snap** all inside `pico_forever`.
2.  **Draw Wink Face**:
  *   From **Display**, drag `pico_oled_clear`. **Snap** below.
  *   From **Display**, drag `pico_oled_rect` (Face).
  *   From **Display**, drag `pico_oled_circle` (Left Eye).
  *   From **Display**, drag `pico_oled_line` (X1=75, Y1=25, X2=85, Y2=25). (Wink).
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 0.5s."""

    # 3. Project 0513: Etch-a-Sketch
    g0513 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare Canvas**:
  *   From **Display**, drag `pico_oled_init`. **Snap** into `start`.
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_show`.

**B. Main Loop Phase**
1.  **Read Inputs & Map**:
  *   From **Variables**, set `x` to:
      *   Map `pico_adc_read(26)` from 0-65535 to 0-127.
  *   From **Variables**, set `y` to:
      *   Map `pico_adc_read(27)` from 0-65535 to 0-63.
  *   **Snap** into `pico_forever`.
2.  **Draw Point**:
  *   From **Display**, drag `pico_oled_pixel`.
  *   Set X to `x`, Y to `y`.
  *   **Snap** below variables.
3.  **Update Screen**:
  *   From **Display**, drag `pico_oled_show`.
  *   *Note: Do NOT clear the screen if you want trails.*"""

    # 4. Project 0514: Screensaver (Bouncing Ball)
    g0514 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Vars**:
  *   Set `x=64`, `y=32` (Center).
  *   Set `dx=2`, `dy=2` (Velocity).
  *   **Snap** after `pico_oled_init`.

**B. Main Loop Phase**
1.  **Clear & Draw**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_circle` (X=`x`, Y=`y`, R=3).
  *   From **Display**, `pico_oled_show`.
  *   **Snap** into loop.
2.  **Move**:
  *   Set `x` to `x + dx`.
  *   Set `y` to `y + dy`.
3.  **Bounce X**:
  *   If `x < 2` OR `x > 125`:
      *   Set `dx` to `dx * -1`.
4.  **Bounce Y**:
  *   If `y < 2` OR `y > 61`:
      *   Set `dy` to `dy * -1`."""

    # 5. Project 0515: Loading Bar
    g0515 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: `pico_oled_init`.

**B. Main Loop Phase**
1.  **Reset**:
  *   From **Functions**, call `pico_oled_clear`.
2.  **Animate Bar**:
  *   From **Loops**, drag `count_with` (width from 0 to 128 by 5).
  *   **Snap** into loop.
  *   From **Display**, `pico_oled_rect` (filled).
      *   X=0, Y=28, W=`width`, H=8.
  *   From **Display**, `pico_oled_text`.
      *   Text: "Loading...", X=30, Y=10.
  *   From **Display**, `pico_oled_show`.
  *   Wait 0.1s."""

    # ... (I will implement 516-520 as well, but splitting for now to ensure applied correctly)
    
    replacements = {
        "## 1. Project 0511": (g0511, "### 9. Execution Flow"),
        "## 2. Project 0512": (g0512, "### 9. Execution Flow"),
        "## 3. Project 0513": (g0513, "### 9. Execution Flow"),
        "## 4. Project 0514": (g0514, "### 9. Execution Flow"),
        "## 5. Project 0515": (g0515, "### 9. Execution Flow")
    }

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for header, (new_text, end_marker) in replacements.items():
        start_idx = content.find(header)
        if start_idx == -1: 
             print(f"Skipping {header} - Not Found")
             continue

        guide_header = "### 8. Step-by-Step Guide"
        guide_start = content.find(guide_header, start_idx)
        guide_end = content.find(end_marker, guide_start)
        
        pre = content[:guide_start]
        post = content[guide_end:]
        content = pre + new_text + "\n\n" + post

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed Batch 52 (Part 1: 0511-0515).")

if __name__ == "__main__":
    fix_batch_52()
