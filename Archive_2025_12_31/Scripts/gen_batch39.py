# Generate Full Elite Documentation for Batch 39 (Projects 0381-0390)

import os

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

batch39_content = r'''
# 🏁 Batch 39: Kitchen Timer 2 & Wi-Fi Web Server 2

---

## 1️⃣ Project 0381: Kitchen Timer 2 - Multi-Stage Timer

### 2️⃣ Learning Objective
Implement a sequential multi-stage timer (e.g., Prep, Cook, Rest) with automatic phase transitions. You will learn about state-machine logic and phase-dependent feedback.

### 3️⃣ Concepts Introduced
*   **State Machine Phases**: Moving through "Ready", "Phase 1", "Phase 2", "Done" states sequentially.
*   **Automatic Transition**: Triggering the next timer phase immediately after the current one finishes.
*   **Phase Indicators**: Using different sounds or text to distinguish between active stages.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display**
*   **Buzzer**
*   **Button** (Start)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |
| **Buzzer** | GP15 | PWM |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Variables** Phase, TimeLeft
🔹 **OLED Text**
🔹 **Buzzer Tone**
🔹 **If/Else If**

### 7️⃣ Variables & State
*   **Phase**: Current stage (0=Prep, 1=Cook, 2=Rest, 3=Done).
*   **TimeLeft**: Seconds remaining in current phase.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup I2C, OLED, and Button.
    *   Initialize `Phase = 0`, `TimeLeft = 10`.

*   **B. Main Loop Phase**
    *   **Phase Management**:
        *   If `Phase = 0` (Prep): Display "PREP", count down. If `TimeLeft = 0`, `Phase = 1`, `TimeLeft = 20`, Beep once.
        *   If `Phase = 1` (Cook): Display "COOK", count down. If `TimeLeft = 0`, `Phase = 2`, `TimeLeft = 5`, Beep twice.
        *   If `Phase = 2` (Rest): Display "REST", count down. If `TimeLeft = 0`, `Phase = 3`.
    *   **Done State**:
        *   If `Phase = 3`: Display "ENJOY!", slow pulse buzzer.
    *   **Update Screen**:
        *   `OLED clear`, `OLED Text (TimeLeft)`, `OLED show`.
        *   `sleep 1s`.

### 9️⃣ Execution Flow (Plain English)
The timer starts in "Prep" mode for 10 seconds. When it hits zero, it automatically switches to "Cook" mode for 20 seconds, and then "Rest" for 5 seconds. Each transition is marked by a unique beep. After all phases finish, the screen says "ENJOY!" and the buzzer alerts the user.

### 🔟 Generated Code (Reference Only)
```python
import machine, time
from ssd1306 import SSD1306_I2C
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
buzzer = machine.PWM(machine.Pin(15))
phase, t = 0, 10
while True:
    oled.fill(0)
    if phase == 0:
        oled.text("PREP", 0, 0)
        if t <= 0: phase, t = 1, 20; buzzer.freq(1000); buzzer.duty_u16(32768); time.sleep(0.5); buzzer.duty_u16(0)
    elif phase == 1:
        oled.text("COOK", 0, 0)
        if t <= 0: phase, t = 2, 5; buzzer.freq(2000); buzzer.duty_u16(32768); time.sleep(0.5); buzzer.duty_u16(0)
    elif phase == 2:
        oled.text("REST", 0, 0)
        if t <= 0: phase = 3
    elif phase == 3:
        oled.text("ENJOY!", 0, 0)
        buzzer.freq(440); buzzer.duty_u16(32768); time.sleep(0.1); buzzer.duty_u16(0)
    
    oled.text(str(t), 0, 20)
    oled.show()
    t -= 1
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Logic Overlap**: Ensure you use `if/elif` so that the code doesn't skip from Phase 0 to Phase 1 and immediately check Phase 1's timer in the same loop iteration.

### 1️⃣2️⃣ Try This Next
*   **Custom Times**: Use a potentiometer to set the duration of the "Cook" phase before starting.

---

## 1️⃣ Project 0382: Kitchen Timer 2 - Progress Bar

### 2️⃣ Learning Objective
Create a visual progress bar on the OLED to represent time remaining proportionally. You will learn about math-to-graphics mapping and dynamic UI updates.

### 3️⃣ Concepts Introduced
*   **Visual Ratio**: Mapping a decreasing time value to an increasing geometry (rectangle width).
*   **Dynamic UI**: Redrawing elements every frame to represent changing data.

### 8️⃣ Step-by-Step Guide
*   **A. Initialization**: Set `totalTime = 30`, `currentTime = 30`.
*   **B. Main Loop**: 
    1. `width = (currentTime / totalTime) * 120`.
    2. `OLED Draw Rect (x:4, y:30, w:width, h:10, fill=True)`.
    3. `currentTime -= 1`, `sleep 1s`.

### 9️⃣ Execution Flow (Plain English)
As the seconds tick down, a solid bar on the screen gets shorter and shorter from right to left, providing a quick visual estimate of how much cooking time is left without reading the numbers.

---

## 1️⃣ Project 0383: Kitchen Timer 2 - Rotary Adjustment

### 2️⃣ Learning Objective
Use a rotary encoder or potentiometer to adjust timer duration in "Set Mode" before starting. You will learn about input mapping and confirmation logic.

### 3️⃣ Concepts Introduced
*   **Set vs. Run Modes**: Toggling behavior between configuration and execution.
*   **Analog Parameter Mapping**: Turning a knob to increase/decrease a variable.

### 8️⃣ Step-by-Step Guide
*   **Setup**: Set `mode = "SET"`.
*   **Loop**:
    *   If `mode == "SET"`: Read Pot, map to 0-3600 seconds. Show on OLED. If Button Pressed -> `mode = "RUN"`.
    *   If `mode == "RUN"`: Count down. If 0 -> Beep and `mode = "SET"`.

---

## 1️⃣ Project 0384: Kitchen Timer 2 - Quick Presets

### 2️⃣ Learning Objective
Implement button-based "Macro" presets (1 min, 5 min, 10 min). You will learn about direct variable assignment from multiple inputs.

### 3️⃣ Concepts Introduced
*   **Shortcuts/Presets**: Preset values assigned to specific hardware buttons.
*   **Input Debouncing**: Ensuring 1 press = 1 preset selection.

### 5️⃣ Wiring / Interfaces
*   **Btn 1**: 1 Min
*   **Btn 2**: 5 Min
*   **Btn 3**: Reset/Start

---

## 1️⃣ Project 0385: Kitchen Timer 2 - Overtime Tracking

### 2️⃣ Learning Objective
Track "Negative Time" after the timer reach zero to show how long ago it finished. You will learn about dual-direction counting.

### 3️⃣ Concepts Introduced
*   **Zero-Crossing Logic**: Switching from counting down to counting up.
*   **Alert Escalation**: Increasing beep frequency as "Overtime" grows.

### 8️⃣ Step-by-Step Guide
*   `currentTime -= 1`.
*   If `currentTime <= 0`:
    *   `print OVERTIME: {abs(currentTime)}`.
    *   Invert OLED colors (Flash Alert).

---

## 1️⃣ Project 0386: Wi-Fi Web Server 2 - Remote Control Timer

### 2️⃣ Learning Objective
Host a web server on the Pico that allows users to start/stop the kitchen timer from a mobile browser. You will learn about HTTP request parsing and networking-to-logic mapping.

### 3️⃣ Concepts Introduced
*   **HTTP GET Handling**: Extracting commands from browser URLs (e.g., `/start`).
*   **Headless Control**: Interacting with hardware via a web interface instead of physical buttons.

### 5️⃣ Wiring / Interfaces
*   **Wi-Fi**: Standard Pico W AP or Station setup.

### 8️⃣ Step-by-Step Guide
*   Connect to Wi-Fi.
*   Start Socket Server on Port 80.
*   Wait for client.
*   If request contains `GET /start`: `set timerRunning = True`.
*   If request contains `GET /stop`: `set timerRunning = False`.

### 🔟 Generated Code (Reference Only)
```python
import network, socket, machine
# Setup Wi-Fi...
s = socket.socket()
s.bind(('', 80))
s.listen(1)
while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    if '/start' in request: timer_active = True
    conn.send('HTTP/1.1 200 OK\n\nTimer Started')
    conn.close()
```

---

## 1️⃣ Project 0387: Wi-Fi Web Server 2 - Live Telemetry

### 2️⃣ Learning Objective
Serve a real-time updating web page showing current sensor data (Temperature/Timer). You will learn about dynamic HTML generation.

### 3️⃣ Concepts Introduced
*   **Dynamic HTML**: Embedding Python variables into a string of HTML code before sending.
*   **Auto-Refresh**: Adding `<meta http-equiv="refresh" content="5">` to the HTML to update the browser view automatically.

---

## 1️⃣ Project 0388: Wi-Fi Web Server 2 - Multi-Button Dashboard

### 2️⃣ Learning Objective
Create a sophisticated web dashboard with multiple buttons to control various Pico outputs. You will learn about UI layout and complex request routing.

### 3️⃣ Concepts Introduced
*   **Web Dashboard**: A central interface for multiple controls.
*   **Request Routing**: Directing `/led/on`, `/buzzer/off`, etc., to specific GPIO functions.

---

## 1️⃣ Project 0389: Wi-Fi Web Server 2 - Password Protection

### 2️⃣ Learning Objective
Secure your web server using a simple authentication check in the request header. You will learn about networking security basics.

### 3️⃣ Concepts Introduced
*   **URL authentication**: Checking for a secret key in the request (e.g., `/control?key=1234`).
*   **Access Rejection**: Sending 403 Forbidden if the key is missing.

---

## 1️⃣ Project 0390: Mastering Web Server

### 2️⃣ Learning Objective
Handle multiple simultaneous web requests and serve static assets (small images/styles). You will learn about socket management and file serving.

### 3️⃣ Concepts Introduced
*   **Non-Blocking Sockets**: Handling connections without stalling the rest of the code.
*   **File Serving**: Reading a `.html` file from the Pico's storage and sending it to the browser.
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch39_content)

print("✅ Successfully appended Batch 39 (0381-0390) to Docs_0301_0400.md")
