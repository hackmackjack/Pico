
# BATCH 13: Binary Counter 1 (Projects 0121-0130)

## Project 0121: Introduction to Binary Counter

### 1. Learning Objective
Understand the concept of binary bits. Learn how a single LED represents a binary digit (bit) with ON=1 and OFF=0.

### 2. Concepts Introduced
*   **Binary Digit (Bit)**: Smallest unit of data (0 or 1)
*   **Digital Logic**: ON/OFF states representing Boolean values
*   **Serial Output**: Printing values to console for debugging

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 LED
*   1x 220-330 Ohm resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Anode (+)** | GP15 | Through current-limiting resistor |
| **LED Cathode (-)** | GND | Ground connection |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **bit_value**: Current bit state (0 or 1)

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LED Pin**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 as OUTPUT.
    *   **Initialize** to LOW (OFF = 0).

**B. Main Loop Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

3.  **Set Bit to 0 (OFF)**:
    *   From **Variables**, drag `variables_set`.
    *   **Set** `bit_value` = 0.
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> LOW.
    *   From **Text**, drag `text_print`.
    *   **Print** "Bit 0: ", `bit_value`.

4.  **Hold State**:
    *   From **Time**, drag `pico_wait` -> 2 seconds.

5.  **Set Bit to 1 (ON)**:
    *   From **Variables**, **Set** `bit_value` = 1.
    *   From **Smart IO**, **Set** GP15 -> HIGH.
    *   From **Text**, **Print** "Bit 0: ", `bit_value`.

6.  **Hold State**:
    *   From **Time**, drag `pico_wait` -> 2 seconds.

### 8. Execution Flow
1.  **Start**: Initialize LED as output, set to OFF.
2.  **Loop**: Alternate between two states:
    *   State 0: LED OFF, print "Bit 0: 0", wait 2s
    *   State 1: LED ON, print "Bit 0: 1", wait 2s
3.  **Repeat**: Continuous demonstration of binary 0 and 1.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure LED
led = Pin(15, Pin.OUT)

# Main loop
while True:
    # Bit = 0
    bit_value = 0
    led.value(0)
    print(f"Bit 0: {bit_value}")
    time.sleep(2)
    
    # Bit = 1
    bit_value = 1
    led.value(1)
    print(f"Bit 0: {bit_value}")
    time.sleep(2)
```

### 10. Common Mistakes
*   **No Current Limiting Resistor**: Always use 220-330 Ohm resistor with LED.
*   **Wrong Polarity**: LED has polarity - long leg (anode) goes to pin, short leg (cathode) to ground.
*   **No Console Output**: Forgetting print statements defeats the learning purpose.

### 11. Try This Next
*   **User Input**: Add button to toggle bit value manually.
*   **Multiple Cycles**: Count how many times the bit toggles.
*   **Timing Variation**: Speed up to 0.5s intervals for faster demonstration.

---

## Project 0122: Blinking Binary Counter

### 1. Learning Objective
Implement a 2-bit binary counter. Learn how multiple bits combine to represent larger numbers (0-3).

### 2. Concepts Introduced
*   **Multi-Bit Numbers**: Combining bits to represent values
*   **Binary Counting**: Sequential increment through all possible states
*   **Positional Notation**: Bit 0 (ones), Bit 1 (twos)

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 LEDs
*   2x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0 (Bit 0)** | GP15 | Ones place (value = 1) |
| **LED 1 (Bit 1)** | GP16 | Twos place (value = 2) |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Direct pin manipulation for this simple counter.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LED Pins**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 (Bit 0) as OUTPUT -> LOW.
    *   **Set** GP16 (Bit 1) as OUTPUT -> LOW.

**B. Main Loop Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

3.  **Count 0 (Binary: 00)**:
    *   **Set** GP15 -> LOW, GP16 -> LOW.
    *   **Wait** 1 second.

4.  **Count 1 (Binary: 01)**:
    *   **Set** GP15 -> HIGH, GP16 -> LOW.
    *   **Wait** 1 second.

5.  **Count 2 (Binary: 10)**:
    *   **Set** GP15 -> LOW, GP16 -> HIGH.
    *   **Wait** 1 second.

6.  **Count 3 (Binary: 11)**:
    *   **Set** GP15 -> HIGH, GP16 -> HIGH.
    *   **Wait** 1 second.

### 8. Execution Flow
1.  **Start**: Initialize both LEDs to OFF (00).
2.  **Loop**: Cycle through all 2-bit combinations:
    *   00 (0) -> 01 (1) -> 10 (2) -> 11 (3) -> repeat
3.  **Timing**: Each state held for 1 second.
4.  **Result**: Visual binary counting demonstration.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure LEDs
led0 = Pin(15, Pin.OUT)  # Bit 0 (ones)
led1 = Pin(16, Pin.OUT)  # Bit 1 (twos)

# Main loop
while True:
    # Count 0: 00
    led0.value(0)
    led1.value(0)
    time.sleep(1)
    
    # Count 1: 01
    led0.value(1)
    led1.value(0)
    time.sleep(1)
    
    # Count 2: 10
    led0.value(0)
    led1.value(1)
    time.sleep(1)
    
    # Count 3: 11
    led0.value(1)
    led1.value(1)
    time.sleep(1)
```

