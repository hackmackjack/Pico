
# BATCH 30: Morse Code 2 (Projects 0291-0300)

## 1. Project 0291: Introduction to Morse Code

### 2. Learning Objective
Explore dual-modality output (The Visual/Audio Sync). Learn how to synchronize a digital output (LED) and a high-frequency pulse (Buzzer) to transmit information simultaneously across two different human senses (Sight and Sound).

### 3. Concepts Introduced
*   **Modality Synchronization**: performing the same action on two different types of hardware.
*   **Morse Code Basics**: understanding that letters are made of short "Dots" and long "Dashes".
*   **Temporal Precision**: ensuring the light and sound start and stop at the exact same millisecond.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + Resistor
*   1 Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Signal Light** | GP15 | Visual pulse |
| **Signal Sound** | GP14 | Auditory pulse |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)
*   **from Actuators, drag `pico_buzzer_pitch`** (set Sound)
*   **from Time, drag `pico_wait`** (signal duration)

### 7. Variables
*   **None**: this is a fixed message sequence ("HI").

### 8. Step-by-Step Guide

**A. Transmit "H" (....)**
1.  **Dot Sequence**:
    *   **Loop** 4 times:
        *   **Turn ON** LED (GP15). **Set** Buzzer to 800Hz.
        *   **Wait** 0.1s.
        *   **Turn OFF** LED. **Silence** Buzzer.
        *   **Wait** 0.1s.

**B. Transmit "I" (..)**
2.  **Wait for Letter Gap**: **Wait** 0.3s.
3.  **Dot Sequence**:
    *   **Loop** 2 times:
        *   **Action**: (Same as Step 1).
        *   **Wait** 0.1s.

**C. Maintenance Phase**
4.  **Loop**: Place everything inside a `pico_forever` loop with a 2-second gap between messages.

### 9. Execution Flow
1.  **Signal**: The Pico fires both GP15 and GP14 at once.
2.  **Modality**: You see a flash and hear a "Pip".
3.  **Timing**: Four fast pips represent "H". Two pips represent "I".
4.  **Result**: The message "HI" is broadcast across the room, which can be seen if you are deaf or heard if you are blind.
5.  **Outcome**: Understanding accessibility in communication design.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

led = Pin(15, Pin.OUT)
bz = PWM(Pin(14))

def pulse(duration):
    led.value(1)
    bz.freq(800); bz.duty_u16(32768)
    time.sleep(duration)
    led.value(0)
    bz.duty_u16(0)
    time.sleep(0.1) # Gap between parts of same letter

while True:
    print("Broadcasting: HI")
    # H: ....
    for _ in range(4): pulse(0.1)
    time.sleep(0.3) # Letter gap
    
    # I: ..
    for _ in range(2): pulse(0.1)
    
    time.sleep(2) # Message gap
```

### 11. Common Mistakes
*   **Unsync**: If you turn the LED on, wait 0.1s, then turn the Buzzer on, the signals won't match perfectly. Always perform the "ON" commands for both pins one after the other with no wait in between.

### 12. Try This Next
*   **Tone Mix**: can you make the "H" a high tone and the "I" a low tone?
*   **SOS**: change the sequence to play "SOS" ([... --- ...]).

---

## 1. Project 0292: Blinking Morse Code

### 2. Learning Objective
Explore time-dilated signal analysis (Slow Motion Morse). Learn how to play a complex message (SOS) at an extremely slow speed (5 seconds per dot) to clearly observe the mathematical relationship between the "Unit Time" (t) of a dot vs. a dash.

### 3. Concepts Introduced
*   **Unit Timing (T)**: in Morse, 1 Dash = 3 Dots.
*   **Gap Timing**: 1 space = 1 dot. 1 letter gap = 3 dots.
*   **Time Dilation**: slowing down data transmission to reveal its structure.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pulse LED** | GP15 | Primary visual signal |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (expanded intervals)

### 7. Variables
*   **unit_t**: Number (5 seconds) defining the speed.

### 8. Step-by-Step Guide

**A. Define "SOS" Structure**
1.  **The Formula**:
    *   Dot = `unit_t`.
    *   Dash = `unit_t` * 3.
    *   Gap = `unit_t`.

**B. Transmit "S" (...)**
2.  **Short Pulses**:
    *   Repeat 3 times: **On** 5s, **Off** 5s.

**C. Transmit "O" (---)**
3.  **Long Pulses**:
    *   Repeat 3 times: **On** 15s, **Off** 5s.

**D. Transmit "S" (...)**
4.  **Final Sequence**:
    *   Repeat 3 times: **On** 5s, **Off** 5s.

### 9. Execution Flow
1.  **Watch**: The light turns ON and stays on for a very long time (5 seconds). You can see the battery voltage stabilizing.
2.  **Contrast**: The light turns OFF for 5 seconds.
3.  **Verify**: The "Dash" phase turns on for 15 seconds. It is exactly three times as long as the dot.
4.  **Result**: By slowing it down, the "Structure" of Morse code becomes obvious and easy to measure with a normal clock.
5.  **Outcome**: Mastery of temporal ratios in serial communication.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)

# SLOW MOTION: 1 unit = 5 seconds
T = 5

def send_signal(duration):
    led.value(1)
    time.sleep(duration)
    led.value(0)
    time.sleep(T) # Space between parts

while True:
    print("--- SOS SLOW MOTION START ---")
    
    # S: (Dot, Dot, Dot)
    for _ in range(3): send_signal(T)
    time.sleep(T * 2) # Letter gap (Total 3 units)
    
    # O: (Dash, Dash, Dash)
    for _ in range(3): send_signal(T * 3)
    time.sleep(T * 2)
    
    # S: (Dot, Dot, Dot)
    for _ in range(3): send_signal(T)
    
    print("FINISHED. Restarting loop.")
    time.sleep(T * 4)
```

