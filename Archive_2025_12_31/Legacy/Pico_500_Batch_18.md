# 🏁 Batch 18: Wireless Control II (171-180)
*Focus: Pico-to-Pico Radio (NRF24/RFM) and WiFi Web Server Basics.*

---

## 1️⃣ Project 171: Radio Chat (Sender)
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
*   **Wiring**: Check your connections.

### 1️⃣2️⃣ Try This Next
*   Experiment with different values.

---


## 1️⃣ Project 172: WiFi Scan
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using WiFi Scan.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 173: Connect to AP
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Connect to AP.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 174: HTTP Get
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using HTTP Get.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 175: Web Server
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Web Server.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 176: Remote Switch
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Remote Switch.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 177: Cloud Data Push
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Cloud Data Push.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 178: Time Sync (NTP)
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Time Sync (NTP).

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 179: Weather Fetcher
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Weather Fetcher.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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


## 1️⃣ Project 180: Mobile Control
### 2️⃣ Learning Objective
Explore advanced concepts in IoT using Mobile Control.

### 3️⃣ Concepts Introduced
*   IoT Control
*   Automation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Raspberry Pi Pico W

### 5️⃣ Wiring / Interfaces
*   Internal WiFi

### 6️⃣ Blocks Used
🔹 **Connect**
*   **Category:** IoT
*   **Block:** `Connect WiFi`
🔹 **HTTP**
*   **Category:** IoT
*   **Block:** `HTTP Request`

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

