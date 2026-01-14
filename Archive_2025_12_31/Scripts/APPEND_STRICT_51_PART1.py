import os

def append_batch51_strict():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Project 0502
    p0502 = """
---

## 1. Project 0502: Blinking Digital Art

### 2. Learning Objective
Cycle through CMY colors (Yellow, Cyan, Magenta) using RGB LED color mixing logic.

### 3. Concepts Introduced
*   Color Mixing (Additive)
*   Sequential Logic
*   CMY Color Model
*   Timing Control

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x 220Ω Resistors
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | Connected via 220Ω resistor |
| **Green LED** | GP17 | Connected via 220Ω resistor |
| **Blue LED** | GP18 | Connected via 220Ω resistor |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: Direct pin control.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_gpio_write` Pin GP16, GP17, GP18.

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Show Yellow (Red + Green)**:
    *   From **Smart IO**, **Set** `pico_gpio_write` (Red) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Green) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Blue) to **LOW**.
    *   From **Time**, **Wait** 1 second.
4.  **Show Cyan (Green + Blue)**:
    *   From **Smart IO**, **Set** `pico_gpio_write` (Red) to **LOW**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Green) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Blue) to **HIGH**.
    *   From **Time**, **Wait** 1 second.
5.  **Show Magenta (Red + Blue)**:
    *   From **Smart IO**, **Set** `pico_gpio_write` (Red) to **HIGH**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Green) to **LOW**.
    *   From **Smart IO**, **Set** `pico_gpio_write` (Blue) to **HIGH**.
    *   From **Time**, **Wait** 1 second.

### 9. Execution Flow
1.  **Start**: Pico configures RGB pins.
2.  **Yellow**: Red and Green pins turn HIGH; Blue turns LOW.
3.  **Cyan**: Green and Blue pins turn HIGH; Red turns LOW.
4.  **Magenta**: Red and Blue pins turn HIGH; Green turns LOW.
5.  **Repeat**: The loop cycles indefinitely through these secondary colors.

### 10. Generated Code
```python
from machine import Pin
import time

red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)

while True:
    # Yellow
    red.on()
    green.on()
    blue.off()
    time.sleep(1)
    
    # Cyan
    red.off()
    green.on()
    blue.on()
    time.sleep(1)
    
    # Magenta
    red.on()
    green.off()
    blue.on()
    time.sleep(1)
```

### 11. Common Mistakes
*   **Color Confusion**: Remembering that Red+Green makes Yellow (additive), not Brown (subtractive).
*   **Leaving Pins High**: Forgetting to turn off the "previous" color component when switching.

### 12. Try This Next
*   **Traffic Light**: Modify the sequence to Red -> Yellow -> Green.
*   **Faster Cycle**: Reduce wait time to 0.1s.
"""

    p0503 = """
---

## 1. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Control RGB color channels independently using three push buttons (Red, Green, Blue).

### 3. Concepts Introduced
*   Digital Input (Reading Buttons)
*   Conditional Logic (If/Else)
*   State Toggling
*   Debouncing (Basic)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x Push Buttons
*   3x 220Ω Resistors (for LED)
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Red** | GP13 | Pull-Down |
| **Button Green** | GP14 | Pull-Down |
| **Button Blue** | GP15 | Pull-Down |
| **Red LED** | GP16 | 220Ω Resistor |
| **Green LED** | GP17 | 220Ω Resistor |
| **Blue LED** | GP18 | 220Ω Resistor |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`**
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Logic, drag `if_do`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **redState**: Boolean (TRUE/FALSE)
*   **greenState**: Boolean
*   **blueState**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   From **Smart IO**, **Set** GP13-15 as Input (Pull Down).
    *   From **Smart IO**, **Set** GP16-18 as Output.
2.  **Init Variables**:
    *   Create variables `redState`, `greenState`, `blueState` and set to **FALSE**.

**B. Main Loop Phase**
3.  **Check Red Button**:
    *   From **Logic**, drag `if_do`.
    *   Condition: If `pico_gpio_read` (GP13) is **HIGH**.
    *   Action: Set `redState` to **NOT** `redState`.
    *   Wait: 0.2s (Debounce).
4.  **Check Green Button**:
    *   Repeat logic for GP14 and `greenState`.
5.  **Check Blue Button**:
    *   Repeat logic for GP15 and `blueState`.
6.  **Update LEDs**:
    *   From **Smart IO**, **Set** GP16 to `redState`.
    *   From **Smart IO**, **Set** GP17 to `greenState`.
    *   From **Smart IO**, **Set** GP18 to `blueState`.

### 9. Execution Flow
1.  **Start**: Variables init to 0. LEDs off.
2.  **Input**: System checks buttons.
3.  **Process**: If a button is pressed, its corresponding state variable flips (toggle).
4.  **Output**: The LEDs update to match the state variables detailed in Step 3.

### 10. Generated Code
```python
from machine import Pin
import time

btn_r = Pin(13, Pin.IN, Pin.PULL_DOWN)
btn_g = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(15, Pin.IN, Pin.PULL_DOWN)

led_r = Pin(16, Pin.OUT)
led_g = Pin(17, Pin.OUT)
led_b = Pin(18, Pin.OUT)

state_r = False
state_g = False
state_b = False

while True:
    if btn_r.value():
        state_r = not state_r
        time.sleep(0.2)
    if btn_g.value():
        state_g = not state_g
        time.sleep(0.2)
    if btn_b.value():
        state_b = not state_b
        time.sleep(0.2)
        
    led_r.value(state_r)
    led_g.value(state_g)
    led_b.value(state_b)
```

### 11. Common Mistakes
*   **No Debounce**: Pressing once toggles it multiple times (flickering).
*   **Floating Inputs**: Forgetting `PULL_DOWN` makes buttons act randomly.

### 12. Try This Next
*   **Master Switch**: Add a 4th button that turns everything OFF.
"""

    p0504 = """
---

## 1. Project 0504: Digital Art Sequences

### 2. Learning Objective
Create a "Campfire" simulation using randomized brightness (PWM) on Red and Green channels.

### 3. Concepts Introduced
*   Pulse Width Modulation (PWM)
*   Randomness (Random Integers)
*   Simulation Logic
*   Color Temperature (Warm colors)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | PWM Output |
| **Green LED** | GP17 | PWM Output |
| **Blue LED** | GP18 | Output (OFF) |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`**
*   **from Smart IO, drag `pico_pwm_write`** (Analog Write)
*   **from Math, drag `random_integer`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **r_val**: Integer (Red brightness)
*   **g_val**: Integer (Green brightness)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, setup PWM on GP16 and GP17.
    *   Set GP18 (Blue) to LOW (Fire isn't blue usually).

**B. Main Loop Phase**
2.  **Generate Random Values**:
    *   Set `r_val` to random int between 30000 and 65535 (Bright Red).
    *   Set `g_val` to random int between 0 and 15000 (Dim Green = Orange/Yellow mix).
3.  **Apply PWM**:
    *   From **Smart IO**, **Set** `pico_pwm_write` GP16 to `r_val`.
    *   From **Smart IO**, **Set** `pico_pwm_write` GP17 to `g_val`.
4.  **Flicker Delay**:
    *   From **Time**, **Wait** random 0.05 to 0.2 seconds.

### 9. Execution Flow
1.  **Start**: Blue LED off.
2.  **Randomize**: Selects a high red value and a low green value.
3.  **Mix**: High Red + Low Green creates dynamic shades of Orange/Gold.
4.  **Flicker**: The random delay simulates the stuttering of flames.

### 10. Generated Code
```python
from machine import Pin, PWM
import time
import random

red = PWM(Pin(16))
green = PWM(Pin(17))
blue = Pin(18, Pin.OUT)

red.freq(1000)
green.freq(1000)
blue.off()

while True:
    r_val = random.randint(40000, 65535)
    g_val = random.randint(0, 20000)
    
    red.duty_u16(r_val)
    green.duty_u16(g_val)
    
    time.sleep(random.uniform(0.05, 0.2))
```

### 11. Common Mistakes
*   **Too much Green**: Makes the fire look lime-colored. Keep green low (< 1/3 of Red).
*   **PWM Freq**: Frequency too low (<50Hz) causes visible blinking instead of dimming.

### 12. Try This Next
*   **Ice Mode**: Simulate ice by using Blue and White (R+G+B).
"""

    p0505 = """
---

## 1. Project 0505: Interactive Digital Art

### 2. Learning Objective
Create a smart night-light that measures ambient light and turns ON the RGB LED only when it is dark.

### 3. Concepts Introduced
*   Analog Input (ADC)
*   Sensor Thresholding
*   Environment Sensing
*   Conditional Output

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Light Dependent Resistor (LDR) + 10kΩ Resistor (Voltage Divider)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR Sensor** | GP26 (ADC0) | Analog Input |
| **RGB LED** | GP16-18 | Output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`**
*   **from Smart IO, drag `pico_adc_read`**
*   **from Logic, drag `if_else`**

### 7. Variables
*   **light_level**: Integer (0-65535)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure ADC**: Setup GP26 as Analog Input.
2.  **Configure LED**: Setup GP16-18 as Outputs.

**B. Main Loop Phase**
3.  **Read Sensor**:
    *   Set `light_level` to `pico_adc_read` (GP26).
4.  **Check Threshold**:
    *   From **Logic**, drag `if_else`.
    *   Condition: If `light_level` < 20000 (Darkness).
5.  **Action (Dark)**:
    *   **Set** RGB LED to Purple (Red+Blue).
6.  **Action (Light)**:
    *   **Set** RGB LED to OFF.
7.  **Wait**: 0.5 seconds.

### 9. Execution Flow
1.  **Sense**: Pico reads voltage from LDR divider. High light = High voltage (or low, depending on wiring).
2.  **Decide**: Compares value to 20000.
3.  **Act**: If below threshold (Dark), turns on mood lighting. Else, saves power.

### 10. Generated Code
```python
from machine import Pin, ADC
import time

ldr = ADC(26)
red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)

THRESHOLD = 20000

while True:
    val = ldr.read_u16()
    
    if val < THRESHOLD:
        # Dark: Purple Mood Light
        red.on()
        green.off()
        blue.on()
    else:
        # Light: Off
        red.off()
        green.off()
        blue.off()
    
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Inverted Logic**: LDR wiring (Pull-up vs Pull-down) flips the logic. If it works backwards, change `<` to `>`.
*   **Threshold Tuning**: 20000 might be wrong for your room. Use `print(val)` to check.

### 12. Try This Next
*   **Gradual Brightness**: Map the darkness level to PWM brightness (Darker = Brighter LED).
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0502 + p0503 + p0504 + p0505)
    
    print("Projects 0502-0505 appended with Strict Compliance.")

if __name__ == "__main__":
    append_batch51_strict()
