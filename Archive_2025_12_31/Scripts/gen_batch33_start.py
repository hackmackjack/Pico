# Pass 1 FINAL: Batch 33 - Binary Counter 2 (Projects 0321-0330)
# Following locked Elite template from Batches 31-32

batch_33_content = '''

---

# 🏁 Batch 33: Binary Counter 2

## 1️⃣ Project 0321: Introduction to Binary Counter

### 2️⃣ Learning Objective
Determine if a number is odd or even using bitwise operations. You will learn to check the least significant bit (LSB) to understand binary representation and bitwise AND operations.

### 3️⃣ Concepts Introduced
*   **Bitwise AND**: Using `&` operator to check specific bits.
*   **Least Significant Bit (LSB)**: The rightmost bit (bit 0) determines odd/even.
*   **Binary Representation**: Understanding how numbers are stored in binary form.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**
*   **220Ω Resistor**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Positive** | GP15 | Via 220Ω Resistor |
| **LED Negative** | GND | Common Ground |

### 6️⃣ Blocks Used

🔹 **Setup Pin**
*   **Category:** Outputs
*   **Block:** `Setup Pin:[15] as OUTPUT`

🔹 **Digital Write**
*   **Category:** Pin Access
*   **Block:** `set Pin [15] to [HIGH/LOW]`

🔹 **Bitwise AND**
*   **Category:** Math
*   **Block:** `[number] & [1]`

🔹 **Sleep**
*   **Category:** Timing
*   **Block:** `sleep [N] seconds`

### 7️⃣ Variables & State
*   **testNumber**: The number to check (hardcoded, e.g., starts at 0, increments each loop).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup Pin:[15] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [testNumber] to [0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check LSB (Odd/Even)**:
        *   From **Logic**, drag `if ([testNumber] & [1]) = [1] then`.
            *   **Snap** into loop.
            *   Then (Odd): From **Pin Access**, drag `set Pin [15] to [HIGH]`.
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Then (Even): From **Pin Access**, drag `set Pin [15] to [LOW]`.
    *   **Increment Number**:
        *   From **Variables**, drag `change [testNumber] by [1]`.
            *   **Snap** below.
        *   From **Logic**, drag `if [testNumber] > [20] then set [testNumber] to [0]`.
            *   **Snap** below (loop through 0-20 for demo).
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico initializes with testNumber=0. Each loop, it performs a bitwise AND operation between testNumber and 1 (`testNumber & 1`). In binary, the number 1 is represented as ...0001, so the AND operation isolates only the LSB of testNumber. If LSB is 1 (odd number), the result is 1 and the LED turns ON. If LSB is 0 (even number), the result is 0 and the LED turns OFF. The number increments each loop (0→1→2...→20→0), causing the LED to blink alternately as it cycles through odd and even numbers, demonstrating that the LSB directly indicates parity.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
testNumber = 0

while True:
    # Check if odd (LSB = 1)
    if testNumber & 1:
        led.on()
    else:
        led.off()
    
    testNumber += 1
    if testNumber > 20:
        testNumber = 0
    
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Bitwise Operator**: Using `%` (modulo) instead of `&` (bitwise AND) works for odd/even but doesn't teach bitwise concepts. Stick to `& 1` for this project.
*   **LED Always On/Off**: If LED doesn't blink, verify the number is actually incrementing. Print testNumber to console for debugging.
*   **No Understanding**: Explain that in binary: 5 = 0101 (LSB=1, odd), 6 = 0110 (LSB=0, even). The `& 1` operation masks all bits except LSB.

### 1️⃣2️⃣ Try This Next

*   **User Input**: Instead of auto-incrementing, read a number from serial input and check if it's odd or even.
*   **Divisible by 4**: Check if `testNumber & 3` equals 0 to determine divisibility by 4 (last 2 bits must be 00).
*   **Power of 2**: Check if `testNumber & (testNumber - 1)` equals 0 to detect powers of 2.

---

## 1️⃣ Project 0322: Blinking Binary Counter

### 2️⃣ Learning Objective
Visualize bit shifting by making a single LED appear to "scan" across multiple bit positions. You will learn left shift operations and how binary patterns can represent positional data.

### 3️⃣ Concepts Introduced
*   **Bit Shifting**: Using `<<` operator to move a bit left.
*   **LED Array**: Using multiple LEDs to represent individual bits.
*   **Positional Binary**: Each LED represents a specific bit position (2⁰, 2¹, 2², 2³).

### 4️⃣ Hardware Required
*   **Pico**
*   **4-8 LEDs**
*   **4-8× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 0 (Bit 0)** | GP10 | Via 220Ω Resistor |
| **LED 1 (Bit 1)** | GP11 | Via 220Ω Resistor |
| **LED 2 (Bit 2)** | GP12 | Via 220Ω Resistor |
| **LED 3 (Bit 3)** | GP13 | Via 220Ω Resistor |
| **All LED Negatives** | GND | Common Ground |

### 6️⃣ Blocks Used

🔹 **Setup Pin (×4)**
*   **Category:** Outputs
*   **Block:** `Setup Pin:[10/11/12/13] as OUTPUT`

🔹 **Digital Write**
*   **Category:** Pin Access
*   **Block:** `set Pin [N] to [HIGH/LOW]`

🔹 **Bit Shift**
*   **Category:** Math
*   **Block:** `1 << [position]`

### 7️⃣ Variables & State
*   **bit Position**: Current bit position being lit (0-3).
*   **pattern**: The binary pattern with single bit set (1, 2, 4, 8).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup Pin:[10] as OUTPUT`.
        *   **Snap** into setup block.
    *   Repeat for pins 11, 12, 13 (×4 total).
    *   From **Variables**, drag `set [bitPosition] to [0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Calculate Pattern**:
        *   From **Variables**, drag `set [pattern] to [1 << bitPosition]`.
            *   **Snap** into loop.
    *   **Update LEDs**:
        *   From **Logic**, drag `set Pin [10] to [HIGH if (pattern & 1) else LOW]`.
            *   **Snap** below.
        *   From **Logic**, drag `set Pin [11] to [HIGH if (pattern & 2) else LOW]`.
            *   **Snap** below.
        *   From **Logic**, drag `set Pin [12] to [HIGH if (pattern & 4) else LOW]`.
            *   **Snap** below.
        *   From **Logic**, drag `set Pin [13] to [HIGH if (pattern & 8) else LOW]`.
            *   **Snap** below.
    *   **Advance Bit Position**:
        *   From **Variables**, drag `change [bitPosition] by [1]`.
            *   **Snap** below.
        *   From **Logic**, drag `if [bitPosition] > [3] then set [bitPosition] to [0]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.3] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system starts with bitPosition=0. It calculates pattern = 1 << 0 = 1 (binary: 0001). This turns ON only LED0 (bit 0). After 0.3s, bitPosition increments to 1, pattern = 1 << 1 = 2 (binary: 0010), turning ON only LED1. This continues: position 2 → pattern 4 (0100) → LED2, position 3 → pattern 8 (1000) → LED3. After position 3, it wraps to 0, creating a continuous scanning effect where one lit LED appears to move left across the array. This visually demonstrates how left shift operations multiply by 2 and shift the bit position.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leds = [
    machine.Pin(10, machine.Pin.OUT),
    machine.Pin(11, machine.Pin.OUT),
    machine.Pin(12, machine.Pin.OUT),
    machine.Pin(13, machine.Pin.OUT)
]

bitPosition = 0

while True:
    pattern = 1 << bitPosition
    
    # Update each LED based on pattern
    for i in range(4):
        if pattern & (1 << i):
            leds[i].on()
        else:
            leds[i].off()
    
    bitPosition = (bitPosition + 1) % 4
    time.sleep(0.3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **All LEDs On**: If all LEDs light simultaneously, verify you're using bitwise AND (`&`) to check each bit, not OR (`|`).
*   **No Scanning**: If only one LED stays on, ensure bitPosition increments and wraps correctly (0→1→2→3→0).
*   **Reversed Order**: If scanning goes right-to-left instead of left-to-right, verify LED wiring matches pin assignments (GP10=LED0=rightmost).
*   **Wrong Shift Direction**: Using right shift (`>>`) instead of left shift (`<<`) will not work for this visualization.

### 1️⃣2️⃣ Try This Next

*   **Bi-Directional Scan**: After reaching LED3, reverse direction and scan back to LED0 (Knight Rider effect).
*   **Variable Speed**: Use a potentiometer to control the sleep duration, changing scan speed dynamically.
*   **8-Bit Display**: Use 8 LEDs to visualize a full byte, showing scans from bit 0 to bit 7.

---

[CONTINUING WITH PROJECTS 0323-0330...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_33_content)

print("✅ Projects 0321-0322 appended (Batch 33 started)")
print("⏳ Generating remaining 8 projects (0323-0330)...")
