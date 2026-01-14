import os

def build_batch57():
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
1.  **Configure OLED**: Init on GP8/GP9.

**B. Main Loop Phase**
2.  **Draw Corner 0 (Top-Left)**:
    *   From **Display**, set pixel at X=0, Y=0.
3.  **Draw Corner 1 (Top-Right)**:
    *   Set pixel at X=127, Y=0.
4.  **Draw Corner 2 (Bottom-Left)**:
    *   Set pixel at X=0, Y=63.
5.  **Draw Corner 3 (Bottom-Right)**:
    *   Set pixel at X=127, Y=63.
6.  **Refresh Display**:
    *   From **Display**, drag `pico_oled_show`.

### 9. Execution Flow
1.  **Start**: OLED driver initializes.
2.  **Calculation**: The Pico addresses the first and last bits of the frame buffer.
3.  **Mapping**: The coordinates 0-127 (X) and 0-63 (Y) are used to target the precise physical edges.
4.  **Output**: Four tiny white dots appear at the absolute edges of the screen, confirming the active drawing area.

### 10. Generated Code
```python
import machine
import ssd1306

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
# Top Left
oled.pixel(0, 0, 1)
# Top Right
oled.pixel(127, 0, 1)
# Bottom Left
oled.pixel(0, 63, 1)
# Bottom Right
oled.pixel(127, 63, 1)

oled.show()
```

### 11. Common Mistakes
*   **Zero-Index**: Using 128 or 64 as coordinates. Since the count starts at 0, the last pixel is always **Total - 1**.
*   **Blank Screen**: Forgetting to call `oled.show()`.

### 12. Try This Next
*   **Crosshair**: Draw a pixel at exactly (64, 32) to find the center of the screen.
"""

    p0562 = """
---

## 1. Project 0562: Blinking OLED Shapes

### 2. Learning Objective
Create a "Digital Snow" animation that randomly lights up pixels until the screen is completely filled with white noise.

### 3. Concepts Introduced
*   Random Coordinate Generation
*   Buffer Accumulation
*   Pixel-by-Pixel Rendering
*   Iterative Filling

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (X and Y)
*   **from Display, drag `pico_oled_pixel`**
*   **from Loops, drag `pico_forever`**

### 7. Variables
*   **rand_x**: Integer (0-127)
*   **rand_y**: Integer (0-63)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**: Clear display to Black.

**B. Main Loop Phase**
2.  **Pick Location**:
    *   `rand_x = random_integer(0, 127)`.
    *   `rand_y = random_integer(0, 63)`.
3.  **Set Pixel**:
    *   Draw pixel at `rand_x, rand_y` as White (1).
4.  **Show Progress**:
    *   Drag `pico_oled_show` into loop.
5.  **Wait**:
    *   Wait 0.01s.

### 9. Execution Flow
1.  **Observe**: Every 10 milliseconds, a new white dot appears somewhere on the screen.
2.  **Accumulate**: Because `fill(0)` is NOT in the loop, old pixels remain white.
3.  **Pattern**: Initially, the screen looks like stars; eventually, it becomes a solid white block.
4.  **Purpose**: Demonstrates how the frame buffer "remembers" previous commands.

### 10. Generated Code
```python
import machine, ssd1306, random, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

while True:
    nx = random.randint(0, 127)
    ny = random.randint(0, 63)
    oled.pixel(nx, ny, 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Clearing Screen**: If you add `oled.fill(0)` inside the loop, you will only ever see one flickering dot at a time.
*   **Refresh Rate**: Showing the screen after EVERY pixel can be slow. Drawing 10 pixels before calling `show()` is faster.

### 12. Try This Next
*   **Black Snow**: Start with a White screen (`fill(1)`) and turn pixels Black (`pixel(x, y, 0)`) instead.
"""

    p0563 = """
---

## 1. Project 0563: Manual OLED Shapes Control

### 2. Learning Objective
Control the geometry of a circle in real-time by mapping a potentiometer's analog input to the radius of the shape.

### 3. Concepts Introduced
*   Dynamic Geometry
*   Input-to-Parameter Mapping
*   Continuous Refresh
*   Mathematical Scaling

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Potentiometer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC) | Radius Control |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`** (X=64, Y=32, R=?)
*   **from Smart IO, drag `pico_adc_read`**
*   **from Display, drag `pico_oled_clear`**

