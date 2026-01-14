# Pass 2 Start: Batch 34 (Projects 0331-0340) - Temperature Alarm 2
# Following locked Elite template from Pass 1

print("🚀 Starting Pass 2: Batch 34 (Temperature Alarm 2)")
print("Generating Projects 0331-0340...")

batch_34 = '''

---

# 🏁 Batch 34: Temperature Alarm 2

## 1️⃣ Project 0331: Introduction to Temperature Alarm

### 2️⃣ Learning Objective
Categorize temperature readings into discrete ranges and display text labels. You will learn data binning and threshold-based classification for environmental monitoring.

### 3️⃣ Concepts Introduced
*   **Data Binning**: Grouping continuous values into discrete categories.
*   **Multiple Thresholds**: Using several comparison points for classification.
*   **Text Output**: Displaying categorical information to users.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor** (DS18B20, DHT11, or onboard RP2040)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | OneWire/Analog depending on sensor type |

### 6️⃣ Blocks Used

🔹 **Setup Temperature Sensor**
*   **Category:** Sensors
*   **Block:** `Setup Temp Sensor pin:[16]`

🔹 **Read Temperature**
*   **Category:** Sensors
*   **Block:** `read temperature sensor`

🔹 **Print**
*   **Category:** Console
*   **Block:** `print [text]`

🔹 **Logic Comparison**
*   **Category:** Logic
*   **Block:** `if... elif... elif... else`

### 7️⃣ Variables & State
*   **temp**: Current temperature reading in Celsius.
*   **category**: Text label for temperature range.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup Temp Sensor pin:[16]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Temperature**:
        *   From **Variables**, drag `set [temp] to`.
            *   **Snap** into loop.
            *   From **Sensors**, drag `read temperature sensor`.
                *   **Snap** into value socket.
    *   **Categorize**:
        *   From **Logic**, drag `if [temp] < [10] then`.
            *   **Snap** below.
            *   Then: `set [category] to [Freezing]`.
        *   From **Logic**, drag `else if [temp] >= [10] and [temp] < [25] then`.
            *   **Snap** below.
            *   Then: `set [category] to [Cool]`.
        *   From **Logic**, drag `else if [temp] >= [25] and [temp] < [35] then`.
            *   **Snap** below.
            *   Then: `set [category] to [Warm]`.
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Then: `set [category] to [Hot]`.
    *   **Display Category**:
        *   From **Console**, drag `print [Temperature: {temp}°C - {category}]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [2] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico reads the temperature sensor every 2 seconds. Based on the value, it assigns a text category: below 10°C is "Freezing", 10-25°C is "Cool", 25-35°C is "Warm", and above 35°C is "Hot". This categorical label is printed to the console alongside the numeric temperature. This demonstrates how raw sensor data is transformed into human-understandable categories for environmental monitoring applications.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

# Temperature sensor (using onboard RP2040 as example)
temp_sensor = machine.ADC(4)

while True:
    # Read temperature
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    # Categorize
    if temp < 10:
        category = "Freezing"
    elif 10 <= temp < 25:
        category = "Cool"
    elif 25 <= temp < 35:
        category = "Warm"
    else:
        category = "Hot"
    
    print(f"Temperature: {temp:.1f}°C - {category}")
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Sensor Type**: Ensure sensor initialization matches your hardware (DS18B20 uses OneWire, DHT11 uses its own protocol, RP2040 uses ADC4).
*   **Overlapping Categories**: Verify threshold conditions don't overlap (use `<` and `>=` pairs consistently).
*   **Category Always Same**: If category doesn't change when temperature varies, check threshold values match your environment. Adjust ranges if needed.

### 1️⃣2️⃣ Try This Next

*   **LED Indicators**: Instead of printing, light different colored LEDs for each category.
*   **More Granular**: Add more categories (e.g., "Very Cold", "Mild", "Very Hot") with narrower ranges.
*   **Historical Trending**: Track which category occurs most frequently over the last hour.

---

'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_34)

print("✅ Project 0331 appended")
print("⏳ Continuing with remaining Batch 34 projects (0332-0340)...")
