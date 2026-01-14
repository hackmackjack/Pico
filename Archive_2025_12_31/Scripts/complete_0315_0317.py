# Complete Projects 0315-0317

final_three = '''
## 1️⃣ Project 0315: Interactive Animation

### 2️⃣ Learning Objective
Map analog input from a potentiometer to control the Y-axis position of a graphical object on the OLED. You will learn real-time analog-to-visual coordinate mapping for interactive graphics.

### 3️⃣ Concepts Introduced
*   **Analog-to-Coordinate Mapping**: Converting ADC values (0-65535) to screen coordinates (0-64).
*   **Real-Time Graphics**: Updating display based on continuous sensor input.
*   **Paddle Mechanic**: Fundamental game controller element.

### 4️⃣ Hardware Required
*   **Pico**
*   **Potentiometer** (10kΩ recommended)
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Center pin to ADC, outer to 3.3V/GND |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup ADC**
*   **Category:** Inputs
*   **Block:** `Setup ADC pin:[26]`

🔹 **Read Analog**
*   **Category:** Pin Access
*   **Block:** `read Analog pin [26]`

🔹 **Map Range**
*   **Category:** Math
*   **Block:** `map [value] from [0]-[65535] to [0]-[54]`

🔹 **OLED Line**
*   **Category:** Displays
*   **Block:** `OLED line x1:[X1] y1:[Y1] x2:[X2] y2:[Y2]`

### 7️⃣ Variables & State
*   **potValue**: Raw ADC reading (0-65535).
*   **paddleY**: Mapped Y-coordinate (0-54, allowing 10-pixel paddle height).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup ADC pin:[26]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read & Map Potentiometer**:
        *   From **Variables**, drag `set [potValue] to`.
            *   **Snap** into loop.
            *   From **Pin Access**, drag `read Analog pin [26]`.
                *   **Snap** into value socket.
        *   From **Variables**, drag `set [paddleY] to`.
            *   **Snap** below.
            *   From **Math**, drag `map [potValue] from [0]-[65535] to [0]-[54]`.
                *   **Snap** into value socket.
    *   **Draw Paddle**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED line x1:[5] y1:[paddleY] x2:[5] y2:[paddleY+10]`.
            *   **Snap** below (vertical line, 10 pixels tall).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico reads the potentiometer's analog value (0-65535) and maps it to a Y-coordinate (0-54). The range 0-54 ensures the 10-pixel-tall paddle never draws off-screen (64 - 10 = 54 max Y). It clears the display, draws a vertical line from (5, paddleY) to (5, paddleY+10) representing the paddle on the left edge, and shows the result. The 0.05s delay provides smooth, responsive movement as the potentiometer is adjusted, demonstrating the core mechanic of classic Pong paddles.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

pot = machine.ADC(26)

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    potValue = pot.read_u16()
    paddleY = map_range(potValue, 0, 65535, 0, 54)
    
    oled.fill(0)
    # Draw vertical paddle line
    for y in range(paddleY, paddleY + 10):
        oled.pixel(5, y, 1)
    oled.show()
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Paddle Draws Off-Screen**: If paddle disappears at extremes, verify map output range is 0 to (screen_height - paddle_height) = 54, not 64.
*   **Jittery Movement**: If paddle jumps erratically, add capacitor (0.1µF) across potentiometer signal and ground to filter noise.
*   **Inverted Control**: If turning pot clockwise moves paddle down instead of up, swap the map output range (54-0 instead of 0-54).
*   **No Line Visible**: Some OLED libraries use `vline()` for vertical lines. Check library documentation or draw pixel-by-pixel in a loop.

### 1️⃣2️⃣ Try This Next

*   **Add Ball**: Draw a moving circle bouncing off paddle when aligned.
*   **Horizontal Paddle**: Map potentiometer to X-axis for a bottom-edge horizontal paddle.
*   **Paddle Width Control**: Use a second potentiometer to control paddle length dynamically.

---

## 1️⃣ Project 0316: Smart Animation Switch

### 2️⃣ Learning Objective
Create a directional UI using four buttons to display arrows pointing North, East, South, or West. You will learn how button input directly controls discrete visual states in a navigation-style interface.

### 3️⃣ Concepts Introduced
*   **Directional Input**: Mapping four buttons to cardinal directions.
*   **Icon Drawing**: Creating simple arrow graphics.
*   **State-to-Visual Mapping**: Translating button state to direction arrow.

### 4️⃣ Hardware Required
*   **Pico**
*   **4 Buttons** (North, East, South, West)
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button North** | GP10 | PULL_DOWN enabled |
| **Button East** | GP11 | PULL_DOWN enabled |
| **Button South** | GP12 | PULL_DOWN enabled |
| **Button West** | GP13 | PULL_DOWN enabled |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup Button (×4)**
*   **Category:** Inputs
*   **Block:** `Setup Button pin:[10/11/12/13]`

🔹 **OLED Shapes**
*   **Category:** Displays
*   **Block:** `OLED line`, `OLED triangle`

🔹 **Logic Blocks**
*   **Category:** Logic
*   **Block:** `if... elif... elif... else`

### 7️⃣ Variables & State
*   None (direction determined by current button press).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[10/11/12/13]` for each direction.
        *   **Snap** into setup block (×4).
        *   Enable PULL_DOWN for all.

*   **B. Main Loop Phase**
    *   From **Displays**, drag `OLED clear`.
        *   **Snap** into loop.
    *   **Check Buttons & Draw Arrow**:
        *   From **Logic**, drag `if [Button 10 Pressed] then`.
            *   **Snap** below.
            *   Then: Draw UP arrow (triangle pointing up at center).
        *   From **Logic**, drag `else if [Button 11 Pressed] then`.
            *   **Snap** below.
            *   Then: Draw RIGHT arrow (triangle pointing right).
        *   From **Logic**, drag `else if [Button 12 Pressed] then`.
            *   **Snap** below.
            *   Then: Draw DOWN arrow (triangle pointing down).
        *   From **Logic**, drag `else if [Button 13 Pressed] then`.
            *   **Snap** below.
            *   Then: Draw LEFT arrow (triangle pointing left).
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Then: Draw "?" or blank (no button pressed).
    *   From **Displays**, drag `OLED show`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico checks all four direction buttons each loop. If North button is pressed, it draws an upward-pointing triangle at screen center (x=60, y=20). If East, a right-pointing triangle. If South, downward. If West, leftward. If no button is pressed, the screen shows blank or a "?" symbol. This creates a simple compass interface where the displayed arrow always matches the currently pressed directional button, useful for navigation UI or directional control systems.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

btn_n = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_e = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_s = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_w = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    oled.fill(0)
    
    if btn_n.value():
        # Up arrow
        oled.fill_triangle(64, 20, 54, 40, 74, 40, 1)
    elif btn_e.value():
        # Right arrow
        oled.fill_triangle(80, 32, 60, 22, 60, 42, 1)
    elif btn_s.value():
        # Down arrow
        oled.fill_triangle(64, 44, 54, 24, 74, 24, 1)
    elif btn_w.value():
        # Left arrow
        oled.fill_triangle(48, 32, 68, 22, 68, 42, 1)
    else:
        oled.text('?', 60, 28)
    
    oled.show()
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Multiple Arrows**: If pressing one button shows multiple arrows, ensure elif (not separate if statements) so only one branch executes.
*   **No Triangle Function**: If library lacks `fill_triangle()`, use polygon or draw arrows with lines forming triangle outline.
*   **Wrong Direction**: If North shows right arrow, verify button pin assignments match problem statement (North=10, East=11, South=12, West=13).
*   **Arrows Off-Center**: Adjust triangle coordinates to ensure visual centering on 128×64 display.

### 1️⃣2️⃣ Try This Next

*   **Diagonal Arrows**: Add NE/SE/SW/NW arrows when two adjacent buttons are pressed simultaneously.
*   **Color Code**: If using color OLED, show North=blue, East=green, South=yellow, West=red for intuitive direction mapping.
*   **Animation**: Make the arrow pulse or grow/shrink while button is held.

---

## 1️⃣ Project 0317: Animation Alarm System

### 2️⃣ Learning Objective
Create an icon-based alert system that flashes when a voltage variable falls below a threshold. You will learn to combine conditional logic with icon animation for visual status alerts.

### 3️⃣ Concepts Introduced
*   **Icon Design**: Creating simple battery symbol using geometric shapes.
*   **Threshold Monitoring**: Triggering visual alert based on variable value.
*   **Flash Animation**: Alternating between icon visible/invisible states.
*   **Status Indication**: Using graphics instead of text for alerts.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306, 128×64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 (I2C0 SDA) | I2C Data |
| **OLED SCL** | GP1 (I2C0 SCL) | I2C Clock |

### 6️⃣ Blocks Used

🔹 **Setup OLED**
*   **Category:** Displays
*   **Block:** `Setup OLED I2C:[0] width:[128] height:[64]`

🔹 **OLED Shapes**
*   **Category:** Displays
*   **Block:** `OLED rect`, `OLED line`

🔹 **Logic Blocks**
*   **Category:** Logic
*   **Block:** `if [voltage] < [3.0] then`

### 7️⃣ Variables & State
*   **voltage**: Simulated battery voltage (starts at 4.2, decrements each loop).
*   **flashState**: Boolean toggling between show/hide icon.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Displays**, drag `Setup OLED I2C:[0] width:[128] height:[64]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [voltage] to [4.2]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [flashState] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Simulate Voltage Drop**:
        *   From **Variables**, drag `change [voltage] by [-0.1]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [voltage] < [2.5] then set [voltage] to [4.2]`.
            *   **Snap** below (reset for continuous demo).
    *   **Check Low Voltage & Flash**:
        *   From **Logic**, drag `if [voltage] < [3.0] then`.
            *   **Snap** below.
            *   Then:
                *   From **Variables**, drag `set [flashState] to [not flashState]`.
                    *   **Snap** inside (toggle flash).
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** below.
                *   From **Logic**, drag `if [flashState] then`.
                    *   **Snap** below.
                    *   Then: Draw battery icon (rect outline + rect fill showing empty).
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
        *   From **Logic**, drag `else`.
            *   **Snap** below (voltage OK).
            *   Then:
                *   Display current voltage value or blank screen.
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system simulates battery voltage starting at 4.2V and decreasing by 0.1V each loop. When voltage drops below 3.0V, it enters alert mode. The `flashState` boolean toggles every loop. When flashState is true and voltage is low, it draws an empty battery icon (rectangle outline with minimal fill) at screen center. When flashState is false, the screen is blank. This creates a flashing effect at 1 Hz (0.5s on, 0.5s off), drawing attention to the low battery condition. The voltage resets to 4.2V when it reaches 2.5V to demonstrate the continuous alert behavior.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306_I2C(128, 64, i2c)

voltage = 4.2
flashState = False

while True:
    # Simulate voltage drop
    voltage -= 0.1
    if voltage < 2.5:
        voltage = 4.2
    
    if voltage < 3.0:
        flashState = not flashState
        oled.fill(0)
        
        if flashState:
            # Draw empty battery icon
            oled.rect(50, 25, 28, 14, 1)  # Battery body
            oled.rect(78, 30, 3, 4, 1)    # Battery terminal
            # Empty = no fill inside
        
        oled.show()
    else:
        oled.fill(0)
        oled.text(f'V:{voltage:.1f}', 40, 28)
        oled.show()
    
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Flashing**: If icon flashes even when voltage is high, verify the `if voltage < 3.0` condition is correctly placed.
*   **No Flash**: If icon stays solid, ensure `flashState` toggles and the `if flashState then draw` logic is correct.
*   **Icon Off-Screen**: Verify battery icon coordinates fit within 128×64 display bounds. Typical centered battery: x=50, y=25, width=28, height=14.
*   **Voltage Never Drops**: If voltage stays at 4.2, ensure the decrement (`voltage -= 0.1`) executes every loop.

### 1️⃣2️⃣ Try This Next

*   **Fill Indicator**: Draw fill inside battery proportional to voltage level (full at >4.0V, empty at <3.0V).
*   **Color Alert**: If using color OLED, flash red for critical (<3.0V), yellow for warning (<3.5V), green for OK.
*   **Real Voltage**: Replace simulated voltage with actual ADC reading from battery monitoring circuit.

---
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_three)

print("✅ Projects 0315-0317 appended successfully")
print("\\n📊 Progress Update:")
print("- Batch 31 (0301-0310): ✅ Complete (10/10)")
print("- Batch 32 (0311-0317): ✅ Complete (7/10)")
print("\\nNext: Projects 0318-0320 to finish Batch 32")
