# 📘 Pico 2500: Batch 26 - Night Light 2 (Projects 0251-0260)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Smart Lighting & Sensing Systems

---

## 1️⃣ Project 0251: Basic Auto-Night Light (LDR)

### 2️⃣ Learning Objective
Create a light that automatically turns on when it gets dark using an LDR (Light Dependent Resistor) sensor, introducing analog sensing.

### 3️⃣ Concepts Introduced
*   Analog Input (ADC)
*   Threshold Values
*   Sensors (LDR)
*   Conditional Output
*   Calibration

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   LDR (Light Dependent Resistor)
*   10kΩ Resistor (for voltage divider)
*   White LED
*   Breadboard & Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR Leg 1** | 3.3V | |
| **LDR Leg 2** | GP26 (ADC0) | Also connect to 10k resistor |
| **10k Resistor** | GND | Pull-down for LDR leg 2 |
| **White LED** | GP15 | With 220Ω resistor |

### 6️⃣ Blocks Used
🔹 **Read Analog**
*   **Category:** Smart IO
*   **Block:** `pico_adc_read` (GP26)

🔹 **Logic Comparison**
*   **Category:** Logic
*   **Block:** `if [sensor] < [threshold]`

### 7️⃣ Variables & State
*   **lightLevel**: Number (0-65535) - Raw sensor reading

### 8️⃣ Step-by-Step Guide
**A. Calibration**
1. Read ADC value from GP26 in a loop.
2. Print value to console.
3. Cover sensor with hand -> Note "Dark" value (e.g., 20000).
4. Shine light -> Note "Bright" value (e.g., 50000).
5. Pick a middle "Threshold" (e.g., 30000).

**B. Logic Implementation**
1. Read `lightLevel` from GP26.
2. If `lightLevel` < `THRESHOLD`:
   - Turn LED ON
3. Else:
   - Turn LED OFF
4. Wait 0.1s

### 9️⃣ Execution Flow (Plain English)
The LDR changes resistance based on light. The Pico reads this as a number. If the number drops below our "darkness line" (threshold), the Pico acts as a switch and turns on the LED. When the sun comes up (number goes up), it turns the light off.

### 🔟 Generated Code
```python
from machine import Pin, ADC
import time

ldr = ADC(Pin(26))
led = Pin(15, Pin.OUT)

# Adjust this based on your room's lighting
DARK_THRESHOLD = 30000 

print("Auto-Night Light Active")

while True:
    light_level = ldr.read_u16()
    # print(light_level) # Uncomment to calibrate
    
    if light_level < DARK_THRESHOLD:
        led.value(1) # Dark -> Light ON
    else:
        led.value(0) # Bright -> Light OFF
        
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Always On/Off**: Your Threshold is wrong. Use print() to check actual values.
*   **Flickering**: If light is right at threshold, it might flash. This needs "Hysteresis" (see advanced concepts).
*   **Wiring**: Forgot the 10k resistor? The LDR needs a voltage divider to work!

### 1️⃣2️⃣ Try This Next
*   **Reverse Logic**: Make a "Sun Alarm" that beeps when light hits it.
*   **Smoothing**: Average 10 readings to prevent flickering.

---

## 1️⃣ Project 0252: Gradual Brightness Fade (PWM)

### 2️⃣ Learning Objective
Use PWM to create a smooth fading effect instead of a harsh on/off switch, simulating premium lighting behavior.

### 3️⃣ Concepts Introduced
*   Pulse Width Modulation (PWM)
*   Duty Cycle
*   Loops for Transition
*   Smooth UI

### 4️⃣ Hardware Required
*   Pico, LED (GP15), LDR (as input)

### 8️⃣ Step-by-Step Guide
**Logic:**
Instead of `led.value(1)`, we map the darkness level directly to brightness.
1. Read Light Level (0-65535).
2. Calculate Brightness: `inverted_light = 65535 - light_level`.
3. Set PWM Duty Cycle = `inverted_light`.
   - The darker it gets, the brighter the LED glows.

### 10️⃣ Generated Code
```python
from machine import Pin, ADC, PWM
import time

ldr = ADC(Pin(26))
led = PWM(Pin(15))
led.freq(1000)

while True:
    light = ldr.read_u16()
    
    # Invert: Dark(low input) = Bright LED(high output)
    brightness = 65535 - light
    
    # Clamp values to avoid weirdness
    if brightness < 0: brightness = 0
    
    led.duty_u16(brightness)
    time.sleep(0.05)
```

---

## 1️⃣ Project 0253: Motion-Activated Light (PIR)

### 2️⃣ Learning Objective
Detect human presence using a PIR (Passive Infrared) sensor to trigger lighting only when needed.

### 3️⃣ Concepts Introduced
*   Digital Sensors (PIR)
*   Motion Detection
*   Timers / Timeouts
*   Energy Saving

### 4️⃣ Hardware Required
*   Pico
*   HC-SR501 or AM312 PIR Sensor
*   LED

### 5️⃣ Wiring / Interfaces
| PIR Sensor | Pico Pin |
| :--- | :--- |
| **VCC** | VBUS (5V) or 3.3V (Check model) |
| **GND** | GND |
| **OUT** | GP14 |

### 8️⃣ Step-by-Step Guide
**A. Init**
1. Setup PIR on GP14 (Input).
2. Setup LED on GP15 (Output).
**B. Loop**
1. If PIR reads HIGH (Motion):
   - Turn LED ON.
   - Print "Motion Detected!".
2. Else:
   - Turn LED OFF.

### 10️⃣ Generated Code
```python
from machine import Pin
import time

