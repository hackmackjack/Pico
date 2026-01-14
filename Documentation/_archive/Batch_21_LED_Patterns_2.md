# 📘 Pico 2500: Documentation (Projects 0201-0300)

## 🏁 Batch 21: LED Patterns 2 (0201-0210)

## 1️⃣ Project 0201: Introduction to LED Patterns (Level 2)

### 2️⃣ Learning Objective
Learn to create dynamic LED patterns using variables to control timing and sequences, building on basic GPIO control from Batch 1.

### 3️⃣ Concepts Introduced
*   Variable-Controlled Timing
*   Pattern Sequencing
*   Multi-LED Coordination
*   Loop-Based Animation
*   Speed Control Variables

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red on GP15, Yellow on GP16, Green on GP17, Blue on GP18)
*   4x 220Ω Resistors
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground Rail |

### 6️⃣ Blocks Used
🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [speed] to [0.3]`

🔹 **Forever Loop**
*   **Category:** Loops
*   **Block:** `forever do`

🔹 **Repeat Loop**
*   **Category:** Loops
*   **Block:** `repeat [4] times`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH (1)]`

🔹 **Wait**
*   **Category:** Smart IO
*   **Block:** `wait [speed] [seconds]`

🔹 **Print**
*   **Category:** Smart IO
*   **Block:** `log/print [message]`

### 7️⃣ Variables & State
*   **speed**: Number (seconds) - Controls animation speed (default 0.3s)
*   **pattern**: String - Current pattern name (e.g., "wave", "chase", "blink")
*   **ledPins**: List - Array of LED pin numbers [15, 16, 17, 18]

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create variable `speed` and set to `0.3`
    *   **Snap** it into the start block.
2. From **Smart IO**, drag `log/print ["LED Pattern Demo - Level 2"]`
    *   **Snap** it below the previous block.

**B. Main Loop Phase**
1. From **Loops**, drag `forever do`
    *   **Snap** it into the workspace.

2. **Pattern 1: Wave Right → **
   *   From **Smart IO**, drag `log/print ["Pattern: Wave →"]`
       *   **Snap** it inside the forever loop.
   *   From **Smart IO**, drag `set Pin [15] to [HIGH (1)]`
       *   **Snap** it below the previous block.
   *   From **Smart IO**, drag `wait [speed] [seconds]`
       *   **Snap** the `speed` variable into the wait block.
       *   **Snap** it below the previous block.
   *   From **Smart IO**, drag `set Pin [15] to [LOW (0)]`
       *   **Snap** it below the previous block.
   *   Repeat for GP16, GP17, GP18 (Yellow, Green, Blue)

3. **Pattern 2: Wave Left ←**
   *   From **Smart IO**, drag `log/print ["Pattern: Wave ←"]`
       *   **Snap** it below the previous pattern.
   *   Repeat the wave pattern but in reverse order (GP18 → GP17 → GP16 → GP15)

4. **Pattern 3: Alternating Pairs**
   *   From **Smart IO**, drag `log/print ["Pattern: Alternating"]`
       *   **Snap** it below the previous pattern.
   *   From **Loops**, drag `repeat [3] times`
       *   **Snap** it below the previous block.
   *   Inside the repeat block:
       *   Turn GP15 (Red) + GP17 (Green) ON
       *   Turn GP16 (Yellow) + GP18 (Blue) OFF
       *   Wait `speed` seconds
       *   Turn GP15 + GP17 OFF
       *   Turn GP16 + GP18 ON
       *   Wait `speed` seconds

5. **Pattern 4: All Blink**
   *   From **Smart IO**, drag `log/print ["Pattern: All Blink"]`
       *   **Snap** it below the previous pattern.
   *   From **Loops**, drag `repeat [3] times`
       *   **Snap** it below the previous block.
   *   Inside the repeat block:
       *   Turn ALL LEDs (GP15-18) ON
       *   Wait `speed` seconds
       *   Turn ALL LEDs OFF
       *   Wait `speed` seconds

**C. Event / Condition Handling**
*   None (automatic pattern cycling)

### 9️⃣ Execution Flow (Plain English)
The program creates four distinct LED patterns that repeat continuously. Unlike Batch 1 projects that used fixed timing, this project introduces a `speed` variable that controls all animation timing from one place. This makes it easy to speed up or slow down the entire show without changing every delay value.

The wave patterns create a "traveling light" effect by turning LEDs on and off in sequence. The alternating pattern splits the LEDs into two groups that blink opposite to each other. The final pattern flashes all LEDs together. After completing all four patterns, the cycle repeats forever.

**Key Advancement from Batch 1:** Using variables for timing control demonstrates how to make code more flexible and maintainable.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

# LED Pin Setup
led_red = Pin(15, Pin.OUT)
led_yellow = Pin(16, Pin.OUT)
led_green = Pin(17, Pin.OUT)
led_blue = Pin(18, Pin.OUT)

# Control Variables
speed = 0.3  # Seconds per animation step
led_pins = [15, 16, 17, 18]

print("LED Pattern Demo - Level 2")
print(f"Speed: {speed}s per step")

while True:
    # Pattern 1: Wave Right
    print("Pattern: Wave →")
    for pin in [15, 16, 17, 18]:
        Pin(pin, Pin.OUT).value(1)
        time.sleep(speed)
        Pin(pin, Pin.OUT).value(0)
    time.sleep(speed)
    
    # Pattern 2: Wave Left
    print("Pattern: Wave ←")
    for pin in [18, 17, 16, 15]:
        Pin(pin, Pin.OUT).value(1)
        time.sleep(speed)
        Pin(pin, Pin.OUT).value(0)
    time.sleep(speed)
    
    # Pattern 3: Alternating Pairs
    print("Pattern: Alternating")
    for _ in range(3):
        led_red.value(1)
        led_green.value(1)
        led_yellow.value(0)
        led_blue.value(0)
        time.sleep(speed)
        
        led_red.value(0)
        led_green.value(0)
        led_yellow.value(1)
        led_blue.value(1)
        time.sleep(speed)
    
    # All OFF between patterns
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(0)
    led_blue.value(0)
    time.sleep(speed)
    
    # Pattern 4: All Blink
    print("Pattern: All Blink")
    for _ in range(3):
        led_red.value(1)
        led_yellow.value(1)
        led_green.value(1)
        led_blue.value(1)
        time.sleep(speed)
        
        led_red.value(0)
        led_yellow.value(0)
        led_green.value(0)
        led_blue.value(0)
        time.sleep(speed)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Forgetting to Turn LEDs OFF**: Each pattern should clean up by turning all LEDs off before the next pattern starts, otherwise you'll get mixed patterns.