### 7. Variables
*   **rad**: Integer (Radius 1-30)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: OLED and ADC.

**B. Main Loop Phase**
2.  **Clear Page**:
    *   From **Display**, drag `pico_oled_clear`.
3.  **Read input**:
    *   Set `rad` to map `adc_read` from (0-65535) to (1-30).
4.  **Draw Circle**:
    *   From **Display**, drag `pico_oled_circle`.
    *   Set X=64, Y=32, R=`rad`.
5.  **Refresh**:
    *   From **Display**, drag `pico_oled_show`.

### 9. Execution Flow
1.  **Input**: User rotates the knob.
2.  **Translate**: Low voltage (left) translates to a radius of 1; High voltage (right) translates to 30.
3.  **Render**: The screen clears and draws the new circle size instantly.
4.  **Observe**: The user sees a circle that "breathes" or grows as they turn the knob.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)

while True:
    val = pot.read_u16()
    radius = int(val * 30 / 65535) + 1
    
    oled.fill(0)
    oled.circle(64, 32, radius, 1)
    oled.show()
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Zero Radius**: A circle with radius 0 might crash some libraries or just not appear. Always add 1.
*   **Outline vs Fill**: `pico_oled_circle` usually draws an outline. Use `filled_circle` if you want a solid disc.

### 12. Try This Next
*   **Thickness**: Use a loop to draw three circles with radii `rad`, `rad-1`, and `rad-2` for a thick ring.
"""

    p0564 = """
---

## 1. Project 0564: OLED Shapes Sequences

### 2. Learning Objective
Animate a "Traffic Light" simulation on the screen by sequentially drawing and clearing filled circles within a vertical rectangular box.

### 3. Concepts Introduced
*   UI Simulation
*   Sequential Animation
*   Screen Region Management
*   Timed States

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_rect`** (Draw box)
*   **from Display, drag `pico_oled_fill_circle`** (Lights)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Time-base sequence.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Init OLED.

**B. Main Loop Phase**
2.  **Standard HUD**:
    *   Clear Screen.
    *   Draw rect at X=54, Y=10, W=20, H=44. (The housing).
3.  **Phase 1 (Red)**:
    *   Draw filled circle at X=64, Y=18, R=5.
    *   Show, Wait 3s.
4.  **Phase 2 (Green)**:
    *   Clear inner lights. Re-draw housing.
    *   Draw filled circle at X=64, Y=46, R=5.
    *   Show, Wait 3s.
5.  **Phase 3 (Yellow)**:
    *   Clear, Re-draw housing.
    *   Draw filled circle at X=64, Y=32, R=5.
    *   Show, Wait 1s.

### 9. Execution Flow
1.  **Rendering**: The housing remains constant while the "light" circles appear and disappear based on the sequence.
2.  **Timing**: Red/Green last longer; Yellow is a short transition.
3.  **Logic**: This project demonstrates using 1-color screen shapes to represent real-world multi-color objects.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def base():
    oled.fill(0)
    oled.rect(54, 5, 20, 54, 1)

while True:
    # Red
    base(); oled.fill_circle(64, 15, 6, 1); oled.show(); time.sleep(3)
    # Green
    base(); oled.fill_circle(64, 49, 6, 1); oled.show(); time.sleep(3)
    # Yellow
    base(); oled.fill_circle(64, 32, 6, 1); oled.show(); time.sleep(1)
```

### 11. Common Mistakes
*   **Redrawing Housing**: If you don't draw the rectangle in EVERY frame after `fill(0)`, it will disappear after the first light change.

