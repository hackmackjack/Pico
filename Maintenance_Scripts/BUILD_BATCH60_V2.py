import os

def build_batch60_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0591 = """
---

# Batch 60: Metronome 3

## 1. Project 0591: Introduction to Metronome

### 2. Learning Objective
Programm a "Visual Tick" metronome that flashes the OLED screen white for 50ms on every beat to provide a high-contrast tempo guide.

### 3. Concepts Introduced
*   Visual Synchronization
*   Duration Control (Pulse width)
*   Display Strobing
*   Frequency to Interval conversion

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
1.  **Init Header**:
    *   From **Display**, `clear` and `text` "BPM: 60" center.
    *   **Snap** into `start`.
    *   `show`.

**B. Main Loop Phase**
1.  **Apply Tick**:
    *   From **Loops**, drag `pico_forever`.
2.  **Visual Flash**:
    *   From **Display**, drag `pico_oled_invert` (Set 1).
    *   **Snap** into loop.
    *   From **Time**, wait 0.05s.
    *   From **Display**, drag `pico_oled_invert` (Set 0).
3.  **Wait for Cycle**:
    *   From **Time**, wait 0.95s. (Total = 1.0s for 60 BPM).

### 9. Execution Flow
1.  **Start**: The screen displays "BPM: 60".
2.  **Output**: The hardware command `invert(1)` turns the whole screen from black to white instantly.
3.  **Delay**: The system holds the "Light" for 50 milliseconds.
4.  **Reaction**: The screen turns black again.
5.  **Output**: Creates a sharp visual "Pop" that acts as a conductor's baton.
6.  **Repeat**: Repeats at a precise 1-second cadence.

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0); oled.text("BPM: 60", 35, 25); oled.show()

while True:
    # Strobe White
    oled.invert(1)
    time.sleep(0.05)
    
    # Strobe Black
    oled.invert(0)
    time.sleep(0.95)
```

### 11. Common Mistakes
*   **Delay Error**: Waiting for exactly 1.0s *after* the 0.05s flash. This would make the real tempo 1.05s (57 BPM). Always subtract the flash time from the main wait.

### 12. Try This Next
*   **Speed Up**: Change the wait to `0.45s` for a 120 BPM tempo.
"""

    p0592 = """
---

## 1. Project 0592: Blinking Metronome

### 2. Learning Objective
Implement a "Leader" count-in sequence where an LED flashes 4 times slowly before the Audible Metronome (Buzzer) begins its cycle.

### 3. Concepts Introduced
*   Lead-in Sequences
*   Phase Transitions
*   Visual-to-Audio handover
*   State Initialization

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED, Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Preparation LED**| GP16 | Visual Count-in |
| **Sound Buzzer**   | GP15 | Rhythm Output |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Count 4)
*   **from Smart IO, drag `pico_buzzer_beep`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Sequential lead-in project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Count-in Phase**:
    *   From **Loops**, drag `repeat` 4 times.
    *   **Snap** into `start`.
2.  **Flicker LED**:
    *   From **Smart IO**, set GP16 HIGH. Wait 0.1s.
    *   Set GP16 LOW. Wait 0.9s.
    *   **Snap** inside repeat.

**B. Main Loop Phase**
1.  **Audible Mode**:
    *   From **Loops**, drag `pico_forever`.
2.  **Synchronize**:
    *   From **Smart IO**, set GP16 HIGH.
    *   From **Smart IO**, pulse GP15 (Buzzer) for 0.05s.
    *   **Snap** into loop.
3.  **Finish Cycle**:
    *   From **Smart IO**, set GP16 LOW.
    *   From **Time**, wait 0.95s.

### 9. Execution Flow
1.  **Start**: The LED flashes 4 times silently.
2.  **Preparation**: This gives a musician exactly 4 seconds to prepare their instrument.
3.  **Process**: The code moves out of the `repeat` block into the `forever` loop.
4.  **Audio**: The buzzer starts "clicking" in perfect sync with the LED.
5.  **Output**: Provides a professional-grade "Count-in" behavior found in stage equipment.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(16, Pin.OUT)
buz = Pin(15, Pin.OUT)

# PHASE 1: SILENT LEAD-IN
for i in range(4):
    print(f"COUNT-IN: {i+1}")
    led.on(); time.sleep(0.1); led.off()
    time.sleep(0.9)

# PHASE 2: ACTIVE METRONOME
print("LIVE")
while True:
    led.on()
    buz.on(); time.sleep(0.02); buz.off() # Short click
    time.sleep(0.98) # Total 1s
    led.off()
```

### 11. Common Mistakes
*   **Click Duration**: Making the buzzer beep for 0.5s. It should be a tiny "Tick" (0.01-0.03s) to sound like a real metronome.

### 12. Try This Next
*   **Accent on 1**: Make the buzzer beep for a slightly longer duration (0.1s) on every 4th beat to mark the start of the bar.
"""

    p0593 = """
---

## 1. Project 0593: Manual Metronome Control

### 2. Learning Objective
Develop a "Tap Tempo" sampler that calculates the average interval between 4 consecutive button taps to set the metronome speed.

### 3. Concepts Introduced
*   Interval Averaging
*   Tap-to-BPM conversion
*   Microsecond Sampling
*   Variable Timelines

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tempo Button**| GP14 | User interaction |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Variables, drag `change_variable`**
*   **from Math, drag `division`**

### 7. Variables
*   **total_ms**: Integer (Accumulator)
*   **bpm**: Integer (Calculated)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Sample Size**:
    *   `print` "Tap the button twice to start...".

**B. Configuration Phase**
1.  **Capture Start**:
    *   Wait for Button GP14. Set `start_ms` = milliseconds.
2.  **Capture End**:
    *   Wait for Button GP14. Set `end_ms` = milliseconds.
3.  **Calculate BPM**:
    *   From **Variables**, set `gap` = `end_ms` - `start_ms`.
    *   **Action**: `bpm = 60000 / gap`.

**C. Active Phase**
1.  **Execute Tempo**:
    *   From **Loops**, drag `pico_forever`.
2.  **Tick**:
    *   Pulse Buzzer.
    *   From **Time**, wait `gap` / 1000 seconds.

### 9. Execution Flow
1.  **Start**: System waits for user rhythm.
2.  **Interact**: User taps the button twice along to a song.
3.  **Process**: The Pico calculates the "Gap" (delta) between the two taps.
4.  **Math**: 60,000 divided by the gap (in ms) gives the Beats Per Minute.
5.  **Output**: The metronome begins clicking at the exact frequency of the user's hand taps.
6.  **Utility**: Essential for syncing electronics with live musicians.

### 10. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
buz = Pin(15, Pin.OUT)

print("TAP TWICE...")
while not btn.value(): pass
t1 = time.ticks_ms()
time.sleep(0.3) # Debounce

while not btn.value(): pass
t2 = time.ticks_ms()
gap = time.ticks_diff(t2, t1)

print(f"SYNC TO: {int(60000/gap)} BPM")

while True:
    buz.on(); time.sleep(0.01); buz.off()
    time.sleep(gap/1000 - 0.01)
```

### 11. Common Mistakes
*   **Double Trigger**: Without the 0.3s sleep after the first tap, a single "long press" might count as two taps, resulting in a 0ms gap and a math error.

### 12. Try This Next
*   **OLED Display**: Show the calculated BPM text on the OLED after a tap is finished.
"""

    p0594 = """
---

## 1. Project 0594: Metronome Sequences

### 2. Learning Objective
Programm a "Clave Rhythm" generator that plays the "Son Clave" (3-2) beat pattern using a list of specific delay durations.

### 3. Concepts Introduced
*   Syncopation Logic
*   Rhythmic Tuples
*   Musical Intervals
*   Pattern Looping

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Output Tick** | GP15 | Rhythm Speaker |

### 6. Blocks Used
*   **from List, drag `create_list`** (Storing the gap pattern)
*   **from Loops, drag `for_each`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **gap_pattern**: List (Wait times)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Groove**:
    *   From **Variables**, set `gap_pattern` to List [0.4s, 0.4s, 0.4s, 0.2s, 0.4s].

**B. Main Loop Phase**
1.  **Execute Sequence**:
    *   From **Loops**, drag `pico_forever`.
2.  **Iterate Taps**:
    *   From **Loops**, drag `for_each` (Item in `gap_pattern`).
    *   **Snap** into loop.
3.  **Perform Hit**:
    *   From **Smart IO**, pulse GP15 for 0.02s.
4.  **Apply Groove**:
    *   From **Time**, drag `pico_wait` and set to variable `Item`.
    *   **Snap** below pulse.

### 9. Execution Flow
1.  **Start**: The code enters the sequencer loop.
2.  **Process**: Instead of a steady beat, it reads different numbers from a list.
3.  **Output**: A series of offset clicks is produced.
4.  **Reaction**: The pattern feels "synchopated" and "musical," mimicking complex Afro-Cuban rhythms.
5.  **Repeat**: The entire 5-note "Son Clave" pattern loops endlessly.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)

# 3-2 Clave pattern gaps
clave = [0.4, 0.4, 0.4, 0.2, 0.4]

while True:
    for gap in clave:
        buz.on(); time.sleep(0.01); buz.off()
        time.sleep(gap)
```

### 11. Common Mistakes
*   **Floating-point precision**: If the list values are too small (e.g., 0.001), the buzzer might not be able to physically keep up.

### 12. Try This Next
*   **Swing**: Add a variable that slightly increases every 2nd number to create a "human feel" swing to the beat.
"""

    p0595 = """
---

## 1. Project 0595: Interactive Metronome

### 2. Learning Objective
Build an "Accented Metronome" with dynamic modifiers where button A toggles "Accent on 1" and button B toggles "Triplets" mode.

### 3. Concepts Introduced
*   Musical Emphasis (Accents)
*   Rhythmic Subdivisions (Triplets)
*   Modifier States
*   Dynamic Logic branching

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons, Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accent Toggle**| GP14 | Strong beat 1 |
| **Triplet Toggle**| GP15 | Division switch |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Math, drag `modulo`** (To check bar 1)
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **count**: Integer (1 to 4)
*   **is_accent**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Default**:
    *   `count = 1`.

**B. Main Loop Phase**
1.  **Check Beat**:
    *   From **Loops**, drag `pico_forever`.
2.  **Evaluate Accent**:
    *   From **Logic**, if (`count` == 1) AND (GP14 is HIGH):
        *   **Action**: Beep for 0.1s (Loud/High).
    *   **Else**:
        *   **Action**: Beep for 0.02s (Standard).
3.  **Evaluate Division**:
    *   From **Logic**, if (GP15 is HIGH):
        *   **Action**: Repeat 3 times (Triplets).
        *   Wait 0.3s.
    *   **Else**:
        *   Wait 1.0s.
4.  **Increment Bar**:
    *   `count = (count + 1)`. If > 4 set to 1.

### 9. Execution Flow
1.  **Start**: Metronome clicks normally 1-2-3-4.
2.  **Interact**: User hits "Accent" button.
3.  **Process**: The system uses the `modulo` operation to find the first beat of the measure.
4.  **Output**: Beat 1 now sounds longer and sharper than 2, 3, and 4.
5.  **Interact**: User toggles "Triplets." The machine switches from 1 click per second to 3 clicks per second.
6.  **Utility**: Demonstrates how simple code can manage complex музыкальная theory.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
bt_a = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bt_b = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

beat = 0

while True:
    # 1. Accent Logic
    if beat == 0 and bt_a.value():
        dur = 0.1
    else:
        dur = 0.02
        
    # 2. Division Logic
    if bt_b.value():
        # Triplets (3 hits in 1s)
        for _ in range(3):
            buz.on(); time.sleep(dur); buz.off()
            time.sleep(0.33 - dur)
    else:
        # Standard
        buz.on(); time.sleep(dur); buz.off()
        time.sleep(1.0 - dur)
        
    beat = (beat + 1) % 4
```

### 11. Common Mistakes
*   **Timing Drift**: If the accent tone takes 0.1s and the normal tone 0.02s, the whole measure will slow down unless you subtract the specific `dur` from your `sleep` time.

### 12. Try This Next
*   **Visual Beat**: Show a "Diamond" on the OLED that grows on beat 1 and stays small on 2, 3, 4.
"""

    p0596 = """
---

## 1. Project 0596: Smart Metronome Switch

### 2. Learning Objective
Programm an "Output Swapper" that redirects the rhythmic pulse from an Audible Buzzer (Sound) to a Vibration Motor (Haptic) for silent private direct-contact use.

### 3. Concepts Introduced
*   Signal Routing
*   Haptic Feedback
*   Environment Awareness
*   Output Mapping

### 4. Hardware Required
*   Raspberry Pi Pico
*   Toggle Switch, Buzzer, Vibration Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Mode Switch**  | GP14 | Silent mode |
| **Vibrate Out**  | GP16 | Haptic output |
| **Audio Out**    | GP15 | Buzzer output |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Text, drag `print`**

### 7. Variables
*   **is_silent**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   Set GP14 (Input), GP15/16 (Outputs).

**B. Main Loop Phase**
1.  **Read Mode**:
    *   From **Variables**, set `is_silent` to **Smart IO** `pico_gpio_read` 14.
2.  **Route Signal**:
    *   From **Logic**, drag `if_else`.
    *   **If `is_silent` is TRUE**:
        *   **Action**: Set GP16 (Vibrate) HIGH for 0.1s.
        *   **Action**: Ensure GP15 (Audio) is LOW.
    *   **Else (AUDIO)**:
        *   **Action**: Pulse GP15 (Buzzer) for 0.01s.
        *   **Action**: Ensure GP16 is LOW.
3.  **Hold Cadence**:
    *   Wait 0.9s (Total 1s cycle).

### 9. Execution Flow
1.  **Start**: Switch is in "Audio" mode. The metronome beeps normally.
2.  **Interact**: User flips the switch to "Silent."
3.  **Process**: The `is_silent` variable is updated via the physical pin.
4.  **Output**: The buzzer stops. The vibration motor kicks in.
5.  **Perception**: The user can now *feel* the beat in their pocket or on their wrist without making any noise.
6.  **Repeat**: Continues rhythmically until power off.

### 10. Generated Code
```python
from machine import Pin
import time

sw = Pin(14, Pin.IN, Pin.PULL_DOWN)
audio = Pin(15, Pin.OUT)
haptic = Pin(16, Pin.OUT)

while True:
    if sw.value():
        # SILENT MODE (Haptic)
        haptic.on(); time.sleep(0.1); haptic.off()
    else:
        # LOUD MODE (Buzzer)
        audio.on(); time.sleep(0.01); audio.off()
        
    time.sleep(0.9)
```

### 11. Common Mistakes
*   **Motor Noise**: Vibration motors can create electrical noise that resets the Pico. Use a small capacitor across the motor terminals if resets occur.

### 12. Try This Next
*   **Visual Silent**: Use the OLED to show a big flashing "!" in sync with the vibration.
"""

    p0597 = """
---

## 1. Project 0597: Metronome Alarm System

### 2. Learning Objective
Create a "Dynamic Volume Monitor" using a microphone sensor to detect if the performer's volume exceeds a reference "Quiet" threshold and signal a visual warning on a Red LED.

### 3. Concepts Introduced
*   Amplitude Thresholding
*   Analog Noise Sampling
*   Visual Overload Alerts
*   Environment Monitoring

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor (Analog), Red LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Noise ADC**    | GP26 | Volume input |
| **Warning Lamp** | GP16 | Alert output |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_adc_read`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **noise_max**: Integer (Peak detect)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep IO**:
    *   Set GP16 to LOW.

**B. Main Loop Phase**
1.  **Sample Sound**:
    *   From **Loops**, repeat 100 times:
        *   If `pico_adc_read` 26 > `noise_max`: `noise_max` = reading.
2.  **Check Peak**:
    *   From **Logic**, if `noise_max` > 40000:
        *   **Action**: Set GP16 HIGH.
        *   **Action**: Print "TOO LOUD!".
    *   **Else**:
        *   **Action**: Set GP16 LOW.
3.  **Reset**:
    *   `noise_max = 0`. Wait 0.01s.

### 9. Execution Flow
1.  **Start**: Pico begins measuring ambient kitchen or practice room noise.
2.  **Process**: The system ignores averages and looks for "Spikes" (loud drum hits or shouts).
3.  **Sense**: The peak volume crosses the 40,000 threshold.
4.  **Output**: The Red LED flashes instantly.
5.  **Reaction**: The performer sees the light and knows to "Quiet down" to maintain musical dynamics.
6.  **Repeat**: Performs this check hundreds of times per second.

### 10. Generated Code
```python
import machine, time

mic = machine.ADC(26)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    peak = 0
    # Windowed Peak Detection
    for _ in range(100):
        val = mic.read_u16()
        if val > peak: peak = val
        
    if peak > 40000:
        led.on()
        print(f"SHHH! VOLUME: {peak}")
    else:
        led.off()
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Averaging**: If you take the average volume of 1 second, a loud single clap will be mathematically "hidden." You must use a "Peak" variable to catch short loud events.

### 12. Try This Next
*   **Volume Bar**: Use a series of 5 LEDs where more LEDs light up as the sound gets louder.
"""

    p0598 = """
---

## 1. Project 0598: The Metronome Game

### 2. Learning Objective
Simulate "Polyrhythmic" music by coordinating two buzzers to play different, competing rhythms (such as 3-against-4) simultaneously using timestamp math.

### 3. Concepts Introduced
*   Polyrhythms (Cross-rhythms)
*   LCM Coordination
*   Mathematical Percussion
*   Asynchronous Loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buzzers (or Piezo speakers)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer 1 (3)** | GP16 | Channel A |
| **Buzzer 2 (4)** | GP17 | Channel B |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `modulo`**
*   **from Logic, drag `if_do`**

### 7. Variables
*   **now_ms**: Integer (Timestamp anchor)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sync Cycle**:
    *   From **Variables**, set `start_tick` to `pico_milliseconds`.
    *   (Total cycle = 1200ms).

**B. Main Loop Phase**
1.  **Track Time**:
    *   From **Loops**, drag `pico_forever`.
    *   `current = pico_milliseconds - start_tick`.
2.  **Task A (3 beats)**:
    *   From **Logic**, if (`current` % 400) < 10:
        *   **Action**: Beep GP16.
3.  **Task B (4 beats)**:
    *   From **Logic**, if (`current` % 300) < 10:
        *   **Action**: Beep GP17.
4.  **Reset Cycle**:
    *   If `current` > 1200: `start_tick = pico_milliseconds`.

### 9. Execution Flow
1.  **Process**: The CPU divides time into a 1.2-second window.
2.  **Output**: Buzzer 1 beeps every 400ms (3 times total).
3.  **Output**: Buzzer 2 beeps every 300ms (4 times total).
4.  **Reaction**: The human ear combines these into a complex "3-against-4" pattern.
5.  **Output**: Both beeps will happen at exactly the same time once every 1200ms.
6.  **Utility**: Essential training for advanced percussionists.

### 10. Generated Code
```python
import machine, time

b1 = machine.Pin(16, machine.Pin.OUT)
b2 = machine.Pin(17, machine.Pin.OUT)

start = time.ticks_ms()

while True:
    now = time.ticks_diff(time.ticks_ms(), start)
    
    # 3 Beats in 1.2s (every 400ms)
    if now % 400 < 5:
        b1.on(); time.sleep(0.01); b1.off()
        
    # 4 Beats in 1.2s (every 300ms)
    if now % 300 < 5:
        b2.on(); time.sleep(0.01); b2.off()
        
    if now > 1200: start = time.ticks_ms()
    time.sleep(0.001)
```

### 11. Common Mistakes
*   **Overlapping Loop**: If you use `time.sleep(0.1)` at the end of the loop, you might "skip" the 5ms window where the beep is supposed to happen. Keep the loop speed very high.

### 12. Try This Next
*   **Tonal Difference**: Use PWM to make the "3" buzzer sound like a low drum and the "4" buzzer sound like a high bell.
"""

    p0599 = """
---

## 1. Project 0599: Automated Metronome

### 2. Learning Objective
Create a "Speed Trainer" that automatically increases the tempo by 5 BPM every 4 bars, forcing the musician to gradually play faster.

### 3. Concepts Introduced
*   Auto-Incrementing States
*   Dynamic Duty-Cycle Math
*   Musical Intensity Ramping
*   Scheduled Transmissions

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pacer Out**    | GP15 | Speed guide |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Bar counter)
*   **from Variables, drag `change_variable`**
*   **from Math, drag `arithmetic`**

### 7. Variables
*   **current_bpm**: Integer (60 to 180)
*   **bar_count**: Integer (Loop index)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start Speed**:
    *   From **Variables**, set `current_bpm` to 60.

**B. Main Loop Phase**
1.  **Master Schedule**:
    *   From **Loops**, drag `pico_forever`.
2.  **Execute Bar**:
    *   From **Loops**, repeat 16 times (4 bars of 4).
    *   Pulse GP15.
    *   From **Time**, wait (60 / `current_bpm`) seconds.
    *   **Snap** into loop.
3.  **Increase Intensity**:
    *   From **Text**, print "ACCELERATING! Target: [current_bpm + 5] BPM".
    *   From **Variables**, change `current_bpm` by 5.

### 9. Execution Flow
1.  **Start**: The metronome begins at a slow walking pace (60 BPM).
2.  **Process**: The user plays their instrument along to the beat.
3.  **Condition**: Once 16 beats have passed, the code finishes the segment.
4.  **Reaction**: The BPM variable jumps up to 65.
5.  **Output**: The clicks noticeably speed up.
6.  **Repeat**: Continues until the player is forced to stop, providing an automated "Coach" experience.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
bpm = 60

while True:
    print(f"PRACTICE LEVEL: {bpm} BPM")
    # 4 bars of 4/4
    for _ in range(16):
        buz.on(); time.sleep(0.02); buz.off()
        time.sleep((60/bpm) - 0.02)
        
    bpm += 5
    if bpm > 220: bpm = 60 # Reset if too crazy
```

### 11. Common Mistakes
*   **Missing Step**: If you increase BPM every 1 bar, it's too jerky. 4 bars gives the human brain enough time to "settle" into the new tempo.

### 12. Try This Next
*   **OLED Goal**: Print "Can you hit level 100?" on the OLED and show the current score.
"""

    p0600 = """
---

## 1. Project 0600: Mastering Metronome

### 2. Learning Objective
Introduce the "Standard MIDI Protocol" by using the UART serial interface to send digital music messages to an external PC synthesizer at exactly 31,250 bits per second.

### 3. Concepts Introduced
*   MIDI Protocol (Note ON/OFF)
*   UART Communication
*   Baud Rate Standards
*   Packet Structuring (Hex Bytes)

### 4. Hardware Required
*   Raspberry Pi Pico
*   USB-to-MIDI cable or MIDI 5-Pin connector

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MIDI TX**      | GP0 | Serial data stream |
| **GND**          | GND | Common ground |

### 6. Blocks Used
*   **from Communication, drag `pico_uart_init`** (31250 baud)
*   **from Communication, drag `pico_uart_write`** (Hex list)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **None**: Protocol-standard byte transmissions.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Protocol Speed**:
    *   From **Communication**, init UART0 at **31250** Baud Rate. (Absolute standard).

**B. Main Loop Phase**
1.  **Send Note ON**:
    *   From **Communication**, drag `pico_uart_write`.
    *   Value: `[0x90, 60, 100]`. (Channel 1, Middle C, Loud).
2.  **Hold Beat**:
    *   From **Time**, wait 0.5s.
3.  **Send Note OFF**:
    *   From **Communication**, drag `pico_uart_write`.
    *   Value: `[0x80, 60, 0]`. (Stop Note 60).
4.  **Hold Gap**:
    *   From **Time**, wait 0.5s.

### 9. Execution Flow
1.  **Process**: The Pico doesn't send audio waves; it sends "instructions."
2.  **Output**: A 3-byte packet is beamed out of GP0 every half second.
3.  **Reaction**: An external synthesizer receives the packet and "plays" its internal piano/synth sound.
4.  **Result**: You have successfully bridged the gap between basic electronics and professional music production standards!
5.  **Completion**: Project 0600 marks the end of the intermediate level!

### 10. Generated Code
```python
import machine, time

# MIDI Standard Baud Rate
midi_uart = machine.UART(0, baudrate=31250, tx=machine.Pin(0), rx=machine.Pin(1))

while True:
    # 1. SEND NOTE ON
    midi_uart.write(bytearray([0x90, 60, 100]))
    time.sleep(0.5)
    
    # 2. SEND NOTE OFF
    midi_uart.write(bytearray([0x80, 60, 0]))
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Wrong Baud Rate**: If you use 9600 or 115200, the external computer will see "gibberish" characters. MIDI and only MIDI requires 31250.

### 12. Try This Next
*   **Scale player**: Change the number `60` in the loop to a variable that increases every time to play a rising melody.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0591 + p0592 + p0593 + p0594 + p0595 + p0596 + p0597 + p0598 + p0599 + p0600)
    
    print("Batch 60 (0591-0600) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch60_v2()
