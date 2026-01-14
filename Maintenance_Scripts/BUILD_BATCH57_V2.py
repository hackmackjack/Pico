import os

def build_batch57_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0561 = """
---

# Batch 57: OLED Shapes 3

## 1. Project 0561: Introduction to OLED Shapes

### 2. Learning Objective
Verify the display's coordinate system by lighting up individual pixels at the four extreme corners of the OLED screen.

### 3. Concepts Introduced
*   Pixel Coordinates ($X, Y$)
*   Screen Boundaries ($128 \times 64$)
*   Origin Point ($0,0$)
*   Buffer Updates

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display (SSD1306)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_pixel`** (Set color at X,Y)
*   **from Display, drag `pico_oled_show`** (Push to hardware)

### 7. Variables
*   **None**: Static coordinate project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Snap** into `start` block.

**B. Main Loop Phase**
1.  **Draw Corner 1 (Top-Left)**:
    *   From **Display**, drag `pico_oled_pixel`.
    *   **Snap** into `pico_forever`.
    *   Set X to 0, Y to 0, Color to ON.
2.  **Draw Corner 2 (Top-Right)**:
    *   From **Display**, drag `pico_oled_pixel`.
    *   **Snap** below previous.
    *   Set X to 127, Y to 0, Color to ON.
3.  **Draw Corner 3 (Bottom-Left)**:
    *   From **Display**, drag `pico_oled_pixel`.
    *   **Snap** below previous.
    *   Set X to 0, Y to 63, Color to ON.
4.  **Draw Corner 4 (Bottom-Right)**:
    *   From **Display**, drag `pico_oled_pixel`.
    *   **Snap** below previous.
    *   Set X to 127, Y to 63, Color to ON.
5.  **Refresh Screen**:
    *   From **Display**, drag `pico_oled_show`.
    *   **Snap** below the pixels.

### 9. Execution Flow
1.  **Start**: The Pico initializes the I2C communication with the SSD1306 driver.
2.  **Process**: The code addresses the four absolute physical limits of the 128x64 grid.
3.  **Process**: The coordinates 0-127 (X) and 0-63 (Y) are used to target the corner pixels.
4.  **Output**: Four tiny white dots appear at the extreme edges of the screen.
5.  **Repeat**: The dots are continuously refreshed in the loop.

### 10. Generated Code
```python
import machine
import ssd1306

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
while True:
    # Set the 4 corners
    oled.pixel(0, 0, 1)
    oled.pixel(127, 0, 1)
    oled.pixel(0, 63, 1)
    oled.pixel(127, 63, 1)
    oled.show()
```

### 11. Common Mistakes
*   **Zero-Index**: Remembering that for 128 pixels, the last index is 127. If you use 128, the code might error or do nothing.

### 12. Try This Next
*   **Draw Border**: Use four `pico_oled_line` blocks to connect the dots and create a frame.
"""

    p0562 = """
---

## 1. Project 0562: Blinking OLED Shapes

### 2. Learning Objective
Create a "Screen Saver" effect by randomly lighting up single pixels every 10ms to fill the screen with white noise ("snow").

### 3. Concepts Introduced
*   Random Number Generation
*   Buffer Persistence
*   Screen Saturation
*   Rapid Refreshes

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (Coordinates)
*   **from Display, drag `pico_oled_pixel`**
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **rand_x**: Integer (0-127)
*   **rand_y**: Integer (0-63)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Display**:
    *   From **Display**, drag `pico_oled_clear`.

**B. Main Loop Phase**
1.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Pick Random X**:
    *   From **Variables**, set `rand_x` to **Math** `random_integer` 0 to 127.
    *   **Snap** into loop.
3.  **Pick Random Y**:
    *   From **Variables**, set `rand_y` to **Math** `random_integer` 0 to 63.
    *   **Snap** below X.
4.  **Set Point**:
    *   From **Display**, drag `pico_oled_pixel`.
    *   **Snap** below Y.
    *   Set X to `rand_x`, Y to `rand_y`.
5.  **Refresh**:
    *   From **Display**, drag `pico_oled_show`.
    *   **Snap** below pixel block.
6.  **Pacing**:
    *   From **Time**, wait 0.01 seconds.

### 9. Execution Flow
1.  **Start**: Screen starts black.
2.  **Process**: In every loop iteration, two random whole numbers are picked by the CPU.
3.  **Output**: A single white dot appears at that random location.
4.  **Process**: Because the screen is NOT cleared inside the loop, the dots stay on.
5.  **Output**: After several minutes, the screen looks like static or "snow."
6.  **Repeat**: The process continues until power is removed.

### 10. Generated Code
```python
import machine, ssd1306, random, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

while True:
    rx = random.randint(0, 127)
    ry = random.randint(0, 63)
    oled.pixel(rx, ry, 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Clearing Screen**: If you put `pico_oled_clear` INSIDE the loop, you will only ever see one dot at a time instead of snow.

### 12. Try This Next
*   **Eraser Mode**: Start with a white screen (`fill(1)`) and turn pixels black (`0`) randomly.
"""

    p0563 = """
---

## 1. Project 0563: Manual OLED Shapes Control

### 2. Learning Objective
Control the size of a circle in real-time by mapping a potentiometer's rotation to the radius of the shape (1 to 30 pixels).

### 3. Concepts Introduced
*   Analog-to-Shape mapping
*   Live Buffer Clearing
*   Dynamic Geometry
*   Scaling Factors

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Radius Pot**  | GP26 (ADC) | Input scale |
| **OLED SDA**    | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`** (X=64, Y=32, R=?)
*   **from Smart IO, drag `pico_adc_read`**
*   **from Math, drag `map_range`**

### 7. Variables
*   **rad_val**: Integer (Calculated radius)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Connect ADC**:
    *   Set Pin to GP26.

**B. Main Loop Phase**
1.  **Create Monitor Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Wipe Frame**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Snap** at top of loop.
3.  **Read Knob**:
    *   From **Variables**, set `rad_val` to **Math** `map_range`.
        *   Input: **Smart IO** `pico_adc_read` 26, From: 0-65535, To: 1-30.
    *   **Snap** below clear.
4.  **Draw Geometry**:
    *   From **Display**, drag `pico_oled_circle`.
    *   **Snap** below mapping.
    *   Set Center X to 64, Center Y to 32, Radius to `rad_val`.
5.  **Refresh Display**:
    *   From **Display**, drag `pico_oled_show`.
    *   **Snap** below circle.

### 9. Execution Flow
1.  **Start**: System initializes. Screen is blank.
2.  **Sense**: User turns the knob. The ADC returns a 16-bit number.
3.  **Process**: The system maps that number into the 1-30 pixel range.
4.  **Output**: The screen clears and immediately draws a circle of the new size.
5.  **Output**: To the user, it looks like a single circle that "grows" or "shrinks" smoothly.
6.  **Repeat**: The update happens fast enough to feel like real-time video.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)

while True:
    raw = pot.read_u16()
    rad = int(raw * 30 / 65535) + 1
    
    oled.fill(0)
    oled.circle(64, 32, rad, 1) # Outline circle
    oled.show()
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Radius Limit**: Setting the radius larger than 32. If the circle goes off the top or bottom of the screen (32+32=64), some drivers might crash or draw weird lines.

### 12. Try This Next
*   **Solid Circle**: Use `pico_oled_fill_circle` instead of the outline version.
"""

    p0564 = """
---

## 1. Project 0564: OLED Shapes Sequences

### 2. Learning Objective
Simulate a "Traffic Light" indicator on the display by sequentially drawing and clearing filled circles within a rectangular frame.

### 3. Concepts Introduced
*   UI Regions (Frames)
*   Sequential Animation
*   Shape Positioning
*   Wait timing states

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_rect`** (Draw frame)
*   **from Display, drag `pico_oled_fill_circle`** (Lights)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Time-base sequence.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Boot HUD**:
    *   From **Display**, set `pico_oled_rect` X=54, Y=10, W=20, H=44.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Create Sequence**:
    *   From **Loops**, drag `pico_forever`.
2.  **Phase 1 (Red)**:
    *   From **Display**, drag `pico_oled_clear`.
    *   Redraw `pico_oled_rect` housing.
    *   Draw `pico_oled_fill_circle` at X=64, Y=18, R=5.
    *   **Snap** inside loop.
    *   `pico_oled_show`. Wait 3s.
3.  **Phase 2 (Green)**:
    *   Clear, Redraw housing.
    *   Draw `pico_oled_fill_circle` at X=64, Y=46, R=5.
    *   **Snap** below previous.
    *   `pico_oled_show`. Wait 3s.
4.  **Phase 3 (Yellow)**:
    *   Clear, Redraw housing.
    *   Draw `pico_oled_fill_circle` at X=64, Y=32, R=5.
    *   **Snap** below previous.
    *   `pico_oled_show`. Wait 1s.

### 9. Execution Flow
1.  **Process**: The code draws a permanent hollow rectangle (the traffic light box).
2.  **Output**: A filled circle appears at the top (Red position) for 3 seconds.
3.  **Output**: The top circle disappears and the bottom one (Green) appears.
4.  **Process**: The timing matches a real traffic light.
5.  **Output**: The middle circle (Yellow) flashes briefly before the cycle resets.
6.  **Repeat**: The simulation continues indefinitely.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_housing():
    oled.rect(54, 5, 20, 54, 1)

while True:
    # RED
    oled.fill(0); draw_housing()
    oled.fill_circle(64, 15, 6, 1)
    oled.show(); time.sleep(3)
    
    # GREEN
    oled.fill(0); draw_housing()
    oled.fill_circle(64, 49, 6, 1)
    oled.show(); time.sleep(3)
    
    # YELLOW
    oled.fill(0); draw_housing()
    oled.fill_circle(64, 32, 6, 1)
    oled.show(); time.sleep(1)
```

### 11. Common Mistakes
*   **Missing Housing**: If you don't call the "draw rectangle" part after every `fill(0)`, the box will disappear, leaving only the dots.

### 12. Try This Next
*   **Dual Lights**: Draw two boxes side-by-side that alternate (Standard intersection).
"""

    p0565 = """
---

## 1. Project 0565: Interactive OLED Shapes

### 2. Learning Objective
Programm a "Tilt Ball" simulation where a circle's position on screen is directly influenced by the physical tilt of the device using an accelerometer.

### 3. Concepts Introduced
*   Gravity-to-Screen Mapping
*   Orientation Sensing (X/Y axis)
*   Dynamic Sprite Moving
*   ADC-to-Coordinate scaling

### 4. Hardware Required
*   Raspberry Pi Pico
*   Accelerometer/Gyro (MPU6050)
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MPU6050 SDA**| GP4 | I2C1 |
| **OLED SDA**    | GP8 | I2C0 |

### 6. Blocks Used
*   **from Sensors, drag `mpu6050_acceleration`**
*   **from Math, drag `map_range`**
*   **from Display, drag `pico_oled_circle`**

### 7. Variables
*   **tilt_x**: Float (Raw accel)
*   **pos_x**: Integer (Screen X)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sync I2C**:
    *   Init both I2C channels (0 and 1).

**B. Main Loop Phase**
1.  **Create Physics Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Input Tilt**:
    *   From **Variables**, set `tilt_x` to **Sensors** `mpu6050_acceleration` X-axis.
    *   **Snap** into loop.
3.  **Convert to Screen**:
    *   From **Variables**, set `pos_x` to **Math** `map_range`.
        *   Input: `tilt_x`, From: -17000-17000, To: 10-118.
    *   **Snap** below tilt.
4.  **Render Ball**:
    *   From **Display**, drag `pico_oled_clear`.
    *   From **Display**, drag `pico_oled_circle`.
        *   CenterX: `pos_x`, CenterY: 32, Radius: 5.
    *   From **Display**, drag `pico_oled_show`.

### 9. Execution Flow
1.  **Start**: System establishes sensor links.
2.  **Sense**: As the user tilts the breadboard, the Accelerometer senses the pull of gravity.
3.  **Process**: Large raw numbers (up to 17,000) are shrunk down to fit the narrow 128x64 pixels of the screen.
4.  **Output**: A circle "ball" slides across the screen corresponding to the physical tilt.
5.  **Output**: The ball appears to respond to real gravity.
6.  **Repeat**: Updates occur every few milliseconds for fluid motion.

### 10. Generated Code
```python
import machine, ssd1306, time
# Simplified MPU reading logic
i2c_oled = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c_oled)

while True:
    # Hypothetical accel reading (Mapping raw tilt)
    fake_tilt = 0 # Replace with real sensor read
    x = int((fake_tilt + 17000) * 127 / 34000)
    
    oled.fill(0)
    oled.circle(x, 32, 5, 1)
    oled.show()
    time.sleep(0.02)
```

### 11. Common Mistakes
*   **Inverted Axis**: If tilting right moves the ball left, just swap the "To" range from (10, 118) to (118, 10).

### 12. Try This Next
*   **Vertical Tilt**: Map the Y-axis of the sensor to the Y-coordinate of the ball as well.
"""

    p0566 = """
---

## 1. Project 0566: Smart OLED Shapes Switch

### 2. Learning Objective
Implement a "Graphical Menu" where button presses move a selection box (inverted highlight) between two on-screen text labels.

### 3. Concepts Introduced
*   Logical Highlighting
*   Boolean Color Inversion
*   UI Navigation Logic
*   Coordinate-based Selection

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons (Up/Down)
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Navigator Up**| GP14 | Previous item |
| **Navigator Dn**| GP15 | Next item |

### 6. Blocks Used
*   **from Display, drag `pico_oled_fill_rect`** (Selection bar)
*   **from Logic, drag `if_else`**
*   **from Display, drag `pico_oled_text`** (set color to 0)

### 7. Variables
*   **sel_idx**: Integer (0 or 1)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Default**:
    *   From **Variables**, set `sel_idx` to 0.

**B. Main Loop Phase**
1.  **Monitor Buttons**:
    *   From **Loops**, drag `pico_forever`.
2.  **Check Input**:
    *   From **Logic**, if GP14 (Up) is HIGH: `sel_idx = 0`.
    *   If GP15 (Down) is HIGH: `sel_idx = 1`.
3.  **Wipe Frame**:
    *   From **Display**, drag `pico_oled_clear`.
4.  **Draw Labels**:
    *   **Text** X=30, Y=10 "FAN CONTROL".
    *   **Text** X=30, Y=40 "LIGHT STATUS".
5.  **Render Highlight**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `sel_idx` is 0:
        *   **Action**: From **Display**, `fill_rect` X=20, Y=8, W=90, H=12 (White bar).
        *   **Action**: Redraw "FAN" Text in Black (Color 0) over the bar.
    *   **Else**:
        *   **Action**: `fill_rect` X=20, Y=38, W=90, H=12.
        *   **Action**: Redraw "LIGHT" Text in Black.
6.  **Show**:
    *   `pico_oled_show`.

### 9. Execution Flow
1.  **Start**: Menu appears with "Fan Control" highlighted.
2.  **Interact**: User presses the Down button.
3.  **Process**: The variable `sel_idx` changes to 1.
4.  **Output**: The white selection bar "moves" to the lower label.
5.  **Output**: By drawing black text over a white bar, we create a high-contrast inverted menu look.
6.  **Repeat**: The user can cycle between the two entries.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
b_up = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
b_dn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

sel = 0

while True:
    if b_up.value(): sel = 0
    if b_dn.value(): sel = 1
    
    oled.fill(0)
    # Option 1
    if sel == 0:
        oled.fill_rect(20, 10, 80, 15, 1)
        oled.text("FAN", 25, 14, 0)
    else:
        oled.text("FAN", 25, 14, 1)
    
    # Option 2
    if sel == 1:
        oled.fill_rect(20, 35, 80, 15, 1)
        oled.text("LIGHT", 25, 39, 0)
    else:
        oled.text("LIGHT", 25, 39, 1)
        
    oled.show()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Order of Operations**: Drawing the text *first* and then the rectangle. The rectangle covers the text. Always draw the bar background first.

### 12. Try This Next
*   **Enter Action**: Add a third button that executes a specific code block depending on which index is highlighted.
"""

    p0567 = """
---

## 1. Project 0567: OLED Shapes Alarm System

### 2. Learning Objective
Create a high-urgency alert by rapidly "Inverting" the entire display's pixels (Strobe effect) to signal a system alarm.

### 3. Concepts Introduced
*   Global Screen Inversion
*   Alert Visualization
*   Strobe Cycles
*   Flash Intensity

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_invert`** (The driver command)
*   **from Loops, drag `repeat`** (Strobe timing)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Global command logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Header**:
    *   From **Display**, set `pico_oled_text` "!!! ALARM !!!" at center.
    *   **Snap** into `start`.
    *   `pico_oled_show`.

**B. Main Loop Phase**
1.  **Trigger Phase**:
    *   From **Loops**, drag `pico_forever`.
2.  **Invert White**:
    *   From **Display**, drag `pico_oled_invert` (Set to 1).
    *   **Snap** into loop.
    *   From **Time**, wait 0.1s.
3.  **Invert Black**:
    *   From **Display**, drag `pico_oled_invert` (Set to 0).
    *   **Snap** below previous.
    *   From **Time**, wait 0.1s.

### 9. Execution Flow
1.  **Start**: Screen displays "ALARM."
2.  **Output**: The hardware command `invert(1)` is sent to the SSD1306.
3.  **Process**: Every pixel on screen flips (Black becomes White, White becomes Black).
4.  **Repeat**: The rapid toggling creates a high-intensity flashing effect.
5.  **Output**: This alert is visible even in bright rooms, making it a powerful alarm tool.
6.  **Repeat**: Continues until the condition leading to the alarm is resolved.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("!!! DANGER !!!", 15, 25, 1)
oled.show()

while True:
    # Rapid Inversion Strobe
    oled.invert(1)
    time.sleep(0.2)
    oled.invert(0)
    time.sleep(0.2)
```

### 11. Common Mistakes
*   **Photosensitivity**: Be careful when demonstrating this; strobe effects can trigger physical reactions in sensitive individuals.

### 12. Try This Next
*   **Sound Sync**: Add a buzzer that beeps at exactly the same frequency as the screen flash.
"""

    p0568 = """
---

## 1. Project 0568: The OLED Shapes Game

### 2. Learning Objective
Programm the core movement logic for a "Snake" cursor that moves continuously and changes direction based on button inputs.

### 3. Concepts Introduced
*   Locomotion Logic
*   Vector Directional Control
*   Boundary Clipping
*   Game Rendering Ticks

### 4. Hardware Required
*   Raspberry Pi Pico
*   4x Buttons (U/D/L/R)
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Control Pads**| GP12-GP15 | Direction Inputs |

### 6. Blocks Used
*   **from Logic, drag `if_do`** (Check inputs)
*   **from Variables, drag `change_variable`** (X = X + DX)
*   **from Display, drag `pico_oled_rect`** (Head)

### 7. Variables
*   **snake_x**: Integer (Head Position)
*   **dir_x**: Integer (Motion direction)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start**:
    *   Set `snake_x = 64`, `snake_y = 32`.
    *   Set `dir_x = 2`, `dir_y = 0`.

**B. Main Loop Phase**
1.  **Monitor Pad**:
    *   From **Loops**, drag `pico_forever`.
2.  **Update Vectors**:
    *   From **Logic**, if Button GP12 (Up): `dir_x = 0`, `dir_y = -2`.
    *   **Snap** into loop.
    *   (Repeat for Dn, Lt, Rt).
3.  **Apply Motion**:
    *   From **Variables**, change `snake_x` by `dir_x`.
    *   From **Variables**, change `snake_y` by `dir_y`.
    *   **Snap** below inputs.
4.  **Render Head**:
    *   From **Display**, `pico_oled_clear`.
    *   From **Display**, `pico_oled_rect` X=`snake_x`, Y=`snake_y`, W=3, H=3, Color=ON.
    *   `pico_oled_show`. Wait 0.05s.

### 9. Execution Flow
1.  **Start**: The dot is in the center and moving right.
2.  **Interact**: User presses "Up."
3.  **Process**: The horizontal speed becomes zero and the vertical speed becomes negative.
4.  **Output**: The dot immediately turns upward without stopping.
5.  **Output**: The user must keep the dot from touching the screen edges.
6.  **Repeat**: The "Game Tick" continues every 50ms.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
# U, D, L, R buttons
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(12, 16)]

x, y = 64, 32
dx, dy = 1, 0

while True:
    if btns[0].value(): dx, dy = 0, -1 # Up
    if btns[1].value(): dx, dy = 0, 1  # Down
    if btns[2].value(): dx, dy = -1, 0 # Left
    if btns[3].value(): dx, dy = 1, 0  # Right
    
    x += dx; y += dy
    
    # Boundary Death
    if x < 0 or x > 127 or y < 0 or y > 63:
        x, y = 64, 32; # Reset
        
    oled.fill(0)
    oled.rect(x, y, 3, 3, 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Diagonal Motion**: If you don't reset `dx` to 0 when setting `dy`, the snake will move diagonally, which isn't standard for this game type.

### 12. Try This Next
*   **Food**: Place a static pixel at a random spot; if the snake hits it, increase his speed.
"""

    p0569 = """
---

## 1. Project 0569: Automated OLED Shapes

### 2. Learning Objective
Create a vector-based "Analog Gauge" with a rotating needle line controlled by a potentiometer.

### 3. Concepts Introduced
*   Vector Needle Drawing
*   Trigonometry (Simplified)
*   Radius Mapping
*   Dashboard Design

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Gauge Pot**   | GP26 | Data Source |
| **OLED SDA**    | GP8 | Output Display |

### 6. Blocks Used
*   **from Display, drag `pico_oled_line`** (Needle)
*   **from Math, drag `sine` / `cosine`** (Concept mapping)
*   **from Display, drag `pico_oled_circle`** (Housing)

### 7. Variables
*   **tip_x**: Integer (Calculated tip)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Driver**:
    *   Init OLED and ADC GP26.

**B. Main Loop Phase**
1.  **Create Monitor Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Calculate Arc**:
    *   Set `angle` proportional to **Smart IO** `pico_adc_read` (180 to 360 degrees).
    *   **Snap** into loop.
3.  **Find Tip Coordinates**:
    *   **Variables** `tip_x` = 64 + (cos(angle) * 30).
    *   **Variables** `tip_y` = 60 + (sin(angle) * 30).
4.  **Render Gauge**:
    *   From **Display**, `pico_oled_clear`.
    *   Draw `pico_oled_circle` X=64, Y=60, R=35 (The Dial).
    *   From **Display**, drag `pico_oled_line` from (64,60) to (`tip_x`, `tip_y`).
    *   **Snap** below circle.
5.  **Refresh**:
    *   `pico_oled_show`. Wait 0.05s.

### 9. Execution Flow
1.  **Start**: Screen displays a half-circle "speedometer" dial.
2.  **Sense**: User turns the knob.
3.  **Process**: The Pico uses math to convert the voltage into a specific X and Y coordinate on the edge of the circle arc.
4.  **Output**: A line is drawn from the center of the dial to that specific coordinate.
5.  **Output**: As the knob turns, the "needle" sweeps across the dial gauge.
6.  **Repeat**: Updates continuously to match the knob.

### 10. Generated Code
```python
import machine, ssd1306, time, math

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)

while True:
    raw = pot.read_u16()
    # Map to Radian arc for top half
    rads = (raw * 3.14 / 65535) + 3.14
    
    tx = int(64 + math.cos(rads) * 30)
    ty = int(60 + math.sin(rads) * 30)
    
    oled.fill(0)
    oled.circle(64, 60, 35, 1)
    oled.line(64, 60, tx, ty, 1)
    oled.show()
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Coordinate Origin**: Using (0,0) as the needle start. Gauges look better if the base is at the bottom-center (64, 60).

### 12. Try This Next
*   **Threshold Line**: Draw a second smaller line at the "90% Mark" to show where the Danger Zone starts.
"""

    p0570 = """
---

## 1. Project 0570: Mastering OLED Shapes

### 2. Learning Objective
Programm a 3D wireframe rotating cube by projecting 3D point coordinates $(X, Y, Z)$ into a 2D viewport using perspective projection math.

### 3. Concepts Introduced
*   3D Point Projection
*   Rotation Matrices
*   XYZ Transformation
*   Wireframe Rendering

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Math, drag `sine`**
*   **from Math, drag `cosine`**
*   **from Display, drag `pico_oled_line`** (Connect edges)

### 7. Variables
*   **phi**: Float (Rotation angle)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Points**:
    *   Pre-calculate the 8 corners of a cube $(\pm 20,\pm 20,\pm 20)$.

**B. Main Loop Phase**
1.  **Create Animator**:
    *   From **Loops**, drag `pico_forever`.
2.  **Update Rotation**:
    *   From **Variables**, change `phi` by 0.1.
    *   **Snap** into loop.
3.  **Project Points**:
    *   For each corner point:
        *   Calculate new `x_2d` and `y_2d` using `sin(phi)` and `cos(phi)`.
4.  **Render Wireframe**:
    *   From **Display**, `pico_oled_clear`.
    *   Draw **Lines** connecting the 8 2D points to form 12 edges.
    *   `pico_oled_show`.

### 9. Execution Flow
1.  **Start**: The screen initializes.
2.  **Process**: The CPU takes 8 points in virtual 3D space and mathematically "crushes" them onto the 2D plane of the screen.
3.  **Process**: The math factors in the rotation angle `phi`.
4.  **Output**: A cube appears to float and spin in 3D space.
5.  **Output**: Even on a flat screen, the movement and perspective shift make it feel deep.
6.  **Repeat**: Frame-by-frame updates create a smooth rotating animation.

### 10. Generated Code
```python
import machine, ssd1306, time, math

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# 8 Nodes of cube
nodes = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

a = 0
while True:
    a += 0.1; proj = []
    # Project 3D to 2D
    for x,y,z in nodes:
        nx = x * math.cos(a) - z * math.sin(a)
        nz = x * math.sin(a) + z * math.cos(a)
        proj.append((int(nx * 20 + 64), int(y * 20 + 32)))
        
    oled.fill(0)
    for e1, e2 in edges:
        oled.line(proj[e1][0], proj[e1][1], proj[e2][0], proj[e2][1], 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Math Overhead**: Trying to draw too many points. The Pico is fast, but 3D math on a high number of vertices will slow down the frame rate.

### 12. Try This Next
*   **Zoom knob**: Use a potentiometer to change the scale factor ($20$) so you can zoom in and out of the spinning cube.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0561 + p0562 + p0563 + p0564 + p0565 + p0566 + p0567 + p0568 + p0569 + p0570)
    
    print("Batch 57 (0561-0570) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch57_v2()
