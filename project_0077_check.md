## Project 0077: Defuse Wire (Boolean Logic)

### 2. Learning Objective
Boolean decision logic and random state management. Program 3 buttons as "wires" where only one is randomly selected as the "Safe Wire" each round, while the others trigger a "Boom" alarm.

### 3. Concepts Introduced
*   **Match Comparison**: Checking if a user input (Button Index) matches a stored target (Safe Index).
*   **Game Logic Gating**: Separating "Active" time (waiting for input) from "Result" time.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **3x Push Buttons**
*   **1x Passive Buzzer**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn 1** | GP10 | Wire 1 (Pull-Down) |
| **Btn 2** | GP11 | Wire 2 (Pull-Down) |
| **Btn 3** | GP12 | Wire 3 (Pull-Down) |
| **Buzzer** | GP15 | Alarm Output |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_pwm`** (pulse Pin ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Text**, drag **`""`** (text string)

### 7. Variables
*   **btn1, btn2, btn3**: Pin objects.
*   **buzzer**: Pin (or PWM) object for the alarm.
*   **safe_wire**: Number variable (1, 2, or 3) chosen at the start of the round.
*   **pressed_wire**: Number variable recording which button was actually clicked.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables for **btn1-3**, **buzzer**, **safe_wire**, and **pressed_wire**.
    *   Initialize Buttons on **GP10, 11, 12**. Initialize Buzzer on **GP15**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Arm the Device**:
    *   From **Variables**, set **`safe_wire`** to **`random integer from 1 to 3`**.
    *   From **Smart IO**, **pico_log** message: **"ARMED! Choose a wire..."**.
    *   From **Variables**, set **`pressed_wire`** to **0**.
4.  **Wait for Decision**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **`pressed_wire`** == **0**.
    *   **Action**: Inside, check each button. If **btn1** is 1, set **pressed_wire** to 1. If **btn2**, set to 2. If **btn3**, set to 3. (Wait 0.01s).
5.  **Evaluate Outcome**:
    *   From **Logic & Math**, drag a **`controls_if`** (with **else**).
    *   **Condition**: Check if **`pressed_wire`** == **`safe_wire`**.
    *   **Action (If - Defused)**:
        *   **pico_log**: "System Defused. Nice work!".
        *   Wait **2.0** seconds.
    *   **Action (Else - BOOM)**:
        *   **pico_log**: "BOOM! Wrong wire!".
        *   From **Smart IO**, set **buzzer** to **HIGH (1)**.
        *   Wait **1.0** second.
        *   Set **buzzer** to **LOW (0)**.
6.  **Cleanup**:
    *   Wait **1.0** second to let the player release the button.

### 9. Execution Flow
1.  **Logic**: The Pico internally rolls a 3-sided die.
2.  **Tension**: Nothing happens until you physically touch a button.
3.  **Result**: If your choice matches the random die roll, the console congratulates you. Otherwise, the alarm sounds immediately.
4.  **Loop**: The system re-arms with a new secret safe wire.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
btns = [Pin(10, Pin.IN, Pin.PULL_DOWN),
        Pin(11, Pin.IN, Pin.PULL_DOWN),
        Pin(12, Pin.IN, Pin.PULL_DOWN)]
buzzer = Pin(15, Pin.OUT)

while True:
    print("ARMED! Choose a wire (Button 1, 2, or 3)...")
    safe_wire_idx = random.randint(0, 2)
    pressed_idx = -1

    # Wait for player input
    while pressed_idx == -1:
        for i in range(3):
            if btns[i].value() == 1:
                pressed_idx = i
                break
        time.sleep(0.01)

    # Evaluate
    if pressed_idx == safe_wire_idx:
        print("DEFUSED! Correct choice.")
        time.sleep(2)
    else:
        print("BOOM! Game Over.")
        buzzer.value(1)
        time.sleep(1)
        buzzer.value(0)

    # Cool down
    time.sleep(1)
```

### 11. Common Mistakes
*   **Double Trigger**: If you don't wait for the button to be released (`time.sleep(1)` at the end helps), the next round might think you pressed Button 1 again.
*   **0-Index vs 1-Index**: The random block might give 1, 2, 3, but your code might look for 0, 1, 2. Keep your numbering consistent!
*   **Passive Tone**: If using a Passive buzzer with `Pin.value(1)`, you will hear a click instead of an alarm. Use `pico_pwm` for a real siren sound.

### 12. Try This Next
*   **Countdown Mode**: Use a variable to count down from 10 to 0. If the player hasn't pressed a button by 0, trigger the "BOOM" automatically.
*   **Flashy Arming**: Pulse an LED (GP13) while the device is armed to increase pressure.
*   **Fake Defuse**: 1 in 10 chance that even the "safe" wire explodes (Project 0068 tie-in).

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-08
---
### 12. Try This Next
*   **Timer**: Add a 10s countdown. If time runs out, BOOM automatically.
*   **Cut Wire**: Use real wires + breadboard. Pulling a wire from logical High to Low triggers the event.

## Project 0078: Memory Master (Color Sequences)
