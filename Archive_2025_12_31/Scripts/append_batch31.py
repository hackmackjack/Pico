# Script to append Projects 0306-0310 to Docs_0301_0400.md

content = '''
## 1️⃣ Project 0306: Smart Digital Art Switch

### 2️⃣ Learning Objective
Implement a state machine to cycle through brightness levels using a single button. You will learn how button presses sequentially change system states to control LED brightness at discrete levels.

### 3️⃣ Concepts Introduced
*   **State Machine**: System behavior based on current state variable.
*   **Brightness Control**: PWM duty cycle modulation for dimming.
*   **State Cycling**: Wrapping state back to start after reaching maximum.
*   **Button Debouncing**: Preventing multiple state changes from single press.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Pushbutton, momentary)
*   **RGB LED** (Common Cathode)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP20 | Enable PULL_DOWN resistor |
| **Red Channel** | GP13 | Via 220Ω Resistor |
| **Green Channel** | GP14 | Via 220Ω Resistor |
| **Blue Channel** | GP15 | Via 220Ω Resistor |
| **Common Cathode** | GND | RGB LED Negative Terminal |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs
*   **Block:** `Setup Button pin:[20]` with PULL_DOWN enabled

🔹 **PWM Write**
*   **Category:** Pin Access
*   **Block:** `PWM Write pin:[N] freq:[F] duty:[D]`

🔹 **Logic Blocks**
*   **Category:** Logic
*   **Block:** `if [Button Pressed] then`

🔹 **Sleep**
*   **Category:** Timing
*   **Block:** `sleep [N] seconds`

### 7️⃣ Variables & State
*   **brightnessState**: Current brightness level (0=Off, 1=Low 10%, 2=Med 50%, 3=High 100%).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [brightnessState] to [0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[20]`.
        *   **Snap** into setup block.
        *   Enable **PULL_DOWN** resistor.
    *   From **Outputs**, drag `Setup PWM pin:[13/14/15]` for each RGB channel.
        *   **Snap** into setup block (×3).

*   **B. Main Loop Phase**
    *   From **Logic**, drag `if [Button Pressed] then`.
        *   **Snap** into loop.
        *   Then:
            *   From **Variables**, drag `change [brightnessState] by [1]`.
                *   **Snap** inside.
            *   From **Logic**, drag `if [brightnessState] > [3] then set [brightnessState] to [0]`.
                *   **Snap** below.
            *   From **Loops**, drag `while [Button Pressed] do sleep [0.01]s`.
                *   **Snap** below (debounce).
    *   **Apply Brightness Based on State**:
        *   From **Logic**, drag `if [brightnessState] = [0] then`.
            *   **Snap** below.
            *   Then (Off): Set RGB to (0, 0, 0).
        *   From **Logic**, drag `else if [brightnessState] = [1] then`.
            *   **Snap** below.
            *   Then (Low 10%): Set RGB to (6553, 6553, 6553).
        *   From **Logic**, drag `else if [brightnessState] = [2] then`.
            *   **Snap** below.
            *   Then (Med 50%): Set RGB to (32768, 32768, 32768).
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Then (High 100%): Set RGB to (65535, 65535, 65535).
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico initializes with the LED off (state 0). When the button is pressed, it increments the brightness state: 0→1 (Low 10%), 1→2 (Medium 50%), 2→3 (High 100%), and 3→0 (Off), cycling continuously. After each button press, it waits for button release to prevent multiple increments from a single press (debouncing). The current state determines the PWM duty cycle applied equally to all three RGB channels, creating white light at varying brightness levels.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

btn = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

brightnessState = 0
brightness_levels = [0, 6553, 32768, 65535]  # 0%, 10%, 50%, 100%

while True:
    if btn.value():
        brightnessState = (brightnessState + 1) % 4
        while btn.value():
            time.sleep(0.01)
    
    duty = brightness_levels[brightnessState]
    red.duty_u16(duty)
    green.duty_u16(duty)
    blue.duty_u16(duty)
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Double Increment**: If brightness jumps two levels per press, debounce is insufficient. Increase debounce wait time.
*   **State Stuck**: If LED stays at one brightness, verify state variable changes by printing to console for debugging.
*   **Wrong Brightness Values**: 10% = 6553 (65535/10), 50% = 32768 (65535/2), 100% = 65535. Verify calculations match problem requirements.
*   **LED Always On**: If LED never turns off, check that state 0 sets all channels to duty 0, not just skips the update.

### 1️⃣2️⃣ Try This Next

*   **Color Cycling**: Instead of white at different brightness, cycle through colors (Red→Green→Blue→White) at full brightness.
*   **Smooth Fade**: Add gradual transitions between brightness levels using small incremental steps instead of instant changes.
*   **Long Press for Off**: Require holding button for 2 seconds to turn off, separate from the quick-press cycling behavior.

---

[CONTINUING WITH PROJECTS 0307-0310 IN NEXT APPEND]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(content)

print("Project 0306 appended successfully")
