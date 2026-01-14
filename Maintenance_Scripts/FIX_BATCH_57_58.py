import os
import re

def fix_batch_57_58():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # --- BATCH 57: OLED SHAPES 3 (0561-0570) ---
    
    # 0561: Intro OLED Shapes
    g0561 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear Screen**:
  *   From **Display**, drag `pico_oled_clear`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Draw Pixels**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, drag `pico_oled_pixel` (X=0, Y=0, Color=1).
  *   **Snap** into loop.
  *   Duplicate block for (127,0), (0,63), (127,63).
2.  **Highlight**:
  *   From **Display**, drag `pico_oled_show`.
  *   **Snap** below pixels."""

    # 0562: Blinking Shapes
    g0562 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset**:
  *   From **Display**, drag `pico_oled_clear`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Random Geometry**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, set `rx` to **Math** `random_integer` (0-127).
  *   **Snap** into loop.
  *   From **Variables**, set `ry` to **Math** `random_integer` (0-63).
2.  **Draw**:
  *   From **Display**, drag `pico_oled_pixel` using `rx`, `ry`.
  *   **Snap** below vars.
  *   From **Display**, drag `pico_oled_show`.
  *   Wait 0.01s."""

    # 0563: Manual Control
    g0563 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup ADC**:
  *   From **Smart IO**, enable GP26.

**B. Main Loop Phase**
1.  **Read Radius**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, set `rad` to **Math** `map_range` (`pico_adc_read` 26, 0-65535 to 1-30).
  *   **Snap** into loop.
2.  **Render**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_circle` (X=64, Y=32, R=`rad`).
  *   From **Display**, drag `pico_oled_show`.
  *   Wait 0.05s."""

    # 0564: Sequences
    g0564 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Draw Frame**:
  *   From **Display**, `pico_oled_rect` (Housing).

**B. Main Loop Phase**
1.  **Red Light**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, `pico_oled_fill_circle` (Top Position).
  *   `pico_oled_show`. Wait 3s.
2.  **Green Light**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_fill_circle` (Bottom Position).
  *   `pico_oled_show`. Wait 3s.
3.  **Yellow Light**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_fill_circle` (Middle Position).
  *   `pico_oled_show`. Wait 1s."""

    # 0565: Interactive
    g0565 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup I2C**:
  *   Init Accelerometer (I2C1) and OLED (I2C0).

**B. Main Loop Phase**
1.  **Read Sensor**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `tilt` to **Sensors** `mpu6050_accel_x`.
2.  **Map Position**:
  *   Set `x_pos` to **Math** `map_range` (`tilt`, -17000 to 17000, 0 to 127).
3.  **Draw Ball**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_circle` (X=`x_pos`, Y=32).
  *   `pico_oled_show`. Wait 0.05s."""

    # 0566: Smart Switch
    g0566 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Variables**:
  *   Set `selected` = 0.

**B. Main Loop Phase**
1.  **Inputs**:
  *   If Btn Up: `selected` = 0.
  *   If Btn Dn: `selected` = 1.
2.  **Render Menu**:
  *   `pico_oled_clear`.
  *   If `selected` == 0:
      *   `fill_rect` (Top Bar). Text "OPTION 1" (Inverse).
      *   Text "OPTION 2" (Normal).
  *   Else:
      *   Text "OPTION 1" (Normal).
      *   `fill_rect` (Bottom Bar). Text "OPTION 2" (Inverse).
  *   `pico_oled_show`."""

    # 0567: Alarm
    g0567 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Message**:
  *   Display "ALARM!".

**B. Main Loop Phase**
1.  **Strobe**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, `pico_oled_invert` (1).
  *   Wait 0.1s.
  *   From **Display**, `pico_oled_invert` (0).
  *   Wait 0.1s."""

    # 0568: Game
    g0568 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: X=64, Y=32, DX=1, DY=0.

**B. Main Loop Phase**
1.  **Input**:
  *   If Up: DX=0, DY=-1.
  *   If Down: DX=0, DY=1.
  *   If Left: DX=-1, DY=0.
  *   If Right: DX=1, DY=0.
2.  **Move**:
  *   Change X by DX. Change Y by DY.
  *   If X < 0: X = 127. (Wrap).
3.  **Draw**:
  *   `pico_oled_clear`.
  *   `pico_oled_pixel` (X, Y).
  *   `pico_oled_show`. Wait 0.05s."""

    # 0569: Automated
    g0569 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: ADC and OLED.

**B. Main Loop Phase**
1.  **Calc**:
  *   Set `angle` from ADC.
  *   Calc `tip_x` = CenterX + cos(angle)*R.
  *   Calc `tip_y` = CenterY + sin(angle)*R.
