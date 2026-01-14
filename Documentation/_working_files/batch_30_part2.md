
## 1. Project 0296: Smart Morse Code Switch

### 2. Learning Objective
Explore carrier control logic (The Loop Sender). Learn how to implement a system that generates a continuous message ("CQ") but provides a physical "Enable" switch to master the transmission, demonstrating how real radio equipment controls the broadcast state.

### 3. Concepts Introduced
*   **Transmission Gating**: using a switch to allow or block a continuous process.
*   **Looping Messages**: repeating a "Call" signal until a contact is made.
*   **Global Variable Controls**: using a hardware state to decide if a function should execute.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Slide Switch
*   1 Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **TX Switch** | GP14 | HIGH = Transmit, LOW = Silence |
| **Carrier Buzzer** | GP15 | Morse audio |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking switch)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)
*   **from Time, drag `pico_wait`** (signal timing)

### 7. Variables
*   **None**: the switch state is used directly.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Check Capability**:
    *   If **Switch** GP14 is HIGH:
        *   **Print** "Carrier ACTIVE. Transmitting 'CQ'...".
        *   **Execute Transmit Routine**.
    *   Else:
        *   **Set** Buzzer OFF.
        *   **Print** "Station SILENT.".

**B. Transmit Routine**
3.  **Letter C (-.-.)**:
    *   **Beep** 0.3s, 0.1s, 0.3s, 0.1s.
    *   **Wait** 0.3s (Letter gap).
4.  **Letter Q (--.-)**:
    *   **Beep** 0.3s, 0.3s, 0.1s, 0.3s.

**C. Maintenance Phase**
5.  **Cooling**: **Wait** 1 second before the next "CQ" starts.

### 9. Execution Flow
1.  **Standby**: The switch is in the "Off" position. The Pico sits in silence.
2.  **Broadcast**: You slide the switch to "On".
3.  **Action**: The loop immediately starts chirping the "CQ" pattern.
4.  **Interrupt**: You slide the switch back. The Pico finishes its current letter and then stays quiet.
5.  **Result**: An professional station control that gives you total power over the radio waves.
6.  **Outcome**: Understanding safety and control in signal broadcasting.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

sw = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = PWM(Pin(15))

def pulse(d):
    bz.freq(1000); bz.duty_u16(32768); time.sleep(d)
    bz.duty_u16(0); time.sleep(0.1)

while True:
    if sw.value() == 1:
        print("CQ CQ CQ...")
        # C: -.-.
        pulse(0.3); pulse(0.1); pulse(0.3); pulse(0.1)
        time.sleep(0.2)
        # Q: --.-
        pulse(0.3); pulse(0.3); pulse(0.1); pulse(0.3)
        time.sleep(1.0)
    else:
        bz.duty_u16(0)
        time.sleep(0.5)
