# Batch 42: Button Logic 3 (Projects 0411-0420) - Part 1 (0411-0415)

target_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'

batch42_part1 = r'''
# 🏁 Batch 42: Button Logic 3

---

## 1️⃣ Project 0411: Introduction to Button Logic

### 2️⃣ Learning Objective
Implement a logic NOT gate where a button inverts LED state. You will learn about inversion logic and normally-on behavior.

### 3️⃣ Concepts Introduced
*   **Logic NOT**: Output is opposite of input.
*   **Inversion Logic**: Active-low behavior.
*   **Normally-On**: LED defaults to on state.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **LED**
*   **Resistor** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |
| **LED** | GP16 | |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Logic NOT**
*   **Category:** Logic

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **buttonState**: Current button value.
*   **ledState**: Inverted button value.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   From **Pin Access**, drag `set [buttonState] to [digital read pin 14]`.
        *   **Snap** into loop.
    *   From **Logic**, drag `set [ledState] to [not buttonState]`.
        *   **Snap** below.
    *   From **Pin Access**, drag `digital write pin:[16] value:[ledState]`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

When the button is NOT pressed (LOW), the LED is ON. When the button IS pressed (HIGH), the LED turns OFF. This implements a NOT gate: LED = !Button. It's the opposite of typical button behavior, useful for kill switches or active-low circuits.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    button_state = button.value()
    led_state = not button_state
    led.value(led_state)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Default**: If LED is off when button unpressed, check PULL_DOWN vs PULL_UP wiring.
*   **Inverted Twice**: Using `not not button` returns original state.

### 1️⃣2️⃣ Try This Next

*   **NAND Gate**: Add second button; LED off only when BOTH pressed.
*   **NOR Gate**: LED on only when NEITHER pressed.

---

## 1️⃣ Project 0412: Blinking Button Logic

### 2️⃣ Learning Objective
Create an armed/disarmed indicator system with visual status differentiation. You will learn about mode toggling and state-specific patterns.

### 3️⃣ Concepts Introduced
*   **Armed Indicator**: Different LED patterns for different states.
*   **Mode Toggle**: Button press switches between states.
*   **Visual Status**: Using color and pattern to communicate state.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Green LED**
*   **Red LED**
*   **2× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |
| **Green LED** | GP16 | Disarmed state |
| **Red LED** | GP17 | Armed state |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Toggle Variable**
*   **Category:** Variables

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **isArmed**: Boolean tracking system state.
*   **lastButton**: Previous button state for edge detection.
*   **blinkState**: Toggle for red LED blinking.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16,17] as OUTPUT`.
        *   **Snap** below.
    *   From **Variables**, drag `set [isArmed] to [False]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [lastButton] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button Press Detection**:
        *   From **Pin Access**, drag `set [currentButton] to [digital read pin 14]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [currentButton] AND not [lastButton] then`.
            *   **Snap** below (rising edge).
            *   Inside:
                *   From **Variables**, drag `set [isArmed] to [not isArmed]`.
                    *   **Snap** inside (toggle).
        *   From **Variables**, drag `set [lastButton] to [currentButton]`.
            *   **Snap** below.
    *   **State Display**:
        *   From **Logic**, drag `if not [isArmed] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                    *   **Snap** inside (green solid).
                *   From **Pin Access**, drag `digital write pin:[17] value:[LOW]`.
                    *   **Snap** below.
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
                   From **Variables**, drag `set [blinkState] to [not blinkState]`.
                *   From **Pin Access**, drag `digital write pin:[17] value:[blinkState]`.
                    *   **Snap** below (red blinking).
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Initially, the system is disarmed: green LED solid on, red LED off. Press the button to arm: green LED turns off, red LED starts blinking (0.5s on, 0.5s off). Press again to disarm: back to green solid. The visual pattern instantly communicates system status without needing displays or serial output.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
green_led = machine.Pin(16, machine.Pin.OUT)
red_led = machine.Pin(17, machine.Pin.OUT)

is_armed = False
last_button = False
blink_state = False

while True:
    current_button = button.value()
    
    # Toggle on button press
    if current_button and not last_button:
        is_armed = not is_armed
    last_button = current_button
    
    # Display state
    if not is_armed:
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        blink_state = not blink_state
        red_led.value(blink_state)
    
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Both LEDs On**: Ensure disarmed explicitly turns red LED off, armed turns green off.
*   **Rapid Toggle**: Without edge detection, holding button toggles repeatedly.

### 1️⃣2️⃣ Try This Next

*   **Armed Countdown**: After arming, show 10-second countdown with rapid blinking before full activation.
*   **Audio Confirmation**: Add beeps on arm/disarm transitions.

---

## 1️⃣ Project 0413: Manual Button Logic Control

### 2️⃣ Learning Objective
Implement an OR logic gate where either of two buttons activates an LED. You will learn about parallel input logic and OR gate behavior.

### 3️⃣ Concepts Introduced
*   **Logic OR**: Output is HIGH if ANY input is HIGH.
*   **Parallel Inputs**: Multiple independent triggers.
*   **Either/Or Logic**: One or both inputs sufficient.

### 4️⃣ Hardware Required
*   **Pico**
*   **2× Buttons**
*   **LED**
*   **Resistor** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | PULL_DOWN |
| **Button B** | GP15 | PULL_DOWN |
| **LED** | GP16 | |

### 6️⃣ Blocks Used

🔹 **Digital Read (×2)**
*   **Category:** Pin Access

🔹 **Logic OR**
*   **Category:** Logic

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **buttonA**: State of button A.
*   **buttonB**: State of button B.
*   **ledState**: Result of OR operation.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14,15] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   From **Pin Access**, drag `set [buttonA] to [digital read pin 14]`.
        *   **Snap** into loop.
    *   From **Pin Access**, drag `set [buttonB] to [digital read pin 15]`.
        *   **Snap** below.
    *   From **Logic**, drag `set [ledState] to [buttonA OR buttonB]`.
        *   **Snap** below.
    *   From **Pin Access**, drag `digital write pin:[16] value:[ledState]`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The LED turns on if Button A is pressed, OR Button B is pressed, OR both are pressed. Only when NEITHER button is pressed does the LED turn off. This is a classic OR gate: output = A + B. Pressing either switch is sufficient to activate the output.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buttonB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    button_a = buttonA.value()
    button_b = buttonB.value()
    led_state = button_a or button_b
    led.value(led_state)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Logic**: Using `and` instead of `or` makes it an AND gate (both required).
*   **One Button Stuck**: If LED never turns off, one button might be stuck HIGH.

### 1️⃣2️⃣ Try This Next

*   **AND Gate**: Require BOTH buttons pressed to light LED.
*   **XOR Gate**: LED on only when EXACTLY one button pressed (not both, not neither).

---

## 1️⃣ Project 0414: Button Logic Sequences

### 2️⃣ Learning Objective
Create a Konami-style cheat code detector using sequential button patterns. You will learn about multi-step input validation and sequence matching.

### 3️⃣ Concepts Introduced
*   **Cheat Code**: Specific button sequence triggers action.
*   **Sequence Matching**: Validating ordered inputs.
*   **State Machine**: Tracking progress through pattern.

### 4️⃣ Hardware Required
*   **Pico**
*   **2× Buttons** (A=Up, B=Down)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A (Up)** | GP14 | PULL_DOWN |
| **Button B (Down)** | GP15 | PULL_DOWN |
| **Buzzer** | GP16 | Success tone |

### 6️⃣ Blocks Used

🔹 **Digital Read (×2)**
*   **Category:** Pin Access

🔹 **List Append**
*   **Category:** Variables

🔹 **List Comparison**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **sequence**: Expected pattern `['A', 'A', 'B', 'B']`.
*   **inputBuffer**: User's button presses.
*   **lastA**, **lastB**: Previous button states for edge detection.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14,15] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [sequence] to [['A', 'A', 'B', 'B']]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [inputBuffer] to [[]]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [lastA] to [False]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [lastB] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button A Detection**:
        *   From **Pin Access**, drag `set [currentA] to [digital read pin 14]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [currentA] AND not [lastA] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `append ['A'] to [inputBuffer]`.
                    *   **Snap** inside.
                *   From **Console**, drag `print [Input: A]`.
                    *   **Snap** below.
        *   From **Variables**, drag `set [lastA] to [currentA]`.
            *   **Snap** below.
    *   **Button B Detection** (same pattern for 'B'):
        *   From **Pin Access**, drag `set [currentB] to [digital read pin 15]`.
        *   From **Logic**, drag `if [currentB] AND not [lastB] then`.
            *   Inside: `append ['B'] to [inputBuffer]`.
        *   From **Variables**, drag `set [lastB] to [currentB]`.
    *   **Sequence Check**:
        *   From **Logic**, drag `if [inputBuffer] = [sequence] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Console**, drag `print [SUCCESS! Code accepted!]`.
                    *   **Snap** inside.
                *   From **Actuators**, drag `Buzzer [16] tone [1000] for [1000]ms`.
                    *   **Snap** below.
                *   From **Variables**, drag `set [inputBuffer] to [[]]`.
                    *   **Snap** below (reset).
    *   **Buffer Overflow Protection**:
        *   From **Logic**, drag `if [length of inputBuffer] > [4] then`.
            *   **Snap** below.
            *   Inside: `set [inputBuffer] to [[]]` (clear on fail).
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The user presses buttons in sequence: Up-Up-Down-Down (A-A-B-B). Each press is recorded in a buffer. When the buffer exactly matches the expected sequence, a success tone plays and the buffer resets. If the user presses wrong buttons (e.g., A-B-A), the buffer clears after 4 inputs and they must start over.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buttonB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.PWM(machine.Pin(16))

sequence = ['A', 'A', 'B', 'B']
input_buffer = []
last_a = False
last_b = False

while True:
    current_a = buttonA.value()
    current_b = buttonB.value()
    
    # Detect button A press
    if current_a and not last_a:
        input_buffer.append('A')
        print(f"Input: A | Buffer: {input_buffer}")
    last_a = current_a
    
    # Detect button B press
    if current_b and not last_b:
        input_buffer.append('B')
        print(f"Input: B | Buffer: {input_buffer}")
    last_b = current_b
    
    # Check sequence
    if input_buffer == sequence:
        print("SUCCESS! Code accepted!")
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(1)
        buzzer.duty_u16(0)
        input_buffer = []
    
    # Clear buffer if too long
    if len(input_buffer) > 4:
        input_buffer = []
        print("Buffer cleared - try again")
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Never Matches**: Ensure you're comparing lists directly: `input_buffer == sequence`.
*   **Double Counting**: Without edge detection, one press registers multiple times.

### 1️⃣2️⃣ Try This Next

*   **Timing Requirement**: Clear buffer if 5 seconds elapse between presses (too slow).
*   **Multi-Level Codes**: After first code, unlock a harder 6-button sequence.

---

## 1️⃣ Project 0415: Interactive Button Logic

### 2️⃣ Learning Objective
Create a color-matching reaction game where users must press the matching button for displayed colors. You will learn about instruction following and correctness tracking.

### 3️⃣ Concepts Introduced
*   **Reaction State**: System presents stimulus, user responds.
*   **Instruction Following**: Matching action to visual cue.
*   **Correctness Tracking**: Recording successes and failures.

### 4️⃣ Hardware Required
*   **Pico**
*   **Blue LED**
*   **Yellow LED**
*   **Blue Button**
*   **Yellow Button**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Blue LED** | GP16 | |
| **Yellow LED** | GP17 | |
| **Blue Button** | GP14 | PULL_DOWN |
| **Yellow Button** | GP15 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Random Choice**
*   **Category:** Math

🔹 **Digital Read/Write**
*   **Category:** Pin Access

🔹 **Score Tracking**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **currentColor**: Which LED is lit ('blue' or 'yellow').
*   **score**: Number of correct responses.
*   **errors**: Number of incorrect responses.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[14,15] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16,17] as OUTPUT`.
        *   **Snap** below.
    *   From **Variables**, drag `set [score] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [errors] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Pick Random Color**:
        *   From **Math**, drag `set [currentColor] to [random choice(['blue', 'yellow'])]`.
            *   **Snap** into loop.
    *   **Light Corresponding LED**:
        *   From **Logic**, drag `if [currentColor] = ['blue'] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                *   From **Pin Access**, drag `digital write pin:[17] value:[LOW]`.
        *   From **Logic**, drag `else`.
            *   Inside: (Yellow LED on, Blue LED off).
    *   **Wait for Button Press**:
        *   From **Logic**, drag `wait until [digital read pin 14 OR digital read pin 15]`.
            *   **Snap** below.
    *   **Check Correctness**:
        *   From **Logic**, drag `if [currentColor] = ['blue'] AND [digital read pin 14] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [score] by [1]`.
                *   From **Console**, drag `print [CORRECT! Blue]`.
        *   From **Logic**, drag `else if [currentColor] = ['yellow'] AND [digital read pin 15] then`.
            *   Inside: `change [score] by [1]`.
        *   From **Logic**, drag `else`.
            *   Inside: `change [errors] by [1]` and `print [WRONG!]`.
    *   **Display Score**:
        *   From **Console**, drag `print [Score: {score} | Errors: {errors}]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below (next round delay).

### 9️⃣ Execution Flow (Plain English)

The system randomly lights either the blue or yellow LED. The user must press the matching button (blue LED → blue button). Correct presses increment the score; wrong presses increment errors. After each round, the score is displayed. This tests reaction speed and color-matching accuracy.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random

blue_led = machine.Pin(16, machine.Pin.OUT)
yellow_led = machine.Pin(17, machine.Pin.OUT)
blue_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellow_btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

score = 0
errors = 0

while True:
    current_color = random.choice(['blue', 'yellow'])
    
    # Light LED
    if current_color == 'blue':
        blue_led.on()
        yellow_led.off()
    else:
        yellow_led.on()
        blue_led.off()
    
    # Wait for button press
    while not blue_btn.value() and not yellow_btn.value():
        time.sleep(0.05)
    
    # Check correctness
    if current_color == 'blue' and blue_btn.value():
        score += 1
        print("CORRECT! Blue")
    elif current_color == 'yellow' and yellow_btn.value():
        score += 1
        print("CORRECT! Yellow")
    else:
        errors += 1
        print("WRONG!")
    
    print(f"Score: {score} | Errors: {errors}")
    
    # Turn off LEDs
    blue_led.off()
    yellow_led.off()
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Both Buttons Counted**: If user presses both simultaneously, define which has priority or reject the input.
*   **Timeout Needed**: If user never presses, game hangs. Add 5-second timeout with auto-fail.

### 1️⃣2️⃣ Try This Next

*   **Speed Bonus**: Award extra points for presses within 1 second.
*   **Three Colors**: Add red LED/button for increased difficulty.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch42_part1)

print("✅ Generated Projects 0411-0415 (Batch 42 Part 1)")
print("📋 Continuing with 0416-0420...")
