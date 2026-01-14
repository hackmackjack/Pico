# 📘 Pico 2500: Batch 31 - Digital Art 2 (Projects 0301-0310)

**Grade Level:** 3-5 (Elementary) | **Bloom's Level:** Apply | **Theme:** OLED Graphics & Generative Art

---

## 1️⃣ Project 0301: Random Pixel Stars

### 2️⃣ Learning Objective
Learn to manipulate individual pixels on an OLED display to create random patterns.

### 3️⃣ Concepts Introduced
*   Pixel Coordinate System (X, Y)
*   Random Number Generation
*   Display RAM Buffering
*   Screen Clearing
*   Refresh Cycles

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display (I2C)
*   Breadboard & Wires

### 5️⃣ Wiring / Interfaces
| SSD1306 | Pico Pin |
| :--- | :--- |
| **VCC** | 3.3V |
| **GND** | GND |
| **SDA** | GP0 |
| **SCL** | GP1 |

### 6️⃣ Blocks Used
🔹 **OLED Init** - Setup display
🔹 **OLED Pixel** - `display.pixel(x, y, 1)`
🔹 **Random** - `random.randint(min, max)`
🔹 **Loops** - Repetition

### 7️⃣ Variables & State
*   **x, y**: Coordinates (0-127, 0-63)
*   **starCount**: Number of stars to draw

### 8️⃣ Step-by-Step Guide
**A. Initialization**
1. Initialize I2C (GP0, GP1)
2. Initialize SSD1306 (128x64)
3. Clear screen

**B. Main Loop**
1. Repeat 50 times:
   - Generate random x (0-127)
   - Generate random y (0-63)
   - Turn on pixel at (x, y)
2. Show display
3. Wait 0.1s

### 9️⃣ Execution Flow
The OLED screen is a grid of 128x64 dots. We pick a random spot by choosing a random X and random Y. We turn that dot "ON". Doing this fast many times looks like stars appearing in the night sky!

### 🔟 Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import random
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

print("Project 0301: Starfield")

while True:
    oled.fill(0) # Clear
    
    # Draw 50 stars
    for i in range(50):
        x = random.randint(0, 127)
        y = random.randint(0, 63)
        oled.pixel(x, y, 1)
        
    oled.show()
    time.sleep(0.5)
```

---

## 1️⃣ Project 0302: Digital Lines (Rain)

### 2️⃣ Learning Objective
Draw mathematical lines to create structured patterns like rain or grids.

### 3️⃣ Concepts Introduced
*   Line Primitives
*   Start/End Points
*   Vertical vs Horizontal
*   Looping Coordinates
*   Pattern density

### 4️⃣ Hardware Required
*   Pico, SSD1306 OLED

### 8️⃣ Step-by-Step Guide
**A. Initialization**
1. Setup OLED
**B. Main Loop**
1. Clear screen
2. Draw 20 vertical lines:
   - Random X position
   - Random length
   - `oled.line(x, y1, x, y2, 1)`
3. Show display

### 🔟 Generated Code
```python
while True:
    oled.fill(0)
    for i in range(20):
        x = random.randint(0, 127)
        y = random.randint(0, 40)
        length = random.randint(5, 20)
        oled.line(x, y, x, y+length, 1)
    oled.show()
    time.sleep(0.2)
```

---

## 1️⃣ Project 0303: Geometric Abstract (Rectangles)

### 2️⃣ Learning Objective
Compose art using filled and outlined rectangles (Mondrian style).

### 3️⃣ Concepts Introduced
*   Shapes: Rectangles
*   Fill vs Outline
*   Overlapping logic
*   Composition
*   Inversion (Color 0 vs 1)

### 10️⃣ Generated Code
```python
while True:
    oled.fill(0)
    for i in range(10):
        x = random.randint(0, 100)
        y = random.randint(0, 40)
        w = random.randint(10, 30)
        h = random.randint(10, 30)
        # Randomly fill or outline
        fill = random.choice([True, False])
        if fill:
            oled.fill_rect(x, y, w, h, 1)
        else:
            oled.rect(x, y, w, h, 1)
    oled.show()
    time.sleep(2)
```

---

## 1️⃣ Project 0304: Concentric Circles

### 2️⃣ Learning Objective
Use math/loops to draw nested shapes, creating targets or tunnels.

### 3️⃣ Concepts Introduced
*   Hollow Circles
*   Center Point
*   Radius
*   Iterative Growth
*   Visual Depth

### 10️⃣ Generated Code
```python
# Function for circle implemented in library usually, 
# if not, we use pixel math. Assuming framebuf-like library:
# oled.ellipse(x, y, xr, yr, c) is available in some versions
# Standard MicroPython framebuf uses rect/line. 
# We'll stick to rects for concentric squares if circle not safe,
# BUT let's assume valid circle helper or manual math.
# Let's use concentric RECTANGLES for safety in standard lib:

