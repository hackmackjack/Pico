## Project 0078: Memory Master (Color Sequences)

### 2. Learning Objective
List processing and indexed data retrieval. Create a Simon-style memory game where the Pico generates a 3-step color pattern that the player must repeat exactly using physical buttons.

### 3. Concepts Introduced
*   **Lists / Arrays**: Storing a series of values (patterns) in a single structured variable.
*   **Index Iteration**: Moving through a list one item at a time (For Each loop) to play back or verify data.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **3x LEDs (Red, Yellow, Green)**
*   **3x Push Buttons**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buttons** | GP10-12 | Inputs (Pull-Down) |
| **LEDs** | GP13-15 | Targets |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Loops**, drag **`controls_flow_statements`** (break)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (logic_compare)
*   From **Lists**, drag **`lists_create_with`** (create list with)
*   From **Lists**, drag **`lists_getIndex`** (in list _ get #)
*   From **Lists**, drag **`lists_length`** (length of)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)

### 7. Variables
*   **sequence**: List variable storing the randomly generated pattern (e.g., [1, 3, 2]).
*   **player_choice**: Number recording which button the player just pressed.
*   **current_step**: Number used to index through the list during verification.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables for **sequence**, **player_choice**, and **current_step**.
    *   Initialize Buttons (GP10-12) and LEDs (GP13-15).
    *   Set **sequence** to an **`empty list`** (found in Lists).
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Generate Pattern**:
    *   From **Variables**, set **`sequence`** to **`create list with`** items.
    *   Inside, add 3 **`random integer 1 to 3`** blocks.
4.  **Pattern Playback (Pico's Turn)**:
    *   From **Loops**, drag **`count with [i] from 1 to 3 by 1`**.
    *   **Inside**:
        *   Get the item at index **i** from **sequence**.
        *   Light up the corresponding LED, wait **0.5s**, and turn it off.
        *   Wait **0.2s** (Gap between blinks).
5.  **Input Verification (Player's Turn)**:
    *   From **Loops**, drag another **`count with [j] from 1 to 3 by 1`**.
    *   **Inside**:
        *   Wait for **any** button press (while loop until GP10-12 != 0).
        *   Compare **pressed_wire** to the item at index **j** in **sequence**.
        *   If it matches: Continue.
        *   If it misses: **pico_log** "MISS! Game Over."; Wait 2s; **break** the loop.

### 9. Execution Flow
1.  **Generation**: The Pico "thinks" of a pattern like Red -> Green -> Red.
2.  **Blink**: The LEDs flash that pattern while you watch.
3.  **Match**: You repeat the pattern. The Pico checks each press against its memory.
4.  **Outcome**: If you finish all 3 steps successfully, you win!

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

while True:
    print("Watch the pattern...")
    # Generate 3-step sequence
    sequence = [random.randint(0, 2) for _ in range(3)]

    # 1. Playback
    for idx in sequence:
        leds[idx].value(1)
        time.sleep(0.5)
        leds[idx].value(0)
        time.sleep(0.2)

    print("Your turn!")
    game_over = False

    # 2. Player Input
    for target in sequence:
        pressed = -1
        while pressed == -1:
            for i in range(3):
                if btns[i].value() == 1:
                    pressed = i
                    break
            time.sleep(0.01)

        # Check correctness
        if pressed != target:
            print("WRONG! Game Over.")
            game_over = True
            break

        # Wait for release
        while btns[pressed].value() == 1:
            time.sleep(0.01)

    if not game_over:
        print("PERFECT! Next pattern starting...")

    time.sleep(2)
```

### 11. Common Mistakes
*   **0-Based Lists**: Remember that Python lists start at index 0. If your random number is 1, 2, 3 but your list only has items at 0, 1, 2, your program will crash.
*   **Fast Fingers**: If you press the second button before release the first, the Pico might get confused. Always add a "Wait for release" loop after a successful press.
*   **Playback Speed**: If the playback is too fast, players can't memorize it. 0.5s is a good starting point.

### 12. Try This Next
*   **Extended Play**: Instead of a fixed 3-step sequence, add one new step to the list every time the player succeeds.
*   **Tone Memory**: Add a buzzer that plays a different frequency for each color.
*   **Difficulty Settings**: Make the LEDs blink faster as the sequence gets longer.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math, Loops and Lists, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-08
---

## Project 0079: Ninja Reflex (Wave Detector)
