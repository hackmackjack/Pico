# Batch 40: Metronome 2 - Projects 0391-0395

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

metronome_batch1 = r'''
## Batch 40: Metronome 2

---

## 1️⃣ Project 0391: Introduction to Metronome

### 2️⃣ Learning Objective
Create a basic metronome that alternates between two distinct tones. You will learn about rhythmic oscillation and dual-status sound patterns.

### 3️⃣ Concepts Introduced
*   **Tick Tock Pattern**: Alternating between two tones (low and high).
*   **Dual-Status Oscillation**: Binary state toggling for rhythm generation.
*   **Even Timing**: Maintaining consistent intervals between beats.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer** (Passive or active)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Buzzer Tone**
*   **Category:** Actuators

🔹 **Modulo Operator**
*   **Category:** Math

🔹 **Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **beatCount**: Tracks current beat number.
*   **isTickBeat**: Boolean alternating true/false.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [beatCount] to [0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Determine Tick or Tock**:
        *   From **Math**, drag `set [isTickBeat] to [(beatCount % 2) = 0]`.
            *   **Snap** into loop.
    *   **Play Appropriate Tone**:
        *   From **Logic**, drag `if [isTickBeat] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [800] for [100]ms`.
                    *   **Snap** inside (low tone = Tick).
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [1200] for [100]ms`.
                    *   **Snap** inside (high tone = Tock).
    *   **Increment Beat**:
        *   From **Variables**, drag `change [beatCount] by [1]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below (120 BPM).

### 9️⃣ Execution Flow (Plain English)

The metronome plays a low tone (Tick) on even beats and a high tone (Tock) on odd beats, creating a 1-2-1-2 pattern. The modulo operator determines if the current beat count is even or odd. This provides auditory feedback for rhythm, helping musicians keep time during practice.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

beat_count = 0

while True:
    if beat_count % 2 == 0:
        # Tick (low tone)
        buzzer.freq(800)
        buzzer.duty_u16(32768)
        time.sleep(0.1)
        buzzer.duty_u16(0)
    else:
        # Tock (high tone)
        buzzer.freq(1200)
        buzzer.duty_u16(32768)
        time.sleep(0.1)
        buzzer.duty_u16(0)
    
    beat_count += 1
    time.sleep(0.4)  # 0.5s total = 120 BPM
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **No Sound**: Passive buzzers require PWM. Active buzzers don't need frequency control.
*   **Timing Drift**: Using `sleep()` accumulates drift. For precision, use `time.ticks_ms()` with target timestamps.

### 1️⃣2️⃣ Try This Next

*   **Variable BPM**: Add buttons to increase/decrease the sleep duration (faster/slower tempo).
*   **Visual Feedback**: Blink an LED in sync with the beats.

---

## 1️⃣ Project 0392: Blinking Metronome

### 2️⃣ Learning Objective
Visualize a metronome as a pendulum using 5 LEDs that light up sequentially. You will learn about sinusoidal motion visualization.

### 3️⃣ Concepts Introduced
*   **Pendulum Visualization**: Simulating back-and-forth swing with LED sequence.
*   **Sinusoidal Motion**: Pattern that mimics a physical pendulum.
*   **Bi-Directional Sequencing**: Moving forward then backward through an array.

### 4️⃣ Hardware Required
*   **Pico**
*   **5× LEDs**
*   **5× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1** | GP16 | Left position |
| **LED 2** | GP17 | |
| **LED 3** | GP18 | Center |
| **LED 4** | GP19 | |
| **LED 5** | GP20 | Right position |

### 6️⃣ Blocks Used

🔹 **Digital Write (×5)**
*   **Category:** Pin Access

🔹 **Lists**
*   **Category:** Variables

🔹 **Reverse List**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **sequence**: List `[0, 1, 2, 3, 4, 3, 2, 1]` representing pendulum swing.
*   **currentIndex**: Position in sequence.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16-20] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [sequence] to [[0, 1, 2, 3, 4, 3, 2, 1]]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [currentIndex] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Turn Off All LEDs**:
        *   From **Loops**, drag `for [pin] in [16, 17, 18, 19, 20]`.
            *   **Snap** into loop.
            *   Inside: From **Pin Access**, drag `digital write pin:[pin] value:[LOW]`.
    *   **Light Current LED**:
        *   From **Variables**, drag `set [activeLED] to [16 + sequence[currentIndex]]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `digital write pin:[activeLED] value:[HIGH]`.
            *   **Snap** below.
    *   **Advance Sequence**:
        *   From **Math**, drag `set [currentIndex] to [(currentIndex + 1) % 8]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [0.2] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The LEDs light up in order: 1→2→3→4→5, then reverse: 4→3→2→1, then repeat. This creates a visual pendulum effect, swinging left to right and back. The sequence list `[0,1,2,3,4,3,2,1]` ensures smooth back-and-forth motion without pausing at the endpoints.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leds = [machine.Pin(16 + i, machine.Pin.OUT) for i in range(5)]
sequence = [0, 1, 2, 3, 4, 3, 2, 1]
current_index = 0

while True:
    # Turn off all LEDs
    for led in leds:
        led.off()
    
    # Light current LED
    active_led = sequence[current_index]
    leds[active_led].on()
    
    # Advance sequence
    current_index = (current_index + 1) % len(sequence)
    
    time.sleep(0.2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **LEDs Stay On**: Ensure all LEDs are turned off before lighting the next one.
*   **Jerky Motion**: If movement looks choppy, reduce sleep time or add more intermediate steps (7 LEDs instead of 5).

### 1️⃣2️⃣ Try This Next

*   **Speed Control**: Link to a potentiometer to adjust pendulum speed dynamically.
*   **Audio Sync**: Play a tick sound each time the pendulum reaches the center LED.

---

## 1️⃣ Project 0393: Manual Metronome Control

### 2️⃣ Learning Objective
Implement rotary speed control using a potentiometer to adjust BPM. You will learn about analog-to-parameter mapping and BPM calculation.

### 3️⃣ Concepts Introduced
*   **Rotary Speed Control**: Using a knob to set tempo.
*   **BPM Mapping**: Converting pot position to Beats Per Minute (40-200 BPM).
*   **Variable Clock Generator**: Dynamic rhythm generation based on user input.

### 4️⃣ Hardware Required
*   **Pico**
*   **Potentiometer**
*   **OLED Display** (to show BPM)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 | ADC0 |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Read Analog Pin**
*   **Category:** Pin Access

🔹 **Map Range**
*   **Category:** Math

🔹 **OLED Text**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **potValue**: Raw ADC reading (0-65535).
*   **bpm**: Calculated Beats Per Minute (40-200).
*   **interval**: Sleep duration in seconds.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Read Pot & Calculate BPM**:
        *   From **Pin Access**, drag `set [potValue] to [read analog pin 26]`.
            *   **Snap** into loop.
        *   From **Math**, drag `map [potValue] from [0-65535] to [40-200]`.
            *   **Snap** below.
            *   Store in `bpm`.
        *   From **Math**, drag `set [interval] to [60 / bpm]`.
            *   **Snap** below.
    *   **Display BPM**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text [BPM: {bpm}]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
    *   **Play Beat**:
        *   From **Actuators**, drag `Buzzer [15] tone [1000] for [50]ms`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [interval] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The user turns the pot. The ADC value (0-65535) is mapped to BPM (40-200). At 40 BPM, the interval is 60/40 = 1.5 seconds. At 200 BPM, interval is 60/200 = 0.3 seconds. The screen displays the current BPM in real-time, and the buzzer clicks at that tempo. Turning the knob instantly adjusts the beat speed.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26)
buzzer = machine.PWM(machine.Pin(15))

while True:
    pot_value = pot.read_u16()
    bpm = int(40 + (pot_value / 65535) * 160)  # Map to 40-200
    interval = 60 / bpm
    
    oled.fill(0)
    oled.text(f"BPM: {bpm}", 0, 20)
    oled.show()
    
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(0.05)
    buzzer.duty_u16(0)
    
    time.sleep(interval - 0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **BPM Jumps Wildly**: Add smoothing by averaging the last 5 pot readings.
*   **Display Flickers**: Only update OLED if BPM changes by >2 to reduce redraws.

### 1️⃣2️⃣ Try This Next

*   **Tap Tempo**: Add a button; calculate BPM from time between 4 taps.
*   **BPM Presets**: Add buttons for instant jump to 60, 90, 120, 150 BPM.

---

## 1️⃣ Project 0394: Metronome Sequences

### 2️⃣ Learning Objective
Implement 3/4 time signature with emphasized beats. You will learn about alternative rhythm patterns and beat accenting.

### 3️⃣ Concepts Introduced
*   **Waltz Time (3/4)**: Three beats per measure: strong, weak, weak.
*   **Alternative Time Signature**: Moving beyond 4/4 (common time).
*   **Beat Accenting**: Making the first beat louder/different than others.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Modulo Operator**
*   **Category:** Math

🔹 **Buzzer Tone**
*   **Category:** Actuators

🔹 **Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **beatInMeasure**: Current beat (1, 2, or 3).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [beatInMeasure] to [1]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Determine Beat Type**:
        *   From **Logic**, drag `if [beatInMeasure] = [1] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [1500] for [150]ms`.
                    *   **Snap** inside (loud, long = ONE).
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [1000] for [80]ms`.
                    *   **Snap** inside (soft, short = two-three).
    *   **Advance Beat**:
        *   From **Math**, drag `set [beatInMeasure] to [(beatInMeasure % 3) + 1]`.
            *   **Snap** below (cycle 1→2→3→1).
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below (120 BPM).

### 9️⃣ Execution Flow (Plain English)

The metronome plays a 3/4 waltz pattern: ONE-two-three, ONE-two-three. Beat 1 is louder (1500 Hz, 150ms) while beats 2 and 3 are softer (1000 Hz, 80ms). The modulo operator wraps the beat count (1→2→3→1), creating the repeating 3-beat measure structure used in waltzes and other 3/4 music.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

beat_in_measure = 1

while True:
    if beat_in_measure == 1:
        # ONE (loud, long)
        buzzer.freq(1500)
        buzzer.duty_u16(32768)
        time.sleep(0.15)
        buzzer.duty_u16(0)
    else:
        # two-three (soft, short)
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(0.08)
        buzzer.duty_u16(0)
    
    beat_in_measure = (beat_in_measure % 3) + 1
    time.sleep(0.35)  # Remaining time to 0.5s total
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Beat Never Resets**: Ensure modulo wraps correctly: `(beat % 3) + 1` gives 1,2,3 not 0,1,2.
*   **All Beats Sound Same**: Check frequency and duration differences are noticeable.

### 1️⃣2️⃣ Try This Next

*   **5/4 Time**: Extend to 5 beats (used in "Take Five" by Dave Brubeck).
*   **Dynamic Accents**: Add button to switch between 3/4 and 4/4 time on the fly.

---

## 1️⃣ Project 0395: Interactive Metronome

### 2️⃣ Learning Objective
Create a rhythm synchronization game that provides feedback on timing accuracy. You will learn about active synchronization and tolerance windows.

### 3️⃣ Concepts Introduced
*   **Keep the Beat Game**: User must press button in sync with LED flashes.
*   **Synchronization Tolerance**: Accepting presses within ±0.1s window.
*   **Active Feedback**: Green LED for success, Red LED for miss.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Green LED**
*   **Red LED**
*   **White LED** (metronome pulse)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |
| **White LED** | GP16 | Beat indicator |
| **Green LED** | GP17 | Success |
| **Red LED** | GP18 | Miss |

### 6️⃣ Blocks Used

🔹 **Time Measurement**
*   **Category:** Timing

🔹 **Absolute Value**
*   **Category:** Math

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **beatTime**: Timestamp when beat should occur.
*   **pressTime**: Timestamp when button was pressed.
*   **timeDiff**: Difference between press and beat.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16,17,18] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Flash Beat LED**:
        *   From **Variables**, drag `set [beatTime] to [time in ms]`.
            *   **Snap** into loop.
        *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.1] seconds`.
            *   **Snap** below.
        *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
            *   **Snap** below.
    *   **Wait for Button Press**:
        *   From **Logic**, drag `wait until [digital read pin 14 OR timeout 0.6s]`.
            *   **Snap** below.
        *   From **Variables**, drag `set [pressTime] to [time in ms]`.
            *   **Snap** below.
    *   **Calculate Timing**:
        *   From **Math**, drag `set [timeDiff] to [abs(pressTime - beatTime)]`.
            *   **Snap** below.
    *   **Feedback**:
        *   From **Logic**, drag `if [timeDiff] <= [100] then`.
            *   **Snap** below (within 100ms).
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[17] value:[HIGH]`.
                    *   **Snap** inside (green = good).
                *   From **Console**, drag `print [Good! Diff: {timeDiff}ms]`.
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[18] value:[HIGH]`.
                    *   **Snap** inside (red = miss).
    *   From **Timing**, drag `sleep [0.3] seconds`.
        *   **Snap** below.
    *   Turn off feedback LEDs.

### 9️⃣ Execution Flow (Plain English)

The white LED flashes to mark the beat. The user must press the button at the exact moment the LED lights up. If pressed within 100ms (0.1 seconds) of the beat, the green LED flashes ("Good!"). If late or early by more than 100ms, the red LED flashes ("Miss"). This trains rhythmic precision and tests the user's ability to maintain tempo.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_white = machine.Pin(16, machine.Pin.OUT)
led_green = machine.Pin(17, machine.Pin.OUT)
led_red = machine.Pin(18, machine.Pin.OUT)

while True:
    beat_time = time.ticks_ms()
    
    # Flash beat
    led_white.on()
    time.sleep(0.1)
    led_white.off()
    
    # Wait for button press with timeout
    start_wait = time.ticks_ms()
    while not button.value():
        if time.ticks_diff(time.ticks_ms(), start_wait) > 600:
            break
    
    press_time = time.ticks_ms()
    time_diff = abs(time.ticks_diff(press_time, beat_time))
    
    # Feedback
    if time_diff <= 100:
        led_green.on()
        print(f"Good! Diff: {time_diff}ms")
    else:
        led_red.on()
        print(f"Miss! Diff: {time_diff}ms")
    
    time.sleep(0.3)
    led_green.off()
    led_red.off()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Red**: Check if button debouncing is causing delayed reads.
*   **Always Green**: If tolerance is too wide (>200ms), tighten to 75ms for harder challenge.

### 1️⃣2️⃣ Try This Next

*   **Score Counter**: Track consecutive "Good" presses; show high score.
*   **Progressive Difficulty**: Start at 120 BPM, increase by 10 BPM after 10 successful presses.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(metronome_batch1)

print("✅ Generated Projects 0391-0395 (Metronome 2 - First 5)")
print("📋 Final 5 Metronome projects coming (0396-0400)...")
