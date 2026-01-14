## Project 0126: Smart Binary Counter Switch

### 1. Learning Objective
Implement countdown logic with binary display. Learn decrement operations and boundary conditions.

### 2. Concepts Introduced
*   **Decrement**: Subtracting 1 from a value
*   **Lower Boundary**: Preventing underflow (staying >= 0)
*   **Edge Detection**: Triggering action on button press

### 3. Hardware Required
*   Raspberry Pi Pico
*   Button
*   4 LEDs
*   10k Ohm pull-down resistor
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | With pull-down resistor |
| **LED 0-3** | GP15-GP18 | 4-bit binary display |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if / then)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **counter**: Current value (0-15)
*   **button_pressed**: Current button state
*   **last_button**: Previous button state

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**: Button and 4 LEDs as in previous projects.
2.  **Initialize Counter**: **Set** `counter` = 15 (all LEDs ON).
3.  **Display Initial State**: Show binary 1111 on LEDs.

**B. Main Loop Phase**
4.  **Read Button**: Check for rising edge (press detection).
5.  **Decrement on Press**:
    *   **If** button pressed AND `counter` > 0:
        *   `counter` = `counter` - 1
        *   Update LED display
6.  **Boundary Check**: If `counter` reaches 0, stop decrementing.

### 8. Execution Flow
1.  **Start**: Counter = 15, all LEDs ON.
2.  **Press**: Each button press decrements counter by 1.
3.  **Display**: LEDs show current binary value.
4.  **Stop**: At counter = 0, further presses have no effect.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure hardware
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
leds = [Pin(15 + i, Pin.OUT) for i in range(4)]

# Initialize
counter = 15
last_button = False

# Display function
def display_binary(value):
    for i in range(4):
        leds[i].value((value >> i) & 1)

# Show initial state
display_binary(counter)

# Main loop
while True:
    button_pressed = button.value()
    
    if button_pressed and not last_button:
        if counter > 0:
            counter -= 1
            display_binary(counter)
    
    last_button = button_pressed
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **No Boundary Check**: Allowing negative values causes wraparound.
*   **Missing Edge Detection**: No last_button tracking causes multiple decrements.

### 11. Try This Next
*   **Reset Button**: Add second button to reset counter to 15.
*   **Decrement by 2**: Subtract 2 per press instead of 1.

---

## Project 0127: Binary Counter Alarm System

### 1. Learning Objective
Implement threshold detection with alarm trigger. Learn conditional logic and automated reset.

### 2. Concepts Introduced
*   **Threshold Comparison**: Checking if value exceeds limit
*   **Alarm Triggering**: Activating output based on condition
*   **Automatic Reset**: Self-correcting behavior

### 3. Hardware Required
*   Raspberry Pi Pico
*   4 LEDs
*   Buzzer
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0-3** | GP15-GP18 | Binary display |
| **Buzzer** | GP19 | Alarm output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if / then)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (addition, modulo, comparison)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **counter**: Current count value (0-15)

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**: 4 LEDs and buzzer as outputs.
2.  **Initialize Counter**: **Set** `counter` = 0.

**B. Main Loop Phase**
3.  **Display Current Value**: Show binary on LEDs.
4.  **Check Threshold**:
    *   **If** `counter` > 10:
        *   Activate buzzer (short beep)
        *   Reset `counter` = 0
5.  **Increment Counter**: `counter` = `counter` + 1.
6.  **Wait**: 0.5 seconds between increments.

### 8. Execution Flow
1.  **Count Up**: 0, 1, 2, ..., 10, 11 (triggers alarm)
2.  **Alarm**: Buzzer beeps when counter > 10
3.  **Reset**: Counter resets to 0
4.  **Repeat**: Continuous cycle

