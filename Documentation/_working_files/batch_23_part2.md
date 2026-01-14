
## 1. Project 0226: Smart Sound & Music Switch

### 2. Learning Objective
Explore duty cycle perception (Software Volume). Learn how to manipulate the "Duty Cycle" of a square wave to change the perceived loudness of a passive buzzer, understanding how air displacement affects volume.

### 3. Concepts Introduced
*   **Duty Cycle (Volume)**: The ratio of "Time ON" vs "Time OFF" in a square wave.
*   **Acoustic Intensity**: How much energy the speaker diaphragm pushes into the air.
*   **Perceptual Volume**: identifying that 50% duty is maximum loudness and 5-10% is whispering quiet.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Slide Switch
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speaker** | GP15 | Pulse-width output |
| **Level Switch** | GP14 | High vs Low volume selector |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking the switch)
*   **from Actuators, drag `pico_buzzer_pitch`** (set frequency)
*   **from Actuators, drag `pico_buzzer_duty`** (set Duty/Volume)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: The switch state directly sets the duty value.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Fixed Frequency**:
    *   Initialize GP15 (Buzzer) to 1000 Hz.

**B. Control Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Detect Volume Mode**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).

**C. Selection Phase**
4.  **Loud Mode (Switch ON)**:
    *   Inside the **If** block:
    *   **Set** GP15 Duty Cycle to **50% (32768)**.
    *   **Print** "Volume: MAX".
5.  **Quiet Mode (Switch OFF)**:
    *   Inside the **Else** block:
    *   **Set** GP15 Duty Cycle to **5% (3276)**.
    *   **Print** "Volume: WHISPER".

### 9. Execution Flow
1.  **Read**: The Pico checks the slide switch position.
2.  **Execute**: If the switch is "ON", the speaker diaphragm is given maximum travel time, moving lots of air.
3.  **Result**: The beep is loud and clear.
4.  **Transition**: You slide the switch "OFF". The Pico reduces the "ON" time to only 5% of the total cycle.
5.  **Result**: The speaker barely vibrates, resulting in a very quiet sound.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))
bz.freq(1000)
sw = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if sw.value() == 1:
        # 50% Duty = Max Volume
        bz.duty_u16(32768)
        print("Loud")
    else:
        # ~5% Duty = Low Volume
        bz.duty_u16(3276)
        print("Quiet")
        
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Inversion**: 100% duty cycle is actually SILENT! The speaker diaphragm is held in one position and doesn't move. 50% is the absolute maximum loudness.

### 12. Try This Next
*   **Potentiometer Volume**: use a knob to smoothly change the duty cycle from 0 to 32768.
*   **Frequency Link**: make the volume get lower as the pitch gets higher to keep the sound "comfortable".

---

## 1. Project 0227: Sound & Music Alarm System

### 2. Learning Objective
Explore proximity hazard alerts (The Parking Sensor). Learn how to use distance data to dynamically modify the "Rate" of a repetitive sound (Beeps), understanding how frequency changes over time act as a warning signal.

