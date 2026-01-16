## Project 0093: Input Quantizer (Auto-Dot & Auto-Dash)

### 2. Learning Objective
Input quantization and semi-automated event handling. Build a telegraph system that uses two buttons: one to automatically fire a perfectly timed "Dot" and another for a "Dash," ensuring perfect signal ratios regardless of how long the human operator holds the button.

### 3. Concepts Introduced
*   **Input Quantization**: Adjusting human input (which varies in length) to a fixed, standardized value (0.2s or 0.6s).
*   **Blocking vs. Non-Blocking**: Ensuring that once a signal starts, it completes its full duration before the next input is accepted.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **2x Push Buttons**
*   **1x Passive Buzzer**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn A (Dot)** | GP10 | Automated Dot Trigger |
| **Btn B (Dash)** | GP11 | Automated Dash Trigger |
| **Buzzer** | GP15 | Audio Output (PWM) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_pwm_freq_duty`** (set PWM)
*   From **Smart IO**, drag **`pico_pwm_duty`** (set duty)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)

### 7. Variables
*   **btn_dot, btn_dash**: Pin objects.
*   **buzzer**: PWM object on GP15.
*   **UNIT**: The base timing unit (0.2s).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn_dot** (GP10), **btn_dash** (GP11), and **buzzer** (GP15).
    *   Set **UNIT** to **0.2**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Check Dot Trigger**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **btn_dot** is HIGH.
    *   **Action**:
        *   Turn **buzzer** ON (Freq: 1000, Duty: 50).
        *   Wait **UNIT** seconds.
        *   Turn **buzzer** OFF (Duty: 0).
        *   Wait **UNIT** seconds (Gap).
        *   Wait while **btn_dot** is HIGH (Prevents repetitive firing).
4.  **Check Dash Trigger**:
    *   Below the first check, drag another **`controls_if`**.
    *   **Condition**: Check if **btn_dash** is HIGH.
    *   **Action**:
        *   Turn **buzzer** ON (Freq: 1000, Duty: 50).
        *   Wait **UNIT * 3** seconds.
        *   Turn **buzzer** OFF (Duty: 0).
        *   Wait **UNIT** seconds (Gap).
        *   Wait while **btn_dash** is HIGH.
5.  **Scan Rate**:
    *   Wait **0.05** seconds.

### 9. Execution Flow
1.  **Selection**: You decide to send the letter "A" (Dot-Dash).
2.  **Action 1**: Tap Button A. Even if you press it for 0.001s, the Buzzer plays a perfect 0.2s Dot.
3.  **Action 2**: Tap Button B. The Buzzer plays a perfect 0.6s Dash.
4.  **Logic Lock**: The `while button is HIGH` check ensures you don't accidentally send 10 Dots by holding the button down too long.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Initialization
btn_dot = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn_dash = Pin(11, Pin.IN, Pin.PULL_DOWN)
buzz = PWM(Pin(15))
UNIT = 0.2

while True:
    # 1. Automate DOT
    if btn_dot.value() == 1:
        buzz.freq(1000)
        buzz.duty_u16(32768) # 50%
        time.sleep(UNIT)
        buzz.duty_u16(0)
        time.sleep(UNIT)
        # Lockout until release
        while btn_dot.value() == 1:
            time.sleep(0.01)

    # 2. Automate DASH
    if btn_dash.value() == 1:
        buzz.freq(1000)
        buzz.duty_u16(32768)
        time.sleep(UNIT * 3)
        buzz.duty_u16(0)
        time.sleep(UNIT)
        # Lockout until release
        while btn_dash.value() == 1:
            time.sleep(0.01)

    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Forgetting the Gap**: Not putting a `time.sleep(UNIT)` after turning the buzzer OFF. Without it, if you press two dots quickly, they will merge into one longer sound.
*   **Frequency Errors**: Setting the frequency to 0 instead of setting the duty to 0 to stop the sound. Setting frequency kills the PWM carrier; setting duty keeps it ready but silent.
*   **The Race Condition**: If you press both buttons at the exact same time, the code will prioritize the "Dot" because it checks that IF statement first.

### 12. Try This Next
*   **Visual Confirmation**: Turn on an LED (GP14) every time the buzzer sounds.
*   **Variable Pitch**: Make the Dash button use a higher frequency (2000Hz) and the Dot button use a lower one (800Hz) to distinguish between them aurally.
*   **Word Space Button**: Add a 3rd button (GP12) that just waits for `UNIT * 7` seconds without sounding the buzzer.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log. Updated 0093 to use PWM for buzzer logic.
- Date Verified: 2026-01-13
---

## Project 0094: Modular Morse (Function-Based Signaling)
