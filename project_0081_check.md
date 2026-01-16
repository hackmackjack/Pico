## Project 0081: Digital Tally (Basic Counter)

### 2. Learning Objective
Variable incrementing and basic state tracking. Build a simple tally counter that increases a number displayed in the console every time a button is pressed, with a modulo wrap-around at 10.

### 3. Concepts Introduced
*   **Variable Incrementing**: Using `x = x + 1` to track accumulation.
*   **Wrap-Around Logic**: Using conditional checks to reset a value back to zero after reaching a limit (e.g., 10).

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Count Trigger (Pull-Down) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if)
*   From **Logic & Math**, drag **`[X] >= [Y]`** (logic_compare)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **btn**: Pin object initialized as `Pin(10, Pin.IN, Pin.PULL_DOWN)`.
*   **count**: Number variable starting at 0.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables **`btn`** and **`count`**.
    *   Set **`btn`** to **`Pin(10, Pin.IN, Pin.PULL_DOWN)`**.
    *   Set **`count`** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Input Detection**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **`pico_gpio_read`** for **btn** equals **1**.
    *   **Action**:
        *   Inside, from **Variables**, drag **`change [count] by 1`**.
        *   From **Smart IO**, drag a **`pico_log`**. Join string "Count: " with variable **count**.
        *   From **Loops**, drag a **`controls_whileUntil`** (set to **while**). Condition: Check if **btn** is **1**. Action: Wait **0.01** seconds (Debounce/Hold-to-Count prevention).
4.  **Reset Logic**:
    *   Below the input check, drag another **`controls_if`**.
    *   **Condition**: Check if **count** >= **10**.
    *   **Action**: Set **count** to **0**. Log: "Counter Reset to 0".
5.  **Scan Rate**:
    *   Wait **0.05** seconds at the bottom of the forever loop.

### 9. Execution Flow
1.  **Idle**: Wait for a press.
2.  **Action**: Hit the button. The console prints "Count: 1".
3.  **Hold**: If you hold the button, the number does NOT increase repeatedly.
4.  **Limit**: Once you reach 10, the next press resets the number to 0.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
count = 0

while True:
    if btn.value() == 1:
        # Increment
        count += 1
        print("Current Count:", count)

        # Debounce: Wait for button release
        while btn.value() == 1:
            time.sleep(0.01)

    # Reset Logic
    if count >= 10:
        count = 0
        print("Counter Reset to 0")

    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Double Counts**: If you forget the `while btn == 1` loop, the Pico will count dozens of times for a single finger tap because it checks the pin so fast.
*   **Initialization Trap**: If you put `count = 0` inside the `while True` loop, the counter will always stay at 0 or 1 because it resets every fraction of a second.
*   **Variable Names**: Using keywords like `Pin` or `time` as variable names can break your imports. Always use descriptive names like `btn` or `count`.

### 12. Try This Next
*   **Step Change**: Add a second button on GP11. Button A (GP10) adds 1. Button B (GP11) adds 5.
*   **Visual Alert**: Turn on an LED (GP15) only when the count is exactly 5.
*   **Persistent Storage**: (Advanced) Learn how to save the count to a file so it remembers the total even if you unplug the battery.

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
## Project 0082: Visual Tally (Blinking Count)
