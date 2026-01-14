import os

def fix_batch_54():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # 1. Project 0531 (Intro)
    g0531 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Vars**:
  *   From **Variables**, set `temp_c` to 0.
  *   From **Variables**, set `temp_f` to 0.

**B. Main Loop Phase**
1.  **Read Temp**:
  *   From **Variables**, set `temp_c` to:
      *   From **Sensors**, `pico_internal_temp`.
  *   **Snap** into `pico_forever`.
2.  **Calculate Fahrenheit**:
  *   From **Variables**, set `temp_f` to:
      *   From **Math**, `arithmetic` block.
      *   ((`temp_c` * 1.8) + 32).
  *   **Snap** below previous block.
3.  **Report**:
  *   From **Text**, use `print` block.
  *   **Snap** below calc block.
  *   *Note: Use "Create Text with" to join strings if needed.*
4.  **Wait**:
  *   From **Time**, wait 1s."""

    # 2. Project 0532 (Freeze Alarm)
    g0532 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16). Snap into `start`.

**B. Main Loop Phase**
1.  **Read**:
  *   From **Variables**, set `temp` to `pico_internal_temp`.
  *   **Snap** into `pico_forever`.
2.  **Check Conditions**:
  *   From **Logic**, drag `if_else`.
  *   Condition: `temp <= 0`.
  *   **Snap** below variable.
3.  **Freeze Mode (If)**:
  *   From **Smart IO**, set GP16 **HIGH**.
  *   From **Time**, wait 0.1s.
  *   From **Smart IO**, set GP16 **LOW**.
  *   From **Time**, wait 0.1s.
4.  **Safe Mode (Else)**:
  *   From **Smart IO**, set GP16 **LOW**.
  *   From **Time**, wait 1s."""

    # 3. Project 0533 (Manual Test)
    g0533 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (In), GP15 (Out).
2.  **Init Sim**:
  *   From **Variables**, set `sim_temp` to 25.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Manual Heat**:
  *   From **Logic**, if `pico_gpio_read(14)`:
      *   Change `sim_temp` by 1.
      *   Wait 0.5s.
      *   **Snap** into `pico_forever`.
2.  **Alarm Logic**:
  *   From **Logic**, if `sim_temp > 35`:
      *   From **Smart IO**, `pico_buzzer_beep` (GP15).
3.  **Natural Cooling**:
  *   From **Logic**, if `sim_temp > 25`:
      *   Change `sim_temp` by -1.
4.  **Wait**:
  *   From **Time**, wait 0.1s."""

    # 4. Project 0534 (Min/Max)
    g0534 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Baseline**:
  *   Set `current` to `pico_internal_temp`.
  *   Set `min_temp` to `current`.
  *   Set `max_temp` to `current`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Update**:
  *   Set `current` to `pico_internal_temp`.
  *   **Snap** into `pico_forever`.
2.  **Check Max**:
  *   From **Logic**, drag `if_do`.
  *   Condition: `current > max_temp`.
  *   Action: Set `max_temp` to `current`.
3.  **Check Min**:
  *   From **Logic**, drag `if_do`.
  *   Condition: `current < min_temp`.
  *   Action: Set `min_temp` to `current`.
4.  **Print**:
  *   Show Min and Max.
  *   Wait 2s."""

    # 5. Project 0535 (Comfort Range)
    g0535 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Red), GP17 (Green) Output.

**B. Main Loop Phase**
1.  **Read**: Set `t` to `pico_internal_temp`.
2.  **Check Range**:
  *   From **Logic**, drag `if_else`.
  *   Condition: From **Logic**, drag `and` block.
      *   Left: `t >= 20`.
      *   Right: `t <= 25`.
  *   **Snap** into Loop.
3.  **Comfort (If)**:
  *   GP17 (Green) HIGH.
  *   GP16 (Red) LOW.
4.  **Uncomfortable (Else)**:
  *   GP17 (Green) LOW.
  *   GP16 (Red) HIGH.
