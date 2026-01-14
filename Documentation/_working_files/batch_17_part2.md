
## Project 0164: OLED Shapes Sequences

### 1. Learning Objective
Understand how to manage library-specific primitive shapes. Learn how to alternate between geometric types (Triangle, Circle, Square) to create a visual sequence or splash screen.

### 2. Concepts Introduced
*   **Geometric Primitives**: Built-in functions for drawing complex shapes beyond a single pixel.
*   **Buffer Clearing**: Ensuring a "Clean Frame" before drawing a new shape in a sequence.
*   **Refresh Management**: Efficiently switching between different drawing states.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0161)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Displays, drag `pico_oled_rect`** (draw square)
*   **from Displays, drag `pico_oled_circle`** (draw circle)
*   **from Displays, drag `pico_oled_triangle`** (draw triangle)
*   **from Displays, drag `pico_oled_clear`** (clear)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **None**: Pre-programmed sequence.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Display**: From **Displays**, drag `pico_oled_init`.

**B. Sequence Phase (Loop)**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.

3.  **Draw Shape 1 (Triangle)**:
    *   **Clear** memory buffer.
    *   From **Displays**, drag `pico_oled_triangle`.
    *   **Set** P1=(64,10), P2=(34,54), P3=(94,54).
    *   **Push** to screen with `pico_oled_show`.
    *   **Wait** 1 second.

4.  **Draw Shape 2 (Circle)**:
    *   **Clear** memory buffer.
    *   From **Displays**, drag `pico_oled_circle`.
    *   **Set** Center=(64,32), Radius=25.
    *   **Push** with `pico_oled_show`.
    *   **Wait** 1 second.

5.  **Draw Shape 3 (Square)**:
    *   **Clear** memory buffer.
    *   From **Displays**, drag `pico_oled_rect`.
    *   **Set** X=39, Y=7, Width=50, Height=50.
    *   **Push** with `pico_oled_show`.
    *   **Wait** 1 second.

### 8. Execution Flow
1.  **Clear**: The Pico wipes the virtual canvas.
2.  **Render**: A triangle is calculated and placed in the buffer.
3.  **Display**: The triangle appears on the OLED for 1 second.
4.  **Transition**: The process repeats with the circle, then the square.
5.  **Result**: An automated geometric slideshow.

### 9. Generated Code
```python
import machine
import ssd1306
import utime

# Init
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # 1. Triangle (using lines)
    oled.fill(0)
    oled.line(64, 10, 34, 54, 1)
    oled.line(34, 54, 94, 54, 1)
    oled.line(94, 54, 64, 10, 1)
    oled.show()
    utime.sleep(1)
    
    # 2. Circle
    oled.fill(0)
    # Placeholder for circle logic (standard ssd1306 doesn't have circle)
    # We use multiple lines or dots to simulate circle
    for i in range(0, 360, 5):
        import math
        x = int(64 + 25 * math.cos(math.radians(i)))
        y = int(32 + 25 * math.sin(math.radians(i)))
        oled.pixel(x, y, 1)
    oled.show()
    utime.sleep(1)
    
    # 3. Square
    oled.fill(0)
    oled.rect(39, 7, 50, 50, 1)
    oled.show()
    utime.sleep(1)
```

### 10. Common Mistakes
*   **Buffer Overlap**: Forgetting to `clear()` between shapes will result in all shapes being drawn on top of each other.
*   **Coordinate Math**: Triangles require 3 points (6 numbers). Ensure they stay within 128x64.

### 11. Try This Next
*   **Solid Sequence**: Change the blocks to use "Fill" versions (Solid Triangle, Solid Circle, Solid Square).
*   **Nested Shapes**: Try drawing a square WITH a circle inside it and hold that on screen.

---

## Project 0165: Interactive OLED Shapes

### 1. Learning Objective
Explore dynamic geometric manipulation. Learn how to use external digital inputs (buttons) to modify a numerical variable (radius) that directly controls the rendering of a shape on screen.

### 2. Concepts Introduced
*   **Dynamic Geometry**: Changing shape properties (size, position) in real-time.
*   **Variable Binding**: connecting a button state to a numerical value increment/decrement.
*   **UI Feedback**: Visualizing the result of a user action immediately on a display.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   2 Buttons
*   2x 10k Ohm pull-down resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A (+)** | GP14 | Increases size |
| **Button B (-)** | GP13 | Decreases size |
| **OLED (I2C)** | GP0/GP1 | Visual output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Displays, drag `pico_oled_circle`** (draw circle)
*   **from Displays, drag `pico_oled_clear`** (clear)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **radius**: Current size of the circle (initialized to 10).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Initialize the OLED at GP0/GP1.
2.  **Initialize Value**: From **Variables**, **Set** `radius` = 10.

**B. Input Phase (Loop)**
3.  **Start Loop**: From **Loops**, drag `pico_forever`.
4.  **Handle Increase Button**:
    *   If **Smart IO** `pico_gpio_read` GP14 is True (A).
    *   **Action**: If `radius` < 30 (limit), **Set** `radius` = `radius` + 2.
5.  **Handle Decrease Button**:
    *   If **Smart IO** `pico_gpio_read` GP13 is True (B).
    *   **Action**: If `radius` > 2 (limit), **Set** `radius` = `radius` - 2.

**C. Render Phase**
6.  **Refresh Graphics**:
    *   **Clear** memory buffer.
    *   From **Displays**, drag `pico_oled_circle`.
    *   **Set** Center=(64,32), Radius=`radius`.
    *   Push with `pico_oled_show`.
