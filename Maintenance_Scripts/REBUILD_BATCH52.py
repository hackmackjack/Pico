import os

def rebuild_batch52():
    file_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Cut off from 0514 (Line 1399 is index 1398)
    # We found 1399 from Select-String
    kept_lines = lines[:1398]
    
    p0514 = """
## 1. Project 0514: Loading Bar

### 2. Learning Objective
Create a visual progress bar that fills from 0% to 100% over a 5-second duration on the OLED display.

### 3. Concepts Introduced
*   Progress Visualization
*   Rectangular Outlines and Filling
*   Timed Increments
*   Dynamic Coordinate Calculation

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display (SSD1306)
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C0 Data |
| **OLED SCL** | GP9 | I2C0 Clock |
| **OLED VCC** | 3.3V | Power |
| **OLED GND** | GND | Ground |

### 6. Blocks Used
*   **from Display, drag `pico_oled_rect`** (Draw outline)
*   **from Display, drag `pico_oled_fill_rect`** (Draw progress)
*   **from Loops, drag `count_with`** (Iterate progress)
*   **from Time, drag `pico_wait`** (Step delay)

### 7. Variables
*   **progress**: Integer (Current fill width from 0 to 100)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Display**:
    *   From **Display**, **Set** `pico_oled_init` on GP8/GP9.

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Draw Outline**:
    *   From **Display**, drag `pico_oled_clear`.
    *   From **Display**, drag `pico_oled_rect`.
        *   **Snap** into loop.
        *   Set X=14, Y=25, Width=100, Height=14.
4.  **Fill Progress**:
    *   From **Loops**, drag `count_with`.
        *   **Snap** below outline.
        *   Set variable `progress`, range 0 to 100.
    *   From **Display**, drag `pico_oled_fill_rect`.
        *   **Snap** inside count loop.
        *   Set X=14, Y=25, Width=`progress`, Height=14.
    *   From **Display**, drag `pico_oled_show`.
    *   From **Time**, drag `pico_wait`.
        *   Set 0.05 seconds (Total 5s for 100 steps).
5.  **Hold and Reset**:
    *   From **Time**, wait 1 second at 100%.

### 9. Execution Flow
1.  **Start**: The system initializes the OLED display.
2.  **Process**: The code enters a main loop that starts the progress at zero.
3.  **Output**: An empty rectangle outline is drawn once per cycle.
4.  **Animation**: An inner loop adds one pixel of width to an internal "fill" rectangle every 0.05 seconds.
5.  **Repeat**: Once the bar is full, the system waits briefly and restarts the sequence.

### 10. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for progress in range(0, 101):
        oled.fill(0)
        # Draw Outline
        oled.rect(14, 25, 100, 14, 1)
        # Draw Progress
        oled.fill_rect(14, 25, progress, 14, 1)
        oled.show()
        time.sleep(0.05)
    time.sleep(1)
```

### 11. Common Mistakes
*   **Flicker**: Clearing the screen *inside* the progress loop is necessary, but clearing it *too* often with very small delays can cause flickering.
*   **Wrong Width**: Setting the fill rectangle width larger than the outline (100) will cause the bar to appear to "leak" out of the box.

### 12. Try This Next
*   **Percentage Text**: Add a text block that displays the numeric percentage (e.g., "50%") above the bar.
*   **Color Warning**: If using a multi-color OLED, change the bar behavior when it reaches 90%.
"""

    p0515 = """
---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Animate a character "Jump" arc (shifting Y-coordinates) triggered by a button press on the OLED screen.

### 3. Concepts Introduced
*   Event-Driven Animation
*   Parabolic Trajectory (Simulated)
*   Input Polling
*   Sprite Positioning

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Input (Pull-Down) |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (Check button)
*   **from Display, drag `pico_oled_rect`** (Draw character)
*   **from Logic, drag `if_do`** (Handle press)

### 7. Variables
*   **is_jumping**: Boolean (Tracks jump state)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: Set GP14 as Input (Pull-Down). Initialize OLED.

**B. Main Loop Phase**
2.  **Draw Grounded Character**:
    *   From **Display**, drag `pico_oled_clear`.
    *   From **Display**, drag `pico_oled_rect` (X=60, Y=50, W=8, H=8).
    *   From **Display**, drag `pico_oled_show`.
3.  **Check for Jump**:
    *   From **Logic**, drag `if_do`.
    *   Condition: `pico_gpio_read` (GP14) is HIGH.
4.  **Execute Jump Arc**:
    *   **Phase 1 (Up)**:
        *   Set Y=40, Show, Wait 0.1s.
        *   Set Y=20, Show, Wait 0.1s.
    *   **Phase 2 (Down)**:
        *   Set Y=40, Show, Wait 0.1s.
        *   Set Y=50, Show, Wait 0.1s.

### 9. Execution Flow
1.  **Start**: The character sits at the bottom of the screen.
2.  **Listen**: The system continuously checks the button state.
3.  **Active**: When the button is pressed, the character's Y coordinate is updated in a sequence.
4.  **Arc**: The sequence (50->40->20->40->50) creates the illusion of upward motion and falling.
5.  **Return**: The character remains at the start position until the next press.

### 10. Generated Code
```python
import machine
import ssd1306
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_player(y):
    oled.fill(0)
    oled.rect(60, y, 8, 8, 1)
    oled.hline(0, 60, 128, 1) # Ground
    oled.show()

while True:
    draw_player(50)
    if btn.value():
        # Jump Arc
        draw_player(40); time.sleep(0.1)
        draw_player(20); time.sleep(0.1)
        draw_player(40); time.sleep(0.1)
        draw_player(50); time.sleep(0.1)
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **No Wait between Frames**: Without `time.sleep`, the jump happens faster than the screen can refresh, making it look like the character disappeared for a split second.
*   **Button Debounce**: Multiple jumps might trigger if the button is held.

### 12. Try This Next
*   **Double Jump**: Allow a second press to go even higher (Y=0).
*   **Gravity**: Use a loop to decrease the Y speed gradually for a smoother "floaty" jump.
"""

    p0516 = """
---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Implement a screen rotation feature that toggles the display orientation (Horizontal to Vertical) when a button is pressed.

### 3. Concepts Introduced
*   Screen Rotation (Orientation)
*   Coordinate Transformation
*   State-Based Rendering
*   Display Flipping

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Rotation Trigger |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_rotate`** (Set rotation)
*   **from Logic, drag `if_else`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **is_vertical**: Boolean (Current rotation state)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: Setup GP14 as Input. Init OLED.
2.  **Set State**: Set `is_vertical` to FALSE.

**B. Main Loop Phase**
3.  **Check Input**:
    *   From **Logic**, drag `if_do`.
    *   If `pico_gpio_read` (GP14) is HIGH:
    *   Set `is_vertical` to NOT `is_vertical`.
    *   Wait 0.3s (Debounce).
4.  **Apply Rotation**:
    *   If `is_vertical` is TRUE:
        *   Draw text "PICO" at (20, 10) in vertical mode.
    *   Else:
        *   Draw text "PICO" at (40, 25) in horizontal mode.
5.  **Update Display**:
    *   From **Display**, drag `pico_oled_show`.

### 9. Execution Flow
1.  **Start**: Screen shows text in landscape mode.
2.  **Input**: User presses the button.
3.  **Toggle**: The internal variable flips from False to True.
4.  **Render**: The code logic shifts the drawing coordinates and labels to fit a portrait (vertical) layout.
5.  **Feedback**: The screen effectively "rotates" its content for the user.

### 10. Generated Code
```python
import machine
import ssd1306
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

is_vertical = False

while True:
    if btn.value():
        is_vertical = not is_vertical
        time.sleep(0.3) # Debounce
        
    oled.fill(0)
    if is_vertical:
        # Simulate Vertical (narrower width)
        oled.text("V", 30, 10)
        oled.text("E", 30, 20)
        oled.text("R", 30, 30)
        oled.text("T", 30, 40)
    else:
        oled.text("HORIZONTAL", 20, 25)
    
    oled.show()
```

### 11. Common Mistakes
*   **Text Cutoff**: Vertical mode has less horizontal space. If you keep the same X coordinate, text may disappear off the side.

### 12. Try This Next
*   **Real Rotation**: Use the `oled.rotate()` method if your specific driver library supports hardware rotation.
"""

    p0517 = """
---

## 1. Project 0517: Animation Alarm System

### 2. Learning Objective
Create a dynamic "Heartbeat" animation that pulses at different speeds depending on a "Stress" button input.

### 3. Concepts Introduced
*   Dynamic Scaling
*   Input-Variable Frequency
*   Visual Signaling
*   Sprite Animation

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stress Button** | GP14 | Pull-Down |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`** (Used for heart lobes)
*   **from Logic, drag `if_else`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **pulse_delay**: Float (Time between pulse frames)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: IO and OLED.

**B. Main Loop Phase**
2.  **Check Stress**:
    *   From **Logic**, drag `if_else`.
    *   If `pico_gpio_read` (GP14) is HIGH:
        *   Set `pulse_delay` to 0.05 (Fast).
    *   Else:
        *   Set `pulse_delay` to 0.5 (Slow).
3.  **Animate Heart (Phase 1 - Big)**:
    *   Clear, Draw Big Heart, Show, Wait `pulse_delay`.
4.  **Animate Heart (Phase 2 - Small)**:
    *   Clear, Draw Small Heart, Show, Wait `pulse_delay`.

### 9. Execution Flow
1.  **Sense**: The system monitors the button.
2.  **Adjust**: If pressed (representing stress), it significantly reduces the delay between frames.
3.  **Process**: The heartbeat animation (scaling between two sizes) runs continuously.
4.  **Output**: The user sees a heart that "beats" faster when the button is held.

### 10. Generated Code
```python
import machine
import ssd1306
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_heart(size):
    oled.fill(0)
    # Simple Heart using 2 circles and a triangle (simplified)
    oled.fill_rect(64-size, 32-size, size*2, size*2, 1)
    oled.show()

while True:
    delay = 0.05 if btn.value() else 0.4
    
    # Pulse Big
    draw_heart(15)
    time.sleep(delay)
    # Pulse Small
    draw_heart(10)
    time.sleep(delay)
```

### 11. Common Mistakes
*   **Zero Delay**: If the delay becomes 0, the animation will be too fast to see anything but a flickering blur.

### 12. Try This Next
*   **Sound Alarm**: Add a buzzer that beeps in sync with each heart pulse.
"""

    p0518 = """
---

## 1. Project 0518: The Animation Game

### 2. Learning Objective
Build a "Falling Object" game where the player must dodge a falling dot by moving their own sprite left and right using buttons.

### 3. Concepts Introduced
*   Collision Detection
*   Game States (Win/Lose)
*   Coordinate Comparison
*   Sprite Movement

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   2x Push Buttons

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Left** | GP14 | Move Player Left |
| **Btn Right** | GP15 | Move Player Right |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Logic, drag `and_operation`** (for collision)
*   **from Display, drag `pico_oled_pixel`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **player_x**: Integer (Position 0-120)
*   **enemy_x**: Integer (Falling position)
*   **enemy_y**: Integer (Falling height)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: 2 Buttons (Pull-Down), OLED.
2.  **Reset Game**: Set `player_x`=60, `enemy_y`=0, `enemy_x`=random.

**B. Main Loop Phase**
3.  **Move Player**:
    *   If GP14 (Left): `player_x = player_x - 5`.
    *   If GP15 (Right): `player_x = player_x + 5`.
4.  **Move Enemy**:
    *   `enemy_y = enemy_y + 2`.
    *   If `enemy_y` > 64: Reset `enemy_y`=0, `enemy_x`=random.
5.  **Check Collision**:
    *   If `enemy_y` is near Player Y (60) AND `enemy_x` is near `player_x`:
    *   Show "GAME OVER", Wait 2s, Reset Score.
6.  **Draw and Show**:
    *   Clear, draw player at `player_x`, draw enemy at `enemy_x, enemy_y`, Show.

### 9. Execution Flow
1.  **Drop**: An "enemy" pixel starts at the top and moves downward.
2.  **React**: The player uses buttons to shift their "sprite" (a small box) out of the enemy's path.
3.  **Judge**: The system calculates the distance between the two objects every frame.
4.  **End**: If the distance is zero (collision), the animation freezes and a message appears.

### 10. Generated Code
```python
import machine
import ssd1306
import time
import random

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
b_l = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
b_r = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

px = 60
ex = random.randint(0, 120)
ey = 0

while True:
    if b_l.value(): px -= 4
    if b_r.value(): px += 4
    
    ey += 2
    if ey > 64:
        ey = 0
        ex = random.randint(0, 120)
        
    oled.fill(0)
    oled.rect(px, 55, 10, 5, 1) # Player
    oled.fill_rect(ex, ey, 4, 4, 1) # Enemy
    
    # Collision check
    if ey > 50 and abs(px - ex) < 8:
        oled.text("CRASH!", 40, 30)
        oled.show()
        time.sleep(2)
        ey = 0; px = 60
        
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **No Boundaries**: Player might move off-screen (X < 0 or X > 120) and become invisible. Add logic to stop them at the edges.

### 12. Try This Next
*   **Score Counter**: Increase a score every time the enemy resets to the top safely.
"""

    p0519 = """
---

## 1. Project 0519: Automated Animation

### 2. Learning Objective
Implement a "Screensaver" mode that activates after 10 seconds of inactivity, displaying a bouncing text animation to prevent "burn-in".

### 3. Concepts Introduced
*   Idle Detection (Timestamps)
*   Bouncing Physics (Boundary detection)
*   State Transition (Active vs Idle)
*   `time.ticks_ms()` usage

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Button (Activity trigger)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Activity Monitor |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`** (Get current time)
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `if_else`**

### 7. Variables
*   **last_activity**: Integer (Value of `ticks_ms`)
*   **is_idle**: Boolean
*   **x, y, dx, dy**: Physics variables for bouncing

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Button (In), OLED.
2.  **Reset Timer**: `last_activity = pico_milliseconds`.

**B. Main Loop Phase**
3.  **Check Activity**:
    *   If GP14 is HIGH: `last_activity = pico_milliseconds`.
4.  **Detect Idle**:
    *   If (`pico_milliseconds` - `last_activity`) > 10000: `is_idle = TRUE`.
    *   Else: `is_idle = FALSE`.
5.  **Render Mode**:
    *   If `is_idle` is TRUE:
        *   Animate "DVD" bouncing: `x += dx`, `y += dy`. If hit edge, `dx = -dx`.
    *   Else:
        *   Regular Display: Show "Press to Idle".

### 9. Execution Flow
1.  **Monitor**: The system constantly notes the time the button was last touched.
2.  **Timer**: It subtracts the current time from that last touch time.
3.  **Threshold**: If that difference exceeds 10 seconds, it enters screensaver mode.
4.  **Animation**: The screen changes from static text to a moving label.
5.  **Wake-up**: Pressing the button resets the timer and brings the static screen back.

### 10. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

last_act = time.ticks_ms()
x, y = 10, 10
dx, dy = 2, 2

while True:
    if btn.value():
        last_act = time.ticks_ms()
        
    oled.fill(0)
    if time.ticks_diff(time.ticks_ms(), last_act) > 5000: # 5s for demo
        x += dx
        y += dy
        if x < 0 or x > 100: dx *= -1
        if y < 0 or y > 50: dy *= -1
        oled.text("DVD", x, y)
    else:
        oled.text("SYSTEM ACTIVE", 10, 25)
        oled.text("Wait for Idle...", 10, 40)
        
    oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Millisecond vs Second**: 10 seconds = 10,000 milliseconds. Using "10" will make the idle mode trigger instantly.

### 12. Try This Next
*   **Random Color**: If using a color display, change the text color every time it hits a wall.
"""

    p0520 = """
---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
Animate a character sprite (Pacman) walking across the screen by alternating between "Open" and "Closed" mouth bitmap frames.

### 3. Concepts Introduced
*   Frame-Based Animation (Sprite Sheets)
*   Bitmap Graphics
*   Spatial Movement logic
*   Cyclic Frame Switching

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`**
*   **from Display, drag `pico_oled_line`** (Draw mouth)
*   **from Loops, drag `pico_forever`**

### 7. Variables
*   **frame**: Integer (0 or 1)
*   **pos_x**: Integer (horizontal position)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**: GP8/9.

**B. Main Loop Phase**
2.  **Iterate Movement**:
    *   Increase `pos_x` by 3. If > 128, reset to -10.
3.  **Toggle Frame**:
    *   Change `frame` to 1 - `frame` (flips between 0 and 1).
4.  **Draw Frame**:
    *   Clear Screen.
    *   Draw body (Yellow circle).
    *   If `frame` == 0 (Open):
        *   Draw lines forming a 60-degree mouth.
    *   If `frame` == 1 (Closed):
        *   Draw single horizontal line for mouth.
5.  **Show**: Wait 0.15s.

### 9. Execution Flow
1.  **Start**: Pacman appears on the left.
2.  **Move**: The sprite's X position increases slightly.
3.  **Flip**: The mouth state changes every single time the loop runs.
4.  **Display**: The sequence shows mouth-open, mouth-closed as he moves.
5.  **Perception**: This rapid alternation creates the illusion of a character "eating" his way across the screen.

### 10. Generated Code
```python
import machine
import ssd1306
import time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

x = 0
frame = 0

while True:
    oled.fill(0)
    
    # Body
    oled.ellipse(x+10, 32, 10, 10, 1, True)
    
    # Mouth logic
    if frame == 0:
        # Open mouth (draw black triangle)
        for y in range(22, 42):
            oled.line(x+10, 32, x+20, y, 0)
    else:
        # Closed mouth (just a line)
        oled.line(x+10, 32, x+20, 32, 0)
        
    oled.show()
    x += 2
    if x > 128: x = -20
    frame = 1 - frame
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Animation Speed**: If `time.sleep` is too long, the walking looks choppy. If too short, the mouth flickers too fast to see.

### 12. Try This Next
*   **Food**: Draw small 2x2 squares ("dots") in the path of Pacman and make them disappear as he passes over their X coordinate.
"""

    # Combine
    full_batch_content = "".join(kept_lines) + p0514 + p0515 + p0516 + p0517 + p0518 + p0519 + p0520
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_batch_content)
    
    print("Batch 52 Rebuilt and Completed (0511-0520) with Elite Standard v2.0.")

if __name__ == "__main__":
    rebuild_batch52()