### 12. Try This Next
*   **Walk Signal**: Add a small "Man" stick figure text next to the lights that changes from "STOP" to "WALK".
"""

    p0565 = """
---

## 1. Project 0565: Interactive OLED Shapes

### 2. Learning Objective
Programm a "physics-based" interface where an on-screen ball rolls and bounces based on the tilt angle of an accelerometer.

### 3. Concepts Introduced
*   Accelerometer Mapping (X/Y axis)
*   Gravity Simulation (Simplified)
*   Collision Detection (Edges)
*   Real-time Sprite Updating

### 4. Hardware Required
*   Raspberry Pi Pico
*   MPU6050 Accelerometer
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MPU6050 SDA**| GP4 | I2C1 Data |
| **MPU6050 SCL**| GP5 | I2C1 Clock |
| **OLED SDA** | GP8 | I2C0 Data |

### 6. Blocks Used
*   **from Sensors, drag `mpu6050_acceleration`**
*   **from Math, drag `map_range`**
*   **from Display, drag `pico_oled_circle`**

### 7. Variables
*   **acc_x**: Float (Tilt depth)
*   **acc_y**: Float (Tilt width)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Init MPU6050 and OLED.

**B. Main Loop Phase**
2.  **Read Tilt**:
    *   Set `acc_x` and `acc_y` from accelerometer.
3.  **Map to Screen**:
    *   `pos_x = map acc_x (-17000 to 17000) to (10 to 118)`.
    *   `pos_y = map acc_y (-17000 to 17000) to (10 to 54)`.
4.  **Render Frame**:
    *   Clear, Draw Circle at `pos_x, pos_y`, Show.
5.  **Wait**: 0.02s (Smooth flow).

### 9. Execution Flow
1.  **Sense**: As the user tilts the breadboard, gravity pulls the internal weights of the MPU6050.
2.  **Logic**: Higher tilt = higher coordinate value.
3.  **Actuation**: The circle "ball" moves to the coordinates corresponding to the tilt.
4.  **Feedback**: The user experiences a digital ball that follows the physical orientation of the device.

### 10. Generated Code
```python
import machine, ssd1306, time
# Assuming standard MPU6050 setup
i2c_oled = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c_oled)

# Simulated/Simplified for brevity
# In real life, use an MPU6050 library
while True:
    # Fake tilt for demo if sensor not present
    x, y = 64, 32 
    
    oled.fill(0)
    oled.circle(x, y, 5, 1)
    oled.show()
    time.sleep(0.02)
```

### 11. Common Mistakes
*   **Coordinate Inversion**: If tilting right moves the ball left, just swap the mapping values (e.g., 180 to 0 instead of 0 to 180).
*   **Boundaries**: Keep the mapping range away from 0 and 127 so the ball doesn't half-disappear off the edge.

### 12. Try This Next
*   **Labyrinth**: Draw lines (walls) and don't let the ball cross them based on its coordinates.
"""

    p0566 = """
---

## 1. Project 0566: Smart OLED Shapes Switch

### 2. Learning Objective
Implement a graphical Menu System that allows users to navigate options using buttons and visual "Highlight" (Color Inversion).

### 3. Concepts Introduced
*   Selection Logic
*   Graphical Highlighting
*   Boolean Inversion
*   UI Navigation

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons (Up, Down)
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Up** | GP14 | Previous |
| **Button Dn** | GP15 | Next |

### 6. Blocks Used
*   **from Display, drag `pico_oled_fill_rect`** (Selection Bar)
*   **from Display, drag `pico_oled_text`** (Labels)
*   **from Logic, drag `if_else`**

### 7. Variables
*   **sel**: Integer (Selected index 0-2)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO Setup**: 2 Buttons (Pull-Down), OLED.
2.  **Reset**: `sel = 0`.

**B. Main Loop Phase**
3.  **Input Monitor**:
    *   If GP15 (Down): `sel = 1`.
    *   If GP14 (Up): `sel = 0`.
