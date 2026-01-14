# 🏁 Batch 11: Smart Sensors & Advanced Logic (101-110)
*Focus: Combining sensors with logic (Hysteresis, State Machines) for smarter systems.*

---

## 1️⃣ Project 101: Smart Smoke Detector
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

# Main Logic (See Block Logic)
while True:
    # Logic from Section 8
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mistake:** Using the `read Digital` pin on the MQ-2.
    *   **Fix:** Use the Analog pin (A0) for precise threshold control. Digital is a fixed hardware threshold.

### 1️⃣2️⃣ Try This Next
*   Add a Red LED that flashes while the alarm is active.

---


## 1️⃣ Project 102: Data Logger
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


## 1️⃣ Project 103: Threshold Alarm
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


## 1️⃣ Project 104: Min/Max Recorder
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


## 1️⃣ Project 105: Calibration Tool
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


## 1️⃣ Project 106: Average Reading
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


## 1️⃣ Project 107: Noise Filter
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


## 1️⃣ Project 108: Graph Plotter
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


## 1️⃣ Project 109: Night Mode Trigger
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


## 1️⃣ Project 110: Security Tripwire
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