### 3. Concepts Introduced
*   **Beep Intervals**: Creating a repeating sound using two wait blocks.
*   **Variable Delay Logic**: Using `wait_time = distance / speed` to control tempo.
*   **Collision Avoidance**: Providing audio feedback to prevent physical impact.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Ultrasonic Sensor
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Alarm output |
| **Trigger/Echo** | GP14, 13 | Distance source |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_ultrasonic_dist`** (read distance)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait block with variable)
*   **from Actuators, drag `pico_buzzer_pitch`** (set tone)

### 7. Variables
*   **dist**: Measured distance in cm.
*   **gap**: The seconds to wait between beeps.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Measure Obstacle**:
    *   **Set** `dist` = **Sensors** `pico_ultrasonic_dist`.

**B. Calculation Phase**
3.  **Determine Tempo**:
    *   Inside the loop, from **Math**, **Set** `gap` = (`dist` / 100).
    *   *Correction: If distance is 50cm, gap is 0.5s. If distance is 10cm, gap is 0.1s (Faster).*
4.  **Capping**: 
    *   If `gap` > 1.0: **Set** `gap` = 1.0 (Stay slow if far away).

**C. Feedback Phase**
5.  **Perform Beep**:
    *   Inside the loop, **Set** Buzzer to 1000Hz. **Wait** 0.05s.
    *   **Turn OFF** Buzzer. **Wait** `gap` seconds.

### 9. Execution Flow
1.  **Far**: The object is 80cm away. The Pico waits 0.8 seconds between beeps. "Beep... Beep... Beep".
2.  **Move**: The object moves to 20cm. The gap becomes 0.2s.
3.  **Near**: The Tempo increases drastically. "Beep-Beep-Beep-Beep".
4.  **Critical**: At 5cm, the beeps are so fast they almost sound like a continuous tone.
5.  **Result**: An intuitive audio warning system that doesn't requires the user to look at a screen.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
trig = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(13, machine.Pin.IN)

def get_dist():
    trig.low(); utime.sleep_us(2); trig.high(); utime.sleep_us(10); trig.low()
    while echo.value() == 0: pass
    t1 = utime.ticks_us()
    while echo.value() == 1: pass
    t2 = utime.ticks_us()
    return (utime.ticks_diff(t2, t1) * 0.0343) / 2

while True:
    d = get_dist()
    
    # Calculate beep gap (0.1s to 1.0s)
    gap = d / 100
    if gap < 0.05: gap = 0.05 # Fast limit
    if gap > 1.0: gap = 1.0   # Slow limit
    
    # Do the Beep
    bz.freq(1000); bz.duty_u16(32768)
    utime.sleep(0.05)
    bz.duty_u16(0)
    
    # Adaptive wait
    utime.sleep(gap)
```

### 11. Common Mistakes
*   **Constant Beep**: if you forget the `wait gap` block, the buzzer will just sound continuously without pulsing.
*   **Unit Scale**: ensure you divide by 100 or a similar factor; if you use the raw `dist` value (50) as the seconds wait, the alarm will only beep once every minute!

### 12. Try This Next
*   **Pitch Variation**: make the pitch go higher as the object gets closer to add even more urgency.
*   **Full Stop**: if the distance is less than 5cm, keep the buzzer ON permanently.

---

## 1. Project 0228: The Sound & Music Game

### 2. Learning Objective
Explore subjective time estimation (The Blind Timer). Learn how to implement a game that measures the difference between a system clock (Absolute Time) and a human's perception of duration using a button.

### 3. Concepts Introduced
*   **Duration Capture**: Measuring how long an input pin remains active (Timestamping).
*   **Error Calculation**: Finding the mathematical difference between 5.0 seconds and the user's actual time.
*   **Feedback Loops**: Signaling "Perfect", "Too Short", or "Too Long" via tones.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Player Button** | GP14 | Hold to start timer |
| **Result Speaker** | GP15 | Success/Fail sounds |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_time_ms`** (get timestamps)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Logic, drag `controls_if`** (evaluating performance)

### 7. Variables
*   **t_start**, **t_end**: The clock values when the button is touched and released.
*   **user_secs**: The final calculated duration.
*   **diff**: error from 5.0 seconds target.

### 8. Step-by-Step Guide

**A. Capture Phase**
1.  **Wait for Touch**:
    *   Repeat-until **Button** GP14 is Pressed.
    *   **Set** `t_start` = **Time** `pico_time_ms`.
    *   **Set** GP15 (Buzzer) to 400Hz (Low steady hum).
2.  **Wait for Release**:
    *   Repeat-until **Button** GP14 is Released.
    *   **Set** `t_end` = **Time** `pico_time_ms`.
    *   **Turn OFF** Buzzer.

**B. Brain Phase (Math)**
3.  **Calculate Result**:
    *   **Set** `user_secs` = (`t_end` - `t_start`) / 1000.
    *   **Set** `diff` = abs(`user_secs` - 5.0).

**C. Feedback Phase**
4.  **Display Verdict**:
    *   If `diff` < 0.2: **Print** "LEGENDARY ACCURACY!". Play High Beep.
    *   Else If `diff` < 1.0: **Print** "NOT BAD!". Play Mid Beep.
    *   Else: **Print** "WAY OFF!". Play Low Beep.
5.  **Print Actual Time**: "Your time: ", `user_secs`, " seconds".

### 9. Execution Flow
1.  **Interaction**: You hold the button. The buzzer hums while you count "1... 2... 3... 4... 5..." in your head.
2.  **Logic**: You release the button.
3.  **Math**: The Pico sees you held it for exactly 4850ms. 
4.  **Reaction**: Since 4.85 is within 0.2s of the target (5.0), the Pico rewards you with a "Legendary" message.
5.  **Result**: A fun game that trains your internal biological clock.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = PWM(Pin(15))

while True:
    print("Hold button for exactly 5 seconds...")
    
    # 1. Wait for press
    while btn.value() == 0: pass
    t1 = time.ticks_ms()
    bz.freq(400); bz.duty_u16(10000) # Quiet hum
    
    # 2. Wait for release
    while btn.value() == 1: pass
    t2 = time.ticks_ms()
    bz.duty_u16(0) # Silence
    
    # 3. Calculate
    dur = (t2 - t1) / 1000
    err = abs(dur - 5.0)
    
    print("You held for: " + str(dur) + "s")
    
    # 4. Score
    if err < 0.2:
        print("PERFECT!")
        bz.freq(2000); bz.duty_u16(32768); time.sleep(0.1); bz.duty_u16(0)
    elif err < 1.0:
        print("GOOD")
        bz.freq(1000); bz.duty_u16(32768); time.sleep(0.1); bz.duty_u16(0)
    else:
        print("TRY AGAIN")
        bz.freq(200); bz.duty_u16(32768); time.sleep(0.1); bz.duty_u16(0)
        
    time.sleep(2)
```

