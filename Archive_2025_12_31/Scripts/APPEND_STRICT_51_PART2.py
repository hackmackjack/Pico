import os

def append_batch51_part2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0506 = """
---

## 1. Project 0506: Smart Digital Art Switch

### 2. Learning Objective
Create a dual-mode lighting system where a switch toggles between "Calm Mode" (Slow Fade) and "Party Mode" (Fast Strobe).

### 3. Concepts Introduced
*   Mode Selection (State Switching)
*   Complex Logic Branching
*   PWM Fading vs Digital Strobing
*   User Interface Design

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Slide Switch (or Button acting as toggle)
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Switch** | GP15 | Pull-Down Input |
| **RGB LED** | GP16-18 | PWM Output |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Loops, drag `count_with`** (for fading)
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **mode**: Boolean (0 = Calm, 1 = Party)
*   **brightness**: Integer (Loop variable)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP15 as Input, GP16-18 as PWM Outputs.

**B. Main Loop Phase**
2.  **Read Mode**:
    *   Set `mode` to `pico_gpio_read` (GP15).
3.  **Check Mode**:
    *   **If** `mode` is TRUE ("Party"):
        *   Flash Red (ON/OFF 0.1s).
        *   Flash Blue (ON/OFF 0.1s).
    *   **Else** ("Calm"):
        *   Fade Green UP (0 to 65000 in steps).
        *   Fade Green DOWN (65000 to 0 in steps).

### 9. Execution Flow
1.  **Check**: The Pico checks the switch position.
2.  **Branch**:
    *   **High (Party)**: Enters a fast loop blinking Red/Blue.
    *   **Low (Calm)**: Enters a slow loop fading Green.
3.  **Repeat**: The loop restarts and checks the switch again.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

sw = Pin(15, Pin.IN, Pin.PULL_DOWN)
red = Pin(16, Pin.OUT)
green = PWM(Pin(17)) # PWM for fade
blue = Pin(18, Pin.OUT)

green.freq(1000)

while True:
    if sw.value():
        # Party Mode
        green.duty_u16(0) # Ensure green off
        red.on(); blue.off(); time.sleep(0.1)
        red.off(); blue.on(); time.sleep(0.1)
    else:
        # Calm Mode
        red.off(); blue.off()
        # Fade Up
        for i in range(0, 65535, 2000):
            green.duty_u16(i)
            time.sleep(0.05)
        # Fade Down
        for i in range(65535, 0, -2000):
            green.duty_u16(i)
            time.sleep(0.05)
```

### 11. Common Mistakes
*   **Blocking Code**: The "Calm" fade loop takes a long time. If you flip the switch, it won't change until the fade finishes.
*   **Flickering**: PWM frequency need to be set (1000Hz).

### 12. Try This Next
*   **Non-Blocking**: Use a timer check instead of `sleep` to make the switch responsive instantly.
"""

    p0507 = """
---

## 1. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Build a visual alarm where different button combinations trigger different color alerts (Red, Blue, or Purple).

### 3. Concepts Introduced
*   Combinatorial Logic (AND, OR, NOT)
*   Truth Tables
*   Multi-Input Handling

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   2x Push Buttons (A and B)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Pull-Down |
| **Button B** | GP15 | Pull-Down |
| **Red LED** | GP16 | Output |
| **Blue LED** | GP18 | Output |

### 6. Blocks Used
*   **from Logic, drag `and_operation`**
*   **from Logic, drag `not_operation`**
*   **from Logic, drag `if_elseif`**

### 7. Variables
*   **a_val**: Boolean
*   **b_val**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14/15 Inputs, GP16/18 Outputs.

**B. Main Loop Phase**
2.  **Read Inputs**: Read Button A and B.
3.  **Logic Check**:
    *   **If** A AND B: Set **Purple** (Red+Blue).
    *   **Else If** A: Set **Red**.
    *   **Else If** B: Set **Blue**.
    *   **Else**: Turn All **OFF**.
4.  **Wait**: 0.1s.

### 9. Execution Flow
1.  **Scan**: Reads both buttons.
2.  **Evaluate**: Checks the "Both" condition *first* (Priority).
3.  **Display**: Sets the LED color based on the combination.

### 10. Generated Code
```python
from machine import Pin
import time

btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(15, Pin.IN, Pin.PULL_DOWN)
red = Pin(16, Pin.OUT)
blue = Pin(18, Pin.OUT)

while True:
    a = btn_a.value()
    b = btn_b.value()
    
    if a and b:
        # Purple
        red.on()
        blue.on()
    elif a:
        # Red
        red.on()
        blue.off()
    elif b:
        # Blue
        red.off()
        blue.on()
    else:
        # Off
        red.off()
        blue.off()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Order of Operations**: Checking "If A" first would make "A+B" impossible to reach in some logical structures. Always check the most specific condition (A AND B) first.

### 12. Try This Next
*   **Blinking Alarm**: Make the Red/Blue/Purple modes flash instead of stay solid.
"""

    p0508 = """
---

## 1. Project 0508: The Digital Art Game

### 2. Learning Objective
Create a "Reaction Tester" game. The LED cycles colors rapidly; the player must press the button ONLY when it is Green.

### 3. Concepts Introduced
*   Game Loops
*   Reaction Time Measurement
*   Win/Loss Conditions
*   Random Intervals

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   1x Push Button

### 6. Blocks Used
*   **from Loops, drag `repeat_while`**
*   **from Math, drag `random_integer`**
*   **from Text, drag `print`**

### 7. Variables
*   **target_color**: Integer (0=Red, 1=Green, 2=Blue)
*   **score**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Button Input, RGB Output.
2.  **Score**: Set `score` to 0.

**B. Main Loop Phase**
3.  **Pick Color**: Random int 0-2.
4.  **Display**:
    *   Show Red/Green/Blue based on number.
5.  **Wait & Check**:
    *   Wait random time (0.5s - 2s).
    *   If Button Pressed:
        *   If Color == Green: `score = score + 1`, Flash White (Win).
        *   If Color != Green: `score = 0`, Flash Red (Lose).

### 9. Execution Flow
1.  **Cycle**: The LED changes visuals unpredictable.
2.  **React**: Player watches for Green.
3.  **Judge**: Code captures the button state during the Green window.

### 10. Generated Code
```python
from machine import Pin
import time
import random

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)] # R, G, B

score = 0

while True:
    target = random.randint(0, 2)
    
    # Show Color
    for i in range(3):
        leds[i].value(1 if i == target else 0)
    
    # Waiting period (Game Window)
    reaction_time = random.uniform(0.5, 1.5)
    start = time.time()
    
    pressed = False
    while time.time() - start < reaction_time:
        if btn.value():
            pressed = True
            break
    
    # Judge
    if pressed:
        if target == 1: # Green
            score += 1
            print(f"Good! Score: {score}")
            # Win Flash
            for l in leds: l.on()
            time.sleep(0.2)
        else:
            score = 0
            print("Wrong! Reset.")
            for i in range(3): leds[i].on() if i==0 else leds[i].off() # Red
            time.sleep(0.5)
            
    # Gap
    for l in leds: l.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Holding Button**: Cheating by holding the button down. (Fix: Wait for button release before starting next round).

### 12. Try This Next
*   **Speed Up**: Decrease the reaction window as the score gets higher.
"""

    p0509 = """
---

## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Create a time-based "Day/Night Cycle" simulator using predefined color palettes (Sunrise -> Noon -> Sunset -> Night).

### 3. Concepts Introduced
*   State Machines (Day Phase)
*   Color Temperature Theory
*   Timed Automation

### 4. Hardware Required
*   Pico, RGB LED

### 6. Blocks Used
*   **from Functions, drag `to_procedure`** (Create a function for each phase)
*   **from Time, drag `pico_wait`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: RGB PWM.

**B. Main Loop Phase**
2.  **Sunrise**: Set Orange (Red + some Green). Wait 5s.
3.  **Noon**: Set White (Max Brightness). Wait 5s.
4.  **Sunset**: Set Red/Pink. Wait 5s.
5.  **Night**: Set Dim Blue. Wait 5s.

### 9. Execution Flow
Sequentially moves through 4 distinct lighting states, creating an atmospheric loop.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

r = PWM(Pin(16)); g = PWM(Pin(17)); b = PWM(Pin(18))
for p in [r,g,b]: p.freq(1000)

def set_color(rv, gv, bv):
    r.duty_u16(rv); g.duty_u16(gv); b.duty_u16(bv)

while True:
    # Sunrise (Orange)
    set_color(60000, 20000, 0)
    time.sleep(5)
    
    # Noon (White)
    set_color(65535, 65535, 65535)
    time.sleep(5)
    
    # Sunset (Red-Purple)
    set_color(50000, 0, 10000)
    time.sleep(5)
    
    # Night (Dim Blue)
    set_color(0, 0, 15000)
    time.sleep(5)
```

### 11. Common Mistakes
*   **Abrupt Transitions**: Colors snap instead of fade (Use loops for fading).

### 12. Try This Next
*   **Smooth Transitions**: Interpolate values between states for a gradual change.
"""

    p0510 = """
---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Combine input, logic, and output to create a "Parametric Color Mixer". A variable changes automatically, and a mathematical function maps it to color.

### 3. Concepts Introduced
*   Mathematical Mapping (Linear Scaling)
*   Parametric variables
*   Functions with Arguments

### 4. Hardware Required
*   Pico, RGB LED

### 6. Blocks Used
*   **from Math, drag `map_range`**
*   **from Functions, drag `procedure_with_return`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: RGB PWM.

**B. Main Loop Phase**
2.  **Loop Variable**: Count `i` from 0 to 100.
3.  **Calculate**:
    *   Red = `i` * 650.
    *   Blue = (100 - `i`) * 650.
4.  **Display**: Show outcome. This creates a smooth cross-fade from Blue to Red.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

r = PWM(Pin(16)); b = PWM(Pin(18))
r.freq(1000); b.freq(1000)

while True:
    # Cross-fade Blue to Red
    for i in range(100):
        red_val = int(i * 655.35)
        blue_val = int((100 - i) * 655.35)
        
        r.duty_u16(red_val)
        b.duty_u16(blue_val)
        time.sleep(0.05)
        
    # Cross-fade Red to Blue
    for i in range(100):
        red_val = int((100 - i) * 655.35)
        blue_val = int(i * 655.35)
        
        r.duty_u16(red_val)
        b.duty_u16(blue_val)
        time.sleep(0.05)
```

### 12. Try This Next
*   **Sine Wave**: Use `math.sin()` for organic breathing effects.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0506 + p0507 + p0508 + p0509 + p0510)
    
    print("Projects 0506-0510 appended with Strict Compliance.")

if __name__ == "__main__":
    append_batch51_part2()
