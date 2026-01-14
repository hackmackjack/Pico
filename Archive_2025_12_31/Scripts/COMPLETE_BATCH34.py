# BATCH 34 FINAL: Last 4 Projects (0337-0340)
# Completing Temperature Alarm batch

print("Generating final 4 projects to complete Batch 34...")

final_four = '''
## 1️⃣ Project 0337: Temperature Alarm Alarm System

### 2️⃣ Learning Objective
Implement a circular buffer data logger that records temperature history and provides on-demand retrieval. You will learn data logging, buffer management, and historical data analysis.

### 3️⃣ Concepts Introduced
*   **Circular Buffer**: Fixed-size array that overwrites oldest data.
*   **Data Logging**: Recording sensor values over time.
*   **Historical Retrieval**: Accessing past data on demand.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **Button** (dump trigger)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor pin |
| **Button** | GP10 | PULL_DOWN enabled |

### 6️⃣ Blocks Used

🔹 **Setup Button & Sensor**
*   **Category:** Inputs/Sensors

🔹 **Lists**
*   **Category:** Lists
*   **Block:** `create list`, `replace item`, `item at index`

🔹 **Print**
*   **Category:** Console

### 7️⃣ Variables & State
*   **tempLog**: List storing last 10 temperature readings.
*   **logIndex**: Current write position in circular buffer (0-9).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Setup button (GP10).
    *   Create list [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
    *   Set logIndex = 0.

*   **B. Main Loop Phase**
    *   Read temperature.
    *   Store in tempLog[logIndex].
    *   Increment logIndex.
    *   If logIndex > 9: logIndex = 0 (wrap around).
    *   If button pressed:
        *   Print "Last 10 readings:".
        *   For each item in tempLog: print value.
    *   Sleep 60 seconds (1 minute intervals).

### 9️⃣ Execution Flow (Plain English)

Every minute, system reads temperature and stores it in a circular buffer holding 10 values. When buffer fills, new readings overwrite oldest ones, always maintaining last 10 minutes of data. When button is pressed, all 10 stored values are dumped to console, showing temperature trend. This "black box" approach enables post-event analysis.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

tempLog = [0] * 10
logIndex = 0

lastLog = time.time()

while True:
    # Log every 60 seconds
    if time.time() - lastLog >= 60:
        reading = temp_sensor.read_u16()
        temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
        
        tempLog[logIndex] = temp
        logIndex = (logIndex + 1) % 10
        lastLog = time.time()
        print(f"Logged: {temp:.1f}°C")
    
    # Dump on button press
    if button.value():
        print("\\n=== Last 10 Readings ===")
        for i, t in enumerate(tempLog):
            print(f"{i+1}: {t:.1f}°C")
        while button.value():
            time.sleep(0.01)
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Timing**: If logs happen too frequently, ensure 60-second check uses proper time comparison, not sleep.
*   **Buffer Not Circular**: If only first 10 values stored, verify logIndex wraps with modulo (%).
*   **Duplicate Dumps**: Add debounce (while button.value sleep) after dump to prevent multiple prints from one press.

### 1️⃣2️⃣ Try This Next

*   **Timestamps**: Store time alongside temperature for each reading.
*   **SD Card**: Save log to SD card for persistent storage across power cycles.
*   **Statistics**: Calculate and display min/max/average from the 10 readings.

---

## 1️⃣ Project 0338: The Temperature Alarm Game

### 2️⃣ Learning Objective
Detect rapid temperature/humidity changes from human breath to create an interactive detection game. You will learn spike detection and time-window analysis.

### 3️⃣ Concepts Introduced
*   **Spike Detection**: Identifying rapid value changes.
*   **Time Window**: Monitoring changes within specific duration.
*   **Baseline Comparison**: Detecting deviation from normal state.

### 4️⃣ Hardware Required
*   **Pico**
*   **DHT11 Sensor** (temp + humidity)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT11 Data** | GP16 | Pull-up resistor (4.7kΩ) required |

### 6️⃣ Blocks Used

🔹 **Setup DHT Sensor**
*   **Category:** Sensors

🔹 **Read DHT**
*   **Category:** Sensors

🔹 **Time Functions**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **baselineHumidity**: Normal humidity level.
*   **currentHumidity**: Latest reading.
*   **detectionWindow**: 2-second window for spike.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup DHT11 (GP16).
    *   Read initial humidity → baselineHumidity.
    *   Print "Blow on sensor within 2 seconds!".

*   **B. Main Loop Phase**
    *   Loop for 2 seconds:
        *   Read humidity.
        *   If humidity > (baselineHumidity + 15%):
            *   Print "BREATH DETECTED!".
            *   Break loop.
        *   Sleep 0.2s.
    *   After 2s timeout:
        *   Print "No breath detected. Try again!".
    *   Sleep 3s before next round.

### 9️⃣ Execution Flow (Plain English)

System establishes baseline humidity when idle. It then monitors for 2 seconds, checking 10 times per second for humidity spikes above baseline+15%. Human breath contains high moisture, so blowing on DHT11 causes instant humidity jump of 20-40%, triggering detection. If no spike occurs within 2 seconds, test fails. This teaches how to detect transient environmental changes.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import dht

sensor = dht.DHT11(machine.Pin(16))

while True:
    # Establish baseline
    sensor.measure()
    baselineHumidity = sensor.humidity()
    print(f"\\nBaseline: {baselineHumidity}% - Blow on sensor NOW!")
    
    start = time.time()
    detected = False
    
    while time.time() - start < 2:
        try:
            sensor.measure()
            currentHumidity = sensor.humidity()
            
            if currentHumidity > baselineHumidity + 15:
                print(f"BREATH DETECTED! Spike: {currentHumidity}%")
                detected = True
                break
        except:
            pass
        time.sleep(0.2)
    
    if not detected:
        print("No breath detected. Try again!")
    
    time.sleep(3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Detects**: If any small change triggers, reduce threshold from +15% to +20% for stricter detection.
*   **Never Detects**: Blow directly on sensor grill. Breath must hit sensor element. Also verify DHT11 is working.
*   **DHT Errors**: DHT11 can fail reads. Wrap in try/except and continue if read fails.

### 1️⃣2️⃣ Try This Next

*   **Temperature Spike**: Detect temp increase from breath instead of humidity.
*   **Score System**: Award points based on detection speed (faster = higher score).
*   **Multi-Player**: Take turns, record who triggers fastest spike.

---

##  1️⃣ Project 0339: Automated Temperature Alarm

### 2️⃣ Learning Objective
Send critical alert messages via UART when temperature exceeds dangerous threshold. You will learn serial communication for emergency notifications.

### 3️⃣ Concepts Introduced
*   **UART Communication**: Asynchronous serial data transmission.
*   **Critical Alerts**: Sending emergency messages to external systems.
*   **Message Formatting**: Structuring alarm data for remote processing.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   *(Optional: Second Pico or USB-serial adapter to receive messages)*

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor pin |
| **UART TX** | GP4 (UART1 TX) | Transmit to main computer |

### 6️⃣ Blocks Used

🔹 **Setup UART**
*   **Category:** Communication
*   **Block:** `Setup UART [1] TX:[4] baud:[9600]`

🔹 **UART Send**
*   **Category:** Communication
*   **Block:** `UART send [message]`

### 7️⃣ Variables & State
*   **temp**: Temperature reading.
*   **alarmSent**: Flag to prevent spam.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Setup UART1 TX on GP4, baud 9600.
    *   Set alarmSent = false.

*   **B. Main Loop Phase**
    *   Read temperature.
    *   If temp > 50°C AND not alarmSent:
        *   Send UART message: "FIRE DETECTED\\n".
        *   Set alarmSent = true.
        *   Print "Alert sent!".
    *   If temp < 45°C:
        *   Set alarmSent = false (reset for next event).
    *   Sleep 1s.

### 9️⃣ Execution Flow (Plain English)

System monitors temperature continuously. When it exceeds 50°C threshold (simulating fire), it transmits "FIRE DETECTED" message via UART to monitoring computer. Flag prevents repeated messages during same event. When temperature drops below 45°C (5-degree hysteresis), flag resets, allowing detection of next event. This demonstrates one-way emergency communication.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4))

alarmSent = False

while True:
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    if temp > 50 and not alarmSent:
        uart.write("FIRE DETECTED\\n")
        print(f"ALERT SENT: {temp:.1f}°C")
        alarmSent = True
    elif temp < 45:
        alarmSent = False
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Message Received**: Verify UART RX device is connected to GP4 and set to 9600 baud. Check ground connection.
*   **Spam Messages**: If messages repeat constantly, ensure alarmSent flag is set and checked properly.
*   **Threshold Too High**: 50°C is extreme for testing. Lower to 30°C for easier demonstration.

### 1️⃣2️⃣ Try This Next

*   **Two-Way**: Add UART RX to receive acknowledgment from main computer.
*   **JSON Format**: Send structured data: `{"type":"fire","temp":52.3,"time":1234567}`.
*   **Multiple Sensors**: Send alerts from different sensor locations on same UART bus.

---

## 1️⃣ Project 0340: Mastering Temperature Alarm

### 2️⃣ Learning Objective
Calibrate temperature sensor by calculating and applying offset correction. You will learn sensor error compensation and calibration procedures.

### 3️⃣ Concepts Introduced
*   **Sensor Calibration**: Correcting systematic measurement errors.
*   **Offset Correction**: Adding fixed value to compensate for bias.
*   **Reference Comparison**: Using known-good standard for validation.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **Console Input** (for reference temperature)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor to calibrate |

### 6️⃣ Blocks Used

🔹 **Setup Temp Sensor**
*   **Category:** Sensors

🔹 **Input**
*   **Category:** Console
*   **Block:** `input [prompt]`

🔹 **Print**
*   **Category:** Console

### 7️⃣ Variables & State
*   **rawReading**: Uncalibrated sensor value.
*   **knownTemp**: Reference temperature (user input).
*   **offset**: Calculated correction value.
*   **calibratedTemp**: Corrected reading.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Set offset = 0.

*   **B. Calibration Phase** (one-time):
    *   Read sensor → rawReading.
    *   Print "Current reading: {rawReading}°C".
    *   Prompt user: "Enter known-good temperature:".
    *   Read input → knownTemp.
    *   Calculate: offset = knownTemp - rawReading.
    *   Print "Calibration complete. Offset: {offset}°C".

*   **C. Main Loop Phase**:
    *   Read sensor → rawReading.
    *   Calculate: calibratedTemp = rawReading + offset.
    *   Print "Raw: {rawReading}°C, Calibrated: {calibratedTemp}°C".
    *   Sleep 2s.

### 9️⃣ Execution Flow (Plain English)

During calibration, system reads current sensor value. User provides reference temperature from accurate thermometer. System calculates difference (offset = reference - measured) and stores it. From then on, all readings are adjusted by adding this offset, compensating for sensor bias. For example, if sensor reads 22°C when actual is 25°C, offset = +3°C, and future readings add 3 degrees.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
offset = 0.0

def read_temp():
    reading = temp_sensor.read_u16()
    return 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721

# Calibration
raw = read_temp()
print(f"Current reading: {raw:.1f}°C")
known = float(input("Enter known-good temperature (°C): "))
offset = known - raw
print(f"Calibration complete. Offset: {offset:.2f}°C\\n")

# Main loop
while True:
    raw = read_temp()
    calibrated = raw + offset
    print(f"Raw: {raw:.1f}°C → Calibrated: {calibrated:.1f}°C")
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Reference**: Ensure reference thermometer is accurate and both sensors are at same location/temperature.
*   **Offset Not Persisting**: Offset resets on power cycle unless stored in file/EEPROM. For this project, recalibrate each run.
*   **Large Offset**: If offset exceeds ±5°C, sensor or reference may be faulty. Verify both work.

### 1️⃣2️⃣ Try This Next

*   **Two-Point Calibration**: Calibrate at ice water (0°C) and boiling water (100°C) for slope correction.
*   **Persistent Storage**: Save offset to file so calibration survives power cycles.
*   **Auto-Calibration**: Use known environmental constant (e.g., room should be 20-25°C) for automatic drift detection.

---
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_four)

print("\\n" + "="*60)
print("🎉 BATCH 34 COMPLETE! 🎉")
print("="*60)
print("\\n✅ All 10 Temperature Alarm projects generated (0331-0340)")
print("\\nPass 2 Progress:")
print("  - Batch 34 COMPLETE (10/10)")
print("  - Batch 35 PENDING (0/10 - Smart Fan 2)")
print("  - Batch 36 PENDING (0/10 - Robotic Arm 2)")
print("\\nTotal documentation: Projects 0301-0340 (40/100)")
print("\\nNext: Batch 35 (Smart Fan 2) with safety-critical guidelines")
