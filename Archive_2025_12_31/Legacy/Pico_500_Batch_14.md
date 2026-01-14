# 🏁 Batch 14: Basic Robotics I (131-140)
*Focus: DC Motor control, Differential Drive Kinematics, and Line Following.*

---

## 1️⃣ Project 131: Single DC Motor Control
### 2️⃣ Learning Objective
Drive a DC motor using a driver module.

### 3️⃣ Concepts Introduced
*   H-Bridge
*   Motor Driver
*   High Current

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor + Driver (L9110/L298)

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC Motor ... Speed**
*   **Category:** Standard
*   **Block:** `DC Motor ... Speed [100]%`
🔹 **Set Pin**
*   **Category:** Standard
*   **Block:** `Set Pin [14] to [HIGH]`

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
*   **Mistake:** Connecting multiple GNDs?
    *   **Fix:** YES. You MUST connect the Battery Negative to the Pico GND key. This is the "Common Ground" reference.

### 1️⃣2️⃣ Try This Next
*   Try "Reverse" by swapping Logic (14 LOW, 15 HIGH).

---


## 1️⃣ Project 132: Speed Control
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Speed Control.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 133: Direction Logic
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Direction Logic.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 134: Soft Start
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Soft Start.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 135: Emergency Stop
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Emergency Stop.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 136: Ramp Up/Down
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Ramp Up/Down.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 137: H-Bridge Safety
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using H-Bridge Safety.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 138: Dual Motor Drive
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Dual Motor Drive.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 139: Tank Turn
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Tank Turn.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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


## 1️⃣ Project 140: Fan Controller
### 2️⃣ Learning Objective
Explore advanced concepts in Motor using Fan Controller.

### 3️⃣ Concepts Introduced
*   Motor Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   L9110 Driver

### 5️⃣ Wiring / Interfaces
*   IA -> GP14
*   IB -> GP15

### 6️⃣ Blocks Used
🔹 **DC**
*   **Category:** Motor
*   **Block:** `DC Motor Speed [50]%`
🔹 **Set**
*   **Category:** Motor
*   **Block:** `Set Pin [14] HIGH`

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

