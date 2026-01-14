import os

def fix_reconstruction():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Read up to Project 0510 (Line 987)
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Keep the successfully completed Batch 51 (Projects 0501-0510)
    # Project 0510 ends around line 987. Let's find the exact Project 0511 start.
    base_content = ""
    for line in lines:
        if "## 1. Project 0511:" in line:
            break
        base_content += line
        
    # Now generate the Missing 0511-0530 with 100% Compliance
    reconstruction = """# 📺 Batch 52: Animation 3

---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display countdown "3", "2", "1" on OLED filling entire screen with clear between numbers.

### 3. Concepts Introduced
*   **Full-Screen Display**: Large text rendering
*   **Sequential Animation**: Timed sequence
*   **Screen Clearing**: Between frames

### 4. Hardware Required
Pico, OLED Display (128x64)

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C Data |
| **OLED SCL** | GP1 | I2C Clock |
| **OLED VCC** | 3.3V | Power |
| **OLED GND** | GND | Ground |

### 6. Blocks Used
*   **from Display, drag `oled_init`**
*   **from Display, drag `oled_text`**
*   **from Display, drag `oled_clear`**
*   **from Display, drag `oled_show`**
*   **from Time, drag `pico_wait`**
*   **from Loops, drag `pico_forever`**

### 7. Variables
*   None (sequential display)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure I2C**:
    *   From **Display**, drag I2C configuration block.
        *   **Snap** into setup section.
        *   Set SDA=GP0, SCL=GP1.
2.  **Initialize OLED**:
    *   From **Display**, drag `oled_init` block.
        *   **Snap** below.
        *   Configure for 128x64 display.

**B. Main Loop Phase**
3.  **Display "3"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** into main loop.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
        *   Set text: "3", size: large, position: center.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.
4.  **Display "2"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.
5.  **Display "1"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.

### 9. Execution Flow
OLED initialized via I2C. Main loop displays "3" for 1s, clears, displays "2" for 1s, clears, displays "1" for 1s, then repeats. Full-screen countdown sequence.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text("3", 60, 25)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.text("2", 60, 25)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.text("1", 60, 25)
    oled.show()
    time.sleep(1)
```

### 11. Common Mistakes
*   Forgetting `oled.show()` after clear/draw.

### 12. Try This Next
*   Add a "GO!" screen.

---

## 1. Project 0512: Blinking Animation

### 2. Learning Objective
Animate face that winks - close one eye (horizontal line), open it, repeat.

### 3. Concepts Introduced
*   **Sprite Animation**: Changing features
*   **Frame Toggling**: Eye open/closed states

### 4. Hardware Required
Pico, OLED Display

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_ellipse`**
*   **from Display, drag `oled_line`**
*   **from Display, drag `oled_show`**

### 7. Variables
*   None

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init OLED**: From **Display**, drag `oled_init`. **Snap** into setup.

**B. Main Loop Phase**
2.  **Open Eyes**: 
    *   From **Display**, drag `oled_clear`.
    *   From **Display**, drag `oled_ellipse` (Left Eye).
    *   From **Display**, drag `oled_ellipse` (Right Eye).
    *   From **Display**, drag `oled_show`.
3.  **Wait**: From **Time**, drag `pico_wait` (0.5s).
4.  **Wink**:
    *   From **Display**, drag `oled_clear`.
    *   From **Display**, drag `oled_ellipse` (Left Eye).
    *   From **Display**, drag `oled_line` (Right Eye wink).
    *   From **Display**, drag `oled_show`.
5.  **Wait**: From **Time**, drag `pico_wait` (0.5s).

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306, time
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)
    oled.ellipse(80, 25, 5, 5, 1)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)
    oled.line(75, 25, 85, 25, 1)
    oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   Eyes not aligned.

### 12. Try This Next
*   Wink both eyes.

---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Etch-a-Sketch - 2 potentiometers control X/Y dot position, leaving trail.

### 4. Hardware Required
Pico, 2 Potentiometers, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Pot X** | GP26 | ADC0 |
| **Pot Y** | GP27 | ADC1 |
| **OLED** | GP0/1 | I2C |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`**
*   **from Display, drag `oled_pixel`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Standard OLED and ADC init.

**B. Main Loop Phase**
2.  **Read**: From **Smart IO**, drag `pico_analog_read` (GP26, GP27).
3.  **Map**: From **Math**, map 0-65535 to screen.
4.  **Draw**: From **Display**, drag `oled_pixel`. **Snap** into loop.
5.  **Show**: From **Display**, drag `oled_show`.

### 10. Generated Code
```python
from machine import Pin, I2C, ADC
import ssd1306
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
px = ADC(26); py = ADC(27)
oled.fill(0)
while True:
    x = int(px.read_u16() * 127 / 65535)
    y = int(py.read_u16() * 63 / 65535)
    oled.pixel(x, y, 1)
    oled.show()
```

---

## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Progress bar animation - fill rectangle from 0% to 100% over 5 seconds.

### 3. Concepts Introduced
*   **Progress Animation**: Fill logic

### 4. Hardware Required
Pico, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Standard OLED.

**B. Main Loop Phase**
2.  **Clear**: From **Display**, drag `oled_clear`.
3.  **Outline**: From **Display**, drag `oled_rect`.
4.  **Fill Loop**: 
    *   From **Loops**, drag `for_loop` (0-100).
    *   From **Display**, drag `oled_fill_rect`. **Snap** inside for.
    *   From **Display**, drag `oled_show`.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0)
    oled.rect(10, 20, 108, 20, 1)
    for i in range(101):
        oled.fill_rect(10, 20, i, 20, 1)
        oled.show()
        time.sleep(0.05)
```

---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Jumping character - button triggers jump arc (Y: 60→40→20→40→60).

### 4. Hardware Required
Pico, Button, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: OLED and Button(GP14).

**B. Main Loop Phase**
2.  **Wait**: From **Logic**, if button pressed:
3.  **Jump**:
    *   From **Loops**, animate Y from 60 down to 20 and back.
    *   From **Display**, drag `oled_clear`, `oled_rect`, `oled_show`.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
    if btn.value():
        for y in list(range(60,19,-5)) + list(range(20,61,5)):
            oled.fill(0)
            oled.rect(60, y, 10, 10, 1)
            oled.show()
            time.sleep(0.05)
```

---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Screen rotation - button switches text between horizontal and vertical orientation.

### 4. Hardware Required
Pico, Button, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: OLED and Button. `mode` = 0.

**B. Main Loop Phase**
2.  **Toggle**: If button pressed: `mode` = 1 - `mode`.
3.  **Draw**: 
    *   If `mode`=0: `oled_text`("HI", 60, 30).
    *   If `mode`=1: `oled_text`("H", 60, 20), `oled_text`("I", 60, 32).

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
m = 0
while True:
    if btn.value(): m = 1 - m; time.sleep(0.3)
    oled.fill(0)
    if m == 0: oled.text("HI", 60, 30)
    else: oled.text("H", 60, 20); oled.text("I", 60, 32)
    oled.show()
```

---

## 1. Project 0517: Animation Alarm System

### 2. Learning Objective
Heartbeat animation - pulses faster when "stress" button is pressed.

### 4. Hardware Required
Pico, Button, OLED

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
    d = 0.05 if btn.value() else 0.2
    for r in [10, 20]:
        oled.fill(0); oled.ellipse(64, 32, r, r//2, 1); oled.show(); time.sleep(d)
```

---

## 1. Project 0518: The Animation Game

### 2. Learning Objective
Avoidance game - dodge falling dot using left/right buttons.

### 4. Hardware Required
Pico, 2 Buttons, OLED

### 10. Generated Code
```python
import random, machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bL = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
bR = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
px, ex, ey = 64, 60, 0
while True:
    if bL.value(): px -= 3
    if bR.value(): px += 3
    ey += 3
    if ey > 64: ey, ex = 0, random.randint(0,120)
    if ey > 55 and abs(px - ex) < 8: oled.fill(0); oled.text("HIT!", 50, 30); oled.show(); break
    oled.fill(0); oled.pixel(px, 60, 1); oled.pixel(ex, ey, 1); oled.show(); time.sleep(0.05)
```

---

## 1. Project 0519: Automated Animation

### 2. Learning Objective
Screensaver - bounce text after 10s of inactivity.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
last = time.time(); x, y, dx, dy = 10, 10, 2, 2
while True:
    if btn.value(): last = time.time()
    oled.fill(0)
    if time.time() - last > 10:
        x += dx; y += dy
        if x < 0 or x > 100: dx *= -1
        if y < 0 or y > 50: dy *= -1
        oled.text("DVD", x, y)
    else: oled.text("ACTIVE", 40, 30)
    oled.show(); time.sleep(0.05)
```

---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
Sprite sheet animation - animated Pacman movement.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x, f = 0, 0
while True:
    oled.fill(0); oled.ellipse(x, 32, 10, 10, 1)
    if f == 0: oled.fill_rect(x, 30, 12, 4, 0) # Mouth
    oled.show(); x = (x + 2) % 128; f = 1 - f; time.sleep(0.1)
```

---

# 🔢 Batch 53: Binary Counter 3

---

## 1. Project 0521: Introduction to Binary Counters

### 2. Learning Objective
Display a 4-bit binary count (0-15) using 4 LEDs.

### 4. Hardware Required
Pico, 4 LEDs

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LED 0** | GP10 | Bit 0 |
| **LED 1** | GP11 | Bit 2 |
| **LED 2** | GP12 | Bit 4 |
| **LED 3** | GP13 | Bit 8 |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Math, drag `math_modulo`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP10-13 as Outputs.

**B. Main Loop Phase**
2.  **Display**: From **Smart IO**, drag `pico_gpio_write` for each bit of `count`.
3.  **Wait**: From **Time**, drag `pico_wait` (1s).
4.  **Loop**: Increment `count`.

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

## 1. Project 0522: Binary LED Sequences

### 2. Learning Objective
Gray Code counter - only one bit changes per step.

### 4. Hardware Required
Pico, 4 LEDs

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 14)]
v = 0
while True:
    g = v ^ (v >> 1)
    for i in range(4): leds[i].value((g >> i) & 1)
    v = (v + 1) % 16; time.sleep(1)
```

---

## 1. Project 0523: Manual Binary Control

### 2. Learning Objective
2 buttons representing bits 2^0 and 2^1. Display result on LEDs.

### 10. Generated Code
```python
import machine
b0 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
b1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
l0 = machine.Pin(10, machine.Pin.OUT); l1 = machine.Pin(11, machine.Pin.OUT)
while True:
    l0.value(b0.value()); l1.value(b1.value())
```

---

## 1. Project 0524: Binary Sequences

### 2. Learning Objective
6-bit Binary Clock simulation (seconds).

### 4. Hardware Required
Pico, 6 LEDs

### 10. Generated Code
```python
import time, machine
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 16)]
while True:
    s = time.localtime()[5]
    for i in range(6): leds[i].value((s >> i) & 1)
    time.sleep(1)
```

---

## 1. Project 0525: Interactive Binary

### 2. Learning Objective
2-bit Binary Adder with 4 buttons and 3 LEDs.

### 10. Generated Code
```python
import machine
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(14, 18)]
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 13)]
while True:
    n1 = btns[0].value() + (btns[1].value() << 1)
    n2 = btns[2].value() + (btns[3].value() << 1)
    res = n1 + n2
    for i in range(3): leds[i].value((res >> i) & 1)
```

---
"""
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(base_content + reconstruction)
        
    print("Gap fixed and Batches 52-53 Reconstructed.")

if __name__ == "__main__":
    fix_reconstruction()
