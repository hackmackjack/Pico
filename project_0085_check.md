## Project 0085: Step Tracker (Tilt Counter)

### 2. Learning Objective
Edge-triggered events and sensor debounce. Build a basic pedometer using a tilt Switch to detect physical "steps" by monitoring changes in a mechanical ball-and-switch circuit.

### 3. Concepts Introduced
*   **Edge Detection (Rising Edge)**: Counting only when a signal changes from LOW to HIGH (or vice versa), rather than counting while it stays HIGH.
*   **State History**: Comparing the `current_state` of a pin against its `last_state` to recognize an event.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Tilt Sensor (SW-520D)**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tilt Sensor** | GP10 | Input Trigger (Pull-Up) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if)
*   From **Logic & Math**, drag **`[X] != [Y]`** (logic_compare)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **tilt**: Pin object initialized on GP10 (Pull-Up mode).
*   **steps**: Number variable tracking the total count.
*   **last_state**: Number variable recording the previous reading of the sensor.
*   **current_state**: Number variable recording the newest reading of the sensor.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **tilt** on **GP10**. Use **Pull-Up** because the sensor acts as a switch.
    *   Set **steps** to **0**.
    *   Set **last_state** to the result of **pico_gpio_read** for **tilt**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Trigger Detection**:
    *   From **Variables**, set **`current_state`** to **pico_gpio_read** for **tilt**.
4.  **The Change Logic**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **`current_state`** != **`last_state`**.
    *   **Action**:
        *   Inside, add another **`controls_if`**.
        *   **Condition**: Check if **`current_state`** equals **1**.
        *   **Action**:
            *   Change **steps** by **1**.
            *   **pico_log**: "Step Count: " + **steps**.
        *   Set **`last_state`** to **`current_state`**.
        *   Wait **0.1** seconds (Mechanical Ball switch debounce).
5.  **Scan Rate**:
    *   Wait **0.01** seconds before the next check.

### 9. Execution Flow
1.  **Stationary**: The ball is still. `current` matches `last`. Nothing happens.
2.  **Shake**: You move the device. The ball breaks contact.
3.  **Detect**: The IF block sees the difference. Because it changed to 1, it adds a step.
4.  **Lock**: The code updates `last_state`, so even if you keep the device tilted, it won't count again until it changes back.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
tilt = Pin(10, Pin.IN, Pin.PULL_UP)
steps = 0
last_state = tilt.value()

while True:
    current = tilt.value()

    # Check for state change (The "Edge")
    if current != last_state:
        # Check if the change was specifically a "switch close" (or open depending on wiring)
        if current == 1:
            steps += 1
            print("Movement Detected! Total Steps:", steps)

        # Update memory for next loop
        last_state = current

        # Debounce: Stop mechanical bounce from double-counting
        time.sleep(0.1)

    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Ghost Steps**: Shaking the device extremely violently can cause the ball to bounce multiple times in 0.1s. Adjust the debounce wait to a larger value (0.2s) if it double-counts.
*   **Pin Floating**: If you use `Pin.IN` without `PULL_UP`, the sensor will give random values and count thousands of steps while sitting on the table.
*   **Inverted Logic**: Depending on your sensor orientation, it might count when you put it down instead of when you pick it up. Swap `current == 1` to `current == 0` to invert the trigger.

### 12. Try This Next
*   **Goal Indicator**: Turn on an LED (GP15) when the user reaches 100 steps.
*   **Reset Key**: Add a physical button (GP11) to set the step count back to 0.
*   **Energy Burn**: Calculate "Calories" by multiplying `steps` by a small constant (e.g., 0.04) and print both.

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
## Project 0086: Capacity Guard (Occupancy Counter)
