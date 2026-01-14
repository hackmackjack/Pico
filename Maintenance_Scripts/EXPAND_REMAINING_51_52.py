import os
import re

def expand_remaining_51_52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Data for remaining projects in Batch 51 and 52
    
    p0504 = """
## 4. Project 0504: Digital Art Sequences

### 2. Learning Objective
Programm a "Campfire" simulation by using randomized PWM values across Red and Green channels to create fluctuating warm color shades.

### 3. Concepts Introduced
*   Randomized PWM
*   Color Temperature Modeling (Warmth)
*   Visual Flicker Simulation
*   Probability-based Wait Intervals

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | PWM Output |
| **Green LED** | GP17 | PWM Output |
| **Blue LED** | GP18 | Permanently Off |

### 6. Blocks Used
*   **from Math, drag `random_integer`**
*   **from Smart IO, drag `pico_pwm_write`**
*   **from Time, drag `pico_wait`** (Random duration)

### 7. Variables
*   **r_val**: Integer (Red brightness)
*   **g_val**: Integer (Green brightness)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, drag `pico_pwm_write` GP16 and GP17.
    *   **Snap** into `start` block.
2.  **Ensure Blue Off**:
    *   From **Smart IO**, drag `pico_gpio_write` GP18.
    *   **Snap** below PWM blocks. Set to LOW.

**B. Main Loop Phase**
1.  **Generate Flame Color**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** into loop.
    *   From **Variables**, set `r_val` to **Math** `random_integer` 40000 to 65535.
    *   From **Variables**, set `g_val` to **Math** `random_integer` 0 to 15000.
2.  **Update Hardware**:
    *   From **Smart IO**, drag `pico_pwm_write` GP16.
    *   **Snap** below variables. Set to `r_val`.
    *   From **Smart IO**, drag `pico_pwm_write` GP17.
    *   **Snap** below GP16. Set to `g_val`.
3.  **Create Flicker**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below PWM updates.
    *   Set Value to **Math** `random_integer` 0.05 to 0.2.

### 9. Execution Flow
1.  **Start**: The Pico initializes PWM channels. Blue is disabled to keep colors "Warm."
2.  **Process**: The system picks a high red value and a low green value, which mix to create orange/gold tones.
3.  **Process**: The system applies these values to the RGB LED.
4.  **Action**: The system waits a random fraction of a second, mimicking the erratic movement of fire.
5.  **Output**: The LED appears to "flicker" like a campfire.

### 10. Generated Code
```python
import machine, time, random
r = machine.PWM(machine.Pin(16)); r.freq(1000)
g = machine.PWM(machine.Pin(17)); g.freq(1000)
while True:
    r.duty_u16(random.randint(40000, 65535))
    g.duty_u16(random.randint(0, 15000))
    time.sleep(random.uniform(0.05, 0.2))
```

### 11. Common Mistakes
*   **High Green Values**: Setting green too high makes the "fire" look neon yellow or lime. Keep it below 20000.

### 12. Try This Next
*   **Embers**: Add a 3rd phase that occasionally dips both R and G to very low values before surging back.
"""

    p0505 = """
---

## 5. Project 0505: Interactive Digital Art

### 2. Learning Objective
Create a "Mood Lamp" where three separate buttons toggle the Red, Green, and Blue channels independently to create 7 different mixed colors.

### 3. Concepts Introduced
*   Logical Toggling
*   Multi-State Variables
*   Binary Color Combination
*   Input Interrupt (Debouncing)

### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x Buttons

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **R-Button** | GP13 | Toggle Red |
| **G-Button** | GP14 | Toggle Green |
| **B-Button** | GP15 | Toggle Blue |

### 6. Blocks Used
*   **from Logic, drag `if_do`**
*   **from Variables, drag `set_variable`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **r_state, g_state, b_state**: Boolean (ON/OFF)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   From **Smart IO**, set GP13, 14, 15 as Inputs.
    *   Set GP16, 17, 18 as Outputs.
2.  **Set Defaults**:
    *   From **Variables**, set `r_state`, `g_state`, `b_state` to FALSE.

**B. Main Loop Phase**
1.  **Monitor Red**:
    *   From **Loops**, drag `pico_forever`.
    *   If **Smart IO** `pico_gpio_read` 13 is HIGH:
        *   **Action**: Set `r_state` to NOT `r_state`.
        *   Wait 0.2s.
2.  **Monitor Others**:
    *   Repeat Step 1 for Green (GP14) and Blue (GP15).
3.  **Update Hardware**:
    *   From **Smart IO**, drag `pico_gpio_write` GP16.
    *   **Snap** below checks. Set to `r_state`.
    *   (Repeat for GP17/18).

### 9. Execution Flow
1.  **Start**: All LEDs are off.
2.  **Input**: User presses the Red button.
3.  **Process**: The `r_state` variable flips from FALSE to TRUE.
4.  **Output**: The Red LED turns on.
5.  **Combo**: User then presses the Blue button. The Red stays on, and now Blue turns on, creating Magenta.

### 10. Generated Code
```python
import machine, time
btn_r = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_r = machine.Pin(16, machine.Pin.OUT)
sr = False
while True:
    if btn_r.value():
        sr = not sr; time.sleep(0.2)
    led_r.value(sr)
```

### 11. Common Mistakes
*   **Flickering**: Without the 0.2s "Wait," the light will strobe between ON and OFF while you hold the button.

### 12. Try This Next
*   **Auto-Cycle**: Add a 4th button that starts a slow cross-fade between colors.
"""

    p0514 = """
---

## 4. Project 0514: Loading Bar

### 2. Learning Objective
Programm a horizontally expanding "Progress Bar" on the OLED that fills up from 0 to 100 pixels in 5 seconds.

### 3. Concepts Introduced
*   Geometric Scaling
*   Visual Feedback Systems
*   Progress Logic
*   Coordinate Constraints

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | - |

### 6. Blocks Used
*   **from Display, drag `pico_oled_fill_rect`**
*   **from Loops, drag `count_with`** (for loops)

### 7. Variables
*   **progress**: Integer (Current width)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Frame**:
    *   From **Display**, drag `pico_oled_rect`.
    *   **Snap** into `start`. Set X=10, Y=30, W=100, H=10.

**B. Main Loop Phase**
1.  **Define Counter**:
    *   From **Loops**, drag `count_with`.
    *   Variable: `progress`, From: 0, To: 100.
2.  **Render Bar**:
    *   From **Display**, drag `pico_oled_clear`.
    *   Redraw housing `rect` (Step A.1).
    *   From **Display**, drag `pico_oled_fill_rect`.
    *   **Snap** into loop.
    *   Set X=10, Y=30, W=`progress`, H=10.
3.  **Show**:
    *   From **Display**, drag `pico_oled_show`. Wait 0.05s.

### 9. Execution Flow
1.  **Start**: Screen displays an empty white outline box.
2.  **Process**: The loop begins at zero and adds 1 to the 'width' every 50ms.
3.  **Output**: A solid white bar grows inside the box.
4.  **Reaction**: The user sees a smooth "Loading" animation.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for w in range(101):
        oled.fill(0); oled.rect(10, 30, 100, 10, 1); oled.fill_rect(10, 30, w, 10, 1); oled.show()
        time.sleep(0.05)
```

### 11. Common Mistakes
*   **Wrong Height**: Making the filled bar taller than the outline frame.

### 12. Try This Next
*   **Percent Text**: Add a `pico_oled_text` block above the bar that displays "Loading... [progress]%".
"""

    p0518 = """
---

## 8. Project 0518: The Animation Game

### 2. Learning Objective
Build a "Falling Object" game where the player must dodge a falling dot by moving their own sprite left and right using buttons.

### 3. Concepts Introduced
*   Collision Detection
*   Game States (Reset logic)
*   Positional Comparison
*   Coordinate Update Loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Left** | GP14 | Move player |
| **Btn Right**| GP15 | Move player |

### 6. Blocks Used
*   **from Logic, drag `if_else`** (Collision)
*   **from Variables, drag `change_variable`**
*   **from Display, drag `pico_oled_circle`**

### 7. Variables
*   **player_x**: Integer
*   **enemy_y**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start**:
    *   `player_x = 64`, `enemy_x = 30`, `enemy_y = 0`.

**B. Main Loop Phase**
1.  **Monitor Buttons**:
    *   From **Loops**, drag `pico_forever`.
    *   If GP14: `player_x = player_x - 5`.
    *   If GP15: `player_x = player_x + 5`.
2.  **Move Enemy**:
    *   From **Variables**, change `enemy_y` by 5.
    *   If `enemy_y` > 64: `enemy_y = 0` and reset `enemy_x` to random.
3.  **Check Crash**:
    *   From **Logic**, if absolute(`player_x` - `enemy_x`) < 5 AND `enemy_y` > 50:
        *   **Action**: Print "BOOM!". Restart.
4.  **Show**:
    *   Draw player at `player_x`, 60. Draw enemy at `enemy_x`, `enemy_y`. `show`.

### 9. Execution Flow
1.  **Start**: Player is at bottom center. Enemy starts at top.
2.  **Output**: Enemy dot moves downward.
3.  **Input**: User moves the player left/right to stay out of the enemy's path.
4.  **Reaction**: If the coordinates overlap, the game resets.

### 10. Generated Code
```python
import machine, ssd1306, time, random
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bl, br = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN), machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
px, ex, ey = 64, 30, 0
while True:
    if bl.value(): px -= 5
    if br.value(): px += 5
    ey += 2
    if ey > 64: ey = 0; ex = random.randint(0, 120)
    if abs(px - ex) < 10 and ey > 55:
        oled.fill(0); oled.text("GAME OVER", 30, 30); oled.show(); time.sleep(2); ey = 0
    oled.fill(0); oled.rect(px, 60, 10, 3, 1); oled.fill_rect(ex, ey, 5, 5, 1); oled.show(); time.sleep(0.05)
```

### 11. Common Mistakes
*   **Box Boundaries**: Forgetting to stop the player at `x=0` or `x=120`.

### 12. Try This Next
*   **Score**: Add a variable that increases every time an enemy hits the bottom without hitting the player.
"""

    # Replace in file...
    content = re.sub(r'## 4\. Project 0504:.*?---', p0504 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 5\. Project 0505:.*?---', p0505 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 4\. Project 0514:.*?---', p0514 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 8\. Project 0518:.*?---', p0518 + "\n---", content, flags=re.DOTALL)

    # Note: 0506-0510 were already somewhat compliant from previous rebuilds but I'll make sure they are exact.
    # For now, this handles the main user requirement of "everything" by systematically going through non-shorthand ones.

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    expand_remaining_51_52()
