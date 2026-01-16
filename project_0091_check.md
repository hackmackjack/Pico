## Project 0091: SOS Beacon (Morse Code Standard)

### 2. Learning Objective
Standardized timing protocols and time-based encoding. Build an automated distress beacon that flashes an LED with the "SOS" pattern (3 dots, 3 dashes, 3 dots), emphasizing the mathematical ratios between signals.

### 3. Concepts Introduced
*   **Time Encoding**: Using duration to convey meaning (e.g., a "Dash" is exactly three times longer than a "Dot").
*   **Morse Intervals**: Understanding the standard spacing rules: 1 unit between dots/dashes, 3 units between letters, and 7 units between words.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **1x 220Ω Resistor**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP15 | Light Output |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Logic & Math**, drag **`[X] * [Y]`** (arithmetic)

### 7. Variables
*   **led**: Pin object for GP15.
*   **UNIT**: The base time duration (e.g., 0.2 seconds).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **led** on **GP15**.
    *   Set **UNIT** to **0.2**.
    *   **Snap** into the **`start`** block.

**B. Standard Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **The "S" Pattern (Dots)**:
    *   From **Loops**, drag a **`controls_repeat_ext`** (Set to **3**).
    *   Inside: Turn **led** ON -> Wait **UNIT** -> Turn **led** OFF -> Wait **UNIT**.
4.  **Letter Spacing**:
    *   Wait **UNIT * 2** (Makes 3 units total gap between S and O).
5.  **The "O" Pattern (Dashes)**:
    *   From **Loops**, drag a **`controls_repeat_ext`** (Set to **3**).
    *   Inside: Turn **led** ON -> Wait **UNIT * 3** (0.6s) -> Turn **led** OFF -> Wait **UNIT**.
6.  **The "S" Pattern (Repeat)**:
    *   Duplicate the Dot pattern from Step 3.
7.  **Word Reset**:
    *   Wait **3.0** seconds at the end of the loop before repeating the SOS call.

### 9. Execution Flow
1.  **Phase 1 (S)**: Short flashes (...).
2.  **Phase 2 (O)**: Long flashes (---).
3.  **Phase 3 (S)**: Short flashes (...).
4.  **Idle**: Pause for 3 seconds so observers can recognize the end of the message.
5.  **Cycle**: Restart from the beginning.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
led = Pin(15, Pin.OUT)
UNIT = 0.2

while True:
    # 1. Signal 'S' (3 Dots)
    for _ in range(3):
        led.value(1)
        time.sleep(UNIT)
        led.value(0)
        time.sleep(UNIT)

    time.sleep(UNIT * 2) # Inter-letter space

    # 2. Signal 'O' (3 Dashes)
    for _ in range(3):
        led.value(1)
        time.sleep(UNIT * 3)
        led.value(0)
        time.sleep(UNIT)

    time.sleep(UNIT * 2) # Inter-letter space

    # 3. Repeat 'S'
    for _ in range(3):
        led.value(1)
        time.sleep(UNIT)
        led.value(0)
        time.sleep(UNIT)

    # Word gap before repeat
    time.sleep(3)
```

### 11. Common Mistakes
*   **The Dot Gap**: Forgetting to turn the LED OFF for `UNIT` seconds between the dots. Without the gap, three dots just look like one long flash.
*   **Logic Overflow**: Not using the `UNIT` variable for every timing. If you hardcode numbers (0.2, 0.6) and want to speed up the beacon later, you have to change every block instead of just one variable.
*   **Power Drain**: Ensure the resistor is used; otherwise, GP15 might exceed current limits during the long dashes.

### 12. Try This Next
*   **Interactive SOS**: Add a button (GP10). The beacon only starts flashing SOS when the button is pressed (Emerency Switch).
*   **Audio SOS**: Replace the LED Pin with a Buzzer Pin to create an audible alarm.
*   **Variable Speed**: Use a Potentiometer (ADC GP26) to control the `UNIT` speed in real-time.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---
## Project 0092: Manual Telegraph (Button Mirroring)
