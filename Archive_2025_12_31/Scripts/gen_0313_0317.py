# Pass 1: Generate Projects 0313-0317
# Following locked Elite template from Batch 31

projects_0313_0317 = '''
## 1️⃣ Project 0313: Manual Animation Control

### 2️⃣ Learning Objective
Create an interactive square that changes size based on button input. You will learn how user input directly modifies visual properties in real-time, demonstrating responsive graphics control.

### 3️⃣ Concepts Introduced
*   **Dynamic Sizing**: Modifying shape dimensions based on variables.
*   **Button Input**: Using multiple buttons for different actions.
*   **Bounded Variables**: Limiting size within valid range to prevent errors.
*   **Redraw Cycle**: Clearing and redrawing shapes after property changes.

### 4️⃣ Hardware Required
*   **Pico**
*   **2 Buttons** (UP and DOWN)
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button UP** | GP10 | Enable PULL_DOWN |
| **Button DOWN** | GP11 | Enable PULL_DOWN |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup I2C OLED**
*   **Category:** Displays
*   **Block:** `Setup OLED I2C:[0] width:[128] height:[64]`

🔹 **Setup Button**
*   **Category:** Inputs
*   **Block:** `Setup Button pin:[N]` with PULL_DOWN

🔹 **OLED Rectangle**
*   **Category:** Displays
*   **Block:** `OLED rect x:[X] y:[Y] w:[W] h:[H] fill:[true/false]`

🔹 **OLED Clear/Show**
*   **Category:** Displays
*   **Block:** `OLED clear` and `OLED show`

### 7️⃣ Variables & State
*   **size**: Current square dimension in pixels (default: 10, range: 5-50).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[10]` (UP).
        *   **Snap** into setup block.
        *   Enable PULL_DOWN.
    *   From **Inputs**, drag `Setup Button pin:[11]` (DOWN).
        *   **Snap** into setup block.
        *   Enable PULL_DOWN.
    *   From **Variables**, drag `set [size] to [10]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check UP Button**:
        *   From **Logic**, drag `if [Button 10 Pressed] then`.
            *   **Snap** into loop.
            *   Then:
                *   From **Variables**, drag `change [size] by [2]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [size] > [50] then set [size] to [50]`.
                    *   **Snap** below (bounds checking).
                *   Wait for button release (debounce).
    *   **Check DOWN Button**:
        *   From **Logic**, drag `if [Button 11 Pressed] then`.
            *   **Snap** below.
            *   Then:
                *   From **Variables**, drag `change [size] by [-2]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [size] < [5] then set [size] to [5]`.
                    *   **Snap** below (bounds checking).
                *   Wait for button release (debounce).
    *   **Draw Square**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED rect x:[64-size/2] y:[32-size/2] w:[size] h:[size] fill:[true]`.
            *   **Snap** below (centered square).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico initializes the OLED and sets the square size to 10 pixels. In the main loop, it checks if the UP button is pressed. If yes, it increases size by 2 pixels (capped at maximum 50 to prevent drawing off-screen). If the DOWN button is pressed, it decreases size by 2 pixels (minimum 5 to keep visible). After checking buttons, it clears the display, calculates the square's center position (64-size/2, 32-size/2 on a 128×64 screen), draws a filled rectangle of the current size, and shows it. The 0.05s delay makes size changes smooth and responsive to button presses.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

btn_up = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_down = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

size = 10

while True:
    if btn_up.value():
        size = min(50, size + 2)
        while btn_up.value():
            time.sleep(0.01)
    
    if btn_down.value():
        size = max(5, size - 2)
        while btn_down.value():
            time.sleep(0.01)
    
    oled.fill(0)
    x = 64 - size // 2
    y = 32 - size // 2
    oled.fill_rect(x, y, size, size, 1)
    oled.show()
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Square Off-Center**: If the square doesn't stay centered, verify centering math: x = (screen_width/2) - (size/2) = 64 - size/2.
*   **No Bounds Checking**: If size goes negative or exceeds screen, add min/max limits (5-50 pixels).
*   **Size Changes Too Fast**: If one button press changes size dramatically, your debounce is missing or insufficient.
*   **Flickering**: If display flickers, ensure `clear` → `draw` → `show` happens in correct order every loop.

### 1️⃣2️⃣ Try This Next

*   **Circle Instead**: Use `OLED.ellipse()` or `OLED.circle()` to draw a growing/shrinking circle instead of a square.
*   **Color Fill Toggle**: Add a third button that toggles between filled and outline-only rectangles.
*   **Aspect Ratio**: Make UP change width and DOWN change height separately for non-square rectangles.

---

## 1️⃣ Project 0314: Animation Sequences

### 2️⃣ Learning Objective
Create a multi-frame animation sequence depicting a rocket launch. You will learn how to structure frame-by-frame animation with distinct visual states and timing to tell a visual story.

### 3️⃣ Concepts Introduced
*   **Keyframe Animation**: Defining distinct visual moments in a sequence.
*   **Position Interpolation**: Moving an object across frames.
*   **Sequence Timing**: Varying frame durations for dramatic effect.
*   **Text Overlays**: Combining graphics with text annotations.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup I2C OLED**
*   **Category:** Displays
*   **Block:** `Setup OLED I2C:[0] width:[128] height:[64]`

🔹 **OLED Shapes**
*   **Category:** Displays
*   **Block:** `OLED rect`, `OLED line`, `OLED triangle`

🔹 **OLED Text**
*   **Category:** Displays
*   **Block:** `OLED text:[text] x:[X] y:[Y]`

🔹 **For Loop**
*   **Category:** Loops
*   **Block:** `for [i] from [0] to [N]`

### 7️⃣ Variables & State
*   **rocketY**: Vertical position of rocket (starts at 50, moves to -10).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Animate Rocket Launch**:
        *   From **Loops**, drag `for [rocketY] from [50] to [-10] step [-6]`.
            *   **Snap** into loop (10 frames total).
            *   Inside loop:
                *   From **Displays**, drag `OLED clear`.
                *   Draw ground: `OLED line x1:[0] y1:[60] x2:[128] y2:[60]`.
                *   Draw rocket (simple triangle):
                    *   `OLED triangle x1:[60] y1:[rocketY] x2:[54] y2:[rocketY+10] x3:[66] y2:[rocketY+10]`.
                *   From **Displays**, drag `OLED show`.
                *   From **Timing**, drag `sleep [0.2] seconds`.
    *   **Show "Liftoff!" Text**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text:[Liftoff!] x:[30] y:[28]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [2] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico initializes the OLED. In the main loop, it starts a for-loop with `rocketY` ranging from 50 (bottom of screen) to -10 (off-screen top) in steps of -6, creating 10 frames. Each frame: clears the screen, draws a horizontal line representing ground at y=60, draws a simple triangle rocket at position (60, rocketY), shows the frame, and waits 0.2 seconds. As rocketY decreases each iteration, the rocket moves upward. After the loop completes (rocket off-screen), the display clears, shows "Liftoff!" text for 2 seconds, then the sequence repeats, creating a continuous launch animation.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Animate rocket launch (10 frames)
    for rocketY in range(50, -10, -6):
        oled.fill(0)
        
        # Draw ground
        oled.line(0, 60, 128, 60, 1)
        
        # Draw rocket (simple triangle)
        oled.fill_triangle(60, rocketY, 54, rocketY+10, 66, rocketY+10, 1)
        
        oled.show()
        time.sleep(0.2)
    
    # Show liftoff message
    oled.fill(0)
    oled.text('Liftoff!', 30, 28)
    oled.show()
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Rocket Doesn't Move**: If rocket stays stationary, verify the for-loop range and step are correct (should decrement Y to move upward).
*   **No Ground Line**: If ground is missing, check `line()` coordinates match screen dimensions (0 to 128 for x-axis).
*   **Triangle Not Visible**: Some OLED libraries don't have `fill_triangle()`. Use `polygon()` or draw the rocket as a filled rectangle instead.
*   **Too Fast/Slow**: Adjust frame count (loop step) or sleep time to control animation speed.

### 1️⃣2️⃣ Try This Next

*   **Smoke Trail**: Add small pixels or circles below the rocket to simulate exhaust.
*   **Countdown**: Show "3... 2... 1..." text frames before the rocket launches.
*   **Variable Speed**: Start rocket slow, then accelerate by decreasing sleep time each frame.

---

[CONTINUING WITH 3 MORE PROJECTS...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(projects_0313_0317)

print("✅ Projects 0313-0314 appended")
print("⏳ Generating Projects 0315-0317...")
