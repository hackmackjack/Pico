# COMPLETE BATCH 34: Final 7 Projects (0334-0340)
# Direct generation following locked Elite template

print("Generating final 7 Batch 34 projects (0334-0340)...")

final_seven = '''
## 1️⃣ Project 0334: Temperature Alarm Sequences

### 2️⃣ Learning Objective
Implement bang-bang feedback control using temperature to trigger motor cooling cycles. You will learn basic closed-loop control systems and automated response sequences.

### 3️⃣ Concepts Introduced
*   **Bang-Bang Control**: Simple on/off feedback control.
*   **Feedback Loop**: Sensor → decision → actuator → sensor.
*   **Cooling Cycle**: Timed intervention with re-evaluation.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **DC Motor** (fan) with driver (L298N or similar)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor pin |
| **Motor Enable** | GP14 | PWM to motor driver |
| **Motor Direction** | GP15 | Direction control (optional, set to one direction) |

### 6️⃣ Blocks Used

🔹 **Setup Temp Sensor**
*   **Category:** Sensors

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **PWM Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **temp**: Current temperature.
*   **threshold**: Temperature limit (30°C).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Setup motor PWM (GP14).
    *   Setup direction pin (GP15) to HIGH (one direction).

*   **B. Main Loop Phase**
    *   Read temperature.
    *   If temp > 30°C:
        *   Turn motor ON (PWM duty 65535).
        *   Sleep 5 seconds.
        *   Turn motor OFF.
    *   Else:
        *   Motor remains OFF.
    *   Sleep 1 second before next check.

### 9️⃣ Execution Flow (Plain English)

System checks temperature every second. When temp exceeds 30°C threshold, it activates cooling fan at full speed for 5 seconds, then stops and rechecks. If still hot, cycle repeats. This bang-bang control demonstrates basic feedback: sensor detects condition, system responds with actuator, then re-evaluates. Simple but effective for many applications.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
motor = machine.PWM(machine.Pin(14))
direction = machine.Pin(15, machine.Pin.OUT)

motor.freq(1000)
direction.high()  # Set one direction

THRESHOLD = 30

while True:
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    if temp > THRESHOLD:
        print(f"HOT ({temp:.1f}°C) - Cooling for 5s")
        motor.duty_u16(65535)
        time.sleep(5)
        motor.duty_u16(0)
    else:
        print(f"OK ({temp:.1f}°C)")
        motor.duty_u16(0)
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Motor Always On**: Ensure motor is turned OFF after 5-second cycle.
*   **Oscillation**: If fan cycles rapidly on/off, add hysteresis (turn on at 30°C, turn off only when below 28°C).
*   **Wrong Driver**: Verify motor driver wiring matches GP14/GP15 configuration.

### 1️⃣2️⃣ Try This Next

*   **Variable Speed**: Use temperature to set fan speed (higher temp = higher PWM duty).
*   **Hysteresis**: Implement 2-degree deadband to reduce cycling.
*   **PID Control**: Advanced: implement proportional control for smoother regulation.

---

## 1️⃣ Project 0335: Interactive Temperature Alarm

### 2️⃣ Learning Objective
Detect dangerous heat conditions using multiple sensor inputs (temperature and humidity). You will learn multi-variate condition checking and how environmental factors combine.

### 3️⃣ Concepts Introduced
*   **Multi-Variate Conditions**: Using AND logic with multiple sensors.
*   **Heat Index**: Combined temperature-humidity danger assessment.
*   **DHT11 Sensor**: Reading both temp and humidity from one device.

### 4️⃣ Hardware Required
*   **Pico**
*   **DHT11 Sensor** (temp + humidity)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT11 Data** | GP16 | Requires pull-up resistor (4.7kΩ) |
| **Buzzer** | GP15 | Alarm output |

### 6️⃣ Blocks Used

🔹 **Setup DHT Sensor**
*   **Category:** Sensors

🔹 **Read DHT**
*   **Category:** Sensors
*   **Block:** `read DHT sensor → returns [temp, humidity]`

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **temp, humidity**: Sensor readings.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup DHT11 (GP16).
    *   Setup buzzer (GP15).

*   **B. Main Loop Phase**
    *   Read DHT11 → temp, humidity.
    *   If temp > 30°C AND humidity > 70%:
        *   Buzzer ON.
        *   Print "DANGER: High Heat Index!".
    *   Else:
        *   Buzzer OFF.
    *   Sleep 2 seconds.

### 9️⃣ Execution Flow (Plain English)

System reads both temperature and humidity from DHT11. High temperature alone isn't alarming, nor is high humidity alone. But when BOTH exceed thresholds (>30°C AND >70% humidity), the combination creates dangerous "feels-like" heat, triggering alarm. This teaches multi-sensor correlation for safety systems.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import dht

sensor = dht.DHT11(machine.Pin(16))
buzzer = machine.Pin(15, machine.Pin.OUT)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        
        if temp > 30 and humidity > 70:
            buzzer.on()
            print(f"DANGER: High Heat Index! T:{temp}°C H:{humidity}%")
        else:
            buzzer.off()
            print(f"OK - T:{temp}°C H:{humidity}%")
    except OSError as e:
        print(f"DHT read error: {e}")
    
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **DHT Read Failures**: DHT11 can be finicky. Always wrap reads in try/except and allow 2+ second delays between reads.
*   **False Negatives**: If alarm never triggers, verify thresholds match your environment. Adjust to 28°C/60% if needed.
*   **Always Alarming**: Check sensor is properly connected and readings are valid before comparing.

### 1️⃣2️⃣ Try This Next

*   **Heat Index Formula**: Calculate actual heat index using meteorological formula instead of simple AND logic.
*   **Three Levels**: Green (safe), Yellow (caution), Red (danger) with different buzzer patterns.
*   **Dew Point**: Calculate and display dew point as additional comfort metric.

---

## 1️⃣ Project 0336: Smart Temperature Alarm Switch

### 2️⃣ Learning Objective
Create a mood ring effect that smoothly transitions RGB LED color based on temperature. You will learn color interpolation and visual status mapping.

### 3️⃣ Concepts Introduced
*   **Color Interpolation**: Blending colors based on continuous value.
*   **Visual Status Mapping**: Using color as intuitive feedback.
*   **RGB Fading**: Smooth transitions between color states.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor**
*   **RGB LED** (common cathode)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP16 | Sensor pin |
| **Red Channel** | GP13 | Via 220Ω |
| **Green Channel** | GP14 | Via 220Ω |
| **Blue Channel** | GP15 | Via 220Ω |

### 6️⃣ Blocks Used

🔹 **Setup PWM (×3)**
*   **Category:** Outputs

🔹 **PWM Write**
*   **Category:** Pin Access

🔹 **Map Range**
*   **Category:** Math

### 7️⃣ Variables & State
*   **temp**: Temperature reading.
*   **r, g, b**: Calculated RGB values.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup temp sensor (GP16).
    *   Setup PWM on GP13/14/15.

*   **B. Main Loop Phase**
    *   Read temp.
    *   If temp < 20°C (Cold):
        *   Set RGB = (0, 0, 65535) Blue.
    *   Elif temp < 25°C (Cool):
        *   Interpolate Blue → Green.
    *   Elif temp < 30°C (Perfect):
        *   Set RGB = (0, 65535, 0) Green.
    *   Elif temp < 35°C (Warm):
        *   Interpolate Green → Red.
    *   Else (Hot):
        *   Set RGB = (65535, 0, 0) Red.
    *   Write RGB to PWM.
    *   Sleep 0.3s.

### 9️⃣ Execution Flow (Plain English)

LED color maps to temperature zones: blue for cold (<20°C), green for perfect (25-30°C), red for hot (>35°C). Between zones, color smoothly interpolates. For example, at 22.5°C (midpoint between 20-25), LED shows cyan (half blue, half green). This creates intuitive visual feedback where color immediately communicates temperature status.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

temp_sensor = machine.ADC(4)
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def map_color(temp):
    if temp < 20:
        return (0, 0, 65535)  # Blue
    elif temp < 25:
        # Blue → Green transition
        t = (temp - 20) / 5
        return (0, int(65535 * t), int(65535 * (1-t)))
    elif temp < 30:
        return (0, 65535, 0)  # Green
    elif temp < 35:
        # Green → Red transition
        t = (temp - 30) / 5
        return (int(65535 * t), int(65535 * (1-t)), 0)
    else:
        return (65535, 0, 0)  # Red

while True:
    reading = temp_sensor.read_u16()
    temp = 27 - (reading * 3.3 / 65535 - 0.706) / 0.001721
    
    r, g, b = map_color(temp)
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)
    
    time.sleep(0.3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Abrupt Color Changes**: If transitions aren't smooth, verify interpolation math and use fractional temperature values.
*   **Wrong Color for Temp**: Check map_color() ranges and RGB value calculations.
*   **Stuck Color**: Ensure temperature is actually changing and sensor reads are updating.

### 1️⃣2️⃣ Try This Next

*   **More Zones**: Add purple for freezing (<10°C) and orange for very hot (>40°C).
*   **Brightness Variation**: Also vary LED brightness with temperature for added dimension.
*   **Custom Palette**: Allow user to set preferred colors for each zone via potentiometers.

---

[Continuing with remaining 4 projects: 0337-0340...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_seven)

print("✅ Projects 0334-0336 appended")
print("⏳ Generating final 4 projects (0337-0340) to complete Batch 34...")