*   **Mixed Pin Numbers**: Ensure GP15-18 are used consistently; don't confuse with physical pin numbers (GP15 is physical pin 20).
*   **Speed = 0**: Setting speed to 0 causes instant transitions (invisible to human eye). Use at least 0.05s.
*   **Current Limit**: Running all 4 LEDs at once may draw ~80mA total; ensure adequate power supply.
*   **Breadboard Connections**: Check common ground rail is properly connected to Pico GND.

### 1️⃣2️⃣ Try This Next
*   **Speed Control Button**: Add a button on GP14 that cycles between slow (0.5s), medium (0.3s), and fast (0.1s) speeds.
*   **Random Colors**: Use `random.choice([15,16,17,18])` to light random LEDs instead of patterns.
*   **Knight Rider Effect**: Create a bouncing back-and-forth pattern with a "tail" effect (multiple LEDs on at once).
*   **Binary Counter**: Display numbers 0-15 in binary using the 4 LEDs (15=1111, 10=1010, etc.).
*   **Music Sync**: Flash LEDs in rhythm to a simple melody from the buzzer.
*   **POV Display**: Speed up to create persistence-of-vision text/shapes when waved rapidly.

---

## 1️⃣ Project 0202: Button Pattern Selector

### 2️⃣ Learning Objective
Add interactive control to LED patterns by using a button to cycle through different animation modes.

### 3️⃣ Concepts Introduced
*   User Input Integration
*   Mode Selection Logic
*   State Variables
*   Conditional Pattern Execution
*   Button Debouncing

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red GP15, Yellow GP16, Green GP17, Blue GP18)
*   4x 220Ω Resistors
*   Pushbutton (GP14)
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground Rail |
| **Button Terminal 1** | GP14 | Internal pull-down enabled |
| **Button Terminal 2** | 3.3V | Power rail |

### 6️⃣ Blocks Used
🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [pattern] to [1]`

🔹 **Read Digital Pin**
*   **Category:** Smart IO
*   **Block:** `read [Digital] Pin [14]`

🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `if [Button Pressed] then...`

🔹 **Change Variable**
*   **Category:** Variables
*   **Block:** `change [pattern] by [1]`

🔹 **Comparison**
*   **Category:** Logic
*   **Block:** `[pattern] > [4]`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH (1)]`

### 7️⃣ Variables & State
*   **pattern**: Number (1-4) - Current pattern mode selected
*   **speed**: Number (0.3s) - Animation timing constant
*   **lastButtonState**: Boolean - Prevents multiple triggers

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create variable `pattern` and set to `1`
    *   **Snap** it into the start block.
2. From **Variables**, create variable `speed` and set to `0.3`
    *   **Snap** it below the previous block.
3. From **Smart IO**, drag `log/print ["Press button to change pattern"]`
    *   **Snap** it below the previous block.

**B. Main Loop Phase**
1. From **Loops**, drag `forever do`
    *   **Snap** it into the workspace.

2. **Button Check Section:**
   *   From **Logic**, drag `if [condition] then`
       *   **Snap** it inside the forever loop.
   *   From **Smart IO**, drag `read [Digital] Pin [14]`
       *   **Snap** into the if condition.
   *   Inside the if block:
       *   From **Variables**, drag `change [pattern] by [1]`
           *   **Snap** it inside.
       *   From **Logic**, drag nested `if [pattern] > [4]`
           *   **Snap** it below previous block.
       *   Inside nested if: `set [pattern] to [1]` (wrap around)
       *   From **Smart IO**, drag `log/print` with joined text "Pattern: " + pattern
           *   **Snap** it below.
       *   From **Smart IO**, drag `wait [0.3] [seconds]` (debounce)
           *   **Snap** it below.

3. **Pattern Execution Section:**
   *   From **Logic**, drag `if [pattern] = [1]` with multiple else-if
       *   **Snap** it below button check.
   *   **If pattern = 1:** Execute Wave Right code (from 0201)
   *   **Else if pattern = 2:** Execute Wave Left code
   *   **Else if pattern = 3:** Execute Alternating code
   *   **Else if pattern = 4:** Execute All Blink code

**C. Event / Condition Handling**
*   Button press increments pattern number
*   Pattern wraps from 4 back to 1
*   Each pattern executes based on current mode

### 9️⃣ Execution Flow (Plain English)
The program starts in Pattern 1 (Wave Right). When you press the button, it increments to Pattern 2, then 3, then 4, then wraps back to 1. Each pattern runs continuously until you press the button again. The debounce delay prevents accidental double-presses.

This project demonstrates **state-based programming** where the same hardware performs different actions based on a mode variable. This is fundamental to building interactive systems.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

# Hardware Setup
led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Control Variables
pattern = 1
speed = 0.3

print("Press button to change pattern")

def wave_right():
    for led in led_pins:
        led.value(1)
        time.sleep(speed)
        led.value(0)

def wave_left():
    for led in reversed(led_pins):
        led.value(1)
        time.sleep(speed)
        led.value(0)

def alternating():
    for _ in range(3):
        led_pins[0].value(1)  # Red
        led_pins[2].value(1)  # Green
        led_pins[1].value(0)  # Yellow
        led_pins[3].value(0)  # Blue
        time.sleep(speed)
        
        led_pins[0].value(0)
        led_pins[2].value(0)
        led_pins[1].value(1)
        led_pins[3].value(1)
        time.sleep(speed)
    
    # All off
    for led in led_pins:
        led.value(0)

def all_blink():
    for _ in range(3):
        for led in led_pins:
            led.value(1)
        time.sleep(speed)
        for led in led_pins:
            led.value(0)
        time.sleep(speed)