### 11. Common Mistakes
*   **Millisecond Math**: forgetting to divide by 1000 will give you a result of "5000" instead of "5.0".

### 12. Try This Next
*   **Variable Target**: make the game pick a random number between 3 and 10 and tell you the target before you start.
*   **Multiple Players**: pass the Pico around and see who has the best internal clock.

---

## 1. Project 0229: Automated Sound & Music

### 2. Learning Objective
Explore code structure and encapsulation (The Jukebox). Learn how to create named functions for complex melodies and use "Random Luck" to select which piece of music plays at startup.

### 3. Concepts Introduced
*   **Melody Bundling**: Grouping many `pitch` and `wait` blocks into a single "Song" function.
*   **Startup Execution**: logic that runs exactly once when power is applied.
*   **List Selection**: picking an item from a collection based on a random index.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Audio Out** | GP15 | Jukebox output |

### 6. Blocks Used
*   **from Functions, drag `to [tune_a]`** (define songs)
*   **from Math, drag `math_random_int`** (picking a song)
*   **from Logic, drag `controls_if`** (logical routing)
*   **from Functions, drag `call [tune_a]`** (executing song)

### 7. Variables
*   **selection**: Number (1, 2, or 3).

### 8. Step-by-Step Guide

**A. Prep Phase (Functions)**
1.  **Define Tune A**: (Happy) C-E-G.
2.  **Define Tune B**: (Sad) G-E-C.
3.  **Define Tune C**: (Siren) High-Low-High.

**B. Brain Phase**
4.  **Pick a Song**:
    *   In the **Setup** area:
    *   **Set** `selection` = **Math** `random integer from 1 to 3`.

**C. Play Phase**
5.  **Route the Command**:
    *   If `selection` == 1: **Call** `tune_a`.
    *   If `selection` == 2: **Call** `tune_b`.
    *   If `selection` == 3: **Call** `tune_c`.

### 9. Execution Flow
1.  **Power**: You plug in the Pico.
2.  **Dice Roll**: The Pico rolls a virtual 3-sided die and gets the number 2.
3.  **Look-up**: The code finds that selection 2 matches the "Sad" tune.
4.  **Action**: The Pico jumps to the `tune_b` function and plays the notes.
5.  **Result**: Every time you reset the project, you might get a different song.

