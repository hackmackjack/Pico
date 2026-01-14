
## 1. Project 0505: Interactive Digital Art

### 2. Learning Objective
Create light-sensitive RGB display that only activates in dark conditions to save battery.

### 3. Concepts Introduced
*   **Light Detection**: Using LDR to measure ambient brightness
*   **Environment-Gated Output**: Conditional activation based on sensor
*   **Power Management**: Battery saving through smart control

### 4. Hardware Required
Pico, LDR (Light Dependent Resistor), RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LDR** | GP26 (ADC0) | 10kΩ pull-down resistor |
| **Red LED** | GP16 | 220Ω resistor |
| **Green LED** | GP17 | 220Ω resistor |
| **Blue LED** | GP18 | 220Ω resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`** (read LDR value)
*   **from Smart IO, drag `pico_gpio_write`** (control RGB)
*   **from Logic, drag `if_compare`** (threshold check)
*   **from Variables, drag `variables_set`** (store light level)

### 7. Variables
*   **lightLevel**: ADC value (0-65535, higher = brighter)
*   **darkThreshold**: 20000 (adjust for room)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LDR Input**:
    *   From **Smart IO**, drag ADC configuration.
        *   **Snap** into setup.
        *   Set GP26 as analog input.
2.  **Configure RGB Outputs**:
    *   From **Smart IO**, drag pin config blocks.
        *   **Snap** below.
        *   Set GP16-18 as outputs.

**B. Main Loop Phase**
3.  **Read Light Sensor**:
    *   From **Smart IO**, drag `pico_analog_read`.
        *   **Snap** into loop.
        *   Read GP26, store in lightLevel.
4.  **Check if Dark**:
    *   From **Logic**, drag `if_compare`.
        *   **Snap** below.
        *   If lightLevel < darkThreshold (room is dark).
5.  **Activate RGB Sequence** (if dark):
    *   From **Smart IO**, drag gpio_write blocks.
        *   **Snap** into if-block.
        *   Cycle through colors (red → green → blue).
6.  **Turn OFF** (if bright):
    *   From **Smart IO**, drag gpio_write blocks.
        *   **Snap** into else-block.
        *   All RGB = LOW (save battery).

### 9. Execution Flow
System continuously monitors ambient light via LDR. When light level falls below threshold (dark room detected), RGB LED activates color cycling sequence. In bright conditions, LED stays OFF to conserve power. This demonstrates environment-responsive automation.

### 10. Generated Code
```python
import machine, time

# LDR sensor
ldr = machine.ADC(26)

# RGB LED
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

# Threshold (adjust for your room)
DARK_THRESHOLD = 20000

while True:
    light_level = ldr.read_u16()
    
    if light_level < DARK_THRESHOLD:  # Dark room
        # Color sequence
        red.on(); green.off(); blue.off()
        time.sleep(0.5)
        red.off(); green.on(); blue.off()
        time.sleep(0.5)
        red.off(); green.off(); blue.on()
        time.sleep(0.5)
    else:  # Bright room - save battery
        red.off()
        green.off()
        blue.off()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Wrong threshold**: Test LDR values in your room, adjust threshold
*   **Inverted logic**: Lower LDR value = darker (not brighter)
*   **Missing voltage divider**: LDR needs resistor for proper ADC reading

### 12. Try This Next
*   Add potentiometer to adjust threshold in real-time
*   Different color sequences for different light levels
*   Add motion sensor (PIR) for combined activation

---

## 1. Project 0506: Smart Digital Art Switch

### 2. Learning Objective  
Create mood lighting system with switch-selectable profiles (Calm vs Energy).

### 3. Concepts Introduced
*   **Profile Switching**: Different behavior modes
*   **PWM Fading**: Smooth brightness transitions
*   **Thematic Control**: Mood-based lighting

### 4. Hardware Required
Pico, Switch (or button), RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Switch** | GP15 | PULL_DOWN |
| **Red LED** | GP16 | PWM capable |
| **Green LED** | GP17 | PWM capable |
| **Blue LED** | GP18 | PWM capable |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read switch)
*   **from Smart IO, drag `pico_pwm_write`** (fade control)
*   **from Logic, drag `if_compare`** (mode selection)
*   **from Math, drag `map_range`** (fade calculations)

### 7. Variables
*   **switchState**: Boolean (LEFT=Calm, RIGHT=Energy)
*   **brightness**: 0-255 for PWM fading

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Switch**:
    *   From **Smart IO**, drag pin config.
        *   **Snap** into setup.
        *   Set GP15 as input with PULL_DOWN.
2.  **Configure RGB PWM**:
    *   From **Smart IO**, drag PWM config blocks.
        *   **Snap** below.
        *   Set GP16-18 as PWM outputs.

**B. Main Loop Phase**
3.  **Read Switch Position**:
    *   From **Smart IO**, read GP15.
        *   **Snap** into loop.
