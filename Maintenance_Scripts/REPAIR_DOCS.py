import os
import re

def restore_pristine_51_52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # 0501-0510 (Batch 51)
    # 0511-0520 (Batch 52)
    
    # I have the content from previous steps, I will now assemble it with EXACT regularity.
    
    header = "#  Pico 2500: Documentation (Projects 0501-0600)\\n\\n---\\n"
    
    batch51_title = "\\n#  Batch 51: Digital Art 3\\n"
    batch52_title = "\\n#  Batch 52: Digital Art 3 (cont.)\\n"
    
    # Projects 0501-0520 content (Highly detailed Section 8)
    # I will generate these programmatically to ensure precision.
    
    projects = {}
    
    # 0501: Introduction to Digital Art
    projects[501] = """
## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create an RGB strobe effect with precise timing control to understand rapid output switching and the Persistence of Vision.

### 3. Concepts Introduced
*   Strobe Effect (POV)
*   RGB Color Mixing (White = R+G+B)
*   Precise Millisecond Timing
*   Simultaneous Pin Control

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED, 3x 220Ω Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Channel** | GP16 | - |
| **Green Channel** | GP17 | - |
| **Blue Channel** | GP18 | - |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Loops, drag `pico_forever`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep IO**:
    *   From **Smart IO**, drag `pico_gpio_write` for GP16, 17, 18.
    *   **Snap** into `start` block. Set to LOW.

**B. Main Loop Phase**
1.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Flash ON (White)**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
    *   **Snap** into loop. Set all to HIGH.
3.  **Wait**:
    *   From **Time**, drag `pico_wait` (0.05s).
    *   **Snap** below writes.
4.  **Flash OFF**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
    *   **Snap** below wait. Set all to LOW.
5.  **Wait**:
    *   From **Time**, drag `pico_wait` (0.1s).
    *   **Snap** below writes.

### 9. Execution Flow
1.  **Start**: Pins 16, 17, 18 are set as outputs.
2.  **Output**: All three LEDs turn on at once (White).
3.  **Delay**: 50ms pulse.
4.  **Repeat**: Rapid cycle creates strobe.

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in [16,17,18]]
while True:
    for l in leds: l.on()
    time.sleep(0.05)
    for l in leds: l.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Resistors**: LEDs may burn out.

### 12. Try This Next
*   **Color Chaser**: Strobe only Red, then only Green, then only Blue.
"""

    # 0502: Blinking Digital Art
    projects[502] = """
## 2. Project 0502: Blinking Digital Art

### 2. Learning Objective
Create a secondary color blinker that alternates between Yellow (R+G) and Cyan (G+B).

### 3. Concepts Introduced
*   Color Combination Logic
*   State Alternation
*   Variable-driven Branching

### 4. Hardware Required
*   Raspberry Pi Pico, RGB LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red** | GP16 | - |
| **Green** | GP17 | - |
| **Blue** | GP18 | - |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **is_yellow**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set State**:
    *   From **Variables**, set `is_yellow` to TRUE.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Branch**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Logic**, drag `if_else`.
    *   **Snap** into loop.
    *   Condition: If `is_yellow` is TRUE.
2.  **Yellow**: Set GP16=HIGH, GP17=HIGH, GP18=LOW.
3.  **Cyan**: Set GP16=LOW, GP17=HIGH, GP18=HIGH.
4.  **Cycle**: Wait 0.5s. Set `is_yellow` to NOT `is_yellow`.

### 9. Execution Flow
1.  **Start**: Flag is true.
2.  **Process**: R+G turns on (Yellow).
3.  **Repeat**: Flag becomes false, G+B turns on (Cyan).

### 10. Generated Code
```python
import machine, time
r,g,b = machine.Pin(16,machine.Pin.OUT), machine.Pin(17,machine.Pin.OUT), machine.Pin(18,machine.Pin.OUT)
y = True
while True:
    if y: r.on(); g.on(); b.off()
    else: r.off(); g.on(); b.on()
    time.sleep(0.5); y = not y
```

### 11. Common Mistakes
*   **Logic Overlap**: Both R and B on at once (Magenta) if not explicitly set to LOW.

### 12. Try This Next
*   **Add Magenta**: Cycle Yellow -> Cyan -> Magenta.
"""

    # 0503: Manual Control
    projects[503] = """
## 3. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Control the intensity of the Blue channel using a potentiometer.

### 3. Concepts Introduced
*   Analog-to-Digital Conversion (ADC)
*   Pulse Width Modulation (PWM) duty cycles

### 4. Hardware Required
*   Pico, RGB LED, 10k Pot

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pot** | GP26 (ADC) | - |
| **Blue LED** | GP18 (PWM) | - |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **val**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep PWM**:
    *   `pico_pwm_write` (GP18). Set to 0.

**B. Main Loop Phase**
1.  **Read Knob**:
    *   `val = pico_adc_read` (GP26).
2.  **Apply Intensity**:
    *   `pico_pwm_write` (GP18, Value: `val`).
    *   **Snap** into `pico_forever`.
3.  **Wait**: 0.01s.

### 9. Execution Flow
1.  **Input**: Read 16-bit analog value.
2.  **Output**: Push same value into 16-bit PWM duty cycle.

### 10. Generated Code
```python
import machine, time
pot = machine.ADC(26); led = machine.PWM(machine.Pin(18))
while True: led.duty_u16(pot.read_u16()); time.sleep(0.01)
```

### 11. Common Mistakes
*   **Pin Type**: Using Pin.OUT instead of PWM.

### 12. Try This Next
*   **Reverse Logic**: Brightest when knob is at zero.
"""

    # 0511: Intro to Animation
    projects[511] = """
## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Launch countdown 3-2-1 on OLED.

### 3. Concepts Introduced
*   Frame Buffer
*   I2C Display Control

### 4. Hardware Required
*   Pico, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | - |
| **OLED SCL** | GP9 | - |

### 6. Blocks Used
*   **pico_oled_clear**, **pico_oled_text**, **pico_oled_show**

### 7. Variables
*   **None**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init OLED**:
    *   `pico_oled_init` (GP8, GP9).

**B. Main Loop Phase**
1.  **Sequence**:
    *   `oled_clear`. `oled_text`("3", 60, 25). `oled_show`. Wait 1s.
    *   Repeat for "2" and "1".

### 9. Execution Flow
1.  **Cycle**: Clear -> Draw -> Show -> Delay.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for n in ["3","2","1"]: oled.fill(0); oled.text(n, 60, 25); oled.show(); time.sleep(1)
```

### 11. Common Mistakes
*   **Missing Show**: Text exists in memory only.

### 12. Try This Next
*   **Blast Off**: Add "BLAST OFF!" at end.
"""

    # 0512: Blinking Animation
    projects[512] = """
## 2. Project 0512: Blinking Animation

### 2. Learning Objective
Winking face animation.

### 3. Concepts Introduced
*   Frame Swapping
*   Geometric Primatives (Circle vs Line)

### 4. Hardware Required
*   Pico, OLED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: `pico_oled_init`.

**B. Main Loop Phase**
1.  **Open Eyes**:
    *   `clear`. `circle`(40,25,5). `circle`(80,25,5). `show`. Wait 2s.
2.  **Wink**:
    *   `clear`. `circle`(40,25,5). `line`(75,25,85,25). `show`. Wait 0.5s.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.circle(40,25,5,1); oled.circle(80,25,5,1); oled.show(); time.sleep(2)
    oled.fill(0); oled.circle(40,25,5,1); oled.line(75, 25, 85, 25, 1); oled.show(); time.sleep(0.5)
```
"""

    # 0513: Manual Animation
    projects[513] = """
## 3. Project 0513: Manual Animation Control

### 2. Learning Objective
Digital Etch-a-Sketch with two pots.

### 3. Concepts Introduced
*   Persistent Pixels
*   ADC-to-XY Mapping

### 4. Hardware Required
*   Pico, OLED, 2x Pot

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start**: `clear` once.

**B. Main Loop Phase**
1.  **Read**: `x = map(adc(26), 0-65535, 0-127)`. `y = map(adc(27), 0-65535, 0-63)`.
2.  **Draw**: `pico_oled_pixel`(x, y). `show`. Wait 0.01s.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
px = machine.ADC(26); py = machine.ADC(27)
oled.fill(0); oled.show()
while True:
    oled.pixel(int(px.read_u16()*127/65535), int(py.read_u16()*63/65535), 1); oled.show(); time.sleep(0.01)
```
"""

    # Assembly logic...
    # I will replace the first part of the file (until Batch 53 starts).
    
    with open(target_file, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Find where Batch 53 starts
    split_point = full_content.find("#  Batch 53:")
    if split_point == -1:
        split_point = full_content.find("# Batch 53:") # Try without extra spaces
        
    remaining_content = full_content[split_point:]

    # Build new head
    new_head = header + batch51_title
    for i in range(501, 511):
        if i in projects:
            new_head += projects[i] + "\\n---\\n"
        else:
            # Placeholder for others in batch 51 (I'll need to fetch these or generate them)
            # To be safe, I'll only replace the ones I have PERFECT content for now.
            pass
            
    # This approach is risky if I don't have all 100 ready to go in one script.
    # Instead, I'll use multi_replace to fix the broken spots.

if __name__ == "__main__":
    # Actually, I'll use a simpler script to just RE-INSERT the missing headers 
    # and their corresponding Section 8s into the existing file.
    pass
