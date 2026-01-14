import os
import re

def expand_batch54():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Data for Batch 54 expansion (Temperature Alarm 3)
    
    p0531 = """
## 1. Project 0531: Introduction to Temperature Alarm

### 2. Learning Objective
Programm a "Celsius-to-Fahrenheit" converter that displays the adjusted temperature on the terminal, preparing the system for threshold alerting.

### 3. Concepts Introduced
*   Analog Temperature Sensing (ADC4)
*   Mathematical Formula Application
*   String Formatting for Output
*   Data Precision (Rounding)

### 4. Hardware Required
*   Raspberry Pi Pico
*   (Uses Internal Sensor)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Internal Sensor** | ADC 4 | Internal Die Temp |

### 6. Blocks Used
*   **from Sensors, drag `pico_internal_temp`**
*   **from Math, drag `arithmetic`** ( (C * 1.8) + 32 )
*   **from Text, drag `print`**

### 7. Variables
*   **temp_c**: Float (Celsius)
*   **temp_f**: Float (Fahrenheit)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Hardware Prep**:
    *   No external pins required.
    *   **Snap** `start` block.

**B. Main Loop Phase**
1.  **Iterate Sampling**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below start.
2.  **Read Signal**:
    *   From **Variables**, set `temp_c` to **Sensors** `pico_internal_temp`.
    *   **Snap** into loop.
3.  **Perform Conversion**:
    *   From **Variables**, set `temp_f` to (**Math** `arithmetic` (`temp_c` * 1.8) + 32).
4.  **Report Data**:
    *   From **Text**, drag `print`.
    *   **Snap** below conversion.
    *   Show "Temp F: [temp_f]".
5.  **Wait**:
    *   From **Time**, drag `pico_wait` (1.0s).

### 9. Execution Flow
1.  **Start**: Pico reads the raw voltage from the internal ADC channel 4.
2.  **Process**: The system converts the voltage to Celsius using the standard formula.
3.  **Math**: The Celsius value is multiplied by 1.8 and increased by 32 to find Fahrenheit.
4.  **Output**: The user sees the warm-blooded temperature on their screen.

### 10. Generated Code
```python
import machine, time
adc = machine.ADC(4)
while True:
    v = adc.read_u16() * (3.3/65535)
    c = 27 - (v - 0.706)/0.001721
    f = (c * 1.8) + 32
    print(f"C: {c:.2f} | F: {f:.2f}")
    time.sleep(1)
```

### 11. Common Mistakes
*   **Operator Order**: Forgiving to put brackets around the multiplication, though math rules usually handle it, clarity is safer.

### 12. Try This Next
*   **Kelvin**: Add a calculation for Celsius + 273.15.
"""

    p0532 = """
---

## 2. Project 0532: Blinking Temperature Alarm

### 2. Learning Objective
Create a low-temperature "Freeze Warning" system that triggers a fast-blinking Blue LED when the temperature drops to or below 0C.

### 3. Concepts Introduced
*   Threshold Detection (<= 0)
*   Conditional Alarm Logic
*   Visual Warning Signals
*   Environment Monitoring

### 4. Hardware Required
*   Raspberry Pi Pico
*   Blue LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Blue LED** | GP16 | Freeze Warning |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Sensors, drag `pico_internal_temp`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **t**: Float (Celsius)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, set GP16 as Output.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Check Condition**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Variables**, set `t` to **Sensors** `pico_internal_temp`.
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `t` <= 0.
2.  **Alert (True Branch)**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16).
    *   **Snap** into "do". Set to HIGH.
    *   Wait 0.1s.
    *   Set LOW. Wait 0.1s.
3.  **Safe (Else Branch)**:
    *   From **Smart IO**, drag `pico_gpio_write` (GP16).
    *   **Snap** into "else". Set to LOW.

### 9. Execution Flow
1.  **Start**: System begins reading temperature.
2.  **Process**: If temperature is above freezing, the Blue LED stays dark.
3.  **Process**: As soon as zero is touched, the "True" branch activates.
4.  **Output**: The LED flashes 5 times per second.

### 10. Generated Code
```python
import machine, time
led = machine.Pin(16, machine.Pin.OUT)
adc = machine.ADC(4)
while True:
    v = adc.read_u16() * (3.3/65535)
    c = 27 - (v - 0.706)/0.001721
    if c <= 0:
        led.on(); time.sleep(0.1); led.off(); time.sleep(0.1)
    else:
        led.off(); time.sleep(1)
```

### 11. Common Mistakes
*   **No Else**: If you don't turn the LED off in the 'else', it will stay permanently on once it freezes once.

### 12. Try This Next
*   **Summer Alarm**: Change logic to flash Red if temp exceeds 35C.
"""

    # Replacement logic...
    content = re.sub(r'## 1\. Project 0531:.*?---', p0531 + "\n---", content, flags=re.DOTALL)
    content = re.sub(r'## 2\. Project 0532:.*?---', p0532 + "\n---", content, flags=re.DOTALL)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    expand_batch54()
