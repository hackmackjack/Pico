
## Project 0167: OLED Shapes Alarm System

### 1. Learning Objective
Learn how to implement high-priority visual alerts. Understand how to use line rendering to create a full-screen "X" graphic that acts as a definitive visual alarm when a specific condition (button press) is met.

### 2. Concepts Introduced
*   **Vector Alerts**: Using lines to cover the entire available display area for impact.
*   **Conditional Graphics**: Drawing specific elements only during an "Alert" state.
*   **Screen Space Navigation**: Calculating diagonal lines from corner to corner (0,0 to 127,63).

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   1 Button
*   10k Ohm pull-down resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alert Button** | GP14 | Trigger for the 'X' alarm |
| **OLED (I2C)** | GP0/GP1 | Display output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Displays, drag `pico_oled_line`** (draw line)
*   **from Displays, drag `pico_oled_text`** (draw text)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **is_alarm**: Boolean flag representing the system state.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Display**: From **Displays**, drag `pico_oled_init`.

**B. Logic Phase (Loop)**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.
3.  **Read Signal**:
    *   From **Logic**, drag `controls_if` with **else**.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True.

**C. Visual Alarm Phase**
4.  **Draw "X Marks the Spot"**:
    *   Inside the **If** (Alarm ON):
    *   **Clear** screen.
    *   From **Displays**, drag `pico_oled_line`. **Set** [0,0] to [127,63]. (Top-Left to Bottom-Right).
    *   From **Displays**, drag another `pico_oled_line`. **Set** [0,63] to [127,0]. (Bottom-Left to Top-Right).
    *   From **Displays**, drag `pico_oled_text`. **Set** text to "SYSTEM HALT" at [30, 28].
5.  **Draw "System Good"**:
    *   Inside the **Else** (Normal):
    *   **Clear** screen.
    *   From **Displays**, drag `pico_oled_text`. **Set** text to "STATUS: OK" at [40, 30].

**D. Finalize Frame**
6.  **Refresh Hardware**:
    *   Snap `pico_oled_show`.
    *   **Wait** 0.1 seconds.

### 8. Execution Flow
1.  **Check**: The Pico monitors the button state.
2.  **Normal**: If released, simple "OK" text is displayed.
3.  **Trigger**: If pressed, the code calculates two diagonal lines that cross the screen's center.
4.  **Action**: The OLED buffer is filled with these lines, creating a massive "X" indicator.
5.  **Result**: High-visibility feedback that unmistakable alerts the user to an event.

### 9. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

# Hardware
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    oled.fill(0)
    
    if button.value() == 1:
        # Drawing the giant X
        oled.line(0, 0, 127, 63, 1)
        oled.line(0, 63, 127, 0, 1)
        oled.text("ALARM!!", 35, 28, 1)
    else:
        oled.text("System OK", 30, 28, 1)
        
    oled.show()
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **Coordinate Math**: Remember the screen is 128 wide (X: 0-127) and 64 high (Y: 0-63). Using (128, 64) as coordinates might cause errors in some drivers.
*   **Color Conflict**: If the text is behind the lines, it might be hard to read. Use an offset to place text in a black space.

### 11. Try This Next
*   **Flashing X**: Make the lines switch between White and Black every 0.2s for a strobe alert.
*   **Borders**: Add a thick rectangle around the edges during the alarm state for even more impact.

---

## Project 0168: The OLED Shapes Game

### 1. Learning Objective
Explore coordinate logic and target detection. Learn how to verify if a user action (button press) aligns with a randomly generated coordinate (circle) during a specific timing window.

### 2. Concepts Introduced
*   **Hit Detection**: Mathematically checking if a point (user input) is inside a circle.
*   **Randomized Spawning**: Using `random` to place objects in unpredictable spots.
*   **Zone Logic**: Defining specific screen areas that are "valid" for interaction.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   1 Button
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Game Button** | GP14 | Press when target is in center |
| **OLED (I2C)** | GP0/GP1 | Game screen |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_random_int`** (randomize placement)
*   **from Displays, drag `pico_oled_circle`** (draw target)
*   **from Logic, drag `controls_if`** (checking coordinates)

### 6. Variables
*   **target_x**: Randomized X position (0-127).
*   **score**: Player's successful hits.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Game State**:
    *   From **Variables**, **Set** `score` = 0.
    *   Initialize OLED.

**B. Target Spawning Phase**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Randomize Location**:
    *   From **Math**, drag `math_random_int`. **Set** X from 10 to 110.
    *   **Set** variable `target_x` to this result.

**C. Game Logic Phase**
4.  **Display Target**:
    *   **Clear** screen.
    *   Draw **Square** outline at [54, 22] (Center 20x20 "Target Zone").
    *   Draw **Circle** at [`target_x`, 32] with radius 5.
    *   Snap `pico_oled_show`.

5.  **Check for "Hit"**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Button** GP14 is Pressed AND (`target_x` > 54) AND (`target_x` < 74).
    *   **Action**: 
        *   **Set** `score` = `score` + 1.
        *   Show "HIT!" text on screen.
        *   **Wait** 0.5s.

**D. Refresh Phase**
6.  **Next Turn**:
    *   **Wait** 0.2 seconds before the target jumps to a new spot.

### 8. Execution Flow
1.  **Spawn**: A circle appears at a random X coordinate.
2.  **Challenge**: The player must wait until the circle is inside the center box.
3.  **Action**: Player hits the button.
4.  **Verify**: The Pico checks if the current `target_x` is between 54 and 74.
5.  **Reward**: If successful, the score increases and visual feedback is given.

### 9. Generated Code
```python
import machine
import ssd1306
import time
import random

