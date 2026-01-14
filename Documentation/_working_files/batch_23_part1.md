
# BATCH 23: Sound & Music 2 (Projects 0221-0230)

## 1. Project 0221: Introduction to Sound & Music

### 2. Learning Objective
Explore frequency perception (The Audio Spectrum). Learn how to use a passive buzzer to generate specific tones and observe how changing the frequency value directly affects the perceived "Pitch" (Low vs. High).

### 3. Concepts Introduced
*   **Frequency (Hertz)**: The number of sound vibrations per second.
*   **Pitch Perception**: understanding the relationship between numbers (Hz) and musical notes.
*   **Passive Buzzer Control**: requiring a square wave signal from the Pico to make sound.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speaker (+)** | GP15 | Square-wave output |
| **Speaker (-)** | GND | Ground |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_buzzer_pitch`** (set frequency)
*   **from Actuators, drag `pico_buzzer_off`** (silence)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: this is a step-by-step sequence of fixed pitches.

### 8. Step-by-Step Guide

**A. Low Pitch Phase**
1.  **Configure Low**:
    *   From **Actuators**, drag `pico_buzzer_pitch`.
    *   **Set** GP15 -> 200 Hz.
    *   From **Time**, **Wait** 1 second.

**B. Mid Pitch Phase**
2.  **Configure Mid**:
    *   From **Actuators**, drag `pico_buzzer_pitch`.
    *   **Set** GP15 -> 1000 Hz.
    *   From **Time**, **Wait** 1 second.

**C. High Pitch Phase**
3.  **Configure High**:
    *   From **Actuators**, drag `pico_buzzer_pitch`.
    *   **Set** GP15 -> 5000 Hz.
    *   From **Time**, **Wait** 1 second.

**D. Silence Phase**
4.  **Finalize**:
    *   From **Actuators**, drag `pico_buzzer_off` for GP15.
    *   **Wait** 2 seconds before looping.

### 9. Execution Flow
1.  **Low**: The Pico sends a slow pulse (200 times per second). The buzzer makes a deep "Hum".
2.  **Mid**: The pulse speeds up to 1000 times per second. The buzzer makes a standard "Beep".
3.  **High**: The pulse reaches 5000 times per second. The buzzer makes a sharp, piercing "Whistle".
4.  **Pause**: The Pico stops the pulsing, giving the speaker (and your ears) a break.
5.  **Result**: A demonstration of how software numbers translate to physical sound waves.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))

while True:
    # 200 Hz (Low)
    bz.freq(200); bz.duty_u16(32768); time.sleep(1)
    
    # 1000 Hz (Mid)
    bz.freq(1000); bz.duty_u16(32768); time.sleep(1)
    
    # 5000 Hz (High)
    bz.freq(5000); bz.duty_u16(32768); time.sleep(1)
    
    # Off
    bz.duty_u16(0); time.sleep(2)
```

### 11. Common Mistakes
*   **Active vs Passive**: If using an *Active* buzzer, changing the frequency in the code won't change the sound; it will only beep at a fixed pitch.
*   **Duty Cycle**: If you don't set the duty cycle to 50% (32768), you might hear silence or "clicking" instead of a pure tone.

### 12. Try This Next
*   **Piano Keys**: Add buttons to play specific frequencies like 262Hz (Middle C) and 294Hz (D).
*   **Ultrasonic**: try to reach 20000Hz to see if your dog can hear it, even if you can't!

---

## 1. Project 0222: Blinking Sound & Music

### 2. Learning Objective
Explore synchronized visual and audio modulation (The Police Siren). Learn how to "Glide" frequencies smoothly up and down while simultaneously toggling light states to create a cohesive emergency vehicle simulation.

### 3. Concepts Introduced
*   **Frequency Sweeping**: Incrementally changing a pitch value inside a loop.
*   **Multi-Output Coordination**: linking audio tempo to visual blinking.
*   **Dynamic Looping**: Using the loop variable as the pitch value itself.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   1 Red LED + 1 Blue LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP14 | Primary strobe |
| **Blue LED** | GP13 | Secondary strobe |
| **Buzzer** | GP15 | Siren generator |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (climbing pitch)
*   **from Actuators, drag `pico_buzzer_pitch`** (set frequency)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)
*   **from Time, drag `pico_wait_ms`** (small delay for smoothness)

### 7. Variables
*   **hz_val**: Number representing the current siren pitch.

### 8. Step-by-Step Guide

**A. Siren Rise Phase**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Climb Frequency**:
    *   From **Loops**, drag `count with hz_val from 500 to 1000 by 10`.
    *   Inside:
        *   **Set** GP15 (Buzzer) to `hz_val`.
        *   **Set** GP14 -> HIGH, GP13 -> LOW.
        *   **Wait** 5 milliseconds for a smooth "Slide" effect.

**B. Siren Fall Phase**
3.  **Descend Frequency**:
    *   From **Loops**, drag `count with hz_val from 1000 down to 500 by 10`.
    *   Inside:
        *   **Set** GP15 (Buzzer) to `hz_val`.
        *   **Set** GP14 -> LOW, GP13 -> HIGH.
        *   **Wait** 5 milliseconds.