```

### 11. Common Mistakes
*   **Mid-Message Cutoff**: In a simple loop, if you turn the switch off *while* the letter "C" is playing, it will finish that letter before stopping. This is actually good behavior, as cutting a tone mid-pulse can cause radio noise!

### 12. Try This Next
*   **Indicator Light**: turn on a Red LED when the switch is ON to serve as an "ON AIR" warning.
*   **Message Select**: use two switches to choose between sending "CQ", "SOS", or "HI".

---

## 1. Project 0297: Morse Code Alarm System

### 2. Learning Objective
Explore context-specific signaling (The Emergency Beacon). Learn how to implement a system that chooses between two completely different Morse messages based on which input button is triggered, allowing for priority alerts.

### 3. Concepts Introduced
*   **Logical Mapping**: connecting a physical button (e.g. Red for Fire) to a specific string of dots and dashes.
*   **Emergency Priority**: ensuring a high-importance signal is transmitted clearly.
*   **Variable Data Loading**: passing different patterns to a shared "Play" function.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Red Button (Fire)
*   1 Blue Button (Medical)
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fire Button** | GP14 | Signal "FIRE" |
| **Medical Button**| GP13 | Signal "MED" |
| **Siren Output** | GP15 | Morse audio |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (with `else if`)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)
*   **from Time, drag `pico_wait`** (timing)

### 7. Variables
*   **None**: this uses direct conditional execution.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Logic Phase (Fire)**
2.  **Detection**:
    *   If **Button GP14** (Red) is Pressed:
        *   **Print** "FIRE EMERGENCY DETECTED. Sending Morse...".
        *   **Execute Word** "FIRE": (F: ..-. | I: .. | R: .-. | E: .)

**C. Logic Phase (Medical)**
3.  **Detection**:
    *   Else If **Button GP13** (Blue) is Pressed:
        *   **Print** "MEDICAL EMERGENCY DETECTED. Sending Morse...".
        *   **Execute Word** "MED": (M: -- | E: . | D: -..)

### 9. Execution Flow
1.  **Standby**: The Pico is quiet.
2.  **Alarm**: A fire is detected; you hit the red button.
3.  **Action**: The Pico immediately starts chirping "..-. .. .-. ." (FIRE). It repeats the message 3 times.
4.  **Security**: The system then returns to standby.
5.  **Result**: A smart alarm that tells the dispatcher *exactly* what type of help is needed using international Morse standards.
6.  **Outcome**: Understanding how data can define the nature of an alert.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
btn_f = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_m = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Simple sender function
def send(pat):
    for char in pat:
        if char == ".": bz.freq(1000); bz.duty_u16(30000); utime.sleep(0.1)
        elif char == "-": bz.freq(1000); bz.duty_u16(30000); utime.sleep(0.3)
        elif char == " ": utime.sleep(0.3); continue # Gap
        bz.duty_u16(0); utime.sleep(0.1)

while True:
    if btn_f.value():
        print("FIRE ALERT")
        send("..-. .. .-. .") # F I R E
        utime.sleep(1)
    elif btn_m.value():
        print("MEDICAL ALERT")
        send("-- . -..") # M E D
        utime.sleep(1)
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Overlap**: If you press both buttons at once, the `if/else if` logic will choose the first one (GP14/Fire). This is actually professional practice to ensure "Fire" always has priority over other alerts!

### 12. Try This Next
*   **SMS Bridge**: if you have a Wifi Pico (Project 0180), make it send an actual text message when the Morse is triggered.

---

## 1. Project 0298: The Morse Code Game

### 2. Learning Objective
Explore sequence replication (The Call-Response Game). Learn how to implement an interactive system that plays a short Morse pattern and challenges the user to replicate it exactly, testing both auditory memory and manual dexterity.

### 3. Concepts Introduced
*   **Playback vs Capture**: transitioning from an output state (Buzzer) to an input state (Button).
*   **Array Matching (concept)**: comparing a list of dots/dashes to a target list.
*   **Pattern Increasing**: making the "Question" longer as the user gets better.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Radio Master** | GP15 | The Teacher (Buzzer) |
| **Recruit Key** | GP14 | The Student (Button) |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking pattern)
*   **from Time, drag `pico_time_ms`** (measuring user)
*   **from Logic, drag `controls_if`** (grading)

### 7. Variables
*   **target_seq**: list of '.' and '-'.
*   **user_seq**: list of what the user tapped.

### 8. Step-by-Step Guide

**A. Presentation Phase**
1.  **Teacher Call**:
    *   Play Dot-Dot (..).
    *   **Print** "Pico: Dot-Dot. Your turn!".

**B. Interaction Phase**
2.  **Student Response**:
    *   Wait for **Button** GP14. Record duration.
    *   Store as "Dot" or "Dash" in `user_seq`.

**C. Evaluation Phase**
3.  **Grade**:
    *   If `user_seq` matches `target_seq`:
        *   **Print** "CORRECT! ADVANCING TO LEVEL 2.".
        *   **Play** Victory Sound.
    *   Else:
        *   **Print** "INCORRECT. REPEAT AFTER ME...".
        *   **Play** Warning.

### 9. Execution Flow
1.  **Call**: Pico beeps: "." (Short).
2.  **Response**: You tap "." (Short).
3.  **Advance**: Pico beeps: ". -" (Short-Long).
4.  **Response**: You tap ". -" (Short-Long).
5.  **Result**: An interactive teacher that helps you learn the rhythm of Morse through physical practice.
6.  **Outcome**: Mastery of the "Call-Response" cycle found in military and emergency radio protocols.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Level 1 Question
challenge = ["dot", "dot"]

while True:
    print("Pico: . .")
    for _ in range(2):
        bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.1); bz.duty_u16(0); utime.sleep(0.1)
        
    print("YOUR TURN!")
    user = []
    for _ in range(2):
        while btn.value() == 0: pass
        t1 = utime.ticks_ms()
        while btn.value() == 1: pass
        t2 = utime.ticks_ms()
        
        d = utime.ticks_diff(t2, t1)
        if d < 250: user.append("dot")
        else: user.append("dash")
        utime.sleep(0.1)
        
    print("User: " + str(user))
    if user == challenge:
        print("WIN!")
        bz.freq(1500); bz.duty_u16(20000); utime.sleep(0.3); bz.duty_u16(0)
    else:
        print("FAIL!")
        bz.freq(200); bz.duty_u16(20000); utime.sleep(0.5); bz.duty_u16(0)
        
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Wait Forever**: If you miss a beat, the Pico will wait forever for you to click. Use a `timeout` variable (Project 0277) to say "Too slow!" if the user doesn't respond in time.

### 12. Try This Next
*   **Random Level**: generate a random 3-bit pattern for every round to make it unpredictable.

---

## 1. Project 0299: Automated Morse Code

### 2. Learning Objective
Explore optical data transmission (The Light Modem). Learn how to implement the "Sender" logic of a communication system that uses light pulses (LED) instead of sound, preparing for advanced infrared or fiber-optic data projects.

### 3. Concepts Introduced
*   **Visual Serial Interface**: sending binary data via photons.
*   **Noise Immunity (concept)**: why Morse is better than speech for distant light signals (easy to see blinking from far away).
*   **Automatic Handloading**: coding a whole string of text to send automatically.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 High-Brightness LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Transmit LED** | GP15 | The Optical Antenna |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (pulsing)
*   **from Time, drag `pico_wait`** (timing units)

### 7. Variables
*   **None**: this is a hard-coded optical beacon.

### 8. Step-by-Step Guide

**A. Structure "HI" (.... ..)**
1.  **Define units**:
    *   Dot = 0.2s.
    *   Gap = 0.2s.

**B. Transmit Pulse**
2.  **Letter H**:
    *   **Loop** 4 times: **On** 0.2s, **Off** 0.2s.
3.  **Letter Gap**:
    *   **Off** for 0.6s.
4.  **Letter I**:
    *   **Loop** 2 times: **On** 0.2s, **Off** 0.2s.

**C. Global Loop**
5.  **Restart**: **Wait** 3 seconds before next flash.

### 9. Execution Flow
1.  **Pulsing**: The Pico starts flashing the LED in a 4-pulse pattern.
2.  **Transmission**: The photons travel across the room.
3.  **Reception (Next level)**: A second person (or a second Pico with an LDR) sees the flashes and decodes them as "HI".
4.  **Result**: You have built an optical modem that works over long distances without any wires between the sender and receiver.
5.  **Outcome**: Understanding the foundation of modern fiber-optic internet.

### 10. Generated Code
```python
from machine import Pin
import time

