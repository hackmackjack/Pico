## Project 0086: Capacity Guard (Occupancy Counter)

### 2. Learning Objective
Threshold monitoring and conditional state signaling. Build a system that counts people entering a room and automatically provides a visual red/green status signal based on a predefined occupancy limit.

### 3. Concepts Introduced
*   **Threshold Comparison**: Evaluating if a variable has exceeded a critical mathematical limit (e.g., `people > 5`).
*   **Mutual Exclusion (LEDs)**: Ensuring that only one indicator (Red or Green) is active at any given time.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Green LED**
*   **1x Red LED**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Person Entry Sensor |
| **Green LED** | GP14 | "Safe to Enter" Signal |
| **Red LED** | GP15 | "Capacity Reached" Signal |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] > [Y]`** (logic_compare)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **btn, red, green**: Pin objects.
*   **people**: Number variable tracking room occupancy.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn** (GP10), **green** (GP14), and **red** (GP15).
    *   Set **people** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Entry Detection**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **pico_gpio_read** for **btn** is 1.
    *   **Action**:
        *   Change **people** by **1**.
        *   **pico_log**: "People in Room: " + **people**.
        *   Wait while **btn** is HIGH (Debounce).
4.  **Security Check**:
    *   From **Logic & Math**, drag a **`controls_if`** with an **else**.
    *   **Condition**: Check if **people** > **5**.
    *   **Action (If - Full)**:
        *   Set **red** to HIGH.
        *   Set **green** to LOW.
    *   **Action (Else - Open)**:
        *   Set **red** to LOW.
        *   Set **green** to HIGH.
5.  **Scan Rate**:
    *   Wait **0.05** seconds.

### 9. Execution Flow
1.  **Start**: Room is empty. Green LED is On.
2.  **Entry**: 3 people enter. Green stays On. Console logs counts.
3.  **Warning**: 5 people in the room. This is the limit.
4.  **Capacity**: 6th person enters. The Pico sees `people > 5`. Green turns Off, Red turns On.
5.  **Status**: The light stays Red until the program is reset (or until an exit button is added).

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
green = Pin(14, Pin.OUT)
red = Pin(15, Pin.OUT)
count = 0

while True:
    # 1. Handle Input
    if btn.value() == 1:
        count += 1
        print("Occupancy Update:", count)
        while btn.value() == 1:
            time.sleep(0.01)

    # 2. Update Safety Signal
    if count > 5:
        red.value(1)
        green.value(0)
    else:
        red.value(0)
        green.value(1)

    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Logic Swap**: Putting the Red logic in the `else` and Green in the `if`. Check your conditions carefully: "If OVER limit -> Red".
*   **The 6th Person**: If you want the limit to be 5 inclusive, use `people > 4` or `people >= 5`.
*   **Output Pins**: Ensure Red and Green aren't plugged into the same pin, or they will always be in the same state.

### 12. Try This Next
*   **The Exit Button**: Add a second button on GP11. When pressed, it subtracts 1 from `count`.
*   **Warning Flash**: If `count` is exactly 5, make the Green LED blink slowly to warn that capacity is almost reached.
*   **Maximum Hard-Cap**: Add an `if count > 10` block that sounds a buzzer until someone leaves.

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

## Project 0087: Digital Egg Timer (Interactive Alarm)