### 10. Common Mistakes
*   **Wrong Bit Order**: Remember Bit 0 is rightmost (least significant).
*   **Timing Too Fast**: Below 0.5s makes it hard to read the pattern.
*   **Skipping States**: Missing any of the 4 states breaks the sequence.

### 11. Try This Next
*   **3-Bit Counter**: Add third LED for counting 0-7.
*   **Reverse Count**: Count down from 3 to 0.
*   **Binary Display**: Add console output showing binary and decimal.

---

## Project 0123: Manual Binary Counter Control

### 1. Learning Objective  
Implement manual bit toggling with buttons. Learn interactive binary number creation.

### 2. Concepts Introduced
*   **Bit Toggling**: Switching bit state (0<->1)
*   **Independent Control**: Each bit controlled separately
*   **State Persistence**: Maintaining bit values between button presses

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (A, B)
*   2 LEDs
*   2x 10k Ohm pull-down resistors (for buttons)
*   2x 220-330 Ohm resistors (for LEDs)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Controls Bit 0 (LED 0) |
| **Button B** | GP13 | Controls Bit 1 (LED 1) |
| **LED 0 (Bit 0)** | GP15 | Ones place |
| **LED 1 (Bit 1)** | GP16 | Twos place |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if / then)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **bit0**: State of Bit 0 (True/False)
*   **bit1**: State of Bit 1 (True/False)
*   **last_button_a**: Previous state of Button A
*   **last_button_b**: Previous state of Button B

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Buttons**:
    *   Configure GP14, GP13 as INPUT with PULL_DOWN.

2.  **Configure LEDs**:
    *   Configure GP15, GP16 as OUTPUT, initialized to LOW.

3.  **Initialize Variables**:
    *   **Set** `bit0` = False, `bit1` = False.
    *   **Set** `last_button_a` = False, `last_button_b` = False.

**B. Main Loop Phase**
4.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

5.  **Read Button States**:
    *   **Read** GP14 -> `button_a`.
    *   **Read** GP13 -> `button_b`.

6.  **Toggle Bit 0 (Button A)**:
    *   **If** (`button_a` == True) AND (`last_button_a` == False):
        *   **Then**: `bit0` = NOT `bit0` (toggle)
        *   Update LED: **Set** GP15 -> `bit0`

7.  **Toggle Bit 1 (Button B)**:
    *   **If** (`button_b` == True) AND (`last_button_b` == False):
        *   **Then**: `bit1` = NOT `bit1` (toggle)
        *   Update LED: **Set** GP16 -> `bit1`

8.  **Update Last States**:
    *   **Set** `last_button_a` = `button_a`.
    *   **Set** `last_button_b` = `button_b`.