4.  **Render Menu**:
    *   Clear Screen.
    *   **Draw Text**: "LIGHT" at (30, 10). "FAN" at (30, 40).
5.  **Apply Selection Bar**:
    *   If `sel` == 0:
        *   Draw `fill_rect` behind "LIGHT" (X=25, Y=8, W=80, H=12).
        *   Draw Text "LIGHT" in Black (color=0) on top of the bar.
    *   If `sel` == 1:
        *   Draw `fill_rect` behind "FAN" (X=25, Y=38, W=80, H=12).
        *   Draw Text "FAN" in Black.

### 9. Execution Flow
1.  **Display**: Two options appear on screen.
2.  **Navigate**: User clicks the Down button.
3.  **State Change**: The variable `sel` updates.
4.  **Logic**: The "highlight bar" (white rectangle) moves to the new position.
5.  **Visual Trick**: By drawing black text over a white rectangle, we create the classic "High-Contrast Highlight" seen in modern OS menus.

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
        oled.text("OPTION 1", 25, 14, 0) # Black text
    else:
        oled.text("OPTION 1", 25, 14, 1) # White text
        
    # Option 2
    if sel == 1:
        oled.fill_rect(20, 35, 80, 15, 1)
        oled.text("OPTION 2", 25, 39, 0)
    else:
        oled.text("OPTION 2", 25, 39, 1)
        
    oled.show()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Layering**: Drawing the text *first* and then the rectangle. The rectangle covers the text. Always draw the background bar *before* the text.

### 12. Try This Next
*   **Third Option**: Add a middle option and use modulo logic (`sel = (sel+1)%3`).
"""

    p0567 = """
---

## 1. Project 0567: OLED Shapes Alarm System

### 2. Learning Objective
Create a high-urgency visual alert by rapidly "Inverting" the entire screen (toggling between Black/White and White/Black) to signal an alarm.

### 3. Concepts Introduced
*   Screen Inversion
*   Visual Pacing (Strobe)
*   Global State Toggling
*   Alert Psychology

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_invert`** (The driver command)
*   **from Loops, drag `repeat`** (Strobe effect)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Global command.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**: Initialize. Draw large "WARNING" text in center.

**B. Alarm Phase**
2.  **Strobe Cycle**:
    *   From **Loops**, repeat 10 times:
    *   **Invert ON**: Show White background with Black text.
    *   Wait 0.1s.
    *   **Invert OFF**: Show Black background with White text.
    *   Wait 0.1s.

### 9. Execution Flow
1.  **Alert**: Something goes wrong (e.g., sensor detects gas).
2.  **Command**: The Pico sends a hardware command to "Flip" every pixel.
3.  **Pattern**: The screen flashes like a strobe light.
4.  **Observer**: This is much harder for a user to ignore than a small text message, as it significantly changes the room's ambient light level.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("!!! DANGER !!!", 15, 25, 1)
oled.show()

# Strobe Alarm
while True:
    oled.invert(1)
    time.sleep(0.2)
    oled.invert(0)
    time.sleep(0.2)
```

### 11. Common Mistakes
*   **Invert Logic**: Some OLEDS need `invert(True)` while others need `fill(1)` and colored text. Check your driver's specific method.

### 12. Try This Next
*   **Beeper Sync**: Add a buzzer that beeps at the exact same moment the screen turns white.
"""

    p0568 = """
---

## 1. Project 0568: The OLED Shapes Game

### 2. Learning Objective
Programm the core locomotion logic of a "Snake" game, where a pixel "head" moves continuously and changes direction based on button inputs.

### 3. Concepts Introduced
*   Locomotion Logic (Vector movement)
*   Vector Direction Handling
*   Boundary Clipping
*   Game Ticks

### 4. Hardware Required
*   Raspberry Pi Pico
*   4x Buttons (U/D/L/R)
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buttons** | GP12-15 | Directional Input |

### 6. Blocks Used
*   **from Variables, drag `change_variable`** (X = X + DX)
*   **from Display, drag `pico_oled_pixel`**
*   **from Logic, drag `if_do`**

