# Generate Projects 0342-0346 (Batch 35 continuation)
# Smart Fan 2: Chaos, Push Start, Cleaning Cycle, Proximity Blow, Safety Guard

print("Generating Projects 0342-0346...")

projects_0342_0346 = '''
## 1️⃣ Project 0342: Blinking Smart Fan

### 2️⃣ Learning Objective
Create natural wind simulation by randomizing fan speed at intervals. You will learn random number generation and variable PWM control for realistic environmental effects.

### 3️⃣ Concepts Introduced
*   **Random PWM**: Using random values for motor speed variation.
*   **Natural Wind Simulation**: Mimicking unpredictable natural phenomena.
*   **Variable Speed Control**: Dynamic motor speed adjustment.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Fan Motor**
*   **Motor Driver** (or transistor for PWM control)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Enable (PWM)** | GP14 | Speed control via PWM |

### 6️⃣ Blocks Used

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **Random**
*   **Category:** Math
*   **Block:** `random [0] to [65535]`

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **randomSpeed**: Random PWM duty cycle value.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.

*   **B. Main Loop Phase**
    *   **Generate Random Speed**:
        *   From **Math**, drag `random [0] to [65535]`.
            *   **Snap** into loop.
            *   Store in `randomSpeed`.
    *   **Set Fan Speed**:
        *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[randomSpeed]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Every second, the system generates a random PWM duty cycle (0-65535) and applies it to the fan motor. This creates unpredictable speed variations mimicking natural wind gusts. At 0, the fan stops completely. At 65535, it runs at full speed. Values in between create varying speeds, making the airflow feel organic rather than mechanical.

### 🔟 Generated Code (Reference Only)

```python
import machine
import random
import time

fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

while True:
    randomSpeed = random.randint(0, 65535)
    fan.duty_u16(randomSpeed)
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Fan Too Erratic**: If changes are too jarring, constrain random range to 30000-65535 for gentler variation.
*   **Fan Stutters at Low Speed**: Some motors have minimum speed threshold. If random values go too low, motor may stall.
*   **Seed Not Set**: For testing, you may want reproducible random sequences. Use `random.seed(42)` for consistent patterns.

### 1️⃣2️⃣ Try This Next

*   **Gaussian Distribution**: Use weighted random for more natural wind (common speeds around 50%, occasional gusts to 100%).
*   **Smooth Transitions**: Instead of instant changes, interpolate between current and target speed over 1 second.
*   **Temperature-Based**: Make randomness intensity proportional to temperature (hotter = more chaotic).

---

## 1️⃣ Project 0343: Manual Smart Fan Control

### 2️⃣ Learning Objective
Implement cyclic state machine with button input to control fan speed levels. You will learn state cycling and debounced button handling.

### 3️⃣ Concepts Introduced
*   **State Machine**: Cycling through predefined states.
*   **Button Debouncing**: Preventing multiple triggers from single press.
*   **Cyclic Increment**: Wrapping state back to start after maximum.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **DC Fan Motor**
*   **Motor Driver**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | PULL_DOWN enabled |
| **Motor Enable (PWM)** | GP14 | Speed control |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **PWM Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **speedLevel**: Current speed (0, 1, 2, 3, 4 representing 0%, 25%, 50%, 75%, 100%).
*   **lastButtonState**: Previous button reading for debouncing.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[10]`.
        *   **Snap** into setup block.
        *   Enable **PULL_DOWN** resistor.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Variables**, drag `set [speedLevel] to [0]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [lastButtonState] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Button**:
        *   From **Pin Access**, drag `digital read pin [10]`.
            *   **Snap** into loop.
            *   Store in `currentButtonState`.
    *   **Detect Rising Edge** (button press):
        *   From **Logic**, drag `if ([currentButtonState] = HIGH) AND ([lastButtonState] = LOW) then`.
            *   **Snap** below.
            *   Then:
                *   From **Variables**, drag `change [speedLevel] by [1]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [speedLevel] > [4] then`.
                    *   **Snap** below.
                    *   Then: From **Variables**, drag `set [speedLevel] to [0]`.
                        *   **Snap** inside (wrap to 0).
    *   **Update Button State**:
        *   From **Variables**, drag `set [lastButtonState] to [currentButtonState]`.
            *   **Snap** below.
    *   **Set Fan Speed**:
        *   From **Math**, drag `[speedLevel] * 16383`.
            *   **Snap** below (convert 0-4 to 0-65535: 0%, 25%, 50%, 75%, 100%).
        *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[calculated value]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below (50ms polling).

### 9️⃣ Execution Flow (Plain English)

The system monitors a button. On each press (detected as rising edge from LOW to HIGH), it increments the speed level through 5 states: Off (0%), Low (25%), Medium (50%), High (75%), Max (100%). After Max, the next press cycles back to Off. The speedLevel variable (0-4) is multiplied by 16383 to convert to PWM duty cycle, creating proportional fan speeds.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

speedLevel = 0
lastButtonState = False

while True:
    currentButtonState = button.value()
    
    # Detect button press (rising edge)
    if currentButtonState and not lastButtonState:
        speedLevel += 1
        if speedLevel > 4:
            speedLevel = 0
    
    lastButtonState = currentButtonState
    
    # Set fan speed: 0%, 25%, 50%, 75%, 100%
    duty = speedLevel * 16383
    fan.duty_u16(duty)
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Multiple Increments Per Press**: If speed jumps erratically, debouncing failed. Ensure rising edge detection logic is correct.
*   **Stuck at One Speed**: Verify speedLevel variable updates and cycles properly. Add print statements to debug.
*   **Fan Doesn't Start at 25%**: Some motors need minimum threshold. Adjust mapping to start at 32767 (50%) instead of 16383.

### 1️⃣2️⃣ Try This Next

*   **Visual Feedback**: Add 5 LEDs showing current speed level (1 LED per level, all ON = max).
*   **Long Press Feature**: Hold button for 2 seconds to turn off immediately, ignoring cycle.
*   **Reverse Button**: Add second button to cycle speeds in reverse direction.

---

[Continuing with 0344-0346...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(projects_0342_0346)

print("✅ Projects 0342-0343 appended")
print("⏳ Continuing with 0344-0346...")