### 10. Generated Code
```python
from machine import Pin, PWM
import time
import random

bz = PWM(Pin(15))

def play_note(f, d):
    bz.freq(f); bz.duty_u16(32768); time.sleep(d)
    bz.duty_u16(0); time.sleep(0.05)

def song_1(): # Happy
    play_note(523, 0.2); play_note(659, 0.2); play_note(783, 0.4)

def song_2(): # Sad
    play_note(392, 0.2); play_note(311, 0.2); play_note(261, 0.4)

def song_3(): # Alarm
    for _ in range(4):
        play_note(1000, 0.1); play_note(500, 0.1)

# Pick song at startup
choice = random.randint(1, 3)
print("Playing selection: " + str(choice))

if choice == 1: song_1()
elif choice == 2: song_2()
elif choice == 3: song_3()

# Wait forever after playing
while True: time.sleep(1)
```

### 11. Common Mistakes
*   **Blocking Start**: if your songs are very long, the Pico won't reach the "Main Loop" for a long time. This is fine for a music box, but bad for a robot!

### 12. Try This Next
*   **Button Selector**: instead of random, use a button to cycle through the songs.
*   **Shuffle Mode**: put the songs inside a loop so it never stops playing new random tunes.

---

## 1. Project 0230: Mastering Sound & Music

### 2. Learning Objective
Explore string parsing and musical data encoding (The RTTTL Player). Learn how to "Decode" a text string that contains note names and lengths, allowing you to store entire songs in a single line of text.

### 3. Concepts Introduced
*   **Data Protocols**: Using a standardized text format (RTTTL) to share music.
*   **String Processing**: Splitting a sentence into "Notes" and "Durations".
*   **Note-to-Frequency Conversion**: A lookup table that maps the character "C" to 261Hz.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Audio Out** | GP15 | Professional music output |

### 6. Blocks Used
*   **from Text, drag `text_split`** (parsing notes)
*   **from Logic, drag `controls_if`** (finding note frequencies)
*   **from Variables, drag `variables_set`** (storing song string)
*   **from Functions, drag `call [play_note]`**

### 7. Variables
*   **song_data**: A string like "c,d,e,c".
*   **note**: The current character being played.

### 8. Step-by-Step Guide

**A. Preparation Phase**
1.  **Enter the Melody**:
    *   **Set** `song_data` = "262,294,330,262,262,294,330,262". (Frère Jacques)

**B. Decoding Phase**
2.  **Split the String**:
    *   From **Text**, drag `split [song_data] by [,]`.
    *   From **Loops**, drag `for each item [note_hz] in list`.

**C. Execution Phase**
3.  **Play the Code**:
    *   Inside the loop:
    *   **Set** GP15 frequency to (`note_hz`).
    *   **Wait** 0.3 seconds.
4.  **Separator**:
    *   **Turn OFF** Buzzer. **Wait** 0.05s.

### 9. Execution Flow
1.  **Read**: The Pico looks at the long string of numbers.
2.  **Split**: The Pico cuts the string at every comma, creating a list of notes.
3.  **Loop**: The Pico takes the first number (262), plays it, then takes the next.
4.  **Result**: You hear a recognizable song that was loaded from a single "Data String".
5.  **Benefit**: You can change the entire song just by typing new numbers in the text block.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))

# Simple data string: frequency1,duration1,frequency2,duration2...
song = "262,0.3,294,0.3,330,0.3,262,0.3"

# Parse the string
parts = song.split(",")

while True:
    for i in range(0, len(parts), 2):
        f = int(parts[i])
        d = float(parts[i+1])
        
        # Play it
        bz.freq(f); bz.duty_u16(32768); time.sleep(d)
        bz.duty_u16(0); time.sleep(0.05)
        
    time.sleep(2) # Pause before restart
```

### 11. Common Mistakes
*   **Syntax Errors**: a single missing comma in the string will cause the "Split" block to fail and the code to crash.
*   **String to Number**: remember that a number in a text box is "Text". You must convert it to an "Integer" before the Buzzer block can use it.

### 12. Try This Next
*   **Alpha Note Parser**: write a function that takes "C" and returns "262" so you can write songs with letters instead of raw Hertz numbers.
*   **Speed Factor**: add a variable at the start called `tempo` and multiply all durations by it so you can speed up the whole song with one change.

---
