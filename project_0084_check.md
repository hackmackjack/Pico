## Project 0084: Binary Counter (3-Bit Display)

### 2. Learning Objective
Binary number representation and bitwise data visualization. Create a counting system that increments from 0 to 7 and displays the value as a 3-bit binary pattern using three LEDs.

### 3. Concepts Introduced
*   **Binary Base-2 System**: Using combinations of On/Off states to represent numbers larger than 1.
*   **Bitwise Extraction**: Using mathematical operations (AND/Shift) to isolate specific bits within a larger number for hardware reporting.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Push Button**
*   **3x LEDs (Preferably different colors)**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Count Increment (Pull-Down) |
| **LED 1 (LSB)** | GP13 | Bit 0 (Value: 1) |
| **LED 2** | GP14 | Bit 1 (Value: 2) |
| **LED 3 (MSB)** | GP15 | Bit 2 (Value: 4) |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`controls_if`** (if)
*   From **Logic & Math**, drag **`math_arithmetic`** (operation: modulo)
*   From **Logic & Math**, drag **`math_bitwise`** (bitwise AND / Shift)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)

### 7. Variables
*   **btn**: Pin object for input.
*   **led0, led1, led2**: Pin objects for binary outputs.
*   **count**: Number variable (0 to 7).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn** (GP10), **led0** (GP13), **led1** (GP14), and **led2** (GP15).
    *   Set **count** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Cyclic Increment**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **pico_gpio_read** for **btn** is 1.
    *   **Action**:
        *   Set **count** to (**count** + 1) **modulo** 8.
        *   **pico_log**: "Binary State: " + **count**.
        *   Wait while **btn** is HIGH (Debounce).
4.  **Bitwise Rendering**:
    *   From **Smart IO**, drag three **`pico_gpio_write`** blocks.
    *   **LED 0**: Set to (**count** Bitwise AND 1).
    *   **LED 1**: Set to ((**count** Bitwise Shift Right 1) Bitwise AND 1).
    *   **LED 2**: Set to ((**count** Bitwise Shift Right 2) Bitwise AND 1).
5.  **Scan Rate**:
    *   Wait **0.05** seconds.

### 9. Execution Flow
1.  **0**: Count is 0 (000 in binary). All LEDs are Off.
2.  **1**: Press button. Count is 1 (001). LED 0 turns On.
3.  **2**: Press button. Count is 2 (010). LED 1 turns On, LED 0 turns Off.
4.  **3**: Press button. Count is 3 (011). LED 0 and 1 turn On.
5.  **Wrap**: After 7 (111), the next press returns everything to 0.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
leds = [Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
count = 0

while True:
    if btn.value() == 1:
        # Increment with auto-wrap at 8
        count = (count + 1) % 8
        print("Count:", count, "Binary Display Updated")

        # Extract bits and set LEDs
        for i in range(3):
            bit = (count >> i) & 1
            leds[i].value(bit)

        # Debounce
        while btn.value() == 1:
            time.sleep(0.01)

    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Bit Position**: If the LEDs are wired in the wrong order (LSB on GP15 instead of GP13), the binary pattern will look inverted or nonsensical.
*   **Modulo Math**: Forgetting `modulo 8` will let the count go higher than 7, which will light up "invisible" bits (GP16+) or do nothing, making the display look frozen.
*   **Ghost Bits**: Tapping too fast can cause "flicker" where the binary state changes twice. Ensure you use the debounce loop.

### 12. Try This Next
*   **4-Bit Upgrade**: Add a 4th LED on GP16 and change modulo to 16 to count up to 15.
*   **Gray Code**: Research Gray Code and try to program the LEDs to only change one bit at a time.
*   **Auto-Counter**: Instead of a button, use a `pico_wait` block to make the LEDs count up automatically every 1 second.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log, merged redundant 0084 sections.
- Date Verified: 2026-01-08
---
## Project 0085: Step Tracker (Tilt Counter)
