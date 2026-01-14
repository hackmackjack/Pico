# Batch 51 Completion: Projects 0503-0510

## 1. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Create interactive color mixer where each button toggles one RGB component independently.

### 3. Concepts Introduced
*   **Toggle Logic**: Button press flips state ON/OFF
*   **Additive Color Synthesis**: Combining R, G, B to make 8 colors
*   **Independent Channel Control**: Each color component controlled separately

### 4. Hardware Required
*   Pico, 3 Buttons, RGB LED

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
*   **from Logic, drag `if_compare`** (detect presses)
*   **from Variables, drag `variables_set`** (store states)

### 7. Variables
*   **redState**, **greenState**, **blueState**: Boolean RGB states

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Buttons**:
    *   From **Smart IO**, drag pin config.
        *   **Snap** into setup.
        *   Set GP13-15 as inputs with PULL_DOWN.
2.  **Configure RGB Outputs**:
    *   From **Smart IO**, drag pin config.
        *   **Snap** below.
        *   Set GP16-18 as outputs.
3.  **Initialize States**:
    *   From **Variables**, drag init blocks.
        *   **Snap** below.
        *   Set all states = FALSE.

**B. Main Loop Phase**
4.  **Toggle Red**:
    *   From **Smart IO**, read GP13.
        *   **Snap** into loop.
    *   From **Logic**, if pressed: NOT redState.
5.  **Toggle Green**:
    *   From **Smart IO**, read GP14.
        *   **Snap** below.
    *   From **Logic**, if pressed: NOT greenState.
6.  **Toggle Blue**:
    *   From **Smart IO**, read GP15.
        *   **Snap** below.
    *   From **Logic**, if pressed: NOT blueState.
7.  **Update Outputs**:
    *   From **Smart IO**, write states to GP16-18.

### 9. Execution Flow
Each button controls one color channel. Press to toggle ON/OFF. Build any of 8 basic colors through additive mixing. Demonstrates independent channel control and additive color synthesis.

### 10. Generated Code
```python
import machine, time

btn_r = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_g = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

r_state = False
g_state = False
b_state = False

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
*   Missing debounce causes multiple toggles
*   Wrong toggle logic (set TRUE instead of NOT)
*   No pull resistors on buttons

### 12. Try This Next
*   Add reset button for all OFF
*   Display color name on OLED
*   PWM for brightness control

---

## 1. Project 0504: Digital Art Sequences

### 2. Learning Objective
Generate procedural fire effect - random Red/Green mix with Red > Green constraint.

### 3. Concepts Introduced
*   **Random Generation**: Unpredictable values
*   **Constrained Randomness**: Red always > Green
*   **Procedural Animation**: Organic flickering

### 4. Hardware Required
*   Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM |
| **Blue LED** | GP18 | OFF |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (intensity control)
*   **from Math, drag `random_int`** (generate values)
*   **from Time, drag `pico_wait`** (flicker timing)

### 7. Variables
*   **redLevel**: 128-255
*   **greenLevel**: 0 to (redLevel-20)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, drag PWM setup.
        *   **Snap** into setup.
        *   GP16, GP17 as PWM.
2.  **Blue OFF**:
    *   From **Smart IO**, GP18 = LOW.

**B. Main Loop Phase**
3.  **Random Red**:
    *   From **Math**, random 128-255.
        *   **Snap** into loop.
4.  **Random Green**:
    *   From **Math**, random 0 to (red-20).
        *   **Snap** below.
5.  **Set PWM**:
    *   From **Smart IO**, write PWM values.
6.  **Flicker Delay**:
    *   From **Time**, wait 0.05-0.15s.

### 9. Execution Flow
Continuous random Red (high) and Green (lower) creates orange-red fire colors. Random timing simulates flickering. Blue OFF. Produces organic campfire effect.

### 10. Generated Code
```python
import machine, time, random

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.Pin(18, machine.Pin.OUT)

red.freq(1000)
green.freq(1000)
blue.off()

while True:
    r = random.randint(40000, 65535)
    g = random.randint(0, r - 10000)
    
    red.duty_u16(r)
    green.duty_u16(g)
    
    time.sleep(random.uniform(0.05, 0.15))
```

### 11. Common Mistakes
*   Green > Red produces wrong colors
*   Blue ON ruins fire effect
*   No randomness = static color

### 12. Try This Next
*   Add blue for white-hot flames
*   Button controls intensity
*   Add buzzer sound effects

---

[Continuing with remaining 6 projects 0505-0510...]

