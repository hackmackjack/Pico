# Complete Kitchen Timer 2: Projects 0388-0390 (CORRECT versions)

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

final_kitchen_timer = r'''
## 1️⃣ Project 0388: The Kitchen Timer Game

### 2️⃣ Learning Objective
Create an interactive game where the user must stop the timer when water reaches boiling point. You will learn about temperature-based event detection and user reaction timing.

### 3️⃣ Concepts Introduced
*   **Phase Change Detection**: Detecting when water reaches 100°C.
*   **Interactive Challenge**: User must press button at the exact right moment.
*   **Temperature Monitoring**: Real-time sensor reading and threshold detection.

### 4️⃣ Hardware Required
*   **Pico**
*   **Temperature Sensor** (DS18B20 or simulated with potentiometer)
*   **Button** (Stop Timer)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP15 | OneWire or ADC |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Read Temperature**
*   **Category:** Sensors

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Logic Comparison**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **currentTemp**: Temperature reading.
*   **timerRunning**: Boolean flag.
*   **perfectStop**: Boolean for success detection.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup Temperature Sensor on pin:[15]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.
    *   From **Variables**, drag `set [timerRunning] to [True]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Read Temperature**:
        *   From **Sensors**, drag `set [currentTemp] to [read temperature sensor]`.
            *   **Snap** into loop.
        *   From **Console**, drag `print [Water temp: {currentTemp}°C]`.
            *   **Snap** below.
    *   **Button Check**:
        *   From **Logic**, drag `if [digital read pin 14] AND [timerRunning] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Logic**, drag `if [currentTemp] >= [99] AND [currentTemp] <= [101] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Console**, drag `print [PERFECT! You stopped exactly at boiling!]`.
                            *   **Snap** inside.
                        *   From **Variables**, drag `set [perfectStop] to [True]`.
                            *   **Snap** below.
                *   From **Logic**, drag `else`.
                    *   Inside:
                        *   From **Console**, drag `print [Too early/late! Temp was {currentTemp}°C]`.
                *   From **Variables**, drag `set [timerRunning] to [False]`.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program monitors water temperature in real-time. The challenge: press the button when the temp is exactly 100°C (±1°C tolerance). If you press too early (e.g., 85°C) or too late (e.g., 105°C), you lose. Success requires watching the temperature closely and timing the button press perfectly at the boiling point.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ds18x20 import DS18X20
from onewire import OneWire

ow = OneWire(machine.Pin(15))
ds = DS18X20(ow)
roms = ds.scan()
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

timer_running = True
perfect_stop = False

while timer_running:
    ds.convert_temp()
    time.sleep_ms(750)
    current_temp = ds.read_temp(roms[0])
    
    print(f"Water temp: {current_temp:.1f}°C")
    
    if button.value():
        if 99 <= current_temp <= 101:
            print("PERFECT! You stopped exactly at boiling!")
            perfect_stop = True
        else:
            print(f"Too early/late! Temp was {current_temp:.1f}°C")
        timer_running = False
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Temperature Never Reaches 100**: If simulating with a pot, ensure sensor is waterproof and submerged.
*   **Button Misses Window**: The 99-101°C window might be too narrow. Expand to 98-102°C for easier gameplay.

### 1️⃣2️⃣ Try This Next

*   **Score System**: Award points based on how close to 100°C you were (100 points for perfect, -1 point per degree off).
*   **Multiple Rounds**: Play 3 rounds and calculate average accuracy.

---

## 1️⃣ Project 0389: Automated Kitchen Timer

### 2️⃣ Learning Objective
Create an automated tea brewing system using a servo to dip the tea bag rhythmically. You will learn about electromechanical automation and timed servo sequences.

### 3️⃣ Concepts Introduced
*   **Electromechanical Automation**: Coordinating timer logic with physical movement.
*   **Servo Sequencing**: Moving servo to specific positions at timed intervals.
*   **Recipe Automation**: Automating multi-step physical processes.

### 4️⃣ Hardware Required
*   **Pico**
*   **Servo Motor**
*   **Timer Display** (optional OLED)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo Signal** | GP15 | PWM |
| **Servo Power** | VSYS | 5V capable |
| **Servo Ground** | GND | |

### 6️⃣ Blocks Used

🔹 **Servo Control**
*   **Category:** Actuators

🔹 **Timing Functions**
*   **Category:** Timing

🔹 **Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **timeLeft**: Remaining brew time (e.g., 180 seconds).
*   **dipInterval**: Seconds between dips (5s).
*   **lastDipTime**: Timestamp of last dip.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Actuators**, drag `Setup Servo on pin:[15]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [timeLeft] to [180]`.
        *   **Snap** below (3 minutes).
    *   From **Variables**, drag `set [dipInterval] to [5]`.
        *   **Snap** below.
    *   From **Actuators**, drag `Servo [15] angle:[90]`.
        *   **Snap** below (initial down position - bag in water).

*   **B. Main Loop Phase**
    *   **Dipping Motion**:
        *   From **Logic**, drag `if [timeLeft] % [dipInterval] = [0] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Actuators**, drag `Servo [15] angle:[0]`.
                    *   **Snap** inside (lift bag up).
                *   From **Timing**, drag `sleep [1] seconds`.
                    *   **Snap** below.
                *   From **Actuators**, drag `Servo [15] angle:[90]`.
                    *   **Snap** below (dip bag down).
    *   **Countdown**:
        *   From **Variables**, drag `change [timeLeft] by [-1]`.
            *   **Snap** below.
        *   From **Console**, drag `print [Brew time: {timeLeft}s]`.
            *   **Snap** below.
    *   **Finish**:
        *   From **Logic**, drag `if [timeLeft] <= [0] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Actuators**, drag `Servo [15] angle:[0]`.
                    *   **Snap** inside (lift bag out completely).
                *   From **Console**, drag `print [Tea ready! Bag removed.]`.
                    *   **Snap** below.
                *   `break` or stop.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The servo starts with the tea bag submerged (90° position). Every 5 seconds, it lifts the bag up (0°) for 1 second, then dips it back down (90°). This continues for 3 minutes. When the timer expires, the servo lifts the bag to 0° and holds it there, removing the tea bag from the water. The entire brewing process is automated.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int((angle / 180) * 1023 + 512)
    servo.duty(duty)

time_left = 180
dip_interval = 5

set_angle(90)  # Start with bag in water

while time_left > 0:
    # Dip every 5 seconds
    if time_left % dip_interval == 0:
        set_angle(0)   # Lift up
        time.sleep(1)
        set_angle(90)  # Dip down
    
    time_left -= 1
    print(f"Brew time: {time_left}s")
    time.sleep(1)

# Finish - remove bag
set_angle(0)
print("Tea ready! Bag removed.")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Servo Jitters**: PWM frequency must be 50Hz for standard servos. Verify with `servo.freq(50)`.
*   **Arm Falls**: Ensure servo has enough power. Weak servos may not hold position under load.

### 1️⃣2️⃣ Try This Next

*   **Variable Dip Speed**: Dip faster in the first minute (every 3s), slower in the last minute (every 10s).
*   **Manual Override**: Add a button to lift the bag early if tea is strong enough.

---

## 1️⃣ Project 0390: Mastering Kitchen Timer

### 2️⃣ Learning Objective
Implement a preset memory system for storing favorite timer durations. You will learn about menu navigation and state persistence in variables.

### 3️⃣ Concepts Introduced
*   **Preset Memory**: Storing multiple timer options in variables.
*   **Menu Selection Logic**: Cycling through options with button presses.
*   **State Persistence**: Maintaining selected presets across multiple uses.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Cycle Presets)
*   **OLED Display** (to show preset names)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Select Button** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |

### 6️⃣ Blocks Used

🔹 **Variables (Lists)**
*   **Category:** Variables

🔹 **Modulo Arithmetic**
*   **Category:** Math

🔹 **OLED Text**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **presets**: List of preset names: `["Soft Boiled", "Medium", "Hard"]`.
*   **presetTimes**: List of durations: `[240, 360, 600]` (4m, 6m, 10m in seconds).
*   **selectedIndex**: Currently selected preset (0, 1, or 2).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** below.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.
    *   From **Variables**, drag `set [presets] to [["Soft Boiled", "Medium", "Hard"]]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [presetTimes] to [[240, 360, 600]]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [selectedIndex] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button Cycle**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Math**, drag `set [selectedIndex] to [(selectedIndex + 1) % 3]`.
                    *   **Snap** inside (cycle through 0, 1, 2).
                *   From **Timing**, drag `sleep [0.5] seconds`.
                    *   **Snap** below (debounce).
    *   **Display Current Preset**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text [Preset: {presets[selectedIndex]}]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text [Time: {presetTimes[selectedIndex] / 60}min]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The screen displays "Preset: Soft Boiled - Time: 4min". Each button press cycles to the next preset: Medium (6min), then Hard (10min), then back to Soft Boiled. The modulo operator ensures the index wraps around (0→1→2→0). This allows quick selection of predefined egg-cooking times without typing or adjusting dials.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

presets = ["Soft Boiled", "Medium", "Hard"]
preset_times = [240, 360, 600]  # 4m, 6m, 10m in seconds
selected_index = 0

while True:
    if button.value():
        selected_index = (selected_index + 1) % 3
        time.sleep(0.5)  # Debounce
    
    oled.fill(0)
    oled.text(f"Preset:", 0, 0)
    oled.text(presets[selected_index], 0, 15)
    oled.text(f"Time: {preset_times[selected_index] // 60}min", 0, 30)
    oled.show()
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Index Out of Range**: If adding a 4th preset, change `% 3` to `% 4`.
*   **Display Doesn't Update**: Ensure `oled.show()` is called after every text change.

### 1️⃣2️⃣ Try This Next

*   **Edit Mode**: Hold button for 3s to enter edit mode and adjust preset times with +/- buttons.
*   **Save to Flash**: Use file I/O to save custom preset times so they persist across reboots.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(final_kitchen_timer)

print("✅ Generated Projects 0388-0390 (Kitchen Timer 2 - COMPLETE)")
print("📋 Now generating Batch 40: Metronome 2 (Projects 0391-0400)...")
