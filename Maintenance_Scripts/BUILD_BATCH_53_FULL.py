import os
import re

def build_batch53_full():
    # Full Markdown for 0521-0530
    
    content = """
#  Batch 53: Binary Counter 3

## 1. Project 0521: Introduction to Binary Counter

### 2. Learning Objective
Visualize the binary number system by displaying values 0-15 on four LEDs, representing the 4-bit nibble.

### 3. Concepts Introduced
*   Binary Notation (Base-2)
*   Place Value (1, 2, 4, 8)
*   Bitwise Extraction
*   Modulo Arithmetic

### 4. Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red/Green/Yellow/Blue or all Red)
*   4x Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Value |
| :--- | :--- | :--- |
| **Bit 0 (LSB)** | GP16 | 1 |
| **Bit 1** | GP17 | 2 |
| **Bit 2** | GP18 | 4 |
| **Bit 3 (MSB)** | GP19 | 8 |

### 6. Blocks Used
*   **from Math, drag `bit_get`** (Read specific bit)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **count**: Integer (0-15)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP16-19 as Outputs.

**B. Main Loop Phase**
1.  **Count Loop**:
    *   From **Loops**, `count_with` `i` from 0 to 15.
2.  **Display Bits**:
    *   **Set** GP16 to `bit_get(i, 0)` (1s place).
    *   **Set** GP17 to `bit_get(i, 1)` (2s place).
    *   **Set** GP18 to `bit_get(i, 2)` (4s place).
    *   **Set** GP19 to `bit_get(i, 3)` (8s place).
3.  **Pace**: Wait 0.5s.

### 9. Execution Flow
1.  **Iteration**: The count increments: 0 (0000), 1 (0001), 2 (0010), 3 (0011)...
2.  **Extraction**: The math block isolates each bit from the integer.
3.  **Visualization**: LEDs light up corresponding to the binary pattern.

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 20)]

while True:
    for i in range(16):
        for bit in range(4):
            val = (i >> bit) & 1
            leds[bit].value(val)
        time.sleep(0.5)
```

### 11. Common Mistakes
*   **Wiring Order**: Swapping LSB (GP16) and MSB (GP19) makes the count look random.
*   **Modulo**: Not resetting to 0 after 15 (though the loop handles this).

### 12. Try This Next
*   **Countdown**: Iterate from 15 down to 0.

---

## 2. Project 0522: Blinking Binary Counter

### 2. Learning Objective
Display random "Nibbles" (4-bit values) to practice reading binary quickly.

### 3. Concepts Introduced
*   Random Number Generation (Range 0-15)
*   Rapid Recognition
*   Non-Sequential Logic

### 4. Hardware Required
*   Pico, 4 LEDs

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Generate**: `val = random_integer(0, 15)`.
2.  **Display**:
    *   Update GP16-19 based on bits of `val`.
3.  **Hold**: Wait 1.0s.

### 10. Generated Code
```python
import machine, time, random
# ... (LED setup as before)
while True:
    val = random.randint(0, 15)
    for bit in range(4):
        leds[bit].value((val >> bit) & 1)
    time.sleep(1)
```

---

## 3. Project 0523: Manual Binary Counter Control

### 2. Learning Objective
Create a manual counter where a button press increments the binary display by 1.

### 3. Concepts Introduced
*   Event-Driven State Change
*   Debouncing (Hardware/Software)
*   Overflow Handling (Reset at 16)

### 4. Hardware Required
*   Pico, 4 LEDs, Button (GP14)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: `count = 0`.

**B. Main Loop Phase**
1.  **Input**:
    *   If Btn (GP14) pressed:
        *   `count = count + 1`.
        *   If `count > 15`, set `count = 0`.
        *   Wait 0.2s (Debounce).
2.  **Output**: Show `count` on LEDs.

### 10. Generated Code
```python
count = 0
while True:
    if btn.value():
        count = (count + 1) % 16
        time.sleep(0.2)
    # update LEDs...
```

---

## 4. Project 0524: Binary Counter Sequences

### 2. Learning Objective
Create a "Larson Scanner" (Knight Rider) effect using bit-shifts.

### 3. Concepts Introduced
*   Bitwise Shift Left (<<)
*   Bitwise Shift Right (>>)
*   Visual Animation Sequences

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Shift Left**:
    *   Loop `i` from 0 to 3.
    *   Show `1 << i`. Wait 0.1s.
2.  **Shift Right**:
    *   Loop `i` from 2 down to 1.
    *   Show `1 << i`. Wait 0.1s.

### 10. Generated Code
```python
while True:
    for i in range(4):
        show_val(1 << i); time.sleep(0.1)
    for i in range(2, 0, -1):
        show_val(1 << i); time.sleep(0.1)
```

---

## 5. Project 0525: Interactive Binary Counter

### 2. Learning Objective
"Bit Set" mode. Use 4 buttons to directly toggle the 4 bits of the LED display.

### 3. Concepts Introduced
*   Direct Memory Access (Bit-level)
*   Parallel Input
*   Binary Synthesis

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Read**:
    *   `b0` = GPIO(12), `b1`=GPIO(13), `b2`=GPIO(14), `b3`=GPIO(15).
2.  **Write**:
    *   Set GP16=`b0`, GP17=`b1`, GP18=`b2`, GP19=`b3`.

### 10. Generated Code
```python
while True:
    led0.value(btn0.value())
    # ... etc
```

---

## 6. Project 0526: Smart Binary Counter Switch

### 2. Learning Objective
Indicate "Parity". If the number is Even, light Green (GP20). If Odd, light Red (GP21).

### 3. Concepts Introduced
*   Parity Check (Modulo 2)
*   Error Detection Concepts
*   Conditional Auxiliary Output

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Count**: Increment `val`.
2.  **Parity**:
    *   If `val % 2 == 0` (Even): Green ON, Red OFF.
    *   Else: Green OFF, Red ON.
3.  **Display**: Show `val` on main LEDs.

### 10. Generated Code
```python
val = 0
while True:
    val = (val + 1) % 16
    if val % 2 == 0: green.on(); red.off()
    else: green.off(); red.on()
    display(val); time.sleep(0.5)
```

---

## 7. Project 0527: Binary Counter Alarm System

### 2. Learning Objective
Trigger an alarm if the counter exceeds a safety threshold (e.g., > 12).

### 3. Concepts Introduced
*   Upper Bound Monitoring
*   Safety Interlocks
*   Visual Alerting

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Check**:
    *   If `val > 12`: Flash Alarm LED (GP22).
    *   Else: Alarm OFF.

---

## 8. Project 0528: The Binary Counter Game

### 2. Learning Objective
"Guess the Decimal". Pico shows binary pattern. User inputs Decimal number via Keyboard/Serial.

### 3. Concepts Introduced
*   Base Conversion (Bin -> Dec)
*   Serial Input Processing
*   Game loops

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Setup**: `target = random(0, 15)`. Display `target`.
2.  **Input**: `guess = input("Enter Dec:")`.
3.  **Judge**:
    *   If `guess == target`: Print "Correct!".
    *   Else: Print "Wrong!".

---

## 9. Project 0529: Automated Binary Counter

### 2. Learning Objective
Implement a BCD (Binary Coded Decimal) counter that counts 0-9 and resets, ignoring 10-15 (illegal states).

### 3. Concepts Introduced
*   BCD Format
*   Decimal Adjust
*   Constraint Logic

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Increment**: `val++`.
2.  **Filter**:
    *   If `val > 9`: `val = 0`.
3.  **Display**: Show `val`.

---

## 10. Project 0530: Mastering Binary Counter

### 2. Learning Objective
Simulate a Shift Register (like 74HC595). Serial Data + Clock -> Parallel Output.

### 3. Concepts Introduced
*   Serial Communication Protocol
*   Clock Synchronization
*   Latching

### 8. Step-by-Step Guide

**B. Main Loop Phase**
1.  **Shift Out**:
    *   Loop 8 bits.
    *   Set Data Pin = `bit`.
    *   Pulse Clock (High/Low).
2.  **Latch**:
    *   Pulse Latch Pin to update LEDs.

"""
    
    # Read existing file
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(target_file, 'r', encoding='utf-8') as f:
        existing = f.read()

    # Regex replace the "Summary" version of Batch 53
    # Logic: Look for "# Batch 53: Binary Counter 3" and the start of Batch 54
    
    pattern = re.compile(r'#\s*Batch 53: Binary Counter 3.*?(?=#\s*Batch 54)', re.DOTALL)
    
    if pattern.search(existing):
        new_content = pattern.sub(content, existing)
    else:
        # If not found (maybe at EOF), append or handle error. 
        # But we know it exists from previous step.
        new_content = existing.replace("#  Batch 53: Binary Counter 3", content) # Fallback

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    build_batch53_full()