# Hardware
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

score = 0

while True:
    # Random spawning
    tx = random.randint(10, 110)
    
    # Draw screen
    oled.fill(0)
    oled.rect(54, 22, 20, 20, 1) # Target Zone
    
    # Draw simple circle
    oled.pixel(tx, 32, 1)
    oled.pixel(tx+1, 32, 1)
    oled.pixel(tx-1, 32, 1)
    oled.pixel(tx, 31, 1)
    oled.pixel(tx, 33, 1)
    
    oled.text("S:" + str(score), 0, 0, 1)
    oled.show()
    
    # Window for reaction
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < 500:
        if button.value() == 1:
            if tx > 54 and tx < 74:
                score += 1
                oled.text("HIT!", 54, 45, 1)
                oled.show()
                time.sleep(0.5)
                break
    
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **No Reaction Time**: If the loop runs too fast, the player won't have time to see the circle before it moves. Use a `while` loop within the timing window to check for button presses.
*   **Strict Equals**: Don't check for `target_x == 64`. It is too hard for a player. Use a range (e.g., 54 to 74).

### 11. Try This Next
*   **Difficulty Scaling**: Make the window for reaction shorter as the score gets higher.
*   **Sound**: Add a Buzzer beep for every "Hit".

---

## Project 0169: Automated OLED Shapes

### 1. Learning Objective
Explore real-world physics visualization. Learn how to map sensor data from a Tilt sensor or Accelerometer to the XY coordinates of a circle on screen to create a "Digital Spirit Level".

### 2. Concepts Introduced
*   **Orientation Mapping**: Translating physical tilt (gravity) into coordinate shifts on a grid.
*   **Inertia (Visual)**: moving a shape based on an external sensor input.
*   **Stabilization**: Handing noisy sensor data to keep the "bubble" from jittering on screen.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Accelerometer (e.g., MPU6050) or 2 Tilt Switches
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **IMU (I2C)** | GP0/GP1 | Shares Bus with OLED |
| **OLED (I2C)** | GP0/GP1 | Display output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_imu_read`** (read accelerometer X/Y)
*   **from Math, drag `math_map`** (convert -1g/+1g to 0-127)
*   **from Displays, drag `pico_oled_circle`** (draw bubble)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **tilt_x**, **tilt_y**: Raw sensor data.
*   **draw_x**, **draw_y**: Screen coordinates for the "bubble".

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**: Start both the OLED and the IMU (mpu6050) modules.

**B. Physics Phase (Loop)**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.
3.  **Read Tilt**:
    *   From **Sensors**, drag the `pico_imu_read` blocks.
    *   **Set** `tilt_x` = Accelerometer X.
    *   **Set** `tilt_y` = Accelerometer Y.

**C. Logic and Rendering Phase**
4.  **Translate to Screen**:
    *   From **Math**, **Map** `tilt_x` from [-10.0 to 10.0] into [10 to 117].
    *   **Map** `tilt_y` from [-10.0 to 10.0] into [10 to 53].
    *   **Set** variable `draw_x` and `draw_y` to these results.

5.  **Refresh Graphics**:
    *   **Clear** screen.
    *   Draw static crosshair lines in the center: [64,0 to 64,63] and [0,32 to 127,32].
    *   From **Displays**, drag `pico_oled_circle`. (Filled Circle).
    *   **Set** position to [`draw_x`, `draw_y`], Radius = 6.
    *   Snap `pico_oled_show`.

6.  **Settle**: **Wait** 0.05 seconds.

### 8. Execution Flow
1.  **Sample**: The Pico reads the MPU6050 to find the direction of gravity.
2.  **Calculate**: If the board is tilted left, the `tilt_x` value becomes negative.
3.  **Update**: The map function calculates a low `draw_x` (e.g., 20) instead of center (64).
4.  **Visualize**: The "Bubble" circle is drawn on the left side of the screen.
5.  **Result**: The user can "Level" their desk by moving the Pico until the circle sits perfectly in the center.

### 9. Generated Code
```python
import machine
import ssd1306
import time

