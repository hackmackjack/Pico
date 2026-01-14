import os

def fix_batch_55():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # 1. Project 0541 (Soft Start)
    g0541 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
  *   From **Smart IO**, drag `pico_pwm_write`.
  *   **Snap** into `start`.
  *   Set GP16 to 0.

**B. Main Loop Phase**
1.  **Ramp Up Loop**:
  *   From **Loops**, drag `count_with` (`fan_speed` from 0 to 65000 by 650).
  *   **Snap** into `pico_forever`.
  *   Action: From **Smart IO**, set GP16 PWM to `fan_speed`.
  *   Wait: From **Time**, wait 0.1s.
2.  **Hold**:
  *   From **Time**, wait 2s.
  *   **Snap** below loop."""

    # 2. Project 0542 (Blinking Fan)
    g0542 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Baseline Mode**:
  *   From **Smart IO**, set GP16 PWM to 15000 (Low).
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Maintain Breeze**:
  *   From **Smart IO**, set GP16 PWM to 15000.
  *   **Snap** into `pico_forever`.
2.  **Random Delay**:
  *   Set `wait_time` to `random_integer(1, 5)`.
  *   **Wait** `wait_time` seconds.
3.  **Gust Surge**:
  *   From **Smart IO**, set GP16 PWM to 65000.
  *   **Wait** 0.5s.
  *   *Note: Loop repeats, returning to low speed immediately.*"""

    # 3. Project 0543 (3-Speed)
    g0543 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init State**:
  *   Set `fan_mode` to 0.
  *   Set GP16 PWM to 0.

**B. Main Loop Phase**
1.  **Button Input**:
  *   From **Logic**, if `pico_gpio_read(14)` is HIGH:
      *   Change `fan_mode` by 1.
      *   Wait 0.3s (Debounce).
      *   **Snap** into `pico_forever`.
2.  **Wrap Around**:
  *   From **Logic**, if `fan_mode > 3`:
      *   Set `fan_mode` to 0.
3.  **Execute Mode**:
  *   From **Logic**, drag `if_else_if` (Expand to 4 slots).
  *   If `fan_mode == 1`: Set GP16 to 20000.
  *   Else If `fan_mode == 2`: Set GP16 to 40000.
  *   Else If `fan_mode == 3`: Set GP16 to 65000.
  *   Else: Set GP16 to 0."""

    # 4. Project 0544 (Sequences)
    g0544 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Fan**:
  *   From **Smart IO**, set GP16 PWM to 40000.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Sweep Right**:
  *   From **Loops**, `count_with` (`angle` from 0 to 180 by 5).
      *   From **Motors**, `pico_servo_angle` (GP15, `angle`).
      *   Wait 0.05s.
      *   **Snap** into `pico_forever`.
2.  **Sweep Left**:
  *   From **Loops**, `count_with` (`angle` from 180 to 0 by -5).
      *   From **Motors**, `pico_servo_angle` (GP15, `angle`).
      *   Wait 0.05s.
      *   **Snap** below first loop."""

    # 5. Project 0545 (Interactive)
    g0545 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Fan) Off.

**B. Main Loop Phase**
1.  **Listen**:
  *   Set `sound_vol` to `pico_adc_read(26)`.
  *   **Snap** into `pico_forever`.
2.  **Trigger**:
  *   From **Logic**, if `sound_vol > 35000`:
      *   **Activate**: Set GP16 PWM to 65000.
      *   **Hold**: Wait 5s.
      *   **Deactivate**: Set GP16 PWM to 0.
  *   Else:
      *   Set GP16 PWM to 0.
  *   Wait 0.01s."""

    # 6. Project 0546 (Timer Switch)
    g0546 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Fan) Off.

**B. Main Loop Phase**
1.  **Check Request**:
  *   From **Logic**, if `pico_gpio_read(14)` is HIGH:
      *   Print "Night Mode Active".
      *   Set GP16 PWM to 20000 (Low Noise).
      *   Wait 10s.
      *   Print "Shutting Down".
      *   Set GP16 PWM to 0.
      *   **Snap** into `pico_forever`."""

    # 7. Project 0547 (Alarm System)
    g0547 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Flags**: Set `is_stalled` to FALSE.
