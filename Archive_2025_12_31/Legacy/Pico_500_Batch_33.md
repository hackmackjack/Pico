# 🏁 Batch 33: Advanced Displays IV (321-330)
*Focus: 7-Segment displays, Dot Matrices, E-Paper, and TFT screens.*

---

## 1️⃣ Project 321: 7-Segment Counter
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
*   **Mistake:** Using 5V logic on 3.3V pins. (Most TM1637 modules work fine on 3.3V VCC).

### 1️⃣2️⃣ Try This Next
*   Make it count down from 10 to 0 (Launch sequence).

---


## 1️⃣ Project 322: Drawing Shapes
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Drawing Shapes.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 323: Animation Demo
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Animation Demo.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 324: Invert Colors
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Invert Colors.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 325: Scrolling Text
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Scrolling Text.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 326: Progress Bar
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Progress Bar.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 327: Bitmap Icon
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Bitmap Icon.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 328: Simple Menu
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Simple Menu.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 329: Screen Saver
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Screen Saver.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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


## 1️⃣ Project 330: Data Dashboard
### 2️⃣ Learning Objective
Explore advanced concepts in OLED using Data Dashboard.

### 3️⃣ Concepts Introduced
*   OLED Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display

### 5️⃣ Wiring / Interfaces
*   SDA -> GP0
*   SCL -> GP1

### 6️⃣ Blocks Used
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Show`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Draw Rect`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Print`
🔹 **OLED**
*   **Category:** OLED
*   **Block:** `OLED Clear`

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

