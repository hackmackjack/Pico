# 🏁 Batch 36: Advanced Industrial II (351-360)
*Focus: SCADA, HMI, and Complex Control Systems.*

---

## 1️⃣ Project 351: SCADA Serial Dashboard
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
i2c = I2C(0, sda=Pin(0), scl=Pin(1)); oled = SSD1306_I2C(128, 64, i2c)

# Main Logic (See Block Logic)
while True:
    # Logic from Section 8
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mistake:** Using debug text ("The Speed is 50").
    *   **Fix:** Computers hate English. Use structured data ("DATA,50,RUN").

### 1️⃣2️⃣ Try This Next
*   Use a Python script on your PC to plot the graph live.

---


## 1️⃣ Project 352: Toggle Logic
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


## 1️⃣ Project 353: Counter Loop
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


## 1️⃣ Project 354: Random Decision
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


## 1️⃣ Project 355: State Machine
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


## 1️⃣ Project 356: Debounce Button
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


## 1️⃣ Project 357: Sequence Timer
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


## 1️⃣ Project 358: Password Check
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


## 1️⃣ Project 359: Reaction Game
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


## 1️⃣ Project 360: Morse Code
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