### 11. Common Mistakes
*   **Patience**: This project takes over 2 minutes to complete one loop! Don't assume the code is frozen. It is just playing very, very slowly as requested.

### 12. Try This Next
*   **Fast Forward**: change `T` to 0.1 for a high-speed data burst.
*   **Buzzer addition**: add the synchronized buzzer from the previous project to the slow-motion loop.

---

## 1. Project 0293: Manual Morse Code Control

### 2. Learning Objective
Explore duration decoding (The Telegraph Key). Learn how to implement a system that measures the exact length of a human button press and categorizes it as either a "Dot" or a "Dash", providing digital translation for manual physical input.

### 3. Concepts Introduced
*   **Threshold Discrimination**: using a single number (e.g. 0.2s) to divide data into two types.
*   **Temporal Capture**: measuring the time between a "Press" and a "Release".
*   **Console Feedback**: reporting processed data back to a human monitor.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 High-quality Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Telegraph Key** | GP14 | Capture duration |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Time, drag `pico_time_ms`** (capturing stamps)
*   **from Logic, drag `controls_if`** (evaluating type)
*   **from Variables, drag `variables_set`** (storing duration)

### 7. Variables
*   **press_start**: timestamp of down-click.
*   **actual_len**: milliseconds of hold.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Wait for Event**:
    *   Wait until **Button** GP14 is Pressed.
    *   **Set** `press_start` = **Time** `pico_time_ms`.

**B. Release Phase**
3.  **Wait for Release**:
    *   Wait until **Button** GP14 is Released.
    *   **Set** `actual_len` = **Time** `pico_time_ms` - `press_start`.

**C. Classification Phase**
4.  **Sort the Data**:
    *   If `actual_len` < 250 (Roughly quarter second):
        *   **Print** "DOT (.)".
    *   Else:
        *   **Print** "DASH (-)".
5.  **Wait for Noise**: **Wait** 0.1s to prevent accidental re-triggers.

### 9. Execution Flow
1.  **Input**: You tap the button quickly. The Pico calculates "80ms".
2.  **Logic**: 80 is less than 250. The screen prints "DOT".
3.  **Input**: You hold the button for a long time. The Pico calculates "600ms".
4.  **Logic**: 600 is greater than 250. The screen prints "DASH".
5.  **Result**: You have a digital telegraph that "Cleans" your messy human movements into perfect dots and dashes.
6.  **Outcome**: Understanding the interface between analog human timing and binary data.

### 10. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    # 1. Wait for press
    while btn.value() == 0: pass
    t_start = time.ticks_ms()
    
    # 2. Wait for release
    while btn.value() == 1: pass
    t_end = time.ticks_ms()
    
    # 3. Process
    dur = time.ticks_diff(t_end, t_start)
    
    if dur < 250:
        print(".", end="") # Continuous string
    else:
        print("-", end="")
        
    time.sleep(0.05) # Tiny debounce
```

### 11. Common Mistakes
*   **No Release Check**: If you only check the "Press", the computer won't know how long you held it for! You MUST have two waiting loops: one for down, one for up.

### 12. Try This Next
*   **Buzzer Feedback**: make the buzzer play exactly as long as you hold the button, so you can "Hear" your telegraph while you use it.
*   **Space Detection**: if you haven't pressed the button for 2 seconds, print a "/" to show the end of a word.

---

## 1. Project 0294: Morse Code Sequences

### 2. Learning Objective
Explore random numeral transmission (The Number Station). Learn how to use a list or data structure to lookup the Morse patterns for digits (0-9) and generate a randomized sequence for "Spy" training exercises.

### 3. Concepts Introduced
*   **Lookup Tables (Concept)**: associating an index (the number 5) with a pattern (".....").
*   **Iterative Pattern Playback**: looping through a string and playing a dot or dash for each character.
*   **Randomized Training**: presenting information the user doesn't know in advance to test their decoding skills.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speaker** | GP15 | Training audio output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Math, drag `math_random_int`** (picking a number)
*   **from Variables, drag `variables_set`** (storing the secret)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)

### 7. Variables
*   **secret_num**: the number being sent.
*   **pattern**: the string of dots and dashes for that number.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare Patterns**: (In your head or a list): 1=.----, 2=..---, etc.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Choose the Secret**:
    *   **Set** `secret_num` = **Math** `random 0 to 9`.
    *   **Print** "Transmitting Secret Number... Get your pen ready!".

**C. Playback Phase**
4.  **Execute Pattern**:
    *   *Example for the number 3 (..---):*
    *   **Loop** 2 times: **Beep** 0.1s. **Wait** 0.1s. (Dots).
    *   **Loop** 3 times: **Beep** 0.3s. **Wait** 0.1s. (Dashes).

**D. Result Phase**
5.  **Reveal**: **Wait** 5 seconds (Time for user to write it down).
    *   **Print** "The number was: ", `secret_num`.

### 9. Execution Flow
1.  **Listen**: The buzzer makes a sequence: "Pip-Pip-Beep-Beep-Beep".
2.  **Decode**: You recognize the "..---" pattern. You write down "2".
3.  **Victory**: Five seconds later, the Pico confirms "The secret was 2".
4.  **Result**: An automated spy-trainer that helps you master the numeric 5-bit sequences of Morse.

### 10. Generated Code
```python
import machine
import utime
import urandom

