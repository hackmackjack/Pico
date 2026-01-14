#!/usr/bin/env python3
"""
BATCH 52 CUSTOM GENERATOR (Projects 0511-0520 - Animation)
Based on specific problem statements
"""

batch52 = '''
# 📺 Batch 52: Animation 3

---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display countdown "3", "2", "1" on OLED filling entire screen.

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
*   **from Display, drag `oled_init`** (initialize OLED)
*   **from Display, drag `oled_text`** (draw text)
*   **from Display, drag `oled_clear`** (clear screen)
*   **from Display, drag `oled_show`** (update display)
*   **from Time, drag `pico_wait`** (timing)

### 7. Variables
*   **count**: Current number (3, 2, 1)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, drag `oled_init`.
        *   **Snap** into setup.
        *   Configure I2C on GP0/GP1.

**B. Main Loop Phase**
2.  **Display "3"**:
    *   From **Display**, drag `oled_clear`.
        *   **Snap** into loop.
    *   From **Display**, drag `oled_text`.
        *   **Snap** below.
        *   Text: "3", Size: Large, Position: Center.
    *   From **Display**, drag `oled_show`.
    *   From **Time**, wait 1s.
3.  **Display "2"**:
    *   Clear, draw "2", show, wait 1s.
4.  **Display "1"**:
    *   Clear, draw "1", show, wait 1s.

### 9. Execution Flow
OLED initialized. Loop displays "3" (1s) → Clear → "2" (1s) → Clear → "1" (1s) → Repeat. Full-screen countdown sequence.

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
*   Wrong I2C pins (check wiring)
*   Not calling `oled.show()` (no update)
*   Text too small (use large font)

### 12. Try This Next
*   Add "GO!" after countdown
*   Animate with growing size
*   Sound effects with buzzer

---

## 1. Project 0512: Blinking Animation

### 2. Learning Objective
Animate face that winks - close one eye (horizontal line), open it, repeat.

### 3. Concepts Introduced
*   **Sprite Animation**: Changing features
*   **Frame Toggling**: Eye open/closed states
*   **Facial Features**: Circles and lines

### 4. Hardware Required
Pico, OLED Display

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Display, drag `oled_circle`** (draw eyes)
*   **from Display, drag `oled_line`** (winking eye)
*   **from Display, drag `oled_clear`** (refresh)
*   **from Display, drag `oled_show`** (update)

### 7. Variables
*   **winking**: Boolean (eye state)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Display**, init I2C OLED.

**B. Main Loop Phase**
2.  **Draw Face (Both Eyes Open)**:
    *   From **Display**, clear screen.
        *   **Snap** into loop.
    *   Draw left eye circle.
    *   Draw right eye circle.
    *   Draw mouth arc.
    *   Show, wait 0.5s.
3.  **Draw Wink (One Eye Closed)**:
    *   Clear screen.
    *   Draw left eye circle.
    *   Draw right eye as LINE (closed).
    *   Draw mouth.
    *   Show, wait 0.5s.

### 9. Execution Flow
Alternates between face with both eyes open and face winking (right eye as line). Creates  winking animation effect.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Both eyes open
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)  # Left eye
    oled.ellipse(80, 25, 5, 5, 1)  # Right eye
    oled.ellipse(60, 45, 15, 10, 1) # Mouth
    oled.show()
    time.sleep(0.5)
    
    # Wink (right eye closed)
    oled.fill(0)
    oled.ellipse(40, 25, 5, 5, 1)  # Left eye open
    oled.line(75, 25, 85, 25, 1)   # Right eye line
    oled.ellipse(60, 45, 15, 10, 1) # Mouth
    oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   Eye positions don't match (looks broken)
*   Timing too fast (hard to see)
*   Not clearing between frames

### 12. Try This Next
*   Alternate which eye winks
*   Add eyebrows that move
*   Smile grows when winking

---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Etch-a-Sketch - 2 potentiometers control X/Y dot position, leaving trail.

### 3. Concepts Introduced
*   **Analog Input Mapping**: Pot → screen coordinates
*   **Persistence Drawing**: Don't clear previous
*   **2D Control**: Independent X and Y

### 4. Hardware Required
Pico, 2 Potentiometers, OLED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Pot 1 (X)** | GP26 (ADC0) | Horizontal |
| **Pot 2 (Y)** | GP27 (ADC1) | Vertical |
| **OLED SDA** | GP0 | I2C |
| **OLED SCL** | GP1 | I2C |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`** (read pots)
*   **from Math, drag `map_range`** (ADC → screen coords)
*   **from Display, drag `oled_pixel`** (draw dot)
*   **from Display, drag `oled_show`** (update)

### 7. Variables
*   **x**, **y**: Current dot position (0-127, 0-63)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   From **Display**, init OLED.
    *   From **Smart IO**, configure ADC on GP26, GP27.
2.  **Clear Screen Once**:
    *   Initial clear to start fresh.

**B. Main Loop Phase**
3.  **Read Pot 1 (X)**:
    *   From **Smart IO**, read GP26.
        *   **Snap** into loop.
    *   From **Math**, map 0-65535 → 0-127.
4.  **Read Pot 2 (Y)**:
    *   From **Smart IO**, read GP27.
    *   From **Math**, map 0-65535 → 0-63.
5.  **Draw Pixel**:
    *   From **Display**, set pixel at (x, y).
        *   **Snap** below.
        *   **Don't clear** (persistence).
6.  **Update Display**:
    *   From **Display**, show.

### 9. Execution Flow
Reads both potentiometers continuously, maps to screen coordinates, draws pixel at current position WITHOUT clearing. Creates drawing trail as pots are adjusted.

### 10. Generated Code
```python
from machine import Pin, I2C, ADC
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

pot_x = ADC(26)
pot_y = ADC(27)

oled.fill(0)  # Initial clear only

while True:
    # Read and map pots to screen coords
    x = int((pot_x.read_u16() / 65535) * 127)
    y = int((pot_y.read_u16() / 65535) * 63)
    
    # Draw pixel (no clear = trail)
    oled.pixel(x, y, 1)
    oled.show()
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   Clearing each frame (loses trail)
*   Wrong mapping range (offscreen)
*   Pots not at full range

### 12. Try This Next
*   Button to clear screen
*   Different brush sizes
*   Save/load drawings

---

'''

# Save Batch 52
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    current = f.read()

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(current + batch52)

print("✓ Batch 52: Projects 0511-0513 added")
print("Continuing with 0514-0520...")