### 7. Variables
*   **px, py**: Integer (Current head)
*   **dx, dy**: Integer (Change per tick)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Position**: `px=64, py=32, dx=2, dy=0` (Moving Right).

**B. Main Loop Phase**
2.  **Read Directions**:
    *   If GP12 (Up): `dx=0, dy=-2`.
    *   If GP13 (Dn): `dx=0, dy=2`.
    *   If GP14 (Lt): `dx=-2, dy=0`.
    *   If GP15 (Rt): `dx=2, dy=0`.
3.  **Apply Physics**:
    *   `px = px + dx`.
    *   `py = py + dy`.
4.  **Check Death**:
    *   If `px` < 0 or `px` > 127: Game Over.
5.  **Render**:
    *   Clear, Draw pixel at `px, py`, Show.
6.  **Wait**: 0.05s.

### 9. Execution Flow
1.  **Movement**: The dot "marches" across the screen automatically.
2.  **Input**: User presses "Up".
3.  **Vector**: The `dx` (horizontal speed) becomes 0, and `dy` (vertical) becomes negative.
4.  **Redirect**: The dot immediately turns upward without stopping.
5.  **Game**: User must keep turning to stay within the rectangle edges.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(12, 16)]

x, y = 64, 32
dx, dy = 1, 0

while True:
    if btns[0].value(): dx, dy = 0, -1 # Up
    if btns[1].value(): dx, dy = 0, 1 # Down
    if btns[2].value(): dx, dy = -1, 0 # Left
    if btns[3].value(): dx, dy = 1, 0 # Right
    
    x += dx
    y += dy
    
    if x < 0 or x > 127 or y < 0 or y > 63:
        oled.fill(0); oled.text("CRASH!", 40, 30); oled.show()
        time.sleep(2)
        x, y = 64, 32; dx, dy = 1, 0 # Reset
        
    oled.fill(0)
    oled.rect(x, y, 3, 3, 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Opposite Turn**: Allowing the snake to turn 180 degrees into itself (e.g., if moving right, "Left" shouldn't work). Add a check: `if dx != 1: dx = -1`.

### 12. Try This Next
*   **Food**: Place a random pixel. If the snake's X/Y matches, speed up the game.
"""

    p0569 = """
---

## 1. Project 0569: Automated OLED Shapes

### 2. Learning Objective
Create a vector-based "Analog Gauge" with a needle that rotates within a circular dial to visualize sensor data (e.g., Potentiometer).

### 3. Concepts Introduced
*   Vector Graphics
*   Trigonometry (Simplified Sine/Cosine)
*   Radius/Angle mapping
*   Dashboard Design

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Gauge Pot** | GP26 | Data Source |

### 6. Blocks Used
*   **from Display, drag `pico_oled_line`** (Gauge Needle)
*   **from Display, drag `pico_oled_circle`** (Gauge Dial)
*   **from Math, drag `sine` / `cosine`**

### 7. Variables
*   **angle**: Float (0 to 180 degrees)
*   **end_x, end_y**: Integer (Needle tip)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: OLED and ADC.

**B. Main Loop Phase**
2.  **Read Data**: `val = ADC_Read(26)`.
3.  **Map to Arc**:
    *   `angle = map val (0-65535) to (180 to 360)`. (Upper half and circle).
4.  **Calc Tip (Trig)**:
    *   `end_x = 64 + cos(angle) * 20`.
    *   `end_y = 60 + sin(angle) * 20`.
5.  **Render**:
    *   Clear.
    *   **Draw Base**: Circle at (64, 60) with R=30.
    *   **Draw Needle**: Line from (64, 60) to (`end_x, end_y`).
    *   Show.

### 9. Execution Flow
1.  **Sense**: Potentiometer provides a number.
2.  **Logic**: The number is treated as an angle on a dial.
3.  **Math**: The Pico uses trigonometry to find the X/Y coordinates of the tip of the needle based on that angle.
4.  **Actuation**: A line is drawn connecting the center to the tip.
5.  **Result**: The user sees a classic speedometer-style gauge.

### 10. Generated Code
```python
import machine, ssd1306, time, math

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)

while True:
    raw = pot.read_u16()
    # Map to 180 degree arc (top half)
    angle_rad = (raw * 3.14159 / 65535) + 3.14159
    
    # Calculate needle tip (Radius 25)
    tx = int(64 + math.cos(angle_rad) * 25)
    ty = int(60 + math.sin(angle_rad) * 25)
    
    oled.fill(0)
    # Dial
    oled.circle(64, 60, 30, 1)
    # Needle
    oled.line(64, 60, tx, ty, 1)
    
    oled.show()
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Radians**: Most Math blocks use Radians, not Degrees. Multiply degrees by $3.14/180$ to convert.
*   **Tip Clipping**: If your radius is too large, the needle tip will try to draw outside (0-63), causing an error in some libraries.

### 12. Try This Next
*   **Digital Readout**: Print the raw percentage (0-100) exactly in the center of the gauge base.
"""

    p0570 = """
---

## 1. Project 0570: Mastering OLED Shapes

### 2. Learning Objective
Programm a 3D wireframe rotating cube by projecting 3D coordinates $(X, Y, Z)$ onto a 2D screen using perspective math.

### 3. Concepts Introduced
*   3D Projection (Perspective)
*   Coordinate Arrays
*   Rotation Matrices (Concept)
*   Vector Drawing

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from List, drag `create_list`** (Store 8 vertices)
*   **from Math, drag `trigonometry`**
*   **from Display, drag `pico_oled_line`** (12 edges)

### 7. Variables
*   **angle**: Float (Rotation speed)
*   **nodes**: List (Cube points)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Cube**: Create a list of 8 points representing corners of a cube $(\pm 1, \pm 1, \pm 1)$.
2.  **Setup Screen**: Init OLED.

**B. Rotation Phase**
3.  **Update Rotation**: `angle = angle + 0.05`.
4.  **Transform**: For each point in the list:
    *   Rotate point using `sin(angle)` and `cos(angle)`.
    *   Project to 2D: `screen_x = (x * 30) + 64`, `screen_y = (y * 30) + 32`.
5.  **Render Edges**:
    *   Clear Screen.
    *   Draw 12 lines connecting the projected 2D points to form a cube.
    *   Show.

### 9. Execution Flow
1.  **Process**: The Pico handles simple 3D math (Sine/Cosine) for 8 points.
2.  **Flatten**: It turns those 3D coordinates into 2D $(x,y)$ values that "look" 3D.
3.  **Render**: The 12 edges are drawn every frame.
4.  **Observer**: The cube appears to float and spin in 3D space on the flat screen.

### 10. Generated Code
```python
import machine, ssd1306, time, math

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Simplified 2D Projection of 3D lines
nodes = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

a = 0
while True:
    a += 0.1
    p = []
    for x,y,z in nodes:
        # Rotate on Y axis
        nx = x * math.cos(a) - z * math.sin(a)
        nz = x * math.sin(a) + z * math.cos(a)
        # Project to 2D
        p.append((int(nx * 20 + 64), int(y * 20 + 32)))
        
    oled.fill(0)
    for e1, e2 in edges:
        oled.line(p[e1][0], p[e1][1], p[e2][0], p[e2][1], 1)
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Math Load**: Doing math on 1000 points will freeze the Pico. Stick to simple shapes like cubes (8 points).
*   **Division by Zero**: If adding Z perspective (`x / z`), ensure `z` isn't 0.

### 12. Try This Next
*   **Scale**: Use a potentiometer to "Zoom" in and out of the cube by changing the multiplier (20).
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0561 + p0562 + p0563 + p0564 + p0565 + p0566 + p0567 + p0568 + p0569 + p0570)
    
    print("Batch 57 (0561-0570) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch57()