while True:
    # Check button
    if btn.value() == 1:
        pattern += 1
        if pattern > 4:
            pattern = 1
        print(f"Pattern: {pattern}")
        time.sleep(0.3)  # Debounce
    
    # Execute current pattern
    if pattern == 1:
        wave_right()
    elif pattern == 2:
        wave_left()
    elif pattern == 3:
        alternating()
    elif pattern == 4:
        all_blink()
    
    time.sleep(0.01)  # Small delay
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Pull Resistor**: Button will give random values - enable `PULL_DOWN` mode.
*   **Pattern Never Changes**: Check button wiring and ensure it's connected to 3.3V.
*   **Multiple Triggers**: Without debounce delay, one press = multiple pattern changes.
*   **Stuck in Pattern**: If logic doesn't wrap (>4 check), pattern number keeps growing.
*   **LEDs Stay On**: Ensure each pattern function turns LEDs off at completion.

### 1️⃣2️⃣ Try This Next
*   **Pattern Name Display**: Print pattern names ("Wave Right", "Alternating") instead of numbers.
*   **Two Buttons**: Add second button on GP13 to go backwards through patterns.
*   **Speed Toggle**: Long press changes speed, short press changes pattern.
*   **Random Mode**: Add Pattern 5 that randomly selects from patterns 1-4.
*   **LED Indicator**: Light specific LED to show current pattern number (1 LED = Pattern 1, etc.).

---

## 1️⃣ Project 0203: Speed Control with Potentiometer

### 2️⃣ Learning Objective
Use analog input to dynamically control animation speed, learning how to map sensor values to useful ranges.

### 3️⃣ Concepts Introduced
*   Analog to Digital Conversion (ADC)
*   Value Mapping (Range Conversion)
*   Real-Time Parameter Adjustment
*   Potentiometer Reading
*   Live Variable Updates

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red GP15, Yellow GP16, Green GP17, Blue GP18)
*   4x 220Ω Resistors
*   Potentiometer (10kΩ recommended)
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground Rail |
| **Pot Left Pin** | GND | Ground |
| **Pot Right Pin** | 3.3V | Power |
| **Pot Center Pin** | GP26 | ADC0 (Analog Input) |

### 6️⃣ Blocks Used
🔹 **Read Analog**
*   **Category:** Smart IO
*   **Block:** `read [Analog] Pin [26]`

🔹 **Map Range**
*   **Category:** Math
*   **Block:** `map [value] from [0-65535] to [0.05-1.0]`

🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [speed] to [mapped value]`

🔹 **Forever Loop**
*   **Category:** Loops
*   **Block:** `forever do`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH (1)]`

### 7️⃣ Variables & State
*   **potValue**: Number (0-65535) - Raw ADC reading
*   **speed**: Number (0.05-1.0 seconds) - Mapped animation speed
*   **minSpeed**: Constant (0.05s) - Fastest animation
*   **maxSpeed**: Constant (1.0s) - Slowest animation

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create `minSpeed` and set to `0.05`
    *   **Snap** it into the start block.
2. From **Variables**, create `maxSpeed` and set to `1.0`
    *   **Snap** it below the previous block.
3. From **Smart IO**, drag `log/print ["Turn knob to adjust speed"]`
    *   **Snap** it below the previous block.

**B. Main Loop Phase**
1. From **Loops**, drag `forever do`
    *   **Snap** it into the workspace.

2. **Read and Map Speed:**
   *   From **Smart IO**, drag `read [Analog] Pin [26]`
       *   Store result in `potValue` variable
       *   **Snap** it inside the forever loop.
   *   From **Math**, drag `map [potValue] from [0] to [65535] to [minSpeed] to [maxSpeed]`
       *   Store result in `speed` variable
       *   **Snap** it below the previous block.

3. **Pattern Execution (Wave Right):**
   *   From **Smart IO**, drag `set Pin [15] to [HIGH]`
       *   **Snap** it below the mapping.
   *   From **Smart IO**, drag `wait [speed] [seconds]`
       *   Use the `speed` variable calculated above
       *   **Snap** it below.
   *   From **Smart IO**, drag `set Pin [15] to [LOW]`
       *   **Snap** it below.
   *   Repeat for GP16, GP17, GP18

**C. Event / Condition Handling**
*   Potentiometer continuously updates speed variable
*   Speed changes take effect immediately on next LED transition
*   No button needed - real-time analog control

### 9️⃣ Execution Flow (Plain English)
The potentiometer acts as a voltage divider. Turning it clockwise increases voltage on GP26, which the ADC reads as a higher number (0-65535). We convert this raw number to a useful time range (0.05s to 1.0s). When the knob is fully left, the pattern is very fast (0.05s per step). Fully right = very slow (1.0s per step).

This demonstrates **analog input mapping** - taking raw sensor data and converting it to meaningful control parameters. This technique is used in thermostats, volume controls, and flight simulators.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

# Hardware Setup
led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
pot = ADC(26)

# Speed Range Constants
MIN_SPEED = 0.05  # Fastest (50ms)
MAX_SPEED = 1.0   # Slowest (1 second)

print("Turn knob to adjust speed")

def map_value(value, in_min, in_max, out_min, out_max):
    """Map value from one range to another"""
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    # Read potentiometer and map to speed range
    pot_value = pot.read_u16()
    speed = map_value(pot_value, 0, 65535, MIN_SPEED, MAX_SPEED)
    
    # Execute wave right pattern with dynamic speed
    for led in led_pins:
        led.value(1)
        time.sleep(speed)
        led.value(0)
    
    # Optional: Print current speed for debugging
    # print(f"Speed: {speed:.2f}s (Pot: {pot_value})")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wrong Pin**: Only GP26, GP27, GP28 support analog input - GP15 won't work!
*   **Floating Values**: If speed jumps randomly when not touching knob, ensure pot's outer pins connect to GND and 3.3V.
*   **Inverted Control**: If clockwise = slower instead of faster, swap the min/max in the map function.
*   **Too Fast/Slow**: Adjust MIN_SPEED and MAX_SPEED constants to your preference.
*   **Pot Wiring**: Left-Center-Right pins must be GND-Signal-3.3V (check pot marking).

### 1️⃣2️⃣ Try This Next
*   **Speed Display**: Add LCD to show current speed value in milliseconds.
*   **Non-Linear Mapping**: Use `speed²` for exponential feel (slow speeds more precise).
*   **Dual Control**: Add button from 0202 to change pattern + pot to change speed.
*   **Speed Memory**: Sample pot value every 2s instead of every loop (smoother).
*   **Visual Indicator**: Blink onboard LED (GP25) at current speed setting.
*   **Calibration Mode**: Press button to set current pot position as "default speed".