bz = machine.PWM(machine.Pin(15))

# Lookup for 0-9
CODE = [
    "-----", ".----", "..---", "...--", "....-",
    ".....", "-....", "--...", "---..", "----."
]

def play_code(s):
    for char in s:
        if char == ".":
            bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.1)
        else:
            bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.3)
        bz.duty_u16(0); utime.sleep(0.1)

while True:
    num = urandom.randint(0, 9)
    print("New Transmission...")
    play_code(CODE[num])
    
    utime.sleep(5)
    print("Number was: " + str(num))
    print("--------------------")
```

### 11. Common Mistakes
*   **Fast Tempo**: If the training is too fast, a beginner won't be able to count the bits. Start with 0.2s dots and 0.6s dashes if playing for humans.

### 12. Try This Next
*   **Triple Series**: send 3 numbers in a row before revealing them.
*   **Higher Speed**: make the gap between letters shorter as you get better.

---

## 1. Project 0295: Interactive Morse Code

### 2. Learning Objective
Explore protocol flow control (The Handshake). Learn how to implement a "Call-and-Response" system where the Pico transmits a signal and then pauses indefinitely to wait for a specific user "Acknowledgment" (Button Press) before proceeding.

### 3. Concepts Introduced
*   **Data Handshaking**: ensuring the receiver is ready before sending the next piece of data.
*   **Blocking Acknowledgments**: pausing code execution until a hardware flag is set.
*   **Error Prevention**: preventing data loss by checking if the user is paying attention.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   Pushbutton (The "Copy" button)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Radio Out** | GP15 | Transmitter audio |
| **Ack Button** | GP14 | Manual Confirmation |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_buzzer_pitch`** (signaling)
*   **from Loops, drag `pico_wait_until`** (the handshake)
*   **from Smart IO, drag `pico_gpio_read`** (listening for user)

### 7. Variables
*   **None**: this is a state-blocking protocol.

### 8. Step-by-Step Guide

**A. Call Phase**
1.  **Transmit "A" (.-)**:
    *   **Beep** 0.1s. **Wait** 0.1s. **Beep** 0.3s.
    *   **Print** "Station Pico calling... Letter A sent. Waiting for ACK.".

**B. Handshake Phase**
2.  **Wait for User**:
    *   From **Loops**, drag `Repeat while Button (GP14) is LOW`.
    *   *Note: The code is stuck here until you press the button.*

**C. Response/Next Phase**
3.  **Proceed to "B" (-...)**:
    *   Once button is pressed:
    *   **Beep** 0.3s. **Loop** 3 times: **Beep** 0.1s.
    *   **Print** "ACK Received. Letter B sent.".

**D. Finish**
4.  **Loop**: restart at the first letter.

### 9. Execution Flow
1.  **Call**: You hear the Pico say "A".
2.  **Pause**: The Pico goes silent. It won't say "B" yet. 
3.  **Interaction**: You write down the "A" in your notebook, then press the "ACK" button.
4.  **Success**: The Pico immediately says "B". 
5.  **Result**: A reliable two-way communication protocol where no information is sent until the human is ready to receive it.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def send_letter(pattern):
    for char in pattern:
        if char == ".":
            bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.1)
        else:
            bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.3)
        bz.duty_u16(0); utime.sleep(0.1)

while True:
    print("Sending A...")
    send_letter(".-")
    
    print("Waiting for your acknowledgement...")
    # WAIT UNTIL BUTTON IS PRESSED
    while btn.value() == 0:
        utime.sleep_ms(10)
        
    print("ACK! Sending B...")
    send_letter("-...")
    
    # Wait for release before next loop
    while btn.value() == 1: utime.sleep_ms(10)
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Missing Release Check**: If you don't wait for the button to be "Let go", the Pico might see the same press as an acknowledgment for the NEXT letter too, skipping the protocol.

### 12. Try This Next
*   **Time-out**: make the Pico play a "sad" sound if you don't acknowledge its message within 10 seconds.
*   **Full Alphabet**: add more steps until the whole alphabet is sent with a handshake for every letter.

---