tx_led = Pin(15, Pin.OUT)

def flash_code(pat):
    for char in pat:
        if char == ".":
            tx_led.value(1); time.sleep(0.2); tx_led.value(0)
        elif char == "-":
            tx_led.value(1); time.sleep(0.6); tx_led.value(0)
        time.sleep(0.2) # Gap between parts

while True:
    print("Transmitting Optical Morse: HI")
    # H
    flash_code("....")
    time.sleep(0.4) # Letter gap
    # I
    flash_code("..")
    
    time.sleep(3)
```

### 11. Common Mistakes
*   **Ambient Light**: In a bright room, the "Off" state might still look like it's on because of reflections. Use a bright LED and a black paper tube to help the receiver see the signals more clearly.

### 12. Try This Next
*   **Dual Transmit**: flash two different LEDs at the same time for redundancy.
*   **Remote Control**: use your optical sender to "Talk" to a light sensor (Project 0156) that opens a door.

---

## 1. Project 0300: Mastering Morse Code

### 2. Learning Objective
Explore asynchronous input buffering and parsing (The Smart Decoder). Learn how to implement a complex system that collects multiple human inputs (Dots/Dashes) into an "Array" or "List", detects the end of a character via silence (Time-Out), and uses a dictionary to translate that collection into a human letter (e.g. "F").

### 3. Concepts Introduced
*   **Data Buffering**: Temporarily storing multiple inputs before processing them as a whole.
*   **Time-Out Recognition**: using a lack of activity (e.g. 2s of silence) to mark the end of a data packet.
*   **Dictionary Mapping**: converting a pattern (['.', '.', '-', '.']) into a character ('F').

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 High-quality Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Input Key** | GP14 | Manual Morse Input |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking the list)
*   **from Time, drag `pico_time_ms`** (measuring silence)
*   **from Logic, drag `controls_if`** (evaluating result)

### 7. Variables
*   **input_buffer**: List containing current sequence of bits.
*   **last_press**: Time since the last button interaction.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear Buffer**: **Set** `input_buffer` = [empty].

**B. Monitoring Phase (Input)**
2.  **Collect Bits**:
    *   If **Button** GP14 Pressed:
        *   **Measure** duration.
        *   If < 0.3s: **Add** "." to `input_buffer`.
        *   Else: **Add** "-" to `input_buffer`.
        *   **Set** `last_press` = **Time** `pico_time_ms`.
        *   **Print** "Buffer: ", `input_buffer`.

**C. Decision Phase (Silence)**
3.  **Detect End-of-Letter**:
    *   If (`pico_time_ms` - `last_press`) > 2000 (2 seconds):
        *   If `input_buffer` is NOT empty:
            *   **GO TO DECODING**.

**D. Decoding Phase**
4.  **Translate**:
    *   If `input_buffer` is [".", ".", "-", "."]:
        *   **Print** "TRANSLATION: F".
        *   **Clear** `input_buffer`.

### 9. Execution Flow
1.  **Input**: You tap ".", ".", "-", ".". 
2.  **Buffering**: The Pico adds each one to its list. It doesn't know what you are saying yet.
3.  **Silence**: You stop tapping. 1 second passes... 2 seconds pass.
4.  **Recognition**: The Pico sees the silence! It looks at its list: [". . - ."].
5.  **Dictionary**: It searches its brain and finds that this pattern belongs to "F".
6.  **Result**: The screen says "F". You have successfully talked to the computer in Morse!

### 10. Generated Code
```python
import machine
import utime

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# MASTER DICTIONARY (Snippet)
MORSE_MAP = {
    "....": "H", "..": "I", ".-": "A", "-...": "B",
    "..-.": "F", "---": "O", "...": "S"
}

