import os

def regenerate_batch_52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # We append to the file created by Batch 51
    
    batch_header = """
---

#  Batch 52: Animation 3
"""

    p0511 = """
## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Create a full-screen "Countdown" animation (3-2-1) using clear-and-redraw logic on an OLED display.

### 3. Concepts Introduced
*   Frame Buffer Management
*   Sequential Display Logic
*   I2C Communication Handshake
*   Text Coordinate Centering

### 4. Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED (128x64)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **SDA** | GP8 | I2C0 Data |
| **SCL** | GP9 | I2C0 Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_clear`**
*   **from Display, drag `pico_oled_text`**
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **None**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init OLED**:
    *   From **Display**, drag `pico_oled_init` (SDA=8, SCL=9).
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Frame 1 (Three)**:
    *   `pico_oled_clear`.
    *   `pico_oled_text`("3", X=60, Y=30).
    *   `pico_oled_show`.
    *   Wait 1s.
2.  **Frame 2 (Two)**:
    *   `pico_oled_clear`.
    *   `pico_oled_text`("2", X=60, Y=30).
    *   `pico_oled_show`.
    *   Wait 1s.
3.  **Frame 3 (One)**:
    *   `pico_oled_clear`.
    *   `pico_oled_text`("1", X=60, Y=30).
    *   `pico_oled_show`.
    *   Wait 1s.

### 9. Execution Flow
1.  **Blank**: Screen wipes previous data.
2.  **Buffer**: The number "3" is written to memory.
3.  **Push**: The `show()` command sends the buffer to the glass.
4.  **Repeat**: The process repeats for each number.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for num in ["3", "2", "1"]:
        oled.fill(0)
        oled.text(num, 60, 30)
        oled.show()
        time.sleep(1)
```

### 11. Common Mistakes
*   **Missing Show**: Changes don't appear until `show()` is called.

### 12. Try This Next
*   **Go Frame**: Add "GO!" at the end.
"""

    p0512 = """
---

## 2. Project 0512: Blinking Animation

### 2. Learning Objective
Animate a facial expression ("Wink") by swapping a Circle primitive (Open Eye) with a Line primitive (Closed Eye).

### 3. Concepts Introduced
*   Geometric Primitives
*   State-based Sprites
*   Animation Timing
*   Composite Drawing (Face + Eyes)

### 4. Hardware Required
*   Pico, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: `pico_oled_init`.

**B. Main Loop Phase**
1.  **Open Face**:
    *   `clear`.
    *   `rect`(30,10, 68,44) (Face).
    *   `circle`(45,25, 5) (Left Eye).
    *   `circle`(80,25, 5) (Right Eye).
    *   `show`. Wait 2s.
2.  **Wink Face**:
    *   `clear`.
    *   `rect` (Face), `circle` (Left Eye).
    *   `line`(75,25, 85,25) (Right Eye Closed).
    *   `show`. Wait 0.5s.

### 10. Generated Code
```python
import machine, ssd1306, time
# ... init ...
while True:
    # Open
    oled.fill(0); oled.rect(30,10,68,44,1); oled.circle(45,25,5,1); oled.circle(80,25,5,1); oled.show(); time.sleep(2)
    # Wink
    oled.fill(0); oled.rect(30,10,68,44,1); oled.circle(45,25,5,1); oled.line(75,25,85,25,1); oled.show(); time.sleep(0.5)
```
"""

    p0513 = """
---

## 3. Project 0513: Manual Animation Control

### 2. Learning Objective
Create a digital Etch-a-Sketch using two potentiometers to control X/Y coordinates without clearing the screen, leaving a trail.

### 3. Concepts Introduced
*   Persistence Drawing
*   Coordinate Mapping (Scaling ADC to Resolution)
*   Continuous Input Sampling

### 4. Hardware Required
*   Pico, OLED, 2x Potentiometers

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pot X** | GP26 | 0-128 |
| **Pot Y** | GP27 | 0-64 |

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear**: `pico_oled_clear`. `pico_oled_show`.

**B. Main Loop Phase**
1.  **Read Inputs**:
    *   `x` = `map`(`pico_adc_read`(26), 0-65535, 0-127).
    *   `y` = `map`(`pico_adc_read`(27), 0-65535, 0-63).
2.  **Draw Dot**:
    *   `pico_oled_pixel`(`x`, `y`).
    *   **Do NOT Clear**.
    *   `pico_oled_show`.
    *   Wait 0.01s.

### 10. Generated Code
```python
import machine, ssd1306, time
# ... init ...
oled.fill(0); oled.show()
adc_x = machine.ADC(26); adc_y = machine.ADC(27)
while True:
    x = int(adc_x.read_u16() * 127 / 65535)
    y = int(adc_y.read_u16() * 63 / 65535)
    oled.pixel(x, y, 1)
    oled.show()
    time.sleep(0.01)
```
"""

    p0514 = """
---

## 4. Project 0514: Animation Sequences

### 2. Learning Objective
Visualize a "Loading Bar" by incrementally filling a rectangle from 0% to 100% width over 5 seconds.

### 3. Concepts Introduced
*   Progress Logic
*   Calculated Geometry
*   Visual Feedback
*   Loops within Loops

### 4. Hardware Required
*   Pico, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Standard OLED setup.

**B. Main Loop Phase**
1.  **Iterate**:
    *   From **Loops**, `count_with` `w` from 0 to 100.
    *   `clear`.
    *   `rect`(10, 30, 100, 10) (Frame).
    *   `fill_rect`(10, 30, `w`, 10) (Bar).
    *   `show`.
    *   Wait 0.05s.

### 10. Generated Code
```python
while True:
    for w in range(101):
        oled.fill(0)
        oled.rect(10,30,100,10,1)
        oled.fill_rect(10,30,w,10,1)
        oled.show()
        time.sleep(0.05)
```
"""

    p0515 = """
---

## 5. Project 0515: Interactive Animation

### 2. Learning Objective
Create a "Jump" animation where a character moves up and down (Y-axis) in a predefined arc when a button is pressed.

### 3. Concepts Introduced
*   Trajectory Logic
*   Triggered Animation Sequences
*   Blocking vs Non-Blocking Animation (Intro to Blocking)

### 4. Hardware Required
*   Pico, OLED, Button (GP14)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Draw Ground**: `char_y = 60`.

**B. Main Loop Phase**
1.  **Idle**: Draw char at 60. Check Button.
2.  **Jump Logic**:
    *   If Button Pressed:
        *   Sets: [50, 40, 30, 40, 50, 60].
        *   For each Y in Set: Clear, Draw at Y, Show, Wait 0.05s.

### 10. Generated Code
```python
y_pos = 60
while True:
    if btn.value():
        # Jump Arc
        for y in [50, 40, 30, 40, 50, 60]:
            oled.fill(0); oled.text("O", 60, y); oled.show(); time.sleep(0.05)
    else:
        # Idle
        oled.fill(0); oled.text("O", 60, 60); oled.show()
```
"""

    p0516 = """
---

## 6. Project 0516: Smart Animation Switch

### 2. Learning Objective
Simulate "Screen Rotation". If Button A is pressed, redraw the text vertically instead of horizontally.

### 3. Concepts Introduced
*   Layout Logic
*   Conditional Rendering
*   Display Orientation

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Check**:
    *   If Button HIGH (Vertical Mode):
        *   `clear`.
        *   `text`("H", 60, 10).
        *   `text`("E", 60, 20).
        *   `text`("L", 60, 30).
    *   Else (Horizontal Mode):
        *   `clear`.
        *   `text`("HELLO", 40, 30).
    *   `show`.

### 10. Generated Code
```python
while True:
    oled.fill(0)
    if btn.value():
        for i, char in enumerate("HELLO"):
            oled.text(char, 60, 10 + (i*10))
    else:
        oled.text("HELLO", 40, 30)
    oled.show()
```
"""

    p0517 = """
---

## 7. Project 0517: Animation Alarm System

### 2. Learning Objective
Create a "Heartbeat" monitor. A heart sprite pulses (Scale Small/Big). If "Stress Button" is held, the pulse rate increases significantly.

### 3. Concepts Introduced
*   Dynamic Sprite Scaling
*   Variable Timing Systems
*   Alarm States

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Determine Delay**:
    *   If Button HIGH: `wait = 0.05` (Stress).
    *   Else: `wait = 0.5` (Relaxed).
2.  **Pump**:
    *   `clear`. Draw Big Heart (R=20). `show`. Wait `wait`.
    *   `clear`. Draw Small Heart (R=10). `show`. Wait `wait`.

### 10. Generated Code
```python
while True:
    w = 0.05 if btn.value() else 0.5
    oled.fill(0); oled.circle(64,32,20,1); oled.show(); time.sleep(w)
    oled.fill(0); oled.circle(64,32,10,1); oled.show(); time.sleep(w)
```
"""

    p0518 = """
---

## 8. Project 0518: The Animation Game

### 2. Learning Objective
"Avoid the Drop". A dot falls from Y=0 to Y=64. Player moves X at Y=60. Collision resets game.

### 3. Concepts Introduced
*   Collision Detection (Distance < Radius)
*   Game Loop Architecture
*   Input Processing

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `px=60`, `ex=30`, `ey=0`.

**B. Main Loop Phase**
1.  **Input**: If BtnL: `px -= 5`. If BtnR: `px += 5`.
2.  **Physics**: `ey += 2`. If `ey > 64`: `ey=0`, `ex=random`.
3.  **Collision**:
    *   If `abs(px - ex) < 5` AND `ey > 55`: "BOOM". Reset.
4.  **Render**: Clear, Draw Player, Draw Enemy, Show.

### 10. Generated Code
```python
while True:
    if btn_l.value(): px -= 5
    if btn_r.value(): px += 5
    ey += 3
    if ey > 64: 
        ey = 0; ex = random.randint(0, 120)
    # Collision
    if abs(px - ex) < 8 and ey > 55:
        oled.text("HIT!", 50, 30); oled.show(); time.sleep(2); ey = 0
    
    oled.fill(0); oled.rect(px,60,10,4,1); oled.pixel(ex,ey,1); oled.show(); time.sleep(0.05)
```
"""

    p0519 = """
---

## 9. Project 0519: Automated Animation

### 2. Learning Objective
"Screensaver". Monitor idle time. If no button pressed for 10s, start bouncing text logic.

### 3. Concepts Introduced
*   Idle Timers
*   State Machine (Active vs Screensaver)
*   Reset on Interrupt

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Timer**:
    *   If Button: `idle_timer = 0`.
    *   Else: `idle_timer += 0.1`.
2.  **Logic**:
    *   If `idle_timer > 10`: Run Bounce Logic.
    *   Else: Show "Active Mode".

### 10. Generated Code
```python
idle = 0
while True:
    if btn.value(): idle = 0
    else: idle += 0.1
    
    oled.fill(0)
    if idle > 100: # 10s approx
        # Screensaver logic
        oled.text("DVD", x, y)
    else:
        oled.text("Working...", 30, 30)
    oled.show(); time.sleep(0.1)
```
"""

    p0520 = """
---

## 10. Project 0520: Mastering Animation

### 2. Learning Objective
"Sprite Sheet". Animate a character walking by toggling between two distinct bitmaps (Legs Open / Legs Closed) while moving across screen.

### 3. Concepts Introduced
*   Frame-based Animation
*   Bitmap/Sprite Management
*   Coordinate Translation

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Move**: `x += 1`.
2.  **Animate**:
    *   If `x % 2 == 0`: Draw "Pacman Open".
    *   Else: Draw "Pacman Closed".
3.  **Render**: Show at `x`, 30.

### 10. Generated Code
```python
x = 0
while True:
    x = (x + 2) % 128
    oled.fill(0)
    if (x // 2) % 2 == 0:
        oled.text("C", x, 30) # Open
    else:
        oled.text("O", x, 30) # Closed
    oled.show(); time.sleep(0.1)
```
"""

    content = batch_header + p0511 + p0512 + p0513 + p0514 + p0515 + p0516 + p0517 + p0518 + p0519 + p0520

    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    regenerate_batch_52()