pir = Pin(14, Pin.IN)
led = Pin(15, Pin.OUT)

print("Motion Sensor Ready (Wait for stabilization...)")
time.sleep(2)

while True:
    if pir.value() == 1:
        led.value(1)
        print("Motion!")
    else:
        led.value(0)
    time.sleep(0.1)
```

### 11️⃣ Common Mistakes
*   **Sensitivity**: PIRs have adjustment pots. If it stays on, turn sensitivity down.
*   **Warmup**: PIRs need 30-60s to stabilize after power on.

---

## 1️⃣ Project 0254: RGB Color Temperature

### 2️⃣ Learning Objective
Use an RGB LED to simulate different lighting moods: Warm White (Relaxing) vs Cool White (Focus).

### 3️⃣ Concepts Introduced
*   Color Temperature (Kelvin)
*   Color Mixing
*   RGB Logic
*   Mood Lighting

### 4️⃣ Hardware
*   Common Anode/Cathode RGB LED
*   3x Resistors

### 10️⃣ Generated Code
```python
from machine import Pin, PWM

# Assuming Common Cathode
red = PWM(Pin(13))
grn = PWM(Pin(14))
blu = PWM(Pin(15))

for p in [red, grn, blu]: p.freq(1000)

def set_color(r, g, b):
    red.duty_u16(int(r * 65535 / 255))
    grn.duty_u16(int(g * 65535 / 255))
    blu.duty_u16(int(b * 65535 / 255))

print("Choose Mode:")
print("1. Warm (Candle)")
print("2. Cool (Daylight)")

# Warm White: High Red, Med Green, No Blue
set_color(255, 147, 41) 
time.sleep(2)

# Cool White: High Blue, High Green
set_color(201, 226, 255)
time.sleep(2)
```

---

## 1️⃣ Project 0255: Sunrise Simulation

### 2️⃣ Learning Objective
Gradually increase light intensity and shift color from red to white over a set time period (Wake-up Light).

### 3️⃣ Concepts Introduced
*   Ramping Loops
*   Color Transition
*   Time-based Animation
*   Biological Clocks

### 10️⃣ Generated Code
```python
# Sunrise Animation
print("Sunrise starting...")

# 1. Dark Red -> Bright Orange -> Yellow -> White
for brightness in range(0, 65535, 500):
    # Ramps Red up first
    red.duty_u16(brightness)
    
    # Then brings in Green (to make Yellow)
    g_val = brightness - 20000
    if g_val < 0: g_val = 0
    grn.duty_u16(g_val)
    
    time.sleep(0.05) # Speed of sunrise
```

---

## 1️⃣ Project 0256: Presence Detection with Timeout

### 2️⃣ Learning Objective
Keep the light on for X seconds AFTER motion stops. This is how real room lights work.

### 3️⃣ Concepts Introduced
*   Latched State
*   Timer Reset
*   Countdown logic
*   Hysteretic Behavior

### 10️⃣ Generated Code
```python
TIMEOUT_SEC = 5
last_motion_time = 0

while True:
    if pir.value():
        last_motion_time = time.time()
        led.value(1) # Keep On
        
    # Check if timeout passed
    if time.time() - last_motion_time > TIMEOUT_SEC:
        led.value(0) # Turn Off
    else:
        led.value(1) # Stay On
        
    time.sleep(0.1)
```

---

## 1️⃣ Project 0257: Adjustable Brightness (Potentiometer)

### 2️⃣ Learning Objective
Manually dim the LED string using a potentiometer knob.

### 10️⃣ Generated Code
```python
pot = ADC(Pin(27))
# ... (PWM setup)

while True:
    val = pot.read_u16()
    # Logarithmic perception correction (optional squared)
    led.duty_u16(val)
    time.sleep(0.05)
```

---

## 1️⃣ Project 0258: Emergency Backup Mode

### 2️⃣ Learning Objective
Detect "Mains Power Loss" (simulated by a switch or pin) and activate a battery-powered emergency light.

### 10️⃣ Generated Code
```python
mains_power = Pin(10, Pin.IN, Pin.PULL_DOWN)
emergency_led = Pin(11, Pin.OUT)

while True:
    if mains_power.value() == 0:
        # Power Failure!
        emergency_led.value(1)
        print("POWER CUT - BACKUP ON")
    else:
        emergency_led.value(0)
```

---

## 1️⃣ Project 0259: Multi-Room Coordination

### 2️⃣ Learning Objective
Link sensing in one area to action in another (e.g., Hallway sensor turns on Bedroom light).

### 3️⃣ Concepts Introduced
*   Remote Triggers
*   System Logic
*   Wired Communication (GPIO Handshake)

### 10️⃣ Generated Code
```python
# Pin connected to another Pico
remote_trigger = Pin(3, Pin.IN) 

while True:
    if remote_trigger.value() or pir.value():
        led.value(1)
    else:
        led.value(0)
```

---

## 1️⃣ Project 0260: Master Smart Lighting System

### 2️⃣ Learning Objective
Integrate Auto-Brightness, Motion-Sensing, Manual Override, and Color Temp into one lamp.

### 3️⃣ Features
1. **Auto Mode:** LDR checks darkness + PIR checks motion.
2. **Manual Mode:** Potentiometer sets brightness.
3. **RGB Mode:** Button cycles colors.

### 10️⃣ Generated Code
```python
# Pseudo-State Machine
mode = "AUTO"

if mode == "AUTO":
    if ldr.read_u16() < DARK and pir.value():
        led.on()
elif mode == "MANUAL":
    led.duty_u16(pot.read_u16())
```

---

**Batch 26 Complete & Fixed.**