buffer = ""
last_act = utime.ticks_ms()

print("Ready to decode. Start tapping!")

while True:
    # 1. Collect Input
    if btn.value() == 1:
        t1 = utime.ticks_ms()
        while btn.value() == 1: pass
        t2 = utime.ticks_ms()
        
        dur = utime.ticks_diff(t2, t1)
        if dur < 250: buffer += "."
        else: buffer += "-"
        
        print("Buffer: " + buffer)
        last_act = utime.ticks_ms()
        utime.sleep(0.1) # Debounce
        
    # 2. Check for Silence (2 seconds)
    if buffer != "" and utime.ticks_diff(utime.ticks_ms(), last_act) > 2000:
        # LOOKUP
        if buffer in MORSE_MAP:
            print(">>> LETTER FOUND: " + MORSE_MAP[buffer])
        else:
            print(">>> Error: Unknown pattern " + buffer)
        
        buffer = "" # Reset
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Buffer Reset**: If you don't clear the buffer after the silence, your next letter will be added to the old one (e.g. "H" + "I" = ".... .."), which might not result in a valid character.

### 12. Try This Next
*   **Complete Alphabet**: Add all 26 letters to your `MORSE_MAP`.
*   **Text Message**: append the discovered letters to a string called `message` and only print it when you double-click the button.

---