5.  **Wait**: 1s."""

    # 6. Project 0536 (Hysteresis)
    g0536 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Fan) Output.

**B. Main Loop Phase**
1.  **Read**: Set `temp` to `pico_internal_temp`.
2.  **Trigger ON**:
  *   From **Logic**, if `temp > 30`:
      *   Set GP16 **HIGH**.
      *   **Snap** into Loop.
3.  **Trigger OFF**:
  *   From **Logic**, if `temp < 28`:
      *   Set GP16 **LOW**.
      *   **Snap** below Trigger ON.
4.  **Deadband**:
  *   *Note: If temp is 29, neither block runs, keeping previous state.*
  *   Wait 1s."""

    # 7. Project 0537 (Rate of Change)
    g0537 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP15 (Buzzer).
2.  **Baseline**: Set `old_temp` to `pico_internal_temp`.

**B. Main Loop Phase**
1.  **Sample Window**:
  *   From **Time**, wait 5s.
  *   **Snap** into `pico_forever`.
2.  **Calculate Rise**:
  *   Set `new_temp` to `pico_internal_temp`.
  *   Set `rise` to `new_temp - old_temp`.
3.  **Check Slope**:
  *   From **Logic**, if `rise > 2`:
      *   Pulse Buzzer (GP15).
4.  **Reset Baseline**:
  *   Set `old_temp` to `new_temp`."""

    # 8. Project 0538 (Body Heat Game)
    g0538 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Display**: Init OLED. Show "Ready".

**B. Wait Phase**:
1.  **Loop**: Repeat while `pico_internal_temp < 28`.
    *   Wait 0.1s.
2.  **Start**: Set `start_ms` to `pico_milliseconds`.

**C. Game Phase**:
1.  **Loop**: Repeat while `pico_internal_temp < 30`.
    *   Update OLED with values.
2.  **Finish**:
    *   Set `final_time` to (`pico_milliseconds` - `start_ms`) / 1000.
    *   Show "Win! Time: `final_time`"."""

    # 9. Project 0539 (Moving Average)
    g0539 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **None**.

**B. Main Loop Phase**
1.  **Collect Samples**:
  *   Set `total` to 0.
  *   From **Loops**, `count_with` (i from 1 to 10).
      *   Change `total` by `pico_internal_temp`.
      *   Wait 0.05s.
      *   **Snap** into `pico_forever`.
2.  **Average**:
  *   Set `avg` to `total / 10`.
  *   **Snap** below loop.
3.  **Report**:
  *   Print `avg`.
  *   Wait 1s."""

    # 10. Project 0540 (Mastering)
    g0540 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Fan) as PWM (Freq 1000).
2.  **Constants**: Set `target` to 28. Set `gain` to 5000.

**B. Main Loop Phase**
1.  **Control Loop**:
  *   Set `current` to `pico_internal_temp`.
  *   Set `error` to `current - target`.
  *   **Snap** into `pico_forever`.
2.  **Proportional Logic**:
  *   From **Logic**, if `error > 0`:
      *   Set `power` to `error * gain`.
  *   Else:
      *   Set `power` to 0.
3.  **Safety**:
  *   If `power > 65535`: Set `power` to 65535.
4.  **Actuate**:
  *   From **Smart IO**, set PWM Duty (GP16) to `power`.
  *   Wait 0.1."""

    replacements = {
        "0531": g0531, "0532": g0532, "0533": g0533, "0534": g0534, "0535": g0535,
        "0536": g0536, "0537": g0537, "0538": g0538, "0539": g0539, "0540": g0540
    }

    import re
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for pid, new_text in replacements.items():
        # Regex find header like "## X. Project 0531"
        match = re.search(rf"## \d+\. Project {pid}", content)
        if not match:
            print(f"Project {pid} Not Found")
            continue
            
        header_idx = match.start()
        
        guide_header = "### 8. Step-by-Step Guide"
        guide_start = content.find(guide_header, header_idx)
        # End marker is typically execution flow
        guide_end = content.find("### 9. Execution Flow", guide_start)
        
        if guide_start == -1 or guide_end == -1:
            print(f"Guide not found for {pid}")
            continue

        pre = content[:guide_start]
        post = content[guide_end:]
        content = pre + new_text + "\n\n" + post

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Batch 54 (0531-0540).")

if __name__ == "__main__":
    fix_batch_54()