### 9. Generated Code
```python
from machine import Pin
import time

# Configure hardware
leds = [Pin(15 + i, Pin.OUT) for i in range(4)]
buzzer = Pin(19, Pin.OUT)

counter = 0

def display_binary(value):
    for i in range(4):
        leds[i].value((value >> i) & 1)

while True:
    display_binary(counter)
    
    # Check threshold
    if counter > 10:
        buzzer.value(1)
        time.sleep(0.2)
        buzzer.value(0)
        counter = 0
    else:
        counter += 1
    
    time.sleep(0.5)
```

### 10. Common Mistakes
*   **Wrong Threshold**: Using >= instead of > changes behavior.
*   **Buzzer Always ON**: Forgetting to turn buzzer OFF.

### 11. Try This Next
*   **Adjustable Threshold**: Use potentiometer to set alarm point.
*   **Visual Alarm**: Flash all LEDs when threshold exceeded.

---

##  Project 0128: The Binary Counter Game

### 1. Learning Objective
Create an interactive binary-to-decimal quiz. Learn user input validation and random number generation.

### 2. Concepts Introduced
*   **Random Generation**: Creating unpredictable values
*   **User Input**: Reading from console
*   **Input Validation**: Checking correctness

### 3. Hardware Required
*   Raspberry Pi Pico
*   4 LEDs
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0-3** | GP15-GP18 | Binary display |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Math, drag `math_random_int`** (random integer)
*   **from Text, drag `text_print`** (print to console)
*   **from Text, drag `text_input`** (read user input)
*   **from Logic, drag `controls_if`** (if / else)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **random_value**: The quiz number (0-15)
*   **user_answer**: Player's guess

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LEDs**: 4 LEDs as outputs.

**B. Main Loop Phase**
2.  **Generate Random Number**: 0-15.
3.  **Display on LEDs**: Show binary representation.
4.  **Prompt User**: "What decimal number is this?"
5.  **Read Answer**: Get user input from console.
6.  **Check Answer**:
    *   If correct: Print "Correct!"
    *   If wrong: Print "Wrong! Answer was: X"
7.  **Wait**: Brief delay before next question.

### 8. Execution Flow
1.  **Start**: Generate random 0-15.
2.  **Display**: Show binary on LEDs.
3.  **Wait**: User reads LEDs and types answer.
4.  **Validate**: Check if answer matches random value.
5.  **Feedback**: Inform user of result.
6.  **Repeat**: New question.

### 9. Generated Code
```python
from machine import Pin
import time
import random

# Configure LEDs
leds = [Pin(15 + i, Pin.OUT) for i in range(4)]

def display_binary(value):
    for i in range(4):
        leds[i].value((value >> i) & 1)

while True:
    # Generate random number
    random_value = random.randint(0, 15)
    display_binary(random_value)
    
    # Prompt user
    print("\\nWhat decimal number is displayed? (0-15)")
    user_answer = int(input("Your answer: "))
    
    # Check answer
    if user_answer == random_value:
        print("Correct!")
    else:
        print(f"Wrong! The answer was: {random_value}")
    
    time.sleep(2)
```

### 10. Common Mistakes
*   **No Input Validation**: User might enter invalid characters.
*   **Range Issues**: Random should be 0-15, not 1-16.

### 11. Try This Next
*   **Score Tracking**: Count consecutive correct answers.
*   **Time Limit**: Add countdown timer for each question.

---

## Project 0129: Automated Binary Counter

### 1. Learning Objective
Implement bidirectional counter with overflow/underflow handling. Learn wraparound logic.

### 2. Concepts Introduced
*   **Overflow**: Value exceeds maximum (15 -> 0)
*   **Underflow**: Value goes below minimum (0 -> 15)
*   **Modulo Arithmetic**: Ensuring values stay in range

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Up, Down)
*   4 LEDs
*   2x 10k Ohm pull-down resistors
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Up** | GP14 | Increment |
| **Button Down** | GP13 | Decrement |
| **LED 0-3** | GP15-GP18 | Binary display |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if / then)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (addition, subtraction, modulo)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **counter**: Current value (0-15)
*   **last_up**, **last_down**: Edge detection variables

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**: 2 buttons, 4 LEDs.
2.  **Initialize**: `counter` = 0.

