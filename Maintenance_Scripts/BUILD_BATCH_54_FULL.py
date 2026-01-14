import os
import re

def build_batch54_full():
    content = """
#  Batch 54: Temperature Alarm 3

## 1. Project 0531: Introduction to Temperature Alarm

### 2. Learning Objective
Read the internal temperature sensor (ADC4), convert the voltage to Celsius and Fahrenheit, and display it.

### 3. Concepts Introduced
*   Analog Sensing
*   Transducer Conversion Formulas
*   String Formatting
*   Internal Peripherals

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Read**: `raw = adc_read(4)`.
2.  **Calc**: 
    *   `volts = raw * 3.3 / 65535`.
    *   `cel = 27 - (volts - 0.706) / 0.001721`.
    *   `fahr = (cel * 1.8) + 32`.
3.  **Display**: Print `cel` and `fahr`.

### 10. Generated Code
```python
import machine, time
adc = machine.ADC(4)
while True:
    v = adc.read_u16() * 3.3 / 65535
    t = 27 - (v - 0.706) / 0.001721
    print(t)
    time.sleep(1)
```

---

## 2. Project 0532: Blinking Temperature Alarm

### 2. Learning Objective
"Freeze Alarm". Blink Blue LED if Temp <= 0C.

### 3. Concepts Introduced
*   Threshold Monitoring
*   Visual Alerting
*   Conditional Logic

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Check**:
    *   If `temp <= 0`:
        *   Blink Blue (0.1s On, 0.1s Off).
    *   Else:
        *   Blue Off.

---

## 3. Project 0533: Manual Temperature Alarm Control

### 2. Learning Objective
Adjust the "Set Point" using a button. If Temp > Set Point, Alarm.

### 3. Concepts Introduced
*   Variable Set Points
*   User Input Adjustment
*   Comparator Logic

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Input**: If Btn press -> `limit += 1`.
2.  **Check**: If `temp > limit`: Alarm.

---

## 4. Project 0534: Temperature Alarm Sequences

### 2. Learning Objective
Track Min and Max temperature over time.

### 3. Concepts Introduced
*   Extremum Tracking
*   State Persistence
*   Data Logging concepts

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Compare**:
    *   If `t < min_t`: `min_t = t`.
    *   If `t > max_t`: `max_t = t`.
2.  **Report**: Print Current, Min, Max.

---

## 5. Project 0535: Interactive Temperature Alarm

### 2. Learning Objective
"Comfort Zone". Green if 20 < T < 25. Red otherwise.

### 3. Concepts Introduced
*   Window Comparators
*   Range Logic (AND conditions)
*   Status Indication

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Logic**:
    *   If `t > 20` AND `t < 25`: Green ON, Red OFF.
    *   Else: Green OFF, Red ON.

---

## 6. Project 0536: Smart Temperature Alarm Switch

### 2. Learning Objective
"Schmitt Trigger" (Hysteresis). Fan ON at 30, OFF at 28.

### 3. Concepts Introduced
*   Hysteresis
*   Debouncing Analog Signals
*   State Stability

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Upper**: If `t > 30` -> Fan ON.
2.  **Lower**: If `t < 28` -> Fan OFF.
3.  **Middle**: Do nothing (Maintain state).

---

## 7. Project 0537: Temperature Alarm Alarm System

### 2. Learning Objective
"Rate of Rise" Heat Detector. Alarm if temp rises > 2 degrees in 1 second.

### 3. Concepts Introduced
*   ToC (Rate of Change)
*   Derivative Logic
*   Fire Safety Algorithms

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Calc**: `delta = current_t - last_t`.
2.  **Check**: If `delta > 2.0`: Alarm!
3.  **Update**: `last_t = current_t`.

---

## 8. Project 0538: The Temperature Alarm Game

### 2. Learning Objective
"Human Heat". Player must raise sensor temp to 30C using body heat as fast as possible.

### 3. Concepts Introduced
*   Physics Interaction
*   Stopwatch Integration
*   Target-based Games

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Wait**: Until `t > 30`.
2.  **Stop**: Capture End Time. Print "Duration: X sec".

---

## 9. Project 0539: Automated Temperature Alarm

### 2. Learning Objective
Implement a "Moving Average Filter" to smooth out noisy readings.

### 3. Concepts Introduced
*   Signal Processing
*   Arrays/Buffers
*   Noise Reduction

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Sample**: Read new `t`.
2.  **Buffer**: Add to List (Max 10 items). Rem oldest.
3.  **Calc**: `avg = sum(list) / len(list)`.

---

## 10. Project 0540: Mastering Temperature Alarm

### 2. Learning Objective
Proportional Control (P-Controller). Fan Speed increases as Temp exceeds target.

### 3. Concepts Introduced
*   PWM Speed Control
*   Linear Feedback
*   Error Calculation

### 8. Step-by-Step Guide
**B. Main Loop Phase**
1.  **Error**: `err = t - target`.
2.  **Output**: `duty = err * Kp` (e.g. 5000 per degree).
3.  **Drive**: `fan.duty_u16(duty)`.
"""

    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(target_file, 'r', encoding='utf-8') as f:
        existing = f.read()

    pattern = re.compile(r'#\s*Batch 54: Temperature Alarm 3.*?(?=#\s*Batch 55)', re.DOTALL)
    
    if pattern.search(existing):
        new_content = pattern.sub(content, existing)
    else:
        new_content = existing.replace("#  Batch 54: Temperature Alarm 3", content)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    build_batch54_full()
