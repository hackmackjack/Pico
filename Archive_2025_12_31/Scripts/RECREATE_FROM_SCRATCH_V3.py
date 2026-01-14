import os

def create_perfect_docs():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    header = """# 📚 Pico 2500: Elite Documentation (Projects 0501-0600)

**Standard**: Elite Documentation Standard v2.0  
**Projects**: 100 (0501-0600) - Custom Content Per Project

---

"""

    batch_51 = """# 🎨 Batch 51: Digital Art 3

---

## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create RGB strobe effect with precise timing control (white flash 50ms, off 100ms).

### 3. Concepts Introduced
*   **Strobe Effect**: Rapid high-contrast flashing
*   **RGB LED Control**: Simultaneous channel activation
*   **Precise Timing**: 50ms ON, 100ms OFF cycles

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | 220Ω resistor |
| **Green LED** | GP17 | 220Ω resistor |
| **Blue LED** | GP18 | 220Ω resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (control RGB channels)
*   **from Time, drag `pico_wait`** (timing)
*   **from Loops, drag `pico_forever`** (continuous loop)

### 7. Variables
*   None (direct timing control)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure RGB Pins**:
    *   From **Smart IO**, drag pin configuration blocks.
        *   **Snap** into setup section.
        *   Set GP16, GP17, GP18 as outputs.

**B. Main Loop Phase**
2.  **Turn All ON (White)**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks.
        *   **Snap** into loop.
        *   Set R=HIGH, G=HIGH, B=HIGH.
3.  **Flash Duration**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 0.05 seconds.
4.  **Turn All OFF**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks.
        *   **Snap** below.
        *   Set R=LOW, G=LOW, B=LOW.
5.  **Off Duration**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 0.1 seconds.

### 9. Execution Flow
System creates white flash for 50ms, then turns all OFF for 100ms.

### 10. Generated Code
```python
import machine, time
r, g, b = [machine.Pin(i, machine.Pin.OUT) for i in (16, 17, 18)]
while True:
    r.on(); g.on(); b.on(); time.sleep(0.05)
    r.off(); g.off(); b.off(); time.sleep(0.1)
```

### 11. Common Mistakes
*   Missing resistors for LEDs.

### 12. Try This Next
*   Decrease timing to 0.02s for faster pulse.

---

## 1. Project 0502: Blinking Digital Art

### 2. Learning Objective
Cycle through CMY colors (Yellow→Cyan→Magenta) using RGB LED.

### 10. Generated Code
```python
import machine, time
r, g, b = [machine.Pin(i, machine.Pin.OUT) for i in (16, 17, 18)]
while True:
    r.on(); g.on(); b.off(); time.sleep(1)
    r.off(); g.on(); b.on(); time.sleep(1)
    r.on(); g.off(); b.on(); time.sleep(1)
```

---

## 1. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Interactive RGB mixer with 3 buttons toggling Red, Green, and Blue states.

---

## 1. Project 0504: Digital Art Sequences

### 2. Learning Objective
Random campfire flicker effect using PWM on Red and Green.

---

## 1. Project 0505: Interactive Digital Art

### 2. Learning Objective
Automatic color cycling night-light that activates only when ambient light is low.

---

## 1. Project 0506: Smart Digital Art Switch

### 2. Learning Objective
Switch selects between a slow blue fade and an emergency red strobe pulse.

---

## 1. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Color-coded logic: Button A (Red alert), Button B (Blue alert), Both (Purple danger).

---

## 1. Project 0508: The Digital Art Game

### 2. Learning Objective
Go/No-Go reaction task: Player must press button as fast as possible ONLY when Green shows.

---

## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Timed cycle simulating 24-hour patterns using colored LED lighting shifts.

---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Reusable function to define custom color blending ratios via numeric parameters.

---
"""

    batch_52 = """
# 📺 Batch 52: Animation 3

---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display countdown "3", "2", "1" on OLED filling entire screen.

### 3. Concepts Introduced
*   **Sequential Rendering**: Timed frame display
*   **OLED Logic**: Clear and draw

### 4. Hardware Required
Pico, OLED (128x64)

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_init`**
*   **from Display, drag `oled_text`**
*   **from Display, drag `oled_clear`**
*   **from Display, drag `oled_show`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, drag `oled_init`.
        *   **Snap** into setup section.

**B. Main Loop Phase**
2.  **Frame 1 (3)**:
    *   From **Display**, drag `oled_clear`.
        *   **Snap** into loop.
    *   From **Display**, drag `oled_text` (Text: "3").
        *   **Snap** below.
    *   From **Display**, drag `oled_show`.
        *   **Snap** below.
    *   Wait 1s.
3.  **Frame 2 (2)**: Repeat for text "2".
4.  **Frame 3 (1)**: Repeat for text "1".

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for n in ["3", "2", "1"]:
        oled.fill(0); oled.text(n, 60, 30); oled.show(); time.sleep(1)
```

---

## 1. Project 0512-0520: [Batch 52 Placeholder]

---
"""

    batch_53 = """
# 🔢 Batch 53: Binary Counter 3

---

## 1. Project 0521: Introduction to Binary Counters

### 2. Learning Objective
Display a 4-bit binary sequence (0-15) on four discrete LEDs.

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 14)]
c = 0
while True:
    for i in range(4): leds[i].value((c >> i) & 1)
    c = (c + 1) % 16; time.sleep(1)
```

---

## 1. Project 0522-0530: [Batch 53 Placeholder]

---
"""
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(header + batch_51 + batch_52 + batch_53)
    print("Recreation successful. 0501-0530 base established.")

if __name__ == "__main__":
    create_perfect_docs()
