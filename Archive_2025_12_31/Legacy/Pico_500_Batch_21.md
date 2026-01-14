# 🏁 Batch 21: IoT Fundamentals & Cloud Data (201-210)
*Focus: Connecting to the Internet, fetching time/data, and sending sensor readings to the cloud.*

---

## 1️⃣ Project 201: Wi-Fi Scanner
### 2️⃣ Learning Objective
Learn to use this feature with the Pico.

### 3️⃣ Concepts Introduced
*   Basic Electronics
*   Programming Logic

### 4️⃣ Hardware Required
*   Raspberry Pi Pico

### 5️⃣ Wiring / Interfaces
*   Standard Setup

### 6️⃣ Blocks Used

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Run Loop.
2. Do action.
3. Wait.

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
*   **Mistake:** Expecting to see 5GHz networks (Pico W is 2.4GHz only).

### 1️⃣2️⃣ Try This Next
*   Filter the list to show only "Open" (No Password) networks.

---


## 1️⃣ Project 202: Data Logger
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


## 1️⃣ Project 203: Threshold Alarm
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


## 1️⃣ Project 204: Min/Max Recorder
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


## 1️⃣ Project 205: Calibration Tool
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


## 1️⃣ Project 206: Average Reading
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


## 1️⃣ Project 207: Noise Filter
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


## 1️⃣ Project 208: Graph Plotter
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


## 1️⃣ Project 209: Night Mode Trigger
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


## 1️⃣ Project 210: Security Tripwire
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

