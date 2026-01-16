## Project 0098: Morse Speed Blitz (Reaction Training)

### 2. Learning Objective
Reflex training and visual pattern recall. Build a trainer that challenges you to identify characters at increasing speeds, testing both your memory of the Morse alphabet and your reaction time.

### 3. Concepts Introduced
*   **Reaction Limit**: Understanding that human processing speed is the bottleneck in real-time communication systems.
*   **Dynamic Variable Update**: Using feedback to change the system's behavior (speeding up or slowing down based on performance).

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **2x Push Buttons**
*   **1x 220Ω Resistor**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn A (Dot)** | GP10 | Input for Dot response |
| **Btn B (Dash)** | GP11 | Input for Dash response |
| **LED** | GP15 | Target Signal |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Loops**, drag **`controls_flow_statements`** (break)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`random integer from _ to _`** (target selection)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)

### 7. Variables
*   **target**: The signal to react to (0 for Dot, 1 for Dash).
*   **speed**: The wait time between flashes (gets shorter).
*   **correct**: Count of successful reactions.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Game State**:
    *   Initialize **btn_dot** (GP10), **btn_dash** (GP11), and **led** (GP15).
    *   Set **speed** to **1.0**.
    *   Set **correct** to **0**.
    *   **Snap** into the **`start`** block.

**B. The Blitz Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Choose Target**:
    *   Set **target** to **random integer 0 to 1**.
4.  **Display Signal**:
    *   If **target** is **0**: Turn **led** ON -> Wait **0.1s** -> OFF.
    *   Else: Turn **led** ON -> Wait **0.4s** -> OFF.
5.  **Catch Reaction**:
    *   From **Variables**, set **guess** to **-1**.
    *   From **Variables**, set **start_time** to **pico_ticks_ms**.
    *   **Drag** a **`controls_whileUntil`** (while **guess** = -1 AND **time_passed** < **speed**):
        *   If **pico_gpio_read(btn_dot)** is HIGH: Set **guess** to **0**.
        *   If **pico_gpio_read(btn_dash)** is HIGH: Set **guess** to **1**.
        *   Wait **0.01s**.
6.  **Scoring and Acceleration**:
    *   If **guess** equals **target**:
        *   Increase **correct** by 1.
        *   Decrease **speed** by **0.05** (Makes it harder next time).
        *   **pico_log** "EXCELLENT! Speed now: " + **speed**.
    *   Else:
        *   **pico_log** "TOO SLOW! Game Over. Final Score: " + **correct**.
        *   Set **speed** to **1.0** and **correct** to **0** (Reset).

### 9. Execution Flow
1.  **Level 1**: LED flashes a quick dot. You tap Button A within 1 second.
2.  **Level 2**: LED flashes again. If you're correct, the time limit drops to 0.95s.
3.  **Climax**: After 10 rounds, the limit is 0.5s. You have to react almost instantly to the flash to stay in the game.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
led = Pin(15, Pin.OUT)
btn_dot = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn_dash = Pin(11, Pin.IN, Pin.PULL_DOWN)

speed = 1.0
correct = 0

while True:
    # 1. New round
    target = random.randint(0, 1)

    # 2. Flash target
    if target == 0:
        led.value(1); time.sleep(0.1); led.value(0)
    else:
        led.value(1); time.sleep(0.4); led.value(0)

    # 3. Capture input within 'speed' seconds
    guess = -1
    start_time = time.ticks_ms()

    while (time.ticks_ms() - start_time) < (speed * 1000):
        if btn_dot.value() == 1:
            guess = 0
            break
        if btn_dash.value() == 1:
            guess = 1
            break
        time.sleep(0.01)

    # 4. Result
    if guess == target:
        correct += 1
        speed = max(0.1, speed - 0.05) # Cap speed at 0.1s
        print("WIN! Current Score:", correct, "| Window:", round(speed, 2), "s")
        time.sleep(1) # Breath between rounds
    else:
        print("FAIL! Game Reset. Total Hits:", correct)
        speed = 1.0
        correct = 0
        time.sleep(3)
```

### 11. Common Mistakes
*   **The Zero-Speed Bug**: Forgetting to use a `max(0.1, speed)` check. Without it, the speed will eventually become 0 or negative, causing a crash.
*   **Reaction Overlap**: Tapping the button so fast that the "release" isn't caught. Ensure a small `time.sleep(0.1)` exists between rounds.
*   **Threshold Preference**: The Dot (0.1s) and Dash (0.4s) timing should be distinct enough. If they are too close, it’s impossible to distinguish them visually at high speed.

### 12. Try This Next
*   **High Score**: Save the highest `correct` count in a variable and compare it every time a user loses.
*   **Audio Targets**: Instead of an LED, use a Buzzer to play the signal.
*   **Combo Bonus**: Give double points if the user reacts in under 0.2 seconds.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---

## Project 0099: Automated Morse Beacon (Low Power Signaling)
