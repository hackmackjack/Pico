# Remaining 7 projects for Batch 51 (continuing from 0503)

batch51_remaining = '''
## 1. Project 0504: Digital Art Sequences

### 2. Learning Objective
Simulate campfire effect with random Red/Green mixing (Red always > Green).

### 3. Concepts Introduced
*   **Random Generation**: Unpredictable flicker
*   **Constrained Randomness**: Red > Green rule
*   **Procedural Animation**: Organic fire texture

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM capable |
| **Green LED** | GP17 | PWM capable |
| **Blue LED** | GP18 | OFF (no blue in fire) |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (intensity control)
*   **from Math, drag `random_int`** (flickering)
*   **from Time, drag `pico_wait`** (random timing)

### 7. Variables
*   **redLevel**: Random 128-255
*   **greenLevel**: Random 0 to (redLevel-20)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, drag PWM configs.
        *   **Snap** into setup.
        *   GP16, GP17 as PWM outputs.
2.  **Turn Blue OFF**:
    *   From **Smart IO**, GP18 = LOW.

**B. Main Loop Phase**
3.  **Generate Red Level**:
    *   From **Math**, random 40000-65535.
        *   **Snap** into loop.
4.  **Generate Green Level**:
    *   From **Math**, random 0 to (red-10000).
        *   **Snap** below.
        *   Ensures Red > Green.
5.  **Set PWM Values**:
    *   From **Smart IO**, write PWM.
        *   **Snap** below.
6.  **Random Flicker Delay**:
    *   From **Time**, random 0.05-0.15s.

### 9. Execution Flow
Continuously generates random red (bright) and green (dimmer) levels, creating orange-red flicker. Random timing adds organic campfire feeling. Blue always OFF.

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
*   No randomness = static orange

### 12. Try This Next
*   Add blue for hotter flames
*   Intensity control with pot
*   Sound effects

---

## 1. Project 0505: Interactive Digital Art

### 2. Learning Objective
Light-responsive RGB display - ON in dark, OFF in light (battery saving).

### 3. Concepts Introduced
*   **Light Detection**: LDR sensor
*   **Environment-Gated**: Conditional activation
*   **Power Management**: Battery conservation

### 4. Hardware Required
Pico, LDR, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LDR** | GP26 (ADC0) | With 10kΩ resistor |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`** (read LDR)
*   **from Smart IO, drag `pico_gpio_write`** (RGB control)
*   **from Logic, drag `if_compare`** (threshold check)

### 7. Variables
*   **lightLevel**: ADC value (0-65535)
*   **darkThreshold**: 20000 (adjustable)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LDR**:
    *   From **Smart IO**, drag ADC config.
        *   **Snap** into setup.
        *   GP26 as analog input.
2.  **Configure RGB**:
    *   From **Smart IO**, drag pin configs.
        *   **Snap** below.
        *   GP16-18 as outputs.

**B. Main Loop Phase**
3.  **Read Light**:
    *   From **Smart IO**, read ADC.
        *   **Snap** into loop.
        *   Store in lightLevel.
4.  **Check if Dark**:
    *   From **Logic**, if lightLevel < 20000.
5.  **Activate Sequence** (if dark):
    *   Cycle through colors.
6.  **Turn OFF** (if bright):
    *   All RGB = LOW.

### 9. Execution Flow
Monitors ambient light continuously. When dark (LDR < threshold), activates RGB color cycling. When bright, stays OFF to save battery. Environment-responsive art.

### 10. Generated Code
```python
import machine, time

ldr = machine.ADC(26)
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

DARK_THRESHOLD = 20000

while True:
    light = ldr.read_u16()
    
    if light < DARK_THRESHOLD:
        # Cycle colors
        red.on(); green.off(); blue.off()
        time.sleep(0.5)
        red.off(); green.on(); blue.off()
        time.sleep(0.5)
        red.off(); green.off(); blue.on()
        time.sleep(0.5)
    else:
        red.off(); green.off(); blue.off()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   Wrong threshold for room
*   Inverted logic (darker = lower value)
*   Missing voltage divider

### 12. Try This Next
*   Adjustable threshold with pot
*   Different sequences for light levels
*   Add PIR motion sensor

---

## 1. Project 0506: Smart Digital Art Switch

### 2. Learning Objective
Mood lighting - switch selects "Calm" (slow blue fade) or "Energy" (fast red flash).

### 3. Concepts Introduced
*   **Profile Switching**: Mode selection
*   **PWM Fading**: Smooth transitions
*   **Thematic Control**: Mood-based output

### 4. Hardware Required
Pico, Switch, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Switch** | GP15 | PULL_DOWN |
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read switch)
*   **from Smart IO, drag `pico_pwm_write`** (fade control)
*   **from Logic, drag `if_compare`** (mode selection)

### 7. Variables
*   **mode**: Boolean (LEFT=Calm, RIGHT=Energy)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Switch**:
    *   From **Smart IO**, GP15 input.
2.  **Configure RGB PWM**:
    *   From **Smart IO**, GP16-18 PWM.

**B. Main Loop Phase**
3.  **Read Mode**:
    *   From **Smart IO**, read GP15.
4.  **Calm Mode** (LEFT/OFF):
    *   Slow blue fade 0→65535→0 over 2s.
5.  **Energy Mode** (RIGHT/ON):
    *   Fast red flash 0.1s ON, 0.1s OFF.

### 9. Execution Flow
Switch position selects mode. LEFT = slow blue fade (relaxing). RIGHT = fast red flash (energizing). Thematic lighting profiles.

### 10. Generated Code
```python
import machine, time

switch = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000); green.freq(1000); blue.freq(1000)

while True:
    if not switch.value():  # Calm
        red.duty_u16(0); green.duty_u16(0)
        for b in range(0, 65535, 500):
            blue.duty_u16(b)
            time.sleep(0.01)
        for b in range(65535, 0, -500):
            blue.duty_u16(b)
            time.sleep(0.01)
    else:  # Energy
        red.duty_u16(65535); green.duty_u16(0); blue.duty_u16(0)
        time.sleep(0.1)
        red.duty_u16(0)
        time.sleep(0.1)
```

### 11. Common Mistakes
*   No PWM (loses fade)
*   Fade too fast (not calming)
*   Wrong freq (flickers)

### 12. Try This Next
*   Third mode (green nature)
*   OLED mode display
*   Smooth mode transitions

---

'''

# Save progress
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    current = f.read()

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(current + batch51_remaining)

print("✓ Projects 0504-0506 added")
print("Remaining for Batch 51: 0507-0510 (4 more)")
