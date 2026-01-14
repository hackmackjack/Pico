
def append_high_quality(content):
    with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'a', encoding='utf-8') as f:
        f.write(content)

batch_53_cont = """
## 1. Project 0523: Manual Binary Control

### 2. Learning Objective
Binary input - 2 buttons representing bits 2^0 and 2^1. Display result on LEDs.

### 3. Concepts Introduced
*   **Combinatorial Binary**: Real-time bit summing

### 4. Hardware Required
Pico, 2 Buttons, 2 LEDs

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Btn 0** | GP14 | Bit 0 |
| **Btn 1** | GP15 | Bit 1 |
| **LED 0** | GP10 | Val 1 |
| **LED 1** | GP11 | Val 2 |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **b0**, **b1**: Inputs

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Pins GP14,15 as In (PullDown); GP10,11 as Out.

**B. Main Loop Phase**
2.  **Read Inputs**:
    *   From **Smart IO**, drag `pico_gpio_read` for GP14.
        *   **Snap** into loop.
    *   From **Smart IO**, drag `pico_gpio_read` for GP15.
        *   **Snap** below.
3.  **Sync Outputs**:
    *   From **Smart IO**, drag `pico_gpio_write` for GP10. Set to `b0`.
    *   From **Smart IO**, drag `pico_gpio_write` for GP11. Set to `b1`.

### 10. Generated Code
```python
from machine import Pin
b0 = Pin(14, Pin.IN, Pin.PULL_DOWN)
b1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
l0 = Pin(10, Pin.OUT)
l1 = Pin(11, Pin.OUT)
while True:
    l0.value(b0.value())
    l1.value(b1.value())
```

---

## 1. Project 0524: Binary Sequences

### 2. Learning Objective
"Binary Clock" simulation - seconds represented in 6-bit binary.

### 3. Concepts Introduced
*   **Time Encoding**: Seconds to bits conversion

### 4. Hardware Required
Pico, 6 LEDs

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Configure 6 LEDs on GP10-15.

**B. Main Loop Phase**
2.  **Get Time**:
    *   From **Time**, drag `pico_ms_ticks`.
3.  **Convert**:
    *   From **Variables**, calculate bit values for current second.
4.  **Wait**: 1 second.

### 10. Generated Code
```python
import time, machine
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 16)]
while True:
    s = time.localtime()[5]
    for i in range(6):
        leds[i].value((s >> i) & 1)
    time.sleep(1)
```

---

## 1. Project 0525: Interactive Binary

### 2. Learning Objective
Binary Adder - User sets two 2-bit numbers with buttons, display sum on LEDs.

### 4. Hardware Required
Pico, 4 Buttons, 3 LEDs

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Buttons on GP14,15,16,17. LEDs on GP10,11,12.

**B. Main Loop Phase**
2.  **Sum**:
    *   From **Math**, `num1` = (b0 + b1*2). `num2` = (b2 + b3*2).
3.  **Output**:
    *   From **Smart IO**, write `num1 + num2` in binary to LEDs.

### 10. Generated Code
```python
import machine
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(14, 18)]
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 13)]
while True:
    n1 = btns[0].value() + (btns[1].value() << 1)
    n2 = btns[2].value() + (btns[3].value() << 1)
    res = n1 + n2
    for i in range(3):
        leds[i].value((res >> i) & 1)
```

---
"""

if __name__ == "__main__":
    append_high_quality(batch_53_cont)
    print("Projects 0523-0525 Appended.")
