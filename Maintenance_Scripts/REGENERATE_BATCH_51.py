import os

def regenerate_batch_51():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    header = """#  Pico 2500: Documentation (Projects 0501-0600)

---

#  Batch 51: Digital Art 3
"""

    p0501 = """
## 1. Project 0501: Introduction to Digital Art

### 2. Learning Objective
Create a visual strobe effect by flashing White light (Red + Green + Blue) for 0.05 seconds and turning it off for 0.1 seconds to understand rapid switching and the Persistence of Vision.

### 3. Concepts Introduced
*   Strobe Effect (Persistence of Vision)
*   RGB Color Mixing (White = R+G+B)
*   Precise Millisecond Timing
*   Simultaneous Pin Control

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED (Common Cathode)
*   3x 220Ω Resistors
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red Anode** | GP16 | via 220Ω Resistor |
| **Green Anode** | GP17 | via 220Ω Resistor |
| **Blue Anode** | GP18 | via 220Ω Resistor |
| **Cathode** | GND | Ground |

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
    *   From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18).
    *   **Snap** into loop.
    *   Set all to **HIGH**.
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
5.  **Delay**: System pauses for 100ms for contrast.
6.  **Repeat**: The process repeats, creating a high-speed strobe effect.

### 10. Generated Code
```python
import machine, time
r = machine.Pin(16, machine.Pin.OUT)
g = machine.Pin(17, machine.Pin.OUT)
b = machine.Pin(18, machine.Pin.OUT)

while True:
    # White
    r.on(); g.on(); b.on()
    time.sleep(0.05)
    # Off
    r.off(); g.off(); b.off()
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Resistors**: Connecting LEDs directly to 3.3V can burn them out.
*   **Photosensitivity**: This project creates flashing lights—avoid if sensitive.

### 12. Try This Next
*   **Color Chaser**: Strobe only Red, then only Green, then only Blue.
"""

    p0502 = """
---

## 2. Project 0502: Blinking Digital Art

### 2. Learning Objective
Create a "Secondary Pulse" effect that cycles through Yellow (Red+Green), Cyan (Green+Blue), and Magenta (Red+Blue) to understand additive color mixing.

### 3. Concepts Introduced
*   Secondary Color Theory (CMY)
*   Sequential Logic
*   State Alternation
*   Multi-Channel coordination

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red** | GP16 | - |
| **Green** | GP17 | - |
| **Blue** | GP18 | - |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
    *   From **Smart IO**, set GP16-18 as Output.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Yellow**:
    *   From **Smart IO**, set GP16=HIGH, GP17=HIGH, GP18=LOW.
    *   **Snap** into `pico_forever`.
    *   Wait 0.5s.
2.  **Cyan**:
    *   From **Smart IO**, set GP16=LOW, GP17=HIGH, GP18=HIGH.
    *   **Snap** below.
    *   Wait 0.5s.
3.  **Magenta**:
    *   From **Smart IO**, set GP16=HIGH, GP17=LOW, GP18=HIGH.
    *   **Snap** below.
    *   Wait 0.5s.

### 9. Execution Flow
1.  **Start**: System initializes pins.
2.  **Frame 1**: Red and Green mix to form Yellow.
3.  **Frame 2**: Green and Blue mix to form Cyan.
4.  **Frame 3**: Red and Blue mix to form Magenta.
5.  **Loop**: The cycle repeats using the CMY color model.

### 10. Generated Code
```python
import machine, time
r = machine.Pin(16, machine.Pin.OUT)
g = machine.Pin(17, machine.Pin.OUT)
b = machine.Pin(18, machine.Pin.OUT)

while True:
    # Yellow
    r.on(); g.on(); b.off()
    time.sleep(0.5)
    # Cyan
    r.off(); g.on(); b.on()
    time.sleep(0.5)
    # Magenta
    r.on(); g.off(); b.on()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Logic Overlap**: Forgetting to turn off the "Red" pin when switching to Cyan results in White (R+G+B).

### 12. Try This Next
*   **All Colors**: Cycle Red -> Yellow -> Green -> Cyan -> Blue -> Magenta -> White.
"""

    p0503 = """
---

## 3. Project 0503: Manual Digital Art Control

### 2. Learning Objective
Build a "Color Paddle" controller where three separate buttons toggle the Red, Green, and Blue components individually to mix any of the 8 basic colors manually.

### 3. Concepts Introduced
*   Bitwise State Control
*   Toggle Logic
*   Input-Output Mapping
*   Manual Synthesis

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x Buttons

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Red** | GP13 | Toggle Red |
| **Btn Green** | GP14 | Toggle Green |
| **Btn Blue** | GP15 | Toggle Blue |
| **RGB LED** | GP16-18 | Output |

### 6. Blocks Used
*   **from Logic, drag `if_do`**
*   **from Variables, drag `set_variable`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **r_on**, **g_on**, **b_on**: Boolean (State)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init State**:
    *   From **Variables**, set `r_on`, `g_on`, `b_on` to FALSE.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Check Red**:
    *   From **Logic**, drag `if_do`.
    *   If `pico_gpio_read`(13) is HIGH:
        *   Set `r_on` to NOT `r_on`.
        *   Wait 0.2s (Debounce).
2.  **Check Green**:
    *   Similar logic for GP14 and `g_on`.
3.  **Check Blue**:
    *   Similar logic for GP15 and `b_on`.
4.  **Update Hardware**:
    *   From **Smart IO**, set GP16 to `r_on`.
    *   From **Smart IO**, set GP17 to `g_on`.
    *   From **Smart IO**, set GP18 to `b_on`.

### 9. Execution Flow
1.  **Input**: User presses the "Green" button.
2.  **Logic**: The `g_on` variable flips from False to True.
3.  **Output**: The Green channel of the LED turns on.
4.  **Mixing**: If "Red" was already on, the light becomes Yellow. If "Blue" was on, it becomes Cyan.

### 10. Generated Code
```python
import machine, time
br = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
bg = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bb = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
lr = machine.Pin(16, machine.Pin.OUT)
lg = machine.Pin(17, machine.Pin.OUT)
lb = machine.Pin(18, machine.Pin.OUT)

rs, gs, bs = False, False, False

while True:
    if br.value(): rs = not rs; time.sleep(0.2)
    if bg.value(): gs = not gs; time.sleep(0.2)
    if bb.value(): bs = not bs; time.sleep(0.2)
    
    lr.value(rs); lg.value(gs); lb.value(bs)
```

### 11. Common Mistakes
*   **No Debounce**: A single press flips the light on and off rapidly.

### 12. Try This Next
*   **Master Off**: Add a 4th button that resets all variables to False.
"""

    p0504 = """
---

## 4. Project 0504: Digital Art Sequences

### 2. Learning Objective
Simulate a "Campfire" by using randomized PWM values where Red is always brighter than Green, creating organic Orange/Gold flickering.

### 3. Concepts Introduced
*   Procedural Texture Generation
*   Color Temperature Rules (Red > Green)
*   Randomized Timing
*   Natural Simulation

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red** | GP16 | PWM |
| **Green** | GP17 | PWM |
| **Blue** | GP18 | Off |

### 6. Blocks Used
*   **from Math, drag `random_integer`**
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **flicker**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Blue Off**:
    *   Set GP18 LOW.

**B. Main Loop Phase**
1.  **Calc Red**:
    *   From **Smart IO**, set `pico_pwm_write` GP16 to **Math** `random_integer`(40000, 65535).
2.  **Calc Green**:
    *   From **Smart IO**, set `pico_pwm_write` GP17 to **Math** `random_integer`(5000, 20000).
    *   *Note*: Keeping Green lower than Red ensures orange/yellow hues, not lime.
3.  **Flicker Wait**:
    *   From **Time**, wait `random_integer`(50, 200) / 1000 seconds.

### 9. Execution Flow
1.  **Generate**: The system picks a bright Red value and a dim Green value.
2.  **Mix**: High Red + Low Green = Orange/Gold.
3.  **Timing**: The chaotic wait times make the light "dance" like a real flame.

### 10. Generated Code
```python
import machine, time, random
r = machine.PWM(machine.Pin(16)); r.freq(1000)
g = machine.PWM(machine.Pin(17)); g.freq(1000)
machine.Pin(18, machine.Pin.OUT).off()

while True:
    r.duty_u16(random.randint(40000, 65535))
    g.duty_u16(random.randint(5000, 20000))
    time.sleep(random.uniform(0.05, 0.2))
```

### 11. Common Mistakes
*   **Too Much Green**: If Green > Red, the fire looks radioactive/toxic.

### 12. Try This Next
*   **Wind Gusts**: Occasionally dim both channels significantly to simulate wind blowing the fire low.
"""

    p0505 = """
---

## 5. Project 0505: Interactive Digital Art

### 2. Learning Objective
Build a "Light Painter" that activates an RGB sequence only when the room is dark (detected via LDR), saving power during the day.

### 3. Concepts Introduced
*   Environmental Gating
*   Threshold Comparison
*   Energy Efficiency Logic
*   Sensor Integration

### 4. Hardware Required
*   Raspberry Pi Pico
*   LDR + Resistor
*   RGB LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR** | GP26 | ADC Input |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Logic, drag `if_else`**

### 7. Variables
*   **light**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Ref GP26 as ADC.

**B. Main Loop Phase**
1.  **Read LDR**:
    *   Set `light` to `pico_adc_read`(26).
2.  **Check Dark**:
    *   If `light` < 20000 (Adjust for room):
        *   **Action**: Turn on RGB Sequence (e.g., Fade colors).
    *   Else:
        *   **Action**: Turn OFF all LEDs.
3.  **Wait**: 0.5s.

### 9. Execution Flow
1.  **Monitor**: The Pico checks ambient light levels.
2.  **Gate**: If it's bright (Day), the code takes the "Else" path and ensures LEDs are off.
3.  **Trigger**: If it's dark (Night), the "Do" path runs, activating the light art.

### 10. Generated Code
```python
import machine, time
ldr = machine.ADC(26)
r = machine.Pin(16, machine.Pin.OUT)
# ... init others

while True:
    if ldr.read_u16() < 20000:
        r.on() # Or sequence
    else:
        r.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Inverse Logic**: Depending on LDR wiring (Pull-up vs Pull-down), "Dark" might be high voltage or low voltage.

### 12. Try This Next
*   **Hysteresis**: Add a buffer so it doesn't flicker at dusk.
"""

    p0506 = """
---

## 6. Project 0506: Smart Digital Art Switch

### 2. Learning Objective
Create a "Mood Selector" where a switch toggles between two thematic profiles: "Calm" (Slow Blue Fade) and "Energy" (Fast Red Flash).

### 3. Concepts Introduced
*   Profile Switching
*   State Management
*   Thematic Logic
*   Loop-in-Loop structures

### 4. Hardware Required
*   Pico, RGB LED, Switch

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Switch** | GP15 | Input |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Loops, drag `count_with`**

### 7. Variables
*   **mode**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **None**.

**B. Main Loop Phase**
1.  **Read Switch**:
    *   If GP15 is HIGH ("Energy"):
        *   **Action**: Flash Red (ON, wait 0.1, OFF, wait 0.1).
    *   Else ("Calm"):
        *   **Action**: Fade Blue (PWM 0->65000->0 over 2 seconds).

### 9. Execution Flow
1.  **Limit**: The loop checks the switch at the start of every cycle.
2.  **Branch**: It enters either the "Energy" block or the "Calm" block.
3.  **Exit**: Once the animation for that block finishes, it checks the switch again.

### 10. Generated Code
```python
import machine, time
sw = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
r = machine.Pin(16, machine.Pin.OUT)
b = machine.PWM(machine.Pin(18)); b.freq(1000)

while True:
    if sw.value():
        # Energy
        r.on(); time.sleep(0.1)
        r.off(); time.sleep(0.1)
    else:
        # Calm
        for i in range(0, 65000, 1000):
            b.duty_u16(i); time.sleep(0.01)
        for i in range(65000, 0, -1000):
            b.duty_u16(i); time.sleep(0.01)
```

### 11. Common Mistakes
*   **Latency**: The switch only works *after* the current fade finishes (could be 2 seconds).

### 12. Try This Next
*   **Interrupts**: Use IRQ to make the switch instant.
"""

    p0507 = """
---

## 7. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Implement a "Color Code Alarm" logic. specific combination of buttons triggers a specific color. A=Red, B=Blue, A+B=Purple.

### 3. Concepts Introduced
*   Combinatorial Logic (AND conditions)
*   Priority Encoding
*   Input Masking

### 4. Hardware Required
*   Pico, 2 Buttons, RGB LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn A** | GP14 | - |
| **Btn B** | GP15 | - |

### 6. Blocks Used
*   **from Logic, drag `if_else_if`**
*   **from Logic, drag `and`**

### 7. Variables
*   **None**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Inputs GP14, 15. Outputs GP16-18.

**B. Main Loop Phase**
1.  **Check Combo**:
    *   If GP14 AND GP15:
        *   Set **Purple** (R+B).
    *   Else If GP14:
        *   Set **Red**.
    *   Else If GP15:
        *   Set **Blue**.
    *   Else:
        *   Set **Off**.

### 9. Execution Flow
1.  **Priority**: The code *must* check "A AND B" first. If it checked "A" first, it would turn Red even if B was also pressed.
2.  **Output**: Correctly reflects the combination of inputs.

### 10. Generated Code
```python
import machine
a = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
r = machine.Pin(16, machine.Pin.OUT)
bl = machine.Pin(18, machine.Pin.OUT)

while True:
    if a.value() and b.value():
        r.on(); bl.on()
    elif a.value():
        r.on(); bl.off()
    elif b.value():
        r.off(); bl.on()
    else:
        r.off(); bl.off()
```

### 11. Common Mistakes
*   **Order of Operations**: Putting the single-button checks before the double-button check breaks the logic.

### 12. Try This Next
*   **Password**: Sequence A -> B -> A to unlock Green.
"""

    p0508 = """
---

## 8. Project 0508: The Digital Art Game

### 2. Learning Objective
Create a "Reaction Color" game. The Pico flashes a random color. The user must press the button ONLY if the color is Green.

### 3. Concepts Introduced
*   Go/No-Go Testing
*   Reaction Time Measurement
*   Random State Geneartion
*   Input Validation

### 4. Hardware Required
*   Pico, RGB LED, Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP15 | Reaction |

### 6. Blocks Used
*   **from Math, drag `random_integer`**
*   **from Loops, drag `break`**

### 7. Variables
*   **color**: Integer (1=Red, 2=Green, 3=Blue)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep**: All Off.

**B. Main Loop Phase**
1.  **Select**: `color` = random(1, 3).
2.  **Display**:
    *   If 1: Red. If 2: Green. If 3: Blue.
3.  **Window**:
    *   Wait 0.5s. During this time check button.
    *   If Button AND `color` == 2 (Green): **WIN** (Flash White).
    *   If Button AND `color` != 2 (Red/Blue): **LOSE** (Flash Red long).
4.  **Reset**: Wait random time.

### 9. Execution Flow
1.  **Stimulus**: System presents a color.
2.  **Decision**: User creates a mental filter: "Is it Green?".
3.  **Action**: User presses or inhibits press.
4.  **Feedback**: System rewards correct action or punishes error.

### 10. Generated Code
```python
import machine, time, random
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
# ... led setup ...
while True:
    c = random.randint(1, 3)
    # Set Color Logic (1=R, 2=G, 3=B)
    time.sleep(0.5) # Wait for react
    if btn.value():
        if c == 2:
            print("WIN")
        else:
            print("FAIL")
    time.sleep(1)
```

### 11. Common Mistakes
*   **Holding Button**: Cheating by holding the button down. Needs edge detection.

### 12. Try This Next
*   **Speed Up**: Decrease the 0.5s window every level.
"""

    p0509 = """
---

## 9. Project 0509: Automated Digital Art

### 2. Learning Objective
Create a "Day Cycle" simulator that transitions from Sunrise (Orange) to Noon (White) to Sunset (Red) to Night (Blue) over a 20-second period.

### 3. Concepts Introduced
*   Temporal Sequencing
*   Color Temperature Modeling
*   Long-duration Simulation
*   State Machines

### 4. Hardware Required
*   Pico, RGB LED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **None**.

**B. Main Loop Phase**
1.  **Sunrise (0-5s)**:
    *   Fade Red 0->100%, Green 0->50%. (Orange).
2.  **Noon (5-10s)**:
    *   Fade Green 50->100%, Blue 0->100%. (White).
3.  **Sunset (10-15s)**:
    *   Fade Green 100->0%, Blue 100->0%. (Red).
4.  **Night (15-20s)**:
    *   Fade Red 100->0%, Blue 0->50%. (Dim Blue).

### 9. Execution Flow
1.  **Process**: The code continuously updates PWM duty cycles to transition smoothly between predefined "Keyframes".
2.  **Visual**: The LED mimics the sky's color evolution.

### 10. Generated Code
```python
# Simplified linear interpolation logic in Python
```

### 11. Common Mistakes
*   **Jerky transitions**: Using large step sizes.

### 12. Try This Next
*   **Moon Phase**: Modulate the brightness of the "Night" blue to simulate moon cycle.
"""

    p0510 = """
---

## 10. Project 0510: Mastering Digital Art

### 2. Learning Objective
Develop a "Custom Shade" function where an input `intensity` (0-100) scales specific color channels (Purple) dynamically.

### 3. Concepts Introduced
*   Parametric Functions
*   Scaling Calculations
*   Code Reusability
*   Input-Driven Output

### 4. Hardware Required
*   Pico, RGB LED

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Func Def**: Define `set_purple(intensity)`.

**B. Main Loop Phase**
1.  **Sweep**:
    *   Loop `i` from 0 to 100.
    *   Call `set_purple(i)`.
    *   Wait 0.01s.

**C. Function Logic**:
1.  **Scale**:
    *   `r_val = intensity * 655` (Map 100 to 65535).
    *   `b_val = intensity * 655`.
    *   `g_val = 0`.
2.  **Apply**: Write to hardware.

### 9. Execution Flow
1.  **Abstraction**: The main loop doesn't know *how* to make purple, it just asks for "Purple at 50%".
2.  **Translation**: The function translates that high-level request into specific hardware voltages.

### 10. Generated Code
```python
import machine, time
r = machine.PWM(machine.Pin(16)); r.freq(1000)
g = machine.PWM(machine.Pin(17)); g.freq(1000)
b = machine.PWM(machine.Pin(18)); b.freq(1000)

def set_purple(intensity): # 0-100
    duty = int(intensity * 655.35)
    r.duty_u16(duty)
    b.duty_u16(duty)
    g.duty_u16(0)

while True:
    for i in range(101):
        set_purple(i)
        time.sleep(0.01)
    for i in range(100, -1, -1):
        set_purple(i)
        time.sleep(0.01)
```

### 11. Common Mistakes
*   **Integer Math**: Scaling 100 to 65535 requires float math or precise multiplication, or `map`.

### 12. Try This Next
*   **Multi-Function**: Add `set_orange(intensity)`.
"""

    full_content = header + p0501 + p0502 + p0503 + p0504 + p0505 + p0506 + p0507 + p0508 + p0509 + p0510

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(full_content)

if __name__ == "__main__":
    regenerate_batch_51()