### 9. Execution Flow
1.  **Rise**: The buzzer pitch slides from a low rumble to a sharp whine. At the same time, the Red LED is ON.
2.  **Peak**: At 1000Hz, the Pico immediately switches directions.
3.  **Fall**: The pitch slides back down, and the Blue LED turns ON while the Red shuts OFF.
4.  **Repeat**: The process cycles indefinitely.
5.  **Result**: A realistic, professionally timed alert system using light and sound.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))
bz.duty_u16(32768)
r_led = Pin(14, Pin.OUT)
b_led = Pin(13, Pin.OUT)

while True:
    # Rise
    r_led.value(1); b_led.value(0)
    for freq in range(500, 1001, 10):
        bz.freq(freq)
        time.sleep_ms(5)
        
    # Fall
    r_led.value(0); b_led.value(1)
    for freq in range(1000, 499, -10):
        bz.freq(freq)
        time.sleep_ms(5)
```

### 11. Common Mistakes
*   **Step Size**: If your "Step" is too large (e.g., skip by 100 instead of 10), the siren will sound "step-wise" like a set of distinct notes rather than a smooth slide.
*   **Wait Time**: If the wait is 1.0s instead of 0.005s, the siren will take 10 minutes to move between pitches!

### 12. Try This Next
*   **Wail vs Yelp**: search for different siren patterns and try to match them with faster or slower loops.
*   **Dual Pitch**: make it go straight from 500 to 1000 without the slide (a "Hi-Lo" siren).

---

## 1. Project 0223: Manual Sound & Music Control

### 2. Learning Objective
Explore sound randomization (The Theremin Button). Learn how to use a physical input (Button) to enable a sound generator that produces "Randomized" frequencies, creating sci-fi "Computer Noises" or sound effects.

### 3. Concepts Introduced
*   **Randomization**: Using the `random` library to pick unpredictable numbers.
*   **Held-to-Generate**: linking a sound's duty cycle to a button state.
*   **SFX Generation**: creating non-musical sounds for games or applications.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Action Button** | GP14 | Hold to play SFX |
| **Speaker** | GP15 | Output for random tones |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking button)
*   **from Math, drag `math_random_int`** (picking a pitch)
*   **from Actuators, drag `pico_buzzer_pitch`** (play tone)
*   **from Actuators, drag `pico_buzzer_off`** (silence)

### 7. Variables
*   **None**: this project uses live random values.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Check Trigger**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).

**B. Execution Phase**
3.  **Generate Random SFX**:
    *   Inside the **If** block:
    *   From **Actuators**, drag `pico_buzzer_pitch`.
    *   **Value**: From **Math**, pick `random integer from 100 to 4000`.
    *   From **Time**, **Wait** 0.05 seconds (Rapid changes).
4.  **Silence Branch**:
    *   Inside the **Else** block:
    *   From **Actuators**, **Set** `pico_buzzer_off` GP15.

### 9. Execution Flow
1.  **Idle**: You aren't touching anything. The buzzer is silent.
2.  **Press**: You hold the button down.
3.  **Randomize**: 20 times per second, the Pico picks a new crazy frequency and plays it.
4.  **Sound**: You hear a chaotic, electronic "Computer Searching" or "Alien Communication" noise.
5.  **Release**: The buzzer immediately cuts off as the code falls into the "Else" branch.

### 10. Generated Code
```python
import machine
import utime
import urandom

bz = machine.PWM(machine.Pin(15))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value():
        # Scifi Generator
        freq = urandom.randint(100, 4000)
        bz.freq(freq)
        bz.duty_u16(32768)
        utime.sleep(0.05)
    else:
        # Silence
        bz.duty_u16(0)
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Range Too Small**: If you pick random between 100 and 110, you won't hear much change. Use a wide range for bigger effects.
*   **Wait Too Long**: If you wait 1 second between randomizing, it will sound like three different notes instead of a futuristic noise.

### 12. Try This Next
*   **Scale Limits**: restrict the random numbers to only "Musical" notes to create a chaotic melody.
*   **LED Sparkle**: flash an LED at a random brightness whenever the sound changes.

---

## 1. Project 0224: Sound & Music Sequences

### 2. Learning Objective
Explore mathematical musical intervals (The C Major Scale). Learn how to play a sequence of specific, predefined frequencies in a list to create a recognizable musical melody or training exercise.

