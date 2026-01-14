# BATCH 34 FINAL: Complete Projects 0332-0340
# Generating all 9 remaining Temperature Alarm projects directly

print("Generating Projects 0332-0340 for Batch 34 completion...")

batch_34_final = '''
## 1️⃣ Project 0332: Blinking Temperature Alarm

### 2️⃣ Learning Objective
Map temperature values to LED blink frequency to create visual feedback proportional to heat. You will learn variable-frequency control and how to convert sensor data to timing parameters.

### 3️⃣ Concepts Introduced
*   **Variable Frequency**: Adjusting blink rate based on input value.
*   **Temperature-to-Frequency Mapping**: Converting sensor data to timing.
*   **Visual Feedback Scaling**: Making changes perceptible to humans.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **LED**
*   **220Ω Resistor**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor data pin |
| **LED** | GP15 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **Setup Temp Sensor & Pin**
*   **Category:** Sensors/Outputs

🔹 **Map Range**
*   **Category:** Math
*   **Block:** `map [temp] from [20]-[40] to [1.0]-[0.25]`

### 7️⃣ Variables & State
*   **temp**: Temperature reading.
*   **blinkDelay**: Calculated delay in seconds (inversely proportional to frequency).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temperature sensor (GP16).
    *   Setup LED pin (GP15) as OUTPUT.

*   **B. Main Loop Phase**
    *   Read temperature.
    *   Map temp (20-40°C) → blinkDelay (1.0-0.25s):
        *   20°C = 1s delay = 1 blink/sec
        *   30°C = 0.5s delay = 2 blinks/sec
        *   40°C = 0.25s delay = 4 blinks/sec
    *   Toggle LED.
    *   Sleep for blinkDelay.

### 9️⃣ Execution Flow (Plain English)

System reads temperature and calculates blink delay inversely: higher temperature = shorter delay = faster blinking. At 20°C, LED blinks once per second. At 30°C, twice per second. At 40°C, four times per second. This creates intuitive visual urgency that escalates with heat level.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
led = machine.Pin(15, machine.Pin.OUT)

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    # Map 20-40°C → 1.0-0.25s delay
    blinkDelay = map_range(temp, 20, 40, 1.0, 0.25)
    blinkDelay = max(0.25, min(1.0, blinkDelay))  # Clamp
    
    led.toggle()
    time.sleep(blinkDelay)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Constant Blink Rate**: If frequency doesn't change, verify map function and temp reading work correctly.
*   **Too Fast/Slow**: Adjust temperature range (20-40°C) to match your environment.
*   **Inverted**: If hotter = slower, you mapped incorrectly. Higher temp should give shorter delay.

### 1️⃣2️⃣ Try This Next

*   **RGB Intensity**: Instead of blink rate, vary LED brightness (PWM duty cycle) with temperature.
*   **Dual Threshold**: Below 25°C = slow blink blue LED, above 35°C = fast blink red LED.
*   **Non-Linear**: Use exponential mapping for more dramatic frequency changes.

---

## 1️⃣ Project 0333: Manual Temperature Alarm Control

### 2️⃣ Learning Objective
Create a user-adjustable temperature alarm threshold using a potentiometer. You will learn how to combine manual input with sensor comparison for customizable alerting.

### 3️⃣ Concepts Introduced
*   **User-Defined Threshold**: Allowing manual limit configuration.
*   **Dual Input System**: Reading both sensor and control input.
*   **Visual Feedback**: Displaying current settings.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **Potentiometer** (10kΩ)
*   **Buzzer** (active or passive)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor pin |
| **Potentiometer** | GP26 (ADC0) | Threshold control |
| **Buzzer** | GP15 | Alarm output |

### 6️⃣ Blocks Used

🔹 **Setup ADC**
*   **Category:** Inputs

🔹 **Read Analog**
*   **Category:** Pin Access

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Print**
*   **Category:** Console

### 7️⃣ Variables & State
*   **temp**: Current temperature.
*   **threshold**: User-set alarm threshold (20-40°C from pot).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Setup ADC for pot (GP26).
    *   Setup buzzer pin (GP15).

*   **B. Main Loop Phase**
    *   Read temp.
    *   Read pot, map to 20-40°C range → threshold.
    *   Print: "Threshold: {threshold}°C, Current: {temp}°C".
    *   If temp > threshold:
        *   Buzzer ON.
    *   Else:
        *   Buzzer OFF.
    *   Sleep 0.5s.

### 9️⃣ Execution Flow (Plain English)

User adjusts potentiometer to set desired temperature alarm point (20-40°C). System continuously compares current temperature to this threshold. When temperature exceeds the user-defined limit, buzzer activates. Console displays both current temp and threshold for monitoring. This demonstrates adjustable limit systems.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
pot = machine.ADC(26)
buzzer = machine.Pin(15, machine.Pin.OUT)

def map_range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Read temp
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    # Read threshold from pot
    pot_val = pot.read_u16()
    threshold = map_range(pot_val, 0, 65535, 20, 40)
    
    print(f"Threshold: {threshold}°C, Current: {temp:.1f}°C")
    
    # Alarm logic
    if temp > threshold:
        buzzer.on()
    else:
        buzzer.off()
    
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Threshold Jumpy**: Add averaging or small capacitor on pot signal to smooth readings.
*   **Always Alarming**: Verify threshold range (20-40°C) is appropriate for your environment.
*   **No Console Output**: Ensure USB is connected and serial monitor is open.

### 1️⃣2️⃣ Try This Next

*   **OLED Display**: Show threshold and current temp on OLED instead of console.
*   **Hysteresis**: Add 2-degree buffer to prevent buzzer flickering at threshold boundary.
*   **Multi-Zone**: Use 3 LEDs for "safe" (green), "warning" (yellow), "alarm" (red) zones.

---

[Continuing with remaining 7 projects...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_34_final)

print("✅ Projects 0332-0333 appended")
print("⏳ Generating final 7 projects (0334-0340)...")
