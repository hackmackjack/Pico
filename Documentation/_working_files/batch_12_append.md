
# BATCH 12: Animation 1 (Projects 0111-0120)

## Project 0111: Introduction to Animation

### 1. Learning Objective
Display simple text frames on an OLED screen. Learn the fundamental concept of animation as sequential image display.

### 2. Concepts Introduced
*   **OLED Display**: Small monochrome screen using I2C or SPI communication
*   **Frame**: Single still image in an animation sequence
*   **Clear and Redraw**: Animation technique of erasing then drawing next frame

### 3. Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display (128x64 pixels, I2C)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED VCC** | 3.3V | Power supply |
| **OLED GND** | GND | Ground |
| **OLED SCL** | GP1 | I2C Clock |
| **OLED SDA** | GP0 | I2C Data |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart Display, drag `pico_oled_init`** (initialize OLED)
*   **from Smart Display, drag `pico_oled_text`** (display text)
*   **from Smart Display, drag `pico_oled_clear`** (clear screen)
*   **from Smart Display, drag `pico_oled_show`** (update display)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Simple sequential display without state tracking.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED Display**:
    *   From **Smart Display**, drag `pico_oled_init`.
    *   **Set** Width -> 128, Height -> 64.
    *   **Set** I2C pins -> SDA=GP0, SCL=GP1.
    *   **Snap** at beginning of program.

**B. Main Loop Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

3.  **Frame 1: Display Text**:
    *   From **Smart Display**, drag `pico_oled_clear`.
    *   **Clear** the screen buffer.
    *   From **Smart Display**, drag `pico_oled_text`.
    *   **Set** text -> "Frame 1"
    *   **Set** position -> X=0, Y=0
    *   From **Smart Display**, drag `pico_oled_show`.
    *   **Update** display to show changes.

4.  **Hold Frame 1**:
    *   From **Time**, drag `pico_wait` -> 0.5 seconds.

5.  **Frame 2: Display Different Text**:
    *   From **Smart Display**, drag `pico_oled_clear`.
    *   From **Smart Display**, drag `pico_oled_text`.
    *   **Set** text -> "Frame 2"
    *   **Set** position -> X=0, Y=0
    *   From **Smart Display**, drag `pico_oled_show`.

6.  **Hold Frame 2**:
    *   From **Time**, drag `pico_wait` -> 0.5 seconds.

### 8. Execution Flow
1.  **Start**: Initialize OLED display via I2C.
2.  **Loop Entry**: Enter infinite animation loop.
3.  **Frame 1**: Clear buffer, write "Frame 1", update display. Wait 0.5s.
4.  **Frame 2**: Clear buffer, write "Frame 2", update display. Wait 0.5s.
5.  **Repeat**: Jump back to Frame 1, creating continuous 2-frame animation at 2 FPS.

### 9. Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Initialize I2C and OLED
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Animation loop
while True:
    # Frame 1
    oled.fill(0)
    oled.text("Frame 1", 0, 0)
    oled.show()
    time.sleep(0.5)
    
    # Frame 2
    oled.fill(0)
    oled.text("Frame 2", 0, 0)
    oled.show()
    time.sleep(0.5)
```

### 10. Common Mistakes
*   **Missing show()**: Forgetting `oled.show()` means buffer changes won't appear on screen.
*   **No Clear**: Not clearing between frames causes text overlap.
*   **Wrong I2C Address**: Some OLED modules use 0x3C, others 0x3D - check your module.

### 11. Try This Next
*   **More Frames**: Add Frame 3, Frame 4, etc. for longer animation.
*   **Position Changes**: Move text to different Y positions each frame.
*   **Countdown**: Display "3", "2", "1", "GO!" sequence.

### 12. Notes
*   This is a foundational project introducing OLED displays and frame-based animation.
*   Future projects will build on these concepts with graphics, sprites, and interactivity.

---

## Project 0112: Blinking Animation

### 1. Learning Objective
Create simple geometric animations using shapes. Learn to draw and erase graphics primitives.

### 2. Concepts Introduced
*   **Graphics Primitives**: Basic shapes (circle, line, rectangle)
*   **Two-State Animation**: Alternating between two distinct images
*   **Drawing Coordinates**: Understanding X,Y position system

### 3. Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display (128x64 pixels, I2C)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0111)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart Display, drag `pico_oled_init`** (initialize OLED)
*   **from Smart Display, drag `pico_oled_circle`** (draw circle)
*   **from Smart Display, drag `pico_oled_line`** (draw line)
*   **from Smart Display, drag `pico_oled_clear`** (clear screen)
*   **from Smart Display, drag `pico_oled_show`** (update display)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED**: Same as Project 0111.

**B. Main Loop Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

3.  **Frame 1: Eye Open (Circle)**:
    *   From **Smart Display**, drag `pico_oled_clear`.
    *   From **Smart Display**, drag `pico_oled_circle`.
    *   **Set** center X=64, Y=32 (screen center)
    *   **Set** radius=15 pixels
    *   **Set** fill=False (outline only)
    *   From **Smart Display**, drag `pico_oled_show`.

4.  **Hold Open Eye**:
    *   From **Time**, drag `pico_wait` -> 1 second.

5.  **Frame 2: Eye Closed (Horizontal Line)**:
    *   From **Smart Display**, drag `pico_oled_clear`.
    *   From **Smart Display**, drag `pico_oled_line`.
    *   **Set** start X=49, Y=32 (left edge of "lid")
    *   **Set** end X=79, Y=32 (right edge of "lid")
    *   From **Smart Display**, drag `pico_oled_show`.

6.  **Hold Closed Eye**:
    *   From **Time**, drag `pico_wait` -> 0.2 seconds (quick blink).

### 8. Execution Flow
1.  **Start**: Initialize OLED.
2.  **Open**: Draw circle (eye open), display for 1 second.
3.  **Blink**: Draw line (eye closed), display for 0.2 seconds.
4.  **Repeat**: Creates blinking effect with asymmetric timing (longer open than closed).

### 9. Generated Code
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Initialize I2C and OLED
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Blinking loop
while True:
    # Eye open (circle)
    oled.fill(0)
    oled.ellipse(64, 32, 15, 15, 1)
    oled.show()
    time.sleep(1)
    
    # Eye closed (line)
    oled.fill(0)
    oled.line(49, 32, 79, 32, 1)
    oled.show()
    time.sleep(0.2)
```

### 10. Common Mistakes
*   **Wrong Coordinates**: Circle center must account for radius to stay on screen.
*   **Line Too Short**: Make sure line spans diameter of circle for realistic blink.
*   **Equal Timing**: Eyes naturally stay open longer than closed - use asymmetric delays.

### 11. Try This Next
*   **Add Pupil**: Draw small filled circle inside larger circle for more detail.
*   **Wink Sequence**: Alternate left and right eye blinking.
*   **Variable Speed**: Use potentiometer to control blink rate.

### 12. Notes
*   Demonstrates simple 2-frame animation with geometric primitives.
*   Asymmetric timing (1s open, 0.2s closed) creates realistic blinking effect.

---
