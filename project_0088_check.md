---## Project 0088: Guess the Number (Select & Submit)

### 2. Learning Objective
Multi-button logic and random outcome evaluation. Create a game where the Pico hiddenly picks a random number, and the player uses one button to cycle through guesses and another button to submit their final answer.

### 3. Concepts Introduced
*   **Action Separation**: Using distinct physical inputs for data entry (`guess += 1`) versus data validation (`submit`).
*   **Evaluating Random State**: Comparing user-generated variables against a system-generated random target.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **2x Push Buttons**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Select** | GP10 | Increment Guess |
| **Btn Submit** | GP11 | Confirm Guess |
| **LED** | GP15 | Success Signal |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] = [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`random integer from 1 to 5`** (math_random_int)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*    From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_gpio_toggle`** (toggle Pin)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **btn_select, btn_submit, led**: Pin objects.
*   **target**: The hidden random number (1 to 5).
*   **guess**: The player's current count of button presses.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn_select** (GP10), **btn_submit** (GP11), and **led** (GP15).
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **New Game Setup**:
    *   Set **target** to **random integer from 1 to 5**.
    *   Set **guess** to **0**.
    *   **pico_log**: "Game Start! Guess a number between 1 and 5.".
4.  **The Input Phase**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **pico_gpio_read** for **btn_submit** equals **0** (Not pressed).
    *   **Action**:
        *   If **btn_select** is HIGH:
            *   Change **guess** by **1**.
            *   **pico_log**: "Current Guess: " + **guess**.
            *   Wait while **btn_select** is HIGH (Debounce).
        *   Wait **0.05** seconds.
5.  **The Judgment Phase**:
    *   From **Logic & Math**, drag a **`controls_if`** with **else**.
    *   **Condition**: Check if **guess** == **target**.
    *   **Action (If - Correct)**:
        *   **pico_log**: "WINNER! The number was " + **target**.
        *   From **Loops**, repeat **10** times: **pico_gpio_toggle** for **led**, wait **0.1s**.
    *   **Action (Else - Wrong)**:
        *   **pico_log**: "SORRY! You guessed: " + **guess** + " but it was: " + **target**.
6.  **Game Reset**:
    *   Wait **2.0** seconds before starting a new round.

### 9. Execution Flow
1.  **Thinking**: Pico picks a target (e.g., 4).
2.  **Select**: You press Button A four times. Console logs "1, 2, 3, 4".
3.  **Submit**: You press Button B.
4.  **Victory**: The LED flashes rapidly, and the console confirms your win.
5.  **Failure**: If you pressed Button A six times, the console would reveal you lost and show the correct number.

### 10. Generated Code
```python
from machine import Pin
import time
import random

# Initialization
btn_select = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn_submit = Pin(11, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

while True:
    # 1. New Target
    target = random.randint(1, 5)
    guess = 0
    print("New Game: Guess 1 to 5. Press Select, then Submit.")

    # 2. Input Phase
    while btn_submit.value() == 0:
        if btn_select.value() == 1:
            guess += 1
            print("Current Guess:", guess)
            while btn_select.value() == 1:
                time.sleep(0.01)
        time.sleep(0.05)

    # 3. Validation Phase
    if guess == target:
        print("YES! Correct Answer:", target)
        for _ in range(10):
            led.toggle()
            time.sleep(0.1)
        led.value(0)
    else:
        print("NO! You guessed", guess, "but it was", target)

    time.sleep(2)
```

### 11. Common Mistakes
*   **Guess Overflow**: If you press the select button 10 times, you can't go back! The logic only adds. You must submit and start a new game.
*   **The Submit Signal**: If your submit button is shaky, it might submit "0" before you even start guessing. Ensure high-quality button connections.
*   **Infinite Toggling**: Using a `repeat` loop for the LED is safer than a while loop, ensuring the game actually restarts.

### 12. Try This Next
*   **Higher Stakes**: Increase the target range from `1 to 10`.
*   **Penalty**: Add a buzzer that sounds if you guess wrong.
*   **Lives**: Give the user 3 submits per target before picking a new number.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---

## Project 0089: Magnitude Counter (Coin Sorter)
