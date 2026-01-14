# Final 4 projects to complete Batch 51

batch51_final = '''## 1. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Color-coded alarm - Button A→Red, Button B→Blue, Both→Purple.

### 3. Concepts Introduced
*   **Combinatorial Logic**: Multiple input combinations
*   **Color Coding**: Different colors for different alerts
*   **Status Indication**: Visual signaling

### 4. Hardware Required
Pico, 2 Buttons, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button A** | GP14 | PULL_DOWN |
| **Button B** | GP15 | PULL_DOWN |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω (unused) |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read buttons)
*   **from Smart IO, drag `pico_gpio_write`** (control RGB)
*   **from Logic, drag `if_compare`** (check combinations)
*   **from Logic, drag `logic_operation`** (AND logic)

### 7. Variables
*   **buttonA**, **buttonB**: Button states

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Buttons**:
    *   From **Smart IO**, drag configs.
        *   **Snap** into setup.
        *   GP14, GP15 as inputs with PULL_DOWN.
2.  **Configure RGB**:
    *   From **Smart IO**, GP16-18 outputs.

**B. Main Loop Phase**
3.  **Read Both Buttons**:
    *   From **Smart IO**, read GP14 and GP15.
        *   **Snap** into loop.
4.  **Check A Only**:
    *   From **Logic**, if A=HIGH AND B=LOW.
        *   **Snap** below.
        *   Flash RED.
5.  **Check B Only**:
    *   From **Logic**, else if B=HIGH AND A=LOW.
        *   Flash BLUE.
6.  **Check Both**:
    *   From **Logic**, else if A=HIGH AND B=HIGH.
        *   Flash PURPLE (R+B).
7.  **None Pressed**:
    *   Else: All OFF.

### 9. Execution Flow
Reads both buttons. Single A→red flash. Single B→blue flash. Both together→purple flash. None→OFF. Combinatorial status indication.

### 10. Generated Code
```python
import machine, time

btn_a = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

while True:
    a, b = btn_a.value(), btn_b.value()
    
    if a and not b:  # A only - Red
        red.on(); green.off(); blue.off()
        time.sleep(0.2)
        red.off()
    elif b and not a:  # B only - Blue
        red.off(); green.off(); blue.on()
        time.sleep(0.2)
        blue.off()
    elif a and b:  # Both - Purple
        red.on(); green.off(); blue.on()
        time.sleep(0.2)
        red.off(); blue.off()
    else:  # None
        red.off(); green.off(); blue.off()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   Wrong AND/OR logic
*   No flash (just solid colors)
*   Check "both" before "single" (order matters)

### 12. Try This Next
*   Third button for 8 combinations
*   Different flash rates
*   Add buzzer tones

---

## 1. Project 0508: The Digital Art Game

### 2. Learning Objective
Reaction game - press button ONLY when green shows (Go/No-Go task).

### 3. Concepts Introduced
*   **Go/No-Go**: Selective response
*   **Random Challenge**: Unpredictable stimuli
*   **Reaction Testing**: Speed measurement

### 4. Hardware Required
Pico, RGB LED, Button

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button** | GP14 | PULL_DOWN |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (button)
*   **from Smart IO, drag `pico_gpio_write`** (RGB)
*   **from Math, drag `random_int`** (color choice)
*   **from Logic, drag `if_compare`** (response check)

### 7. Variables
*   **currentColor**: 0=Red, 1=Green, 2=Blue
*   **score**: Correct count

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
    *   From **Smart IO**, configs.
        *   **Snap** into setup.
        *   Button input, RGB outputs.
2.  **Initialize Score**:
    *   From **Variables**, score = 0.

**B. Main Loop Phase**
3.  **Pick Random Color**:
    *   From **Math**, random 0-2.
        *   **Snap** into loop.
4.  **Display Color**:
    *   Show selected color for 1s.
5.  **Check Response**:
    *   If GREEN and button pressed: score++.
    *   If NOT GREEN and button pressed: error.
6.  **Next Round**:
    *   Delay, repeat.

### 9. Execution Flow
Randomly shows red/green/blue for 1s each. Player presses button ONLY for green. Pressing on red/blue is error. Tests impulse control and visual discrimination.

### 10. Generated Code
```python
import machine, time, random

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

score = 0

while True:
    color = random.randint(0, 2)
    
    # Show color
    red.value(color == 0)
    green.value(color == 1)
    blue.value(color == 2)
    
    time.sleep(1)
    
    if btn.value():
        if color == 1:  # Green - correct!
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print("Error! Don't press on red/blue")
    
    red.off(); green.off(); blue.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   Pressing on every color
*   Not waiting for full display
*   Missing random import

### 12. Try This Next
*   30-second time limit
*   Variable display time
*   Difficulty levels

---

## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Day/night cycle - Sunrise(Orange)→Noon(White)→Sunset(Red)→Night(Blue) over 20s.

### 3. Concepts Introduced
*   **Timed Sequences**: Precise intervals
*   **Color Transitions**: Simulate daily cycle
*   **Temporal Palette**: Time-based colors

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (color mixing)
*   **from Time, drag `pico_wait`** (5s per phase)

### 7. Variables
*   None (sequential timing)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, GP16-18 PWM.

**B. Main Loop Phase**
2.  **Sunrise (Orange)**:
    *   R=HIGH, G=MED, B=LOW.
    *   Wait 5s.
3.  **Noon (White)**:
    *   R=HIGH, G=HIGH, B=HIGH.
    *   Wait 5s.
4.  **Sunset (Red)**:
    *   R=HIGH, G=LOW, B=LOW.
    *   Wait 5s.
5.  **Night (Blue)**:
    *   R=LOW, G=LOW, B=HIGH.
    *   Wait 5s.

### 9. Execution Flow
Cycles through 4 phases: Sunrise(orange,5s) → Noon(white,5s) → Sunset(red,5s) → Night(blue,5s). Total 20s cycle simulating day/night.

### 10. Generated Code
```python
import machine, time

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000); green.freq(1000); blue.freq(1000)

while True:
    # Sunrise - Orange
    red.duty_u16(65535); green.duty_u16(20000); blue.duty_u16(0)
    time.sleep(5)
    
    # Noon - White
    red.duty_u16(65535); green.duty_u16(65535); blue.duty_u16(65535)
    time.sleep(5)
    
    # Sunset - Red
    red.duty_u16(65535); green.duty_u16(0); blue.duty_u16(0)
    time.sleep(5)
    
    # Night - Blue
    red.duty_u16(0); green.duty_u16(0); blue.duty_u16(40000)
    time.sleep(5)
```

### 11. Common Mistakes
*   Wrong color mixing (orange needs R+G)
*   Unequal timing (should be 5s each)
*   Digital instead of PWM

### 12. Try This Next
*   Smooth fades between phases
*   Speed control with pot
*   Add phase names on OLED

---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Parametric shading function - Purple intensity controlled by parameter (0-100).

### 3. Concepts Introduced
*   **Parametric Control**: Intensity parameter
*   **Color Scaling**: Multiply by intensity
*   **Function Design**: Reusable shading

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM (OFF for purple) |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (intensity)
*   **from Math, drag `map_range`** (0-100 → 0-65535)
*   **from Functions, drag `create_function`** (shading function)

### 7. Variables
*   **intensity**: 0-100 input
*   **scaledValue**: PWM output

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, GP16, GP18 PWM.
2.  **Define Function**:
    *   Create `shadePurple(intensity)`.
    *   Maps intensity to R and B.

**B. Main Loop Phase**
3.  **Iterate Intensity**:
    *   For i = 0 to 100.
4.  **Apply Shading**:
    *   Call shadePurple(i).
5.  **Display**:
    *   Show purple at current intensity.

### 9. Execution Flow
Function calculates R=intensity, B=intensity, G=0. Loop cycles 0→100, creating fade from black to full purple. Demonstrates parametric color control.

### 10. Generated Code
```python
import machine, time

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000); green.freq(1000); blue.freq(1000)

def shade_purple(intensity):
    value = int((intensity / 100) * 65535)
    red.duty_u16(value)
    green.duty_u16(0)
    blue.duty_u16(value)

while True:
    for i in range(0, 101, 5):
        shade_purple(i)
        time.sleep(0.05)
    for i in range(100, -1, -5):
        shade_purple(i)
        time.sleep(0.05)
```

### 11. Common Mistakes
*   Green not 0 (ruins purple)
*   Wrong mapping (0-100 must→0-65535)
*   R and B not equal

### 12. Try This Next
*   Manual intensity with pot
*   Other color functions
*   Color mixing ratios

---

'''

# Final append
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    current = f.read()

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(current + batch51_final)

print("=" * 70)
print("✅ BATCH 51 COMPLETE!")
print("=" * 70)
print()
print("Projects 0501-0510: All 10 projects with CUSTOM content")
print("Each project based on its specific problem statement")
print()
print("Next: Batch 52 (Projects 0511-0520) - Animation")
print("=" * 70)
