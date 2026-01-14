# 🏁 Batch 34: Advanced Interfaces (331-340)
*Focus: Touch screens, Persistence of Vision (POV), Lasers, and Gestures.*

---

## 1️⃣ Project 331: Touch Screen Button
### 2️⃣ Learning Objective
React to user input via a pushbutton.

### 3️⃣ Concepts Introduced
*   Digital Input
*   Pull-up/Pull-down

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display
*   Pushbutton

### 5️⃣ Wiring / Interfaces
*   Pin 1 -> GP14
*   Pin 2 -> GND

### 6️⃣ Blocks Used
🔹 **Button (Debounced) Pin**
*   **Category:** Standard
*   **Block:** `Button (Debounced) Pin [14]`
🔹 **If / Else**
*   **Category:** Standard
*   **Block:** `If / Else`

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Loop:
    * If Button Pressed:
        * Do Action.
    * Else:
        * Stop.

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
*   **Mistake:** Touch coordinates are mirrored.
    *   **Fix:** Adjust the `Calibration` block logic (e.g., `width - x`).

### 1️⃣2️⃣ Try This Next
*   Make a "Toggle" button (Click On, Click Off).

---


## 1️⃣ Project 332: Drawing Shapes
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


## 1️⃣ Project 333: Animation Demo
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


## 1️⃣ Project 334: Invert Colors
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


## 1️⃣ Project 335: Scrolling Text
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


## 1️⃣ Project 336: Progress Bar
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


## 1️⃣ Project 337: Bitmap Icon
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


## 1️⃣ Project 338: Simple Menu
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


## 1️⃣ Project 339: Screen Saver
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


## 1️⃣ Project 340: Data Dashboard
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

