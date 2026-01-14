# BATCH 2: Generate Full Elite Documentation for Projects 0388-0392

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

# Read current file
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find where Project 0387 ends and append from there
# We need to append after the last "---" of 0387

batch2_content = r'''
## 1️⃣ Project 0388: Wi-Fi Web Server 2 - Multi-Button Dashboard

### 2️⃣ Learning Objective
Create a sophisticated web dashboard with multiple buttons to control various Pico outputs. You will learn about UI layout, complex request routing, and multi-endpoint handling.

### 3️⃣ Concepts Introduced
*   **Web Dashboard**: A central interface for multiple controls.
*   **Request Routing**: Directing `/led/on`, `/buzzer/off`, etc., to specific GPIO functions.
*   **HTML Forms**: Using buttons and links to trigger different server endpoints.

### 4️⃣ Hardware Required
*   **Pico W**
*   **3× LEDs** (Red, Green, Blue)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Red** | GP16 | |
| **LED Green** | GP17 | |
| **LED Blue** | GP18 | |
| **Buzzer** | GP15 | PWM |
| **Wi-Fi** | Built-in | Pico W |

### 6️⃣ Blocks Used

🔹 **String Contains**
*   **Category:** Text

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Socket Send**
*   **Category:** Networking

### 7️⃣ Variables & State
*   **htmlDashboard**: Template string for the control panel.
*   **ledStates**: Dictionary tracking LED on/off status.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Networking**, drag `Connect to Wi-Fi`.
        *   **Snap** into setup block.
    *   From **Networking**, drag `Create Socket Server on Port:[80]`.
        *   **Snap** below.
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT`.
        *   **Snap** below (Repeat for pins 17, 18, 15).

*   **B. Main Loop Phase**
    *   **Accept Connection**:
        *   From **Networking**, drag `wait for client connection`.
            *   **Snap** into loop.
        *   From **Networking**, drag `set [request] to [receive 1024 bytes]`.
            *   **Snap** below.
    *   **Route Requests**:
        *   From **Logic**, drag `if [request] contains [/led/red/on] then`.
            *   **Snap** below.
            *   Inside: From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
        *   From **Logic**, drag `if [request] contains [/led/red/off] then`.
            *   **Snap** below.
            *   Inside: From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
        *   (Repeat for Green LED pin 17, Blue LED pin 18, Buzzer pin 15).
    *   **Send Dashboard HTML**:
        *   From **Text**, drag `set [htmlDashboard] to [<html><body><h1>Pico Control Panel</h1><a href="/led/red/on">Red ON</a> | <a href="/led/red/off">Red OFF</a><br>...</body></html>]`.
        *   From **Networking**, drag `send [HTTP/1.1 200 OK\n\n{htmlDashboard}]`.
        *   From **Networking**, drag `close connection`.

### 9️⃣ Execution Flow (Plain English)

The web server hosts a dashboard with multiple hyperlinks. Clicking "Red ON" navigates to `/led/red/on`, which the server detects and sets GP16 HIGH. Each LED and the buzzer have dedicated on/off endpoints. The server responds with the same dashboard HTML, allowing continuous control without refreshing manually.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import machine
import time

# Wi-Fi setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
while not wlan.isconnected(): time.sleep(1)

# Setup GPIO
led_red = machine.Pin(16, machine.Pin.OUT)
led_green = machine.Pin(17, machine.Pin.OUT)
led_blue = machine.Pin(18, machine.Pin.OUT)
buzzer = machine.Pin(15, machine.Pin.OUT)

s = socket.socket()
s.bind(('', 80))
s.listen(1)

dashboard_html = """
<html>
<head><title>Pico Dashboard</title></head>
<body>
    <h1>Pico Control Panel</h1>
    <p><a href="/led/red/on">Red ON</a> | <a href="/led/red/off">Red OFF</a></p>
    <p><a href="/led/green/on">Green ON</a> | <a href="/led/green/off">Green OFF</a></p>
    <p><a href="/led/blue/on">Blue ON</a> | <a href="/led/blue/off">Blue OFF</a></p>
    <p><a href="/buzzer/on">Buzzer ON</a> | <a href="/buzzer/off">Buzzer OFF</a></p>
</body>
</html>
"""

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    # Route requests
    if '/led/red/on' in request:
        led_red.on()
    elif '/led/red/off' in request:
        led_red.off()
    elif '/led/green/on' in request:
        led_green.on()
    elif '/led/green/off' in request:
        led_green.off()
    elif '/led/blue/on' in request:
        led_blue.on()
    elif '/led/blue/off' in request:
        led_blue.off()
    elif '/buzzer/on' in request:
        buzzer.on()
    elif '/buzzer/off' in request:
        buzzer.off()
    
    conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n' + dashboard_html)
    conn.close()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Link Not Working**: Ensure `href` paths exactly match your `if` conditions (case-sensitive).
*   **Button Instead of Link**: For a more polished UI, use HTML `<button>` elements with form submission or JavaScript `fetch()`.

### 1️⃣2️⃣ Try This Next

*   **CSS Styling**: Add inline CSS to make buttons look professional (colors, padding, hover effects).
*   **Status Feedback**: After each action, show "LED Red is now ON" message on the page.

---

## 1️⃣ Project 0389: Wi-Fi Web Server 2 - Password Protection

### 2️⃣ Learning Objective
Secure your web server using a simple authentication check in the request header or URL. You will learn about networking security basics and access control.

### 3️⃣ Concepts Introduced
*   **URL Authentication**: Checking for a secret key in the request (e.g., `/control?key=1234`).
*   **Access Rejection**: Sending HTTP 403 Forbidden if the key is missing or incorrect.
*   **Security Trade-offs**: Understanding that URL keys are NOT secure for critical applications (plaintext).

### 4️⃣ Hardware Required
*   **Pico W**
*   **LED** (for control demonstration)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP16 | |
| **Wi-Fi** | Built-in | Pico W |

### 6️⃣ Blocks Used

🔹 **String Contains**
*   **Category:** Text

🔹 **String Split**
*   **Category:** Text

🔹 **Logic Comparison**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **secretKey**: The correct password (e.g., "pico1234").
*   **providedKey**: Extracted from the URL query string.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [secretKey] to ["pico1234"]`.
        *   **Snap** into setup block.
    *   Connect to Wi-Fi and start socket server.

*   **B. Main Loop Phase**
    *   **Parse URL**:
        *   From **Networking**, drag `wait for client`.
        *   From **Text**, drag `split [request] by [?key=]`.
            *   Store in `parts`.
        *   From **Variables**, drag `set [providedKey] to [parts[1]]`.
    *   **Validate Key**:
        *   From **Logic**, drag `if [providedKey] = [secretKey] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `toggle LED 16`.
                *   From **Networking**, drag `send [HTTP/1.1 200 OK\n\nAccess Granted]`.
        *   From **Logic**, drag `else`.
            *   Inside: From **Networking**, drag `send [HTTP/1.1 403 Forbidden\n\nInvalid Key]`.
    *   **Close Connection**.

### 9️⃣ Execution Flow (Plain English)

When a user navigates to `http://<pico_ip>/control?key=pico1234`, the server extracts "pico1234" from the URL. If it matches the stored secret, the LED toggles and "Access Granted" is shown. If the key is wrong or missing, the server responds with "403 Forbidden" and no action is taken.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import machine
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
while not wlan.isconnected(): time.sleep(1)

led = machine.Pin(16, machine.Pin.OUT)

s = socket.socket()
s.bind(('', 80))
s.listen(1)

SECRET_KEY = "pico1234"

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    # Extract key from URL
    if '?key=' in request:
        key_part = request.split('?key=')[1].split(' ')[0]
        
        if key_part == SECRET_KEY:
            led.toggle()
            conn.send('HTTP/1.1 200 OK\n\nAccess Granted! LED Toggled.')
        else:
            conn.send('HTTP/1.1 403 Forbidden\n\nInvalid Key')
    else:
        conn.send('HTTP/1.1 403 Forbidden\n\nKey Required')
    
    conn.close()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Key in Browser History**: URL parameters are stored in browser history, making them visible.
*   **No HTTPS**: Without encryption, the key is sent in plaintext over the network. Use WPA2 Wi-Fi at minimum.

### 1️⃣2️⃣ Try This Next

*   **Session Cookies**: After successful authentication, set a cookie to avoid re-entering the key every time.
*   **Hash Comparison**: Store a hash of the password instead of the plaintext password for slightly better security.

---

## 1️⃣ Project 0390: Mastering Web Server

### 2️⃣ Learning Objective
Handle multiple simultaneous web requests and serve static assets (small images/styles). You will learn about socket management, non-blocking I/O, and file serving.

### 3️⃣ Concepts Introduced
*   **Non-Blocking Sockets**: Handling connections without stalling the rest of the code.
*   **File Serving**: Reading a `.html` or `.css` file from the Pico's storage and sending it to the browser.
*   **MIME Types**: Sending correct `Content-Type` headers for different file types.

### 4️⃣ Hardware Required
*   **Pico W**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Wi-Fi** | Built-in | Pico W |

### 6️⃣ Blocks Used

🔹 **File Read**
*   **Category:** File System

🔹 **Socket Set Timeout**
*   **Category:** Networking

🔹 **String Manipulation**
*   **Category:** Text

### 7️⃣ Variables & State
*   **requestedFile**: Parsed filename from the URL.
*   **fileContent**: Contents read from storage.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Connect to Wi-Fi.
    *   From **Networking**, drag `Create Socket Server on Port:[80]`.
    *   From **Networking**, drag `set socket timeout to [1] seconds`.
        *   **Snap** below (enables non-blocking).

*   **B. Main Loop Phase**
    *   **Accept with Timeout**:
        *   From **Logic**, drag `try:`.
            *   Inside: From **Networking**, drag `wait for client`.
        *   From **Logic**, drag `except timeout:`.
            *   Inside: `continue` (skip to next loop iteration).
    *   **Parse Request**:
        *   From **Text**, drag `split [request] by [ ]`.
            *   Get method and path.
        *   From **Variables**, drag `set [requestedFile] to [path or "index.html"]`.
    *   **Serve File**:
        *   From **Logic**, drag `if file exists [requestedFile] then`.
            *   Inside:
                *   From **File System**, drag `read file [requestedFile]`.
                    *   Store in `fileContent`.
                *   From **Networking**, drag `send [HTTP/1.1 200 OK\nContent-Type: text/html\n\n{fileContent}]`.
        *   Else:
            *   From **Networking**, drag `send [HTTP/1.1 404 Not Found\n\nFile Not Found]`.

### 9️⃣ Execution Flow (Plain English)

The server uses a non-blocking socket with a 1-second timeout. This allows it to check for new connections without freezing. When a request comes in, it parses the URL to extract the requested filename (e.g., `/style.css`). If the file exists in the Pico's storage, it reads and sends it. Otherwise, it returns a 404 error. This enables serving full websites with separate HTML, CSS, and JavaScript files.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import os

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
while not wlan.isconnected(): pass

s = socket.socket()
s.bind(('', 80))
s.listen(5)
s.settimeout(1.0)  # Non-blocking with 1s timeout

print(f"Server running at {wlan.ifconfig()[0]}")

while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()
        
        # Parse requested file
        try:
            path = request.split(' ')[1]
            if path == '/':
                path = '/index.html'
            filename = path.lstrip('/')
        except:
            filename = 'index.html'
        
        # Serve file
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            # Determine content type
            if filename.endswith('.css'):
                content_type = 'text/css'
            elif filename.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'text/html'
            
            response = f'HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n{content}'
            conn.send(response)
        except OSError:
            conn.send('HTTP/1.1 404 Not Found\n\n404 - File Not Found')
        
        conn.close()
    except OSError:
        pass  # Timeout, no connection available
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Files in Storage**: Use Thonny or `ampy` to upload `.html` files to the Pico's root directory first.
*   **Blocking Forever**: Without `settimeout()`, `accept()` blocks indefinitely, preventing other code from running.

### 1️⃣2️⃣ Try This Next

*   **Logging**: Track how many times each file is accessed and log to a separate file.
*   **Compression**: For large files, implement basic gzip compression before sending.

---

## 1️⃣ Project 0391: File System 2 - Data Persistence

### 2️⃣ Learning Objective
Implement "Settings Memory" that survives a power reboot. You will learn about write-once read-many cycles and persistent state management.

### 3️⃣ Concepts Introduced
*   **Non-Volatile Storage**: Saving variables to the internal flash so they remain after power is lost.
*   **Initialization Retrieval**: Checking for the existence of a config file during boot.
*   **Read-Modify-Write Pattern**: Loading, changing, and saving data in sequence.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Configuration Trigger)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Write File**
*   **Category:** File System

🔹 **Read File**
*   **Category:** File System

🔹 **Check File Exists**
*   **Category:** File System

### 7️⃣ Variables & State
*   **configVal**: A settings value (e.g., 1 or 0) stored in `settings.txt`.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **File System**, drag `if file "settings.txt" exists then`.
        *   **Snap** into setup block.
        *   Inside:
            *   From **File System**, drag `set [configVal] to [read from "settings.txt"]`.
                *   **Snap** inside.
    *   From **Logic**, drag `else`.
        *   Inside: From **Variables**, drag `set [configVal] to [0]`.
            *   **Snap** inside (default value).
    *   From **Console**, drag `print [Config loaded: {configVal}]`.

*   **B. Main Loop Phase**
    *   **Change Setting**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Math**, drag `set [configVal] to [1 - configVal]`.
                    *   **Snap** inside (toggle between 0 and 1).
                *   From **File System**, drag `write [configVal] to "settings.txt"`.
                    *   **Snap** below.
                *   From **Console**, drag `print [Setting saved: {configVal}]`.
                    *   **Snap** below.
                *   From **Timing**, drag `sleep [0.5] seconds`.
                    *   **Snap** below (debounce).

### 9️⃣ Execution Flow (Plain English)

On boot, the Pico checks if a file called "settings.txt" exists in its memory chip. If it does, it loads the value into a variable. If not, it defaults to 0. When you press the button, the value toggles (0→1 or 1→0) and is immediately written back to the file. If you unplug the Pico and plug it back in, it will remember the last setting you saved.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import os

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def save_config(value):
    with open("settings.txt", "w") as f:
        f.write(str(value))

def load_config():
    try:
        with open("settings.txt", "r") as f:
            return int(f.read())
    except OSError:
        return 0  # Default if file doesn't exist

config_val = load_config()
print(f"Config loaded: {config_val}")

while True:
    if button.value():
        config_val = 1 - config_val  # Toggle
        save_config(config_val)
        print(f"Setting saved: {config_val}")
        time.sleep(0.5)  # Debounce
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **File Not Created**: Ensure the Pico has write permissions. If using CIRCUITPY mode, switch to MicroPython mode.
*   **Flash Wear**: Flash memory has limited write cycles (~10,000-100,000). Avoid writing every loop iteration.

### 1️⃣2️⃣ Try This Next

*   **JSON Config**: Store multiple settings as JSON: `{"brightness": 80, "alarm": True}`.
*   **Backup File**: Create `settings_backup.txt` and copy to it before writing new data to prevent corruption.

---

## 1️⃣ Project 0392: File System 2 - CSV Data Logging

### 2️⃣ Learning Objective
Create a structured datasheet in CSV format for spreadsheet analysis. You will learn about string formatting and append-mode writing.

### 3️⃣ Concepts Introduced
*   **CSV Format**: Comma Separated Values for universal compatibility with Excel/Sheets.
*   **Append Mode ('a')**: Adding new data to the end of a file without deleting old data.
*   **Header Row**: Writing column names as the first line for clarity.

### 4️⃣ Hardware Required
*   **Pico**
*   **DHT22 Sensor** (for data logging example)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT22 Data** | GP15 | Temperature/Humidity sensor |

### 6️⃣ Blocks Used

🔹 **Read DHT22**
*   **Category:** Sensors

🔹 **String Join**
*   **Category:** Text

🔹 **File Append**
*   **Category:** File System

### 7️⃣ Variables & State
*   **timestamp**: Current time in seconds.
*   **temperature**: Latest reading.
*   **humidity**: Latest reading.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup DHT22 on pin:[15]`.
        *   **Snap** into setup block.
    *   From **File System**, drag `if NOT file "log.csv" exists then`.
        *   **Snap** below.
        *   Inside:
            *   From **File System**, drag `write ["Time,Temperature,Humidity\n"] to "log.csv"`.
                *   **Snap** inside (create header).

*   **B. Main Loop Phase**
    *   **Read Sensor**:
        *   From **Sensors**, drag `read DHT22 temperature and humidity`.
            *   **Snap** into loop.
            *   Store in `temperature` and `humidity`.
    *   **Format CSV Line**:
        *   From **Timing**, drag `set [timestamp] to [time()]`.
        *   From **Text**, drag `set [csvLine] to [{timestamp},{temperature},{humidity}\n]`.
            *   **Snap** below.
    *   **Append to File**:
        *   From **File System**, drag `append [csvLine] to "log.csv"`.
            *   **Snap** below.
        *   From **Console**, drag `print [Data logged]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [60] seconds`.
        *   **Snap** below (log every minute).

### 9️⃣ Execution Flow (Plain English)

Every 60 seconds, the program reads the temperature and humidity from the DHT22 sensor. It formats these values, along with a timestamp, into a CSV line like "1672531200,25.3,55.2\n". This line is appended to "log.csv". Over time, the file accumulates rows that can be opened in Excel or Google Sheets for graphing and analysis.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from dht import DHT22
import os

dht_sensor = DHT22(machine.Pin(15))

# Create CSV with header if it doesn't exist
if 'log.csv' not in os.listdir():
    with open('log.csv', 'w') as f:
        f.write('Time,Temperature,Humidity\n')

while True:
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    
    timestamp = time.time()
    csv_line = f'{timestamp},{temp},{hum}\n'
    
    # Append to CSV
    with open('log.csv', 'a') as f:
        f.write(csv_line)
    
    print(f'Data logged: {temp}°C, {hum}%')
    time.sleep(60)  # Log every minute
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Newline**: Ensure each line ends with `\n`, or all data will appear on one line.
*   **File Gets Huge**: CSV files grow indefinitely. Implement log rotation (see Project 0393).

### 1️⃣2️⃣ Try This Next

*   **Real-Time Clock**: Use the DS3231 RTC module to log actual date/time instead of uptime seconds.
*   **Conditional Logging**: Only log if temperature changes by more than 0.5°C to save space.

---
'''

# Append to file
with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch2_content)

print("✅ BATCH 2 COMPLETE: Generated full 12-section Elite docs for Projects 0388-0392")
print("📊 Progress: 11/19 projects completed")
print("📋 Remaining: 8 projects (0393-0400)")
