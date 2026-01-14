
# BATCH 20: Metronome 1 (Projects 0191-0200)

## Project 0191: Introduction to Metronome

### 1. Learning Objective
Understand the concept of rhythmic timekeeping using software loops. Learn how to create a steady beat (BPM) by controlling the frequency of a buzzer "click".

### 2. Concepts Introduced
*   **BPM (Beats Per Minute)**: The standard unit for measuring tempo in music.
*   **Acoustic Pulse**: Creating a short sound to represent a single beat.
*   **Steady Interval**: Maintaining a consistent time delay between actions to ensure rhythmic accuracy.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Active Buzzer
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+)** | GP15 | Generates the click sound |
| **Buzzer (-)** | GND | Ground |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: This project uses a fixed delay for 60 BPM.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   Initialize GP15 (Buzzer) to LOW.

**B. Rhythmic Cycle Phase**
2.  **Start Steady Loop**:
    *   From **Loops**, drag the `pico_forever` block.
3.  **Produce the "Click"**:
    *   Inside the loop, from **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> HIGH.
    *   From **Time**, drag `pico_wait` -> 0.05 seconds (A very short "blip").
    *   **Set** GP15 -> LOW.
4.  **Enforce the Tempo**:
    *   From **Time**, drag `pico_wait` -> 0.95 seconds.
    *   *Note: 0.05s (Sound) + 0.95s (Silence) = Exactly 1.0 second per beat (60 BPM).*

### 8. Execution Flow
1.  **Pulse**: The Pico sends energy to the buzzer for a fraction of a second.
2.  **Sound**: The user hears a short "click".
3.  **Pause**: The Pico waits for the remainder of the second.
4.  **Repeat**: The process cycles indefinitely, creating a steady 60 BPM metronome.

### 9. Generated Code
```python
from machine import Pin
import time

buzzer = Pin(15, Pin.OUT)

while True:
    # 60 BPM = 1 beat per second
    # Click duration: 0.05s
    buzzer.value(1)
    time.sleep(0.05)
    buzzer.value(0)
    
    # Wait for the next beat
    time.sleep(0.95)
```

### 10. Common Mistakes
*   **Long Beep**: If you wait 0.5s for the beep, it won't sound like a "click" but a long note.
*   **Wrong BPM Math**: If you wait 1.0s AFTER the beep, your total cycle is 1.05s, which is slower than 60 BPM.

### 11. Try This Next
*   **Double Time**: Change the delays to 0.05s sound and 0.45s pause to achieve 120 BPM.
*   **Buzzer Quality**: If using a passive buzzer, use PWM to change the pitch of the click.

---

## Project 0192: Blinking Metronome

### 1. Learning Objective
Learn the importance of multimodal feedback in engineering. Understand how to synchronize two different outputs (Audio and Visual) to provide a more effective user cue for musicians.

### 2. Concepts Introduced
*   **Audio-Visual Sync**: Ensuring light and sound triggers happen at the same instant.
*   **Visual Metronome**: Using an LED as a silent rhythmic guide.
*   **Output Parallelism**: Controlling multiple hardware components within a single logical step.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   LED + Resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Audio Click |
| **LED** | GP14 | Visual Pulse |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Fixed 60 BPM sync.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**:
    *   Initialize GP15 (Buzzer) and GP14 (LED) to LOW.

**B. Synchronized Beat Phase**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Trigger Both Outputs**:
    *   Inside: From **Smart IO**, drag `pico_gpio_write`. **Set** GP15 (Buzzer) -> HIGH.
    *   Inside: Drag another `pico_gpio_write`. **Set** GP14 (LED) -> HIGH.
4.  **Short Pulse Duration**:
    *   From **Time**, **Wait** 0.05 seconds.
5.  **Turn Both OFF**:
    *   **Set** GP15 -> LOW and GP14 -> LOW.

**C. Timing Phase**
6.  **Maintain Rhythm**:
    *   From **Time**, **Wait** 0.95 seconds.

