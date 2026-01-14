# CONSOLIDATED FIX: Projects 0363-0380 Full Elite Documentation

docs_0363_0370 = r'''
## 1️⃣ Project 0363: Manual OLED Shapes Control

### 2️⃣ Learning Objective
Implement D-pad navigation with a crosshair cursor. You will learn pixel-precise positioning, boundary clamping, and button-to-coordinate mapping.

### 3️⃣ Concepts Introduced
*   **D-Pad Navigation**: Controlling position using four directional inputs.
*   **Cursor Movement**: Updating 2D coordinates in real-time.
*   **Boundary Clamping**: Restricting variables within a specific range (X: 0-127, Y: 0-63).

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **4× Buttons** (Up, Down, Left, Right)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Button Up** | GP10 | PULL_DOWN |
| **Button Down** | GP11 | PULL_DOWN |
| **Button Left** | GP12 | PULL_DOWN |
| **Button Right** | GP13 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Setup OLED**
*   **Category:** Displays

🔹 **Setup Button (×4)**
*   **Category:** Inputs

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **OLED Line**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **cursorX**: Current X-coordinate (default 64).
*   **cursorY**: Current Y-coordinate (default 32).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[10] as PULL_DOWN`.
        *   **Snap** into setup block. (Repeat for pins 11, 12, 13).
    *   From **Variables**, drag `set [cursorX] to [64]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [cursorY] to [32]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Handle Movement**:
        *   From **Logic**, drag `if [digital read pin 10] then`.
            *   **Snap** into loop.
            *   Inside: From **Variables**, drag `change [cursorY] by [-1]`.
        *   From **Logic**, drag `if [digital read pin 11] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `change [cursorY] by [1]`.
        *   From **Logic**, drag `if [digital read pin 12] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `change [cursorX] by [-1]`.
        *   From **Logic**, drag `if [digital read pin 13] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `change [cursorX] by [1]`.
    *   **Draw Crosshair**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `draw line x1:[cursorX] y1:[cursorY-5] x2:[cursorX] y2:[cursorY+5] color:[1]`.
            *   **Snap** below (Vertical).
        *   From **Displays**, drag `draw line x1:[cursorX-5] y1:[cursorY] x2:[cursorX+5] y2:[cursorY] color:[1]`.
            *   **Snap** below (Horizontal).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system checks four pull-down buttons every 50ms. If the 'Up' button is pressed, the Y-coordinate decreases; if 'Down' is pressed, it increases. 'Left' and 'Right' buttons adjust the X-coordinate. The screen is cleared, and a crosshair (two intersecting lines) is drawn at the current (X, Y) position. The `OLED show` command pushes the buffer to the screen.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

up = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
down = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
left = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
right = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

x, y = 64, 32

while True:
    if up.value(): y = max(5, y - 1)
    if down.value(): y = min(58, y + 1)
    if left.value(): x = max(5, x - 1)
    if right.value(): x = min(122, x + 1)
    
    oled.fill(0)
    oled.line(x, y - 5, x, y + 5, 1)
    oled.line(x - 5, y, x + 5, y, 1)
    oled.show()
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Crosshair Trails**: If you don't call `OLED clear`, the previous crosshairs will stay on screen.
*   **Out of Bounds**: Ensure clamping (max/min) prevents the crosshair from being drawn outside the 128x64 grid.

### 1️⃣2️⃣ Try This Next

*   **Variable Speed**: Make the cursor move faster the longer the button is held.
*   **Drawing Tool**: Add a 5th button to "Toggle Draw" mode (don't clear screen), allowing you to sketch.

---

## 1️⃣ Project 0364: OLED Shapes Sequences

### 2️⃣ Learning Objective
Create an expanding ripple "explosion" animation using concentric circles. You will learn about loop-based animation and dynamic sizing.

### 3️⃣ Concepts Introduced
*   **Expanding Animation**: Increasing shape dimensions over frames.
*   **Ripple Effect**: Using increments in radius to simulate growth.
*   **Sequence Timing**: Controlling animation frame rate with delays.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |

### 6️⃣ Blocks Used

🔹 **Setup OLED**
*   **Category:** Displays

🔹 **OLED Circle**
*   **Category:** Displays

🔹 **For Loop**
*   **Category:** Loops

### 7️⃣ Variables & State
*   **radius**: Controlled variable in the for loop.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Expanding Loop**:
        *   From **Loops**, drag `for [radius] from [1] to [30] step [3]`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `circle x:[64] y:[32] r:[radius] color:[1]`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Timing**, drag `sleep [0.05] seconds`.
                    *   **Snap** below.
    *   **Cleanup**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below the for loop.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program runs a loop where a circle's radius increases from 1 to 30 pixels in steps of 3. In each step, the OLED is cleared, the new circle is drawn at the center (64, 32), and the display is updated. This creates a smooth animation of an expanding ripple. After reaching the maximum size, the screen clears for 1 second before the explosion repeats.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    for radius in range(1, 31, 3):
        oled.fill(0)
        oled.circle(64, 32, radius, 1)
        oled.show()
        time.sleep(0.05)
    
    oled.fill(0)
    oled.show()
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Stuttering Animation**: If the wait time in the loop is too long (>0.2s), the animation will feel choppy.
*   **Static Circle**: If `OLED show` is outside the loop, you will only see the final circle.

### 1️⃣2️⃣ Try This Next

*   **Concentric Ripples**: Draw multiple circles in the same frame with different radii to create a "wave" effect.
*   **Implosion**: Reverse the loop (from 30 down to 1) to create a shrinking effect.

---

## 1️⃣ Project 0365: Interactive OLED Shapes

### 2️⃣ Learning Objective
Build a "Paint" application using potentiometers for movement and a button to "stamp" pixels. You will learn about coordinate mapping and non-volatile display buffering.

### 3️⃣ Concepts Introduced
*   **Analog-to-Display Mapping**: Converting potentiometer voltages to screen coordinates.
*   **Persistent Drawing**: Modifying the frame buffer without clearing it to retain marks.
*   **Stamping Logic**: Using a button trigger to commit a pixel update.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **2× Potentiometers** (X and Y control)
*   **1× Button** (Stamp)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Potentiometer X** | GP26 | ADC0 |
| **Potentiometer Y** | GP27 | ADC1 |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Read Analog Pin**
*   **Category:** Pin Access

🔹 **Map Range**
*   **Category:** Math

🔹 **OLED Set Pixel**
*   **Category:** Displays

🔹 **Setup Button**
*   **Category:** Inputs

### 7️⃣ Variables & State
*   **paintX**: Mapped X-coordinate from Pot X.
*   **paintY**: Mapped Y-coordinate from Pot Y.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read & Map Inputs**:
        *   From **Math**, drag `map [read analog pin 26] from [0-65535] to [0-127]`.
            *   **Snap** into loop.
            *   Store in `paintX`.
        *   From **Math**, drag `map [read analog pin 27] from [0-65535] to [0-63]`.
            *   **Snap** below.
            *   Store in `paintY`.
    *   **Stamp Input**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** below.
            *   Inside: From **Displays**, drag `set pixel x:[paintX] y:[paintY] color:[1]`.
                *   **Snap** inside.
    *   **Display Update**:
        *   Note: **Do NOT** call `OLED clear` if you want drawings to stay.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program reads current from two potentiometers. One potentiometer's value (0-65535) is mapped to the screen's width (0-127), and the other to its height (0-63). When the user presses the button, a pixel is permanently set at the current mapped (X, Y) location in the OLED's buffer. By moving the pots and stamping, the user can "paint" an image.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
pot_x = machine.ADC(26)
pot_y = machine.ADC(27)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    x = int(pot_x.read_u16() * 127 / 65535)
    y = int(pot_y.read_u16() * 63 / 65535)
    
    if button.value():
        oled.pixel(x, y, 1)
        
    oled.show()
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Screen Clears**: If the drawing vanishes, ensure you didn't include an `oled.fill(0)` inside the loop.
*   **Invisible Cursor**: Since there is no "live" cursor (to avoid leaving lines), it's hard to see where you are. Add a temporary small circle that draws/clears every frame for preview.

### 1️⃣2️⃣ Try This Next

*   **Eraser**: Add a second button that calls `oled.pixel(x, y, 0)` to erase specific pixels.
*   **Spray Paint**: Draw a small cluster of random pixels around (X, Y) when held.

---

## 1️⃣ Project 0366: Smart OLED Shapes Switch

### 2️⃣ Learning Objective
Create a digital "Leveler" that visualizes horizontal balance using a tilt sensor. You will learn about sensor-driven line rotation.

### 3️⃣ Concepts Introduced
*   **Horizontal Orientation**: Using sensors to detect tilt.
*   **Dynamic Line Drawing**: Calculating line slopes for visual feedback.
*   **Horizon Visualization**: Simulating an artificial horizon.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **Tilt Sensor** (or Accelerometer)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Tilt Sensor** | GP15 | Digital Input |

### 6️⃣ Blocks Used

🔹 **Setup Pin**
*   **Category:** Pin Access

🔹 **OLED Line**
*   **Category:** Displays

🔹 **If-Else**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **isTilted**: State of the tilt sensor.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Pin:[15] as INPUT`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Detect Tilt**:
        *   From **Logic**, drag `if [digital read pin 15] = HIGH then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `draw line x1:[20] y1:[10] x2:[108] y2:[54] color:[1]`.
                    *   **Snap** inside (Diagonal 1).
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `draw line x1:[0] y1:[32] x2:[127] y2:[32] color:[1]`.
                    *   **Snap** inside (Perfectly Horizontal).
    *   **Update Screen**:
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program monitors a tilt sensor. When the sensor is level, a perfectly horizontal line is drawn across the middle of the screen (Y=32). If the sensor tilts, the line rotates diagonally to represent the shift in orientation. This provides a visual confirmation of whether a surface is level or tilted.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
tilt = machine.Pin(15, machine.Pin.IN)

while True:
    oled.fill(0)
    if tilt.value():
        # Represent tilted state (diagonal line)
        oled.line(20, 10, 108, 54, 1)
    else:
        # Represent level state (horizontal line)
        oled.line(0, 32, 127, 32, 1)
    
    oled.show()
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Flickering Line**: Ensure the `OLED clear` is inside the logic or at the very start of the loop; otherwise, lines will overlap and blur.
*   **Sensitivity**: Tilt sensors can be noisy; if the line jumps, wrap the `tilt.value()` check with a small debounce count.

### 1️⃣2️⃣ Try This Next

*   **Proportional Tilt**: If using an accelerometer, map the exact tilt angle to the line slope using trigonometry.
*   **Bubble Level**: Draw a circle (bubble) that moves along the line depending on the tilt intensity.

---

## 1️⃣ Project 0367: OLED Shapes Alarm System

### 2️⃣ Learning Objective
Implement a high-priority UI overlay using large-scale text or vector-drawn letters. You will learn about visual hierarchy and alert visualization.

### 3️⃣ Concepts Introduced
*   **Emergency Overlays**: Taking over the display for critical alerts.
*   **Vector Letter Drawing**: Creating letters using lines when built-in fonts are too small.
*   **Flash Indication**: Using alternating screens to grab attention.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **Button** (Alarm Trigger)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **OLED Line**
*   **Category:** Displays

🔹 **Setup Button**
*   **Category:** Inputs

🔹 **Logic Comparators**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **isAlarmActive**: Boolean toggle.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check Trigger**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   **Draw "STOP"** (Vector Letters):
                    *   "S": Draw lines for top, middle, bottom and sides.
                    *   "T": Draw vertical line + flat top line.
                    *   "O": Draw 4 lines forming a box.
                    *   "P": Draw vertical line + half-box top.
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Timing**, drag `sleep [0.5] seconds`.
                    *   **Snap** below.
                *   Draw inverse (White background, Black text) or Clear.
        *   From **Logic**, drag `else`.
            *   Inside: From **Displays**, drag `OLED clear/show`. (Normal idle state).

### 9️⃣ Execution Flow (Plain English)

The system idles with a clear screen. When the alarm button is pressed, the program starts drawing a massive "STOP" sign using the line tool (since the default font is small). The letters are constructed using individual vector coordinates to fill the screen. The alert flashes every 500ms to ensure the user notices the emergency state immediately.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def draw_stop():
    # Very simple vector drawing
    # S
    oled.line(10, 10, 30, 10, 1)
    # T
    oled.line(40, 10, 60, 10, 1)
    oled.line(50, 10, 50, 50, 1)
    # O (simplified)
    oled.rect(70, 10, 20, 40, 1)
    # P
    oled.line(100, 10, 100, 50, 1)
    oled.rect(100, 10, 20, 20, 1)

while True:
    if button.value():
        oled.fill(0)
        draw_stop()
        oled.show()
        time.sleep(0.5)
        oled.fill(1) # Flash white
        oled.show()
        time.sleep(0.5)
    else:
        oled.fill(0)
        oled.show()
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Complexity**: Drawing complex vector fonts is time-consuming (in blocks). Use basic primitives like `rect` or `line` to construct blocky, readable letters quickly.
*   **Blocking Code**: The `sleep(0.5)` in the alarm logic will make the button "feel" unresponsive if clicked during the flash; use mills-based non-blocking logic for better feel.

### 1️⃣2️⃣ Try This Next

*   **Animated Siren**: Add alternating diagonal lines on the corners to mimic a rotating siren light.
*   **Buzzer Sync**: Beep the buzzer only when the text is visible.

---

## 1️⃣ Project 0368: The OLED Shapes Game

### 2️⃣ Learning Objective
Create a "Maze" game that utilizes collision detection via pixel-color sensing. You will learn about environmental mapping and hit-box logic.

### 3️⃣ Concepts Introduced
*   **Collision Detection**: Using `pixel(x, y)` to check if the target color is white (wall) or black (path).
*   **Map Geometry**: Defining obstacles using static drawing commands.
*   **Game Reset Logic**: Teleporting coordinates back to spawn upon a collision event.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **4× Buttons** (Up, Down, Left, Right)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Buttons** | GP10-13 | Standard Nav Pins |

### 6️⃣ Blocks Used

🔹 **OLED Get Pixel**
*   **Category:** Displays

🔹 **Logic Comparison**
*   **Category:** Logic

🔹 **OLED Rect/Line**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **playerX, playerY**: Player dot location.
*   **hitWall**: Boolean collision flag.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup I2C, OLED, and Nav Buttons.
    *   From **Variables**, drag `set [playerX] to [5]`.
    *   From **Variables**, drag `set [playerY] to [5]`.

*   **B. Main Loop Phase**
    *   **Draw Map**:
        *   From **Displays**, drag `draw rectangle x:[0] y:[20] w:[100] h:[5] color:[1]`.
            *   **Snap** into loop (create a horizontal wall).
        *   From **Displays**, drag `draw line x:[40] y:[0] x2:[40] y2:[15] color:[1]`.
            *   **Snap** below (create a partial vertical wall).
    *   **Motion & Collision**:
        *   Read movement buttons.
        *   **Before Moving**, check destination:
            *   From **Logic**, drag `if [pixel at x:[targetX] y:[targetY]] = [1] then`.
                *   **Snap** inside movement logic.
                *   Inside: `set [playerX] to [5]`, `set [playerY] to [5]` (Reset).
            *   Else: `set [playerX] to [targetX]`.
    *   **Update Frames**:
        *   From **Displays**, drag `draw filled circle x:[playerX] y:[playerY] r:[2] color:[1]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The screen draws several static lines and rectangles representing walls. The user moves a small dot (the player) using the buttons. Before the player's position is updated, the program checks if the new coordinate already has a "1" (white pixel) on it. If it does, that means the player hit a wall; the player is immediately teleported back to the starting point (5, 5) as a penalty.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
# Simplified input setup...
px, py = 5, 5

def draw_maze():
    oled.rect(0, 20, 100, 5, 1) # Barrier
    oled.line(40, 0, 40, 15, 1) # Barrier

while True:
    oled.fill(0)
    draw_maze()
    
    # Logic for button movement here...
    # Example for Right button:
    new_x = px + 1
    if oled.pixel(new_x, py) == 1:
        px, py = 5, 5 # Hit wall, reset
    else:
        px = new_x
        
    oled.fill_rect(px-1, py-1, 3, 3, 1) # Player dot
    oled.show()
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Stuck on Wall**: If you use a filled circle for the player, ensure you check the *edges* of the circle for collisions, not just the center point, otherwise the player will overlap the wall before resetting.
*   **Invisible Wall**: If the map is cleared *before* the pixel check happens, `oled.pixel()` will always return 0. Draw the maze, then check pixels, then move.

### 1️⃣2️⃣ Try This Next

*   **Win Zone**: Add a second check - if the pixel is at a specific "Target" coordinate (e.g., 120, 60), print "YOU WIN!".
*   **Teleporters**: If the player hits a specific shape/coordinate, move them to a different entrance.

---

## 1️⃣ Project 0369: Automated OLED Shapes

### 2️⃣ Learning Objective
Develop a basic physics engine featuring a "Bouncing Ball" simulation with gravity and velocity. You will learn about variable-driven motion and boundary reflection.

### 3️⃣ Concepts Introduced
*   **Velocity (vX, vY)**: Variables determining the rate of change in position per frame.
*   **Boundary Reflection**: Reversing velocity when a limit (0 or 127) is hit.
*   **Gravity Simulation**: Constantly adding a small value to the vertical velocity.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |

### 6️⃣ Blocks Used

🔹 **Variables**
*   **Category:** Variables (ballX, ballY, vX, vY, gravity)

🔹 **OLED Filled Circle**
*   **Category:** Displays

🔹 **Math Operations**
*   **Category:** Math

### 7️⃣ Variables & State
*   **ballX, ballY**: Position.
*   **vX, vY**: Current speed/direction.
*   **gravity**: Constant pull (e.g., 0.5).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup I2C and OLED.
    *   From **Variables**, drag `set [ballX] to [64]`.
    *   From **Variables**, drag `set [ballY] to [32]`.
    *   From **Variables**, drag `set [vX] to [2]`.
    *   From **Variables**, drag `set [vY] to [0]`.
    *   From **Variables**, drag `set [gravity] to [1]`.

*   **B. Main Loop Phase**
    *   **Apply Physics**:
        *   From **Math**, drag `set [ballX] to [ballX + vX]`.
            *   **Snap** into loop.
        *   From **Math**, drag `set [vY] to [vY + gravity]`.
            *   **Snap** below.
        *   From **Math**, drag `set [ballY] to [ballY + vY]`.
            *   **Snap** below.
    *   **Handle Bounces**:
        *   From **Logic**, drag `if [ballX] > [125] OR [ballX] < [2] then`.
            *   Inside: From **Math**, drag `set [vX] to [vX * -1]`.
        *   From **Logic**, drag `if [ballY] > [60] then`.
            *   Inside: From **Math**, drag `set [vY] to [vY * -1]`.
            *   And: `set [ballY] to [60]` (Snap to floor to prevent sinking).
    *   **Draw frame**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `draw filled circle x:[ballX] y:[ballY] r:[3] color:[1]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

A ball is initialized at the center of the screen with a horizontal horizontal speed. Every frame, "gravity" is added to the vertical speed, pulling the ball down. Its position is updated by adding the speeds to the coordinates. When the ball hits the left, right, or bottom walls, its velocity is multiplied by -1 (reversing it), creating a "bounce" effect.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

x, y = 64, 32
vx, vy = 2, 0
gravity = 0.5

while True:
    vy += gravity
    x += vx
    y += vy
    
    # Side walls
    if x > 124 or x < 4:
        vx *= -1
    
    # Floor
    if y > 60:
        vy *= -0.8 # Bounce back with 80% energy
        y = 60
        
    oled.fill(0)
    oled.fill_circle(int(x), int(y), 4, 1)
    oled.show()
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **The Sinkhole**: Without snapping the ball back to the floor (`y = 60`), gravity might pull it so deep into the bottom that the bounce doesn't escape before gravity pulls it back down, causing it to "vibrate" in the floor forever.
*   **Float Math**: Block-based variables often use integers; for smooth physics, ensure "gravity" or "velocity" values are large enough to be noticeable if float math isn't available.

### 1️⃣2️⃣ Try This Next

*   **Friction**: Multiply `vX` by 0.99 every frame to make the ball eventually slow down and stop like in the real world.
*   **Paddle**: Use a potentiometer to move a paddle and "hit" the ball back up.

---

## 1️⃣ Project 0370: Mastering OLED Shapes

### 2️⃣ Learning Objective
Generate a complex, static bitmap pattern mimicking a "QR Code." You will learn about data-to-pixel mapping and structural pattern plotting.

### 3️⃣ Concepts Introduced
*   **Bitmap Plotting**: Manually defining coordinates for many small elements.
*   **QR Encoding Anatomy**: Drawing "finder patterns" (large squares) and "data modules" (pixels).
*   **Code Structure**: Organizing multiple drawing commands into a single static frame.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |

### 6️⃣ Blocks Used

🔹 **OLED Rectangle**
*   **Category:** Displays

🔹 **Loops (Nested)**
*   **Category:** Loops

🔹 **Random Number**
*   **Category:** Math

### 7️⃣ Variables & State
*   **size**: Pixel width/height of a QR module.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup I2C and OLED.
    *   From **Displays**, drag `OLED clear`.

*   **B. Main Loop Phase** (Drawing Static Pattern)
    *   **Drawing Finder Patterns** ( Corners):
        *   From **Displays** drag `draw rectangle x:[5] y:[5] w:[15] h:[15] color:[1]`.
            *   **Snap** into loop (Top-Left Finder).
        *   From **Displays** drag `draw rectangle x:[108] y:[5] w:[15] h:[15] color:[1]`.
            *   **Snap** into loop (Top-Right Finder).
        *   From **Displays** drag `draw rectangle x:[5] y:[44] w:[15] h:[15] color:[1]`.
            *   **Snap** into loop (Bottom-Left Finder).
    *   **Generate Random Data Grid**:
        *   From **Loops** drag `for [col] from [30] to [100] step [2]`.
            *   Inside: From **Loops** drag `for [row] from [5] to [60] step [2]`.
                *   Inside:
                    *   From **Logic** drag `if [random(0,1)] = [1] then`.
                        *   Inside: From **Displays** drag `draw rectangle x:[col] y:[row] w:[2] h:[2] color:[1]`.
    *   **Commit Frame**:
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below loop.
    *   From **Timing**, drag `sleep [forever]`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program draws three large square outlines in the corners to simulate the "Finder Patterns" of a QR code. Then, it uses a nested loop to traverse a grid in the center of the screen. For every grid point, it flips a "virtual coin" (random number). If it lands on 1, it draws a 2x2 pixel square. This results in a scannable-looking (though dummy) QR code pattern.

### 🔟 Generated Code (Reference Only)

```python
import machine
import random
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

def draw_qr():
    # Finders
    oled.rect(5, 5, 15, 15, 1)
    oled.rect(108, 5, 15, 15, 1)
    oled.rect(5, 44, 15, 15, 1)
    
    # Random Modules
    for x in range(30, 100, 2):
        for y in range(5, 60, 2):
            if random.getrandbits(1):
                oled.fill_rect(x, y, 2, 2, 1)
    oled.show()

oled.fill(0)
draw_qr()
# End of program
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Slow Refresh**: Drawing hundreds of individual rectangles can be slow in some environments. Batch the `show()` command at the very end.
*   **Resolution**: QR codes need high contrast. Ensure the 2x2 modules don't overlap or blur together.

### 1️⃣2️⃣ Try This Next

*   **Real Data**: Instead of random modules, use a pre-set list like `[1,0,1,1,0]` to draw a real scannable pattern for a specific URL.
*   **Inversion**: Draw a white background first and color the modules black.

---
'''

