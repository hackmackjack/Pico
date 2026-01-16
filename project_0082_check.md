## Project 0082: Visual Tally (Blinking Count)

### 2. Learning Objective
Data visualization through timed sequences. Create a device that increments a counter on button press and provides immediate physical feedback by blinking an LED a number of times equal to the current total.

### 3. Concepts Introduced
*   **Sequence Feedback**: Iterating a physical signal (light) based on a dynamic data value.
*   **Blocking Interaction**: Understanding that the program cannot read new inputs while it is "busy" executing a blink sequence.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **1x Push Button**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Input Trigger |
| **LED** | GP15 | Visual Reporter |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Logic & Math**, drag **`controls_if`** (if)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)

### 7. Variables
*   **btn, led**: Pin objects.
*   **count**: Number variable starting at 0.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn** (GP10, Input/Pull-Down) and **led** (GP15, Output).
    *   Set **count** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Count Input**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **`pico_gpio_read`** for **btn** equals **1**.
    *   **Action**:
        *   Change **count** by **1**.
        *   **pico_log**: "Total Count: " + **count**.
        *   Wait while **btn** is HIGH (Debounce).
4.  **Blink Reporting**:
        *   From **Loops**, drag a **`controls_repeat_ext`**. Set count to variable **count**.
        *   **Inside**: Set **led** HIGH, wait **0.2s**, set **led** LOW, wait **0.2s**.
5.  **Scan Rate**:
    *   Wait **0.1** seconds.

### 9. Execution Flow
1.  **Press**: You tap the button once.
2.  **Log**: The console says "Total Count: 1".
3.  **Flash**: The LED blinks once.
4.  **Repress**: You tap again. Console says "2".
5.  **Report**: The LED blinks twice (Pulse... Pulse).

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)
count = 0

while True:
    if btn.value() == 1:
        count += 1
        print("Blinking count:", count)

        # Debounce
        while btn.value() == 1:
            time.sleep(0.01)

        # Physical Feedback Loop
        for _ in range(count):
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2)

    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Impatient Mashing**: If the count is 5, you have to wait for 2 seconds of blinking to complete before the button will sense your next press. This is a design choice!
*   **Memory Growth**: Without a reset button or logic, your `count` could eventually reach 100, meaning you'd have to wait 40 seconds of blinking for every press.
*   **Pin Mismatch**: Ensure the LED resistor is connected to GP15 as specified in Step 1.

### 12. Try This Next
*   **Double Speed**: Increase blink speed (0.1s On/Off) to reduce the "busy" time.
*   **Count Cap**: If `count` > 5, reset it to 1 automatically.
*   **Buzzer Chime**: Add a buzzer that beeps along with the blinks.

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

## Project 0083: Dual Control (Up/Down Counter)
