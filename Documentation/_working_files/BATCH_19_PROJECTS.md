# 🏁 Batch 19: Communication & Networking (181-190)

## Domain 5: Communication Protocols & IoT Integration

This batch covers all essential communication interfaces from basic serial to advanced IoT cloud integration, providing students with comprehensive networking capabilities for embedded systems.

---

## 1️⃣ Project 0181: UART Serial Communication Basics

### 2️⃣ Learning Objective
Master asynchronous serial communication using UART for device-to-device data transfer and debugging.

### 3️⃣ Concepts Introduced
*   **UART Protocol**: Universal Asynchronous Receiver-Transmitter
*   **Baud Rate**: Communication speed (9600, 115200, etc.)
*   **Start/Stop Bits**: Frame structure
*   **Data Bits & Parity**: Error checking

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   USB-to-Serial adapter OR second Pico
*   GPS module (optional application)
*   Serial LCD display (optional)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **UART0 TX** | GP0 |
| **UART0 RX** | GP1 |
| **UART1 TX** | GP4 |
| **UART1 RX** | GP5 |

### 6️⃣ Blocks Used
🔹 **UART Initialization**
*   **Category:** Smart IO
*   **Block:** `pico_uart_init`
*   **Settings:** UART ID (0 or 1), Baud rate, TX/RX pins

🔹 **UART Write**
*   **Category:** Smart IO
*   **Block:** `pico_uart_write`
*   **Settings:** UART ID, data string

🔹 **UART Read**
*   **Category:** Smart IO
*   **Block:** `pico_uart_read`
*   **Settings:** UART ID, bytes to read

### 7️⃣ Variables
*   **received_data**: String buffer for incoming data
*   **tx_message**: Message to transmit
*   **bytes_available**: Number of bytes in RX buffer

### 8️⃣ Block Logic (Step-by-Step)
**Implementation: Basic UART Communication**

*   **A. Initialization Phase (Setup Block)**
    1.  **Configure UART0**:
        *   From **Smart IO**, drag `pico_uart_init` block
        *   **Snap** to **Setup**: Set UART: 0, Baud: 115200
        *   TX: GP0, RX: GP1
    2.  **Create Communication Variables**:
        *   From **Variables**, create `message_count` = 0
        *   Create `received_data` = ""
        *   Create `tx_buffer` = ""

*   **B. Main Loop Phase (Transmit/Receive)**
    3.  **Create Forever Loop**:
        *   From **Loops**, drag `forever do` block
    4.  **Transmit Message**:
        *   **Snap** inside loop:
            *   From **Variables**, create `tx_message` = "Hello from Pico!"
            *   From **Smart IO**, drag `pico_uart_write`
            *   Set UART: 0, Data: `tx_message`
            *   Increment `message_count`
    5.  **Check for Incoming Data**:
        *   From **Smart IO**, drag `pico_uart_any` (checks if data available)
        *   From **Logic**, drag `if` data available
    6.  **Read Received Data**:
        *   **Snap** inside if:
            *   From **Smart IO**, drag `pico_uart_read`
            *   Set UART: 0, Bytes: -1 (read all available)
            *   Store in `received_data`
    7.  **Process Received Data**:
        *   From **Text**, print "Received: {received_data}"
        *   From **Logic**, parse or respond to commands

*   **C. Application Example (GPS Parsing)**
    8.  **GPS Module Communication**:
        *   GPS sends NMEA sentences at 9600 baud
        *   From **Text**, use `split` to parse $GPGGA messages
        *   Extract latitude, longitude, time
    9.  **Display Results**:
        *   From **Text**, print parsed GPS coordinates
    10. **Loop Delay**:
        *   From **Time**, drag `pico_wait` → 1 second

### 9️⃣ Execution Flow
```
Loop (1 Hz):
  1. Transmit message via UART
  2. Check if data received
  3. If yes: Read & process
  4. Display/act on received data
  5. Wait 1 second
```

**Baud Rate Selection**:
- **9600**: GPS, simple sensors
- **115200**: Debug console, high-speed data
- **230400+**: Camera data, fast logging

### 🔟 Generated Code
```python
from machine import UART, Pin
import time

# Initialize UART0
uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

message_count = 0

print("📡 UART Communication Demo")
print("Baud: 115200")
print("\nTransmitting and receiving...")

while True:
    # Transmit
    tx_message = f"Message #{message_count}: Hello from Pico!\n"
    uart0.write(tx_message.encode())
    print(f"TX: {tx_message.strip()}")
    message_count += 1
    
    # Receive
    if uart0.any():
        received_data = uart0.read()
        received_str = received_data.decode('utf-8', 'ignore')
        print(f"RX: {received_str.strip()}")
    
    time.sleep(1)
```

**GPS Parsing Example**:
```python
# GPS at 9600 baud
gps_uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

while True:
    if gps_uart.any():
        line = gps_uart.readline().decode('utf-8', 'ignore')
        if line.startswith("$GPGGA"):
            parts = line.split(',')
            if len(parts) > 5:
                lat = parts[2]
                lon = parts[4]
                print(f"Position: {lat}, {lon}")
    time.sleep(0.1)
```

### 11️⃣ Common Mistakes
*   **Baud Rate Mismatch**: TX and RX must match exactly
*   **Wrong Pins**: UART0 and UART1 have specific pin assignments
*   **Buffer Overflow**: Not reading fast enough causes data loss
*   **No Line Ending**: Some devices need \r\n terminator

### 12️⃣ Try This Next
*   **AT Command Devices**: Control GSM/WiFi modules
*   **Modbus Protocol**: Industrial sensor communication
*   **Binary Protocols**: Efficient data structures

---

**Progress: 81/100 projects complete! (0101-0181)** 🎉

Continuing with remaining Batch 19 projects...
