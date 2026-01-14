import os

def fix_universal_57_60():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Dictionary of Fixes (Same content as before, merged for efficiency)
    replacements = {}
    
    # --- BATCH 57 (0561-0570) ---
    replacements["0561"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear Screen**:
  *   From **Display**, drag `pico_oled_clear`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Draw Pixels**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, drag `pico_oled_pixel`.
  *   **Snap** into loop.
  *   Set X to 0, Y to 0, Color to 1.
  *   From **Display**, drag `pico_oled_show`.
  *   **Snap** below pixel."""
  
    replacements["0562"] = """### 8. Step-by-Step Guide

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
  *   From **Display**, drag `pico_oled_pixel`.
  *   **Snap** below vars.
  *   Set X to `rx`, Y to `ry`.
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 0.01s."""

    replacements["0563"] = """### 8. Step-by-Step Guide

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
  *   From **Display**, drag `pico_oled_circle`.
  *   **Snap** below clear.
  *   Set X=64, Y=32, R=`rad`.
  *   From **Display**, drag `pico_oled_show`.
  *   Wait 0.05s."""

    replacements["0564"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Draw Frame**:
  *   From **Display**, drag `pico_oled_rect` (Housing).
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Red Light**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, drag `pico_oled_fill_circle` (Top Pos).
  *   **Snap** into loop.
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 3s.
2.  **Green Light**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_fill_circle` (Bottom Pos).
  *   **Snap** below wait.
  *   From **Display**, drag `pico_oled_show`.
3.  **Yellow Light**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_fill_circle` (Mid Pos).
  *   **Snap** below previous.
  *   From **Display**, drag `pico_oled_show`.
  *   From **Time**, wait 1s."""

    replacements["0565"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup I2C**:
  *   Init Accelerometer (I2C1) and OLED (I2C0).

**B. Main Loop Phase**
1.  **Read Sensor**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `tilt` to **Sensors** `mpu6050_accel_x`.
  *   **Snap** into loop.
2.  **Map Position**:
  *   Set `x_pos` to **Math** `map_range` (`tilt`, -17000 to 17000, 0 to 127).
  *   **Snap** below tilt.
3.  **Draw Ball**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_circle`.
  *   **Snap** below mapping.
  *   Set CenterX=`x_pos`, CenterY=32.
  *   From **Display**, drag `pico_oled_show`."""

    replacements["0566"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Variables**:
  *   Set `selected` = 0.

**B. Main Loop Phase**
1.  **Inputs**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Btn Up: `selected` = 0.
  *   From **Logic**, if Btn Dn: `selected` = 1.
  *   **Snap** into loop.
2.  **Render Menu**:
  *   From **Display**, drag `pico_oled_clear`.
  *   From **Logic**, if `selected` == 0:
      *   `pico_oled_fill_rect` (Top Bar). 
      *   `pico_oled_text` "OPTION 1" (Inverse).
  *   From **Display**, `pico_oled_show`."""

    replacements["0567"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Message**:
  *   From **Display**, `pico_oled_text` "ALARM!".
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Strobe**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, drag `pico_oled_invert` (1).
  *   **Snap** into loop.
  *   From **Time**, wait 0.1s.
  *   From **Display**, drag `pico_oled_invert` (0).
  *   From **Time**, wait 0.1s."""

    replacements["0568"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: Set X=64, Y=32, DX=1, DY=0.

**B. Main Loop Phase**
1.  **Input**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Up: DX=0, DY=-1.
  *   **Snap** into loop.
  *   (Repeat for Down/Left/Right).
2.  **Move**:
  *   From **Variables**, change X by DX. Change Y by DY.
  *   **Snap** below inputs.
3.  **Draw**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_pixel` (X, Y).
  *   From **Display**, `pico_oled_show`."""

    replacements["0569"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: ADC and OLED.

**B. Main Loop Phase**
1.  **Calc**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `angle` from ADC.
  *   **Snap** into loop.
  *   Set `tip_x` = CenterX + cos(angle)*R.
  *   Set `tip_y` = CenterY + sin(angle)*R.
2.  **Draw**:
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, drag `pico_oled_line`.
  *   **Snap** below calc.
  *   Line from (64,64) to (`tip_x`, `tip_y`).
  *   `pico_oled_show`."""

    replacements["0570"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Nodes**: Define 8 corner points of cube.

**B. Main Loop Phase**
1.  **Rotate**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, change `angle` by 0.1.
  *   **Snap** into loop.
2.  **Project**:
  *   For each node (x,y,z):
      *   RX = x*cos(a) - z*sin(a).
      *   RZ = x*sin(a) + z*cos(a).
      *   Plot 2D (RX, Y).
3.  **Wireframe**:
  *   From **Display**, drag `pico_oled_line`.
  *   Connect projected points.
  *   `pico_oled_show`."""

    # --- BATCH 58 (0571-0580) ---
    replacements["0571"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start**: Print "Ready".

**B. Main Loop Phase**
1.  **Log**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, set `ms` to **Time** `pico_milliseconds`.
  *   **Snap** into loop.
  *   From **Text**, print `ms`.
  *   From **Time**, wait 0.1s."""

    replacements["0572"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 LED.

**B. Main Loop Phase**
1.  **Check Second**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `ms` = `pico_milliseconds`.
  *   **Snap** into loop.
  *   From **Logic**, if (`ms` % 1000) < 500:
      *   From **Smart IO**, set GP16 HIGH.
  *   Else:
      *   From **Smart IO**, set GP16 LOW."""

    replacements["0573"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Zero**:
  *   Set `start_time` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Lap**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Btn A (Lap) Pressed:
      *   Set `current` = `pico_milliseconds`.
      *   Set `lap_time` = `current` - `last_lap`.
      *   From **Text**, print `lap_time`.
      *   Set `last_lap` = `current`."""

    replacements["0574"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Buzzer**: GP15.

**B. Main Loop Phase**
1.  **Relay Loop**:
  *   From **Loops**, drag `repeat` 4 times.
  *   **Snap** into `start`.
  *   Print "Runner Go".
  *   From **Smart IO**, pulse Buzzer.
  *   From **Time**, wait 5s.
2.  **Finish**:
  *   From **Smart IO**, beep long."""

    replacements["0575"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wait**:
  *   Wait Random (1-5s).

**B. Active Phase**
1.  **Signal**:
  *   From **Smart IO**, set LED HIGH.
  *   Set `start` = `pico_milliseconds`.
2.  **React**:
  *   From **Loops**, repeat until Button Pressed.
  *   Set `end` = `pico_milliseconds`.
3.  **Score**:
  *   From **Text**, print `end - start`."""

    replacements["0576"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Activity**:
  *   Set `last_act` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Interaction**:
  *   From **Loops**, drag `pico_forever`.
  *   If Button Pressed -> Set `last_act` = `pico_milliseconds`.
  *   **Snap** into loop.
2.  **Timeout**:
  *   From **Logic**, if (`pico_milliseconds` - `last_act`) > 10000:
      *   From **Smart IO**, turn System Off.
  *   Else:
      *   Turn System On."""

    replacements["0577"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Monitor**: `run_start` = 0.

**B. Main Loop Phase**
1.  **Detect On**:
  *   From **Loops**, drag `pico_forever`.
  *   If Switch ON and NOT Running:
      *   Set `run_start` = `pico_milliseconds`. `running` = True.
2.  **Safety**:
  *   If `running` AND (`now` - `run_start` > 5000):
      *   From **Smart IO**, trigger Buzzer.
      *   **Snap** into loop."""

    replacements["0578"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**: 1000ms.

**B. Play Phase**
1.  **Start**:
  *   Wait for Button -> Set `start` = `pico_milliseconds`.
2.  **Stop**:
  *   Wait for Button -> Set `stop` = `pico_milliseconds`.
3.  **Result**:
  *   Set `diff` = `stop` - `start`.
  *   Set `error` = abs(`diff` - 1000).
  *   From **Display**, show `error`."""

    replacements["0579"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Lifetime**: `total_secs` = 0.

**B. Main Loop Phase**
1.  **Accumulate**:
  *   From **Loops**, drag `pico_forever`.
  *   If Switch On:
      *   If 1 second passed: Change `total_secs` by 1.
      *   From **Text**, print `total_secs`."""

    replacements["0580"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Timers**: `t1`=0, `t2`=0.

**B. Main Loop Phase**
1.  **Task 1**:
  *   From **Loops**, drag `pico_forever`.
  *   If (`now` - `t1`) > 200:
      *   Toggle LED1. `t1` = `now`.
  *   **Snap** into loop.
2.  **Task 2**:
  *   If (`now` - `t2`) > 1000:
      *   Toggle LED2. `t2` = `now`."""

    # --- BATCH 59 (0581-0590) ---
    replacements["0581"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Print**:
  *   From **Text**, print "Timer Started...".

**B. Main Loop Phase**
1.  **Count Seconds**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, change `ticks` by 1.
2.  **Format**:
  *   From **Logic**, if (`ticks` % 10) == 0:
      *   From **Text**, print " [10s Marks]".
  *   Else:
      *   From **Text**, print "."."""

    replacements["0582"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `timer` = 15.

**B. Main Loop Phase**
1.  **Urgency Check**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if `timer` > 10: `wait` = 0.5.
  *   Else If `timer` > 0: `wait` = 0.1.
  *   Else: Break.
  *   **Snap** into loop.
2.  **Blink**:
  *   From **Smart IO**, LED On. Wait `wait`.
  *   LED Off. Wait `wait`."""

    replacements["0583"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Select**:
  *   From **Loops**, repeat Until Button Pressed:
      *   Set `m` = Map `pico_adc_read` to 1-60.
      *   From **Display**, show "SET: `m` MINS".
2.  **Run**:
  *   Set `s` = m * 60.
  *   Repeat while `s` > 0:
      *   Show Time. Wait 1s.
      *   Change `s` by -1."""

    replacements["0584"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Green (16), Blue (17).

**B. Main Loop Phase**
1.  **Pomodoro**:
  *   From **Loops**, repeat 4 times:
      *   **Focus**: Green On, Blue Off. Wait 1500s.
      *   **Break**: Green Off, Blue On. Wait 300s.
      *   **Snap** into `start`."""

    replacements["0585"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mode**: `type` = 0.

**B. Select Phase**
1.  **Cycle**:
  *   From **Loops**, repeat Until Button Released.
  *   If Button Click: `type` = (`type` + 1) % 3.
  *   From **Logic**, if 0: Print "Small".
  *   If 1: Print "Medium".
  *   If 2: Print "Large"."""

    replacements["0586"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **IO**: Lock (14), Start (15).

**B. Main Loop Phase**
1.  **Permission**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Button (15) AND Lock (14):
      *   From **Text**, print "GRANTED".
  *   Else If Button (15) AND NOT Lock (14):
      *   From **Text**, print "LOCKED".
  *   **Snap** into loop."""

    replacements["0587"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Anchor**: `finish` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Escalate**:
  *   From **Loops**, drag `pico_forever`.
  *   Set `over` = `pico_milliseconds` - `finish`.
  *   **Snap** into loop.
  *   From **Logic**, if `over` < 10000:
      *   From **Smart IO**, beep Slow.
  *   Else If `over` < 30000:
      *   From **Smart IO**, beep Fast."""

    replacements["0588"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wires**: Defuse(14), Trap(15,16).

**B. Main Loop Phase**
1.  **Check**:
  *   From **Loops**, drag `pico_forever`.
  *   If Defuse High: "WIN". Break.
  *   If Trap High: "FAIL". `spd`=0.2.
  *   **Snap** into loop.
2.  **Tick**:
  *   Print `time`.
  *   Wait `spd`."""

    replacements["0589"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `deadline` = 0.

**B. Main Loop Phase**
1.  **Motion**:
  *   From **Loops**, drag `pico_forever`.
  *   If PIR High:
      *   LED On.
      *   `deadline` = `now` + 10000.
  *   **Snap** into loop.
2.  **Expiry**:
  *   If `now` > `deadline`:
      *   LED Off."""

    replacements["0590"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **RTC**: Set to (2025, 12, 31, 16, 59, 50).

**B. Main Loop Phase**
1.  **Watch**:
  *   From **Loops**, drag `pico_forever`.
  *   If Hr==17 AND Min==0:
      *   From **Smart IO**, Alarm On.
      *   Wait 60s.
  *   **Snap** into loop."""

    # --- BATCH 60 (0591-0600) ---
    replacements["0591"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Screen**: "BPM: 60".

**B. Main Loop Phase**
1.  **Pulse**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, drag `pico_oled_invert` (1).
  *   **Snap** into loop.
  *   Wait 0.05s.
  *   From **Display**, drag `pico_oled_invert` (0).
  *   Wait 0.95s."""

    replacements["0592"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Count-In**:
  *   From **Loops**, repeat 4 times:
      *   Flash LED.
      *   Wait 1s.
      *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Live**:
  *   From **Loops**, drag `pico_forever`.
  *   LED On.
  *   Click Buzzer.
  *   **Snap** into loop."""

    replacements["0593"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Tap Detect**:
  *   Wait for Tap 1 -> `t1`.
  *   Wait for Tap 2 -> `t2`.
  *   Set `gap` = t2 - t1.

**B. Main Loop Phase**
1.  **Playback**:
  *   From **Loops**, drag `pico_forever`.
  *   Click Buzzer.
  *   Wait `gap` seconds.
  *   **Snap** into loop."""

    replacements["0594"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Pattern**: List [0.4, 0.4, 0.4, 0.2, 0.4].

**B. Main Loop Phase**
1.  **Groove**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Loops**, for each `item` in List:
      *   Click Buzzer.
      *   Wait `item` seconds.
      *   **Snap** into loop."""

    replacements["0595"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Beat**: 1.

**B. Main Loop Phase**
1.  **Accent**:
  *   From **Loops**, drag `pico_forever`.
  *   If `beat` == 1 AND Btn A: Tone = Loud.
  *   Else: Tone = Normal.
  *   **Snap** into loop.
2.  **Triplet**:
  *   If Btn B: Play 3 clicks.
  *   Else: Play 1 click."""

    replacements["0596"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Pins**: Switch(14), Audio(15), Haptic(16).

**B. Main Loop Phase**
1.  **Route**:
  *   From **Loops**, drag `pico_forever`.
  *   If Switch On (Silent):
      *   Pulse Haptic.
  *   Else:
      *   Pulse Audio.
  *   **Snap** into loop."""

    replacements["0597"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mic**: GP26.

**B. Main Loop Phase**
1.  **Level**:
  *   From **Loops**, drag `pico_forever`.
  *   Scan 100 samples -> Find Max.
  *   **Snap** into loop.
2.  **Threshold**:
  *   From **Logic**, if Max > 40000:
      *   From **Smart IO**, Flash Red LED.
  *   else:
      *   LED Off."""

    replacements["0598"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sync**: `start` = `now`.

**B. Main Loop Phase**
1.  **Polyrhythm**:
  *   From **Loops**, drag `pico_forever`.
  *   `t` = `now` - `start`.
  *   If (`t` % 400) == 0: Click B1.
  *   If (`t` % 300) == 0: Click B2.
  *   **Snap** into loop."""

    replacements["0599"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Tempo**: `gap` = 1.0s.

**B. Main Loop Phase**
1.  **Accelerate**:
  *   From **Loops**, drag `pico_forever`.
  *   Repeat 4 times (Bar):
      *   Click. Wait `gap`.
  *   Change `gap` by -5%.
  *   **Snap** into loop."""

    replacements["0600"] = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **UI**: Draw Metronome.

**B. Main Loop Phase**
1.  **Swing**:
  *   From **Loops**, drag `pico_forever`.
  *   Calculate `angle` (Sine wave).
  *   Draw Line from Center.
  *   If `angle` crosses 0: Click Buzzer.
  *   **Snap** into loop."""

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for pid, new_text in replacements.items():
        # Exact string finding for header
        start_marker = f"## {1 if pid[0]=='0' else ''}{int(pid)}. Project {pid}"
        
        # We need to find this marker.
        # Note: formatting in file might be "## 50. Project 0500" or similar.
        # The file uses "## 99. Project 0599" etc.
        # But wait, the file uses "## 1. Project 0572" style relative numbering in batches?
        # Let's check the file content again.
        # Line 5679: "## 1. Project 0572: Blinking Stopwatch"
        # So it is "## 1. Project XXXX" not "## 572."!
        # This explains why the previous regex failed. it looked for "## \d+\. Project {pid}" which matched,
        # but maybe the "## \d+" part matched "1" instead of "572".
        
        # Robust search: Find "Project {pid}:"
        idx_proj = content.find(f"Project {pid}:")
        if idx_proj == -1:
            print(f"Skipping {pid} - Header not found.")
            continue
            
        # Backtrack to "## " to get the full header start
        idx_header = content.rfind("## ", 0, idx_proj)
        
        # Find Section 8
        idx_guide = content.find("### 8. Step-by-Step Guide", idx_proj)
        if idx_guide == -1:
            print(f"Skipping {pid} - Guide not found.")
            continue
            
        # Find Section 9
        idx_exec = content.find("### 9. Execution Flow", idx_guide)
        if idx_exec == -1:
            print(f"Skipping {pid} - Exec Flow not found.")
            continue
            
        # Replace
        pre = content[:idx_guide]
        post = content[idx_exec:]
        content = pre + new_text + "\n\n" + post
        print(f"Applied fix for {pid}")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Universal Fix Applied.")

if __name__ == "__main__":
    fix_universal_57_60()
