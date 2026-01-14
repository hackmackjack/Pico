# 🏁 Batch 28: Smart Display II (271-280)
*Focus: Graphs, Menus, and Interactive UI.*

---

## 1️⃣ Project 271: Rolling Graph
### 2️⃣ Learning Objective
Master the OLED display to show text, graphics, or data.

### 3️⃣ Concepts Introduced
*   I2C Protocol
*   Pixel Coordinates
*   Display Buffers

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1
*   VCC -> 3.3V
*   GND -> GND

### 6️⃣ Blocks Used
🔹 **Init OLED ...**
*   **Category:** Standard
*   **Block:** `Init OLED ...`
🔹 **OLED Show**
*   **Category:** Standard
*   **Block:** `OLED Show`
🔹 **OLED Print**
*   **Category:** Standard
*   **Block:** `OLED Print [Text] ...`
🔹 **OLED Fill (Clear)**
*   **Category:** Standard
*   **Block:** `OLED Fill (Clear)`

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Init OLED (SDA 0, SCL 1).
2. Loop:
    * Clear Screen.
    * Draw Content.
    * Show Screen.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
We draw to the memory buffer first, then send it to the screen with 'Show'.

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
*   **Wiring**: Check your connections.

### 1️⃣2️⃣ Try This Next
*   Experiment with different values.

---


## 1️⃣ Project 272: Toggle Logic
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


## 1️⃣ Project 273: Counter Loop
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


## 1️⃣ Project 274: Random Decision
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


## 1️⃣ Project 275: State Machine
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


## 1️⃣ Project 276: Debounce Button
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


## 1️⃣ Project 277: Sequence Timer
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


## 1️⃣ Project 278: Password Check
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


## 1️⃣ Project 279: Reaction Game
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


## 1️⃣ Project 280: Morse Code
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

