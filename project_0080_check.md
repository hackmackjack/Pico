## Project 0080: Binary Brain (Cognitive Count)

### 2. Learning Objective
Multi-stage input validation and cognitive-load processing. Build a game that flashes an LED a random number of times, then requires the player to repeat that exact number of button presses within a strictly timed 3-second window.

### 3. Concepts Introduced
*   **Variable Comparison (Final Stage)**: Evaluating a player's collected data (`press_count`) against a predefined target (`flash_count`) only after a time-based trigger.
*   **Cognitive Gating**: Forcing the user to process visual information before allowing physical interaction.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Input (Pull-Down) |
| **LED** | GP15 | Visual Signal |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Smart IO**, drag **`get current time (ms)`** (ticks_ms)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)

### 7. Variables
*   **btn, led**: Pin objects for hardware.
*   **flash_count**: Number variable determining the required presses.
*   **press_count**: Number variable tracking user clicks.
*   **window_end**: Number variable marking the end of the 3s input phase.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables **`btn`**, **`led`**, **`flash_count`**, **`press_count`**, and **`window_end`**.
    *   Initialize **btn** (GP10) and **led** (GP15).
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **The Challenge Phase**:
    *   From **Variables**, set **`flash_count`** to **`random integer from 1 to 5`**.
    *   From **Loops**, drag a **`controls_repeat_ext`**. Set to **`flash_count`**.
    *   **Action**: Inside, turn **led** HIGH, wait **0.2s**, turn **led** LOW, wait **0.2s**.
4.  **The Input Phase**:
    *   From **Variables**, set **`press_count`** to **0**.
    *   From **Variables**, set **`window_end`** to (**`get current time (ms)`** + **3000**).
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **`get current time (ms)`** < **`window_end`**.
    *   **Action**:
        *   If **btn** is HIGH:
            *   Change **`press_count`** by **1**.
            *   Wait while **btn** is HIGH (Debounce).
        *   Wait **0.01** seconds.
5.  **The Judgment Phase**:
    *   From **Logic & Math**, drag a **`controls_if`** (with **else**).
    *   **Condition**: Check if **`press_count`** == **`flash_count`**.
    *   **Action (If - Correct)**:
        *   **pico_log**: "Correct! Binary Brain active.".
        *   Wait **2.0** seconds.
    *   **Action (Else - Wrong)**:
        *   **pico_log**: "Wrong! Expected: " + **flash_count**.
6.  **Cycle Reset**:
    *   Wait **2.0** seconds before restarting.

### 9. Execution Flow
1.  **Watch**: The LED flashes 4 times.
2.  **Think**: "Okay, I need to press the button 4 times."
3.  **Act**: You press the button 1, 2, 3, 4 times during the 3-second window.
4.  **Result**: After the timer runs out, the Pico compares the totals and tells you if you won.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

while True:
    # 1. Flash the challenge
    target = random.randint(1, 5)
    print("Watch carefully...")
    for _ in range(target):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    print("GO! Repeat the count.")
    press_count = 0
    window_ms = 3000
    start_input = time.ticks_ms()

    # 2. Collect inputs for 3 seconds
    while time.ticks_diff(time.ticks_ms(), start_input) < window_ms:
        if btn.value() == 1:
            press_count += 1
            # Wait for release
            while btn.value() == 1:
                time.sleep(0.01)
        time.sleep(0.01)

    # 3. Judge
    if press_count == target:
        print("Success! Correct count.")
    else:
        print("Fail! Expected", target, "but got", press_count)

    time.sleep(2)
```

### 11. Common Mistakes
*   **The Phantom Press**: Tapping the button before the LED finishes flashing. The code only starts counting *after* the `repeat` loop ends.
*   **Time's Up**: If you press too slowly, the 3-second window closes before you finish your count. Ensure you press quickly!
*   **Release Gating**: If you don't use the `while btn == 1` release check, the Pico will count one long press as hundreds of clicks.

### 12. Try This Next
*   **Speed Up**: Reduce the input window to 1.5 seconds to increase difficulty.
*   **Color Math**: Add a second LED (GP14). Red blinks = Subtract, Green blinks = Add.
*   **Life System**: Lose a life for every wrong answer. 3 lives = Permanent Game Over.

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

# Batch 9: Counting Machine 1

## Project 0081: Digital Tally (Basic Counter)
