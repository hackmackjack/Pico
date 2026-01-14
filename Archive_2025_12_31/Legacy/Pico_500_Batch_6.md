# 🏁 Batch 6: Displays & Visuals (051-060)
*Focus: OLED Displays, Text, Graphics, and UI.*

---

## 1️⃣ Project 051: OLED Hello World
### 2️⃣ Learning Objective
Control Digital Outputs to switch lights.

### 3️⃣ Concepts Introduced
*   GPIO
*   Voltage Levels

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display
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
*   **Mistake:** Forgetting `OLED Show`.
    *   **Result:** Screen stays black. Drawing commands only update the internal RAM, not the display.
*   **Mistake:** Wiring SDA/SCL backwards.

### 1️⃣2️⃣ Try This Next
*   Change coordinates to `x 20 y 30` to center the text.

---


## 1️⃣ Project 052: Drawing Shapes
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


## 1️⃣ Project 053: Animation Demo
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


## 1️⃣ Project 054: Invert Colors
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


## 1️⃣ Project 055: Scrolling Text
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


## 1️⃣ Project 056: Progress Bar
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


## 1️⃣ Project 057: Bitmap Icon
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


## 1️⃣ Project 058: Simple Menu
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


## 1️⃣ Project 059: Screen Saver
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


## 1️⃣ Project 060: Data Dashboard
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

