import re

def fix_batch_52():
    batch_52_content = """## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display countdown "3", "2", "1" on OLED filling entire screen with clear between numbers.

### 3. Concepts Introduced
*   **Full-Screen Display**: Large text rendering
*   **Sequential Animation**: Timed sequence
*   **Screen Clearing**: Between frames

### 4. Hardware Required
Pico, OLED Display (128x64, I2C)

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
        *   Set text: "2", size: large, position: center.
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
        *   Set text: "1", size: large, position: center.
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
    # Display 3
    oled.fill(0)
    oled.text("  3", 40, 24, 1)
    oled.show()
    time.sleep(1)
    
    # Display 2
    oled.fill(0)
    oled.text("  2", 40, 24, 1)
    oled.show()
    time.sleep(1)
    
    # Display 1
    oled.fill(0)
    oled.text("  1", 40, 24, 1)
    oled.show()
    time.sleep(1)
```

### 11. Common Mistakes
*   Wrong I2C pins (verify wiring)
*   Not calling show() after drawing
*   Text too small (increase font size)

### 12. Try This Next
*   Add "GO!" after countdown

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
*   **from Display, drag `oled_circle`**
*   **from Display, drag `oled_line`**
*   **from Display, drag `oled_clear`**
*   **from Display, drag `oled_show`**

### 7. Variables
*   None

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, drag I2C configuration block.
        *   **Snap** into setup section.
    *   From **Display**, drag `oled_init` block.
        *   **Snap** below.

**B. Main Loop Phase**
2.  **Draw Face (Eyes Open)**:
    *   From **Display**, drag `oled_clear`.
        *   **Snap** into loop.
    *   From **Display**, drag `oled_circle` for Left Eye.
    *   From **Display**, drag `oled_circle` for Right Eye.
    *   From **Display**, drag `oled_show`.
3.  **Hold Frame**:
    *   From **Time**, drag `pico_wait` (0.5s).
4.  **Draw Wink (One Eye Closed)**:
    *   From **Display**, drag `oled_clear`.
    *   From **Display**, drag `oled_circle` for Left Eye.
    *   From **Display**, drag `oled_line` for Right Eye (Closed).
    *   From **Display**, drag `oled_show`.
5.  **Hold Frame**:
    *   From **Time**, drag `pico_wait` (0.5s).

### 9. Execution Flow
Alternates between face with both eyes open and face winking (right eye as line).

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)  # Left eye
    oled.ellipse(80, 25, 5, 5, 1)  # Right eye
    oled.show()
    time.sleep(0.5)
    
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)  # Left eye open
    oled.line(75, 25, 85, 25, 1)   # Right eye line
    oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   Not clearing between frames

### 12. Try This Next
*   Alternate which eye winks

---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Etch-a-Sketch - 2 potentiometers control X/Y dot position, leaving trail.

### 3. Concepts Introduced
*   **Analog Input Mapping**: Pot → screen coordinates
*   **Persistence Drawing**: Don't clear previous

### 4. Hardware Required
Pico, 2 Potentiometers, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Pot 1 (X)** | GP26 | ADC0 |
| **Pot 2 (Y)** | GP27 | ADC1 |
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`**
*   **from Math, drag `map_range`**
*   **from Display, drag `oled_pixel`**
*   **from Display, drag `oled_show`**

### 7. Variables
*   **x**, **y**: Coordinates

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   From **Display**, drag OLED config and `oled_init`.
    *   From **Smart IO**, drag `pico_analog_read` setup for GP26/GP27.

**B. Main Loop Phase**
2.  **Read Potentiometers**:
    *   From **Smart IO**, drag `pico_analog_read` for GP26.
        *   **Snap** into loop.
    *   From **Smart IO**, drag `pico_analog_read` for GP27.
        *   **Snap** below.
3.  **Map to Screen**:
    *   From **Math**, drag `map_range` (0-65535 to 0-127).
    *   From **Math**, drag `map_range` (0-65535 to 0-63).
4.  **Draw Without Clear**:
    *   From **Display**, drag `oled_pixel` at (x, y).
        *   **Snap** below.
    *   From **Display**, drag `oled_show`.

### 9. Execution Flow
Reads pots, maps to coordinates, and draws a pixel. Since `oled_clear` is omitted, it leaves a trail.

### 10. Generated Code
```python
from machine import Pin, I2C, ADC
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot_x = ADC(26)
pot_y = ADC(27)

oled.fill(0)
while True:
    x = int((pot_x.read_u16() / 65535) * 127)
    y = int((pot_y.read_u16() / 65535) * 63)
    oled.pixel(x, y, 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   Adding `oled_clear` in loop (erases trail)

### 12. Try This Next
*   Add button to clear

---

## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Progress bar animation - fill rectangle from 0% to 100% over 5 seconds.

### 3. Concepts Introduced
*   **Progress Visualization**: Incremental filling

### 4. Hardware Required
Pico, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_rect`**
*   **from Display, drag `oled_fill_rect`**
*   **from Loops, drag `for_loop`**

### 7. Variables
*   **width**: Rect width

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, drag OLED config blocks.

**B. Main Loop Phase**
2.  **Draw Background**:
    *   From **Display**, drag `oled_clear`.
    *   From **Display**, drag `oled_rect` (outline).
3.  **Loop Fill**:
    *   From **Loops**, drag `for_loop` (0 to 100).
        *   **Snap** below outline.
    *   From **Display**, drag `oled_fill_rect` with width proportional to loop index.
        *   **Snap** inside loop.
    *   From **Display**, drag `oled_show`.
    *   From **Time**, drag `pico_wait` (0.05s).

### 9. Execution Flow
Draws a static outline and then a dynamically expanding filled rectangle inside it.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.rect(10, 25, 108, 14, 1)
    for w in range(0, 107):
        oled.fill_rect(11, 26, w, 12, 1)
        oled.show()
        time.sleep(0.05)
```

### 11. Common Mistakes
*   Overwriting the outline

### 12. Try This Next
*   Add text label

---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Jumping character - button triggers jump arc (Y: 60→40→20→40→60).

### 3. Concepts Introduced
*   **Trajectory Animation**: Parabolic jump

### 4. Hardware Required
Pico, Button, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Display, drag `oled_rect`**
*   **from Loops, drag `for_loop`**

### 7. Variables
*   **y**: Position

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   From **Display**, drag oled config.
    *   From **Smart IO**, drag `pico_gpio_read` for GP14.

**B. Main Loop Phase**
2.  **Detect Trigger**:
    *   From **Logic**, drag `if` (button pressed).
        *   **Snap** into loop.
3.  **Execute Jump**:
    *   From **Loops**, drag `for_loop` (Upward: 60 to 20).
    *   From **Display**, drag `oled_clear`, `oled_rect` (at y), `oled_show`.
    *   From **Loops**, drag `for_loop` (Downward: 20 to 60).
    *   From **Display**, drag `oled_clear`, `oled_rect` (at y), `oled_show`.

### 9. Execution Flow
Waits for button, then runs two loops to move the character vertically.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn.value():
        for y in range(60, 19, -5):
            oled.fill(0)
            oled.rect(60, y, 8, 8, 1)
            oled.show()
            time.sleep(0.05)
        for y in range(20, 61, 5):
            oled.fill(0)
            oled.rect(60, y, 8, 8, 1)
            oled.show()
            time.sleep(0.05)
```

### 11. Common Mistakes
*   No clear in jump loops

### 12. Try This Next
*   Double jump

---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Screen rotation - button switches text between horizontal and vertical orientation.

### 3. Concepts Introduced
*   **Text Rotation**: Layout switching

### 4. Hardware Required
Pico, Button, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_text`**
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Logic, drag `if_compare`**

### 7. Variables
*   **rot**: Mode

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   Standard OLED/Button setup.

**B. Main Loop Phase**
2.  **Check Switch**:
    *   From **Logic**, if button pressed: toggle `rot`.
3.  **Horizontal Mode**:
    *   If `rot` = 0: From **Display**, drag `oled_text`("HI", 40, 30).
4.  **Vertical Mode**:
    *   If `rot` = 1: From **Display**, drag `oled_text`("H", 60, 20), `oled_text`("I", 60, 30).
5.  **Refresh**:
    *   From **Display**, `oled_show`.

### 9. Execution Flow
Button toggles a variable. If 0, text is drawn horizontally. If 1, char-by-char vertically.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
rot = False

while True:
    if btn.value():
        rot = not rot
        time.sleep(0.5)
    oled.fill(0)
    if not rot:
        oled.text("HI", 50, 25)
    else:
        oled.text("H", 60, 15)
        oled.text("I", 60, 25)
    oled.show()
```

---

## 1. Project 0517: Animation Alarm System

### 2. Learning Objective
Animated heartbeat - scale heart small→big→small, faster when "stress" button pressed.

### 3. Concepts Introduced
*   **Sprite Scaling**: Rate control

### 4. Hardware Required
Pico, Button, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button** | GP14 | Stress |
| **OLED SDA** | GP0 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_ellipse`**
*   **from Smart IO, drag `pico_gpio_read`**

### 7. Variables
*   **delay**: Speed

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   Standard OLED/Button setup.

**B. Main Loop Phase**
2.  **Check Stress**:
    *   From **Smart IO**, read GP14.
    *   If Pressed: set `delay` = 0.05s.
    *   Else: set `delay` = 0.2s.
3.  **Heart Expansion**:
    *   From **Display**, `oled_clear`, `oled_ellipse`(radius 10), `oled_show`.
    *   From **Time**, wait `delay`.
4.  **Heart Contraction**:
    *   From **Display**, `oled_clear`, `oled_ellipse`(radius 20), `oled_show`.
    *   Wait `delay`.

### 9. Execution Flow
Heartbeat rate is controlled by the input variable `delay`.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    delay = 0.05 if btn.value() else 0.2
    for r in [10, 20]:
        oled.fill(0)
        oled.ellipse(64, 32, r, r//2, 1)
        oled.show()
        time.sleep(delay)
```

---

## 1. Project 0518: The Animation Game

### 2. Learning Objective
Avoidance game - falling dot from top, player dodges with left/right buttons.

### 3. Concepts Introduced
*   **Collision Detection**: Logic checks

### 4. Hardware Required
Pico, 2 Buttons, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Btn L** | GP13 | Left |
| **Btn R** | GP14 | Right |
| **OLED** | GP0/1 | I2C |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Display, drag `oled_pixel`**

### 7. Variables
*   **px**, **ex**, **ey**: Positions

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Hardware**:
    *   Standard OLED / 2x Button setup.

**B. Main Loop Phase**
2.  **Control Player**:
    *   If GP13: px -= 2.
    *   If GP14: px += 2.
3.  **Move Enemy**:
    *   ey += 2. If ey > 64: reset ey=0, random ex.
4.  **Collision Check**:
    *   If dist between (px, 60) and (ex, ey) < 3: Game Over.
5.  **Render**:
    *   `oled_clear`, `oled_pixel`(px, 60), `oled_pixel`(ex, ey), `oled_show`.

### 9. Execution Flow
Enemy falls. Collision check returns true if pixel coordinates overlap.

### 10. Generated Code
```python
import random, machine, ssd1306, time
from machine import Pin, I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bL = Pin(13, Pin.IN, Pin.PULL_DOWN)
bR = Pin(14, Pin.IN, Pin.PULL_DOWN)
px, ex, ey = 64, 60, 0
while True:
    if bL.value(): px -= 2
    if bR.value(): px += 2
    ey += 2
    if ey > 64: ey, ex = 0, random.randint(0,127)
    if ey > 58 and abs(px - ex) < 5: break
    oled.fill(0)
    oled.pixel(px, 60, 1); oled.pixel(ex, ey, 1)
    oled.show(); time.sleep(0.05)
```

---

## 1. Project 0519: Automated Animation

### 2. Learning Objective
Screensaver - after 10s idle, bounce "DVD" text around screen.

### 3. Concepts Introduced
*   **Idle Detection**: Movement logic

### 4. Hardware Required
Pico, Button, OLED

### 5. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Standard.
2.  **Tracking**: `timer` = current time.

**B. Main Loop Phase**
3.  **Activity Sensor**:
    *   If button pressed: reset `timer`.
4.  **Logic**:
    *   If current_time - `timer` > 10s: Run Bouncing Text function.
    *   Else: Display "Active Mode".

### 6. Blocks Used
*   **from Display, drag `oled_text`**
*   **from Time, drag `pico_ms_ticks`**

---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
Sprite sheet animation - Pacman open/closed frames alternate while moving.

### 3. Concepts Introduced
*   **Sprite Sheets**: Alternating bitmaps

### 4. Hardware Required
Pico, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED** | GP0/1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_ellipse`** (shape manipulation)
*   **from Math, drag `modulo`** (frame toggle)

### 7. Variables
*   **frame**: 0 or 1

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Hardware**: Standard.

**B. Main Loop Phase**
2.  **Animate Mouth**:
    *   From **Logic**, if `frame` = 0: Draw ellipse with "pie slice" cut (arc).
    *   Else: Draw full ellipse.
3.  **Move Position**:
    *   Update X coordinate.
4.  **Iterate**:
    *   `frame` = 1 - `frame`.
5.  **Show**:
    *   `oled_clear`, draw shape at X, `oled_show`.

### 9. Execution Flow
Alternating frame variable changes the drawn geometry each step.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306, time
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x, frame = 0, 0
while True:
    oled.fill(0)
    oled.ellipse(x, 32, 10, 10, 1)
    if frame == 0: # Pacman open mouth (cut)
        oled.fill_rect(x, 30, 12, 4, 0)
    oled.show()
    x = (x + 2) % 128
    frame = 1 - frame
    time.sleep(0.1)
```

### 11. Common Mistakes
*   No clear

### 12. Try This Next
*   Add dots to eat

---

'''

    content_fixed = before_batch52 + batch_52_content + after_batch52
    with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
        f.write(content_fixed)

if __name__ == "__main__":
    fix_batch_52()
    print("Batch 52 Fixed with Elite Standard Format.")