4.  **Calm Mode** (switch LEFT/OFF):
    *   From **Logic**, if switch = LOW.
        *   **Snap** below.
    *   Slow blue fade: PWM 0→255→0 over 2 seconds.
5.  **Energy Mode** (switch RIGHT/ON):
    *   From **Logic**, else block.
        *   **Snap** below.
    *   Fast red flash: ON 0.1s, OFF 0.1s.

### 9. Execution Flow
Switch position selects between two lighting profiles. LEFT position triggers slow, smooth blue fade for calming effect. RIGHT position activates rapid red flashing for energetic atmosphere. Demonstrates thematic profile switching.

### 10. Generated Code
```python
import machine, time

switch = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

while True:
    if not switch.value():  # Calm mode (left)
        # Slow blue fade
        red.duty_u16(0)
        green.duty_u16(0)
        
        # Fade up
        for b in range(0, 65535, 500):
            blue.duty_u16(b)
            time.sleep(0.01)
        
        # Fade down
        for b in range(65535, 0, -500):
            blue.duty_u16(b)
            time.sleep(0.01)
    
    else:  # Energy mode (right)
        # Fast red flash
        red.duty_u16(65535)
        green.duty_u16(0)
        blue.duty_u16(0)
        time.sleep(0.1)
        
        red.duty_u16(0)
        time.sleep(0.1)
```

### 11. Common Mistakes
*   **No PWM**: Using digital ON/OFF instead of PWM loses fade effect
*   **Wrong freq**: PWM frequency too low causes visible flickering
*   **Fade too fast**: Calm mode should take 2+ seconds per cycle

### 12. Try This Next
*   Add third mode with potentiometer selection
*   Green "Nature" mode with slow random variations
*   OLED display showing current mode name

---

## 1. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Create color-coded alarm system with combinatorial button logic.

### 3. Concepts Introduced
*   **Combinatorial Logic**: Multiple input combinations
*   **Color Coding**: Different colors for different alerts
*   **Status Indication**: Visual signaling system

### 4. Hardware Required
Pico, 2 Buttons, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button A** | GP14 | PULL_DOWN |
| **Button B** | GP15 | PULL_DOWN |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read buttons)
*   **from Smart IO, drag `pico_gpio_write`** (control RGB)
*   **from Logic, drag `if_compare`** (check combinations)

### 7. Variables
*   **buttonA**, **buttonB**: Boolean button states

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Buttons**:
    *   From **Smart IO**, drag pin config.
        *   **Snap** into setup.
        *   Set GP14, GP15 as inputs with PULL_DOWN.
2.  **Configure RGB**:
    *   From **Smart IO**, drag pin config.
        *   **Snap** below.
        *   Set GP16-18 as outputs.

**B. Main Loop Phase**
3.  **Read Both Buttons**:
    *   From **Smart IO**, read GP14 and GP15.
        *   **Snap** into loop.
4.  **Check Button A Only**:
    *   From **Logic**, if A=HIGH and B=LOW.
        *   **Snap** below.
    *   Flash RED (alarm type 1).
5.  **Check Button B Only**:
    *   From **Logic**, else if B=HIGH and A=LOW.
        *   **Snap** below.
    *   Flash BLUE (alarm type 2).
6.  **Check Both Buttons**:
    *   From **Logic**, else if A=HIGH and B=HIGH.
        *   **Snap** below.
    *   Flash PURPLE/Magenta (critical alarm).
7.  **No Buttons**:
    *   From **Logic**, else.
        *   **Snap** below.
    *   All OFF (standby).

### 9. Execution Flow
System monitors two buttons continuously. Single button A triggers red flash. Single button B triggers blue flash. Both buttons together trigger purple flash (R+B). No buttons = all OFF. This demonstrates combinatorial status indication.

### 10. Generated Code
```python
import machine, time

btn_a = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

while True:
    a = btn_a.value()
    b = btn_b.value()
    
    if a and not b:  # Button A only - Red alarm
        red.on(); green.off(); blue.off()
        time.sleep(0.2)
        red.off()
        time.sleep(0.2)
    
    elif b and not a:  # Button B only - Blue alarm
        red.off(); green.off(); blue.on()
        time.sleep(0.2)
        blue.off()
        time.sleep(0.2)
    
    elif a and b:  # Both - Purple alarm (critical)
        red.on(); green.off(); blue.on()
        time.sleep(0.2)
        red.off(); blue.off()
        time.sleep(0.2)
    
    else:  # Neither - Standby
        red.off(); green.off(); blue.off()
        time.sleep(0.1)
```

### 11. Common Mistakes
*   **Wrong AND/OR logic**: Use AND for "both", individual checks for "only one"
*   **No flash**: Forgetting to add blink timing makes colors hard to see
*   **Order of if-statements**: Check "both" before checking individual buttons

### 12. Try This Next
*   Add third button for 8 total combinations
*   Different flash rates for different severities
*   Add buzzer with different tones per color

---

[Continue with Projects 0508-0510...]