---

## 1️⃣ Project 0204: Light-Reactive LED Patterns

### 2️⃣ Learning Objective
Create patterns that automatically respond to ambient light using an LDR sensor, introducing environmental sensing.

### 3️⃣ Concepts Introduced
*   Light Dependent Resistor (LDR)
*   Environmental Sensing
*   Threshold-Based Logic
*   Auto-Brightness Adjustment
*   Sensor-Driven Behavior

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red GP15, Yellow GP16, Green GP17, Blue GP18)
*   4x 220Ω Resistors
*   LDR (Light Dependent Resistor)
*   10kΩ Resistor (for voltage divider)
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground |
| **LDR One Terminal** | 3.3V | Power |
| **LDR Other Terminal** | GP27 + 10kΩ to GND | Voltage divider circuit |
| **10kΩ Resistor** | GP27 to GND | Pull-down resistor |

### 6️⃣ Blocks Used
🔹 **Read Analog**
*   **Category:** Smart IO
*   **Block:** `read [Analog] Pin [27]`

🔹 **Comparison**
*   **Category:** Logic
*   **Block:** `[lightLevel] < [threshold]`

🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `if [dark] then... else...`

🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [threshold] to [30000]`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH (1)]`

### 7️⃣ Variables & State
*   **lightLevel**: Number (0-65535) - Current ambient light reading
*   **DARK_THRESHOLD**: Constant (30000) - Below this = dark
*   **BRIGHT_THRESHOLD**: Constant (50000) - Above this = bright
*   **isDark**: Boolean - True when light level < threshold
*   **currentMode**: String - "Night" or "Day" mode

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create `DARK_THRESHOLD` and set to `30000`
    *   **Snap** it into the start block.
2. From **Variables**, create `BRIGHT_THRESHOLD` and set to `50000`
    *   **Snap** it below the previous block.
3. From **Variables**, create `currentMode` and set to `"Auto"`
    *   **Snap** it below the previous block.
4. From **Smart IO**, drag `log/print ["Light-reactive mode active"]`
    *   **Snap** it below.

**B. Main Loop Phase**
1. From **Loops**, drag `forever do`
    *   **Snap** it into the workspace.

2. **Read Light Sensor:**
   *   From **Smart IO**, drag `read [Analog] Pin [27]`
       *   Store in `lightLevel` variable
       *   **Snap** it inside forever loop.

3. **Determine Environment:**
   *   From **Logic**, drag `if [lightLevel] < [DARK_THRESHOLD]`
       *   **Snap** it below sensor read.
   *   Inside if (DARK mode):
       *   Set `currentMode` to "Night"
       *   Execute slow, calm pattern (All Blink, 0.5s speed)
       *   Print "Night Mode"
   *   From **Logic**, add `else if [lightLevel] > [BRIGHT_THRESHOLD]`
   *   Inside else-if (BRIGHT mode):
       *   Set `currentMode` to "Day"
       *   Execute fast, energetic pattern (Wave, 0.1s speed)
       *   Print "Day Mode"
   *   Else (MEDIUM light):
       *   Set `currentMode` to "Auto"
       *   Execute medium speed (0.3s)
       *   Print "Auto Mode"

**C. Event / Condition Handling**
*   Continuously monitors light level
*   Switches pattern speed based on ambient lighting
*   Creates "smart lighting" effect
*   No button needed - fully automatic

### 9️⃣ Execution Flow (Plain English)
The LDR's resistance changes with light. Bright light = low resistance = high voltage on GP27. Dark = high resistance = low voltage. The ADC reads this voltage as numbers: 0 (dark) to 65535 (bright).

When you cover the sensor (simulate night), the program detects low light and switches to slow, gentle patterns. When you shine a light on it (simulate day), it speeds up with energetic patterns. This creates an "ambient awareness" system.

**Real-world application:** Smart nightlights that only activate in darkness, or billboards that adjust brightness based on time of day.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

# Hardware Setup
led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
ldr = ADC(27)

# Light Thresholds
DARK_THRESHOLD = 30000   # Below this = Night mode
BRIGHT_THRESHOLD = 50000 # Above this = Day mode

print("Light-reactive mode active")

def slow_blink():
    """Calm pattern for night"""
    for _ in range(2):
        for led in led_pins:
            led.value(1)
        time.sleep(0.5)
        for led in led_pins:
            led.value(0)
        time.sleep(0.5)

def fast_wave():
    """Energetic pattern for day"""
    for led in led_pins:
        led.value(1)
        time.sleep(0.1)
        led.value(0)

def medium_alternating():
    """Balanced pattern for auto"""
    led_pins[0].value(1)
    led_pins[2].value(1)
    time.sleep(0.3)
    led_pins[0].value(0)
    led_pins[2].value(0)
    led_pins[1].value(1)
    led_pins[3].value(1)
    time.sleep(0.3)
    led_pins[1].value(0)
    led_pins[3].value(0)

while True:
    # Read ambient light level
    light_level = ldr.read_u16()
    
    # Determine mode and execute appropriate pattern
    if light_level < DARK_THRESHOLD:
        # DARK - Night mode
        print(f"Night Mode (Light: {light_level})")
        slow_blink()
    elif light_level > BRIGHT_THRESHOLD:
        # BRIGHT - Day mode
        print(f"Day Mode (Light: {light_level})")
        fast_wave()
    else:
        # MEDIUM - Auto mode
        print(f"Auto Mode (Light: {light_level})")
        medium_alternating()
    
    time.sleep(0.1)  # Small delay between checks
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Voltage Divider**: LDR alone won't work - must have 10kΩ resistor to ground creating voltage divider.
*   **Backwards Values**: If covering sensor makes it brighter, your LDR and resistor positions might be swapped.
*   **Threshold Too High/Low**: Room light ≈ 40000, darkness ≈ 10000, bright light ≈ 60000 - adjust thresholds for your environment.
*   **Flickering**: If rapidly switching modes, add hysteresis (different thresholds for on/off).
*   **Wrong Pin**: GP27 is ADC1 - don't use GP15 or other digital pins.
*   **LDR Type**: Different LDRs have different resistances; you may need to calibrate thresholds.