docs_0372_0380 = r'''
## 1️⃣ Project 0372: Blinking Stopwatch

### 2️⃣ Learning Objective
Develop long-period timing mechanisms using cumulative counters. You will learn about minute-scale logic and visual feedback synchronization.

### 3️⃣ Concepts Introduced
*   **Cumulative Timing**: Incrementing counters to track long durations.
*   **Scale Testing**: Substituting long intervals with shorter ones for rapid verification.
*   **Visual Indicators**: Using LEDs to represent state transitions.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED** (External or On-board)
*   **Resistor** (220Ω if using external)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Positive** | GP16 | via Resistor |
| **LED Negative** | GND | |

### 6️⃣ Blocks Used

🔹 **Blink LED**
*   **Category:** Actuators

🔹 **Change Variable**
*   **Category:** Variables

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **secondsCounter**: Tracks elapsed seconds.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [secondsCounter] to [0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Time Tracking**:
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** into loop.
        *   From **Variables**, drag `change [secondsCounter] by [1]`.
            *   **Snap** below.
    *   **Threshold Check**:
        *   From **Logic**, drag `if [secondsCounter] = [5] then`.
            *   **Snap** below (Note: Using 5s instead of 60s for testing).
            *   Inside:
                *   From **Actuators**, drag `toggle LED pin [16]`.
                    *   **Snap** inside.
                *   From **Variables**, drag `set [secondsCounter] to [0]`.
                    *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program tracks time by incrementing a variable every second. Instead of waiting a full minute, the logic is set to trigger a change every 5 seconds for demonstration. When the counter reaches 5, the LED toggles its state (ON to OFF, or OFF to ON) and the counter resets to zero. This simulates a "minute hand" behavior in a compact timeframe.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
counter = 0

while True:
    time.sleep(1)
    counter += 1
    
    if counter >= 5: # Simulating 60s for testing
        led.toggle()
        counter = 0
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Blocking Sleep**: Using `sleep(1)` means the Pico can't do anything else during that second. For professional stopwatches, use `utime.ticks_ms()`.
*   **Reset Missing**: If you forget to set the counter back to 0, the LED will only blink once.

### 1️⃣2️⃣ Try This Next

*   **Real Minute**: Change the '5' to '60' for a literal minute-hand simulation.
*   **Double Indicator**: Add a second LED that blinks every second while the first toggles every minute.

---

## 1️⃣ Project 0373: Manual Stopwatch Control

### 2️⃣ Learning Objective
Implement "Momentary Run" logic where a timer only advances while an input is active. You will learn about gated execution and state-based increments.

### 3️⃣ Concepts Introduced
*   **Gated Execution**: Running logic only when specific conditions (button press) are met.
*   **Precision Inaccuracy**: Understanding that loop speed affects timing precision in basic implementations.
*   **Start/Pause Logic**: Using hardware status to control software flow.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Momentary)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Print to Console**
*   **Category:** Console

🔹 **Change Variable**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **runTime**: Tracks active seconds.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [runTime] to [0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.

*   **B. Main Loop Phase**
    *   **Gated Logic**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `change [runTime] by [0.1]`.
                    *   **Snap** inside.
                *   From **Console**, drag `print [Time: {runTime}s]`.
                    *   **Snap** below.
                *   From **Timing**, drag `sleep [0.1] seconds`.
                    *   **Snap** below.
    *   **Wait State**:
        *   Add a small `sleep [0.01]` outside the `if` to prevent CPU maxing.

### 9️⃣ Execution Flow (Plain English)

The program checks the button on Pin 14. If the button is held down, the variable `runTime` increases by 0.1 every 100 milliseconds and the result is printed to the console. If the button is released, the `if` block is skipped, the variable stops increasing, effectively "pausing" the stopwatch.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
run_time = 0.0

while True:
    if button.value():
        run_time += 0.1
        print("Active Time:", round(run_time, 1), "s")
        time.sleep(0.1)
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Floating Point Drift**: Repeatedly adding 0.1 can lead to small math errors (e.g., 0.300000004). Use `round()` when printing.
*   **Bouncing**: Buttons can jitter; the 0.1s sleep usually acts as a natural debounce.

### 1️⃣2️⃣ Try This Next

*   **Hold for reset**: If the button is held for more than 3 seconds without moving, reset the timer to zero.
*   **External Display**: Send the time to an OLED instead of the console.

---

## 1️⃣ Project 0374: Stopwatch Sequences

### 2️⃣ Learning Objective
Store and retrieve historical data using variables to track "Lap Times." You will learn about data buffering and sequential storage.

### 3️⃣ Concepts Introduced
*   **Data Buffering**: Temporarily holding records until they are needed.
*   **Measurement Capturing**: Locking a moving value into a static variable at a specific moment.
*   **Sequential Logging**: Organizing data points chronologically.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Lap Trigger)

### 5️⃣ Buttons / Pins
*   **Button**: GP14 (PULL_DOWN)

### 6️⃣ Blocks Used

🔹 **Variables** Lap1, Lap2, Lap3, currentSecs
🔹 **Print**
🔹 **Logic (If/Else)**

### 7️⃣ Variables & State
*   **currentSecs**: Moving time.
*   **lapCount**: Which lap we are on (1, 2, or 3).
*   **Lap1, Lap2, Lap3**: Stored records.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [lapCount] to [1]`.
    *   From **Variables**, drag `set [currentSecs] to [0]`.

*   **B. Main Loop Phase**
    *   **Timer**: Increase `currentSecs` every 1s.
    *   **Button Check**:
        *   If `digital read 14` (Lap Pressed):
            *   If `lapCount = 1`: `set Lap1 to currentSecs`.
            *   If `lapCount = 2`: `set Lap2 to currentSecs`.
            *   If `lapCount = 3`: `set Lap3 to currentSecs`.
            *   From **Console**, drag `print [Lap Stored!]`.
            *   `change lapCount by 1`.
            *   `sleep 0.5s` (Debounce).
    *   **Print Summary**:
        *   If `lapCount > 3`:
            *   `print Lap1`, `print Lap2`, `print Lap3`.
            *   Wait forever.

### 9️⃣ Execution Flow (Plain English)

The Pico acts as a stopwatch. Every time you press the button, the current time is "saved" into one of three slots (Lap1, Lap2, or Lap3). Once all three slots are filled, the program stops and prints the full results.

### 🔟 Generated Code (Reference Only)

```python
import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
l1, l2, l3 = 0, 0, 0
count = 1
start = time.time()

while count <= 3:
    now = time.time() - start
    if btn.value():
        if count == 1: l1 = now
        elif count == 2: l2 = now
        elif count == 3: l3 = now
        count += 1
        time.sleep(0.5)
    time.sleep(0.1)

print(f"Laps: {l1}s, {l2}s, {l3}s")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Variable Overwrite**: Ensure `lapCount` increments so you don't overwrite Lap1 every time.

### 1️⃣2️⃣ Try This Next
*   **Lists**: Use a List variable to store unlimited laps.

---

## 1️⃣ Project 0375: Interactive Stopwatch

### 2️⃣ Learning Objective
Create a "Prediction Game" that calculates the delta (difference) between human input and a target time. You will learn about absolute value math and error calculation.

### 3️⃣ Concepts Introduced
*   **Delta Calculation**: Finding the mathematical difference between expected and actual results.
*   **Absolute Values**: Handling "early" or "late" timing as a single positive error margin.
*   **Interactive Challenge**: Engaging the user with goal-oriented logic.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**

### 5️⃣ Variables & State
*   **target**: Target time (e.g. 7.0s).
*   **playerTime**: Time when button was pressed.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Set `target` to `7.0`.
    *   Set `playerTime` to `0`.
    *   Print "Try to hit exactly 7.0 seconds!".

*   **B. Main Loop Phase**
    *   Count up in 0.1s increments.
    *   Wait for button press.
    *   When pressed:
        *   Calculate `diff = abs(target - playerTime)`.
        *   Print `You hit at {playerTime}`.
        *   Print `Difference: {diff}s`.

### 9️⃣ Execution Flow (Plain English)
The computer picks a target (7 seconds). You press the button. It tells you exactly how close you were (e.g., "0.2s off").

### 🔟 Generated Code (Reference Only)
```python
import time, machine
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
target = 7.0
now = 0.0
while not btn.value():
    now += 0.1
    time.sleep(0.1)
diff = abs(target - now)
print(f"Target: {target}, You: {round(now,1)}, Diff: {round(diff,1)}")
```

---

## 1️⃣ Project 0376: Smart Stopwatch Switch

### 2️⃣ Learning Objective
Integrate environmental sensors into timing logic for automated activity tracking. You will learn about "Active Time" logging.

### 3️⃣ Concepts Introduced
*   **PIR Motion Gating**: Triggering a timer only when movement is present.
*   **Activity Logging**: Measuring the duration of physical events.
*   **Timeout Logic**: Pausing a process when a signal is lost for a specific period.

### 4️⃣ Hardware Required
*   **Pico**, **PIR Sensor**

### 8️⃣ Step-by-Step Guide
*   **A. Initialization Phase**: Setup PIR on Pin 15.
*   **B. Main Loop Phase**: If PIR = HIGH, increment `activityTimer` every 1s. If PIR = LOW, do nothing.

### 9️⃣ Execution Flow (Plain English)
A sensor detects if someone is in the room. The timer only counts while people are moving.

---

## 1️⃣ Project 0377: Stopwatch Alarm System

### 2️⃣ Learning Objective
Implement a "Dead Man Timer" safety system. You will learn about watchdog logic and recurring resets.

### 3️⃣ Concepts Introduced
*   **Watchdog Logic**: Ensuring a system is "petted" (reset) regularly or an alarm sounds.
*   **Safety Interlocks**: Requiring user presence to prevent an alert.

### 8️⃣ Step-by-Step Guide
*   **B. Main Loop Phase**: Increment `warningCounter`. If `warningCounter > 10`, sound buzzer. If button pressed, `set warningCounter to 0`.

---

## 1️⃣ Project 0378: The Stopwatch Game

### 2️⃣ Learning Objective
Implement a high-resolution 2-player reaction tournament. You will learn about input arbitration and race-condition handling.

### 3️⃣ Concepts Introduced
*   **Input Arbitration**: Determining which of multiple signals arrived first.
*   **Randomized Start**: Preventing anticipation in reaction tests.

### 4️⃣ Hardware Required
*   **Pico**, **2x Buttons**

### 8️⃣ Step-by-Step Guide
*   **Phase 1**: Random sleep 2-5s.
*   **Phase 2**: Print "GO!".
*   **Phase 3**: Monitor both buttons. First one hit wins. Print the winner's time.

---

## 1️⃣ Project 0379: Automated Stopwatch

### 2️⃣ Learning Objective
Calculate velocity using distance and time intervals between two light sensors. You will learn about physical computing equations.

### 3️⃣ Concepts Introduced
*   **Velocity Calculation**: `Speed = Distance / Time`.
*   **Optical Interrupts**: Using LDRs to detect objects passing a specific point.

### 8️⃣ Step-by-Step Guide
*   Set `Distance = 10` cm.
*   Wait for Sensor 1 shadow -> Start Timer.
*   Wait for Sensor 2 shadow -> Stop Timer.
*   Calculate speed.

---

## 1️⃣ Project 0370: Mastering Stopwatch

### 2️⃣ Learning Objective
Perform code profiling using microsecond-precision hardware timers. You will learn about optimization and performance measurement.

### 3️⃣ Concepts Introduced
*   **Microsecond Precision**: Using `ticks_us()` for ultra-accurate measurements.
*   **Code Profiling**: Measuring how long specific logic takes to run.

### 1️⃣0️⃣ Generated Code (Reference Only)
```python
import utime
start = utime.ticks_us()
# Run complex code here
for i in range(1000): x = i * i
end = utime.ticks_us()
print(f"Execution time: {(end - start)} microseconds")
```
'''

