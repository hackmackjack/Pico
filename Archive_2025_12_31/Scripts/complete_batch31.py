# Complete Batch 31: Append Projects 0307-0310

final_projects = '''
## 1️⃣ Project 0307: Digital Art Alarm System

### 2️⃣ Learning Objective
Create a persistent notification system using visual feedback. You will implement a mailbox alert that pulses green until acknowledged, demonstrating stateful alarm behavior.

### 3️⃣ Concepts Introduced
*   **Persistent State**: Alarm remains active until explicitly cleared.
*   **PWM Pulsing**: Fade in/out effect using duty cycle modulation.
*   **Event-Driven Logic**: One event triggers alarm, another event clears it.

### 4️⃣ Hardware Required
*   **Pico**
*   **Switch/Sensor** (Mailbox door switch)
*   **Acknowledge Button**
*   **RGB LED** (Common Cathode)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Mailbox Switch** | GP18 | PULL_DOWN enabled |
| **Ack Button** | GP19 | PULL_DOWN enabled |
| **Red Channel** | GP13 | Via 220Ω Resistor |
| **Green Channel** | GP14 | Via 220Ω Resistor |
| **Blue Channel** | GP15 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs  
*   **Block:** `Setup Button pin:[N]`

🔹 **PWM Write**
*   **Category:** Pin Access
*   **Block:** `PWM Write pin:[N] freq:[F] duty:[D]`

### 7️⃣ Variables & State
*   **mailArrived**: Boolean flag indicating mail delivery detected.
*   **pulseValue**: Current PWM duty for pulsing effect (0-65535).
*   **pulseDirection**: +1 for brightening, -1 for dimming.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [mailArrived] to [false]`.
    *   From **Variables**, drag `set [pulseValue] to [0]`.
    *   From **Variables**, drag `set [pulseDirection] to [1]`.
    *   From **Inputs**, drag `Setup Button pin:[18/19]` for both switches.
    *   From **Outputs**, drag `Setup PWM pin:[14]` (Green only).

*   **B. Main Loop Phase**
    *   From **Logic**, drag `if [Mailbox Switch OPEN] and [not mailArrived] then`.
        *   Then: `set [mailArrived] to [true]`.
    *   From **Logic**, drag `if [Ack Button Pressed] then`.
        *   Then: `set [mailArrived] to [false]`, `set [pulseValue] to [0]`.
    *   From **Logic**, drag `if [mailArrived] then`.
        *   Then (Pulse Green):
            *   `change [pulseValue] by [pulseDirection * 2000]`.
            *   `if [pulseValue] >= [65535] then set [pulseDirection] to [-1]`.
            *   `if [pulseValue] <= [0] then set [pulseDirection] to [1]`.
            *   `PWM Write green [pulseValue]`.
    *   From **Timing**, drag `sleep [0.05] seconds`.

### 9️⃣ Execution Flow (Plain English)

The system monitors the mailbox switch. When the switch opens (mail arrives), it sets `mailArrived` to true. While this flag is true, the green LED pulses slowly by incrementing/decrementing its PWM duty cycle between 0 and 65535, creating a breathing effect. When the acknowledge button is pressed, the flag clears and the LED turns off. The alarm persists even if the mailbox closes, requiring explicit acknowledgment to silence.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

mailbox_switch = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
ack_button = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
green = machine.PWM(machine.Pin(14))
green.freq(1000)

mailArrived = False
pulseValue = 0
pulseDirection = 2000

while True:
    if mailbox_switch.value() and not mailArrived:
        mailArrived = True
    
    if ack_button.value():
        mailArrived = False
        pulseValue = 0
        while ack_button.value():
            time.sleep(0.01)
    
    if mailArrived:
        pulseValue += pulseDirection
        if pulseValue >= 65535:
            pulseValue = 65535
            pulseDirection = -2000
        if pulseValue <= 0:
            pulseValue = 0
            pulseDirection = 2000
        green.duty_u16(pulseValue)
    else:
        green.duty_u16(0)
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Alarm Clears Immediately**: If alarm sets then immediately clears, the mailbox switch might be bouncing. Add debounce logic or use pull-up/pull-down correctly.
*   **No Pulsing**: If LED is solid instead of pulsing, verify pulse increment (2000) is appropriate. Too small = imperceptible, too large = jumpy.
*   **Can't Clear**: If acknowledge button doesn't work, verify button wiring and PULL_DOWN configuration.

### 1️⃣2️⃣ Try This Next

*   **Dual Color**: Flash red if mail sits unacknowledged for >1 hour (add timer logic).
*   **Adjustable Pulse Speed**: Use potentiometer to control pulse rate.
*   **Multi-State**: Add yellow for "mail collected but not acknowledged".

---

## 1️⃣ Project 0308: The Digital Art Game

### 2️⃣ Learning Objective
Create an interactive color-matching game using a color sensor. You will implement a Simon Says variant where players match LED colors by presenting colored objects, combining sensor input with game logic.

### 3️⃣ Concepts Introduced
*   **Color Sensor Reading**: RGB channel detection from TCS34725 or similar.
*   **Color Matching Logic**: Comparing sensor values to expected ranges.
*   **Basic Game Flow**: Challenge → Response → Validation.

### 4️⃣ Hardware Required
*   **Pico**
*   **RGB LED** (Common Cathode)
*   **Color Sensor** (TCS34725 or similar I2C color sensor)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sensor SDA** | GP0 (I2C0 SDA) | I2C Data |
| **Sensor SCL** | GP1 (I2C0 SCL) | I2C Clock |
| **Red Channel** | GP13 | Via 220Ω Resistor |
| **Green Channel** | GP14 | Via 220Ω Resistor |
| **Blue Channel** | GP15 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **Setup I2C Color Sensor**
*   **Category:** Sensors
*   **Block:** `Setup Color Sensor I2C:[0]`

🔹 **Read Color**
*   **Category:** Sensors
*   **Block:** `read color sensor → returns [R, G, B]`

🔹 **PWM Write**
*   **Category:** Pin Access
*   **Block:** `PWM Write pin:[N] freq:[F] duty:[D]`

### 7️⃣ Variables & State
*   **targetColor**: Random choice (0=Red, 1=Green, 2=Blue).
*   **sensedR/G/B**: Color sensor readings.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup Color Sensor I2C:[0]`.
    *   From **Outputs**, drag `Setup PWM pin:[13/14/15]`.

*   **B. Main Loop Phase**
    *   From **Variables**, drag `set [targetColor] to [random 0 to 2]`.
    *   **Show Target**:
        *   Display target color on LED for 2 seconds.
    *   **Read Player Response**:
        *   From **Sensors**, drag `read color sensor`.
        *   Store R, G, B values.
    *   **Validate**:
        *   From **Logic**, drag matching logic (if target=Red and sensedR>threshold, success).
        *   Flash white for success, flash red for fail.
    *   From **Timing**, drag `sleep [2] seconds` before next round.

### 9️⃣ Execution Flow (Plain English)

The game picks a random color (Red, Green, or Blue) and displays it on the LED for 2 seconds. The player must place a matching colored object (card, paper, toy) in front of the color sensor. The sensor reads the object's RGB values. If the dominant color matches the target (e.g., Red channel > Green and Blue for Red target), the game flashes white (success). If mismatched, it flashes red (fail). This tests color recognition and sensor-physical world interaction.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random
from tcs34725 import TCS34725

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
sensor = TCS34725(i2c)

red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

while True:
    target = random.randint(0, 2)  # 0=Red, 1=Green, 2=Blue
    
    # Show target color
    if target == 0:
        red.duty_u16(65535); green.duty_u16(0); blue.duty_u16(0)
    elif target == 1:
        red.duty_u16(0); green.duty_u16(65535); blue.duty_u16(0)
    else:
        red.duty_u16(0); green.duty_u16(0); blue.duty_u16(65535)
    
    time.sleep(2)
    
    # Read player object
    r, g, b = sensor.read()
    
    # Validate
    success = False
    if target == 0 and r > g and r > b:
        success = True
    elif target == 1 and g > r and g > b:
        success = True
    elif target == 2 and b > r and b > g:
        success = True
    
    # Show result
    if success:
        red.duty_u16(65535); green.duty_u16(65535); blue.duty_u16(65535)  # White
    else:
        red.duty_u16(65535); green.duty_u16(0); blue.duty_u16(0)  # Red
    
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sensor Not Detected**: Verify I2C wiring and address (usually 0x29 for TCS34725).
*   **Always Fails**: If validation never succeeds, print the R/G/B values to see actual sensor readings. Adjust thresholds or use ratios instead of absolute comparisons.
*   **Lighting Dependent**: Color sensors are highly sensitive to ambient light. Play in consistent lighting or use the sensor's LED.

### 1️⃣2️⃣ Try This Next

*   **Speed Round**: Reduce time from 2s to 1s for faster-paced gameplay.
*   **Score Tracking**: Count consecutive correct matches and display high score.
*   **Multi-Color**: Require matching composite colors (yellow = red+green card).

---

## 1️⃣ Project 0309: Automated Digital Art

### 2️⃣ Learning Objective
Create a smooth color transition over time by interpolating between color stops. You will simulate a sunrise gradient from dark blue to bright white over 30 seconds using calculated intermediate steps.

### 3️⃣ Concepts Introduced
*   **Color Interpolation**: Calculating intermediate colors between two endpoints.
*   **Gradient Sequences**: Chaining multiple color transitions.
*   **Time-Based Animation**: Updating color based on elapsed time.

### 4️⃣ Hardware Required
*   **Pico**
*   **RGB LED** (Common Cathode)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Channel** | GP13 | Via 220Ω Resistor |
| **Green Channel** | GP14 | Via 220Ω Resistor |
| **Blue Channel** | GP15 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **PWM Write**
*   **Category:** Pin Access
*   **Block:** `PWM Write pin:[N] freq:[F] duty:[D]`

🔹 **Math Operations**
*   **Category:** Math
*   **Block:** Linear interpolation calculations

🔹 **For Loop**
*   **Category:** Loops
*   **Block:** `for [i] from [0] to [N]`

### 7️⃣ Variables & State
*   **step**: Current interpolation step in the gradient.
*   **r/g/b**: Calculated color values for current step.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[13/14/15]`.

*   **B. Main Loop Phase**
    *   Define color sequence (6 stops over 30s = 5s per transition):
        1. Dark Blue (0, 0, 32768)
        2. Purple (16384, 0, 49152)
        3. Red (65535, 0, 0)
        4. Orange (65535, 32768, 0)
        5. Yellow (65535, 65535, 0)
        6. White (65535, 65535, 65535)
    *   For each transition:
        *   From **Loops**, drag `for [step] from [0] to [50]`.
            *   Calculate: `r = start_r + (end_r - start_r) * step / 50`.
            *   Calculate similarly for g and b.
            *   `PWM Write` calculated r/g/b values.
            *   `sleep [0.1] seconds` (50 steps ×  0.1s = 5s per transition).

### 9️⃣ Execution Flow (Plain English)

The Pico defines six color waypoints representing sunrise stages. For each pair of waypoints, it calculates 50 intermediate color steps using linear interpolation. Starting from dark blue, it gradually shifts  toward purple by incrementally increasing red while adjusting blue. This continues through each transition (purple→red→orange→yellow→white), with each transition taking 5 seconds. The total 30-second sequence creates a smooth, realistic sunrise simulation through mathematical color blending.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Color stops: (R, G, B)
colors = [
    (0, 0, 32768),        # Dark Blue
    (16384, 0, 49152),    # Purple
    (65535, 0, 0),        # Red
    (65535, 32768, 0),    # Orange
    (65535, 65535, 0),    # Yellow
    (65535, 65535, 65535) # White
]

while True:
    for i in range(len(colors) - 1):
        start_r, start_g, start_b = colors[i]
        end_r, end_g, end_b = colors[i + 1]
        
        for step in range(51):  # 0 to 50 inclusive
            r = int(start_r + (end_r - start_r) * step / 50)
            g = int(start_g + (end_g - start_g) * step / 50)
            b = int(start_b + (end_b - start_b) * step / 50)
            
            red.duty_u16(r)
            green.duty_u16(g)
            blue.duty_u16(b)
            
            time.sleep(0.1)
    
    time.sleep(2)  # Pause at white before restarting
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sudden Jumps**: If colors change abruptly instead of smoothly, increase the number of interpolation steps or decrease sleep time.
*   **Wrong Colors**: If orange looks red or yellow looks green, verify the RGB values for each waypoint match the color names.
*   **Too Fast/Slow**: If the 30-second timing is off, verify: (steps per transition) × (sleep time) × (number of transitions) = 30s.

### 1️⃣2️⃣ Try This Next

*   **Sunset Reverse**: Run the sequence in reverse (white→yellow→orange→red→purple→blue) for a sunset.
*   **Non-Linear Interpolation**: Use easing functions (quadratic, sine) instead of linear for more natural transitions.
*   **Real-Time Sync**: Trigger sunrise at actual dawn time using RTC module.

---

## 1️⃣ Project 0310: Mastering Digital Art

### 2️⃣ Learning Objective
Implement HSV (Hue, Saturation, Value) to RGB color space conversion. You will create a function that accepts intuitive color parameters and mathematically converts them to PWM values, demonstrating advanced color manipulation.

### 3️⃣ Concepts Introduced
*   **HSV Color Space**: Hue (0-360°), Saturation (0-100%), Value (0-100%).
*   **Color Space Conversion**: Mathematical transformation between color models.
*   **Function Parameters**: Passing multiple arguments to reusable code.
*   **Mathematical Algorithms**: Implementing published conversion formulas.

### 4️⃣ Hardware Required
*   **Pico**
*   **RGB LED** (Common Cathode)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Channel** | GP13 | Via 220Ω Resistor |
| **Green Channel** | GP14 | Via 220Ω Resistor |
| **Blue Channel** | GP15 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **Define Function**
*   **Category:** Functions
*   **Block:** `to [set_hsv] with [h] [s] [v] do`

🔹 **Math Operations**
*   **Category:** Math
*   **Block:** Modulo, floor division, conditional expressions

🔹 **PWM Write**
*   **Category:** Pin Access
*   **Block:** `PWM Write pin:[N] freq:[F] duty:[D]`

### 7️⃣ Variables & State
*   **h**: Hue (0-360 degrees).
*   **s**: Saturation (0-1 as decimal).
*   **v**: Value/brightness (0-1 as decimal).
*   **r/g/b**: Calculated RGB values (0-65535).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[13/14/15]`.
    *   **Define set_hsv() function**:
        *   From **Functions**, drag `to [set_hsv] with [h] [s] [v]`.
            *   **Snap** into setup.
            *   Inside function, implement HSV→RGB conversion:
                1. Normalize H to 0-1 range: `h = h / 360`.
                2. Calculate chroma: `c = v * s`.
                3. Calculate X: `x = c * (1 - abs((h * 6) mod 2 - 1))`.
                4. Calculate m: `m = v - c`.
                5. Determine RGB' based on hue sector (0-60°, 60-120°, etc.).
                6. Convert to 16-bit: `r/g/b = (r' + m) * 65535`.
                7. `PWM Write` the calculated values.

*   **B. Main Loop Phase**
    *   Demonstrate function usage:
        *   `call set_hsv(0, 1, 1)` → Pure Red
        *   `call set_hsv(120, 1, 1)` → Pure Green
        *   `call set_hsv(240, 1, 1)` → Pure Blue
        *   `call set_hsv(60, 0.5, 0.8)` → Muted Yellow

### 9️⃣ Execution Flow (Plain English)

The `set_hsv()` function takes three intuitive parameters: Hue (color wheel angle), Saturation (color purity), and Value (brightness). Using the standard HSV-to-RGB conversion algorithm, it calculates intermediate values (chroma, X, m), determines which RGB sector the hue falls into (red-yellow, yellow-green, etc.), assigns preliminary RGB values, adds the brightness offset (m), scales to 16-bit (0-65535), and writes to PWM. This allows calling `set_hsv(180, 0.7, 0.9)` instead of manually calculating RGB (46, 230, 230), making color selection intuitive.

### 🔟 Generated Code (Reference Only)

```python
import machine

red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_hsv(h, s, v):
    h = h / 360.0
    c = v * s
    x = c * (1 - abs(((h * 6) % 2) - 1))
    m = v - c
    
    if h < 1/6:
        r_prime, g_prime, b_prime = c, x, 0
    elif h < 2/6:
        r_prime, g_prime, b_prime = x, c, 0
    elif h < 3/6:
        r_prime, g_prime, b_prime = 0, c, x
    elif h < 4/6:
        r_prime, g_prime, b_prime = 0, x, c
    elif h < 5/6:
        r_prime, g_prime, b_prime = x, 0, c
    else:
        r_prime, g_prime, b_prime = c, 0, x
    
    r = int((r_prime + m) * 65535)
    g = int((g_prime + m) * 65535)
    b = int((b_prime + m) * 65535)
    
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# Demo usage
import time
while True:
    for hue in range(0, 360, 10):
        set_hsv(hue, 1.0, 1.0)  # Full saturation/brightness, cycling hue
        time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Hue Out of Range**: If colors don't match expectations, verify hue is 0-360. Values >360 need modulo wrapping.
*   **Saturation/Value 0-1**: Ensure S and V are decimals (0.0-1.0), not percentages (0-100). Using 100 instead of 1.0 will overflow calculations.
*   **Sector Logic Errors**: If specific hue ranges show wrong colors (e.g., yellow appears cyan), check the if/elif sector boundaries (1/6, 2/6, etc.).
*   **Integer Truncation**: Use floating-point math throughout until final 16-bit conversion to avoid rounding errors.

### 1️⃣2️⃣ Try This Next

*   **Rainbow Cycle**: Loop hue from 0° to 360° at constant S=1, V=1 for full spectrum cycling.
*   **Desaturation Effect**: Gradually reduce S from 1.0 to 0.0 to fade color to white.
*   **HSL Alternative**: Implement HSL (Hue, Saturation, Lightness) conversion instead, which handles dark colors differently.

---
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_projects)

print("✅ Batch 31 COMPLETE! Projects 0307-0310 appended successfully.")
print("Total: All 10 projects (0301-0310) now in Docs_0301_0400.md")