### 8. Execution Flow
1.  **Action**: The Pico flips both digital pins to ON at the exact same clock cycle.
2.  **Feedback**: The user simultaneously hears a beep and sees a flash.
3.  **Silence**: Both components turn off after 50 milliseconds.
4.  **Wait**: The Pico idles for the rest of the second.
5.  **Result**: A professional-style metronome that is useful in both loud and silent environments.

### 9. Generated Code
```python
from machine import Pin
import time

buzzer = Pin(15, Pin.OUT)
led = Pin(14, Pin.OUT)

while True:
    # Synchronized Pulse
    buzzer.value(1)
    led.value(1)
    time.sleep(0.05)
    
    buzzer.value(0)
    led.value(0)
    
    # Wait for the 60 BPM beat
    time.sleep(0.95)
```

### 10. Common Mistakes
*   **Staggered Code**: If you put a `wait` block between the Buzzer and LED commands, the light will flash AFTER the sound.
*   **Brightness**: A 0.05s flash might be too dim for some LEDs. You can increase the pulse to 0.1s if needed (and set pause to 0.9s).

### 11. Try This Next
*   **Backlight**: If the LED is too bright, use PWM to dim the flash while keeping the Buzzer loud.
*   **Alternating colors**: If you have two LEDs, make them alternate every beat (Left, Right, Left, Right).

---

## Project 0193: Manual Metronome Control

### 1. Learning Objective
Explore dynamic tempo calculation. Learn how to use buttons to adjust a BPM variable and calculate the corresponding delay in real-time using the formula: `Delay = 60 / BPM`.

### 2. Concepts Introduced
*   **Dynamic Delay**: Using a variable to control the timing of a loop rather than a fixed number.
*   **Math-to-Timing Conversion**: Converting musical units (BPM) into technical units (Seconds).
*   **Incremental Adjustment**: Tuning a value up or down based on user input.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   2 Buttons (Faster, Slower)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Faster (+)** | GP14 | Increases BPM by 10 |
| **Btn Slower (-)** | GP13 | Decreases BPM by 10 |
| **Buzzer** | GP15 | Final output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (division, addition)
*   **from Logic, drag `controls_if`** (checking buttons)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **bpm_val**: The current tempo setting (init: 60).
*   **beat_delay**: The calculated time to wait between clicks.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup Tempo**:
    *   From **Variables**, **Set** `bpm_val` = 60.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Speed Up**:
    *   If **Button** GP14 is Pressed: **Set** `bpm_val` = `bpm_val` + 10. **Wait** 0.3s.
4.  **Slow Down**:
    *   If **Button** GP13 is Pressed AND `bpm_val` > 20: **Set** `bpm_val` = `bpm_val` - 10. **Wait** 0.3s.

**C. Calculation Phase**
5.  **Find the Gap**:
    *   From **Math**, **Set** `beat_delay` = 60 / `bpm_val`.
    *   **Print** "Tempo: ", `bpm_val`, " BPM".

**D. Rhythmic Phase**
6.  **Perform Click**:
    *   **Set** GP15 (Buzzer) -> HIGH, **Wait** 0.05s, **Set** GP15 -> LOW.
7.  **Adaptive Wait**:
    *   From **Time**, drag `pico_wait`. 
    *   **Set** value to (`beat_delay` - 0.05).

### 8. Execution Flow
1.  **Read**: The Pico checks for any tempo changes from the buttons.
2.  **Update**: If you press "+", `bpm_val` becomes 70.
3.  **Math**: The Pico calculates 60 / 70 = 0.857 seconds.
4.  **Action**: The buzzer clicks, and the Pico waits for exactly 0.857s before clicking again.
5.  **Result**: The user can "re-tune" their metronome while practicing.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware
btn_f = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_s = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)

bpm = 60