# Placeholder for MPU6050 logic
# Assuming standard i2c setup
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Simulated tilt values (Replace with actual IMU read)
    # tx, ty range from -10 to 10
    tx = 0 # Read Accelerometer X
    ty = 0 # Read Accelerometer Y
    
    # Mapping to screen center
    bx = int((tx + 10) / 20 * 127)
    by = int((ty + 10) / 20 * 63)
    
    oled.fill(0)
    # Static guide lines
    oled.line(64, 0, 64, 63, 1)
    oled.line(0, 32, 127, 32, 1)
    
    # The bubble
    oled.fill_rect(bx-3, by-3, 6, 6, 1)
    
    oled.show()
    time.sleep(0.05)
```

### 10. Common Mistakes
*   **Inverted Axes**: If tilting left moves the bubble right, subtract the mapped value from the max (e.g., 127 - mapped_x).
*   **Sensitivity**: Values from an accelerometer jump around a lot. You might need to average the last 5 readings for a stable "Level".

### 11. Try This Next
*   **Precision Mode**: Blow up the center area so tiny tilts move the bubble much further (Digital magnifying glass).
*   **Calibration**: Add a button that tells the Pico "This current tilt is perfectly flat".

---

## Project 0170: Mastering OLED Shapes

### 1. Learning Objective
Explore 3D perspective rendering in a 2D space. Learn how to use coordinate offsets and diagonal line connections to simulate a 3D Cube (Wireframe) on a flat OLED display.

### 2. Concepts Introduced
*   **3D Projection (Simple)**: Rendering multiple planes (Front and Back) to create depth.
*   **Perspective Scaling**: understanding that an object "further away" (the back square) should be shifted or smaller.
*   **Vertex Connection**: Manually connecting specific points (Corners) across different planes to form a solid-looking object.

### 3. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0161)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Displays, drag `pico_oled_rect`** (draw the planes)
*   **from Displays, drag `pico_oled_line`** (connect corners)
*   **from Displays, drag `pico_oled_show`** (sync)

### 6. Variables
*   **offset**: The amount the back square is shifted from the front (initialized to 15).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Hardware**: Start OLED on GP0/GP1.

**B. Perspective Phase**
2.  **Define Planes**:
    *   **Clear** screen.
    *   **Draw Front Square**: (X=30, Y=10, Width=40, Height=40).
    *   **Draw Back Square**: (X=30+`offset`, Y=10+`offset`, Width=40, Height=40).

3.  **Connect Vertices**:
    *   From **Displays**, drag `pico_oled_line` blocks to connect the four corners:
    *   **Top-Left**: Connect [30, 10] to [30+`offset`, 10+`offset`].
    *   **Top-Right**: Connect [70, 10] to [70+`offset`, 10+`offset`].
    *   **Bottom-Left**: Connect [30, 50] to [30+`offset`, 50+`offset`].
    *   **Bottom-Right**: Connect [70, 50] to [70+`offset`, 50+`offset`].

**C. Finalize Graphics**
4.  **Reveal**: Snap `pico_oled_show`.
5.  **Steady Display**: **Wait** 1 second. (Or put in a loop to animate the `offset`).

### 8. Execution Flow
1.  **Plane A**: The "Front Face" is drawn as a standard square.
2.  **Plane B**: The "Back Face" is drawn slightly lower and to the right.
3.  **Logic**: By drawing lines between the matching corners of these two squares, the brain perceives it as a 3D box stretching into the screen.
4.  **Result**: A wireframe 3D cube appears on the miniature OLED.

### 9. Generated Code
```python
import machine
import ssd1306
import utime

# OLED Init
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_cube(x, y, size, offset):
    oled.fill(0)
    
    # Front Square
    oled.rect(x, y, size, size, 1)
    
    # Back Square
    oled.rect(x + offset, y + offset, size, size, 1)
    
    # Connect Corners
    oled.line(x, y, x + offset, y + offset, 1) # TL
    oled.line(x + size, y, x + size + offset, y + offset, 1) # TR
    oled.line(x, y + size, x + offset, y + size + offset, 1) # BL
    oled.line(x + size, y + size, x + size + offset, y + size + offset, 1) # BR
    
    oled.show()

while True:
    # Draw static cube
    draw_cube(30, 10, 35, 12)
    utime.sleep(2)
```

### 10. Common Mistakes
*   **Coordinate Overrun**: If your front square is too large or your offset too big, the back square will be drawn off the bottom of the screen.
*   **Calculating WRONG Corners**: Be very careful to connect the Top-Right of Square A to the Top-Right of Square B. Swapping them will result in a distorted "twisted" box.

### 11. Try This Next
*   **Animate Depth**: Put the `offset` in a loop (1 to 20 then back to 1) to make the cube look like it is growing and shrinking in depth.
*   **The Rotating Cube**: Shift the X and Y positions of the back square in a circle while keeping the front square still to simulate a rotating box.

---
