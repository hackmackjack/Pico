# 🏁 Batch 7: Actuators & Motion (061-070)
*Focus: Creating movement with Servos, DC Motors, and Relays.*

---

## 1️⃣ Project 061: Standard Servo Control
### 2️⃣ Learning Objective
Control a servo motor specifically to specific angles.

### 3️⃣ Concepts Introduced
*   PWM
*   Duty Cycle
*   Mechanical Movement

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0
*   VCC -> 5V/3.3V
*   GND -> GND

### 6️⃣ Blocks Used
🔹 **Servo Pin**
*   **Category:** Standard
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Standard
*   **Block:** `Wait [1] [seconds]`

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Loop:
    * Move Servo to 0.
    * Wait.
    * Move Servo to 90.
    * Wait.

### 9️⃣ Execution Flow (Plain English)
The program runs in a continuous loop.

### 🔟 Generated Code (Reference Only)
```python
import time

# Initialize Hardware (Reference)
servo = PWM(Pin(0)); servo.freq(50)

# Main Logic (See Block Logic)
while True:
    # Logic from Section 8
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mistake:** Connecting the Servo Red wire to 3.3V.
    *   **Result:** The servo might twitch but won't move fully because it needs 5V (VBUS).
*   **Mistake:** Using `set Pin 0 to HIGH`. Servos need complex PWM, not just High/Low.

### 1️⃣2️⃣ Try This Next
*   Try angles like 45° or 135° to point diagonally.

---


## 1️⃣ Project 062: Sweep Motion
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Sweep Motion.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 063: Knob Control
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Knob Control.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 064: Dual Arm
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Dual Arm.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 065: Gripper Logic
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Gripper Logic.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 066: Slow Motion
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Slow Motion.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 067: Sequence Playback
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Sequence Playback.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 068: Torque Test
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Torque Test.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 069: Interactive Arm
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Interactive Arm.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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


## 1️⃣ Project 070: Safety Limits
### 2️⃣ Learning Objective
Explore advanced concepts in Servo using Safety Limits.

### 3️⃣ Concepts Introduced
*   Servo Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5️⃣ Wiring / Interfaces
*   Signal -> GP0

### 6️⃣ Blocks Used
🔹 **Servo**
*   **Category:** Servo
*   **Block:** `Servo Pin [0] Angle [90]`
🔹 **Wait**
*   **Category:** Servo
*   **Block:** `Wait [1]s`

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

