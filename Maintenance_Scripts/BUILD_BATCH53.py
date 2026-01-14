import os

def build_batch53():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0521 = """
---

# Batch 53: Binary Counter 3

## 1. Project 0521: Introduction to Binary Counter

### 2. Learning Objective
Detect a specific bit in a numerical value using a bitwise AND mask operation and indicate the result via an LED.

### 3. Concepts Introduced
*   Bitwise AND (`&`)
*   Bit Masking
*   Binary Weighting (Bit 2 = Value 4)
*   Conditional Output

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x LED
*   1x 220Ω Resistor
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP16 | Connected via 220Ω resistor |

### 6. Blocks Used
*   **from Logic, drag `bitwise_and`** (Perform bitwise mask)
*   **from Math, drag `number`** (Set mask value)
*   **from Logic, drag `greater_than`** (Check result)
*   **from Smart IO, drag `pico_gpio_write`** (Set LED)

### 7. Variables
*   **test_num**: Integer (The decimal number being checked)
*   **is_bit_on**: Boolean (Result of the bitwise check)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_gpio_write` Pin GP16 as Output.
2.  **Set Test Value**:
    *   From **Variables**, set `test_num` to a decimal value (e.g., 6).
    *   *Note: In binary, 6 is 110. Bit 2 is the second bit from right ($2^2=4$), which is 1.*

**B. Main Loop Phase**
3.  **Perform Mask**:
    *   From **Variables**, set `is_bit_on` to result of:
        *   From **Logic**, drag `bitwise_and`.
        *   **Snap** `test_num` and `4` (the mask for Bit 2).
4.  **Check Result**:
    *   From **Logic**, drag `if_else`.
    *   Condition: `is_bit_on` > 0.
5.  **Output**:
    *   **If True**:
        *   From **Smart IO**, set GP16 to **HIGH**.
    *   **Else**:
        *   From **Smart IO**, set GP16 to **LOW**.

### 9. Execution Flow
1.  **Start**: Pico initializes GP16 and sets the variable `test_num`.
2.  **Process**: The system applies a "Mask" (value 4) to the number. This strips away all bits except the one we care about.
3.  **Check**: If the result is non-zero, it means Bit 2 was indeed active in the original number.
4.  **Output**: The LED turns ON if the bit exists, otherwise it stays OFF.

### 10. Generated Code
```python
from machine import Pin

led = Pin(16, Pin.OUT)
test_num = 6 # Binary 110 (Bit 2 is ON)

# Check Bit 2 (Value 4)
if (test_num & 4) > 0:
    led.on()
else:
    led.off()
```

### 11. Common Mistakes
*   **Wrong Mask**: Using Bit 2 to mean "the second bit" (value 2) instead of the mathematically correct bit index ($2^2=4$).
*   **Non-binary Thinking**: Thinking it checks the digit "2"—it checks the binary position representing 4.

### 12. Try This Next
*   **Change Number**: Test with `test_num = 2` (LED should be OFF) or `test_num = 12` (LED should be ON).
*   **User Input**: Connect a potentiometer and check the bits of its value dynamically.
"""

    p0522 = """
---

## 1. Project 0522: Blinking Binary Counter

### 2. Learning Objective
Display a random 4-bit binary number using a sequence of four LEDs to visualize a random "nibble".

### 3. Concepts Introduced
*   Binary Nibbles (4 bits)
*   Random Number Generation
*   Bit Extraction Logic
*   Visualizing Binary Patterns

### 4. Hardware Required
*   Raspberry Pi Pico
*   4x LEDs
*   4x 220Ω Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0** | GP16 | Least Significant Bit (1) |
| **LED 1** | GP17 | Value 2 |
| **LED 2** | GP18 | Value 4 |
| **LED 3** | GP19 | Most Significant Bit (8) |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (0 to 15)
*   **from Logic, drag `bitwise_and`** (Mask individual bits)
*   **from Loops, drag `pico_forever`** (Repeat)

### 7. Variables
*   **val**: Integer (Stored random number)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Outputs**:
    *   From **Smart IO**, set GP16, GP17, GP18, GP19 as Outputs.

**B. Main Loop Phase**
2.  **Generate Number**:
    *   From **Math**, set `val` to random integer between 0 and 15.
3.  **Display Bit 0 (1s)**:
    *   If (`val` & 1) > 0: Set GP16 HIGH. Else: LOW.
4.  **Display Bit 1 (2s)**:
    *   If (`val` & 2) > 0: Set GP17 HIGH. Else: LOW.
5.  **Display Bit 2 (4s)**:
    *   If (`val` & 4) > 0: Set GP18 HIGH. Else: LOW.
6.  **Display Bit 3 (8s)**:
    *   If (`val` & 8) > 0: Set GP19 HIGH. Else: LOW.
7.  **Wait**:
    *   From **Time**, wait 0.5 seconds before picking a new number.

### 9. Execution Flow
1.  **Start**: Hardware initializes.
2.  **Generate**: Pico picks a number between 0 and 15 (e.g., 9).
3.  **Convert**: The code checks the binary components of 9 ($8 + 1 \Rightarrow 1001$ in binary).
4.  **Output**: LED 3 and LED 0 turn ON.
5.  **Delay**: Patterns change twice a second.

### 10. Generated Code
```python
from machine import Pin
import time
import random

leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

while True:
    val = random.randint(0, 15)
    
    # Update all 4 pins based on bits
    leds[0].value(1 if (val & 1) else 0)
    leds[1].value(1 if (val & 2) else 0)
    leds[2].value(1 if (val & 4) else 0)
    leds[3].value(1 if (val & 8) else 0)
    
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Order of LEDs**: Placing the LSB (1) on the left of the board can be counter-intuitive; usually, MSB is left and LSB is right.
*   **Range Error**: Picking 0-16. 16 requires a 5th bit ($2^4$) which won't show.

### 12. Try This Next
*   **Double Speed**: Reduce the delay to 0.1s for a "flicker" effect.
*   **8-bit Expansion**: Add 4 more LEDs to GP20-23 to show numbers up to 255.
"""

    p0523 = """
---

## 1. Project 0523: Manual Binary Counter Control

### 2. Learning Objective
Build a manual 4-bit binary incrementer/decrementer using two buttons to control a multi-LED binary display.

### 3. Concepts Introduced
*   Binary Arithmetic (Increment/Decrement)
*   Boundary Clamping (0 and 15)
*   Button Debouncing
*   State Persistence

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons (Up, Down)
*   4x LEDs

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Up** | GP14 | Increment count |
| **Btn Down** | GP15 | Decrement count |
| **LEDs (4x)** | GP16-19 | LSB to MSB |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `if_do`** (Handle press)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **count**: Integer (Current numerical state)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Hardware Config**: Setup 2 Inputs (Pull-Down) and 4 Outputs.
2.  **Reset Count**: Set `count` to 0.

**B. Main Loop Phase**
3.  **Handle Increment**:
    *   If GP14 is HIGH and `count` < 15:
        *   Increment `count` by 1.
        *   Wait 0.2s for debounce.
4.  **Handle Decrement**:
    *   If GP15 is HIGH and `count` > 0:
        *   Decrement `count` by 1.
        *   Wait 0.2s for debounce.
5.  **Display Update**:
    *   Check each bit of `count` (1, 2, 4, 8) and set GP16-19 accordingly.

### 9. Execution Flow
1.  **Monitor**: Pico listens for button signals.
2.  **Logic**: If UP is signal, the internal number increases. It stops at 15 to prevent overflow logic errors.
3.  **Mapping**: The internal base-10 number is translated to 4 physical lights.
4.  **Observation**: Pressing buttons "writes" binary code to the LEDs.

### 10. Generated Code
```python
from machine import Pin
import time

btn_up = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_dn = Pin(15, Pin.IN, Pin.PULL_DOWN)
leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

count = 0

while True:
    if btn_up.value() and count < 15:
        count += 1
        time.sleep(0.2)
    if btn_dn.value() and count > 0:
        count -= 1
        time.sleep(0.2)
        
    for i in range(4):
        leds[i].value(1 if (count & (1 << i)) else 0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **No Clamping**: If count goes to 16, the LEDs will show 0000 (because the 5th bit isn't wired), confusing the user.
*   **Debounce**: No delay results in one press counting as 3 or 4 increments.

### 12. Try This Next
*   **Wrap Around**: Change code so 15 + 1 goes back to 0.
"""

    p0524 = """
---

## 1. Project 0524: Binary Counter Sequences

### 2. Learning Objective
Simulate the "Knight Rider" (KITT) scanner effect by shifting a single active bit bi-directionally across a bank of LEDs.

### 3. Concepts Introduced
*   Bit Shifting (`<<`, `>>`)
*   Directional Flags
*   Boundary Detection
*   Sequential Animation

### 4. Hardware Required
*   Raspberry Pi Pico
*   6x LEDs
*   6x 220Ω Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LEDs (6x)** | GP16-21 | Wired in sequence |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `if_else`** (Direction toggle)
*   **from Math, drag `shift`** (Move bit)

### 7. Variables
*   **pos**: Integer (Current LED index 0-5)
*   **dir**: Integer (1 for Right, -1 for Left)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP16-GP21 as Outputs.
2.  **Start State**: `pos = 0`, `dir = 1`.

**B. Main Loop Phase**
3.  **Identify Active LED**:
    *   Turn all LEDs OFF.
    *   Set LED at current `pos` to HIGH.
4.  **Calculate Movement**:
    *   Update `pos` by adding `dir`.
5.  **Check Edges**:
    *   If `pos` == 4 (near right end): Set `dir = -1`.
    *   If `pos` == 1 (near left end): Set `dir = 1`.
6.  **Wait**: 0.1s for motion speed.

### 9. Execution Flow
1.  **Process**: A single bit starts at position 0.
2.  **Shift**: It moves right every step.
3.  **Detect**: When it hits the last LED, the "Direction" flag flips.
4.  **Return**: The bit shifts back to the start.
5.  **Visual**: Creates a scanning eye effect.

### 10. Generated Code
```python
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(16, 22)]
pos = 0
direction = 1

while True:
    for i in range(6):
        leds[i].value(1 if i == pos else 0)
        
    pos += direction
    if pos == 5 or pos == 0:
        direction *= -1
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Array Out of Bounds**: Setting `pos` to 6 when only 6 LEDs (0-5) exist will cause a crash.
*   **Ghosting**: Not turning the *previous* LED off before turning the next one on.

### 12. Try This Next
*   **Trailing Effect**: Keep the previous LED on at 50% brightness (PWM) for a "comet" look.
"""

    p0525 = """
---

## 1. Project 0525: Interactive Binary Counter

### 2. Learning Objective
Develop a basic Binary Clock that counts seconds (0-59) and displays the count across 6 LEDs.

### 3. Concepts Introduced
*   Timekeeping (`seconds`)
*   Modulo Arithmetic (`% 60`)
*   Multi-bit Mapping
*   6-bit Binary Range (Up to 63)

### 4. Hardware Required
*   Raspberry Pi Pico
*   6x LEDs
*   6x Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LEDs (6x)** | GP16-21 | Values 1, 2, 4, 8, 16, 32 |

### 6. Blocks Used
*   **from Time, drag `pico_wait`**
*   **from Variables, drag `change_variable`** (i = i + 1)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **seconds**: Integer (0 to 59)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init GPIO**: GP16-21 as Outputs.
2.  **Init Clock**: `seconds = 0`.

**B. Main Loop Phase**
3.  **Display Binary**:
    *   Update LEDs 1-32 based on the bits of `seconds`.
4.  **Wait**: Wait **exactly** 1 second.
5.  **Tick**:
    *   Increment `seconds` by 1.
6.  **Cycle Reset**:
    *   If `seconds` >= 60: Set `seconds = 0`.

### 9. Execution Flow
1.  **Start**: The clock starts at 000000.
2.  **Tick**: Every second, the count ripples through the LEDs.
3.  **Carry**: Just like decimal addition, the bits "carry over" (e.g., 011 -> 100).
4.  **Loop**: At 60 seconds (1 minute), the display wipes and begins again.

### 10. Generated Code
```python
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(16, 22)]
sec = 0

while True:
    for i in range(6):
        leds[i].value(1 if (sec & (1 << i)) else 0)
        
    time.sleep(1)
    sec = (sec + 1) % 60
```

### 11. Common Mistakes
*   **Drift**: `time.sleep(1)` isn't perfect; over hours, it will lose time. (Advanced: Use RTC).
*   **Missing Bits**: 59 in binary is 111011. If LED #2 (val 4) is broken, it shows 55.

### 12. Try This Next
*   **Minute LED**: Add a 7th LED that toggles every time the seconds count resets.
"""

    p0526 = """
---

## 1. Project 0526: Smart Binary Counter Switch

### 2. Learning Objective
Implement a "Parity Bit" error-checking algorithm that calculates if an odd number of inputs are active and signals a "check" LED.

### 3. Concepts Introduced
*   Error Detection (Parity)
*   Odd/Even Logic
*   Boolean Accumulation
*   Data Integrity Concepts

### 4. Hardware Required
*   Raspberry Pi Pico
*   3x Switches (Data)
*   1x LED (Parity)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Switch 1-3** | GP14,15,16 | Data bits |
| **Parity LED** | GP17 | ON if number of bits is ODD |

### 6. Blocks Used
*   **from Math, drag `arithmetic`** (Add inputs)
*   **from Logic, drag `is_even`**
*   **from Logic, drag `not`**

### 7. Variables
*   **total_on**: Integer (Sum of active switches)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14-16 as Inputs (Pull-Down). GP17 as Output.

**B. Main Loop Phase**
2.  **Sum Bits**:
    *   Set `total_on` to (Read GP14 + Read GP15 + Read GP16).
3.  **Check Parity (Even Parity Rule)**:
    *   If `total_on % 2` != 0:
        *   Turn LED on GP17 **ON**.
    *   Else:
        *   Turn LED on GP17 **OFF**.

### 9. Execution Flow
1.  **Sense**: Pico reads which switches are flipped.
2.  **Calculate**: It adds them up (e.g., if bit 1 and 3 are on, sum is 2).
3.  **Verify**: With Even Parity, the goal is for the TOTAL bits (switches + LED) to be even.
    *   If sum is 2 (Even), LED stays OFF (Total 2 = Even).
    *   If sum is 3 (Odd), LED turns ON (Total 4 = Even).
4.  **Result**: The system "corrects" the parity in real-time.

### 10. Generated Code
```python
from machine import Pin
import time

switches = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in [14, 15, 16]]
parity_led = Pin(17, Pin.OUT)

while True:
    on_count = sum([s.value() for s in switches])
    
    # Even Parity Logic: If sum is ODD, Parity bit becomes 1
    if on_count % 2 != 0:
        parity_led.on()
    else:
        parity_led.off()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Confusion between Even/Odd Parity**: In Odd Parity, the goal is for the total to be ODD.
*   **Switch Bounce**: Rapidly flipping a switch might cause the LED to flicker for a millisecond.

### 12. Try This Next
*   **Odd Parity**: Change the logic so the LED turns on only when the sum is already even.
"""

    p0527 = """
---

## 1. Project 0527: Binary Counter Alarm System

### 2. Learning Objective
Design a system that monitors a 4-bit count and triggers a physical alarm (Buzzer) if the value exceeds its maximum capacity (Overflow).

### 3. Concepts Introduced
*   Overflow Detection
*   System Reset Logic
*   Safety Interlocks
*   Buzzer Control

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x Button (Add +1)
*   1x Buzzer
*   4x LEDs (Monitor)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Add** | GP14 | Increment |
| **Buzzer** | GP15 | Alarm Output |
| **LEDs** | GP16-19 | Binary display |

### 6. Blocks Used
*   **from Logic, drag `greater_than`** (Check 15)
*   **from Variables, drag `set_variable`** (Reset)
*   **from Smart IO, drag `pico_buzzer_beep`**

### 7. Variables
*   **count**: Integer (0 to 16)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Buttons, LEDs, and Buzzer.
2.  **Reset**: `count = 0`.

**B. Main Loop Phase**
3.  **Handle Input**:
    *   If Button pressed: Increment `count` by 1.
4.  **Check Overflow**:
    *   If `count` > 15:
        *   **Trigger Alarm**: Beep buzzer for 1s.
        *   **Reset**: Set `count = 0`.
5.  **Display**: Show `count` bits on LEDs.

### 9. Execution Flow
1.  **Process**: User adds numbers to the 4-bit memory.
2.  **Monitor**: The system constantly compares memory against the size limit (2^4-1 = 15).
3.  **Alarm**: If user adds 1 to 15, the "Overflow" condition is met.
4.  **Action**: The system warns the user with sound and wipes the memory clean.

### 10. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)
leds = [Pin(i, Pin.OUT) for i in range(16, 20)]

count = 0

while True:
    if btn.value():
        count += 1
        time.sleep(0.2)
        
        if count > 15:
            # Overflow!
            buzzer.on()
            time.sleep(0.5)
            buzzer.off()
            count = 0
            
    for i in range(4):
        leds[i].value(1 if (count & (1 << i)) else 0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Zero Index**: Forgetting that 1111 (all on) is 15, not 16.
*   **Blocking Code**: If the buzzer "on" code uses `time.sleep`, buttons won't work while the buzzer is sounding.

### 12. Try This Next
*   **Critical Warning**: Flash all LEDs red (if RGB) when overflow occurs.
"""

    p0528 = """
---

## 1. Project 0528: The Binary Counter Game

### 2. Learning Objective
Improve binary-to-decimal mental math by creating an educational terminal game where the Pico displays random patterns for the player to decode.

### 3. Concepts Introduced
*   Human-Computer Interaction (HCI)
*   UART/Terminal Communication
*   Mathematical Verification
*   Educational Drills

### 4. Hardware Required
*   Raspberry Pi Pico
*   4x LEDs

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LEDs (4x)** | GP16-19 | Binary bits (8, 4, 2, 1) |

### 6. Blocks Used
*   **from Text, drag `input`** (Get user guess)
*   **from Math, drag `random_integer`**
*   **from Logic, drag `if_else`**

### 7. Variables
*   **target**: Integer (The secret number)
*   **guess**: Integer (User's input)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Display**: GP16-19 as Outputs.

**B. Main Loop Phase**
2.  **New Round**:
    *   Pick random `target` from 1 to 15.
3.  **Show Challenge**:
    *   Update LEDs to match bit pattern of `target`.
    *   Print: "What number is shown on the LEDs?"
4.  **Get Guess**:
    *   Wait for user to type number in Thonny/MicroPython console.
5.  **Calculate Result**:
    *   If `guess` == `target`:
        *   Print "Correct! Well done."
        *   Flash all LEDs twice.
    *   Else:
        *   Print "Incorrect. The answer was [target]".
6.  **Pause**: 1s before next round.

### 9. Execution Flow
1.  **Generate**: Pico generates a binary puzzle.
2.  **Prompt**: The player sees a light pattern (e.g., ON, OFF, ON, OFF).
3.  **Logic**: Player calculates ($8 + 2 = 10$).
4.  **Verification**: Pico compares the player's text input against the integer.
5.  **Score**: Provides instant feedback via terminal.

### 10. Generated Code
```python
from machine import Pin
import random
import time

leds = [Pin(i, Pin.OUT) for i in range(16, 20)]

while True:
    target = random.randint(1, 15)
    
    # Display on LEDs (LSB=0, MSB=3)
    for i in range(4):
        leds[i].value(1 if (target & (1 << i)) else 0)
    
    print("\\n--- New Challenge ---")
    try:
        guess = int(input("Convert the LED pattern to Decimal: "))
        
        if guess == target:
            print("CORRECT! You're a binary master.")
        else:
            print(f"WRONG. The pattern was {target}.")
    except ValueError:
        print("Please enter a valid number.")
        
    time.sleep(1)
```

### 11. Common Mistakes
*   **Input Blocking**: The `input()` command pauses the code entirely. If you want other animations to run while waiting, you can't use this simple command.
*   **Endianness**: Ensure the LEDs are physically arranged so the biggest bit (8) is on the side the user expects.

### 12. Try This Next
*   **Timer**: Add a delay—if the user doesn't answer in 5 seconds, they lose a life.
"""

    p0529 = """
---

## 1. Project 0529: Automated Binary Counter

### 2. Learning Objective
Implement a BCD (Binary Coded Decimal) counter that counts from 0-99 and displays the ones and tens digits separately using two 4-LED banks.

### 3. Concepts Introduced
*   Binary Coded Decimal (BCD)
*   Digit Separation (Division/Modulo)
*   Expanded GPIO Mapping (8 Outputs)
*   Cooperative Displays

### 4. Hardware Required
*   Raspberry Pi Pico
*   8x LEDs
*   8x Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Ones (4 LEDs)** | GP10-13 | 0 to 9 in Binary |
| **Tens (4 LEDs)** | GP16-19 | 10 to 90 in Binary digits |

### 6. Blocks Used
*   **from Math, drag `modulo`** (Get remainder)
*   **from Math, drag `division`** (Get quotient)
*   **from Loops, drag `count_with`**

### 7. Variables
*   **count**: Integer (0-99)
*   **ones**: Integer (0-9)
*   **tens**: Integer (0-9)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure 8 Outputs**: GP10-13 and GP16-19.

**B. Main Loop Phase**
2.  **Iterate Count**: Loop `count` from 0 to 99.
3.  **Split Digits**:
    *   Set `ones` = `count` % 10.
    *   Set `tens` = `count` // 10 (Integer division).
4.  **Display Ones**:
    *   Map the 4 bits of `ones` to GP10-GP13.
5.  **Display Tens**:
    *   Map the 4 bits of `tens` to GP16-GP19.
6.  **Wait**: 0.5s per increment.

### 9. Execution Flow
1.  **Start**: System starts at 0 (All LEDs off).
2.  **Splitting**: At number 23, the Pico calculates 2 and 3.
3.  **Translation**:
    *   Tens LEDs show `0010` (Value 2).
    *   Ones LEDs show `0011` (Value 3).
4.  **Observation**: This makes long binary numbers much easier for humans to read because it maps to standard decimal positions.

### 10. Generated Code
```python
from machine import Pin
import time

ones_leds = [Pin(i, Pin.OUT) for i in range(10, 14)]
tens_leds = [Pin(i, Pin.OUT) for i in range(16, 20)]

while True:
    for count in range(100):
        o = count % 10
        t = count // 10
        
        # Display Ones
        for i in range(4):
            ones_leds[i].value(1 if (o & (1 << i)) else 0)
            
        # Display Tens
        for i in range(4):
            tens_leds[i].value(1 if (t & (1 << i)) else 0)
            
        time.sleep(0.5)
```

### 11. Common Mistakes
*   **Integer Division**: Using `/` instead of `//` in Python will return a float (e.g. 2.0), which bitwise logic cannot process.
*   **Wiring**: Swapping the "Ones" and "Tens" cable bundles will show very strange numbers.

### 12. Try This Next
*   **Hex Display**: Change the code so each 4-bit block shows 0-F (Hexadecimal) instead of stopping at 9.
"""

    p0530 = """
---

## 1. Project 0530: Mastering Binary Counter

### 2. Learning Objective
Emulate a "Serial-to-Parallel" communication protocol (similar to a 74HC595 shift register) by manually pulsing clock and data lines to send a byte.

### 3. Concepts Introduced
*   Synchronous Serial Protocol
*   Clock and Data Lines
*   Bitwise Decomposition
*   Function-based Automation (`shiftOut`)

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x LEDs (Simulating Logic Lines)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Data Pin** | GP16 | Representing BIT state |
| **Clock Pin** | GP17 | Representing SYNC signal |

### 6. Blocks Used
*   **from Functions, drag `to_procedure`** (Create shiftOut)
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Loops, drag `count_with`**

### 7. Variables
*   **payload**: Integer (Number to send, e.g. 170)
*   **bit_index**: Integer (0 to 7)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Set GP16 and GP17 as Outputs.

**B. Define Transfer Function**
2.  **Define `Send_Byte`**:
    *   Loop `bit_index` from 7 down to 0.
    *   Check if Bit `bit_index` of payload is on.
    *   **Step A (Data)**: Set DATA (GP16) to HIGH or LOW.
    *   **Step B (Clock)**: Set CLOCK (GP17) HIGH, then LOW. (This "taps" the bit into memory).

**C. Main Loop Phase**
3.  **Execute**:
    *   Call `Send_Byte` with value 170 (Binary `10101010`).
    *   Wait 2s.
    *   Call `Send_Byte` with value 255.
    *   Wait 2s.

### 9. Execution Flow
1.  **Process**: Instead of having many wires, we use 2.
2.  **Logic**: For every bit in the number, we set a wire and then blink the clock wire.
3.  **Timing**: The receiver (simulated) knows to look at the Data wire only when the Clock wire blinks.
4.  **Result**: We can send large numbers across single wires.

### 10. Generated Code
```python
from machine import Pin
import time

data_pin = Pin(16, Pin.OUT)
clock_pin = Pin(17, Pin.OUT)

def shift_out(byte):
    print(f"Sending: {bin(byte)}")
    # Send bits MSB first (bit 7 down to 0)
    for i in range(7, -1, -1):
        # Set Data
        bit = (byte >> i) & 1
        data_pin.value(bit)
        
        # Pulse Clock
        clock_pin.on()
        time.sleep(0.01) # Short pulse
        clock_pin.off()
        time.sleep(0.01)

while True:
    shift_out(170) # 10101010
    time.sleep(2)
    shift_out(15)  # 00001111
    time.sleep(2)
```

### 11. Common Mistakes
*   **Clock Pulse too fast**: If the pulse is too short, the receiver might miss it.
*   **Endianness**: Sending Bit 0 first (LSB First) instead of Bit 7 (MSB First) will flip the number at the receiver.

### 12. Try This Next
*   **Shift Register**: Connect a real 74HC595 chip to these pins and control 8 LEDs with only 3 wires!
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0521 + p0522 + p0523 + p0524 + p0525 + p0526 + p0527 + p0528 + p0529 + p0530)
    
    print("Batch 53 (0521-0530) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch53()