7.  **Response Delay**: **Wait** 0.1 seconds (for smooth scaling feeling).

### 8. Execution Flow
1.  **Monitor**: The Pico checks for button presses.
2.  **Adjust**: If 'A' is pressed, the value in `radius` grows.
3.  **Clear**: The old frame is wiped.
4.  **Redraw**: A new circle is drawn using the updated `radius` value.
5.  **Result**: The user sees the circle "Grow" or "Shrink" based on their button taps.

### 9. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time
import math

# Init
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn_up = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_down = Pin(13, Pin.IN, Pin.PULL_DOWN)

radius = 10

while True:
    if btn_up.value() == 1 and radius < 30:
        radius += 2
    if btn_down.value() == 1 and radius > 2:
        radius -= 2
        
    oled.fill(0)
    # Manual circle draw
    for i in range(0, 360, 10):
        x = int(64 + radius * math.cos(math.radians(i)))
        y = int(32 + radius * math.sin(math.radians(i)))
        oled.pixel(x, y, 1)
        
    oled.show()
    time.sleep(0.05)
```

### 10. Common Mistakes
*   **Bounding Error**: If `radius` gets too large (e.g., 100), the circle drawing might attempt to draw pixels off-screen and cause unexpected results. Always cap the variable.
*   **Missing `clear()`**: If you forget to clear, the screen will fill with overlapping circles of all previous sizes.

### 11. Try This Next
*   **Speed Scaling**: Make the circle grow faster if 'A' is HELD down rather than just tapped.
*   **Pulse Effect**: Instead of buttons, use a calculation to make the circle "breathe" (grow and shrink automatically).

---

## Project 0166: Smart OLED Shapes Switch

### 1. Learning Objective
Explore data visualization (GUI basics). Learn how to create a "Battery Bar" indicator where a numerical percentage (0-100) is translated into the physical width of a drawn rectangle.

### 2. Concepts Introduced
*   **Data-Driven Graphics**: Using a data variable to control a visual property (width).
*   **UI Layout**: combining static outlines with dynamic fill areas.
*   **Clamping/Saturation**: Ensuring a 110% charge doesn't draw outside the battery icon.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Potentiometer (to simulate charge level)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Simulates battery voltage |
| **OLED (I2C)** | GP0/GP1 | HUD display |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Displays, drag `pico_oled_rect`** (draw outline and fill)
*   **from Math, drag `math_map`** (scale 0-1023 to 0-40)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **charge**: Simulated percentage (0-100).
*   **fill_width**: Calculated pixel width for the bar.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**: From **Displays**, drag `pico_oled_init`.

**B. Monitoring Phase (Loop)**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.
3.  **Read Potential**:
    *   Read GP26. **Map** [0 to 1023] into [0 to 100].
    *   **Set** variable `charge` to this percentage.

**C. Visualization Phase**
4.  **Clear Screen**: `pico_oled_clear`.
5.  **Draw Battery Case (Static)**:
    *   From **Displays**, drag `pico_oled_rect`.
    *   **Set** X=44, Y=22, Width=40, Height=20, Fill=False. (The main box).
    *   **Set** X=84, Y=27, Width=4, Height=10, Fill=True. (The battery 'tip' or 'positive terminal').
6.  **Draw Battery Charge (Dynamic)**:
    *   From **Math**, calculate `fill_width` = (`charge` / 100) * 36. (36 pixels is the inner width).
    *   From **Displays**, drag `pico_oled_rect`.
    *   **Set** X=46, Y=24, Width=`fill_width`, Height=16, Fill=True.
7.  **Finalize**:
    *   Snap `pico_oled_show`.
    *   **Wait** 0.1 seconds.

### 8. Execution Flow
1.  **Input**: The user turns the knob (simulating a battery draining or charging).
2.  **Calc**: The Pico converts the knob position into a percentage.
3.  **Static**: The battery outline is drawn first.
4.  **Dynamic**: The "Fill" box is drawn inside the outline, its width expanding or shrinking.
5.  **Result**: A realistic battery meter that updates in real-time.

### 9. Generated Code
```python
import machine
import ssd1306
import utime

# Init
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
knob = machine.ADC(26)

while True:
    # Read simulated charge
    val = knob.read_u16()
    percent = (val / 65535) * 100
    
    # Calculate pixel width (inner space is 40-4=36)
    fill_px = int((percent / 100) * 36)
    
    oled.fill(0)
    
    # 1. Main Outline
    oled.rect(44, 22, 40, 20, 1)
    
    # 2. Battery Tip
    oled.fill_rect(84, 27, 4, 10, 1)
    
    # 3. Dynamic Fill
    if fill_px > 0:
        oled.fill_rect(46, 24, fill_px, 16, 1)
        
    oled.show()
    utime.sleep(0.1)
```

### 10. Common Mistakes
*   **Fill vs Outline**: If you fill the battery case, you won't see the interior bar clearly. Always use `Fill=False` for the outer shell.
*   **Coordinate Misalignment**: Make sure the filling box (Starting at X=46) actually sits inside the outline box (Starting at X=44).

### 11. Try This Next
*   **Low Battery Warning**: If `charge` is < 20, make the entire battery icon FLASH to warn the user.
*   **Voltage Text**: add `pico_oled_text` below the battery to show the exact percentage number.

---