### 1️⃣2️⃣ Try This Next
*   **Calibration Button**: Press button to sample current light as "threshold" value.
*   **Gradual Transition**: Slowly fade speed instead of instant mode switch.
*   **Three Modes**: Add "Sunset" mode for mid-range light with orange LED emphasis.
*   **Data Logger**: Print light values to console every 5 seconds to find your room's ranges.
*   **PWM Brightness**: Use PWM to actually dim LEDs in dark mode (not just speed).
*   **Multi-Sensor**: Add temperature sensor - cold+dark = winter mode, hot+bright = summer mode.

---

## 1️⃣ Project 0205: Dual-Button Control (Pattern + Speed)

### 2️⃣ Learning Objective
Combine multiple input methods by using two buttons to independently control pattern selection and animation speed.

### 3️⃣ Concepts Introduced
*   Multi-Input Systems
*   Independent Control Channels
*   State Management with Multiple Variables
*   Separate Button Handlers
*   User Interface Design

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red GP15, Yellow GP16, Green GP17, Blue GP18)
*   4x 220Ω Resistors
*   2x Pushbuttons (GP14, GP13)
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground Rail |
| **Pattern Button** | GP14 | Internal pull-down, to 3.3V |
| **Speed Button** | GP13 | Internal pull-down, to 3.3V |

### 6️⃣ Blocks Used
🔹 **Read Digital Pin** (x2)
*   **Category:** Smart IO
*   **Block:** `read [Digital] Pin [14]` and `Pin [13]`

🔹 **Variables** (pattern, speedMode)
*   **Category:** Variables
*   **Block:** `set [pattern] to [1]`, `set [speedMode] to [2]`

🔹 **If/Else**
*   **Category:** Logic
*   **Block:** Multiple if blocks for button checking

🔹 **List**
*   **Category:** Lists
*   **Block:** `create list with [0.1] [0.3] [0.5]` (speed presets)

### 7️⃣ Variables & State
*   **pattern**: Number (1-4) - Current pattern mode
*   **speedMode**: Number (1-3) - Speed preset index (fast/medium/slow)
*   **speedList**: List - [0.1, 0.3, 0.5] speed values
*   **currentSpeed**: Number - Active speed from list

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create `pattern` = 1, `speedMode` = 2
2. From **Lists**, create `speedList` with items [0.1, 0.3, 0.5]
3. Print "Pattern Btn: GP14 | Speed Btn: GP13"

**B. Main Loop Phase**
1. **Pattern Button Check:**
   - If GP14 pressed: increment pattern, wraparound at 4
   - Print current pattern number
   - Debounce delay 0.3s

2. **Speed Button Check:**
   - If GP13 pressed: increment speedMode, wraparound at 3
   - Get speed from list: `speedList[speedMode-1]`
   - Print speed value
   - Debounce delay 0.3s

3. **Execute Pattern:**
   - Based on current pattern (1-4)
   - Using currentSpeed from speedList

**C. Event / Condition Handling**
*   Two independent button handlers
*   Pattern and speed can be changed anytime
*   Changes take effect immediately on next cycle

### 9️⃣ Execution Flow (Plain English)
This project demonstrates **multi-input control**. Button 1 controls WHAT pattern runs (wave/blink/etc). Button 2 controls HOW FAST it runs (slow/medium/fast). Each button has its own state variable and they work independently. This is how real products work - volume separate from channel selection.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
btn_pattern = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_speed = Pin(13, Pin.IN, Pin.PULL_DOWN)

pattern = 1
speed_mode = 2
speed_list = [0.1, 0.3, 0.5]
current_speed = speed_list[speed_mode - 1]

print("Pattern Btn: GP14 | Speed Btn: GP13")

def wave_right():
    for led in led_pins:
        led.value(1)
        time.sleep(current_speed)
        led.value(0)

def wave_left():
    for led in reversed(led_pins):
        led.value(1)
        time.sleep(current_speed)
        led.value(0)

def alternating():
    for _ in range(2):
        led_pins[0].value(1); led_pins[2].value(1)
        time.sleep(current_speed)
        led_pins[0].value(0); led_pins[2].value(0)
        led_pins[1].value(1); led_pins[3].value(1)
        time.sleep(current_speed)
        led_pins[1].value(0); led_pins[3].value(0)

def all_blink():
    for _ in range(2):
        for led in led_pins: led.value(1)
        time.sleep(current_speed)
        for led in led_pins: led.value(0)
        time.sleep(current_speed)

while True:
    if btn_pattern.value():
        pattern = (pattern % 4) + 1
        print(f"Pattern: {pattern}")
        time.sleep(0.3)
    
    if btn_speed.value():
        speed_mode = (speed_mode % 3) + 1
        current_speed = speed_list[speed_mode - 1]
        print(f"Speed: {current_speed}s")
        time.sleep(0.3)
    
    if pattern == 1: wave_right()
    elif pattern == 2: wave_left()
    elif pattern == 3: alternating()
    elif pattern == 4: all_blink()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Buttons Interfere**: Ensure separate debounce for each button.
*   **Speed Not Updating**: Remember to update `currentSpeed` from list after changing mode.
*   **List Index Error**: Array is 0-indexed but speedMode is 1-3, use `[speedMode-1]`.

### 1️⃣2️⃣ Try This Next
*   **LCD Display**: Show current pattern name and speed on LCD.
*   **Long Press**: Hold speed button to fine-tune, tap to cycle presets.
*   **Pattern Builder**: Press both buttons simultaneously to enter custom mode.

---

## 1️⃣ Project 0206: Pattern Memory (Save Preferences)

### 2️⃣ Learning Objective
Implement persistent state by saving user preferences in variables that survive across pattern changes.

### 3️⃣ Concepts Introduced
*   Persistent State Management
*   User Preference Storage
*   Default/Custom Modes
*   State Restoration
*   Memory Variables

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red GP15, Yellow GP16, Green GP17, Blue GP18)
*   4x 220Ω Resistors
*   2x Pushbuttons (GP14 for pattern, GP13 for save)
*   Breadboard

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LEDs** | GP15-18 | Via 220Ω resistors |
| **Pattern Button** | GP14 | Cycles patterns |
| **Save Button** | GP13 | Saves current as favorite |

### 6️⃣ Blocks Used
🔹 **Variables** (favoritePattern, isSaved)
🔹 **If/Else** (check if saved pattern exists)
🔹 **Print** (confirmation messages)

