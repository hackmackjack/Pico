#!/usr/bin/env python3
"""
BATCH 51 CUSTOM GENERATOR (Projects 0501-0510)
Each project custom-made based on its specific problem statement
"""

output = '''# 📚 Pico 2500: Elite Documentation (Projects 0501-0600)

**Standard**: Elite Documentation Standard v2.0  
**Projects**: 100 (0501-0600) - Custom Content Per Project

---

# 🎨 Batch 51: Digital Art 3

---

## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create RGB strobe effect with precise timing control (white flash 50ms, off 100ms).

### 3. Concepts Introduced
*   **Strobe Effect**: Rapid high-contrast flashing
*   **RGB LED Control**: Simultaneous channel activation  
*   **Precise Timing**: 50ms ON, 100ms OFF cycles

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | 220Ω resistor |
| **Green LED** | GP17 | 220Ω resistor |
| **Blue LED** | GP18 | 220Ω resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (control RGB channels)
*   **from Time, drag `pico_wait`** (0.05s, 0.1s timing)
*   **from Loops, drag `pico_forever`** (continuous loop)

### 7. Variables
*   None (direct timing control)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure RGB Pins**:
    *   From **Smart IO**, drag pin configuration blocks.
        *   **Snap** into setup.
        *   Set GP16, GP17, GP18 as outputs.

**B. Main Loop Phase**
2.  **Turn All ON (White)**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks.
        *   **Snap** into loop.
        *   Set R=HIGH, G=HIGH, B=HIGH.
3.  **Flash Duration**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 0.05 seconds (50ms).
4.  **Turn All OFF**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks.
        *   **Snap** below.
        *   Set R=LOW, G=LOW, B=LOW.
5.  **Off Duration**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 0.1 seconds (100ms).

### 9. Execution Flow
System creates white flash (all RGB HIGH) for 50ms, then turns all OFF for 100ms. This rapid cycle creates strobe effect. **Warning**: May trigger photosensitivity.

### 10. Generated Code
```python
import machine, time

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

while True:
    # White flash
    red.on(); green.on(); blue.on()
    time.sleep(0.05)
    
    # Off
    red.off(); green.off(); blue.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   Wrong timing (must be exactly 0.05s/0.1s)
*   Missing resistors for RGB LED
*   Not adding photosensitivity warning

### 12. Try This Next
*   Add potentiometer to control flash rate
*   Different color strobes (not just white)
*   Add pause/resume button

---

## 1. Project 0502: Blinking Digital Art

### 2. Learning Objective
Cycle through CMY colors (Yellow→Cyan→Magenta) using RGB LED.

### 3. Concepts Introduced
*   **CMY Color Model**: Cyan, Magenta, Yellow
*   **Color Mixing**: Y(R+G), C(G+B), M(R+B)
*   **Sequential Display**: Cycling through colors

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | 220Ω resistor |
| **Green LED** | GP17 | 220Ω resistor |
| **Blue LED** | GP18 | 220Ω resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (RGB control)
*   **from Time, drag `pico_wait`** (color timing)
*   **from Loops, drag `pico_forever`** (cycle)

### 7. Variables
*   None (sequential color display)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure RGB**:
    *   From **Smart IO**, drag pin configs.
        *   **Snap** into setup.
        *   Set GP16-18 as outputs.

**B. Main Loop Phase**
2.  **Yellow (R+G)**:
    *   From **Smart IO**, drag gpio_write.
        *   **Snap** into loop.
        *   R=HIGH, G=HIGH, B=LOW.
    *   From **Time**, wait 1s.
3.  **Cyan (G+B)**:
    *   From **Smart IO**, drag gpio_write.
        *   **Snap** below.
        *   R=LOW, G=HIGH, B=HIGH.
    *   From **Time**, wait 1s.
4.  **Magenta (R+B)**:
    *   From **Smart IO**, drag gpio_write.
        *   **Snap** below.
        *   R=HIGH, G=LOW, B=HIGH.
    *   From **Time**, wait 1s.

### 9. Execution Flow
System cycles: Yellow(R+G) 1s → Cyan(G+B) 1s → Magenta(R+B) 1s, then repeats. Demonstrates CMY secondary colors using RGB additive mixing.

### 10. Generated Code
```python
import machine, time

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

while True:
    # Yellow
    red.on(); green.on(); blue.off()
    time.sleep(1)
    
    # Cyan
    red.off(); green.on(); blue.on()
    time.sleep(1)
    
    # Magenta
    red.on(); green.off(); blue.on()
    time.sleep(1)
```

### 11. Common Mistakes
*   Wrong combinations (Yellow is R+G, not R+B)
*   Timing too fast to see colors
*   Forgetting to turn OFF unused channels

### 12. Try This Next
*   Add RGB primaries to cycle
*   Smooth PWM fades between colors
*   Reverse direction button

---

## 1. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Build interactive color mixer with 3 buttons controlling R, G, B independently.

### 3. Concepts Introduced
*   **Toggle Logic**: Button flips state ON/OFF
*   **Additive Synthesis**: Combine R, G, B for 8 colors
*   **Independent Control**: Each channel separate

### 4. Hardware Required
Pico, 3 Buttons, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button 1 (Red)** | GP13 | PULL_DOWN |
| **Button 2 (Green)** | GP14 | PULL_DOWN |
| **Button 3 (Blue)** | GP15 | PULL_DOWN |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read buttons)
*   **from Smart IO, drag `pico_gpio_write`** (control RGB)
*   **from Logic, drag `if_compare`** (detect press)
*   **from Variables, drag `variables_set`** (store states)
*   **from Logic, drag `logic_negate`** (NOT for toggle)

### 7. Variables
*   **redState**, **greenState**, **blueState**: Boolean states

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Buttons**:
    *   From **Smart IO**, drag pin configs.
        *   **Snap** into setup.
        *   GP13-15 as inputs with PULL_DOWN.
2.  **Configure RGB**:
    *   From **Smart IO**, drag pin configs.
        *   **Snap** below.
        *   GP16-18 as outputs.
3.  **Initialize States**:
    *   From **Variables**, drag init.
        *   **Snap** below.
        *   All states = FALSE.

**B. Main Loop Phase**
4.  **Check Button 1**:
    *   From **Smart IO**, read GP13.
        *   **Snap** into loop.
    *   From **Logic**, if pressed:
        *   Toggle redState with NOT.
        *   Wait for release.
5.  **Check Button 2**:
    *   From **Smart IO**, read GP14.
        *   **Snap** below.
    *   From **Logic**, if pressed:
        *   Toggle greenState.
        *   Wait for release.
6.  **Check Button 3**:
    *   From **Smart IO**, read GP15.
        *   **Snap** below.
    *   From **Logic**, if pressed:
        *   Toggle blueState.
        *   Wait for release.
7.  **Update Outputs**:
    *   From **Smart IO**, write states to RGB.

### 9. Execution Flow
Each button toggles its color channel ON/OFF. Combine buttons to create any of 8 basic colors: Black(000), R(100), G(010), B(001), Y(110), C(011), M(101), W(111).

### 10. Generated Code
```python
import machine, time

btn_r = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_g = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

r_state, g_state, b_state = False, False, False

while True:
    if btn_r.value():
        r_state = not r_state
        while btn_r.value(): time.sleep(0.01)
    if btn_g.value():
        g_state = not g_state
        while btn_g.value(): time.sleep(0.01)
    if btn_b.value():
        b_state = not b_state
        while btn_b.value(): time.sleep(0.01)
    
    red.value(r_state)
    green.value(g_state)
    blue.value(b_state)
    time.sleep(0.05)
```

### 11. Common Mistakes
*   Missing debounce (multiple toggles per press)
*   Wrong toggle logic (set TRUE instead of NOT)
*   No pull resistors on buttons

### 12. Try This Next
*   Reset button for all OFF
*   Display color name on OLED
*   PWM for brightness control

---

'''

# Continue with remaining 7 projects (0504-0510)...
print("Generating Batch 51: Projects 0501-0510")
print("Projects 0501-0503 complete...")
print("Continuing with 0504-0510...")

# Write what we have so far
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(output)

print("✓ First 3 projects written")
print("Next: Projects 0504-0510")