while True:
    oled.fill(0)
    # Draw target
    cx, cy = 64, 32
    for r in range(2, 32, 4):
        oled.rect(cx-r, cy-r, r*2, r*2, 1)
    oled.show()
    time.sleep(1)
    
    # Invert effect
    oled.fill(1)
    for r in range(2, 32, 4):
        oled.rect(cx-r, cy-r, r*2, r*2, 0)
    oled.show()
    time.sleep(1)
```

---

## 1️⃣ Project 0305: Diagonal Hatching

### 2️⃣ Learning Objective
Create texture and shading effects using line patterns.

### 3️⃣ Concepts Introduced
*   Slope/Gradient
*   Step Functions
*   Texture Generaton
*   Screen Filling

### 10️⃣ Generated Code
```python
oled.fill(0)
# Draw diagonal lines
for i in range(0, 200, 5):
    # Line from top edge to left edge
    oled.line(i, 0, 0, i, 1)
oled.show()
```

---

## 1️⃣ Project 0306: Etch-A-Sketch (Interactive)

### 2️⃣ Learning Objective
Create interactive drawing tool using inputs to control cursor.

### 3️⃣ Concepts Introduced
*   User Input (Potentiometer)
*   ADC Mapping
*   Cursor Persistence
*   Drawing State
*   Reset Function

### 4️⃣ Hardware
*   Pico, OLED
*   2x Potentiometers (GP26=X, GP27=Y)

### 10️⃣ Generated Code
```python
adc_x = machine.ADC(26)
adc_y = machine.ADC(27)

x, y = 64, 32

oled.fill(0)
while True:
    # Read pots (0-65535) -> map to screen
    dx = int(adc_x.read_u16() / 65535 * 127)
    dy = int(adc_y.read_u16() / 65535 * 63)
    
    # Draw dot
    oled.pixel(dx, dy, 1)
    oled.show()
    time.sleep(0.05)
```

---

## 1️⃣ Project 0307: Spirograph (Math Art)

### 2️⃣ Learning Objective
Use trigonometry (sine/cosine) to generate complex geometric curves.

### 3️⃣ Concepts Introduced
*   Trigonometry (Sin/Cos)
*   Polar Coordinates
*   Parametric Equations
*   Floating Point Math

### 10️⃣ Generated Code
```python
import math

oled.fill(0)
cx, cy = 64, 32
r = 20

for angle in range(0, 360*5, 10):
    rad = math.radians(angle)
    # Epicycloid-ish math
    x = int(cx + r * math.cos(rad) + 10 * math.cos(3*rad))
    y = int(cy + r * math.sin(rad) + 10 * math.sin(3*rad))
    oled.pixel(x, y, 1)
    oled.show()
```

---

## 1️⃣ Project 0308: Bitmap Icon Display

### 2️⃣ Learning Objective
Display custom designed icons or sprites using byte arrays.

### 3️⃣ Concepts Introduced
*   Bitmaps / Sprites
*   Binary Data Representation
*   Byte Arrays (framebuf)
*   Blitting (Block Transfer)

### 10️⃣ Generated Code
```python
import framebuf

# 8x8 smiley face
# 00111100 = 0x3C
# 01000010 = 0x42
# 10100101 = 0xA5
# ...
icon_data = bytearray([
    0x3C, 0x42, 0xA5, 0x81, 0xA5, 0x99, 0x42, 0x3C
])

fbuf = framebuf.FrameBuffer(icon_data, 8, 8, framebuf.MONO_HLSB)

oled.fill(0)
oled.blit(fbuf, 60, 28) # Draw at center
oled.show()
```

---

## 1️⃣ Project 0309: Negative Space (Invert)

### 2️⃣ Learning Objective
Understand display memory and inversion effects.

### 3️⃣ Concepts Introduced
*   Display Buffer
*   Inversion command
*   Pixel negation
*   Visual Contrast

### 10️⃣ Generated Code
```python
oled.fill(0)
oled.text("HELLO", 40, 20, 1)
oled.fill_rect(20, 40, 80, 10, 1)
oled.show()
time.sleep(1)

# Invert command (hardware)
oled.invert(1) 
time.sleep(1)
oled.invert(0)
```

---

## 1️⃣ Project 0310: Master Art Gallery

### 2️⃣ Learning Objective
Create a slideshow combining all previous effects into a portfolio.

### 10️⃣ Generated Code
```python
def show_stars(): pass # (Code from 0301)
def show_lines(): pass # (Code from 0302)

modes = [show_stars, show_lines] # etc...

while True:
    for mode in modes:
        oled.fill(0)
        mode()
        time.sleep(2)
```

---

**Batch 31 Complete**