**B. Main Loop Phase**
3.  **Read Buttons**: Check both UP and DOWN.
4.  **Increment (UP button)**:
    *   If pressed: `counter` = (`counter` + 1) % 16
5.  **Decrement (DOWN button)**:
    *   If pressed: `counter` = (`counter` - 1 + 16) % 16
6.  **Update Display**: Show binary on LEDs.

### 8. Execution Flow
1.  **UP**: Increments with wraparound (15 -> 0).
2.  **DOWN**: Decrements with wraparound (0 -> 15).
3.  **Display**: Always shows valid 0-15 value.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure hardware
btn_up = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_down = Pin(13, Pin.IN, Pin.PULL_DOWN)
leds = [Pin(15 + i, Pin.OUT) for i in range(4)]

counter = 0
last_up = False
last_down = False

def display_binary(value):
    for i in range(4):
        leds[i].value((value >> i) & 1)

while True:
    up = btn_up.value()
    down = btn_down.value()
    
    if up and not last_up:
        counter = (counter + 1) % 16
        display_binary(counter)
    
    if down and not last_down:
        counter = (counter - 1 + 16) % 16
        display_binary(counter)
    
    last_up = up
    last_down = down
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **Negative Modulo**: Use (counter - 1 + 16) % 16, not (counter - 1) % 16.
*   **No Edge Detection**: Causes rapid counting.

### 11. Try This Next
*   **Speed Control**: Hold button for fast counting.
*   **Step Size**: Add buttons for +2/-2 jumps.

---

## Project 0130: Mastering Binary Counter

### 1. Learning Objective
Implement BCD (Binary Coded Decimal) with digit rollover. Learn constrained counting and event triggers.

### 2. Concepts Introduced
*   **BCD**: Using binary to represent decimal digits (0-9 only)
*   **Digit Rollover**: 9 -> 0 transition with carry
*   **Time-Based Counting**: Incrementing every second

### 3. Hardware Required
*   Raspberry Pi Pico
*   4 LEDs
*   Buzzer
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0-3** | GP15-GP18 | BCD display (0-9) |
| **Buzzer** | GP19 | Rollover indicator |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if / then)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (modulo)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **seconds**: Current second count (0-9)

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**: 4 LEDs and buzzer.
2.  **Initialize**: `seconds` = 0.

**B. Main Loop Phase**
3.  **Display BCD**: Show binary 0-9 on LEDs.
4.  **Wait**: 1 second.
5.  **Increment**: `seconds` = `seconds` + 1.
6.  **Check Rollover**:
    *   If `seconds` >= 10:
        *   Beep buzzer
        *   Reset `seconds` = 0

### 8. Execution Flow
1.  **Count**: 0, 1, 2, ..., 8, 9
2.  **Rollover**: At 10, beep and reset to 0
3.  **Repeat**: Continuous BCD seconds display

### 9. Generated Code
```python
from machine import Pin
import time

# Configure hardware
leds = [Pin(15 + i, Pin.OUT) for i in range(4)]
buzzer = Pin(19, Pin.OUT)

seconds = 0

def display_bcd(value):
    for i in range(4):
        leds[i].value((value >> i) & 1)

while True:
    display_bcd(seconds)
    time.sleep(1)
    
    seconds += 1
    if seconds >= 10:
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        seconds = 0
```

### 10. Common Mistakes
*   **Using Full Binary**: BCD only uses 0-9, not 0-15.
*   **Missing Beep**: Forgetting buzzer defeats rollover indication.

### 11. Try This Next
*   **Two Digits**: Add 4 more LEDs for tens digit (00-99).
*   **Minutes Counter**: Count to 60 instead of 10.

---
