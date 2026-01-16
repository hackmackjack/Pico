## Project 0076: Disqualifier (False Start Detector)

### 2. Learning Objective
Negative constraints and state polling within loops. Develop a reaction game that monitors for button presses *during* the wait period and triggers a "Foul" animation if the player jumps the gun.

### 3. Concepts Introduced
*   **Prohibited Action Sensing**: Detecting and reacting to inputs that occur during restricted intervals.
*   **State Flagging**: Using a boolean (`foul`) to remember an event that happened earlier and affect future code branches.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Red LED**
*   **1x Green LED**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Reaction Input (Pull-Down) |
| **Red LED** | GP14 | "Wait" / Foul Indicator |
| **Green LED** | GP15 | "GO!" Indicator |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_flow_statements`** (break)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Logic & Math**, drag **`true`** / **`false`** (boolean)
*   From **Smart IO**, drag **`get current time (ms)`** (ticks_ms)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_gpio_toggle`** (toggle Pin ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Text**, drag **`""`** (text string)

### 7. Variables
*   **btn, red, grn**: Pin objects for hardware.
*   **foul**: Boolean variable set to True if the player presses too early.
*   **wait_end**: Number variable marking the end of the random delay.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables for **btn**, **red**, **grn**, **foul**, and **wait_end**.
    *   Initialize **btn** (GP10), **red** (GP14), **grn** (GP15).
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Prepare Run**:
    *   From **Smart IO**, set **red** to HIGH and **grn** to LOW.
    *   From **Variables**, set **`foul`** to **false**.
    *   From **Variables**, set **`wait_end`** to (**`get current time (ms)`** + **math_random_int(2000, 5000)**).
4.  **Early Press Surveillance**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **`get current time (ms)`** < **`wait_end`**.
    *   **Action**: Inside, check if **btn** is HIGH. If true: Set **`foul`** to **true** and **break** the loop.
5.  **Reaction Logic**:
    *   If **`foul`** is **true**:
        *   **pico_log**: "FALSE START! Penalty applied!".
        *   Repeat **10** times: Toggle **red** and wait **0.05** seconds.
    *   **Else (Clean Wait)**:
        *   Set **red** to **LOW** and **grn** to **HIGH**.
        *   **Loops**: Wait while **btn** is LOW.
        *   **pico_log**: "Success! Fast reaction!".
6.  **Cycle Reset**:
    *   From **Smart IO**, wait **2.0** seconds before starting the next round.

### 9. Execution Flow
1.  **Tension**: Red light is on. The buzzer might even beep once (Project Upgrade).
2.  **Jump**: If you press the button during the 2-5s window, the code catches the Foul state.
3.  **Go**: If you are patient, the light turns Green.
4.  **Reaction**: The code now waits for your winning press.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
red = Pin(14, Pin.OUT)
grn = Pin(15, Pin.OUT)

while True:
    red.value(1)
    grn.value(0)
    foul = False

    # Calculate a random wait between 2 and 5 seconds
    wait_ms = random.randint(2000, 5000)
    start_wait = time.ticks_ms()

    # Monitoring loop
    while time.ticks_diff(time.ticks_ms(), start_wait) < wait_ms:
        if btn.value() == 1:
            foul = True
            break
        time.sleep(0.01)

    if foul:
        print("FALSE START! DQ!")
        for _ in range(10): # Angry Red flash
            red.toggle()
            time.sleep(0.05)
    else:
        # Success, turn on Green
        red.value(0)
        grn.value(1)

        # Wait for actual reaction
        while btn.value() == 0:
            time.sleep(0.01)
        print("Nice Start!")

    time.sleep(2) # Cooldown
```

### 11. Common Mistakes
*   **The Wait Trap**: If you use `time.sleep(3)`, the Pico literally sleeps; it cannot check for a false start. You *must* use a `while` loop with a timer check and an `if btn` check inside.
*   **Foul Scope**: If you don't reset `foul = False` at the top of the loop, once you jump the gun once, every subsequent round will be a foul.
*   **Wait Persistence**: Ensure the `while not btn.value()` (green phase) doesn't accidentally trigger if the player's finger is still moving from a "barely" foul press.

### 12. Try This Next
*   **Disqualification Lockout**: If a foul occurs, wait 5 seconds before the next round to punish the player.
*   **Sound Effects**: Play a low "Buzz" on foul and a high "Beep" on success.
*   **Speed Meter**: Combine with Project 0073 to tell the player exactly how fast they reacted.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Loops and Logic & Math, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax.
- Date Verified: 2026-01-08
---

## Project 0077: Defuse Wire (Boolean Logic)
