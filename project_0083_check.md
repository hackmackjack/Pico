## Project 0083: Dual Control (Up/Down Counter)

### 2. Learning Objective
Bi-directional data manipulation and value clamping. Build a counter system with two buttons where one increases the total and the other decreases it, ensuring the value never drops below zero.

### 3. Concepts Introduced
*   **Bi-Directional Input**: Handling multiple input sources that affect the same shared variable.
*   **Value Clamping (Logic Gating)**: Preventing a variable from entering an invalid state (e.g., negative items in a tally).
*   **Dirty Flagging**: Using a boolean (`changed`) to only update the console/display when an actual event occurs, saving processor time.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **2x Push Buttons**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Up** | GP10 | Incrementer (+1) |
| **Btn Down** | GP11 | Decrementer (-1) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if / else if)
*   From **Logic & Math**, drag **`[X] < [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`true`** / **`false`** (boolean)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)

### 7. Variables
*   **btn_up, btn_down**: Pin objects.
*   **count**: Number variable.
*   **changed**: Boolean variable (flag) to trigger a print event.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn_up** (GP10) and **btn_down** (GP11) as inputs.
    *   Set **count** to **0**.
    *   Set **changed** to **false**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Poll Up Button**:
    *   If **pico_gpio_read** for **btn_up** is 1:
        *   Change **count** by **1**.
        *   Set **changed** to **true**.
        *   Wait while **btn_up** is HIGH.
4.  **Poll Down Button**:
    *   If **pico_gpio_read** for **btn_down** is 1:
        *   Change **count** by **-1**.
        *   Set **changed** to **true**.
        *   Wait while **btn_down** is HIGH.
5.  **Clamp & Report**:
    *   If **changed** equals **true**:
        *   **Sub-Check**: If **count** < **0**, set **count** to **0**.
        *   **pico_log**: "New Count: " + **count**.
        *   Set **changed** to **false**.
6.  **Scan Rate**:
    *   Wait **0.05** seconds.

### 9. Execution Flow
1.  **Up**: Tap Button A. Count becomes 1.
2.  **Report**: Message "New Count: 1" appears.
3.  **Down**: Tap Button B. Count becomes 0.
4.  **Floor**: Tap Button B again. Count stays at 0 (Clamped).
5.  **Quiet**: If you don't press anything, the console stays silent (thanks to the flag).

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn_up = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn_down = Pin(11, Pin.IN, Pin.PULL_DOWN)
count = 0

while True:
    changed = False

    # 1. Check Increment
    if btn_up.value() == 1:
        count += 1
        changed = True
        while btn_up.value() == 1:
            time.sleep(0.01)

    # 2. Check Decrement
    if btn_down.value() == 1:
        count -= 1
        changed = True
        while btn_down.value() == 1:
            time.sleep(0.01)

    # 3. Validation & Reporting
    if changed:
        if count < 0:
            count = 0
        print("Current Inventory Count:", count)

    time.sleep(0.05)
```

### 11. Common Mistakes
*   **The Negative Inventory**: Forgetting the `count < 0` check. In a real shop, you can't have -5 apples! Always clamp your minimums.
*   **Dirty Flag Logic**: If you forget to reset `changed = False` at the end of the report block, the Pico will print the same count thousands of times per second.
*   **Hold for Speed**: Because we use `while btn.value()`, you can't hold the button to count fast. To change this, replace the while loop with a small `time.sleep(0.1)` inside the IF.

### 12. Try This Next
*   **Maximum Limit**: Add logic to clamp the high end at 100.
*   **Double Tap Reset**: Check if both buttons are pressed at the exact same time to set count to 0.
*   **Servo Gauge**: Use a Servo (GP15) to point to the current count on a physical dial.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log. Clarified section separation between 0082 and 0083.
- Date Verified: 2026-01-08
---
## Project 0084: Binary Counter (3-Bit Display)
