# 🏁 Batch 16: Stepper Motors (151-160)
*Focus: Precision control using Stepper Motors (28BYJ-48).*

---

## 1️⃣ Project 151: Stepper Hello World
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
*   **Mistake:** Wiring order incorrect (e.g., swapping IN2 and IN3).
    *   **Result:** Motor vibrates but doesn't spin.
*   **Mistake:** Powering from 3.3V. It might work weakly, but 5V is recommended.

### 1️⃣2️⃣ Try This Next
*   Make it spin 360 degrees (4096 steps).

---


## 1️⃣ Project 152: Speed Control
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


## 1️⃣ Project 153: Direction Logic
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


## 1️⃣ Project 154: Soft Start
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


## 1️⃣ Project 155: Emergency Stop
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


## 1️⃣ Project 156: Ramp Up/Down
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


## 1️⃣ Project 157: H-Bridge Safety
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


## 1️⃣ Project 158: Dual Motor Drive
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


## 1️⃣ Project 159: Tank Turn
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


## 1️⃣ Project 160: Fan Controller
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

