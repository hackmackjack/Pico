
# BATCH 17: OLED Shapes 1 (Projects 0161-0170)

## Project 0161: Introduction to OLED Shapes

### 1. Learning Objective
Learn the fundamentals of coordinate-based graphics on an OLED display. Understand how to control individual pixels to create the building blocks for all visual interfaces.

### 2. Concepts Introduced
*   **Pixel-Based Rendering**: Addressing the screen as a grid of individual light-emitting points.
*   **XY Coordinate System**: Understanding the screen as a 128x64 grid where (0,0) is usually the top-left corner.
*   **Atomic Units**: Recognizing that every complex shape is just a collection of pixels.

### 3. Hardware Required
*   Raspberry Pi Pico
*   I2C OLED Display (SSD1306, 128x64)
*   Jumper wires
*   Breadboard

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED VCC** | 3.3V | Power |
| **OLED GND** | GND | Ground |
| **OLED SCL** | GP1 (I2C0 SCL) | Clock Line |
| **OLED SDA** | GP0 (I2C0 SDA) | Data Line |

### 5. Blocks Used
*   **from Displays, drag `pico_oled_init`** (initialize I2C OLED)
*   **from Displays, drag `pico_oled_pixel`** (draw pixel at X... Y...)
*   **from Displays, drag `pico_oled_show`** (update display)

### 6. Variables
*   **None**: This project focuses on fixed coordinates.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize the Display**:
    *   From **Displays**, drag the `pico_oled_init` block and snap it into the workspace.
    *   **Set** SCL pin to GP1 and SDA pin to GP0.

**B. Rendering Phase**
2.  **Draw First Pixel**:
    *   From **Displays**, drag the `pico_oled_pixel` block and snap it below initialization.
    *   **Set** X to 10 and Y to 10.
    *   Ensure the state is set to ON (or color = 1).
3.  **Draw Second Pixel**:
    *   From **Displays**, drag another `pico_oled_pixel` block.
    *   **Set** X to 60 and Y to 30.
4.  **Update the Hardware**:
    *   From **Displays**, drag the `pico_oled_show` block and snap it at the end.
    *   *Note: Graphics are drawn in the Pico's memory first; this block sends the image to the actual screen.*

### 8. Execution Flow
1.  **Start**: The Pico configures the I2C communication with the OLED.
2.  **Paint**: Two specific bits in the Pico's display buffer are flipped to "1" (Active).
3.  **Sync**: The `pico_oled_show` command pushes the buffer to the physical OLED controller.
4.  **Result**: Two tiny dots appear on the dark screen at the specified grid locations.

### 9. Generated Code
```python
import machine
import ssd1306

# Configure I2C
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Draw individual pixels
oled.pixel(10, 10, 1)
oled.pixel(60, 30, 1)

# Push buffer to hardware
oled.show()
```

### 10. Common Mistakes
*   **Coordinates Out of Bounds**: Trying to draw at (150, 80) on a 128x64 screen will either do nothing or throw an error.
*   **Forgetting `show()`**: The pixels will exist in memory, but the screen will remain blank until `show()` is called.
*   **I2C Swap**: Swapping SDA and SCL pins will prevent the display from initializing.

### 11. Try This Next
*   **Corner Challenge**: Try to light up the four extreme corners of the screen: (0,0), (127,0), (0,63), and (127,63).
*   **Connect the Dots**: Try drawing a third pixel at (35, 20) halfway between the two.

---

## Project 0162: Blinking OLED Shapes

### 1. Learning Objective
Learn how to create animated effects on a display. Understand the "Draw-Wait-Clear" cycle required to make static shapes appear to flash or change over time.

### 2. Concepts Introduced
*   **Animation Loop**: Repeating a set of visual commands to simulate motion or state changes.
*   **Inversion/Clearing**: Removing or "turning off" a drawn area to reset the visual state.
*   **Refresh Strategy**: Balancing drawing logic with timing delays.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0161)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Displays, drag `pico_oled_rect`** (draw rectangle)
*   **from Displays, drag `pico_oled_show`** (update display)
*   **from Displays, drag `pico_oled_clear`** (clear display)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Direct timing control.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**:
    *   From **Displays**, drag `pico_oled_init` to the start.

**B. Animation Phase**
2.  **Create Infinite Loop**:
    *   From **Loops**, drag the `pico_forever` block.
3.  **Draw the Shape**:
    *   Inside the loop, from **Displays**, drag `pico_oled_rect`.
    *   **Set** X = 59, Y = 27 (Center-ish).
    *   **Set** Width = 10, Height = 10.
    *   **Set** Fill = True (Solid box).
4.  **Display and Wait (State ON)**:
    *   Snap a `pico_oled_show` block.
    *   Snap a `pico_wait` block -> 0.5 seconds.
5.  **Clear the Shape**:
    *   From **Displays**, drag `pico_oled_clear`. (This empties the memory buffer).
6.  **Display and Wait (State OFF)**:
    *   Snap a `pico_oled_show` block.
    *   Snap a `pico_wait` block -> 0.5 seconds.

