import os

def expand_batches_51_52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Pre-defined expanded sections for Batches 51 and 52
    
    p0501 = """
## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create an RGB strobe effect with precise timing control (flash ON for 50ms, OFF for 100ms) to understand rapid output switching and the Persistence of Vision.

### 3. Concepts Introduced
*   Strobe Effect (Persistence of Vision)
*   RGB Color Mixing (White = R+G+B)
*   Precise Millisecond Timing
*   Simultaneous Digital Output

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x 220Ω Resistors
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Channel** | GP16 | via 220Ω Resistor |
| **Green Channel** | GP17 | via 220Ω Resistor |
| **Blue Channel** | GP18 | via 220Ω Resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (Set pin state)
*   **from Loops, drag `pico_forever`** (Repeat logic)
*   **from Time, drag `pico_wait`** (Control duration)

### 7. Variables
*   **None**: Direct pin control project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks for GP16, GP17, and GP18.
    *   **Snap** into `start` block.
    *   Set all to **LOW**.

**B. Main Loop Phase**
1.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Turn ON (White)**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16).
    *   **Snap** into loop. Set to HIGH.
    *   From **Smart IO**, drag `pico_gpio_write` (GP17).
    *   **Snap** below GP16. Set to HIGH.
    *   From **Smart IO**, drag `pico_gpio_write` (GP18).
    *   **Snap** below GP17. Set to HIGH.
3.  **Hold Flash**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below writes.
    *   Set value to 0.05 seconds.
4.  **Turn OFF**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
    *   **Snap** below wait.
    *   Set all to **LOW**.
5.  **Hold Darkness**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below writes.
    *   Set value to 0.1 seconds.

### 9. Execution Flow
1.  **Start**: The Pico configures pins 16, 17, and 18 as digital outputs.
2.  **Output**: All three channels turn on simultaneously, producing White light.
3.  **Delay**: The system pauses for 50ms, allowing the eye to register the flash.
4.  **Output**: All channels turn off.
5.  **Delay**: System pauses for 100ms.
6.  **Repeat**: The process repeats, creating a rapid strobe effect.

### 10. Generated Code
```python
from machine import Pin
import time

r = Pin(16, Pin.OUT); g = Pin(17, Pin.OUT); b = Pin(18, Pin.OUT)

while True:
    r.on(); g.on(); b.on()
    time.sleep(0.05)
    r.off(); g.off(); b.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Pin Mismatch**: Connecting to GP0-2 while the code expects GP16-18.
*   **Missing Resistors**: Connecting directly to 3.3V can burn out the RGB LED.

### 12. Try This Next
*   **Colored Strobe**: Alternate only Red and Blue at high speed.
"""

    p0502 = """
---

## 2. Project 0502: Blinking Digital Art

### 2. Learning Objective
Programm a "Secondary Color" blinker that alternates between Yellow (R+G) and Cyan (G+B) to understand additive color mixing in logic.

### 3. Concepts Introduced
*   Secondary Color Theory
*   Conditional Logic Patterns
*   State Alternation
*   Channel Masking

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Channel** | GP16 | - |
| **Green Channel**| GP17 | - |
| **Blue Channel** | GP18 | - |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **is_yellow**: Boolean (State toggle)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   From **Variables**, set `is_yellow` to TRUE.
    *   **Snap** into `start` block.

**B. Main Loop Phase**
1.  **Branch Logic**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Logic**, drag `if_else`.
    *   **Snap** into loop.
    *   **Condition**: If `is_yellow` is TRUE.
2.  **Display Yellow**:
    *   From **Smart IO**, set GP16=HIGH, GP17=HIGH, GP18=LOW.
    *   **Snap** into "do" part.
3.  **Display Cyan**:
    *   From **Smart IO**, set GP16=LOW, GP17=HIGH, GP18=HIGH.
    *   **Snap** into "else" part.
4.  **Hold Color**:
    *   From **Time**, drag `pico_wait` (0.5s).
    *   **Snap** below `if_else`.
5.  **Toggle State**:
    *   From **Variables**, set `is_yellow` to **Logic** NOT `is_yellow`.
    *   **Snap** below wait.

### 9. Execution Flow
1.  **Start**: System sets the internal flag to TRUE (Yellow mode).
2.  **Decide**: The loop checks the flag.
3.  **Output**: Since it's true, Red and Green turn on (Yellow).
4.  **Process**: After a pause, the flag is flipped to FALSE.
5.  **Repeat**: The next loop iteration sees FALSE and activates Green and Blue (Cyan).

### 10. Generated Code
```python
from machine import Pin
import time

r, g, b = Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)
is_yellow = True

while True:
    if is_yellow:
        r.on(); g.on(); b.off()
    else:
        r.off(); g.on(); b.on()
    
    time.sleep(0.5)
    is_yellow = not is_yellow
```

### 11. Common Mistakes
*   **No Toggle**: Forgetting to update the `is_yellow` variable, resulting in only one color.

### 12. Try This Next
*   **Magenta ADD**: Add a third state for Magenta (R+B).
"""

    p0503 = """
---

## 3. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Control the intensity of the Blue channel in an RGB LED by mapping an analog potentiometer's value to a PWM duty cycle.

### 3. Concepts Introduced
*   Analog-to-PWM Mapping
*   Duty Cycle Resolution
*   Optical Intensity Control
*   Real-time Feedback loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   10kΩ Potentiometer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Blue Pin** | GP18 | PWM Enabled |
| **Control Knob**| GP26 (ADC) | Intensity Input |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Smart IO, drag `pico_pwm_write`**
*   **from Math, drag `map_range`**

### 7. Variables
*   **knob_pos**: Integer (Raw ADC reading)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, drag `pico_pwm_write` Pin GP18.
    *   **Snap** into `start` block.
    *   Set Value to 0.

**B. Main Loop Phase**
1.  **Sense Input**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Read Knob**:
    *   From **Variables**, set `knob_pos` to **Smart IO** `pico_adc_read` GP26.
    *   **Snap** into loop.
3.  **Drive LED**:
    *   From **Smart IO**, drag `pico_pwm_write` GP18.
    *   **Snap** below read.
    *   Set Value to variable `knob_pos`.
4.  **Wait**:
    *   From **Time**, drag `pico_wait` (0.01s) for stability.

### 9. Execution Flow
1.  **Start**: System sets the LED brightness to zero.
2.  **Input**: Every 10ms, the Pico reads the exact rotation of the knob.
3.  **Process**: The system uses that 16-bit number directly as the PWM duty cycle.
4.  **Output**: The LED brightness changes instantly as you turn the knob.

### 10. Generated Code
```python
import machine, time
pot = machine.ADC(26)
blue = machine.PWM(machine.Pin(18)); blue.freq(1000)

while True:
    blue.duty_u16(pot.read_u16())
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Wrong Pin Type**: Using digital_write instead of pwm_write, which doesn't support dimming.

### 12. Try This Next
*   **Reversed Dimming**: Use a math block to subtract the knob value from 65535.
"""

    p0511 = """
---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Create a visual "Launch Countdown" by sequencing numbers 3, 2, and 1 on the OLED display with 1-second intervals.

### 3. Concepts Introduced
*   Visual Pacing
*   Frame Clearing (Buffer management)
*   I2C Communication
*   Numeric-to-String Rendering

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |
| **OLED SCL** | GP9 | I2C Clock |

### 6. Blocks Used
*   **from Display, drag `pico_oled_clear`**
*   **from Display, drag `pico_oled_text`**
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **None**: Static sequence project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure OLED**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Snap** into `start` block.

**B. Main Loop Phase**
1.  **Create Sequence**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Show "3"**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Snap** into loop.
    *   From **Display**, drag `pico_oled_text`.
    *   **Snap** below clear. Set to "3", X=60, Y=25.
    *   From **Display**, drag `pico_oled_show`.
    *   **Snap** below text.
3.  **Hold**:
    *   From **Time**, wait 1.0s.
    *   **Snap** below show.
4.  **Show "2"**:
    *   Repeat Clear, Text ("2"), Show.
    *   Wait 1.0s.
5.  **Show "1"**:
    *   Repeat Clear, Text ("1"), Show.
    *   Wait 1.0s.

### 9. Execution Flow
1.  **Start**: The Pico initializes the I2C bus and clear the screen.
2.  **Output**: The screen clears, draws "3", and pushes it to the display.
3.  **Delay**: System pauses for 1 second.
4.  **Repeat**: The process repeats for "2" and "1", then restarts at "3".

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for n in ["3", "2", "1"]:
        oled.fill(0); oled.text(n, 60, 25); oled.show()
        time.sleep(1)
```

### 11. Common Mistakes
*   **Double Drawing**: Not clearing the screen between numbers, causing them to overlap.

### 12. Try This Next
*   **Add "Liftoff!"**: Show a final frame with the word "LIFTOFF".
"""

    p0512 = """
---

## 2. Project 0512: Blinking Animation

### 2. Learning Objective
Animate a "Winking Face" by toggling between drawing a full circle for an eye and a single line for a closed eyelid.

### 3. Concepts Introduced
*   Frame-by-Frame Animation
*   Symbolic Shapes
*   Persistence of Vision
*   Graphic Sync

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | - |

### 6. Blocks Used
*   **from Display, drag `pico_oled_circle`**
*   **from Display, drag `pico_oled_line`**
*   **from Display, drag `pico_oled_show`**

### 7. Variables
*   **None**: Frame-based project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset OLED**:
    *   From **Display**, drag `pico_oled_clear`.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Frame 1 (Open Eye)**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Display**, clear screen.
    *   Draw Left Eye (Circle), Mouth (Line).
    *   Draw Right Eye: `pico_oled_circle` X=80, Y=25, R=5.
    *   `show`. Wait 2.0s.
2.  **Frame 2 (Wink)**:
    *   Clear screen.
    *   Redraw Static parts.
    *   Draw Right Eye (Closed): `pico_oled_line` X1=75, Y1=25, X2=85, Y2=25.
    *   `show`. Wait 0.5s.

### 9. Execution Flow
1.  **Start**: Screen is prepared.
2.  **Output**: Face with two open eyes appears for 2 seconds.
3.  **Process**: Right eye circle is replaced by a flat line.
4.  **Reaction**: User perceives a slow, intentional wink.
5.  **Repeat**: Cycle continues.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Frame 1
    oled.fill(0); oled.circle(40, 25, 5, 1); oled.circle(80, 25, 5, 1); oled.show()
    time.sleep(2)
    # Frame 2
    oled.fill(0); oled.circle(40, 25, 5, 1); oled.line(75, 25, 85, 25, 1); oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Eye Mismatch**: Placing the wink line higher or lower than the center of the original eye.

### 12. Try This Next
*   **Both Eyes**: Make both eyes blink simultaneously.
"""

    p0513 = """
---

## 3. Project 0513: Manual Animation Control

### 2. Learning Objective
Programm a "Digital Canvas" (Etch-a-Sketch) where two knobs control the drawing of persistent lines on the OLED display.

### 3. Concepts Introduced
*   Coordinate Mapping
*   Pixel Persistence (Avoiding clears)
*   ADC-to-XY Conversion
*   User Interaction

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   2x Potentiometers

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **X-Knob** | GP26 (ADC) | Horizontal |
| **Y-Knob** | GP27 (ADC) | Vertical |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Display, drag `pico_oled_pixel`**
*   **from Math, drag `map_range`**

### 7. Variables
*   **cur_x, cur_y**: Integer (Screen coords)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Startup**:
    *   From **Display**, clear screen ONCE at `start`.
    *   **Snap** `pico_oled_show`.

**B. Main Loop Phase**
1.  **Read Knobs**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Variables**, set `cur_x` to map `pico_adc_read` 26 (0-127).
    *   From **Variables**, set `cur_y` to map `pico_adc_read` 27 (0-63).
2.  **Draw Point**:
    *   From **Display**, drag `pico_oled_pixel` at X=`cur_x`, Y=`cur_y`.
    *   **Snap** into loop.
3.  **Push to Screen**:
    *   From **Display**, drag `pico_oled_show`.
    *   **Snap** below pixel.
4.  **Wait**:
    *   Small pause (0.01s).

### 9. Execution Flow
1.  **Start**: Screen is clear.
2.  **Input**: Pico calculates the knob positions as screen coordinates.
3.  **Output**: A single white dot appears at that location.
4.  **Process**: Because there is NO "clear" block in the loop, old dots stay on screen.
5.  **Result**: Moving the knobs draws a continuous line on the display.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
px = machine.ADC(26); py = machine.ADC(27)

oled.fill(0); oled.show()
while True:
    x = int(px.read_u16() * 127 / 65535)
    y = int(py.read_u16() * 63 / 65535)
    oled.pixel(x, y, 1); oled.show()
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Clearing Screen**: If you put 'pico_oled_clear' inside the loop, the line will disappear as you draw.

### 12. Try This Next
*   **Thickness**: Use 'pico_oled_circle' with Radius 2 instead of a single pixel for a fat pen.
"""

    # ... and so on for 0514-0520. For now I'll just append these Rebuilt versions to the file.
    # I will focus on replacing the first 50 lines which contain Batches 51/52.
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will replace Projects 0501, 0502, 0503, 0511, 0512, 0513 with the Elite versions.
    # Note: I have already expanded 0517 directly using replace_file_content earlier.
    
    import re
    content = re.sub(r'## 1\. Project 0501:.*?---', p0501 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 1\. Project 0502:.*?---', p0502 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 1\. Project 0503:.*?---', p0503 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 1\. Project 0511:.*?---', p0511 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 1\. Project 0512:.*?---', p0512 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 1\. Project 0513:.*?---', p0513 + "\n---", content, flags=re.DOTALL)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    expand_batches_51_52()
