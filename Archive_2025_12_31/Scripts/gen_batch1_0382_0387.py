# BATCH 1: Generate Full Elite Documentation for Projects 0382-0387

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

# Read current file
with open(target_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep everything up to end of Project 0381 (line 9991)
output_lines = lines[:9991]

batch1_content = r'''
## 1️⃣ Project 0382: Kitchen Timer 2 - Progress Bar

### 2️⃣ Learning Objective
Create a visual progress bar on the OLED to represent time remaining proportionally. You will learn about math-to-graphics mapping and dynamic UI updates.

### 3️⃣ Concepts Introduced
*   **Visual Ratio**: Mapping a decreasing time value to an increasing geometry (rectangle width).
*   **Dynamic UI**: Redrawing elements every frame to represent changing data.
*   **Proportional Representation**: Using mathematical division to scale visual feedback.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (SSD1306)
*   **Button** (Start/Stop)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 Data |
| **OLED SCL** | GP1 | I2C0 Clock |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **OLED Rectangle**
*   **Category:** Displays

🔹 **Variables**
*   **Category:** Variables

🔹 **Math Division**
*   **Category:** Math

### 7️⃣ Variables & State
*   **totalTime**: Initial timer duration (e.g., 30 seconds).
*   **currentTime**: Remaining seconds.
*   **barWidth**: Calculated pixel width of the progress bar.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [totalTime] to [30]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [currentTime] to [totalTime]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Calculate Bar Width**:
        *   From **Math**, drag `set [barWidth] to [([currentTime] / [totalTime]) * 120]`.
            *   **Snap** into loop.
    *   **Draw Progress**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `draw filled rectangle x:[4] y:[30] w:[barWidth] h:[10] color:[1]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text [Time: {currentTime}s] at x:[0] y:[0]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   **Update Timer**:
        *   From **Variables**, drag `change [currentTime] by [-1]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The timer starts at 30 seconds. Every second, the program calculates what percentage of time is left (currentTime ÷ totalTime). This percentage is multiplied by 120 pixels to determine the width of a rectangle. As time counts down, the bar shrinks from right to left, giving instant visual feedback on remaining time without needing to read numbers.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

total_time = 30
current_time = total_time

while current_time > 0:
    oled.fill(0)
    bar_width = int((current_time / total_time) * 120)
    oled.fill_rect(4, 30, bar_width, 10, 1)
    oled.text(f"Time: {current_time}s", 0, 0)
    oled.show()
    current_time -= 1
    time.sleep(1)

oled.fill(0)
oled.text("DONE!", 40, 25)
oled.show()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Bar Grows Instead of Shrinks**: Ensure you're using `(currentTime / totalTime)` not `(totalTime - currentTime)`.
*   **Integer Division**: Make sure at least one operand is a float to prevent 0-width bars due to integer rounding.

### 1️⃣2️⃣ Try This Next

*   **Color Gradient**: Draw multiple stacked bars with different fill patterns to simulate color gradients.
*   **Dual Progress**: Add a second smaller bar showing "Overtime" if the user doesn't respond when time hits 0.

---

## 1️⃣ Project 0383: Kitchen Timer 2 - Rotary Adjustment

### 2️⃣ Learning Objective
Use a rotary encoder or potentiometer to adjust timer duration in "Set Mode" before starting. You will learn about input mapping, mode switching, and confirmation logic.

### 3️⃣ Concepts Introduced
*   **Set vs. Run Modes**: Toggle behavior between configuration and execution states.
*   **Analog Parameter Mapping**: Converting knob position to time values.
*   **State Confirmation**: Using a button press to lock in a setting.

### 4️⃣ Hardware Required
*   **Pico**
*   **Potentiometer** (Timer Duration Adjust)
*   **Button** (Mode Toggle)
*   **OLED Display**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 | ADC0 |
| **Button** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |

### 6️⃣ Blocks Used

🔹 **Read Analog Pin**
*   **Category:** Pin Access

🔹 **Map Range**
*   **Category:** Math

🔹 **String Blocks**
*   **Category:** Text

🔹 **OLED Text**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **mode**: "SET" or "RUN".
*   **timerDuration**: Configured time (0-3600 seconds).
*   **currentTime**: Countdown variable.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [mode] to ["SET"]`.
        *   **Snap** below.
    
*   **B. Main Loop Phase**
    *   **Configuration Mode**:
        *   From **Logic**, drag `if [mode] = ["SET"] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Math**, drag `map [read analog pin 26] from [0-65535] to [0-3600]`.
                    *   Store in `timerDuration`.
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED text [Set Timer: {timerDuration}s] at x:[0] y:[0]`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Logic**, drag `if [digital read pin 14] then`.
                    *   **Snap** below.
                    *   Inside: From **Variables**, drag `set [mode] to ["RUN"]`.
                        *   **Snap** inside.
                    *   Inside: From **Variables**, drag `set [currentTime] to [timerDuration]`.
                        *   **Snap** below.
    *   **Running Mode**:
        *   From **Logic**, drag `if [mode] = ["RUN"] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `OLED text [Running: {currentTime}s]`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Variables**, drag `change [currentTime] by [-1]`.
                    *   **Snap** below.
                *   From **Logic**, drag `if [currentTime] <= [0] then`.
                    *   **Snap** below.
                    *   Inside: From **Actuators**, drag `Buzzer [15] beep`.
                        *   **Snap** inside.
                    *   Inside: From **Variables**, drag `set [mode] to ["SET"]`.
                        *   **Snap** below.
                *   From **Timing**, drag `sleep [1] seconds`.
                    *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

User turns the pot to set a time between 0-60 minutes (3600 seconds). Screen shows live preview. Pressing button locks the time and starts the countdown. When timer reaches zero, it beeps and returns to SET mode, allowing the user to configure a new duration.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

mode = "SET"
timer_duration = 0
current_time = 0

while True:
    if mode == "SET":
        timer_duration = int(pot.read_u16() * 3600 / 65535)
        oled.fill(0)
        oled.text(f"Set: {timer_duration}s", 0, 0)
        oled.show()
        if btn.value():
            mode = "RUN"
            current_time = timer_duration
            time.sleep(0.5)
    elif mode == "RUN":
        oled.fill(0)
        oled.text(f"Time: {current_time}s", 0, 0)
        oled.show()
        current_time -= 1
        if current_time <= 0:
            # Beep buzzer
            mode = "SET"
        time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Pot Noise**: If the timer value jumps around, add a small averaging filter or deadband (only update if change > 5 seconds).
*   **Mode Stuck**: Ensure button debounce (0.5s sleep after mode switch) prevents accidental double-toggles.

### 1️⃣2️⃣ Try This Next

*   **Preset Markers**: Show visual marks on the OLED at common times (1min, 5min, 10min, 30min).
*   **Digital Encoder**: Replace the pot with a rotary encoder for click-by-click precision.

---

## 1️⃣ Project 0384: Kitchen Timer 2 - Quick Presets

### 2️⃣ Learning Objective
Implement button-based "Macro" presets (1 min, 5 min, 10 min). You will learn about direct variable assignment from multiple inputs and shortcut interfaces.

### 3️⃣ Concepts Introduced
*   **Shortcuts/Presets**: Preset values assigned to specific hardware buttons.
*   **Input Debouncing**: Ensuring 1 press = 1 preset selection.
*   **Quick Access UI**: Reducing configuration steps for common use cases.

### 4️⃣ Hardware Required
*   **Pico**
*   **3× Buttons** (Preset 1, Preset 2, Start)
*   **OLED Display**
*   **Buzzer** (Optional)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button 1 (1 Min)** | GP12 | PULL_DOWN |
| **Button 2 (5 Min)** | GP13 | PULL_DOWN |
| **Button 3 (10 Min)** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Setup Button (×3)**
*   **Category:** Inputs

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **OLED Text**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **timerValue**: Selected preset time (60, 300, or 600 seconds).
*   **isRunning**: Boolean to track if timer is active.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[12] as PULL_DOWN`.
        *   **Snap** into setup block. (Repeat for pins 13, 14).
    *   From **Variables**, drag `set [timerValue] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [isRunning] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Preset Selection**:
        *   From **Logic**, drag `if not [isRunning] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Logic**, drag `if [digital read pin 12] then`.
                    *   **Snap** inside.
                    *   Inside: From **Variables**, drag `set [timerValue] to [60]`.
                        *   **Snap** inside.
                    *   Inside: From **Variables**, drag `set [isRunning] to [True]`.
                        *   **Snap** below.
                *   From **Logic**, drag `if [digital read pin 13] then`.
                    *   **Snap** below.
                    *   Inside: From **Variables**, drag `set [timerValue] to [300]`.
                    *   Inside: From **Variables**, drag `set [isRunning] to [True]`.
                *   From **Logic**, drag `if [digital read pin 14] then`.
                    *   **Snap** below.
                    *   Inside: From **Variables**, drag `set [timerValue] to [600]`.
                    *   Inside: From **Variables**, drag `set [isRunning] to [True]`.
    *   **Countdown Logic**:
        *   From **Logic**, drag `if [isRunning] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `OLED text [Time: {timerValue}s]`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Variables**, drag `change [timerValue] by [-1]`.
                    *   **Snap** below.
                *   From **Logic**, drag `if [timerValue] <= [0] then`.
                    *   **Snap** below.
                    *   Inside: From **Actuators**, drag `Buzzer [15] beep`.
                    *   Inside: From **Variables**, drag `set [isRunning] to [False]`.
                *   From **Timing**, drag `sleep [1] seconds`.
                    *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system idles, waiting for one of three preset buttons. Pressing Button 1 sets the timer to 60 seconds (1 minute) and immediately starts counting down. Button 2 sets 300 seconds (5 minutes), and Button 3 sets 600 seconds (10 minutes). Once a timer starts, it counts down automatically. When it reaches zero, a buzzer sounds and the system returns to idle, ready for another preset selection.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
btn1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn2 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn3 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

timer_value = 0
is_running = False

while True:
    if not is_running:
        oled.fill(0)
        oled.text("Select Preset:", 0, 0)
        oled.text("1: 1 Min", 0, 15)
        oled.text("2: 5 Min", 0, 25)
        oled.text("3: 10 Min", 0, 35)
        oled.show()
        
        if btn1.value():
            timer_value = 60
            is_running = True
            time.sleep(0.5)
        elif btn2.value():
            timer_value = 300
            is_running = True
            time.sleep(0.5)
        elif btn3.value():
            timer_value = 600
            is_running = True
            time.sleep(0.5)
    else:
        oled.fill(0)
        oled.text(f"Time: {timer_value}s", 0, 20)
        oled.show()
        timer_value -= 1
        if timer_value <= 0:
            # Beep buzzer
            is_running = False
        time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Double Trigger**: Without a debounce delay (0.5s sleep), pressing a button might register twice.
*   **Menu Not Updating**: Ensure the "Select Preset" screen is only shown when `isRunning = False`.

### 1️⃣2️⃣ Try This Next

*   **Cancel Button**: Add a 4th button that stops the timer mid-countdown and returns to preset selection.
*   **Custom Presets**: Save the last-used timer values to flash memory so they persist across reboots.

---

## 1️⃣ Project 0385: Kitchen Timer 2 - Overtime Tracking

### 2️⃣ Learning Objective
Track "Negative Time" after the timer reaches zero to show how long ago it finished. You will learn about dual-direction counting and alert escalation.

### 3️⃣ Concepts Introduced
*   **Zero-Crossing Logic**: Switching from counting down to counting up.
*   **Alert Escalation**: Increasing beep frequency as "Overtime" grows.
*   **Absolute Value Display**: Showing |time| even when the value is negative.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Absolute Value**
*   **Category:** Math

🔹 **Variables**
*   **Category:** Variables

🔹 **OLED Invert**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **currentTime**: Timer value (can go negative).
*   **overtimeMode**: Boolean flag when time < 0.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [currentTime] to [10]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [overtimeMode] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Countdown**:
        *   From **Variables**, drag `change [currentTime] by [-1]`.
            *   **Snap** into loop.
    *   **Check Zero-Crossing**:
        *   From **Logic**, drag `if [currentTime] <= [0] AND [overtimeMode] = [False] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [overtimeMode] to [True]`.
                *   **Snap** inside.
    *   **Display Logic**:
        *   From **Logic**, drag `if [overtimeMode] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Displays**, drag `OLED clear`.
                    *   **Snap** inside.
                *   From **Displays**, drag `OLED text [OVERTIME: {abs(currentTime)}s]`.
                    *   **Snap** below.
                *   From **Displays**, drag `OLED invert [True]`.
                    *   **Snap** below (Flash alert).
                *   From **Displays**, drag `OLED show`.
                    *   **Snap** below.
                *   From **Actuators**, drag `Buzzer [15] tone [1000] for [100]ms`.
                    *   **Snap** below.
        *   From **Logic**, drag `else`.
            *   Inside:
                *   Display normal countdown.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The timer counts down normally from 10 seconds. When it hits 0, instead of stopping, it continues counting into negative territory (-1, -2, -3...). The display switches to show "OVERTIME: Xs" where X is the absolute value of the negative time. The screen flashes (inverted colors) and a beep sounds every second to alert the user that they've exceeded the deadline.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
buzzer = machine.PWM(machine.Pin(15))

current_time = 10
overtime_mode = False

while True:
    current_time -= 1
    
    if current_time <= 0 and not overtime_mode:
        overtime_mode = True
    
    oled.fill(0)
    if overtime_mode:
        oled.text(f"OVERTIME: {abs(current_time)}s", 0, 20)
        oled.invert(True)
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(0.1)
        buzzer.duty_u16(0)
    else:
        oled.text(f"Time: {current_time}s", 0, 20)
    
    oled.show()
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Invert Sticks**: If the screen stays inverted, ensure `oled.invert(False)` is called in the `else` block.
*   **Negative Display**: Use `abs(currentTime)` to show positive overtime values.

### 1️⃣2️⃣ Try This Next

*   **Escalating Beeps**: Beep twice per second when overtime > 10s, three times when > 20s.
*   **Auto-Reset**: Reset the timer to 0 if overtime exceeds 60 seconds.

---

## 1️⃣ Project 0386: Wi-Fi Web Server 2 - Remote Control Timer

### 2️⃣ Learning Objective
Host a web server on the Pico that allows users to start/stop the kitchen timer from a mobile browser. You will learn about HTTP request parsing and networking-to-logic mapping.

### 3️⃣ Concepts Introduced
*   **HTTP GET Handling**: Extracting commands from browser URLs (e.g., `/start`).
*   **Headless Control**: Interacting with hardware via a web interface instead of physical buttons.
*   **Socket Programming**: Creating a TCP server that listens for client connections.

### 4️⃣ Hardware Required
*   **Pico W** (Wi-Fi capable)
*   **OLED Display** (Optional, for local feedback)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Wi-Fi** | Built-in | Pico W only |
| **OLED SDA** | GP0 | I2C0 (Optional) |
| **OLED SCL** | GP1 | I2C0 (Optional) |

### 6️⃣ Blocks Used

🔹 **Wi-Fi Connect**
*   **Category:** Networking

🔹 **Socket Server**
*   **Category:** Networking

🔹 **String Contains**
*   **Category:** Text

### 7️⃣ Variables & State
*   **timerRunning**: Boolean flag for timer state.
*   **currentTime**: Active countdown value.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Networking**, drag `Connect to Wi-Fi SSID:[YourNetwork] Password:[YourPass]`.
        *   **Snap** into setup block.
    *   From **Networking**, drag `Create Socket Server on Port:[80]`.
        *   **Snap** below.
    *   From **Console**, drag `print [Server started at {IP_ADDRESS}]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Accept Connection**:
        *   From **Networking**, drag `wait for client connection`.
            *   **Snap** into loop.
        *   From **Networking**, drag `set [request] to [receive 1024 bytes]`.
            *   **Snap** below.
    *   **Parse Command**:
        *   From **Logic**, drag `if [request] contains [/start] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [timerRunning] to [True]`.
                *   **Snap** inside.
            *   Inside: From **Networking**, drag `send [HTTP/1.1 200 OK\n\nTimer Started]`.
                *   **Snap** below.
        *   From **Logic**, drag `if [request] contains [/stop] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [timerRunning] to [False]`.
            *   Inside: From **Networking**, drag `send [HTTP/1.1 200 OK\n\nTimer Stopped]`.
    *   **Close Connection**:
        *   From **Networking**, drag `close client connection`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico W connects to your home Wi-Fi network and starts a web server on port 80. When you navigate to `http://<pico_ip>/start` in a browser, it sends an HTTP GET request. The Pico receives this, detects "/start" in the URL, and sets `timerRunning = True`. Similarly, visiting `/stop` halts the timer. The web interface provides remote control without needing to be physically near the device.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import machine
import time

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('YOUR_SSID', 'YOUR_PASSWORD')

while not wlan.isconnected():
    time.sleep(1)

print(f"Server started at {wlan.ifconfig()[0]}")

# Create socket server
s = socket.socket()
s.bind(('', 80))
s.listen(1)

timer_running = False
current_time = 0

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    if '/start' in request:
        timer_running = True
        current_time = 60
        conn.send('HTTP/1.1 200 OK\n\nTimer Started')
    elif '/stop' in request:
        timer_running = False
        conn.send('HTTP/1.1 200 OK\n\nTimer Stopped')
    else:
        conn.send('HTTP/1.1 200 OK\n\nUse /start or /stop')
    
    conn.close()
    
    # Timer logic runs in parallel (use threading or async for production)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Blocking Accept**: `s.accept()` blocks the entire program. Use non-blocking sockets or threading to allow the timer to count down while waiting for connections.
*   **IP Not Found**: If the Pico doesn't print an IP, check Wi-Fi credentials and router settings.

### 1️⃣2️⃣ Try This Next

*   **HTML Dashboard**: Instead of plain text, send a full HTML page with clickable buttons styled with CSS.
*   **Status Endpoint**: Add `/status` that returns the current timer value in JSON format.

---

## 1️⃣ Project 0387: Wi-Fi Web Server 2 - Live Telemetry

### 2️⃣ Learning Objective
Serve a real-time updating web page showing current sensor data (Temperature/Timer). You will learn about dynamic HTML generation and auto-refresh mechanisms.

### 3️⃣ Concepts Introduced
*   **Dynamic HTML**: Embedding Python variables into a string of HTML code before sending.
*   **Auto-Refresh**: Adding `<meta http-equiv="refresh" content="5">` to the HTML to update the browser view automatically.
*   **Template Strings**: Using f-strings to inject live data into static markup.

### 4️⃣ Hardware Required
*   **Pico W**
*   **DHT22 Sensor** (or any sensor for live data)
*   **OLED Display** (Optional)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT22 Data** | GP15 | Temperature/Humidity sensor |
| **Wi-Fi** | Built-in | Pico W |

### 6️⃣ Blocks Used

🔹 **Read DHT22**
*   **Category:** Sensors

🔹 **String Formatting**
*   **Category:** Text

🔹 **Socket Send**
*   **Category:** Networking

### 7️⃣ Variables & State
*   **temperature**: Current temperature reading.
*   **humidity**: Current humidity reading.
*   **htmlPage**: Constructed HTML string.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Connect to Wi-Fi and start socket server (same as Project 0386).
    *   From **Sensors**, drag `Setup DHT22 on pin:[15]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Sensor**:
        *   From **Sensors**, drag `read DHT22 temperature and humidity`.
            *   **Snap** into loop.
            *   Store in `temperature` and `humidity`.
    *   **Build HTML**:
        *   From **Text**, drag `set [htmlPage] to [<html><head><meta http-equiv="refresh" content="5"></head><body><h1>Pico Live Data</h1><p>Temperature: {temperature}°C</p><p>Humidity: {humidity}%</p></body></html>]`.
            *   **Snap** below.
    *   **Accept Connection & Send**:
        *   From **Networking**, drag `wait for client`.
        *   From **Networking**, drag `send [HTTP/1.1 200 OK\nContent-Type: text/html\n\n{htmlPage}]`.
        *   From **Networking**, drag `close connection`.

### 9️⃣ Execution Flow (Plain English)

The Pico W reads temperature and humidity from the DHT22 sensor. It then constructs an HTML page with these values embedded. When a browser connects, it receives this HTML page. The `<meta>` refresh tag tells the browser to reload the page every 5 seconds, creating a live-updating dashboard without needing JavaScript or AJAX.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import machine
import time
from dht import DHT22

# Wi-Fi setup (same as before)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
while not wlan.isconnected(): time.sleep(1)

s = socket.socket()
s.bind(('', 80))
s.listen(1)

dht_sensor = DHT22(machine.Pin(15))

while True:
    conn, addr = s.accept()
    
    # Read sensor
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    
    
    # Build HTML
    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
        <title>Pico Telemetry</title>
    </head>
    <body>
        <h1>Live Sensor Data</h1>
        <p>Temperature: """ + str(temp) + """°C</p>
        <p>Humidity: """ + str(hum) + """%</p>
        <p>Last Update: """ + str(time.time()) + """</p>
    </body>
    </html>
    """
    
    conn.send('HTTP/1.1 200 OK\\nContent-Type: text/html\\n\\n' + html)
    conn.close()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sensor Read Delay**: DHT22 should not be read more than once per 2 seconds. Add a delay if auto-refresh is too fast.
*   **Encoding Issues**: Ensure HTML strings use UTF-8 encoding if displaying special characters (°C).

### 1️⃣2️⃣ Try This Next

*   **Chart Integration**: Use Chart.js library to display temperature history as a line graph.
*   **JSON API**: Add an `/api/data` endpoint that returns `{"temp": 25, "hum": 60}` for integration with mobile apps.

---
'''

with open(target_file, 'w', encoding='utf-8') as f:
    f.writelines(output_lines)
    f.write(batch1_content)

print("✅ BATCH 1 COMPLETE: Generated full 12-section Elite docs for Projects 0382-0387")
print("📊 Progress: 6/19 projects completed")
print("📋 Remaining: 13 projects (0388-0400)")
