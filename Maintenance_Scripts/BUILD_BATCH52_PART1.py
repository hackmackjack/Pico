import os

def build_batch52_part1():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0511 = """
---

#  Batch 52: Animation 3

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display a full-screen numeric countdown ("3", "2", "1") on the OLED display using screen clearing and text positioning.

### 3. Concepts Introduced
*   OLED Buffer Management (Clear, Show)
*   Text Scaling (Visual impact)
*   Frame Sequencing
*   I2C Communication

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display (SSD1306, 128x64)
*   Jumper Wires
*   Breadboard

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED VCC** | 3.3V (OUT) | Power supply |
| **OLED GND** | GND | Ground |
| **OLED SDA** | GP8 | I2C0 Data |
| **OLED SCL** | GP9 | I2C0 Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_clear`** (Clear buffer)
*   **from Display, drag `pico_oled_text`** (Draw text)
*   **from Display, drag `pico_oled_show`** (Update screen)
*   **from Time, drag `pico_wait`** (Delay)

### 7. Variables
*   **None**: This project uses hardcoded values for the numeric sequence.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**:
    *   From **Display**, **Set** `pico_oled_init` with SDA=GP8, SCL=GP9.

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Display "3"**:
    *   From **Display**, drag `pico_oled_clear`.
        *   **Snap** into loop.
    *   From **Display**, drag `pico_oled_text`.
        *   **Snap** below.
        *   Set Text to "3", X=60, Y=25.
    *   From **Display**, drag `pico_oled_show`.
        *   **Snap** below.
4.  **Wait**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 1 second.
5.  **Display "2"**:
    *   Repeat clear, text ("2"), and show blocks.
    *   Wait 1 second.
6.  **Display "1"**:
    *   Repeat clear, text ("1"), and show blocks.
    *   Wait 1 second.

### 9. Execution Flow
1.  **Start**: The Pico initializes the I2C bus and the OLED driver.
2.  **Process**: The code enters the main loop.
3.  **Output**: The screen clears, draws the number "3", and updates the pixels.
4.  **Delay**: The system pauses for 1 second so the user can read the number.
5.  **Output**: The process repeats for the numbers "2" and "1".
6.  **Repeat**: The loop jumps back to "3" instantly.

### 10. Generated Code
```python
import machine
import ssd1306
import time

# Initialize I2C and OLED
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Show 3
    oled.fill(0)
    oled.text("3", 60, 25)
    oled.show()
    time.sleep(1)
    
    # Show 2
    oled.fill(0)
    oled.text("2", 60, 25)
    oled.show()
    time.sleep(1)
    
    # Show 1
    oled.fill(0)
    oled.text("1", 60, 25)
    oled.show()
    time.sleep(1)
```

### 11. Common Mistakes
*   **Forgetting Show**: Drawing text to the buffer but not calling `show()` results in a blank screen.
*   **Buffer Overlap**: Not clearing the screen (`fill(0)`) causes numbers to draw on top of each other, creating a mess.

### 12. Try This Next
*   **Add "GO!"**: Add one more frame at the end of the countdown with the text "GO!".
*   **Move Text**: Change the X/Y coordinates to make the numbers appear in different corners.
"""

    p0512 = """
---

## 1. Project 0512: Blinking Animation

### 2. Learning Objective
Animate a simple facial expression ("Wink") by toggling between drawing a circle and a line for one eye.

### 3. Concepts Introduced
*   Primitive Shapes (Circle, Line)
*   Conditional Animation Frames
*   Persistence of Vision
*   Graphic Layout

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`** (Draw eye)
*   **from Display, drag `pico_oled_line`** (Draw wink)
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **None**: Direct sequential drawing sequence.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare Display**:
    *   From **Display**, **Set** `pico_oled_init`.

**B. Main Loop Phase**
2.  **Draw Open Face**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Draw Static Parts**: Draw a large circle for the face and a circle for the Left Eye.
    *   **Draw Right Eye (Open)**: From **Display**, drag `pico_oled_circle` (X=80, Y=25, R=5).
    *   From **Display**, drag `pico_oled_show`.
3.  **Wait**:
    *   From **Time**, wait 2 seconds.
4.  **Draw Winking Face**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Draw Static Parts**: Re-draw face and Left Eye.
    *   **Draw Right Eye (Closed)**: From **Display**, drag `pico_oled_line` (X1=75, Y1=25, X2=85, Y2=25).
    *   From **Display**, drag `pico_oled_show`.
5.  **Wait**:
    *   From **Time**, wait 0.5 seconds.

### 9. Execution Flow
1.  **Start**: The OLED is configured.
2.  **Phase 1**: Both eyes are drawn as circles, creating a "staring" look.
3.  **Phase 2**: The right eye is replaced by a horizontal line, simulating a closed eyelid.
4.  **Repeat**: The cycle repeats, giving the appearance of a person winking.

### 10. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_face():
    # Face outline
    oled.rect(30, 10, 68, 44, 1)
    # Left eye
    oled.rect(45, 20, 5, 5, 1)

while True:
    # Eye Open
    oled.fill(0)
    draw_face()
    oled.rect(78, 20, 5, 5, 1) # Right eye
    oled.show()
    time.sleep(2)
    
    # Eye Closed (Wink)
    oled.fill(0)
    draw_face()
    oled.hline(75, 22, 10, 1) # Right eye line
    oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Coordinate Math**: Getting the wink line's Y-coordinate slightly higher or lower than the original eye center makes the wink look detached.
*   **Missing Clear**: If you don't clear between frames, the wink line will simply overlap the eye circle.

### 12. Try This Next
*   **Both Eyes**: Make both eyes blink simultaneously by changing both to lines.
*   **Add Mouth**: Draw a smile using a rectangle or pixels and make it move.
"""

    p0513 = """
---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Build a digital "Etch-a-Sketch" using two potentiometers to control the X and Y coordinates of a drawing pixel.

### 3. Concepts Introduced
*   Analog-to-Digital Mapping
*   Coordinate Clipping (Screen boundaries)
*   Persistent Graphics (No auto-clear)
*   User Input Mapping

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   2x 10kΩ Potentiometers

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer 1** | GP26 (ADC0) | Horizontal Control (X) |
| **Potentiometer 2** | GP27 (ADC1) | Vertical Control (Y) |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`** (Read knob)
*   **from Math, drag `map_range`** (Convert 0-65535 to 0-127)
*   **from Display, drag `pico_oled_pixel`** (Place dot)
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **x_pos**: Integer (Current X coordinate)
*   **y_pos**: Integer (Current Y coordinate)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure ADC**: Set GP26 and GP27 as analog inputs.
2.  **Configure Display**: Initialize OLED on GP8/9. Clear screen **once** at start.

**B. Main Loop Phase**
3.  **Read Inputs**:
    *   From **Smart IO**, drag `pico_adc_read` (GP26) into `x_raw`.
    *   From **Smart IO**, drag `pico_adc_read` (GP27) into `y_raw`.
4.  **Map Coordinates**:
    *   From **Math**, set `x_pos` to map `x_raw` from range 0-65535 to 0-127.
    *   From **Math**, set `y_pos` to map `y_raw` from range 0-65535 to 0-63.
5.  **Draw**:
    *   From **Display**, drag `pico_oled_pixel`.
        *   **Snap** into loop.
        *   Set X=`x_pos`, Y=`y_pos`.
    *   From **Display**, drag `pico_oled_show`.
6.  **Loop**: Do **NOT** use a clear screen block inside the loop. This allows the line to form.

### 9. Execution Flow
1.  **Start**: Screen is cleared.
2.  **Input**: Pico reads the voltages from both knobs.
3.  **Scaling**: The high-resolution ADC value is scaled down to fit the OLED resolution.
4.  **Output**: A single pixel is turned on at the current knob position.
5.  **Persistence**: Because the screen isn't cleared, the old pixels stay lit, creating a continuous line as the knobs turn.

### 10. Generated Code
```python
import machine
import ssd1306

# Inputs
pot_x = machine.ADC(26)
pot_y = machine.ADC(27)

# Display
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear once at start
oled.fill(0)
oled.show()

while True:
    # Read and scale
    x = int(pot_x.read_u16() * 127 / 65535)
    y = int(pot_y.read_u16() * 63 / 65535)
    
    # Draw point
    oled.pixel(x, y, 1)
    oled.show()
```

### 11. Common Mistakes
*   **Resolution Mismatch**: Using the raw ADC value (65535) as a pixel coordinate will result in the dot being stuck at the bottom right corner (off-screen).
*   **Clearing Screen**: If you call `oled.fill(0)` in the loop, you will only see a single moving dot instead of a drawing.

### 12. Try This Next
*   **Clear Button**: Add a push button on GP14 that clears the screen when pressed.
*   **Thickness**: Draw a small 2x2 square instead of a single pixel for a bolder line.
"""

    p0514 = """
---

## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Animate a "Growing Circle" that expands from the center of the screen to the edges using a variable-driven loop.

### 3. Concepts Introduced
*   Iterative Animation
*   Variable Scoping
*   Frame Rate Control
*   Recursive Geometry

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (for i from ...)
*   **from Display, drag `pico_oled_circle`**
*   **from Display, drag `pico_oled_clear`**

### 7. Variables
*   **radius**: Integer (Current size of the circle)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**: Initialize on GP8/9.

**B. Main Loop Phase**
2.  **Create Expansion Loop**:
    *   From **Loops**, drag `count_with`.
    *   Set variable `radius`, range 1 to 30.
3.  **Draw Frame**:
    *   From **Display**, drag `pico_oled_clear`.
        *   **Snap** inside count loop.
    *   From **Display**, drag `pico_oled_circle`.
        *   **Snap** below.
        *   Set X=64, Y=32, R=`radius`.
    *   From **Display**, drag `pico_oled_show`.
        *   **Snap** below.
4.  **Wait**:
    *   From **Time**, wait 0.05 seconds.

### 9. Execution Flow
1.  **Start**: Screen initializes.
2.  **Iterate**: The `radius` variable increases by 1 each time the inner loop runs.
3.  **Render**: For every value of radius, the old screen is wiped and a new, larger circle is drawn.
4.  **Loop**: Once the circle reaches max size (30), it resets to 1 and starts over.

### 10. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for radius in range(1, 31):
        oled.fill(0)
        oled.circle(64, 32, radius, 1)
        oled.show()
        time.sleep(0.05)
```

### 11. Common Mistakes
*   **No Clear**: Without clearing, you get a solid white "tunnel" effect because all previous circles stay on screen.
*   **Range Error**: If the radius goes beyond 32, it might clip or wrap depending on the library version.

### 12. Try This Next
*   **Shrinking Circle**: Modify the loop to count from 30 down to 1 after it finishes expanding.
*   **Multiple Circles**: Draw three circles at once with offsets to create a "ripple" effect.
"""

    p0515 = """
---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Control a character's "Expressivity" (Mouth size) using a potentiometer, creating an interactive "Mood Eyes" interface.

### 3. Concepts Introduced
*   Human-Machine Interaction (HMI)
*   Dynamic Geometry Positioning
*   Real-time Rendering
*   Parameter Mapping

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   10kΩ Potentiometer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Expression control |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Display, drag `pico_oled_rect`** (Draw mouth)
*   **from Display, drag `pico_oled_circle`** (Draw eyes)

### 7. Variables
*   **mood_val**: Integer (Mapped ADC value)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Init OLED and ADC(26).

**B. Main Loop Phase**
2.  **Read Feeling**:
    *   Set `raw` to `pico_adc_read` (GP26).
    *   Set `mood_val` to map `raw` (0-65535) to mouth height (2 to 25).
3.  **Animate**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Draw Eyes**: Draw two static circles at top.
    *   **Draw Dynamic Mouth**:
        *   From **Display**, drag `pico_oled_rect`.
        *   Set X=44, Y=40, Width=40, Height=`mood_val`.
    *   From **Display**, drag `pico_oled_show`.

### 9. Execution Flow
1.  **Sense**: Pico measures the knob position.
2.  **Scale**: The voltage determines how wide the character's mouth opens.
3.  **Render**: The screen updates rapidly (multiple times per second).
4.  **Observe**: As the user turns the knob, the character appears to "scream" or "talk" in real-time.

### 10. Generated Code
```python
import machine
import ssd1306

pot = machine.ADC(26)
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    raw = pot.read_u16()
    # Map to mouth height (max 30)
    mouth_h = int(raw * 30 / 65535) + 2
    
    oled.fill(0)
    # Eyes
    oled.circle(44, 20, 5, 1)
    oled.circle(84, 20, 5, 1)
    # Mouth (Rectangle)
    oled.rect(44, 40, 40, mouth_h, 1)
    
    oled.show()
```

### 11. Common Mistakes
*   **Static Rendering**: Forgetting to put the `pico_adc_read` block *inside* the loop means the expression never updates.
*   **Inverted Mapping**: If turning the knob right makes the mouth smaller, swap the mapping values.

### 12. Try This Next
*   **Angry Eyes**: Add diagonal lines over the eyes that change angle based on the same pot.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0511 + p0512 + p0513 + p0514 + p0515)
    
    print("Projects 0511-0515 appended to Docs_0501_0600.md (Elite v2.0 Standard).")

if __name__ == "__main__":
    build_batch52_part1()