### 7️⃣ Variables & State
*   **currentPattern**: Number - Active pattern (1-4)
*   **favoritePattern**: Number - User's saved favorite (default 1)
*   **isSaved**: Boolean - Has user saved a preference?
*   **useDefault**: Boolean - Should load favorite on startup?

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set `favoritePattern` = 1 (default)
2. Set `isSaved` = False
3. Print "Hold Save Btn (GP13) to store favorite pattern"

**B. Main Loop Phase**
1. **Pattern Button**: Cycle through patterns 1-4
2. **Save Button Check**:
   - If held for 2 seconds:
     - Save currentPattern to favoritePattern
     - Set isSaved = True
     - Print "Pattern [X] saved as favorite!"
3. **Startup Restore**:
   - On first loop, if isSaved, load favoritePattern

**C. Event / Condition Handling**
*   Long press detection (button held >2s)
*   State persistence across pattern cycles
*   Favorite recall mechanism

### 9️⃣ Execution Flow (Plain English)
The program remembers your favorite pattern. Press and hold the Save button for 2 seconds while any pattern is running. That pattern becomes your "favorite." Next time the program starts (or you can add a recall button), it loads your saved pattern. This teaches **state persistence** - vital for user preferences in real applications.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
btn_pattern = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_save = Pin(13, Pin.IN, Pin.PULL_DOWN)

current_pattern = 1
favorite_pattern = 1
is_saved = False
save_start_time = 0

print("Hold Save Btn (GP13) for 2s to store favorite")

def execute_pattern(p):
    if p == 1:
        for led in led_pins:
            led.value(1); time.sleep(0.2); led.value(0)
    # ... other patterns

while True:
    # Pattern button
    if btn_pattern.value():
        current_pattern = (current_pattern % 4) + 1
        print(f"Pattern: {current_pattern}")
        time.sleep(0.3)
    
    # Save button (long press detection)
    if btn_save.value():
        if save_start_time == 0:
            save_start_time = time.ticks_ms()
        elif time.ticks_diff(time.ticks_ms(), save_start_time) > 2000:
            favorite_pattern = current_pattern
            is_saved = True
            print(f"★ Pattern {favorite_pattern} saved as favorite!")
            save_start_time = 0
            time.sleep(0.5)
    else:
        save_start_time = 0
    
    execute_pattern(current_pattern)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Timer Doesn't Reset**: Must clear `save_start_time` when button released.
*   **No Persistence Across Reboot**: Variables reset on power loss - use EEPROM for true persistence.

### 1️⃣2️⃣ Try This Next
*   **EEPROM Storage**: Use `pico_eeprom_write` for permanent storage across reboots.
*   **Three Favorites**: Save patterns 1-3 with different button combinations.

---

## 1️⃣ Project 0207: Custom Pattern Builder (Using Lists)

### 2️⃣ Learning Objective
Create user-defined LED sequences using lists to store custom patterns, introducing data-driven programming.

### 3️⃣ Concepts Introduced
*   Lists/Arrays
*   Data-Driven Behavior
*   Dynamic Pattern Generation
*   Sequence Programming
*   For-Each Loops

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (GP15-18)
*   4x 220Ω Resistors
*   Breadboard

### 5️⃣ Wiring / Interfaces
*(Same as previous projects - 4 LEDs on GP15-18)*

### 6️⃣ Blocks Used
🔹 **Create List** - `[15, 16, 15, 17, 18, 17]`
🔹 **For Each** - Iterate through list
🔹 **GPIO Write** - Control LEDs by pin number

### 7️⃣ Variables & State
*   **patternSequence**: List - [15, 16, 15, 17, 18, 17] (custom order)
*   **currentPin**: Number - Pin being processed in loop
*   **speed**: Number - Delay between steps

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Create list `patternSequence` = [15, 16, 15, 17, 18, 17, 15, 16]
2. Set `speed` = 0.2
3. Print "Custom sequence ready"

**B. Main Loop Phase**
1. **For Each pin in patternSequence:**
   - Turn pin ON
   - Wait `speed` seconds
   - Turn pin OFF
2. Repeat forever

**C. Event / Condition Handling**
*   List defines execution order
*   Can easily modify sequence by changing list
*   Same pin can appear multiple times

### 9️⃣ Execution Flow (Plain English)
Instead of hardcoding "turn on LED 1, then 2, then 3," we store the sequence in a list: [15, 16, 15, 17]. The program reads the list and lights each pin in order. Want a different pattern? Just change the list! This is **data-driven programming** - behavior controlled by data, not code structure.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

led_pins_obj = {15: Pin(15, Pin.OUT), 16: Pin(16, Pin.OUT), 
                17: Pin(17, Pin.OUT), 18: Pin(18, Pin.OUT)}

pattern_sequence = [15, 16, 15, 17, 18, 17, 16, 15]
speed = 0.2

print("Custom sequence ready")

while True:
    for pin_num in pattern_sequence:
        led_pins_obj[pin_num].value(1)
        time.sleep(speed)
        led_pins_obj[pin_num].value(0)
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Pin Objects**: Create Pin objects in dict for easy lookup.
*   **Duplicate Entries**: Lists can have repeats - this is intentional for custom effects.

### 1️⃣2️⃣ Try This Next
*   **Button Input**: Add 4 buttons to let user build sequence (press button = add that LED to list).
*   **Reverse Mode**: Add reverse list traversal.

---

## 1️⃣ Project 0208: Interactive Simon Says Game

### 2️⃣ Learning Objective
Build a complete interactive game combining LEDs, buttons, random sequences, and user input validation.

### 3️⃣ Concepts Introduced
*   Game Logic
*   Random Sequence Generation
*   User Input Validation
*   Score Tracking
*   Increasing Difficulty

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (GP15-18)
*   4x Buttons (GP10-13, one per LED)
*   4x 220Ω Resistors
*   Breadboard

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Red LED + Button** | GP15, GP10 |
| **Yellow LED + Button** | GP16, GP11 |
| **Green LED + Button** | GP17, GP12 |
| **Blue LED + Button** | GP18, GP13 |

### 6️⃣ Blocks Used
🔹 **Random** - Generate sequence
🔹 **Lists** - Store game sequence
🔹 **For loops** - Show and check sequence
🔹 **Comparison** - Validate player input

