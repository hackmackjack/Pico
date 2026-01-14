import os

def build_batch60():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0591 = """
---

# Batch 60: Metronome 3

## 1. Project 0591: Introduction to Metronome

### 2. Learning Objective
Programm a visual metronome that uses a short, high-contrast strobing effect on the OLED display to track musical beats.

### 3. Concepts Introduced
*   Visual Synchronization
*   Duration Control (Pulse width)
*   Frequency to Interval conversion
*   Display Strobing

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_invert`** (Flash effect)
*   **from Time, drag `pico_wait`**
*   **from Loops, drag `pico_forever`**

### 7. Variables
*   **None**: Static BPM project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Init OLED. Show "BPM: 60" on center.

**B. Main Loop Phase**
2.  **Flash Pulse**:
    *   From **Display**, drag `pico_oled_invert` (Set to 1).
    *   Wait 0.05 seconds.
    *   From **Display**, drag `pico_oled_invert` (Set to 0).
3.  **Calculate Wait**:
    *   For 60 BPM, the interval is exactly 1 second.
    *   Since the flash took 0.05s, wait **0.95 seconds**.
4.  **Repeat**: Loop to create a steady rhythm.

### 9. Execution Flow
1.  **Start**: System calculates the time between beats.
2.  **Actuation**: The screen briefly turns white (inverted).
3.  **Observation**: The flash serves as a "visual tick," helping a musician keep time without needing sound.
4.  **Timing**: The total cycle of `Flash + Wait` equals exactly the requested BPM.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("METRONOME 60BPM", 5, 25)
oled.show()

while True:
    # Strobe
    oled.invert(1)
    time.sleep(0.05)
    oled.invert(0)
    
    # Wait for next beat
    time.sleep(0.95)
```

### 11. Common Mistakes
*   **Not Subtracting Pulse**: If you wait exactly 1 second AFTER a 0.05s flash, your metronome will actually run at ~57 BPM and "drift" over time. Always subtract the flash duration from the wait.

### 12. Try This Next
*   **BPM Control**: Change the wait to `60 / bpm`.
"""

    p0592 = """
---

## 1. Project 0592: Blinking Metronome

### 2. Learning Objective
Implement a "Lead-in" or "Count-in" sequence where a visual indicator (LED) provides a preparatory pulse 4 times before the audible metronome (Buzzer) begins.

### 3. Concepts Introduced
*   Preparatory Beats
*   State Transitions
*   Audible/Visual Coordination
*   Loop Counting

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Count LED** | GP16 | Visual Lead |
| **Sound Buzzer**| GP15 | Metronome Body |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Count 4)
*   **from Smart IO, drag `pico_buzzer_beep`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Sequential behavior.

### 8. Step-by-Step Guide

**A. Lead-in Phase**
1.  **Repeat 4 Times**:
    *   Turn LED ON.
    *   Print "ONE...", "TWO..." etc.
    *   Wait 0.5s.
    *   Turn LED OFF.
    *   Wait 0.5s.

**B. Performance Phase**
2.  **Main Loop**:
    *   Turn LED ON **AND** Beep Buzzer.
    *   Wait 0.5s.
    *   Turn LED OFF.
    *   Wait 0.5s.

### 9. Execution Flow
1.  **Preparation**: The LED flashes 4 times slowly. No sound is played yet. This allows an artist to find the tempo.
2.  **Activation**: After the 4th blink, the Pico enters the "Performance" loop.
3.  **Result**: Both sound and light work together to maintain the beat.
4.  **Utility**: Mimics how a drummer clicks their sticks together 4 times before a song starts.

### 10. Generated Code
```python
import machine, time

led = machine.Pin(16, machine.Pin.OUT)
buz = machine.Pin(15, machine.Pin.OUT)

# Lead-in (4 beats)
for i in range(4):
    print(f"Ready: {i+1}")
    led.on(); time.sleep(0.1); led.off()
    time.sleep(0.4)

# Go!
print("--- GO ---")
while True:
    led.on()
    buz.on(); time.sleep(0.05); buz.off() # Click
    time.sleep(0.45) # Total 0.5s
    led.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Pitch**: Use a very short beep (0.01s - 0.05s) for the metronome. A long beep sounds like an alarm, not a musical click.

### 12. Try This Next
*   **Accent on 1**: Make the buzzer beep for 0.1s on the first beat of every 4-bar measure.
"""

    p0593 = """
---

## 1. Project 0593: Manual Metronome Control

### 2. Learning Objective
Develop a "Tap Tempo" engine that calculates the average interval between 4 consecutive button presses to set the metronome's BPM dynamically.

### 3. Concepts Introduced
*   Interval Averaging
*   Tap-to-BPM conversion
*   Microsecond Deltas
*   Real-time Recalibration

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tap Button** | GP14 | User Input |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `arithmetic`** (Current-Last)
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **last_tap**: Integer
*   **avg_interval**: Float
*   **bpm**: Integer

### 8. Step-by-Step Guide

**A. Capture Phase**
1.  **Prepare**: `samples = 0`, `total_time = 0`.
2.  **Loop 4 times**:
    *   Wait for Button GP14.
    *   Calculate `delta = current_ms - last_tap`.
    *   Add `delta` to `total_time`.
    *   Set `last_tap = current_ms`.
    *   Wait 0.1s for debounce.

**B. Calculation Phase**
3.  **Process**:
    *   `avg_interval = total_time / 4`.
    *   `bpm = 60000 / avg_interval`.
4.  **Report**:
    *   Print "Calculated BPM: [bpm]".

**C. Play Phase**
5.  **Steady Beat**: Run metronome at the new `bpm`.

### 9. Execution Flow
1.  **Input**: User taps the button along to a song.
2.  **Capture**: The Pico records the precise spacing between taps.
3.  **Math**: It averages the gaps to reduce "human error" and then converts the millisecond gap into "Beats Per Minute".
4.  **Output**: The metronome starts clicking at the synchronized speed.

### 10. Generated Code
```python
import machine, time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.Pin(15, machine.Pin.OUT)

print("Tap button 4 times for tempo...")
taps = []
while len(taps) < 4:
    if btn.value():
        taps.append(time.ticks_ms())
        print(f"Captured {len(taps)}/4")
        time.sleep(0.3)

# Calc intervals
diffs = [taps[i+1] - taps[i] for i in range(len(taps)-1)]
avg = sum(diffs) / len(diffs)
bpm = int(60000 / avg)

print(f"Tempo Linked: {bpm} BPM")
while True:
    buz.on(); time.sleep(0.02); buz.off()
    time.sleep(avg/1000 - 0.02)
```

### 11. Common Mistakes
*   **Single Tap**: You need at least 2 taps (1 gap) to find the speed. Use 4 for better accuracy.

### 12. Try This Next
*   **Continuous Tap**: After the first 4, allow subsequent taps to keep updating the average "rolling" in real-time.
"""

    p0594 = """
---

## 1. Project 0594: Metronome Sequences

### 2. Learning Objective
Programm complex, non-linear rhythmic patterns (such as the "Son Clave" 3-2 beat) using a sequence of varying wait durations.

### 3. Concepts Introduced
*   Non-linear Rhythms
*   Syncopation
*   Rhythmic Tuples
*   Musical Timing

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Click Output |

### 6. Blocks Used
*   **from List, drag `create_list`** (Storing the gap pattern)
*   **from Loops, drag `for_each`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **clave_pattern**: List (Wait durations)

### 8. Step-by-Step Guide

**A. Define Rhythm**
1.  **Set Pattern**: Create a list of durations (in seconds):
    *   `pattern = [0.4, 0.4, 0.4, 0.2, 0.4, 0.2]` (Simplified Clave).

**B. Execution Phase**
2.  **Main Loop**:
    *   **For Each** `wait_time` in `pattern`:
        *   Beep Buzzer (short).
        *   Wait `wait_time`.

### 9. Execution Flow
1.  **Start**: The system doesn't play a steady "1-1-1-1."
2.  **Syncopation**: Some gaps are longer ($0.4s$) and some are shorter ($0.2s$).
3.  **Result**: The buzzer plays a recognizable "African Rhythm" or "Latin Clave" beat.
4.  **Utility**: Teaches musicians to play along to something more complex than a basic pulse.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)

# 3-2 Clave Pattern (Gaps between hits)
clave = [0.4, 0.4, 0.4, 0.2, 0.4]

while True:
    for gap in clave:
        buz.on(); time.sleep(0.02); buz.off()
        time.sleep(gap)
```

### 11. Common Mistakes
*   **Gap Math**: Forgetting that the "total bar" must still add up to a round number (like 2 seconds) for it to loop correctly.

### 12. Try This Next
*   **Swing**: Add a variable to one of the gaps to make the rhythm feel "loose" or "tight".
"""

    p0595 = """
---

## 1. Project 0595: Interactive Metronome

### 2. Learning Objective
Build an "Accented Metronome" with dynamic modifiers that allow the user to toggle "Triple-time" or "Downbeat Emphasis" using buttons.

### 3. Concepts Introduced
*   Musical Accents (Louder/Longer)
*   Rhythmic Subdivisions (Triplets)
*   Modifier Flags
*   Loop Branching

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accent Btn** | GP14 | Emphasis on beat 1 |
| **Triplet Btn**| GP15 | Change subdivision |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Math, drag `modulo`** (Check bar count)
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **count**: Integer (1 to 4)
*   **use_triplets**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14/15 (Inputs), GP16 (Output).
2.  **Reset**: `count = 1`.

**B. Main Loop Phase**
3.  **Check Modifiers**:
    *   If GP14: `do_accent = TRUE`.
    *   If GP15: `do_triplets = TRUE`.
4.  **Sound Logic**:
    *   **If `count` == 1 AND `do_accent`**: Beep LOUD (long pulse).
    *   **Else**: Beep SHORT.
5.  **Timing Subdivision**:
    *   If `do_triplets`: Play 3 quick clicks per second.
    *   Else: Play 1 click per second.
6.  **Progress Measure**:
    *   `count = (count + 1) % 4`.

### 9. Execution Flow
1.  **Ready**: System clicks steadily.
2.  **Accent**: User hits the "Accent" button. Now, the first beat of every four sounds sharper/higher.
3.  **Subdivision**: User hits "Triplets." The machine maintains the same BPM but clicks three times inside every single beat instead of once.
4.  **Feedback**: Provides a powerful practice environment for rhythm students.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
accent_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
tri_btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

beat = 0

while True:
    # Check beat type (Accent on 0)
    dur = 0.1 if (beat == 0 and accent_btn.value()) else 0.02
    
    if tri_btn.value():
        # Triplets mode: 3 pulses in 1 second
        for _ in range(3):
            buz.on(); time.sleep(dur); buz.off()
            time.sleep(0.33 - dur)
    else:
        # Standard mode: 1 pulse in 1 second
        buz.on(); time.sleep(dur); buz.off()
        time.sleep(1.0 - dur)
        
    beat = (beat + 1) % 4
```

### 11. Common Mistakes
*   **Timing Skew**: If the accent pulse is much longer than the standard pulse, the entire bar will stretch out unless you calculate the remaining `sleep` time properly.

### 12. Try This Next
*   **Visual Count**: Display "1", "2", "3", "4" on the OLED sync'd with the clicks.
"""

    p0596 = """
---

## 1. Project 0596: Smart Metronome Switch

### 2. Learning Objective
Programm an "Output Router" that allows the user to switch between an audible alarm (Buzzer) and a haptic alert (Vibration Motor / LED) for silent practice.

### 3. Concepts Introduced
*   Output Routing
*   Conditional Mapping
*   Haptic Feedback
*   UI Selection States

### 4. Hardware Required
*   Raspberry Pi Pico
*   Toggle Switch
*   Buzzer
*   Vibration Motor (or LED)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Silent Switch**| GP14 | Mode Selection |
| **Buzzer** | GP15 | Audible Output |
| **Vibrate/LED** | GP16 | Silent Output |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **is_silent**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO**: GP14 (Input), GP15/16 (Outputs).

**B. Main Loop Phase**
2.  **Read Mode**:
    *   `is_silent = GP14_READ`.
3.  **Route Signal**:
    *   **If `is_silent`**:
        *   Pulse GP16 (Vibration/LED).
        *   GP15 (Buzzer) stays OFF.
    *   **Else**:
        *   Pulse GP15 (Buzzer).
        *   GP16 stays OFF.
4.  **Wait**:
    *   Wait 1s between pulses.

### 9. Execution Flow
1.  **Audio Mode**: The metronome beeps normally.
2.  **Switching**: The user flips the physical toggle switch.
3.  **Reaction**: The code branch changes.
4.  **Haptic**: The speaker is silenced, and the vibration motor kicks in.
5.  **Use Case**: Allows a musician to feel the beat against their wrist without disturbing others in the room.

### 10. Generated Code
```python
from machine import Pin
import time

mode_sw = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)
vibrate = Pin(16, Pin.OUT)

while True:
    silent = mode_sw.value()
    
    if silent:
        # Haptic Tick
        vibrate.on(); time.sleep(0.1); vibrate.off()
    else:
        # Audio Tick
        buzzer.on(); time.sleep(0.05); buzzer.off()
    
    time.sleep(0.9) # BPM 60
```

### 11. Common Mistakes
*   **Floating Pins**: If the Vibration motor draws high current, it might cause the Buzzer to "crackel" due to noise. Power them separately if possible.

### 12. Try This Next
*   **Dual Mode**: Create a middle switch position that turns on BOTH sound and vibration.
"""

    p0597 = """
---

## 1. Project 0597: Metronome Alarm System

### 2. Learning Objective
Create a "Dynamic Volume Monitor" using a microphone sensor to detect if the performer's volume exceeds a reference "Quiet" threshold and signal a visual warning.

### 3. Concepts Introduced
*   Amplitude Thresholding
*   Analog Noise Sampling
*   Visual Overload Alerts
*   Feedback Loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor / Microphone (Analog)
*   Red LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Microphone** | GP26 (ADC) | Sound Level |
| **Warning LED** | GP16 | Alert Indicator |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Logic, drag `greater_than`**
*   **from Display, drag `pico_oled_clear`**

### 7. Variables
*   **noise_level**: Integer (Latest reading)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure**: ADC(26) and Output(16).

**B. Monitoring Phase**
2.  **Measure**:
    *   Read `noise_level` from ADC(26).
3.  **Evaluate**:
    *   If `noise_level` > 45000:
        *   Turn GP16 (Red LED) ON.
        *   Print "TOO LOUD!".
    *   Else:
        *   Turn GP16 OFF.
4.  **Loop Rate**:
    *   Check every 0.05s.

### 9. Execution Flow
1.  **Calibration**: System tracks background noise.
2.  **Performance**: The user begins playing an instrument along with the metronome.
3.  **Peak Detection**: If a drum hit or loud note is detected, the analog reading registers a high voltage.
4.  **Instruction**: The Red LED lights up as a "shush" signal, helping the user learn to manage their dynamics and play quieter.

### 10. Generated Code
```python
import machine
import time

mic = machine.ADC(26)
warning = machine.Pin(16, machine.Pin.OUT)

threshold = 40000

while True:
    # Sampling 100 times to get the 'peak'
    peak = 0
    for _ in range(100):
        val = mic.read_u16()
        if val > peak: peak = val
        
    if peak > threshold:
        warning.on()
        print(f"OVER VOLUME! Peak: {peak}")
    else:
        warning.off()
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Average vs Peak**: If you average the microphone values, you might never see a loud drum hit (which only lasts a millisecond). Monitoring for the "Maximum" reading over a short window is more effective.

### 12. Try This Next
*   **LED Meter**: Use 5 LEDs to create a "Volume Bar" that grows taller as the sound gets louder.
"""

    p0598 = """
---

## 1. Project 0598: The Metronome Game

### 2. Learning Objective
Simulate "Polyrhythmic" music by coordinating two buzzers to play different, competing rhythms (such as 3-against-4) simultaneously.

### 3. Concepts Introduced
*   Polyrhythms (Cross-rhythms)
*   LCM (Least Common Multiple)
*   Asynchronous Beats
*   Mathematical Percussion

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buzzers (or Piezo speakers)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer A** | GP16 | Rhtyhm 1 (e.g. 3 beats) |
| **Buzzer B** | GP17 | Rhythm 2 (e.g. 4 beats) |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `modulo`**
*   **from Logic, drag `if_do`**

### 7. Variables
*   **interval1, interval2**: Integer (Gap lengths)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Mastery**: Total cycle time = 1200ms.
2.  **Logic**:
    *   Buzzer A needs 3 beats in 1200ms $\Rightarrow$ Beat every **400ms**.
    *   Buzzer B needs 4 beats in 1200ms $\Rightarrow$ Beat every **300ms**.

**B. Parallel Loop Phase**
3.  **Process A**:
    *   If `current_ms % 400 == 0`: Beep Buzzer A.
4.  **Process B**:
    *   If `current_ms % 300 == 0`: Beep Buzzer B.
5.  **Synchronization**:
    *   Both will beep together exactly at 0ms and 1200ms.

### 9. Execution Flow
1.  **Complexity**: The system calculates the subdivision of time.
2.  **Sound**: The user hears two distinct "speeds" happening at once.
3.  **Perception**: The human brain combines these into a complex 3-against-4 pattern.
4.  **Utility**: Essential training for jazz and classical percussionists.

### 10. Generated Code
```python
import machine, time

# Setup two pins
b_a = machine.Pin(16, machine.Pin.OUT)
b_b = machine.Pin(17, machine.Pin.OUT)

start = time.ticks_ms()

while True:
    now = time.ticks_diff(time.ticks_ms(), start)
    
    # 3 in 1200ms (every 400)
    if now % 400 < 5:
        b_a.on(); time.sleep(0.01); b_a.off()
    
    # 4 in 1200ms (every 300)
    if now % 300 < 5:
        b_b.on(); time.sleep(0.01); b_b.off()
        
    if now > 1200: start = time.ticks_ms()
    time.sleep(0.001)
```

### 11. Common Mistakes
*   **Modulo Drift**: If the subtraction logic isn't perfect, the two rhythms will slowly drift apart. Use the `ticks_diff` anchor to keep them locked.

### 12. Try This Next
*   **Pitch Difference**: Use a high pitch for Buzzer A and a low pitch for Buzzer B so they are easy to tell apart.
"""

    p0599 = """
---

## 1. Project 0599: Automated Metronome

### 2. Learning Objective
Create a "Speed Trainer" that automatically increases the tempo by 5 BPM every 4 bars, forcing the musician to gradually play faster.

### 3. Concepts Introduced
*   Auto-Incrementing Loops
*   Bar Counting
*   Dynamic Tempo Calculation
*   Skill Training Automation

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Trainer Output**| GP15 | Speed Clock |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Loops, drag `repeat`** (Measure loop)
*   **from Math, drag `arithmetic`**

### 7. Variables
*   **bpm**: Integer (60 -> 120)
*   **bar**: Integer (1 to 4)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start**: `bpm = 60`.

**B. Training Loop Phase**
2.  **Execute Bar**:
    *   Repeat 4 times:
        *   Beep Buzzer.
        *   Wait `60 / bpm` seconds.
3.  **Increase Intensity**:
    *   Print "LEVEL UP! Set BPM to [bpm + 5]".
    *   Add 5 to `bpm`.
4.  **Safety Limit**:
    *   If `bpm` > 160: Return to 60.

### 9. Execution Flow
1.  **Automation**: The metronome starts out very slow and easy.
2.  **Transition**: Every 16 beats (4 bars of 4), the speed noticeably jumps.
3.  **Benefit**: The user doesn't have to stop playing to reach over and turn a knob—the "Coach" (Pico) does it for them.
4.  **Repeat**: The process continues until the user can no longer keep up.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
bpm = 60

while True:
    print(f"MODE: Training at {bpm} BPM")
    
    # Run for 16 beats (4 bars)
    for _ in range(16):
        buz.on(); time.sleep(0.02); buz.off()
        time.sleep((60/bpm) - 0.02)
    
    # Level Up
    bpm += 5
    if bpm > 200: bpm = 60
```

### 11. Common Mistakes
*   **Too Fast**: If the increments are too high (e.g., 20 BPM), the user will lose their rhythm during the transition. Stick to 2-5 BPM jumps.

### 12. Try This Next
*   **OLED Display**: Show a "Goal" text—"Can you hit 120 BPM?".
"""

    p0600 = """
---

## 1. Project 0600: Mastering Metronome

### 2. Learning Objective
Introduce the "Standard MIDI Protocol" by using the UART serial interface to send digital music messages to an external synthesizer or PC.

### 3. Concepts Introduced
*   MIDI Protocol (Note ON/OFF)
*   UART Communication
*   Baud Rate (31250 bps)
*   Data Packet Structure (Hex)

### 4. Hardware Required
*   Raspberry Pi Pico
*   USB-to-MIDI cable or MIDI 5-Pin connector

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MIDI Serial Out**| GP0 (TX) | Serial data stream |
| **GND** | GND | Common ground |

### 6. Blocks Used
*   **from Communication, drag `pico_uart_init`** (31250 bps)
*   **from Communication, drag `pico_uart_write`** (Binary data)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Protocol-standard byte arrays.

### 8. Step-by-Step Guide

**A. Communication Setup**
1.  **Initiate UART**: Set UART0 on GP0/1 with **Baud Rate = 31250**. (This is the strict global standard for MIDI).

**B. Main Loop Phase**
2.  **Send "Note ON" (Middle C)**:
    *   Send 3 Bytes: `0x90` (Note On Channel 1), `0x3C` (Note 60 = Middle C), `0x64` (Velocity 100).
3.  **Timing**:
    *   Wait 0.5s.
4.  **Send "Note OFF"**:
    *   Send 3 Bytes: `0x80` (Note Off), `0x3C` (Middle C), `0x00` (Velocity 0).
5.  **Loop**:
    *   Wait 0.5s.

### 9. Execution Flow
1.  **Protocol**: The Pico doesn't send audio; it sends "instructions."
2.  **Link**: A computer or keyboard receives these packets and produces the sound.
3.  **Result**: The Pico becomes a digital metronome for pro-grade music equipment, capable of triggering grand pianos or electronic beats.
4.  **Completion**: You have successfully mastered the bridge between binary code and musical performance!

### 10. Generated Code
```python
import machine, time

# MIDI Standard Baud Rate
uart = machine.UART(0, baudrate=31250, tx=machine.Pin(0), rx=machine.Pin(1))

# Channel 1 Note ON Command
def note_on(note, vel):
    uart.write(bytearray([0x90, note, vel]))

# Channel 1 Note OFF Command
def note_off(note):
    uart.write(bytearray([0x80, note, 0x00]))

while True:
    # Play Middle C (60)
    note_on(60, 100)
    time.sleep(0.5)
    note_off(60)
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Baud Rate**: Using 9600 or 115200. External MIDI devices ONLY talk at 31250. Any other speed results in "garbage" data.
*   **Logic Voltage**: The Pico is 3.3V. Some old 5V MIDI gear might need a level shifter, though many work with 3.3V.

### 12. Try This Next
*   **Arpeggio**: Use a loop to play a scale ($60, 62, 64, 65...$) instead of just one note.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0591 + p0592 + p0593 + p0594 + p0595 + p0596 + p0597 + p0598 + p0599 + p0600)
    
    print("Batch 60 (0591-0600) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch60()