### 8. Execution Flow
1.  **Draw**: A solid square is painted into the Pico's memory.
2.  **Flash ON**: The `show()` command makes the square appear on screen for half a second.
3.  **Wipe**: The memory is cleared.
4.  **Flash OFF**: The `show()` command updates the screen to be blank for half a second.
5.  **Repeat**: The square appears and disappears continuously.

### 9. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Phase 1: Draw
    oled.fill_rect(59, 27, 10, 10, 1)
    oled.show()
    time.sleep(0.5)
    
    # Phase 2: Clear
    oled.fill(0)
    oled.show()
    time.sleep(0.5)
```

### 10. Common Mistakes
*   **Clearing Without `show()`**: Just calling `clear()` won't turn off the pixels on screen; you MUST call `show()` after clearing.
*   **Centered Math**: Remember that a 10x10 square at (64,32) starts its top-left at the center, meaning it isn't perfectly centered. Subtract half the width/height for better centering.

### 11. Try This Next
*   **Hollow Blink**: Set `Fill` to False to blink just the outline of the square.
*   **Alternating Shapes**: Instead of clearing to black, replace the square with a circle during the second phase.

---

## Project 0163: Manual OLED Shapes Control

### 1. Learning Objective
Explore real-time user-driven graphics (Etch-a-Sketch). Learn how to link multiple analog inputs (potentiometers) to screen coordinates and implement "Persistence" to leave a path behind.

### 2. Concepts Introduced
*   **Persistence**: Intentionally NOT clearing the screen between frames to build an image.
*   **Input-to-Coordinate Mapping**: Scaling 0-1023 analog values to 0-127 and 0-63 grid values.
*   **Cumulative Buffer**: understanding that pixels added to the buffer stay there until explicitly removed.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   2 Potentiometers
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED (I2C)** | GP0/GP1 | Display output |
| **Potentiometer X** | GP26 (ADC0) | Controls Horizontal position |
| **Potentiometer Y** | GP27 (ADC1) | Controls Vertical position |

### 5. Blocks Used
*   **from Displays, drag `pico_oled_init`** (initialize display)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Math, drag `math_map`** (scale ranges)
*   **from Displays, drag `pico_oled_pixel`** (draw point)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **current_x**: The translated horizontal coordinate.
*   **current_y**: The translated vertical coordinate.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**:
    *   From **Displays**, drag `pico_oled_init`.
    *   From **Displays**, drag `pico_oled_clear` then `pico_oled_show` to start with a blank canvas.

**B. Interaction Phase (Loop)**
2.  **Create Forever Loop**: From **Loops**, drag `pico_forever`.
3.  **Process X-Axis**:
    *   Read GP26. From **Math**, map the result from [0 to 1023] into [0 to 127].
    *   **Set** variable `current_x` to this result.
4.  **Process Y-Axis**:
    *   Read GP27. From **Math**, map the result from [0 to 1023] into [0 to 63].
    *   **Set** variable `current_y` to this result.

**C. Drawing Phase**
5.  **Mark the Point**:
    *   From **Displays**, drag `pico_oled_pixel`.
    *   **Set** coordinate to (`current_x`, `current_y`).
    *   *Crucial: Notice we do NOT clear the screen here!*
6.  **Refresh Hardware**:
    *   From **Displays**, drag `pico_oled_show`.
7.  **Settle Delay**:
    *   **Wait** 0.05 seconds for smooth drawing.

### 8. Execution Flow
1.  **Input**: The user turns two knobs.
2.  **Translate**: The Pico calculates the exact pixel location matches the knob positions.
3.  **Ink**: A single pixel is turned on at the new location.
4.  **Persistence**: The old pixels from the previous loop are NOT removed.
5.  **Result**: As the user moves the knobs, a visible line "grows" on the screen, creating a drawing.

### 9. Generated Code
```python
import machine
import ssd1306
import utime

# Configure Hardware
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot_x = machine.ADC(26)
pot_y = machine.ADC(27)

# Start clean
oled.fill(0)
oled.show()

while True:
    # Read and Scale Inputs
    x_val = pot_x.read_u16()
    y_val = pot_y.read_u16()
    
    # Map 65535 range to 127 and 63
    draw_x = int((x_val / 65535) * 127)
    draw_y = int((y_val / 65535) * 63)
    
    # Draw pixel (Persistent)
    oled.pixel(draw_x, draw_y, 1)
    oled.show()
    
    utime.sleep(0.02)
```

### 10. Common Mistakes
*   **Accidental Clear**: If you put a `clear()` block inside the loop, the dot will move but won't leave a tail (Etch-a-Sketch effect lost).
*   **Integer Requirement**: Coordinates MUST be whole numbers. If your mapping returns 12.5, the code will crash. Always ensure your mapping result is an integer.

### 11. Try This Next
*   **Reset Button**: Add a button that, when pressed, clears the entire screen so you can start a new drawing.
*   **Fat Brush**: Draw a 2x2 square instead of a single 1x1 pixel for a thicker line.

---
