# 🏁 Batch 2: Analog & Sensors (011-020)
*Focus: Reading Sensors (ADC), Controlling Brightness (PWM), and Sound.*

---

## 1️⃣ Project 011: Potentiometer Reading
### 2️⃣ Learning Objective
Read real-world data from a sensor.

### 3️⃣ Concepts Introduced
*   Analog vs Digital
*   Sampling

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Generic Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26 (Analog) or GP14 (Digital)

### 6️⃣ Blocks Used
🔹 **read**
*   **Category:** Standard
*   **Block:** `read [Analog] Pin [26]`

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Loop:
    * Read Sensor Value.
    * Log Value.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The program runs in a continuous loop.

### 🔟 Generated Code (Reference Only)
```python
import time

# Initialize Hardware (Reference)
i2c = I2C(0, sda=Pin(0), scl=Pin(1)); oled = SSD1306_I2C(128, 64, i2c)

# Main Logic (See Block Logic)
while True:
    # Logic from Section 8
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mistake:** Connecting the wiper (middle leg) to 3.3V or GND.
    *   **Result:** Short circuit or constant value. The middle leg MUST go to GP26.
*   **Mistake:** Using a Digital Read.
    *   **Result:** You only see 0 or 1, no smooth change.

### 1️⃣2️⃣ Try This Next
*   Try Pin 27 or 28 (ADC1 and ADC2).
*   Wrap the knob with tape and mark 0, 50%, 100%.

---


## 1️⃣ Project 012: Data Logger
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Data Logger.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 013: Threshold Alarm
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Threshold Alarm.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 014: Min/Max Recorder
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Min/Max Recorder.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 015: Calibration Tool
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Calibration Tool.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 016: Average Reading
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Average Reading.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 017: Noise Filter
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Noise Filter.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 018: Graph Plotter
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Graph Plotter.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 019: Night Mode Trigger
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Night Mode Trigger.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---


## 1️⃣ Project 020: Security Tripwire
### 2️⃣ Learning Objective
Explore advanced concepts in Sensor using Security Tripwire.

### 3️⃣ Concepts Introduced
*   Sensor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Analog/Digital Sensor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP26

### 6️⃣ Blocks Used
🔹 **Read**
*   **Category:** Sensor
*   **Block:** `Read Analog Pin [26]`
🔹 **Log**
*   **Category:** Sensor
*   **Block:** `Log Data`

### 7️⃣ Variables & State
*   **state:** Holds the current status.

### 8️⃣ Block Logic
1. Initialize System.
2. Loop:
    * Check Conditions.
    * Update Output.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The system continuously monitors inputs and updates the interface based on the logic defined.

### 🔟 Generated Code (Reference Only)
```python
import time
import machine

# Setup
# ...

while True:
    # Logic
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: Ensure external power is connected if needed.

### 1️⃣2️⃣ Try This Next
*   Modify the timing parameters.

---