### 7️⃣ Variables & State
*   **gameSequence**: List - Generated LED sequence
*   **playerInput**: List - User's button presses
*   **level**: Number - Current difficulty (sequence length)
*   **score**: Number - Successful rounds completed

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Create empty `gameSequence` list
2. Set `level` = 1, `score` = 0
3. Print "Simon Says - Watch and repeat!"

**B. Main Loop Phase**
1. **Generate Round:**
   - Add random LED (15-18) to gameSequence
   - Increment level

2. **Show Sequence:**
   - For each LED in gameSequence:
     - Light LED for 0.5s
     - Wait 0.3s between

3. **Get Player Input:**
   - Wait for button presses
   - Store each press in playerInput list
   - Timeout after 5s of no input

4. **Validate:**
   - Compare playerInput to gameSequence
   - If match: score++, next round
   - If mismatch: Game Over, reset

**C. Event / Condition Handling**
*   Progressive difficulty (sequence gets longer)
*   Input timeout mechanism
*   Win/lose conditions

### 9️⃣ Execution Flow (Plain English)
Simon Says is a memory game. The Pico shows a sequence of LED flashes. You must press the corresponding buttons in the same order. Each round adds one more step. Miss once = game over. This teaches **game state management**, **input validation**, and **dynamic difficulty**.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time
import random

leds = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
btns = [Pin(10, Pin.IN, Pin.PULL_DOWN), Pin(11, Pin.IN, Pin.PULL_DOWN),
        Pin(12, Pin.IN, Pin.PULL_DOWN), Pin(13, Pin.IN, Pin.PULL_DOWN)]
led_to_idx = {15:0, 16:1, 17:2, 18:3}

game_sequence = []
score = 0

print("Simon Says - Watch and repeat!")

def show_sequence():
    for led_num in game_sequence:
        leds[led_to_idx[led_num]].value(1)
        time.sleep(0.5)
        leds[led_to_idx[led_num]].value(0)
        time.sleep(0.3)

def get_player_input():
    player = []
    for _ in range(len(game_sequence)):
        while True:
            for i, btn in enumerate(btns):
                if btn.value():
                    player.append(15 + i)
                    leds[i].value(1)
                    time.sleep(0.2)
                    leds[i].value(0)
                    while btn.value(): time.sleep(0.01)
                    time.sleep(0.1)
                    break
            else:
                continue
            break
    return player

while True:
    game_sequence.append(random.choice([15, 16, 17, 18]))
    print(f"Level {len(game_sequence)}")
    
    show_sequence()
    time.sleep(1)
    
    player_input = get_player_input()
    
    if player_input == game_sequence:
        score += 1
        print(f"Correct! Score: {score}")
        time.sleep(1)
    else:
        print(f"Wrong! Final Score: {score}")
        game_sequence = []
        score = 0
        time.sleep(3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Input Timeout**: Add timer to end turn if player takes too long.
*   **Button Bounce**: Ensure wait for button release before accepting next press.

### 1️⃣2️⃣ Try This Next
*   **Speed Mode**: Faster flashes as level increases.
*   **Sound**: Add buzzer tones for each color.
*   **Multiplayer**: Two players alternate turns.

---

## 1️⃣ Project 0209: Ambient Light Show (Auto-Adjust Everything)

### 2️⃣ Learning Objective
Create a fully autonomous system that automatically adjusts both pattern and speed based on environmental light levels.

### 3️⃣ Concepts Introduced
*   Autonomous Behavior
*   Multi-Parameter Adjustment
*   Environmental Adaptation
*   Smart Algorithms
*   Sensor-Driven Logic

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (GP15-18)
*   LDR Sensor (GP27)
*   10kΩ Resistor
*   Breadboard

### 5️⃣ Wiring / Interfaces
*(LEDs on GP15-18 + LDR voltage divider on GP27)*

### 6️⃣ Blocks Used
🔹 **Read Analog** (GP27)
🔹 **Map** (light to speed)
🔹 **Multiple If/Else** (pattern selection)

### 7️⃣ Variables & State
*   **lightLevel**: ADC reading
*   **autoSpeed**: Calculated from light
*   **autoPattern**: Selected based on light
*   **mode**: "Dawn", "Day", "Dusk", "Night"

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set thresholds: NIGHT<20000, DUSK<40000, DAY<55000, else BRIGHT
2. Print "Ambient Light Show Active"

**B. Main Loop Phase**
1. Read lightLevel from GP27
2. **Determine Mode:**
   - 0-20000: Night (slow, calm, pattern 4)
   - 20000-40000: Dusk (medium, pattern 3)
   - 40000-55000: Day (fast, pattern 1)
   - 55000+: Bright (very fast, pattern 2)
3. Map lightLevel to speed (inverted: bright=fast)
4. Execute selected pattern at calculated speed

**C. Event / Condition Handling**
*   Continuous environmental monitoring
*   Both speed AND pattern auto-adjust
*   Smooth transitions between modes

### 9️⃣ Execution Flow (Plain English)
This is a "set it and forget it" system. Place it near a window and it becomes a natural ambient light. Morning sunrise = gentle slow patterns. Midday = energetic fast waves. Evening = calm fading. Night = very slow breathing effect. No buttons needed - pure environmental awareness.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, ADC
import time

leds = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
ldr = ADC(27)

print("Ambient Light Show Active")

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    light = ldr.read_u16()
    
    # Determine mode and pattern
    if light < 20000:
        mode, pattern, base_speed = "Night", 4, 0.8
    elif light < 40000:
        mode, pattern, base_speed = "Dusk", 3, 0.5
    elif light < 55000:
        mode, pattern, base_speed = "Day", 1, 0.2
    else:
        mode, pattern, base_speed = "Bright", 2, 0.1
    
    # Fine-tune speed based on exact light level
    speed = map_value(light, 0, 65535, 0.8, 0.1)
    
    print(f"{mode} | Light: {light} | Speed: {speed:.2f}s")
    
    # Execute pattern
    if pattern == 1:  # Fast wave
        for led in leds:
            led.value(1); time.sleep(speed); led.value(0)
    elif pattern == 2:  # Reverse wave
        for led in reversed(leds):
            led.value(1); time.sleep(speed); led.value(0)
    elif pattern == 3:  # Alternating
        leds[0].value(1); leds[2].value(1)
        time.sleep(speed)
        leds[0].value(0); leds[2].value(0)
        leds[1].value(1); leds[3].value(1)
        time.sleep(speed)
        leds[1].value(0); leds[3].value(0)
    elif pattern == 4:  # Slow breathe
        for led in leds: led.value(1)
        time.sleep(speed)
        for led in leds: led.value(0)
        time.sleep(speed)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Rapid Mode Changes**: Add hysteresis (different thresholds for up/down transitions).
*   **LDR Calibration**: Print light values and adjust thresholds for your environment.

### 1️⃣2️⃣ Try This Next
*   **Time-Based**: Use RTC module to add time-of-day awareness.
*   **Weather Sync**: If WiFi-enabled, fetch weather and adjust colors (sunny=yellow, rainy=blue).

---

## 1️⃣ Project 0210: Master LED Controller (Integration Project)

### 2️⃣ Learning Objective
Integrate all previous concepts into a comprehensive LED control system with menu selection, multiple modes, and full customization.

### 3️⃣ Concepts Introduced
*   System Integration
*   Menu-Driven Interface
*   Mode Management
*   Feature Combination
*   Complete System Design

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (GP15-18)
*   4x 220Ω Resistors
*   2x Buttons (GP14 Menu, GP13 Select)
*   Potentiometer (GP26)
*   LDR (GP27)
*   Optional: I2C LCD for menu display

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Function |
| :--- | :--- | :--- |
| **LEDs** | GP15-18 | Output |
| **Menu Button** | GP14 | Navigate menu |
| **Select Button** | GP13 | Choose option |
| **Potentiometer** | GP26 | Speed/brightness |
| **LDR** | GP27 | Auto mode sensor |

### 6️⃣ Blocks Used
*   All blocks from Projects 0201-0209 combined
*   Menu system logic
*   State machine for mode switching

### 7️⃣ Variables & State
*   **menuItem**: Number (1-5) - Current menu position
*   **activeMode**: String - "Manual", "Auto", "Game", "Custom"
*   **pattern, speed, brightness**: Mode-specific variables
*   **savedSettings**: Dict/List - User preferences

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize all hardware (LEDs, buttons, sensors)
2. Create menu structure:
   - 1: Manual Control (pattern + speed buttons)
   - 2: Auto Mode (light-reactive from 0204)
   - 3: Game Mode (Simon Says from 0208)
   - 4: Custom Builder (list-based from 0207)
   - 5: Settings (save favorites)
3. Start in menu selection mode

**B. Main Loop Phase**
1. **Menu Mode:**
   - Display current menu item
   - Menu button: navigate options
   - Select button: enter chosen mode

2. **Active Mode Execution:**
   - Run selected mode's main logic
   - Menu button (long press): return to menu
   - Each mode has sub-controls via other inputs

3. **Mode-Specific Behavior:**
   - Manual: Buttons control pattern/speed
   - Auto: LDR drives everything
   - Game: Simon Says logic
   - Custom: Build/play custom sequences
   - Settings: Configure defaults

**C. Event / Condition Handling**
*   Menu navigation state machine
*   Mode switching with state persistence
*   Input context changes per mode
*   Settings saved across sessions

### 9️⃣ Execution Flow (Plain English)
This is the **master project** combining everything. On startup, you see a menu (1-5). Press Menu button to scroll, Select to enter a mode. Each mode uses different inputs:
- Manual = buttons control pattern/speed
- Auto = LDR sensor takes over
- Game = Simon Says memory challenge
- Custom = Build your own sequences
- Settings = Configure favorites

Long-press Menu from any mode returns you to main menu. This demonstrates **professional system architecture** with clear separation of concerns and mode management.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, ADC
import time
import random

# Hardware initialization
leds = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]
btn_menu = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_select = Pin(13, Pin.IN, Pin.PULL_DOWN)
pot = ADC(26)
ldr = ADC(27)