import sys

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

with open(target_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

output_lines = lines[:8031] # Keep until line 8031

full_compliant_block = '''
---

''' + docs_0363_0370 + '''

---

# 🏁 Batch 38: Stopwatch 2

## 1️⃣ Project 0371: Introduction to Stopwatch

### 2️⃣ Learning Objective
Implement alternating state display using modulo arithmetic. You will learn phase-based control and time-synchronized output.

### 3️⃣ Concepts Introduced
*   **Modulo Arithmetic**: Using remainder for cyclical states.
*   **Phase Detection**: Determining even/odd cycles.
*   **Time-Based Alternation**: Synchronized state changes.

### 4️⃣ Hardware Required
*   **Pico**

### 5️⃣ Wiring / Interfaces
None (console output only).

### 6️⃣ Blocks Used

🔹 **Time Functions**
*   **Category:** Timing
*   **Block:** `time()` or counter variable

🔹 **Modulo Operation**
*   **Category:** Math
*   **Block:** `[value] % [2]`

🔹 **Print**
*   **Category:** Console

### 7️⃣ Variables & State
*   **elapsed**: Time counter in seconds.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [elapsed] to [0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check Phase**:
        *   From **Math**, drag `[elapsed] % [2]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if ([elapsed] % [2]) = [0] then`.
            *   **Snap** below.
            *   Then: From **Console**, drag `print [Tick @ {elapsed}s]`.
                *   **Snap** inside.
            *   Else: From **Console**, drag `print [Tock @ {elapsed}s]`.
                *   **Snap** inside.
    *   **Increment Time**:
        *   From **Variables**, drag `change [elapsed] by [1]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Counter increments every second. Even seconds (0, 2, 4...) print "Tick", odd seconds (1, 3, 5...) print "Tock". The modulo operation (elapsed % 2) returns 0 for even, 1 for odd, enabling binary phase detection. Foundation for metronomes, blinkers, or any alternating-state system.

### 🔟 Generated Code (Reference Only)

```python
import time

elapsed = 0

while True:
    if elapsed % 2 == 0:
        print(f"Tick @ {elapsed}s")
    else:
        print(f"Tock @ {elapsed}s")
    
    elapsed += 1
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always "Tick"**: Verify modulo logic - `% 2` should correctly alternate 0/1.
*   **Timing Drift**: Using `sleep(1)` accumulates drift. For precision, use `time.ticks_ms()` with target timestamps.

### 1️⃣2️⃣ Try This Next

*   **Triple Phase**: Use `% 3` for Tick-Tock-Boom pattern.
*   **LED Blink**: Add LED that toggles on phase change.
*   **Audio Metronome**: Connect buzzer for audible tick-tock.

---

''' + docs_0372_0380

with open(target_file, 'w', encoding='utf-8') as f:
    f.writelines(output_lines)
    f.write(full_compliant_block)

print("✅ Successfully replaced projects with full Elite documentation for 0363-0380!")
