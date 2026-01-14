
# 🏁 Batch 19: Communication & Networking (181-190)

## 1️⃣ Project 0181: UART Serial Communication Basics

### 2️⃣ Learning Objective
Master asynchronous serial communication using UART for device-to-device data transfer.

### 3️⃣ Concepts Introduced
*   **UART Protocol**: Asynchronous serial communication
*   **Baud Rate**: Communication speed (9600, 115200)
*   **TX/RX**: Transmit and Receive lines
*   **Frame Structure**: Start/stop bits, data bits, parity

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   USB-to-Serial adapter OR second Pico
*   GPS module (optional)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **UART0 TX** | GP0 |
| **UART0 RX** | GP1 |
| **UART1 TX** | GP4 |
| **UART1 RX** | GP5 |

### 6️⃣ Blocks Used
🔹 **UART Init**: `pico_uart_init` - Configure UART with baud rate
🔹 **UART Write**: `pico_uart_write` - Send data
🔹 **UART Read**: `pico_uart_read` - Receive data

### 7️⃣ Variables
*   **message_count**: Transmitted message counter
*   **received_data**: Incoming data buffer

### 8️⃣ Block Logic (Step-by-Step)
**Implementation: UART Communication**

*   **A. Initialization Phase**
    1.  From **Smart IO**, drag `pico_uart_init`
    2.  Set UART: 0, Baud: 115200, TX: GP0, RX: GP1

*   **B. Main Loop**
    3.  From **Smart IO**, drag `pico_uart_write`
    4.  Send message: "Hello from Pico!"
    5.  From **Smart IO**, drag `pico_uart_read`
    6.  Check if data available, read if yes

### 9️⃣ Execution Flow
Transmit → Check RX → Read if available → Process → Repeat

### 🔟 Generated Code
```python
from machine import UART, Pin
import time

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Hello!\n")
    if uart.any():
        data = uart.read()
        print(f"RX: {data.decode()}")
    time.sleep(1)
```

### 11️⃣ Common Mistakes
*   Baud rate mismatch
*   Wrong pin assignment

### 12️⃣ Try This Next
*   GPS parsing
*   AT command devices

---

## 1️⃣ Project 0182: I2C Multi-Device Communication

### 2️⃣ Learning Objective
Communicate with multiple I2C sensors on a shared bus.

### 3️⃣ Concepts Introduced
*   **I2C Bus**: Shared 2-wire protocol (SDA/SCL)
*   **7-bit Addressing**: Device identification
*   **Pull-up Resistors**: Required for I2C
*   **Clock Stretching**: Slave-controlled timing

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Multiple I2C devices (BME280, OLED, RTC, IMU)
*   4.7kΩ pull-up resistors (×2)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **I2C0 SDA** | GP0 |
| **I2C0 SCL** | GP1 |
| **I2C1 SDA** | GP2 (optional) |
| **I2C1 SCL** | GP3 (optional) |

### 6️⃣ Blocks Used
🔹 **I2C Init**: Configure I2C bus
🔹 **I2C Scan**: Detect device addresses
🔹 **I2C Read/Write**: Data transfer

### 7️⃣ Variables
*   **device_addresses**: List of found devices
*   **sensor_data**: Dictionary for each sensor

### 8️⃣ Block Logic (Step-by-Step)
**Implementation: Multi-Device I2C**

*   **A. Initialization**
    1.  Init I2C at 100kHz
    2.  Scan bus for devices
    3.  Store addresses

*   **B. Main Loop**
    4.  Read each sensor by address
    5.  Store in sensor_data dict
    6.  Display all readings

### 9️⃣ Execution Flow
Scan bus → Identify devices → Read each → Display → Repeat

### 🔟 Generated Code
```python
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Scan bus
devices = i2c.scan()
print(f"Found devices: {[hex(d) for d in devices]}")

while True:
    for addr in devices:
        # Read from each device
        data = i2c.readfrom(addr, 2)
        print(f"Device {hex(addr)}: {data}")
    time.sleep(1)
```

### 11️⃣ Common Mistakes
*   No pull-up resistors
*   Address conflicts
*   Wrong frequency

### 12️⃣ Try This Next
*   Sensor fusion
*   I2C multiplexer

---

## 1️⃣ Project 0183: SPI High-Speed Data Transfer

### 2️⃣ Learning Objective
Implement high-speed SPI communication for displays and memory.

### 3️⃣ Concepts Introduced
*   **SPI Protocol**: Full-duplex serial
*   **MOSI/MISO**: Master Out/In lines
*   **Clock Polarity/Phase**: CPOL/CPHA
*   **Chip Select**: Device selection

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   SD card module OR TFT display
*   SPI flash memory (optional)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :----|:----|
| **SPI0 SCK** | GP2 |
| **SPI0 MOSI** | GP3 |
| **SPI0 MISO** | GP4 |
| **SPI0 CS** | GP5 |

### 6️⃣ Blocks Used
🔹 **SPI Init**: Configure SPI bus
🔹 **SPI Write**: Send data
🔹 **SPI Read**: Receive data

### 7️⃣ Variables
*   **spi_data**: Buffer for transfer
*   **chip_select**: CS pin state

### 8️⃣ Block Logic (Step-by-Step)
**Implementation: SPI Communication**

*   **A. Initialization**
    1.  Init SPI: 1MHz, CPOL=0, CPHA=0
    2.  Configure CS pin

*   **B. Data Transfer**
    3.  Set CS LOW
    4.  Write/Read data
    5.  Set CS HIGH

### 9️⃣ Execution Flow
CS LOW → Transfer data → CS HIGH → Process → Repeat

### 🔟 Generated Code
```python
from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
cs = Pin(5, Pin.OUT)

cs.value(1)  # Idle HIGH

while True:
    cs.value(0)
    spi.write(b'Hello')
    response = spi.read(5)
    cs.value(1)
    print(f"Response: {response}")
    time.sleep(1)
```

### 11️⃣ Common Mistakes
*   Wrong clock settings
*   CS timing issues
*   Speed too high

### 12️⃣ Try This Next
*   SD card file system
*   TFT graphics

---

**Batch 19 continues with Projects 0184-0190...**

Due to scope, shall I:
A) Continue adding all 7 remaining Batch 19 projects now
B) Or append to main file and continue systematically

Proceeding with appending to main file...
