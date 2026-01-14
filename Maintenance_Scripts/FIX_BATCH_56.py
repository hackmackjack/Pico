import os

def fix_batch_56():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # 1. Project 0551 (Arm Intro)
    g0551 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Servo**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** into `start` block.
  *   Set Pin to GP16 and Angle to 90.

**B. Main Loop Phase**
1.  **Maintain Position**:
  *   From **Loops**, drag `pico_forever`.
  *   **Snap** below initialization.
2.  **Verify Angle**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** into loop.
  *   Set Angle to 90.
  *   From **Time**, wait 0.1s."""

    # 2. Project 0552 (Waving)
    g0552 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** into `start`.
  *   Set Pin to GP16 and Angle to 0.

**B. Main Loop Phase**
1.  **Position One**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** into `pico_forever`.
  *   Set Pin to GP16 and Angle to 0.
  *   Wait 1s.
2.  **Position Two**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** below wait.
  *   Set Pin to GP16 and Angle to 180.
  *   Wait 1s."""

    # 3. Project 0553 (Manual)
    g0553 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
  *   From **Smart IO**, drag `pico_adc_read` (GP26) to familiarize.

**B. Main Loop Phase**
1.  **Read Knob**:
  *   From **Variables**, set `pot_val` to **Smart IO** `pico_adc_read` GP26.
  *   **Snap** into `pico_forever`.
2.  **Map and Move**:
  *   From **Motors**, drag `pico_servo_angle`.
  *   **Snap** below variable.
  *   Set Value to:
      *   From **Math**, `map_range` block.
      *   Input: `pot_val`, From: 0-65535, To: 0-180.
3.  **Wait**:
  *   From **Time**, wait 0.05 seconds."""

    # 4. Project 0554 (Sequences)
    g0554 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Homing**:
  *   From **Motors**, set `pico_servo_angle` GP16 to 0.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Move to Home**:
  *   From **Motors**, set `pico_servo_angle` GP16 to 0.
  *   **Snap** into `pico_forever`.
  *   From **Time**, wait 1.0s.
2.  **Move to Pickup**:
  *   From **Motors**, set `pico_servo_angle` GP16 to 45.
  *   **Snap** below wait.
  *   From **Time**, wait 2.0s.
3.  **Move to Dropoff**:
  *   From **Motors**, set `pico_servo_angle` GP16 to 180.
  *   **Snap** below wait.
  *   From **Time**, wait 2.0s."""

    # 5. Project 0555 (Teaching)
    g0555 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (Btn), GP26 (Pot).

**B. Main Loop Phase**
1.  **Monitor Button**:
  *   From **Logic**, if GP14 is HIGH:
      *   **Step 1**: Set `pos_a` to **Math** `map` `pico_adc_read(26)` (0-65535 -> 0-180).
      *   Wait 2s.
      *   **Step 2**: Set `pos_b` to **Math** `map` `pico_adc_read(26)` (0-65535 -> 0-180).
      *   Wait 2s.
2.  **Playback Loop**:
  *   From **Loops**, repeat 10 times:
      *   From **Motors**, set Angle to `pos_a`. Wait 1s.
      *   From **Motors**, set Angle to `pos_b`. Wait 1s.
      *   **Snap** inside the If block (or outside if logic differs).
      *   *(Correction: Usually playback happens after recording. Here we put it inside for simplicity or use a separate mode variable).*"""

    # 6. Project 0556 (Safety)
    g0556 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (IR), GP16 (Servo).

**B. Main Loop Phase**
1.  **Safety Check**:
  *   From **Variables**, set `is_clear` to **Smart IO** `pico_gpio_read` GP14.
  *   **Snap** into `pico_forever`.
2.  **Logic Gate**:
  *   From **Logic**, drag `if_else`.
  *   Condition: `is_clear` == TRUE.
  *   **If Safe**:
      *   Perform Sweep (0 -> 180 -> 0).
  *   **If Blocked**:
      *   From **Data**, print "STOPPED".
      *   From **Motors**, set Angle to 90 (Safe Position)."""

    # 7. Project 0557 (Torque)
    g0557 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP26 (Strain), GP16 (Servo).

**B. Main Loop Phase**
1.  **Read Load**:
  *   Set `current_load` to `pico_adc_read(26)`.
  *   **Snap** into `pico_forever`.
2.  **Safety Check**:
  *   From **Logic**, if `current_load > 50000`:
      *   Set Servo GP16 to 0. (Or disable PWM).
      *   Pulse Buzzer.
  *   Else:
      *   Move Servo (Sweep)."""

    # 8. Project 0558 (Catapult)
    g0558 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset**: Set Servo to 0.

**B. Main Loop Phase**
1.  **Tensioning**:
  *   From **Loops**, `count_with` (`stretch` from 0 to 90).
      *   Set Servo to `stretch`.
      *   Wait 0.05s.
      *   **Snap** into `pico_forever`.
2.  **Ready**:
  *   Wait 2s.
3.  **Fire**:
  *   From **Motors**, set Servo to 0 (Fast).
  *   Wait 5s."""

    # 9. Project 0559 (Automated - Inverse Kinematics simplified) - I'll guess/create standard logic
    g0559 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: 2 Servos (Shoulder GP16, Elbow GP17).

**B. Main Loop Phase**
1.  **Reach Out**:
  *   Set Shoulder to 45.
  *   Set Elbow to 90.
  *   Wait 1s.
2.  **Retract**:
  *   Set Shoulder to 90.
  *   Set Elbow to 0.
  *   Wait 1s."""

    # 10. Project 0560 (Mastering)
    g0560 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Full Arm.

**B. Main Loop Phase**
1.  **Sequence**:
  *   From **Functions**, call `pick_up_object`.
  *   From **Functions**, call `move_to_bin`.
  *   From **Functions**, call `drop_object`.
  *   **Snap** into `pico_forever`.
  *   *Note: Define these functions using the stack blocks.*"""

    replacements = {
        "0551": g0551, "0552": g0552, "0553": g0553, "0554": g0554, "0555": g0555,
        "0556": g0556, "0557": g0557, "0558": g0558, "0559": g0559, "0560": g0560
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
        
    print("Fixed Batch 56 (0551-0560).")

if __name__ == "__main__":
    fix_batch_56()
