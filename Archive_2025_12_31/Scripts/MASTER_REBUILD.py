import os

def master_rebuild():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Read the current content
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # We keep the first 1970 lines which contain the correct Batch 51 and Batch 52
    high_quality_base = "".join(lines[:1970])
    
    print(f"Base size: {len(high_quality_base)} characters")
    
    # Now we need to generate Batches 53-60 (0521-0600)
    # I will start with Batch 53: Binary Counters
    
    batch_53 = """
# 🔢 Batch 53: Binary Counter 3

---

## 1. Project 0521: Introduction to Binary Counters

### 2. Learning Objective
Display a 4-bit binary count (0-15) using 4 LEDs.

### 3. Concepts Introduced
*   **Binary Representation**: Power of 2 (1, 2, 4, 8)
*   **Bit Manipulation**: Converting decimal to binary states

### 4. Hardware Required
Pico, 4 LEDs, 4 Resistors

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LED 0 (LSB)** | GP10 | 220Ω |
| **LED 1** | GP11 | 220Ω |
| **LED 2** | GP12 | 220Ω |
| **LED 3 (MSB)** | GP13 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Math, drag `math_modulo`**
*   **from Variables, drag `variables_set`**

### 7. Variables
*   **count**: Decimal value (0-15)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output Pins**:
    *   From **Smart IO**, drag `pico_gpio_write` setup blocks.
        *   **Snap** into setup section.
        *   Configure GP10, GP11, GP12, GP13 as outputs.
2.  **Reset Counter**:
    *   From **Variables**, drag `variables_set`.
        *   **Snap** below.
        *   Set `count` = 0.

**B. Main Loop Phase**
3.  **Calculate Bit States**:
    *   From **Variables**, drag logic to check if `count` bit 0 is HIGH.
        *   **Snap** into loop.
4.  **Update Hardware**:
    *   From **Smart IO**, drag `pico_gpio_write` for each LED.
        *   **Snap** below.
5.  **Increment**:
    *   From **Math**, set `count` = `count` + 1.
    *   From **Math**, if `count` > 15: set `count` = 0.
6.  **Delay**:
    *   From **Time**, drag `pico_wait` (1s).

### 9. Execution Flow
The system iterates through decimal numbers 0-15. For each number, it determines the HIGH/LOW state for 4 GPIO pins representing bits, then waits.

### 10. Generated Code
```python
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(10, 14)]
count = 0

while True:
    for i in range(4):
        leds[i].value((count >> i) & 1)
    count = (count + 1) % 16
    time.sleep(1)
```

---

## 1. Project 0522: Binary LED Sequences

### 2. Learning Objective
Binary "Gray Code" counter - only one bit changes at a time to prevent errors.

### 3. Concepts Introduced
*   **Gray Code**: Single-bit transition logic

### 4. Hardware Required
Pico, 4 LEDs

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LEDs** | GP10-13 | Binary Array |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Math, drag `bit_xor`**

### 7. Variables
*   **val**: Binary state
*   **gray**: Converted state

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Hardware**: Configure GP10-13 as outputs.

**B. Main Loop Phase**
2.  **Convert to Gray**:
    *   From **Math**, `gray` = `val` XOR (`val` >> 1).
        *   **Snap** into loop.
3.  **Display**:
    *   From **Smart IO**, write bits of `gray` to pins.
4.  **Iterate**: increment `val`.

### 10. Generated Code
```python
from machine import Pin
import time
leds = [Pin(i, Pin.OUT) for i in range(10, 14)]
val = 0
while True:
    gray = val ^ (val >> 1)
    for i in range(4):
        leds[i].value((gray >> i) & 1)
    val = (val + 1) % 16
    time.sleep(1)
```

---
"""
    # I am going to save this first part and continue the generation.
    # To avoid cutting corners, I will produce the rest of the 8 batches properly.
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(high_quality_base + batch_53)
        
    print("Base rebuilt. Project 0521-0522 Added.")

if __name__ == "__main__":
    master_rebuild()
