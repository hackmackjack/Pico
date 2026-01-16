## Project 0095: Morse Rhythm Game (Pattern Recognition)

### 2. Learning Objective
Pattern recognition and interactive state management. Build a game where the Pico randomly chooses a Morse code letter (e.g., A or B), flashes it on an LED, and evaluates if the user's button choice matches the hidden challenge.

### 3. Concepts Introduced
*   **Pattern Recognition**: Challenging the user's ability to identify time-encoded sequences (Short vs. Long).
*   **Randomized Logic**: Using the `random integer` block to ensure the game is different every time.
*   **Input Blocking**: Creating a "Wait for Input" state where the code pauses execution until the user makes a choice.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED (Signaling)**
*   **2x Push Buttons (Player Inputs)**
*   **1x 220Ω Resistor**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn A (Option 0)** | GP10 | Player's first choice |
| **Btn B (Option 1)** | GP11 | Player's second choice |
| **LED** | GP15 | Visual Signal |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (comparison)
*   From **Logic & Math**, drag **`random integer from _ to _`** (randomization)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)

### 7. Variables
*   **btn_a, btn_b, led**: Pin objects.
*   **choice**: The random target (0 for "A", 1 for "B").
*   **guess**: The user's input (-1 until pressed).
*   **UNIT**: The base timing unit (0.2s).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Constants**:
    *   Initialize **btn_a** (GP10), **btn_b** (GP11), and **led** (GP15).
    *   Set **UNIT** to **0.2**.
    *   **Snap** into the **`start`** block.

**B. Messaging Phase**
2.  **Generate Challenge**:
    *   From **Smart IO**, drag a **`pico_forever`**.
    *   Set **choice** to a **random integer** from **0** to **1**.
3.  **Flash the Pattern**:
    *   If **choice** is **0** (Letter A: .-): Turn **led** ON -> Wait **UNIT** -> OFF -> Wait **UNIT** -> ON -> Wait **UNIT * 3** -> OFF.
    *   Else (Letter B: -...): Flash one long (UNIT * 3) and three short (UNIT) pulses.
4.  **Wait for Answer**:
    *   Set **guess** to **-1**.
    *   Drag a **`controls_whileUntil`** (while **guess** = -1).
    *   Inside the while loop:
        *   If **pico_gpio_read(btn_a)** is HIGH: Set **guess** to **0**.
        *   If **pico_gpio_read(btn_b)** is HIGH: Set **guess** to **1**.
        *   Wait **0.01s** (Scan rate).
5.  **Evaluate and Repeat**:
    *   If **guess** equals **choice**: Log "CORRECT!" to the console.
    *   Else: Log "WRONG! It was choice " + **choice**.
    *   Wait **2.0** seconds before starting the next round.

### 9. Execution Flow
1.  **Thinking**: Pico picks "1" (Dash-Dot-Dot-Dot).
2.  **Signal**: The LED flashes one long and three shorts.
3.  **Waiting**: The code stops and polls the buttons.
4.  **Action**: You press Button B (Option 1).
5.  **Judgment**: `guess` (1) == `choice` (1). You win!
6.  **Cooldown**: A 2-second pause allows you to check the log before the next flash.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
led = Pin(15, Pin.OUT)
btn_a = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(11, Pin.IN, Pin.PULL_DOWN)
UNIT = 0.2

while True:
    # 1. Randomly pick A (0) or B (1)
    choice = random.randint(0, 1)

    # 2. Transmit challenge
    if choice == 0: # A (.-)
        led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)
        led.value(1); time.sleep(UNIT * 3); led.value(0)
    else: # B (-...)
        led.value(1); time.sleep(UNIT * 3); led.value(0); time.sleep(UNIT)
        for _ in range(3):
            led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)

    # 3. Blocking Wait for Input
    guess = -1
    while guess == -1:
        if btn_a.value() == 1:
            guess = 0
        elif btn_b.value() == 1:
            guess = 1
        time.sleep(0.01)

    # 4. Feedback
    if guess == choice:
        print("MATCH! Correct decoding.")
    else:
        print("FAIL! You selected the wrong character.")

    time.sleep(2)
```

### 11. Common Mistakes
*   **Double-Tap**: If the user holds the button too long, the next round might pick up the same press as the new `guess`. Always ensure the user has released the button before continuing.
*   **Variable Scope**: Forgetting to reset `guess` to -1 at the start of every loop. If you don't, the game will automatically "guess" based on the last round's answer.
*   **Complexity Gap**: Using letters that are too similar (like E and I) for beginners. Start with distinct patterns like dot-only vs dash-only.

### 12. Try This Next
*   **Score Counter**: Create a `score` variable that increases with every correct answer.
*   **Difficulty Scaling**: Reduce the `UNIT` time (making patterns faster) every time the player gets three in a row correct.
*   **Sound Hints**: Use a Buzzer to play the pattern while it flashes, helping the user learn via audio/visual cues.

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
---

## Project 0096: Optical Morse Link (Light Communication)