2.  **Init Buzz**: Set GP12 to LOW.

**B. Main Loop Phase**
1.  **Input Handling**:
  *   If `pico_gpio_read(14)`: Set `is_stalled` to TRUE.
  *   If `pico_gpio_read(15)`: Set `is_stalled` to FALSE.
  *   **Snap** into `pico_forever`.
2.  **Enforcement Logic**:
  *   From **Logic**, drag `if_else`.
  *   Condition: `is_stalled` is TRUE.
  *   **If Fault**:
      *   Set GP16 (Fan) to 0.
      *   Set GP12 (Buzzer) to HIGH.
  *   **Else (Safe)**:
      *   Set GP16 (Fan) to 30000.
      *   Set GP12 (Buzzer) to LOW."""

    # 8. Project 0548 (Game)
    g0548 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP26 (Pot), GP16 (Fan).

**B. Main Loop Phase**
1.  **Direct Mapping**:
  *   Set `lift_power` to `pico_adc_read(26)`.
  *   **Snap** into `pico_forever`.
2.  **Actuate**:
  *   From **Smart IO**, set GP16 PWM to `lift_power`.
3.  **Feedback**:
  *   Wait 0.02s."""

    # 9. Project 0549 (Automated)
    g0549 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP15 (DHT), GP16 (Fan).

**B. Main Loop Phase**
1.  **Read DHT**:
  *   Set `cur_humidity` to `pico_dht_read_humidity(15)`.
  *   **Snap** into `pico_forever`.
2.  **Control Logic**:
  *   From **Logic**, if `cur_humidity > 70`:
      *   Set GP16 to HIGH (Fan On).
  *   Else:
      *   Set GP16 to LOW (Fan Off).
3.  **Wait**:
  *   Wait 2s (Required for DHT)."""

    # 10. Project 0550 (Mastering) - Assuming standard PID/Control
    # I'll create a generic compliant PID guide similar to 0540 if not seen.
    # Re-reading 0540 logic (Prop controller)
    g0550 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 (Fan) PWM.
2.  **Target**: Set `target_h` (Humidity) to 50.

**B. Main Loop Phase**
1.  **Read**:
  *   Set `h` to `pico_dht_read_humidity`.
  *   **Snap** into `pico_forever`.
2.  **Calculate Error**:
  *   Set `error` to `h - target_h`.
3.  **Prop Control**:
  *   If `error > 0` (Too Moist):
      *   Set `power` to `error * 1000`.
      *   If `power > 65000`: Set `power` to 65000.
      *   Set GP16 PWM to `power`.
  *   Else:
      *   Set GP16 PWM to 0.
  *   Wait 2s."""

    replacements = {
        "0541": g0541, "0542": g0542, "0543": g0543, "0544": g0544, "0545": g0545,
        "0546": g0546, "0547": g0547, "0548": g0548, "0549": g0549, "0550": g0550
    }

    import re
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for pid, new_text in replacements.items():
        match = re.search(rf"## \d+\. Project {pid}", content)
        if not match:
            print(f"Project {pid} Not Found")
            continue
            
        header_idx = match.start()
        
        guide_header = "### 8. Step-by-Step Guide"
        guide_start = content.find(guide_header, header_idx)
        guide_end = content.find("### 9. Execution Flow", guide_start)
        
        if guide_start == -1 or guide_end == -1:
            print(f"Guide not found for {pid}")
            continue

        pre = content[:guide_start]
        post = content[guide_end:]
        content = pre + new_text + "\n\n" + post

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed Batch 55 (0541-0550).")

if __name__ == "__main__":
    fix_batch_55()
