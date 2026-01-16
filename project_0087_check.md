## Project 0087: Digital Egg Timer (Interactive Alarm)

### 2. Learning Objective
Multi-phase logic and inactivity timeouts. Build a timer that allows the user to set a duration (in seconds) by repeatedly tapping a button, then automatically switches to "Run Phase" and sounds an alarm when the time expires.

### 3. Concepts Introduced
*   **Mode Switching**: Designing logic that transitions from an "Input/Setup" state to an "Active/Task" state without a separate physical switch.
*   **Current Time Delta**: Calculating the time elapsed since the last user action to trigger a timeout.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Passive Buzzer**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Setting Trigger (Pull-Down) |
| **Buzzer** | GP15 | Alarm Output (PWM) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if)
*   From **Logic & Math**, drag **`[X] > [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`[X] - [Y]`** (arithmetic)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_pwm_freq_duty`** (set frequency/duty)
*   From **Smart IO**, drag **`pico_pwm_duty`** (set duty)
*   From **Smart IO**, drag **`get current time (ms)`** (ticks_ms)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)

### 7. Variables
*   **btn, buzz**: Pin/PWM objects.
*   **timer_val**: Number of seconds to count down.
*   **last_act**: Timestamp of the last button press in milliseconds.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn** (GP10) and **buzz** (GP15, PWM).
    *   Set **timer_val** to **0**.
    *   Set **last_act** to **`get current time (ms)`**.
    *   **Snap** into the **`start`** block.

**B. Setup Phase**
2.  **Input Loop**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if (**`get current time (ms)`** - **`last_act`**) < **3000** (Wait 3 seconds for inactivity).
    *   **Inside**:
        *   If **btn** is HIGH:
            *   Change **timer_val** by **1**.
            *   Set **last_act** to **`get current time (ms)`**.
            *   **pico_log**: "Timer set to: " + **timer_val** + " seconds".
            *   Wait while **btn** is HIGH.
        *   Wait **0.05** seconds.

**C. Run Phase**
3.  **The Countdown**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **timer_val** > **0**.
    *   **Action**:
        *   **pico_log**: "Seconds remaining: " + **timer_val**.
        *   Wait **1.0** seconds.
        *   Change **timer_val** by **-1**.
4.  **The Alarm**:
    *   From **Smart IO**, set **buzz** frequency to **1000** and duty to **50** (Sound On).
    *   Wait **2.0** seconds.
    *   Set **buzz** duty to **0** (Sound Off).

### 9. Execution Flow
1.  **Set**: You tap the button 10 times. Console says "Timer set to: 10".
2.  **Wait**: You stop. After 3 seconds of silence, the Pico knows you are done.
3.  **Run**: "Seconds remaining: 10... 9... 8...".
4.  **Alarm**: At 0, the buzzer makes a loud BEEP for 2 seconds.
5.  **Finish**: The program ends.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
buzz = PWM(Pin(15))
timer_val = 0
last_act = time.ticks_ms()

# 1. SETUP PHASE (Collection)
print("Tap button to add seconds. Stop for 3s to start.")
while time.ticks_diff(time.ticks_ms(), last_act) < 3000:
    if btn.value() == 1:
        timer_val += 1
        last_act = time.ticks_ms()
        print("Timer:", timer_val, "s")
        while btn.value() == 1:
            time.sleep(0.01)
    time.sleep(0.05)

# 2. RUN PHASE (Countdown)
if timer_val > 0:
    print("Countdown Started...")
    while timer_val > 0:
        print("T-minus:", timer_val)
        time.sleep(1)
        timer_val -= 1

    # 3. ALARM PHASE
    print("TIME IS UP!")
    buzz.freq(1000)
    buzz.duty_u16(32768) # 50%
    time.sleep(2)
    buzz.duty_u16(0)
else:
    print("Timer cancelled (0s).")
```

### 11. Common Mistakes
*   **The Inactivity Gap**: Tapping too slowly. If you wait 3.1 seconds between taps, the timer will start counting down early.
*   **PWM Duty**: Forgetting to set duty back to 0. If you don't, the buzzer will scream forever until you unplug the Pico.
*   **Variable Decay**: Correctly using `timer_val -= 1` inside the loop. If you use `+= 1`, the timer will count up to infinity!

### 12. Try This Next
*   **Visual Tick**: Flash an LED (GP14) every time a second passes.
*   **Pulse Alarm**: Instead of a solid beep, make the buzzer go "Beep-Beep-Beep" using a small loop.
*   **Variable Pitch**: Start the alarm at 500Hz and increase the frequency as you get closer to 0.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log. Clarified Setup vs Run phases in 0087. Updated 0087 to use PWM for buzzer.
- Date Verified: 2026-01-08
---## Project 0088: Guess the Number (Select & Submit)