9.  **Small Delay**:
    *   **Wait** 0.01 seconds.

### 8. Execution Flow
1.  **Start**: Initialize buttons and LEDs, all bits set to 0.
2.  **Monitor**: Continuously read both button states.
3.  **Edge Detection**: When button transitions LOW->HIGH:
    *   Toggle corresponding bit
    *   Update corresponding LED
4.  **Result**: User can create any 2-bit number (0-3) by pressing buttons.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure hardware
btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)
led0 = Pin(15, Pin.OUT)
led1 = Pin(16, Pin.OUT)

# Initialize state
bit0 = False
bit1 = False
last_button_a = False
last_button_b = False

# Main loop
while True:
    # Read buttons
    button_a = btn_a.value()
    button_b = btn_b.value()
    
    # Toggle Bit 0
    if button_a and not last_button_a:
        bit0 = not bit0
        led0.value(bit0)
    
    # Toggle Bit 1
    if button_b and not last_button_b:
        bit1 = not bit1
        led1.value(bit1)
    
    # Update last states
    last_button_a = button_a
    last_button_b = button_b
    
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **No Edge Detection**: Without tracking last state, each press toggles multiple times.
*   **Missing Pull Resistors**: Causes floating inputs and random toggles.
*   **No Debouncing**: Physical buttons may need debouncing for clean toggles.

### 11. Try This Next
*   **Display Value**: Print the decimal value (0-3) to console after each toggle.
*   **4-Bit Version**: Add 2 more buttons and LEDs for 4-bit (0-15) control.
*   **Reset Button**: Add button to clear all bits to 0.

---

## Project 0124: Binary Counter Sequences

### 1. Learning Objective
Implement automatic 4-bit counting. Learn algorithmic binary increment and modulo arithmetic.

### 2. Concepts Introduced
*   **4-Bit Binary**: Numbers 0-15 (0000 to 1111)
*   **Automatic Increment**: Software-driven counting
*   **Binary Representation**: Converting decimal to binary display

### 3. Hardware Required
*   Raspberry Pi Pico
*   4 LEDs
*   4x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0 (Bit 0)** | GP15 | Ones place (value = 1) |
| **LED 1 (Bit 1)** | GP16 | Twos place (value = 2) |
| **LED 2 (Bit 2)** | GP17 | Fours place (value = 4) |
| **LED 3 (Bit 3)** | GP18 | Eights place (value = 8) |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (modulo, bitwise operations)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **counter**: Current count value (0-15)

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LED Pins**:
    *   Configure GP15, GP16, GP17, GP18 as OUTPUT.

2.  **Initialize Counter**:
    *   **Set** `counter` = 0.
0//;'''
**B. Main Loop Phase**
3.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

4.  **Display Binary Value**:
    *   **Extract** each bit using bitwise AND:
    *   Bit 0: **Set** GP15 -> (`counter` & 1)
    *   Bit 1: **Set** GP16 -> (`counter` & 2) >> 1
    *   Bit 2: **Set** GP17 -> (`counter` & 4) >> 2
    *   Bit 3: **Set** GP18 -> (`counter` & 8) >> 3

5.  **Wait**:
    *   From **Time**, drag `pico_wait` -> 0.5 seconds.

6.  **Increment Counter**:
    *   **Calculate**: `counter` = (`counter` + 1) % 16
    *   Modulo 16 ensures wraparound (15 -> 0).

### 8. Execution Flow
1.  **Start**: Initialize LEDs, set counter to 0.
2.  **Loop**:
    *   Convert counter value to binary
    *   Set each LED based on corresponding bit
    *   Wait 0.5 seconds
    *   Increment counter (with wraparound at 16)
3.  **Result**: Continuous 0-15 binary counting display.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure LEDs
leds = [
    Pin(15, Pin.OUT),  # Bit 0
    Pin(16, Pin.OUT),  # Bit 1
    Pin(17, Pin.OUT),  # Bit 2
    Pin(18, Pin.OUT)   # Bit 3
]

