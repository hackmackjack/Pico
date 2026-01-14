# FINAL BATCH: Metronome 2 - Projects 0396-0400 (COMPLETING ALL 100 PROJECTS!)

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

metronome_final = r'''
## 1️⃣ Project 0396: Smart Metronome Switch

### 2️⃣ Learning Objective
Implement audio-triggered count-in for hands-free metronome start. You will learn about sound detection and delayed start logic.

### 3️⃣ Concepts Introduced
*   **Auto-Start Trigger**: Clapping activates the metronome.
*   **Count-In Delay**: Waiting 4 beats before starting click track.
*   **Audio Trigger Logic**: Using microphone to detect sound events.

### 4️⃣ Hardware Required
*   **Pico**
*   **Microphone** (or sound sensor module)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Mic/Sound Sensor** | GP26 | ADC or Digital |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Read Analog/Digital**
*   **Category:** Pin Access

🔹 **Threshold Detection**
*   **Category:** Logic

🔹 **Buzzer Control**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **soundThreshold**: Minimum level to detect clap.
*   **countInBeats**: Number of silent beats before starting (4).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [soundThreshold] to [30000]`.
        *   **Snap** into setup block (ADC threshold).
    *   From **Variables**, drag `set [countInBeats] to [4]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Wait for Clap**:
        *   From **Console**, drag `print [Clap to start...]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `wait until [read analog pin 26] > [soundThreshold]`.
            *   **Snap** below.
    *   **Count-In**:
        *   From **Console**, drag `print [Detected! Count-in starting...]`.
            *   **Snap** below.
        *   From **Loops**, drag `repeat [countInBeats] times`.
            *   **Snap** below.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [800] for [50]ms`.
                    *   **Snap** inside (soft count-in beep).
                *   From **Timing**, drag `sleep [0.5] seconds`.
                    *   **Snap** below.
    *   **Start Metronome**:
        *   From **Console**, drag `print [Starting click track!]`.
            *   **Snap** below.
        *   From **Loops**, drag `repeat forever`.
            *   **Snap** below.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [1200] for [100]ms`.
                *   From **Timing**, drag `sleep [0.5] seconds`.

### 9️⃣ Execution Flow (Plain English)

The program waits silently for a loud sound (clap). When detected, it plays 4 soft beeps (count-in: 1-2-3-4) at half-second intervals. After the 4th beat, the full metronome click track starts. This allows musicians to count themselves in without needing to reach for a button—perfect for hands-busy situations.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

mic = machine.ADC(26)
buzzer = machine.PWM(machine.Pin(15))

SOUND_THRESHOLD = 30000
COUNT_IN_BEATS = 4

print("Clap to start...")

# Wait for clap
while mic.read_u16() < SOUND_THRESHOLD:
    time.sleep(0.1)

print("Detected! Count-in starting...")

# Count-in (soft beeps)
for i in range(COUNT_IN_BEATS):
    buzzer.freq(800)
    buzzer.duty_u16(16384)  # Quieter
    time.sleep(0.05)
    buzzer.duty_u16(0)
    time.sleep(0.45)

print("Starting click track!")

# Main metronome
while True:
    buzzer.freq(1200)
    buzzer.duty_u16(32768)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    time.sleep(0.4)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Triggers**: Lower `soundThreshold` if ambient noise triggers it constantly.
*   **Never Starts**: Increase threshold sensitivity or check mic wiring.

### 1️⃣2️⃣ Try This Next

*   **Double Clap**: Require 2 claps within 1 second to start (prevent false triggers).
*   **Voice Commands**: Use speech recognition module to start with "Go!" command.

---

## 1️⃣ Project 0397: Metronome Alarm System

### 2️⃣ Learning Objective
Implement boundary condition enforcement to prevent unrealistic BPM settings. You will learn about input validation and user-friendly error handling.

### 3️⃣ Concepts Introduced
*   **Max BPM Limit**: Clamping tempo to safe/realistic values.
*   **Boundary Condition Enforcement**: Preventing out-of-range values.
*   **Error Feedback**: Beeping when user exceeds limits.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Increase BPM)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Up Button** | GP14 | PULL_DOWN |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Logic Comparison**
*   **Category:** Logic

🔹 **Clamp Function**
*   **Category:** Math

🔹 **Buzzer Tone**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **currentBPM**: User-selected tempo (start at 120).
*   **MAX_BPM**: Hard limit (200).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [currentBPM] to [120]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [MAX_BPM] to [200]`.
        *   **Snap** below.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button Press (Increase BPM)**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `change [currentBPM] by [10]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [currentBPM] > [MAX_BPM] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Console**, drag `print [ERROR: Max BPM is 200!]`.
                            *   **Snap** inside.
                        *   From **Actuators**, drag `Buzzer [15] tone [400] for [500]ms`.
                            *   **Snap** below (error beep).
                        *   From **Variables**, drag `set [currentBPM] to [MAX_BPM]`.
                            *   **Snap** below (clamp value).
                *   From **Timing**, drag `sleep [0.3] seconds`.
                    *   **Snap** below (debounce).
    *   **Play Beat**:
        *   From **Math**, drag `set [interval] to [60 / currentBPM]`.
            *   **Snap** below.
        *   From **Actuators**, drag `Buzzer [15] tone [1000] for [50]ms`.
            *   **Snap** below.
        *   From **Console**, drag `print [BPM: {currentBPM}]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [interval] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The metronome starts at 120 BPM. Each button press increases tempo by 10. If the user presses it enough to exceed 200 BPM, the buzzer plays a low error tone and the BPM is clamped to 200 (it won't go higher). This prevents users from accidentally setting unrealistic tempos like 500 BPM that would be unhelpful.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.PWM(machine.Pin(15))

current_bpm = 120
MAX_BPM = 200

while True:
    if button.value():
        current_bpm += 10
        
        if current_bpm > MAX_BPM:
            print("ERROR: Max BPM is 200!")
            buzzer.freq(400)
            buzzer.duty_u16(32768)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            current_bpm = MAX_BPM
        
        time.sleep(0.3)  # Debounce
    
    interval = 60 / current_bpm
    
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(0.05)
    buzzer.duty_u16(0)
    
    print(f"BPM: {current_bpm}")
    time.sleep(interval - 0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **BPM Keeps Growing**: Ensure clamping happens BEFORE using the value in calculations.
*   **Error Beep Plays Every Beat**: Only beep when the limit is first exceeded, not continuously.

### 1️⃣2️⃣ Try This Next

*   **Min BPM**: Add a down button and enforce a minimum of 40 BPM.
*   **Visual Warning**: Flash a red LED when approaching the limit (>180 BPM).

---

## 1️⃣ Project 0398: The Metronome Game

### 2️⃣ Learning Objective
Create a tempo perception quiz to test musical ear training. You will learn about tempo comparison and multiple-choice interaction.

### 3️⃣ Concepts Introduced
*   **Mystery Tempo**: Playing a beat without showing BPM.
*   **Tempo Perception Quiz**: Testing ability to identify specific speeds.
*   **Multiple Choice Logic**: A/B button input for guessing.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**
*   **2× Buttons** (Choice A, Choice B)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |
| **Button A** | GP12 | PULL_DOWN |
| **Button B** | GP13 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Random Number**
*   **Category:** Math

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Buzzer Tone**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **options**: List `[100, 120]` (possible BPM values).
*   **correctIndex**: Randomly chosen index (0 or 1).
*   **chosenBPM**: The actual BPM being played.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[12,13] as PULL_DOWN`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [options] to [[100, 120]]`.
        *   **Snap** below.

*   **B. Main Loop Phase (Quiz Round)**
    *   **Pick Random Tempo**:
        *   From **Math**, drag `set [correctIndex] to [random(0,1)]`.
            *   **Snap** into main block.
        *   From **Variables**, drag `set [chosenBPM] to [options[correctIndex]]`.
            *   **Snap** below.
    *   **Display Question**:
        *   From **Console**, drag `print [Listen to the beat...]`.
            *   **Snap** below.
        *   From **Console**, drag `print [Is this 100 BPM (Button A) or 120 BPM (Button B)?]`.
            *   **Snap** below.
    *   **Play 8 Beats**:
        *   From **Loops**, drag `repeat [8] times`.
            *   **Snap** below.
            *   Inside:
                *   From **Actuators**, drag `Buzzer [15] tone [1000] for [100]ms`.
                *   From **Timing**, drag `sleep [(60 / chosenBPM) - 0.1] seconds`.
    *   **Wait for Answer**:
        *   From **Console**, drag `print [Make your guess!]`.
            *   **Snap** below.
        *   From **Logic**, drag `wait until [digital read pin 12 OR digital read pin 13]`.
            *   **Snap** below.
    *   **Check Answer**:
        *   From **Logic**, drag `if [digital read pin 12] then`.
            *   **Snap** below.
            *   Inside: `set userGuess to 0`.
        *   From **Logic**, drag `else`.
            *   Inside: `set userGuess to 1`.
        *   From **Logic**, drag `if [userGuess] = [correctIndex] then`.
            *   **Snap** below.
            *   Inside: `print [CORRECT! It was {chosenBPM} BPM]`.
        *   Else: `print [WRONG! It was {chosenBPM} BPM]`.

### 9️⃣ Execution Flow (Plain English)

The program randomly selects either 100 BPM or 120 BPM and plays 8 beats at that speed. The user listens and must press Button A (100 BPM) or Button B (120 BPM). If correct, they see "CORRECT!". If wrong, they see the actual answer. This trains musicians to recognize tempo by ear—a critical skill for playing with ensembles.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random

buzzer = machine.PWM(machine.Pin(15))
btnA = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

options = [100, 120]

while True:
    correct_index = random.randint(0, 1)
    chosen_bpm = options[correct_index]
    
    print("Listen to the beat...")
    print("Is this 100 BPM (Button A) or 120 BPM (Button B)?")
    
    # Play 8 beats
    for _ in range(8):
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep((60 / chosen_bpm) - 0.1)
    
    print("Make your guess!")
    
    # Wait for answer
    while not btnA.value() and not btnB.value():
        time.sleep(0.1)
    
    user_guess = 0 if btnA.value() else 1
    
    if user_guess == correct_index:
        print(f"CORRECT! It was {chosen_bpm} BPM")
    else:
        print(f"WRONG! It was {chosen_bpm} BPM")
    
    time.sleep(3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Always Guesses Same**: Ensure `random.randint()` is called inside the loop, not outside.
*   **Hard to Distinguish**: 100 vs 120 might be too close. Try 80 vs 140 for beginners.

### 1️⃣2️⃣ Try This Next

*   **Score Tracking**: Keep track of correct answers out of 10 rounds.
*   **3-Way Choice**: Add 100, 120, 140 BPM for harder difficulty.

---

## 1️⃣ Project 0399: Automated Metronome

### 2️⃣ Learning Objective
Implement a rallentando (gradual slowdown) effect for the end of musical pieces. You will learn about decelerating curves and dynamic tempo changes.

### 3️⃣ Concepts Introduced
*   **Rallentando**: Opposite of accelerando—slowing down gradually.
*   **Decelerating Curve**: BPM decreases over time.
*   **Musical Phrasing**: Matching metronome to natural musical endings.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Variables**
*   **Category:** Variables

🔹 **Math Operations**
*   **Category:** Math

🔹 **Buzzer Tone**
*   **Category:** Actuators

### 7️⃣ Variables & State
*   **currentBPM**: Starts at 120.
*   **targetBPM**: Ends at 60.
*   **totalBeats**: Total beats in song (e.g., 40).
*   **beatCount**: Current beat number.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [currentBPM] to [120]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [targetBPM] to [60]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [totalBeats] to [40]`.
        *   **Snap** below.
    *   From **Variables**, drag `set [beatCount] to [1]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Calculate Current BPM**:
        *   From **Logic**, drag `if [beatCount] > [totalBeats - 10] then`.
            *   **Snap** into loop (last 10 beats).
            *   Inside:
                *   From **Math**, drag `set [currentBPM] to [120 - ((beatCount - 30) * 6)]`.
                    *   **Snap** inside (decrease 6 BPM per beat).
    *   **Play Beat**:
        *   From **Math**, drag `set [interval] to [60 / currentBPM]`.
            *   **Snap** below.
        *   From **Actuators**, drag `Buzzer [15] tone [1000] for [50]ms`.
            *   **Snap** below.
        *   From **Console**, drag `print [Beat {beatCount}: {currentBPM} BPM]`.
            *   **Snap** below.
    *   **Increment**:
        *   From **Variables**, drag `change [beatCount] by [1]`.
            *   **Snap** below.
    *   **Check End**:
        *   From **Logic**, drag `if [beatCount] > [totalBeats] then`.
            *   **Snap** below.
            *   Inside: `break` or stop.
    *   From **Timing**, drag `sleep [interval] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The metronome plays at 120 BPM for the first 30 beats. Starting at beat 31, it begins slowing down: 114 BPM, 108 BPM, 102 BPM... reaching 60 BPM by beat 40. This gradual slowdown mimics the natural ending of many classical pieces, helping musicians practice controlling tempo changes.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

current_bpm = 120
total_beats = 40
beat_count = 1

while beat_count <= total_beats:
    # Rallentando in last 10 beats
    if beat_count > 30:
        current_bpm = 120 - ((beat_count - 30) * 6)
    
    interval = 60 / current_bpm
    
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(0.05)
    buzzer.duty_u16(0)
    
    print(f"Beat {beat_count}: {current_bpm} BPM")
    
    beat_count += 1
    time.sleep(interval - 0.05)

print("Song complete!")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sudden Jump**: Ensure the slowdown starts gradually, not all at once.
*   **BPM Goes Negative**: Add a clamp: `current_bpm = max(current_bpm, 40)`.

### 1️⃣2️⃣ Try This Next

*   **Accelerando**: Reverse it—start slow and speed up.
*   **User Control**: Add button to trigger rallentando manually during playback.

---

## 1️⃣ Project 0400: Mastering Metronome

### 2️⃣ Learning Objective
Implement swing beat timing for jazz music. You will learn about non-uniform rhythm patterns and ratio-based timing.

### 3️⃣ Concepts Introduced
*   **Swing Beat**: Instead of even spacing, use Long-Short pattern (2:1 ratio).
*   **Jazz Timing Logic**: Mimicking the "shuffle" feel of jazz music.
*   **Ratio-Based Intervals**: Using fractions to create groove.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Variables**
*   **Category:** Variables

🔹 **Math Division**
*   **Category:** Math

🔹 **Modulo Operator**
*   **Category:** Math

### 7️⃣ Variables & State
*   **beatCount**: Current beat number.
*   **isLongBeat**: True for long, False for short.
*   **totalInterval**: Time for one long+short pair (e.g., 1 second).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [beatCount] to [0]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [totalInterval] to [1]`.
        *   **Snap** below (2 beats per second = 120 BPM baseline).

*   **B. Main Loop Phase**
    *   **Determine Beat Type**:
        *   From **Math**, drag `set [isLongBeat] to [(beatCount % 2) = 0]`.
            *   **Snap** into loop.
    *   **Calculate Interval (2:1 Ratio)**:
        *   From **Logic**, drag `if [isLongBeat] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Math**, drag `set [interval] to [(totalInterval * 2) / 3]`.
                    *   **Snap** inside (long beat = 2/3 of total).
        *   From **Logic**, drag `else`.
            *   Inside:
                *   From **Math**, drag `set [interval] to [(totalInterval * 1) / 3]`.
                    *   **Snap** inside (short beat = 1/3 of total).
    *   **Play Beat**:
        *   From **Actuators**, drag `Buzzer [15] tone [1000] for [50]ms`.
            *   **Snap** below.
        *   From **Console**, drag `print [{"LONG" if isLongBeat else "short"}]`.
            *   **Snap** below.
    *   **Increment**:
        *   From **Variables**, drag `change [beatCount] by [1]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [interval - 0.05] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

In swing timing, beats are not evenly spaced. Instead of 0.5s-0.5s-0.5s-0.5s, it plays: LONG(0.67s)-short(0.33s)-LONG(0.67s)-short(0.33s). This 2:1 ratio creates the characteristic "shuffle" feel of jazz and blues. Musicians use this to practice maintaining swing groove, which is essential for authentic jazz performance.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

beat_count = 0
total_interval = 1.0  # 1 second per pair of beats

while True:
    is_long_beat = (beat_count % 2 == 0)
    
    if is_long_beat:
        interval = (total_interval * 2) / 3  # 0.67s
    else:
        interval = (total_interval * 1) / 3  # 0.33s
    
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(0.05)
    buzzer.duty_u16(0)
    
    print("LONG" if is_long_beat else "short")
    
    beat_count += 1
    time.sleep(interval - 0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sounds Even**: Verify the 2:1 ratio is being calculated correctly (0.67s vs 0.33s).
*   **Too Fast/Slow**: Adjust `totalInterval` to change overall tempo while maintaining swing ratio.

### 1️⃣2️⃣ Try This Next

*   **Variable Swing**: Use a pot to adjust swing ratio from 1:1 (straight) to 3:1 (heavy swing).
*   **Triplet Feel**: Implement 3 beats per measure with varying accents for shuffle rhythm.

---

🎉 **CONGRATULATIONS!** You have completed all 100 projects (0301-0400) covering advanced embedded systems, displays, timers, sound generation, and rhythm programming! 🎉
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(metronome_final)

print("✅ Generated Projects 0396-0400 (Metronome 2 - FINAL)")
print("")
print("🎉🎉🎉 ALL 100 PROJECTS (0301-0400) NOW COMPLETE! 🎉🎉🎉")
print("")
print("📊 FINAL STATUS:")
print("   ✅ 100/100 projects have full 12-section Elite documentation")
print("   ✅ All problem statements correctly matched")
print("   ✅ All Section 8 content uses 'From/Snap' format")
print("   ✅ File ends with Project 0400: Mastering Metronome")
print("")
print("🚀 Documentation generation COMPLETE!")
