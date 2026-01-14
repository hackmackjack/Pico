import os

def fix_batch51_part2():
    file_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find start of Project 0507
    cutoff_index = -1
    for i, line in enumerate(lines):
        if "## 1. Project 0507:" in line:
            cutoff_index = i
            break
            
    if cutoff_index == -1:
        print("Error: Could not find Project 0507 start.")
        return

    # Keep content up to 0506 (inclusive)
    kept_lines = lines[:cutoff_index]
    
    # ---------------------------------------------------------
    # NEW ELITE-COMPLIANT CONTENT FOR 0507-0510
    # ---------------------------------------------------------
    
    p0507 = """
## 1. Project 0507: Digital Art Alarm System

### 2. Learning Objective
Build a visual alarm system where specific button combinations trigger distinct color modes (Red, Blue, or Purple).

### 3. Concepts Introduced
*   Combinatorial Logic (AND, NOT)
*   Truth Tables
*   Multi-Input Handling
*   Conditional Logic (`if/elif/else`)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   2x Push Buttons (Labelled A and B)
*   3x 220Ω Resistors (for LED)
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Input (Pull-Down) |
| **Button B** | GP15 | Input (Pull-Down) |
| **Red LED** | GP16 | Connected via 220Ω resistor |
| **Blue LED** | GP18 | Connected via 220Ω resistor |

### 6. Blocks Used
*   **from Logic, drag `and_operation`** (Check multiple conditions)
*   **from Logic, drag `if_elseif`** (Multi-branch decision)
*   **from Smart IO, drag `pico_gpio_read`** (Read Input)
*   **from Smart IO, drag `pico_gpio_write`** (Set Output)

### 7. Variables
*   **btn_a**: Boolean (State of Button A)
*   **btn_b**: Boolean (State of Button B)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Inputs**:
    *   From **Smart IO**, drag `pico_gpio_read`.
        *   **Snap** into `start` slot.
        *   Configure GP14 and GP15 as **Input (Pull-Down)**.
2.  **Configure Outputs**:
    *   From **Smart IO**, drag `pico_gpio_write`.
        *   **Snap** below.
        *   Configure GP16 (Red) and GP18 (Blue) as **Outputs**.

**B. Main Loop Phase**
3.  **Read Buttons**:
    *   From **Smart IO**, drag `pico_gpio_read`.
        *   **Snap** into loop.
        *   Read GP14 into variable `btn_a`.
    *   Duplicate and read GP15 into variable `btn_b`.
4.  **Check Combination (Priority)**:
    *   From **Logic**, drag `if_elseif`.
        *   **Snap** below reading.
        *   Condition 1: `btn_a` AND `btn_b` (Both pressed).
5.  **Action: Purple Alarm**:
    *   From **Smart IO**, drag `pico_gpio_write`.
        *   **Snap** into first branch.
        *   Set Red HIGH, Blue HIGH (Purple).
6.  **Check Single Buttons**:
    *   Add `else if` branch.
    *   Condition 2: `btn_a` is TRUE.
        *   Action: Set Red HIGH, Blue LOW.
    *   Add `else if` branch.
    *   Condition 3: `btn_b` is TRUE.
        *   Action: Set Red LOW, Blue HIGH.
7.  **Default State (Else)**:
    *   Add `else` branch.
        *   Action: Set Red LOW, Blue LOW (All Off).
8.  **Wait**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below logic block.
        *   Wait 0.1 seconds.

### 9. Execution Flow
1.  **Start**: Pico configures inputs and outputs.
2.  **Scan**: System reads current state of Button A and Button B.
3.  **Evaluate**:
    *   Checks if **BOTH** are pressed first (highest priority).
    *   If not, checks A only.
    *   If not, checks B only.
4.  **Output**: Sets the LED color matching the valid condition.
5.  **Repeat**: Loops back to scanning constraints.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialize Hardware
button_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_b = Pin(15, Pin.IN, Pin.PULL_DOWN)
red = Pin(16, Pin.OUT)
blue = Pin(18, Pin.OUT)

while True:
    # Read Inputs
    btn_a = button_a.value()
    btn_b = button_b.value()
    
    # Priority Logic
    if btn_a and btn_b:
        # Both = Purple
        red.on()
        blue.on()
    elif btn_a:
        # A = Red
        red.on()
        blue.off()
    elif btn_b:
        # B = Blue
        red.off()
        blue.on()
    else:
        # None = Off
        red.off()
        blue.off()
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Logic Order**: Putting the single checks (`if A`) before the combined check (`if A and B`). If you check A first, the code might stop there and never see that B is also pressed.
*   **Missing Pull-Downs**: Buttons floating HIGH will cause false alarms.

### 12. Try This Next
*   **Latching Alarm**: Change code so the alarm stays ON until a reset button is pressed.
"""

    p0508 = """
---

## 1. Project 0508: The Digital Art Game

### 2. Learning Objective
Create a reaction time game where the player must press a button ONLY when the LED is Green.

### 3. Concepts Introduced
*   Game Loops (State Logic)
*   Reaction Time Measurement
*   Conditional Success/Fail
*   Randomness (`random.randint`)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   1x Push Button
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Input (Pull-Down) |
| **Red LED** | GP16 | Output |
| **Green LED** | GP17 | Output |
| **Blue LED** | GP18 | Output |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (Generate random number)
*   **from Loops, drag `repeat_while`** (Conditional loop)
*   **from Text, drag `print`** (Console output)
*   **from Time, drag `pico_seconds`** (Get timestamp)

### 7. Variables
*   **color_code**: Integer (0=Red, 1=Green, 2=Blue)
*   **score**: Integer (Player points)
*   **pressed**: Boolean (Button flag)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
    *   From **Smart IO**, configure GP14 (In), GP16-18 (Out).
2.  **Init Score**:
    *   From **Variables**, set `score` to 0.

**B. Main Loop Phase**
3.  **Pick Color**:
    *   From **Math**, set `color_code` to random integer (0 to 2).
4.  **Display Color**:
    *   From **Control**, use `if` blocks to turn on Red (if 0), Green (if 1), or Blue (if 2).
5.  **Wait Window**:
    *   From **Time**, drag `pico_wait`.
    *   Wait random duration (0.5 to 1.5s).
    *   *Note: In advanced version, we check button continuously here.*
6.  **Check Input**:
    *   From **Logic**, drag `if_else`.
    *   Condition: If `pico_gpio_read` (GP14) is TRUE.
7.  **Judge Result**:
    *   **If Pressed**:
        *   If `color_code` == 1 (Green): Increment `score`, Flash White (Win).
        *   Else: Set `score` to 0, Flash Red (Loss).
8.  **Reset**:
    *   Turn all LEDs OFF.
    *   Wait 0.5s.

### 9. Execution Flow
1.  **Challenge**: System selects and displays a random color.
2.  **Window**: Player has a short window to react.
3.  **Action**: Player presses (or doesn't press) the button.
4.  **Verdict**:
    *   Green + Press = Point.
    *   Red/Blue + Press = Fail.
5.  **Feedback**: LED flashes to indicate Win/Loss.

### 10. Generated Code
```python
from machine import Pin
import time
import random

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)
leds = [red, green, blue]

score = 0

while True:
    # 1. Pick Color
    target = random.randint(0, 2)
    for i in range(3):
        leds[i].value(1 if i == target else 0)
        
    # 2. Reaction Window (Simplified)
    # Checks if button held at END of delay for basic version
    time.sleep(random.uniform(0.5, 1.0))
    is_pressed = btn.value()
    
    # 3. Judge
    if is_pressed:
        if target == 1: # Green
            score += 1
            print("Score:", score)
            # Win Flash
            red.on(); green.on(); blue.on()
            time.sleep(0.2)
        else:
            score = 0
            print("Game Over")
            # Fail Flash (Red)
            red.on(); green.off(); blue.off()
            time.sleep(0.5)
            
    # 4. Reset
    red.off(); green.off(); blue.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Mismatched Indices**: Remembering that 0=Red, 1=Green is arbitrary—make sure code matches your plan.
*   **Simple Logic**: This basic version checks button at the *end* of the wait. If you press and release too fast, it misses. (Advanced: Use interrupts).

### 12. Try This Next
*   **High Score**: Save the highest score reached to a variable.
"""

    p0509 = """
---

## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Create a time-based "Day/Night Cycle" simulator that smoothly transitions between predefined color palettes (Sunrise, Noon, Sunset, Night).

### 3. Concepts Introduced
*   State Machines (Sequential Logic)
*   Color Temperature (Warm vs Cool)
*   PWM Mixing (Creating shades)
*   Automated Timing

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | PWM Output |
| **Green LED** | GP17 | PWM Output |
| **Blue LED** | GP18 | PWM Output |

### 6. Blocks Used
*   **from Functions, drag `to_procedure`** (Create named function)
*   **from Smart IO, drag `pico_pwm_write`** (Analog write)
*   **from Time, drag `pico_wait`** (Delay)

### 7. Variables
*   **None**: Direct output control via functions.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, setup GP16, GP17, GP18 with 1000Hz frequency.

**B. Define Helper Function**
2.  **Create Function "SetColor"**:
    *   From **Functions**, drag `to_procedure` "SetColor" with inputs `r`, `g`, `b`.
    *   Inside, add **Smart IO** blocks to set GP16=`r`, GP17=`g`, GP18=`b`.

**C. Main Loop Phase**
3.  **Sunrise (Orange)**:
    *   Call `SetColor(60000, 20000, 0)`.
    *   From **Time**, wait 3 seconds.
4.  **Noon (White)**:
    *   Call `SetColor(65535, 65535, 65535)`.
    *   From **Time**, wait 3 seconds.
5.  **Sunset (Purple/Red)**:
    *   Call `SetColor(50000, 0, 10000)`.
    *   From **Time**, wait 3 seconds.
6.  **Night (Dim Blue)**:
    *   Call `SetColor(0, 0, 10000)`.
    *   From **Time**, wait 3 seconds.

### 9. Execution Flow
1.  **Start**: System initializes PWM drivers.
2.  **State 1 (Sunrise)**: High Red + Low Green creates warm Orange.
3.  **State 2 (Noon)**: All Max creates bright White.
4.  **State 3 (Sunset)**: Red + Blue creates dramatic Purple.
5.  **State 4 (Night)**: Low Blue creates moonlight effect.
6.  **Loop**: Cycle repeats endlessly.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Init PWM
r = PWM(Pin(16)); r.freq(1000)
g = PWM(Pin(17)); g.freq(1000)
b = PWM(Pin(18)); b.freq(1000)

def set_color(rv, gv, bv):
    r.duty_u16(rv)
    g.duty_u16(gv)
    b.duty_u16(bv)

while True:
    # Sunrise
    set_color(60000, 20000, 0)
    time.sleep(3)
    
    # Noon
    set_color(65535, 65535, 65535)
    time.sleep(3)
    
    # Sunset
    set_color(50000, 0, 10000)
    time.sleep(3)
    
    # Night
    set_color(0, 0, 10000)
    time.sleep(3)
```

### 11. Common Mistakes
*   **Mixing Colors**: Forgetting that Green is very bright. Use less Green than Red to make Orange.
*   **PWM Range**: MicroPython uses 0-65535, not 0-255.

### 12. Try This Next
*   **Weather Effects**: Add a random "Thunderstorm" state (flickering white) during the Night phase.
"""

    p0510 = """
---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Create a "Parametric Color Mixer" where a mathematical loop automatically generates a smooth cross-fade gradient between colors.

### 3. Concepts Introduced
*   Linear Interpolation (Fading)
*   For Loops (Iteration)
*   Mathematical Mapping
*   Inverse Relationships (As A goes up, B goes down)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | PWM Output |
| **Blue LED** | GP18 | PWM Output |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (For loop)
*   **from Math, drag `arithmetic`** (Multiplication/Subtraction)
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **i**: Integer (Loop counter 0-100)
*   **red_val**: Integer (Calculated brightness)
*   **blue_val**: Integer (Calculated brightness)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, setup GP16 and GP18 (1000Hz).

**B. Main Loop Phase**
2.  **Fade Red to Blue**:
    *   From **Loops**, drag `count_with` variable `i` from 0 to 100.
    *   **Calculate Blue**: Scale `i` (0-100) to PWM (0-65000).
        *   Math: `i * 650`.
    *   **Calculate Red**: Scale `100 - i` to PWM.
        *   Math: `(100 - i) * 650`.
    *   **Apply**:
        *   From **Smart IO**, set GP18 (Blue) to `blue_val`.
        *   From **Smart IO**, set GP16 (Red) to `red_val`.
    *   **Wait**: 0.05s.
3.  **Fade Blue to Red**:
    *   Repeat the loop but swap the logic (or count backwards).

### 9. Execution Flow
1.  **Init**: Pico sets up localized PWM.
2.  **Loop Start**: `i` starts at 0.
3.  **Math**:
    *   At i=0: Red is Max (100%), Blue is Min (0%).
    *   At i=50: Red is 50%, Blue is 50% (Purple).
    *   At i=100: Red is 0%, Blue is Max (100%).
4.  **Result**: The LED smoothly transitions from Red to Purple to Blue.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

r = PWM(Pin(16)); r.freq(1000)
b = PWM(Pin(18)); b.freq(1000)

while True:
    # 0 to 100% Blue, 100 to 0% Red
    for i in range(101):
        blue_v = int(i * 650)
        red_v = int((100 - i) * 650)
        
        b.duty_u16(blue_v)
        r.duty_u16(red_v)
        time.sleep(0.05)
        
    # Reverse
    for i in range(101):
        blue_v = int((100 - i) * 650)
        red_v = int(i * 650)
        
        b.duty_u16(blue_v)
        r.duty_u16(red_v)
        time.sleep(0.05)
```

### 11. Common Mistakes
*   **Math Integers**: MicroPython requires PWM duty to be an integer (`int()`), but math operations often result in floats (`650.0`). Code will crash if not converted.

### 12. Try This Next
*   **3-Way Fade**: Add Green and fade Red->Green->Blue->Red.
"""

    # Combine and Write
    new_content = "".join(kept_lines) + p0507 + p0508 + p0509 + p0510
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Projects 0507-0510 fixed with Elite Standard v2.0.")

if __name__ == "__main__":
    fix_batch51_part2()
