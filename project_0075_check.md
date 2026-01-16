## Project 0075: Hot Potato (Accelerating Reaction)

### 2. Learning Objective
Variable-rate sequences and arithmetic logic scaling. Create a game where a buzzer ticks exponentially faster, requiring players to hold a "Safety" button to stay in the game.

### 3. Concepts Introduced
*   **Arithmetic Scaling**: Using mathematical operations to decrease a delay value over time.
*   **Critical Thresholds**: Using a "minimum" value floor (0.1s) to prevent the program from crashing or becoming mathematically impossible.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Passive Buzzer**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Safety Trigger (Pull-Down) |
| **Buzzer** | GP15 | Potato "Ticking" Output |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`[X] > [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`math_arithmetic`** (operation)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_pwm`** (pulse Pin ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Text**, drag **`""`** (text string)

### 7. Variables
*   **btn**: Pin object initialized as `Pin(10, Pin.IN, Pin.PULL_DOWN)`.
*   **buzzer**: PWM object initialized as `PWM(Pin(15))`.
*   **delay_time**: Number variable tracking the current interval between beeps.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables **`btn`**, **`buzzer`**, and **`delay_time`**.
    *   Set **`btn`** to **`Pin(10, Pin.IN, Pin.PULL_DOWN)`**.
    *   Set **`buzzer`** to **`PWM(Pin(15))`**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Wait for Start**:
    *   From **Loops**, drag a **`controls_whileUntil`** (set to **while**). Condition: **btn** is **LOW (0)**. Action: Wait **0.01** seconds.
    *   From **Variables**, set **`delay_time`** to **1.0**.
4.  **Ticking Sequence (Potato Active)**:
    *   From **Loops**, drag another **`controls_whileUntil`** (while).
    *   **Condition**: Check if **`delay_time`** > **0.1**.
    *   **Action**:
        *   Inside, drag a **`controls_if`** (with **else**).
        *   **Condition**: Check if **`pico_gpio_read`** for **btn** equals **1**.
        *   **Action (If - Safe)**:
            *   From **Smart IO**, drag **`pico_pwm`**. Set Freq to **800**, Duty to **50**.
            *   Wait **0.1** seconds.
            *   Set Duty to **0** (Silence).
            *   Wait **`delay_time`** seconds.
            *   From **Variables**, set **`delay_time`** to (**`delay_time`** - **0.05**).
        *   **Action (Else - Dropped)**:
            *   From **Variables**, set **`delay_time`** to **0** (Instant Game Over).
5.  **The Explosion**:
    *   From **Smart IO**, drag **`pico_pwm`**. Freq: **100**, Duty: **50**.
    *   Wait **2.0** seconds.
    *   Set Duty to **0**.
    *   Wait **3.0** seconds before allowing a new game.

### 9. Execution Flow
1.  **Preparation**: Hold the button to start the game.
2.  **Ticking**: The buzzer sounds every 1 second initially.
3.  **Accelerando**: Each successful tick reduces the wait time by 0.05s.
4.  **Danger**: If you let go of the button or the time reaches 0.1s, the buzzer lets out a long low "exploding" growl.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(15))

while True:
    # 1. Wait for player to hold button
    while btn.value() == 0:
        time.sleep(0.01)

    delay_time = 1.0

    # 2. Accelerating Tick Loop
    while delay_time > 0.1:
        if btn.value() == 1:
            # Audible Tick
            buzzer.freq(800)
            buzzer.duty_u16(32768)
            time.sleep(0.05)
            buzzer.duty_u16(0)

            # Scalable wait
            time.sleep(delay_time)

            # Reduce interval
            delay_time -= 0.05
        else:
            # Dropped!
            delay_time = 0

    # 3. Game Over Tone
    buzzer.freq(100)
    buzzer.duty_u16(32768)
    time.sleep(2) # BOOM
    buzzer.duty_u16(0)

    print("Potato Exploded! Game Over.")
    time.sleep(3)
```

### 11. Common Mistakes
*   **Infinite Loop**: If you don't subtract from `delay_time`, the game never ends. Ensure the math block is inside the "Safe" branch.
*   **Variable Reset**: If `delay_time` isn't reset to 1.0 at the start of each game, subsequent games will end instantly because the variable stays at 0.1.
*   **Button Debounce**: Passing the potato requires careful timing. If the code is too fast, a tiny flicker in the button state might count as a "Drop".

### 12. Try This Next
*   **Random Fuse**: Use `math_random_float` to subtract between 0.01 and 0.08 each time to make the explosion unpredictable.
*   **Visual Tension**: Blink an LED (GP14) faster and faster along with the beeps.
*   **Multiplayer Mod**: Require 3 distinct button presses within a short window to "pass" the potato to the next virtual player.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Loops and Logic & Math, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax.
- Date Verified: 2026-01-08
------

## Project 0076: Disqualifier (False Start Detector)
