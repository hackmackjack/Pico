import os

def create_project_0501():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    content = """#  Pico 2500: Documentation (Projects 0501-0600)

---

#  Batch 51: Digital Art 3

## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create an RGB strobe effect with precise timing control (flash ON for 50ms, OFF for 100ms).

### 3. Concepts Introduced
*   Strobe Effect (Rapid switching)
*   RGB LED Control (Simultaneous channels)
*   Precise Timing (Milliseconds)
*   Infinite Loops (`while True`)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x 220Ω Resistors
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | Connected via 220Ω resistor |
| **Green LED** | GP17 | Connected via 220Ω resistor |
| **Blue LED** | GP18 | Connected via 220Ω resistor |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: This project controls output pins directly without state variables.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_gpio_write` Pin GP16 (Red), GP17 (Green), and GP18 (Blue).

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Turn ON (White Flash)**:
    *   From **Smart IO**, **Set** `pico_gpio_write` (Red) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Green) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Blue) to **HIGH**.
4.  **Wait**:
    *   From **Time**, **Wait** 0.05 seconds.
5.  **Turn OFF**:
    *   From **Smart IO**, **Set** `pico_gpio_write` (Red) to **LOW**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Green) to **LOW**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Blue) to **LOW**.
6.  **Wait Again**:
    *   From **Time**, **Wait** 0.1 seconds.

### 9. Execution Flow
1.  **Start**: The Pico powers up and configures GP16, GP17, and GP18 as outputs.
2.  **Process**: The code enters the main loop.
3.  **Output**: All three LEDs turn HIGH simultaneously (creating white light).
4.  **Delay**: The system waits for 0.05 seconds (flash).
5.  **Output**: All three LEDs turn LOW.
6.  **Delay**: The system waits for 0.1 seconds (darkness).
7.  **Repeat**: The process jumps back to Step 3 instantly.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialize RGB pins
red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)

while True:
    # Turn ON (White)
    red.on()
    green.on()
    blue.on()
    time.sleep(0.05)
    
    # Turn OFF
    red.off()
    green.off()
    blue.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Wrong Timing**: Using seconds instead of milliseconds (e.g., `time.sleep(50)` instead of `0.05`).
*   **Photosensitivity**: This project creates flashing lights—avoid if sensitive.
*   **Missing Resistors**: Connecting LEDs directly to 3.3V can burn them out.

### 12. Try This Next
*   **Colored Strobe**: Change the code to flash only Red or Blue.
*   **Variable Speed**: Add a potentiometer to control the delay time.
"""
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Project 0501 created with Elite Standard v2.0 (Strict Compliance).")

if __name__ == "__main__":
    create_project_0501()