### 3. Concepts Introduced
*   **Musical Scales**: specific sets of frequencies (C, D, E...) that sound harmonious.
*   **Array Selection (Pseudo-List)**: stepping through a series of commands for each note.
*   **Tempo and Sustain**: controlling how long each note lasts.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Output Buzzer** | GP15 | Musical output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_buzzer_pitch`** (set note)
*   **from Time, drag `pico_wait`** (sustain)

### 7. Variables
*   **None**: this is a hard-coded sequence.

### 8. Step-by-Step Guide

**A. Ascending Phase**
1.  **Note C4**: **Set** Pitch to 262. **Wait** 0.5s.
2.  **Note D4**: **Set** Pitch to 294. **Wait** 0.5s.
3.  **Note E4**: **Set** Pitch to 330. **Wait** 0.5s.
4.  **Note F4**: **Set** Pitch to 349. **Wait** 0.5s.
5.  **Note G4**: **Set** Pitch to 392. **Wait** 0.5s.
6.  **Note A4**: **Set** Pitch to 440. **Wait** 0.5s.
7.  **Note B4**: **Set** Pitch to 494. **Wait** 0.5s.
8.  **Note C5**: **Set** Pitch to 523. **Wait** 0.5s.

**B. Finish Phase**
9.  **Silence**: **Turn OFF** Buzzer. **Wait** 2s.

### 9. Execution Flow
1.  **Execution**: The Pico plays each note in perfect mathematical order.
2.  **Timing**: Each note takes precisely half a second.
3.  **Result**: The user hears the "Do-Re-Mi-Fa-So-La-Ti-Do" scale, demonstrating that math and music are the same thing to a computer.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
# C Major Scale Frequencies
scale = [262, 294, 330, 349, 392, 440, 494, 523]

while True:
    for note in scale:
        bz.freq(note)
        bz.duty_u16(32768)
        utime.sleep(0.5)
        
    # Silence between repeats
    bz.duty_u16(0)
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Missing Duty Cycle**: forgetting to set volume (32768) means you won't hear any notes.
*   **Note Values**: mixing up the frequencies (e.g. playing 262 then 200) will sound "flat" or out of tune.

### 12. Try This Next
*   **Descending Scale**: make the scale go from C5 down to C4 after it reaches the top.
*   **Tempo Variation**: change the wait time to 0.2s to play the scale faster.

---

## 1. Project 0225: Interactive Sound & Music

### 2. Learning Objective
Explore spatial-to-audio mapping (The Ultrasonic Theremin). Learn how to use distance data from an ultrasonic sensor to dynamically calculate sound frequencies, creating an air-instrument that responds to hand movement.

### 3. Concepts Introduced
*   **Proximity Sensing**: Using ultrasound to measure distance in centimeters.
*   **Live Data Mapping**: Converting a range of physical space (10-50cm) into a range of audio frequency (200-2000Hz).
*   **Dynamic Oscillation**: The buzzer follows the hand's motion in real-time.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Ultrasonic Sensor (HC-SR04)
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Output sound |
| **Echo (Sensor)** | GP14 | Reads the pulse |
| **Trigger (Sensor)** | GP13 | Sends the pulse |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_ultrasonic_dist`** (read distance)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_map`** (convert range)
*   **from Actuators, drag `pico_buzzer_pitch`** (output tone)

### 7. Variables
*   **dist_cm**: Number tracking hand position.
*   **target_hz**: calculated frequency.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Measure Hand Space**:
    *   **Set** `dist_cm` = **Sensors** `pico_ultrasonic_dist` on GP13/14.

**B. Brain Phase (Math)**
3.  **Map Distance to Pitch**:
    *   From **Math**, drag the `math_map` block.
    *   **Input**: `dist_cm`.
    *   **From Range**: [5 to 50] (centimeters).
    *   **To Range**: [300 to 3000] (Hertz).
    *   **Set** `target_hz` = the result.

**C. Feedback Phase**
4.  **Perform Sound**:
    *   From **Actuators**, **Set** GP15 (Buzzer) frequency to `target_hz`.
5.  **Pace**: **Wait** 0.05 seconds for high responsiveness.

### 9. Execution Flow
1.  **Input**: The sensor sends out sound waves and times the echo off your hand.
2.  **Calculate**: If your hand is 10cm away, the math map converts that to a low note (~600Hz).
3.  **Move**: You move your hand to 40cm. The math map immediately calculates a high note (~2400Hz).
4.  **Result**: You "play" the instrument by waving your hand in the air like a musical maestro.

### 10. Generated Code
```python
import machine
import utime

# Hardware
trigger = machine.Pin(13, machine.Pin.OUT)
echo = machine.Pin(14, machine.Pin.IN)
bz = machine.PWM(machine.Pin(15))

def get_dist():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0: pass
    t1 = utime.ticks_us()
    while echo.value() == 1: pass
    t2 = utime.ticks_us()
    return (utime.ticks_diff(t2, t1) * 0.0343) / 2

while True:
    d = get_dist()
    
    if 5 <= d <= 50:
        # Map 5-50cm to 300-3000Hz
        f = int((d - 5) * (3000 - 300) / (50 - 5) + 300)
        bz.freq(f)
        bz.duty_u16(32768)
    else:
        # Silence if out of range
        bz.duty_u16(0)
        
    utime.sleep(0.05)
```

### 11. Common Mistakes
*   **Echo Timeout**: if there is no surface (hand) for the sound to hit, the sensor might hang. Always check if the hand is within a reasonable range (5-50cm).
*   **Pitch Inversion**: if you want "closer = higher pitch", swap the numbers in the `to range` part of the math block.

### 12. Try This Next
*   **Staccato**: instead of a constant slide, make the sound only play "Beeps" that get faster as you move your hand closer.
*   **Dual Hand**: use two sensors, one for pitch and one for volume!

---