# State variables
menu_item = 1
active_mode = None
pattern = 1
speed = 0.3

print("=== MASTER LED CONTROLLER ===")
print("Menu Btn: GP14 | Select: GP13")

def show_menu():
    menus = ["1: Manual", "2: Auto", "3: Game", "4: Custom", "5: Settings"]
    print(f"\n>>> {menus[menu_item-1]}")

def manual_mode():
    global pattern, speed
    print("Manual Mode Active")
    # Implementation from 0202-0203
    # ...

def auto_mode():
    print("Auto Mode (Light-Reactive)")
    # Implementation from 0204/0209
    # ...

def game_mode():
    print("Simon Says Game")
    # Implementation from 0208
    # ...

def custom_mode():
    print("Custom Pattern Builder")
    # Implementation from 0207
    # ...

def settings_mode():
    print("Settings & Favorites")
    # Save/load preferences
    # ...

show_menu()

while True:
    if active_mode is None:  # Menu navigation
        if btn_menu.value():
            menu_item = (menu_item % 5) + 1
            show_menu()
            time.sleep(0.3)
        
        if btn_select.value():
            if menu_item == 1: active_mode = "manual"
            elif menu_item == 2: active_mode = "auto"
            elif menu_item == 3: active_mode = "game"
            elif menu_item == 4: active_mode = "custom"
            elif menu_item == 5: active_mode = "settings"
            time.sleep(0.3)
    
    else:  # Mode execution
        # Check for exit (long press menu)
        if btn_menu.value():
            active_mode = None
            show_menu()
            time.sleep(0.5)
            continue
        
        # Execute active mode
        if active_mode == "manual": manual_mode()
        elif active_mode == "auto": auto_mode()
        elif active_mode == "game": game_mode()
        elif active_mode == "custom": custom_mode()
        elif active_mode == "settings": settings_mode()
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **State Confusion**: Clear all LEDs when switching modes.
*   **Menu Stuck**: Ensure mode exit logic (long press) is always checked.
*   **Resource Conflicts**: Each mode must clean up (turn off LEDs) before exiting.
*   **Input Lag**: Use non-blocking delays where possible.

### 1️⃣2️⃣ Try This Next
*   **LCD Menu**: Add I2C LCD to show menu visually instead of serial.
*   **EEPROM Settings**: Save mode preferences to EEPROM (survive reboots).
*   **Remote Control**: Add IR receiver to navigate menu remotely.
*   **Bluetooth**: Add BLE for smartphone control via app.
*   **Multi-User**: Support multiple saved profiles (User 1, 2, 3).
*   **Animation Preview**: Show mini version of each mode in menu (LED previews).

---