2.  **Draw**:
  *   `pico_oled_clear`.
  *   `pico_oled_line` (Center -> Tip).
  *   `pico_oled_show`."""

    # 0570: Mastering
    g0570 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Nodes**: Define 8 corner points of cube.

**B. Main Loop Phase**
1.  **Rotate**:
  *   Change `angle` by 0.1.
2.  **Project**:
  *   For each node (x,y,z):
      *   RX = x*cos(a) - z*sin(a).
      *   RZ = x*sin(a) + z*cos(a).
      *   Plot 2D (RX, Y).
3.  **Wireframe**:
  *   Connect projected points with Lines.
  *   `pico_oled_show`."""


    # --- BATCH 58: STOPWATCH 3 (0571-0580) ---

    # 0571: Intro
    g0571 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start**: Print "Ready".

**B. Main Loop Phase**
1.  **Log**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `ms` to **Time** `pico_milliseconds`.
  *   Print `ms`.
  *   Wait 0.1s."""

    # 0572: Blinking
    g0572 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 LED.

**B. Main Loop Phase**
1.  **Check Second**:
  *   `ms` = `pico_milliseconds`.
  *   If (`ms` % 1000) < 500:
      *   Turn LED On.
  *   Else:
      *   Turn LED Off."""

    # 0573: Manual
    g0573 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Zero**:
  *   Set `start_time` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Lap**:
  *   If Btn A (Lap) Pressed:
      *   `current` = `pico_milliseconds`.
      *   `lap_time` = `current` - `last_lap`.
      *   Print `lap_time`.
      *   `last_lap` = `current`."""

    # 0574: Sequences
    g0574 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Buzzer**: GP15.

**B. Main Loop Phase**
1.  **Relay Loop**:
  *   From **Loops**, `repeat` 4 times:
      *   Print "Runner Go".
      *   Pulse Buzzer.
      *   Wait 5s (Lap duration).
2.  **Finish**:
  *   Long Beep."""

    # 0575: Interactive
    g0575 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wait**:
  *   Wait Random (1-5s).

**B. Active Phase**
1.  **Signal**:
  *   Turn LED On.
  *   `start` = `pico_milliseconds`.
2.  **React**:
  *   Wait until Button Pressed.
  *   `end` = `pico_milliseconds`.
3.  **Score**:
  *   Print `end - start`."""

    # 0576: Smart Switch
    g0576 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Activity**:
  *   `last_act` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Interaction**:
  *   If Button Pressed -> `last_act` = `pico_milliseconds`.
2.  **Timeout**:
  *   If (`pico_milliseconds` - `last_act`) > 10000:
      *   Turn System Off (Sleep).
  *   Else:
      *   Stay On."""

    # 0577: Alarm
    g0577 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Monitor**: `run_start` = 0.

**B. Main Loop Phase**
1.  **Detect On**:
  *   If Switch ON and NOT Running:
      *   `run_start` = `pico_milliseconds`. `running` = True.
2.  **Detect Off**:
  *   If Switch OFF: `running` = False.
3.  **Safety**:
  *   If `running` AND (`now` - `run_start` > 5000):
      *   Trigger Buzzer."""

    # 0578: Game
    g0578 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**: 1000ms.

**B. Play Phase**
1.  **Start**:
  *   On Button Press -> `start` = `pico_milliseconds`.
2.  **Stop**:
  *   On Button Press -> `stop` = `pico_milliseconds`.
3.  **Result**:
  *   `diff` = `stop` - `start`.
  *   `error` = abs(`diff` - 1000).
  *   Show on OLED."""

    # 0579: Automated
    g0579 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Lifetime**: `total_secs` = 0.

**B. Main Loop Phase**
1.  **Accumulate**:
  *   If Switch On:
      *   If 1 second passed: `total_secs` += 1.
      *   Print `total_secs`."""

    # 0580: Multitasking
    g0580 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Timers**: `t1`=0, `t2`=0.

**B. Main Loop Phase**
1.  **Task 1**:
  *   If (`now` - `t1`) > 200:
      *   Toggle LED1. `t1` = `now`.
2.  **Task 2**:
  *   If (`now` - `t2`) > 1000:
      *   Toggle LED2. `t2` = `now`."""

    replacements = {
        "0561": g0561, "0562": g0562, "0563": g0563, "0564": g0564, "0565": g0565,
        "0566": g0566, "0567": g0567, "0568": g0568, "0569": g0569, "0570": g0570,
        "0571": g0571, "0572": g0572, "0573": g0573, "0574": g0574, "0575": g0575,
        "0576": g0576, "0577": g0577, "0578": g0578, "0579": g0579, "0580": g0580
    }

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for pid, new_text in replacements.items():
        pattern = rf"(## \d+\. Project {pid}.*?)(### 8\. Step-by-Step Guide.*?)(### 9\. Execution Flow)"
        # Regex to find the Step-by-Step block
        # We need dotall
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # We replace the middle group
            full_match = match.group(0)
            header = match.group(1)
            footer = match.group(3)
            new_block = header + new_text + "\n\n" + footer
            content = content.replace(full_match, new_block)
        else:
            print(f"Project {pid} Not Found for Regex")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Batches 57 & 58 (0561-0580).")

if __name__ == "__main__":
    fix_batch_57_58()