while True:
    # Adjust Tempo
    if btn_f.value():
        bpm += 10
        print("BPM: " + str(bpm))
        time.sleep(0.3)
    if btn_s.value() and bpm > 20:
        bpm -= 10
        print("BPM: " + str(bpm))
        time.sleep(0.3)
        
    # Calculate Delay
    beat_sec = 60 / bpm
    
    # Click
    buzzer.value(1)
    time.sleep(0.05)
    buzzer.value(0)
    
    # Precise wait
    time.sleep(beat_sec - 0.05)
```

### 10. Common Mistakes
*   **Division by Zero**: If `bpm` reaches 0, the program will crash. Always set a minimum limit (> 10).
*   **Wait Timing**: If you don't subtract the 0.05s click from the total delay, the tempo will be slightly slower than the number on the screen.

### 11. Try This Next
*   **Fine Tuning**: Change the step to +/- 1 BPM for professional precision.
*   **OLED Display**: Show the `bpm_val` on the screen so you don't need the computer console.

---

## Project 0194: Metronome Sequences

### 1. Learning Objective
Explore measure accentuation and musical meter (4/4 time). Learn how to use counting logic within a loop to distinguish the "Downbeat" (Beat 1) using pitch variation.

### 2. Concepts Introduced
*   **Time Signature**: The structure of beats in a measure (e.g., 4 beats).
*   **Accentuation**: Making one beat distinct from others to help keep track of the start of the measure.
*   **Modulo Counting**: cycling through a set of numbers (1, 2, 3, 4) repeatedly.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer (best for changing pitch) or two active buzzers
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+)** | GP15 | Pitch-controlled output |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Logic, drag `controls_if`** (checking beat number)
*   **from Math, drag `math_arithmetic`** (addition, modulo)
*   **from Actuators, drag `pico_buzzer_pitch`** (set frequency)

### 6. Variables
*   **beat_count**: Current position in the measure (0 to 3).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Measure Start**:
    *   **Set** `beat_count` = 0.

**B. Rhythmic Loop Phase**
2.  **Start Measure Loop**: From **Loops**, drag `pico_forever`.
3.  **Identify the Downbeat**:
    *   From **Logic**, drag `controls_if` with **else**.
    *   **Condition**: If `beat_count` == 0.
4.  **Accent (Beat 1)**:
    *   Inside the **If**:
    *   **Set** Buzzer Frequency to 800Hz (High).
    *   **Wait** 0.05s. **Silence** Buzzer.
    *   **Print** "1 (ACCENT)".
5.  **Normal (Beats 2-3-4)**:
    *   Inside the **Else**:
    *   **Set** Buzzer Frequency to 400Hz (Low).
    *   **Wait** 0.05s. **Silence** Buzzer.
    *   **Print** `beat_count` + 1.

**C. Update Phase**
6.  **Progress Measure**:
    *   **Set** `beat_count` = (`beat_count` + 1) % 4.
7.  **Tempo Wait**:
    *   **Wait** 0.95 seconds (for 60 BPM).

### 8. Execution Flow
1.  **Beat 1**: Pico sees `beat_count` is 0. It plays a high "Ding".
2.  **Tick**: `beat_count` becomes 1. Pico plays a low "Click".
3.  **Tick**: `beat_count` becomes 2, then 3. More low clicks.
4.  **Loop**: At 4, the modulo resets `beat_count` to 0.
5.  **Result**: The user hears: **DING**, click, click, click... **DING**, click, click, click.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))
beat_count = 0

def play_beep(freq):
    bz.freq(freq)
    bz.duty_u16(32768) # 50% volume
    time.sleep(0.05)
    bz.duty_u16(0) # Off

while True:
    if beat_count == 0:
        # High Downbeat
        print("ONE")
        play_beep(1000)
    else:
        # Lower Ticks
        print(beat_count + 1)
        play_beep(500)
        
    # Cycle through 0, 1, 2, 3
    beat_count = (beat_count + 1) % 4
    
    time.sleep(0.95)
```

### 10. Common Mistakes
*   **Variable Scope**: If `beat_count = 0` is inside the loop, the metronome will play ONLY "ONE" over and over.
*   **Modulo Math**: ensure you modulo by the total beats in the measure (4) to stay in sync.

