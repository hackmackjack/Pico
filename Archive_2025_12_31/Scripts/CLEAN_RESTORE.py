import os

def clean_rebuild_batch52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # We keep only Projects 0501-0510 which are roughly the first 980 lines.
    # We will search for the end of Project 0510 precisely.
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    clean_base = []
    for line in lines:
        clean_base.append(line)
        if "## 1. Project 0510: Mastering Digital Art" in line:
            # Found 0510, continue until the end of its section (the next ---)
            found_header = True
            continue
    
    # Actually, a safer way: Keep up to the line before "Batch 52"
    final_base = []
    for line in lines:
        if "# 📺 Batch 52:" in line or "## 1. Project 0511:" in line:
            break
        final_base.append(line)
    
    batch_52 = """
# 📺 Batch 52: Animation 3

---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display a full-screen countdown from "3" to "1" on the OLED display.

### 3. Concepts Introduced
*   **Sequential Logic**: Timed frames
*   **Screen Buffering**: Clearing and showing

### 4. Hardware Required
Pico, OLED Display

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C Data |
| **OLED SCL** | GP1 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `oled_init`**
*   **from Display, drag `oled_text`**
*   **from Display, drag `oled_clear`**
*   **from Display, drag `oled_show`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   None

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, drag `oled_init`.
        *   **Snap** into setup section.
        *   Configure I2C pins.

**B. Main Loop Phase**
2.  **Show "3"**:
    *   From **Display**, drag `oled_clear`.
        *   **Snap** into loop.
    *   From **Display**, drag `oled_text` (Text: "3").
        *   **Snap** below.
    *   From **Display**, drag `oled_show`.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` (1s).
3.  **Show "2"**:
    *   Repeat steps: Clear, Text("2"), Show, Wait.
4.  **Show "1"**:
    *   Repeat steps: Clear, Text("1"), Show, Wait.

### 9. Execution Flow
Initializes display, clears screen, draws "3", waits, and cycles through numbers.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for n in ["3", "2", "1"]:
        oled.fill(0); oled.text(n, 60, 30); oled.show(); time.sleep(1)
```

### 11. Common Mistakes
*   Forgetting to call `show()`.

### 12. Try This Next
*   Decrease timing for a faster countdown.

---

## 1. Project 0512: Blinking Animation

### 2. Learning Objective
Animate a winking face by toggling a line and a circle for the eye.

### 4. Hardware Required
Pico, OLED Display

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED** | GP0/1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_ellipse`**
*   **from Display, drag `oled_line`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Standard OLED initialization.

**B. Main Loop Phase**
2.  **Draw Normal**:
    *   From **Display**, drag `oled_clear`.
    *   Draw two ellipses for eyes.
    *   From **Display**, drag `oled_show`.
3.  **Wait**: From **Time**, drag `pico_wait` (0.5s).
4.  **Draw Wink**:
    *   From **Display**, drag `oled_clear`.
    *   Draw one ellipse and one horizontal line.
    *   From **Display**, drag `oled_show`.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.ellipse(40,30,5,5); oled.ellipse(80,30,5,5); oled.show(); time.sleep(0.5)
    oled.fill(0); oled.ellipse(40,30,5,5); oled.line(75,30,85,30,1); oled.show(); time.sleep(0.5)
```

---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Create a drawing "trail" where a dot moves based on two potentiometers.

### 3. Concepts Introduced
*   **Analog Mapping**: Range conversion
*   **Frame Persistence**: Drawing without clearing

### 4. Hardware Required
Pico, 2 Potentiometers, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Pot X** | GP26 | ADC |
| **Pot Y** | GP27 | ADC |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`**
*   **from Display, drag `oled_pixel`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Initialize OLED and ADC pins.
2.  **Clear Screen**: From **Display**, drag `oled_clear` (once only).

**B. Main Loop Phase**
3.  **Read Position**:
    *   From **Smart IO**, drag `pico_analog_read` for X and Y.
4.  **Draw Dot**:
    *   From **Display**, drag `oled_pixel`. 
    *   **Snap** into loop. **Do not** clear screen.
5.  **Refresh**: From **Display**, drag `oled_show`.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
ax, ay = machine.ADC(26), machine.ADC(27)
oled.fill(0)
while True:
    oled.pixel(int(ax.read_u16()*127/65535), int(ay.read_u16()*63/65535), 1)
    oled.show()
```

---

## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Animate a filling progress bar.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Standard OLED init.

**B. Main Loop Phase**
2.  **Background**: From **Display**, drag `oled_clear` and `oled_rect`.
3.  **Progress**: From **Loops**, drag `for_loop` (0-100).
4.  **Render**: From **Display**, drag `oled_fill_rect`. **Snap** into for loop.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.rect(10,20,108,20,1)
    for i in range(101):
        oled.fill_rect(10,20,i,20,1); oled.show(); time.sleep(0.01)
```

---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Button-triggered jumping animation.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: OLED and Button(GP14).

**B. Main Loop Phase**
2.  **Trigger**: If button pressed:
3.  **Animate**: 
    *   Loop characters Y position from 60 to 20.
    *   From **Display**, drag `oled_clear`, `oled_rect`, `oled_show`.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
    if btn.value():
        for y in list(range(60,20,-4)) + list(range(20,61,4)):
            oled.fill(0); oled.rect(60,y,8,8,1); oled.show(); time.sleep(0.02)
```

---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Toggle screen orientation with a button.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn, m = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN), 0
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
Heart rate pulse visualizer.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
while True:
    d = 0.05 if btn.value() else 0.2
    for r in [10, 15]:
        oled.fill(0); oled.ellipse(64,32,r,r,1); oled.show(); time.sleep(d)
```

---

## 1. Project 0518: The Animation Game

### 2. Learning Objective
Avoidance game with collision detection.

### 10. Generated Code
```python
import random, machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bL, bR = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN), machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
px, ex, ey = 64, 60, 0
while True:
    if bL.value(): px -= 4
    if bR.value(): px += 4
    ey += 4
    if ey > 64: ey, ex = 0, random.randint(0,120)
    if ey > 55 and abs(px - ex) < 10: break
    oled.fill(0); oled.pixel(px, 60, 1); oled.pixel(ex, ey, 1); oled.show(); time.sleep(0.05)
```

---

## 1. Project 0519: Automated Animation

### 2. Learning Objective
Screensaver with idle time logic.

### 10. Generated Code
```python
import time, machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
last, x, y, dx, dy = time.time(), 10, 10, 2, 2
while True:
    if btn.value(): last = time.time()
    oled.fill(0)
    if time.time() - last > 5:
        x += dx; y += dy
        if x < 0 or x > 110: dx *= -1
        if y < 0 or y > 55: dy *= -1
        oled.text("DVD", x, y)
    oled.show(); time.sleep(0.05)
```

---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
Walking sprite animation loop.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x, f = 0, 0
while True:
    oled.fill(0); oled.ellipse(x, 32, 10, 10, 1)
    if f == 0: oled.fill_rect(x, 30, 12, 4, 0)
    oled.show(); x = (x + 2) % 128; f = 1 - f; time.sleep(0.1)
```

---
"""
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(final_base)
        f.write(batch_52)
        
    print("File cleaned. Batch 51 preserved. Batch 52 restored to Elite Standard.")

if __name__ == "__main__":
    clean_rebuild_batch52()
