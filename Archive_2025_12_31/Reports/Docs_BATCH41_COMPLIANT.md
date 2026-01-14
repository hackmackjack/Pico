# 📚 Pico 2500: Elite Documentation (Projects 0401-0500)

**Documentation Standard**: All projects follow the 12-section Elite Documentation Standard v2.0.

**Source**: Problem statements from `Projects_0401_0500.md` are treated as immutable truth.

---

# 🏁 Batch 41: LED Patterns 3

---

## 1. Project 0401: Introduction to LED Patterns

### 2. Learning Objective
Create a numeric signaling system using repeated LED flashes. You will learn about pulse counting as a communication method and loop-based repetition patterns.

### 3. Concepts Introduced
*   **Binary Blink**: Using pulse count to encode numbers.
*   **Numeric Signaling**: Communicating values through flash repetition.
*   **Wait-Repeat Pattern**: Pausing between message transmissions for clarity.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **LED**
*   **Resistor** (220Ω)

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP16 | With 220Ω resistor to GND |

### 6. Blocks Used
*   **from Loops, drag `pico_repeat`** (repeat N times)
*   **from Smart IO, drag `pico_gpio_write`** (set pin HIGH/LOW)
*   **from Time, drag `pico_wait`** (wait seconds)
*   **from Variables, drag `set_variable`** (store number value)

### 7. Variables
*   **number**: The value to signal (e.g., 5).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LED Pin**:
    *   From **Smart IO**, drag `pico_gpio_setup` and configure GP16 as OUTPUT.
2.  **Set Signal Number**:
    *   From **Variables**, **Set** `number` to `5`.

**B. Main Loop Phase**
3.  **Start Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.
4.  **Flash Sequence**:
    *   From **Loops**, drag `pico_repeat` with variable `number` times.
    *   Inside repeat loop:
        *   From **Smart IO**, **Set** GP16 → HIGH.
        *   From **Time**, **Wait** 0.3 seconds.
        *   From **Smart IO**, **Set** GP16 → LOW.
        *   From **Time**, **Wait** 0.3 seconds.
5.  **Inter-Message Pause**:
    *   From **Time**, **Wait** 2 seconds (outside the repeat loop).

### 9. Execution Flow
The LED flashes 5 times in quick succession (on 0.3s, off 0.3s), then waits 2 seconds. This pattern repeats indefinitely. An observer can count the flashes to determine the encoded number. This is useful for simple numeric communication without displays or serial output.

### 10. Generated Code
```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
number = 5

while True:
    # Flash 'number' times
    for _ in range(number):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)
    
    # Wait before next transmission
    time.sleep(2)
```

### 11. Common Mistakes
*   **Flashes Blend Together**: If you can't count individual flashes, increase the off-time to 0.5s.
*   **Continuous Flashing**: Ensure the 2-second pause is outside the `for` loop, not inside.

### 12. Try This Next
*   **Variable Signal**: Use a button to increment the number, then signal the new value.
*   **Morse Numbers**: Encode digits 0-9 using Morse code patterns instead of simple counts.

---
