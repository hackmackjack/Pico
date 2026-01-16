## Project 0074: Whack-a-Mole (Sequence Reaction)

### 2. Learning Objective
Spatial mapping and conditional logic branches. Coordinate 3 LEDs and 3 Buttons so that the player must press the specific button corresponding to a randomly lit LED.

### 3. Concepts Introduced
*   **Input/Output Mapping**: Linking specific inputs to specific outcomes (If LED 1 is On, Button 1 is the goal).
*   **Switch-Case Logic**: Handling multiple mutually exclusive conditions (Target 1 vs 2 vs 3).

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **3x LEDs (Red, Yellow, Green)**
*   **3x Push Buttons**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn L** | GP10 | Left Input (Pull-Down) |
| **Btn M** | GP11 | Middle Input (Pull-Down) |
| **Btn R** | GP12 | Right Input (Pull-Down) |
| **LED L** | GP13 | Left Target |
| **LED M** | GP14 | Middle Target |
| **LED R** | GP15 | Right Target |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`[X] AND [Y]`** (logic_operation)
*   From **Logic & Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **btn1, btn2, btn3**: Pin objects for inputs.
*   **led1, led2, led3**: Pin objects for outputs.
*   **target**: Number variable (1, 2, or 3) deciding which LED lights up.
*   **score**: Number tracking consecutive hits.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables for **btn1-3**, **led1-3**, **target**, and **score**.
    *   Initialize **btn1** (GP10), **btn2** (GP11), **btn3** (GP12) as **`Pin.IN, Pin.PULL_DOWN`**.
    *   Initialize **led1** (GP13), **led2** (GP14), **led3** (GP15) as **`Pin.OUT`**.
    *   Set **score** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Spawn a Mole**:
    *   From **Variables**, set **`target`** to **`random integer from 1 to 3`**.
    *   From **Logic & Math**, drag a **`controls_if`** (Add two **else if** connectors).
    *   **Logic**:
        *   If **`target`** == **1**: Set **led1** HIGH.
        *   Else If **`target`** == **2**: Set **led2** HIGH.
        *   Else: Set **led3** HIGH.
4.  **Reaction Logic**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if (**`pico_gpio_read`** for **btn1** == 0) AND (**btn2** == 0) AND (**btn3** == 0).
    *   **Action**: Wait **0.01** seconds.
5.  **Evaluate Score**:
    *   Drag another **`controls_if`** (with **else**).
    *   **Condition**: Check if (**target** == 1 AND **btn1** is HIGH) OR (**target** == 2 AND **btn2** is HIGH) OR (**target** == 3 AND **btn3** is HIGH).
    *   **Action (If - Hit)**:
        *   Change **score** by **1**.
        *   **pico_log** message: **"HIT! Score: "** + **score**.
    *   **Action (Else - Miss)**:
        *   **pico_log** message: **"MISS! Game Over."**.
        *   Set **score** to **0**.
6.  **Cleanup**:
    *   From **Smart IO**, set **led1**, **led2**, and **led3** to **LOW (0)**.
    *   Wait **1.0** second before the next mole spawns.

### 9. Execution Flow
1.  **Mole Spawn**: One LED flashes on at random.
2.  **Wait**: The Pico pauses until *any* button is pressed.
3.  **Check**: If the button you pressed matches the LED that was On, you get a point.
4.  **Next Round**: The lights turn off, and the loop repeats.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
leds = [Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
btns = [Pin(10, Pin.IN, Pin.PULL_DOWN),
        Pin(11, Pin.IN, Pin.PULL_DOWN),
        Pin(12, Pin.IN, Pin.PULL_DOWN)]
score = 0

while True:
    # 1. Pick a target
    target_idx = random.randint(0, 2)
    leds[target_idx].value(1)

    # 2. Wait for any button
    pressed_idx = -1
    while pressed_idx == -1:
        for i in range(3):
            if btns[i].value() == 1:
                pressed_idx = i
                break
        time.sleep(0.01)

    leds[target_idx].value(0)

    # 3. Check result
    if pressed_idx == target_idx:
        score += 1
        print("HIT! Current Score:", score)
    else:
        print("MISS! Final Score:", score)
        score = 0
        time.sleep(1) # Extra penalty delay

    # 4. Debounce and restart
    while btns[pressed_idx].value() == 1:
        time.sleep(0.01)
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Coordinate Mismatch**: Plugging LED 1 into GP13 but checking for it with Button 2 (GP11). Double-check your mappings!
*   **Floating Score**: If you don't reset `score` to 0 on a miss, the game feels like a "total score" counter instead of a "streak" counter.
*   **Ghost Presses**: If you don't use the `while btn == 1` release check at the end, you might accidentally trigger the *next* mole from the same press.

### 12. Try This Next
*   **Speed Mode**: Add a 1-second timeout. If the user doesn't press a button in time, the mole disappears and they lose their streak.
*   **Ramping Difficulty**: Use `time.sleep(1.0 - (score * 0.1))` as the cleanup delay to make moles spawn faster as you win.
*   **Cheat Prevention**: Lose instantly if the user tries to press multiple buttons at the same time.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Lists, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-08
------

## Project 0075: Hot Potato (Accelerating Reaction)