# Initialize counter
counter = 0

# Main loop
while True:
    # Display binary value
    for i in range(4):
        bit_value = (counter >> i) & 1
        leds[i].value(bit_value)
    
    # Wait
    time.sleep(0.5)
    
    # Increment with wraparound
    counter = (counter + 1) % 16
```

### 10. Common Mistakes
*   **No Modulo**: Forgetting % 16 causes counter to exceed 15.
*   **Wrong Bit Extraction**: Bit shift and AND operations must be correct.
*   **LED Order**: Ensure Bit 0 is rightmost LED for conventional display.

### 11. Try This Next
*   **Console Display**: Print decimal and binary representation to console.
*   **Speed Control**: Use potentiometer to control count speed.
*   **8-Bit Counter**: Expand to 8 LEDs for 0-255 counting.

---

## Project 0125: Interactive Binary Counter

### 1. Learning Objective
Implement binary-to-decimal conversion using button inputs. Learn weighted bit values and summation.

### 2. Concepts Introduced
*   **Weighted Bits**: Each bit position has a specific value (1, 2, 4, 8)
*   **Summation**: Adding weighted values to get decimal equivalent
*   **Multi-Input Reading**: Checking multiple buttons simultaneously

### 3. Hardware Required
*   Raspberry Pi Pico
*   4 Buttons (representing values 1, 2, 4, 8)
*   4x 10k Ohm pull-down resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button 1** | GP14 | Value = 1 (Bit 0) |
| **Button 2** | GP13 | Value = 2 (Bit 1) |
| **Button 4** | GP12 | Value = 4 (Bit 2) |
| **Button 8** | GP11 | Value = 8 (Bit 3) |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (addition)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **total**: Sum of all pressed button values (0-15)

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Button Pins**:
    *   Configure GP14, GP13, GP12, GP11 as INPUT with PULL_DOWN.

**B. Main Loop Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever` block.

3.  **Initialize Total**:
    *   **Set** `total` = 0.

4.  **Read and Sum Button Values**:
    *   **Read** GP14 -> if HIGH, **add** 1 to `total`
    *   **Read** GP13 -> if HIGH, **add** 2 to `total`
    *   **Read** GP12 -> if HIGH, **add** 4 to `total`
    *   **Read** GP11 -> if HIGH, **add** 8 to `total`

5.  **Print Result**:
    *   From **Text**, drag `text_print`.
    *   **Print** "Binary Sum: ", `total`.

6.  **Small Delay**:
    *   **Wait** 0.1 seconds.

### 8. Execution Flow
1.  **Start**: Configure all button inputs.
2.  **Loop**:
    *   Reset total to 0
    *   Read all 4 buttons
    *   Add value of each pressed button to total
    *   Print total to console
    *   Wait briefly
3.  **Result**: Real-time display of binary-to-decimal conversion.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure buttons
btn1 = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Value 1
btn2 = Pin(13, Pin.IN, Pin.PULL_DOWN)  # Value 2
btn4 = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Value 4
btn8 = Pin(11, Pin.IN, Pin.PULL_DOWN)  # Value 8

# Main loop
while True:
    # Calculate sum
    total = 0
    if btn1.value():
        total += 1
    if btn2.value():
        total += 2
    if btn4.value():
        total += 4
    if btn8.value():
        total += 8
    
    # Print result
    print(f"Binary Sum: {total}")
    
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **Wrong Weights**: Ensure buttons are assigned correct powers of 2 (1, 2, 4, 8).
*   **Not Resetting Total**: Forgetting to reset total to 0 causes accumulation.
*   **Update Too Fast**: Printing faster than 0.1s floods the console.

### 11. Try This Next
*   **LED Display**: Add 4 LEDs to show which buttons are pressed visually.
*   **Binary Display**: Print both binary representation and decimal value.
*   **Range Check**: Validate that total is always between 0-15.

---
