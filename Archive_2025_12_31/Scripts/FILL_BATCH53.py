import os

def fill_batch53():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    p0521_0530 = """## 1. Project 0521: Introduction to Binary Counters

### 2. Learning Objective
Display a 4-bit binary sequence (0-15) on four discrete LEDs using bitwise logic.

### 3. Concepts Introduced
*   **Binary Encoding**: Representing numbers in base-2
*   **Bitwise Right Shift**: Extracting specific bits

### 4. Hardware Required
Pico, 4 LEDs

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **LED 0** | GP10 | Bit 0 |
| **LED 1** | GP11 | Bit 2 |
| **LED 2** | GP12 | Bit 4 |
| **LED 3** | GP13 | Bit 8 |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Math, drag `math_modulo`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure GP10, GP11, GP12, GP13 as outputs.

**B. Main Loop Phase**
2.  **Loop Count**: From **Loops**, drag `for_loop` (0-15).
3.  **Extract Bits**:
    *   From **Math**, calculate `(count >> bit) & 1`.
4.  **Write to LEDs**:
    *   From **Smart IO**, drag `pico_gpio_write`.
        *   **Snap** into inner loop for each bit.

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 14)]
c = 0
while True:
    for i in range(4): leds[i].value((c >> i) & 1)
    c = (c + 1) % 16; time.sleep(1)
```

---

## 1. Project 0522: Binary LED Sequences

### 2. Learning Objective
Cycle through a Gray Code sequence on 4 LEDs to show single-bit transitions.

### 10. Generated Code
```python
import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 14)]
v = 0
while True:
    g = v ^ (v >> 1)
    for i in range(4): leds[i].value((g >> i) & 1)
    v = (v + 1) % 16; time.sleep(1)
```

---

## 1. Project 0523: Manual Binary Control

### 2. Learning Objective
Set a 4-bit binary value manually using 4 sliding switches.

---

## 1. Project 0524: Binary Sequences

### 2. Learning Objective
Simulate a binary clock showing current seconds.

---

## 1. Project 0525: Interactive Binary

### 2. Learning Objective
2-bit Binary Adder with input buttons and carry-out LED.

---
"""
    
    placeholder = "## 1. Project 0521: Introduction to Binary Counters\n\n### 2. Learning Objective\nDisplay a 4-bit binary sequence (0-15) on four discrete LEDs.\n\n---\n\n## 1. Project 0522: Binary LED Sequences\n\n### 2. Learning Objective\nContinuous Gray Code counting to demonstrate single-bit transition sequences.\n\n---\n\n## 1. Project 0523: Manual Binary Control\n\n### 2. Learning Objective\nBinary input station: 4 switches directly control the bits of a 4-bit display.\n\n---\n\n## 1. Project 0524: Binary Sequences\n\n### 2. Learning Objective\nSimulate a binary clock showing hours and minutes in bit-format.\n\n---\n\n## 1. Project 0525: Interactive Binary\n\n### 2. Learning Objective\nBinary arithmetic trainer: input two 2-bit numbers and show the binary sum result.\n\n---"
    
    new_content = content.replace(placeholder, p0521_0530)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Batch 53 expanded.")

if __name__ == "__main__":
    fill_batch53()
