# Continue Batch 41: Projects 0404-0407

target_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'

batch41_part2 = r'''
## 1️⃣ Project 0404: LED Patterns Sequences

### 2️⃣ Learning Objective
Create a bouncing LED animation that reverses direction at endpoints. You will learn about bi-directional sequencing and array index management.

### 3️⃣ Concepts Introduced
*   **Bounce Pattern**: Movement that reverses at boundaries (1→2→3→4→5→4→3→2→1...).
*   **Bi-Directional Sweeping**: Traveling forward then backward through a sequence.
*   **Direction Flag**: Using a variable to track current direction.

### 4️⃣ Hardware Required
*   **Pico**
*   **5× LEDs**
*   **5× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1** | GP16 | Left end |
| **LED 2** | GP17 | |
| **LED 3** | GP18 | Center |
| **LED 4** | GP19 | |
| **LED 5** | GP20 | Right end |

### 6️⃣ Blocks Used

🔹 **Digital Write (×5)**
*   **Category:** Pin Access

🔹 **Lists**
*   **Category:** Variables

🔹 **Direction Variable**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **currentLED**: Index of currently lit LED (0-4).
*   **direction**: 1 for forward, -1 for backward.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16-20] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [currentLED] to [0]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [direction] to [1]`.
        *   **Snap** below (start moving forward).

*   **B. Main Loop Phase**
    *   **Turn Off All LEDs**:
        *   From **Loops**, drag `for [pin] in [16, 17, 18, 19, 20]`.
            *   **Snap** into loop.
            *   Inside: From **Pin Access**, drag `digital write pin:[pin] value:[LOW]`.
    *   **Light Current LED**:
        *   From **Pin Access**, drag `digital write pin:[16 + currentLED] value:[HIGH]`.
            *   **Snap** below.
    *   **Move to Next LED**:
        *   From **Variables**, drag `change [currentLED] by [direction]`.
            *   **Snap** below.
    *   **Check Boundaries & Reverse**:
        *   From **Logic**, drag `if [currentLED] = [4] then`.
            *   **Snap** below (hit right end).
            *   Inside: From **Variables**, drag `set [direction] to [-1]`.
        *   From **Logic**, drag `if [currentLED] = [0] then`.
            *   **Snap** below (hit left end).
            *   Inside: From **Variables**, drag `set [direction] to [1]`.
    *   From **Timing**, drag `sleep [0.2] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The light starts at LED 1 and moves right (LED 1→2→3→4→5). Upon reaching LED 5, the direction flips, and it moves left (5→4→3→2→1). At LED 1, it reverses again. This creates a continuous bouncing effect, like a ball bouncing between two walls. The pattern is smooth and symmetrical.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leds = [machine.Pin(16 + i, machine.Pin.OUT) for i in range(5)]
current_led = 0
direction = 1

while True:
    # Turn off all LEDs
    for led in leds:
        led.off()
    
    # Light current LED
    leds[current_led].on()
    
    # Move to next position
    current_led += direction
    
    # Reverse at boundaries
    if current_led == 4:
        direction = -1
    elif current_led == 0:
        direction = 1
    
    time.sleep(0.2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Out of Bounds**: If you check boundaries after incrementing, you might get index 5 (invalid). Check *at* the endpoints (0 and 4), not after.
*   **Stuck at End**: Ensure direction changes to -1 at 4 and +1 at 0.

### 1️⃣2️⃣ Try This Next

*   **Accelerating Bounce**: Gradually decrease sleep time on each bounce (0.2s → 0.15s → 0.1s) until very fast.
*   **Two Balls**: Run two independent sequences, one starting at each end.

---

## 1️⃣ Project 0405: Interactive LED Patterns

### 2️⃣ Learning Objective
Implement multi-mode selection using a potentiometer to switch between different LED behaviors. You will learn about range-based mode switching and analog input mapping.

### 3️⃣ Concepts Introduced
*   **Dial-a-Pattern**: Using analog position to select discrete modes.
*   **Multi-Mode Selection**: Dividing a continuous range into distinct zones.
*   **Range Thresholds**: Defining boundaries for mode transitions.

### 4️⃣ Hardware Required
*   **Pico**
*   **Potentiometer**
*   **LED**
*   **Resistor** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 | ADC0 |
| **LED** | GP16 | PWM capable |

### 6️⃣ Blocks Used

🔹 **Read Analog Pin**
*   **Category:** Pin Access

🔹 **Map Range**
*   **Category:** Math

🔹 **PWM Control**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **potValue**: Raw ADC reading (0-65535).
*   **percentage**: Mapped value (0-100%).
*   **mode**: Selected pattern mode (0-4).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16] as OUTPUT (PWM)`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Potentiometer**:
        *   From **Pin Access**, drag `set [potValue] to [read analog pin 26]`.
            *   **Snap** into loop.
        *   From **Math**, drag `map [potValue] from [0-65535] to [0-100]`.
            *   **Snap** below.
            *   Store in `percentage`.
    *   **Determine Mode**:
        *   From **Logic**, drag `if [percentage] < [20] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [mode] to [0]`.
                *   **Snap** inside (Off).
        *   From **Logic**, drag `else if [percentage] < [40] then`.
            *   **Snap** below.
            *   Inside: From **Variables**, drag `set [mode] to [1]`.
                *   **Snap** inside (Solid On).
        *   (Continue for modes 2=Slow Blink, 3=Fast Blink, 4=Strobe)
    *   **Execute Pattern**:
        *   From **Logic**, drag `if [mode] = [0] then`.
            *   Inside: `LED off`.
        *   From **Logic**, drag `else if [mode] = [1] then`.
            *   Inside: `LED full brightness`.
        *   From **Logic**, drag `else if [mode] = [2] then`.
            *   Inside: `Slow blink (1s on, 1s off)`.
        *   From **Logic**, drag `else if [mode] = [3] then`.
            *   Inside: `Fast blink (0.2s on, 0.2s off)`.
        *   From **Logic**, drag `else`.
            *   Inside: `Strobe (0.05s on, 0.05s off)`.

### 9️⃣ Execution Flow (Plain English)

Turning the potentiometer left (0-20%) keeps the LED off. Slightly right (20-40%) turns it solid on. Middle-left (40-60%) makes it blink slowly. Middle-right (60-80%) blinks fast. Far right (80-100%) strobes rapidly. Each 20% range triggers a distinct behavior, allowing mode selection without buttons.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

pot = machine.ADC(26)
led = machine.PWM(machine.Pin(16))
led.freq(1000)

while True:
    pot_value = pot.read_u16()
    percentage = (pot_value / 65535) * 100
    
    if percentage < 20:
        # Mode 0: Off
        led.duty_u16(0)
    elif percentage < 40:
        # Mode 1: Solid On
        led.duty_u16(65535)
    elif percentage < 60:
        # Mode 2: Slow Blink
        led.duty_u16(65535)
        time.sleep(1)
        led.duty_u16(0)
        time.sleep(1)
    elif percentage < 80:
        # Mode 3: Fast Blink
        led.duty_u16(65535)
        time.sleep(0.2)
        led.duty_u16(0)
        time.sleep(0.2)
    else:
        # Mode 4: Strobe
        led.duty_u16(65535)
        time.sleep(0.05)
        led.duty_u16(0)
        time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Mode Flicker**: If pot is near a boundary (e.g., 39%), it might flicker between modes. Add hysteresis (e.g., switch at 38% down, 42% up).
*   **Blocking Sleep**: Slow/Fast blink modes block other code. For non-blocking, use timestamp-based toggling.

### 1️⃣2️⃣ Try This Next

*   **RGB Modes**: Use 3 LEDs (RGB) and create color-changing modes.
*   **Smooth Fade**: Instead of discrete modes, have brightness continuously fade from 0-100% as you turn the pot.

---

## 1️⃣ Project 0406: Smart LED Patterns Switch

### 2️⃣ Learning Objective
Create a proximity-based dimmer using an ultrasonic sensor to control LED brightness via PWM. You will learn about distance-to-brightness mapping and inverse proportional control.

### 3️⃣ Concepts Introduced
*   **Proximity Dimmer**: Closer distance → brighter light.
*   **Distance-to-Brightness Mapping**: Converting sensor reading to PWM duty cycle.
*   **Inverse Mapping**: Near = high value, far = low value.

### 4️⃣ Hardware Required
*   **Pico**
*   **Ultrasonic Sensor** (HC-SR04)
*   **LED**
*   **Resistor** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Ultrasonic Trigger** | GP14 | |
| **Ultrasonic Echo** | GP15 | |
| **LED** | GP16 | PWM |

### 6️⃣ Blocks Used

🔹 **Read Ultrasonic Distance**
*   **Category:** Sensors

🔹 **Map Range (Inverted)**
*   **Category:** Math

🔹 **PWM Duty Cycle**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **distance**: Measured distance in cm (0-400).
*   **brightness**: PWM duty cycle (0-65535).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup Ultrasonic Trigger:[14] Echo:[15]`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16] as PWM`.
        *   **Snap** below.
    *   From **PWM**, drag `set PWM frequency to [1000] Hz`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Read Distance**:
        *   From **Sensors**, drag `set [distance] to [read ultrasonic distance]`.
            *   **Snap** into loop.
    *   **Clamp Distance**:
        *   From **Math**, drag `clamp [distance] between [5-30]`.
            *   **Snap** below.
    *   **Map to Brightness (Inverted)**:
        *   From **Math**, drag `map [distance] from [30-5] to [0-65535]`.
            *   **Snap** below (note: inverted range).
            *   Store in `brightness`.
    *   **Set LED Brightness**:
        *   From **Pin Access**, drag `set PWM duty cycle pin:[16] to [brightness]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The ultrasonic sensor measures distance to the nearest object (e.g., your hand). When your hand is 30cm away, the LED is at 0% brightness (off). As you move your hand closer, brightness increases linearly. At 5cm, the LED is at 100% brightness. This creates an interactive dimmer controlled by proximity, useful for touchless control.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

trigger = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(15, machine.Pin.IN)
led = machine.PWM(machine.Pin(16))
led.freq(1000)

def read_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = pulse_duration * 0.034 / 2
    return distance

while True:
    distance = read_distance()
    distance = max(5, min(30, distance))  # Clamp
    
    # Invert mapping: 30cm=0%, 5cm=100%
    brightness = int((30 - distance) / 25 * 65535)
    
    led.duty_u16(brightness)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong Brightness Direction**: If LED gets dimmer when closer, you mapped forward instead of inverted. Use `(30 - distance)` not `distance`.
*   **Flickering**: Ultrasonic readings can be noisy. Average the last 3 readings for stability.

### 1️⃣2️⃣ Try This Next

*   **Exponential Response**: Use `brightness = (30 - distance)²` for more dramatic dimming near the sensor.
*   **Color Shift**: Use RGB LED—close = red, far = blue (heatmap effect).

---

## 1️⃣ Project 0407: LED Patterns Alarm System

### 2️⃣ Learning Objective
Implement a visual confirmation code to indicate system status (armed/disarmed). You will learn about output-based status feedback and pattern recognition.

### 3️⃣ Concepts Introduced
*   **Pattern Lock**: Specific flash sequence to confirm state.
*   **System Status Feedback**: Using LEDs to communicate readiness.
*   **Distinctive Codes**: Creating unique patterns for different states.

### 4️⃣ Hardware Required
*   **Pico**
*   **Red LED**
*   **Green LED**
*   **2× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | |
| **Green LED** | GP17 | |

### 6️⃣ Blocks Used

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Sleep**
*   **Category:** Timing

🔹 **Sequence Logic**
*   **Category:** Loops

### 7️⃣ Variables & State
*   **isArmed**: Boolean indicating alarm state.
*   **confirmationCode**: List of colors to flash (e.g., `['R', 'R', 'G']`).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16,17] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [isArmed] to [False]`.
        *   **Snap** below.

*   **B. Main Loop Phase (Arming Sequence)**
    *   **Trigger Arm**:
        *   (Simulate with button or auto-arm for demo)
        *   From **Variables**, drag `set [isArmed] to [True]`.
            *   **Snap** into loop.
    *   **Confirmation Code**:
        *   From **Console**, drag `print [Arming system...]`.
            *   **Snap** below.
        *   From **Variables**, drag `set [code] to [['R', 'R', 'G']]`.
            *   **Snap** below.
        *   From **Loops**, drag `for [color] in [code]`.
            *   **Snap** below.
            *   Inside:
                *   From **Logic**, drag `if [color] = ['R'] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                            *   **Snap** inside (flash red).
                        *   From **Timing**, drag `sleep [0.3] seconds`.
                            *   **Snap** below.
                        *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
                            *   **Snap** below.
                *   From **Logic**, drag `else`.
                    *   Inside: (Same for green LED on pin 17).
                *   From **Timing**, drag `sleep [0.2] seconds`.
                    *   **Snap** outside if (gap between flashes).
    *   **Armed Confirmation**:
        *   From **Console**, drag `print [System ARMED]`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

When the alarm system is armed, it flashes a confirmation code: Red-Red-Green. This visual pattern confirms the system is ready. An observer sees two red flashes followed by one green flash, distinct from any error or status pattern. This provides non-verbal confirmation without requiring a display or speaker.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

red_led = machine.Pin(16, machine.Pin.OUT)
green_led = machine.Pin(17, machine.Pin.OUT)

is_armed = False

# Arming trigger (simulate with button in real use)
print("Arming system...")
is_armed = True

# Confirmation code: R-R-G
code = ['R', 'R', 'G']
for color in code:
    if color == 'R':
        red_led.on()
        time.sleep(0.3)
        red_led.off()
    else:
        green_led.on()
        time.sleep(0.3)
        green_led.off()
    time.sleep(0.2)  # Gap between flashes

print("System ARMED")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Code Not Distinctive**: If R-R-G looks like other patterns, add longer pauses or use G-R-G-R for uniqueness.
*   **Missed Flash**: Ensure LED-off time is visible (at least 0.2s) so individual flashes are distinct.

### 1️⃣2️⃣ Try This Next

*   **Disarm Code**: Create a different pattern (G-G-R) for disarm confirmation.
*   **Audio Sync**: Play matching beeps (low-low-high) alongside the visual pattern.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch41_part2)

print("✅ Generated Projects 0404-0407 (Batch 41 continued)")
print("📋 Next: Projects 0408-0410 (completing Batch 41)...")