### 11. Try This Next
*   **3/4 Waltz**: Change the modulo to 3 to get a "DING-click-click" rhythm.
*   **Visual Measure**: Flash a Red LED on Beat 1 and a Green LED on all other beats.

---

## Project 0195: Interactive Metronome

### 1. Learning Objective
Implement "Tap Tempo" logic. Learn how to capture the time interval between two user events (Button Taps), average them, and use that physics-derived data to set the rhythm of a machine.

### 2. Concepts Introduced
*   **Interval Capture**: calculating the delta (difference) between two points in time.
*   **Physics-to-Software Link**: Translating human physical rhythm into machine-based BPM.
*   **Temporal Averaging**: using the last two taps to find a stable speed.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Button
*   Buzzer
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tap Button** | GP14 | Tap your rhythm here |
| **Buzzer** | GP15 | Outputs the calculated beat |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_time_ms`** (get current clock)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Logic, drag `controls_if`** (detecting taps)

### 6. Variables
*   **t1, t2**: timestamps of the first and second taps.
*   **gap**: the milliseconds between taps.
*   **live_bpm**: the converted tempo.

### 7. Step-by-Step Guide

**A. Capture Phase**
1.  **Wait for First Tap**:
    *   Repeat-until **Button** GP14 is Pressed.
    *   **Set** `t1` = **Time** `pico_time_ms`.
    *   **Wait** 0.2s (Debounce).
2.  **Wait for Second Tap**:
    *   Repeat-until **Button** GP14 is Pressed.
    *   **Set** `t2` = **Time** `pico_time_ms`.

**B. Brain Phase**
3.  **Calculate the Rhythm**:
    *   From **Math**, **Set** `gap` = `t2` - `t1`.
    *   **Set** `live_bpm` = (60000 / `gap`) rounded.
    *   **Print** "Rhythm Detected: ", `live_bpm`, " BPM".

**C. Feedback Phase (Metronome)**
4.  **Perform Beat**:
    *   From **Loops**, Repeat 10 times:
        *   **Click** Buzzer.
        *   **Wait** `gap` milliseconds.

### 8. Execution Flow
1.  **Interaction**: You tap the button once... wait a moment... tap again.
2.  **Math**: The Pico sees that exactly 500ms passed between taps.
3.  **Translate**: 500ms = 2 beats per second = 120 beats per minute.
4.  **Play**: The Pico immediately starts a metronome at exactly 120 BPM to match your hand.
5.  **Result**: An organic way to communicate tempo to a computer without typing numbers.

### 9. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = Pin(15, Pin.OUT)

print("Tap the button twice to set tempo...")

while True:
    # First Tap
    while btn.value() == 0: pass
    t1 = time.ticks_ms()
    time.sleep(0.2) # Debounce
    
    # Second Tap
    while btn.value() == 0: pass
    t2 = time.ticks_ms()
    
    # Logic
    gap_ms = time.ticks_diff(t2, t1)
    if gap_ms > 100: # Ignore accidental double clicks
        bpm = int(60000 / gap_ms)
        print("Detected Tempo: " + str(bpm) + " BPM")
        
        # Play 10 beats to confirm
        for _ in range(10):
            bz.value(1); time.sleep(0.05); bz.value(0)
            time.sleep((gap_ms/1000) - 0.05)
            
    print("Ready for next tap...")
    time.sleep(1)
```

### 10. Common Mistakes
*   **Accidental Jitters**: hitting the button once often creates two signals (bouncing). Always use a small `wait` after the first tap.
*   **Gap Too Big**: If you wait 10 seconds between taps, the BPM will be 6. Ensure you handle "Timeouts" if the user doesn't hit the second tap.

### 11. Try This Next
*   **Averaging Multi-Tap**: Capture 4 taps and find the average gap for a much more accurate tempo.
*   **Visual Confirm**: Make an LED flash while you are waiting for the second tap.

---
