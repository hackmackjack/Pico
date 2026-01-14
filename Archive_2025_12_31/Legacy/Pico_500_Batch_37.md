# 🏁 Batch 37: Smart City III (361-370)
*Focus: Urban infrastructure, Traffic management, and Environmental monitoring.*

---

## 1️⃣ Project 361: Adaptive Traffic Light
### 2️⃣ Learning Objective
Control Digital Outputs to switch lights.

### 3️⃣ Concepts Introduced
*   GPIO
*   Voltage Levels

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   LED (330ohm Resistor)

### 5️⃣ Wiring / Interfaces
*   Positive -> GP15
*   Negative -> GND

### 6️⃣ Blocks Used
🔹 **set Pin**
*   **Category:** Standard
*   **Block:** `set Pin [15] to [HIGH]`
🔹 **wait**
*   **Category:** Standard
*   **Block:** `wait [1] [seconds]`

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Loop:
    * Turn On.
    * Wait.
    * Turn Off.
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
*   **Mistake:** Counting one stationary car as multiple cars.
    *   **Fix:** Wait for the beam to CLEAR before counting again.

### 1️⃣2️⃣ Try This Next
*   Network two Picos to coordinate an intersection.

---


## 1️⃣ Project 362: Toggle Logic
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Toggle Logic.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 363: Counter Loop
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Counter Loop.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 364: Random Decision
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Random Decision.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 365: State Machine
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using State Machine.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 366: Debounce Button
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Debounce Button.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 367: Sequence Timer
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Sequence Timer.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 368: Password Check
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Password Check.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 369: Reaction Game
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Reaction Game.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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


## 1️⃣ Project 370: Morse Code
### 2️⃣ Learning Objective
Explore advanced concepts in Logic using Morse Code.

### 3️⃣ Concepts Introduced
*   Logic Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Button
*   LED

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `If/Else`
🔹 **Wait**
*   **Category:** Logic
*   **Block:** `Wait`
🔹 **Variable**
*   **Category:** Logic
*   **Block:** `Variable`

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

