
# BATCH 27: Doorball 2 (Projects 0261-0270)

## 1. Project 0261: Introduction to Doorball

### 2. Learning Objective
Explore multi-note audio patterns (The Triple Ding). Learn how to combine multiple `pitch` and `wait` blocks to create a recognizable melodic sequence that signals an event, rather than just a single monotonic beep.

### 3. Concepts Introduced
*   **Melodic Intervals**: using changes in frequency to create a musical "Signature".
*   **Sequential Audio Execution**: performing notes in a specific order (High-Low-High).
*   **Acoustic Branding**: identifying an event through its unique sound.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   1 Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speaker/Buzzer** | GP15 | Audio Output |
| **Doorbell Button** | GP14 | Trigger Input |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking the button)
*   **from Actuators, drag `pico_buzzer_pitch`** (play notes)
*   **from Actuators, drag `pico_buzzer_off`** (silence)
*   **from Time, drag `pico_wait`** (tempo)

### 7. Variables
*   **None**: this is a hard-coded musical sequence.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Wait for Guest**:
    *   If **Button** GP14 is Pressed:
        *   **Print** "Doorbell active! Playing 'Triple Ding'...".

**B. Melodic Phase**
3.  **Note 1 (High)**:
    *   Inside the **If** block, **Set** Buzzer to 1000Hz. **Wait** 0.2s.
4.  **Note 2 (Low)**:
    *   **Set** Buzzer to 600Hz. **Wait** 0.3s.
5.  **Note 3 (High)**:
    *   **Set** Buzzer to 1000Hz. **Wait** 0.2s.

**C. Cleanup Phase**
6.  **Silence**:
    *   **Set** `pico_buzzer_off`.
    *   **Wait** 1 second (Debounce/Pause before next ring).

### 9. Execution Flow
1.  **Read**: The Pico checks if someone is at the door.
2.  **Activate**: You push the button.
3.  **Perform**: The Pico immediately starts the script.
4.  **Sound**: "Ding (High) - Dong (Low) - Ding (High)".
5.  **Result**: A professional and welcoming doorbell chime that alerts the household.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

bz = PWM(Pin(15))
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        # High Note
        bz.freq(1000); bz.duty_u16(32768); time.sleep(0.2)
        # Low Note
        bz.freq(600); bz.duty_u16(32768); time.sleep(0.3)
        # High Note
        bz.freq(1000); bz.duty_u16(32768); time.sleep(0.2)
        
        # Off
        bz.duty_u16(0)
        time.sleep(1) # Gap
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Forgetting Silence**: If you don't use `pico_buzzer_off` at the end, the last note will hum forever after you let go of the button.
*   **Wait Times**: If your notes are too long (e.g. 2 seconds each), the guest will be long gone before the "Ding-Dong" finish!

### 12. Try This Next
*   **Tempo Dial**: add a potentiometer (Project 0195) to change how fast the "Ding-Dong" plays.
*   **LED Flash**: make the house lights flash whenever the bell rings for people who are wearing headphones.

---

## 1. Project 0262: Blinking Doorball

### 2. Learning Objective
Explore long-duration blocking logic (The Occupied Indicator). Learn how to implement a system that provides visual feedback for a significant duration (10 seconds) and intentionally ignores further inputs during that time to prevent "Bell Spamming".

### 3. Concepts Introduced
*   **Temporal Blocking**: writing code that refuses to listen to sensors while a task is in progress.
*   **Multi-Modal Feedback**: combining audible (Buzzer) and visual (Red LED) signals.
*   **Status Indicators**: using a light to communicate the "Busy" state of a room.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 Red LED + Resistor
*   1 Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Doorbell Button** | GP14 | Caller trigger |
| **Occupied LED** | GP15 | Status indicator |
| **Speaker** | GP13 | Audio chime |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (detecting click)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)
*   **from Time, drag `pico_wait`** (blocking duration)

### 7. Variables
*   **None**: the sequential wait handles the state.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Safety Check**: Ensure Red LED (GP15) is LOW.

**B. Response Phase**
3.  **Detect Ring**:
    *   If **Button** GP14 is Pressed:
        *   **Print** "Doorbell Rang! Notifying Resident.".

**C. Audio/Visual Phase**
4.  **Signal Arrival**:
    *   **Set** Buzzer to 800Hz for 0.5s.
5.  **Set "Busy" Mode**:
    *   **Set** GP15 (Red LED) -> HIGH.
    *   **Print** "Status: BUSY (10s Delay active)".

**D. Blocking Phase**
6.  **Wait Out the Clock**:
    *   **Wait** 10 seconds.
    *   *Note: Any further button presses during these 10 seconds are ignored because the Pico is "blocked" on this line.*
7.  **Reset**:
    *   **Set** GP15 -> LOW.

### 9. Execution Flow
1.  **Idle**: The door is quiet.
2.  **Action**: Someone mashes the button 10 times.
3.  **Reaction**: The Pico catches the FIRST press. It rings the bell and turns ON the "Occupied" LED.
4.  **Ignore**: For the next 10 seconds, the Pico is busy waiting. It doesn't see the other 9 presses.
5.  **Finish**: The LED turns off. The Pico is now ready for a new visitor.
6.  **Result**: Prevents annoying repetitive ringing while alerting the resident.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

red = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = PWM(Pin(13))

while True:
    if btn.value() == 1:
        # Ring once
        bz.freq(800); bz.duty_u16(32768); time.sleep(0.5)
        bz.duty_u16(0)
        
        # Turn on Busy Light
        red.value(1)
        print("Someone is at the door. Ignoring extra rings for 10s.")
        
        # BLOCKING WAIT
        time.sleep(10)
        
        # Reset
        red.value(0)
        print("Ready for next guest.")
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Sleep inside Loop**: if you place the 10-second sleep *outside* the `if` block, your doorbell will only work for 1 second every 11 seconds! Always ensure your long sleeps are triggered *by* the event.

### 12. Try This Next
*   **Blink Busy**: instead of solid ON, make the Red LED flash slowly during the 10 seconds to make it more noticeable.
*   **Resident Reset**: add a button INSIDE the room that cancels the 10-second busy light immediately if you answer the door.

---

## 1. Project 0263: Manual Doorball Control

### 2. Learning Objective
Explore configuration parameter selection (The Ringtone Selector). Learn how to use a physical switch to route a single trigger (The Button) to different blocks of code (Tones), allowing the user to customize the device's behavior.

### 3. Concepts Introduced
*   **Input Selection**: Using a switch to decide "Which" code path to follow.
*   **Audio Previews**: Playing a sound when a selection is changed so the user knows what they picked.
*   **Variable Logic Routing**: using an `if/else` based on switch state inside the main trigger block.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   1 Button (Doorbell)
*   1 Slide Switch
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Main Button** | GP14 | Trigger doorbell |
| **Select Switch** | GP13 | Tone A vs Tone B |
| **Speaker** | GP15 | Output sound |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (nested evaluation)
*   **from Actuators, drag `pico_buzzer_pitch`** (chimes)
*   **from Smart IO, drag `pico_gpio_read`** (checking switch)

### 7. Variables
*   **None**: switch position acts as the hardware variable.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Detect Ring Request**:
    *   If **Doorbell Button** GP14 is Pressed:
        *   **Continue to check selection.**

**B. Decision Phase (Nested Logic)**
3.  **Choose the Tune**:
    *   Inside the first "If" block, drag another `controls_if` with **else**.
    *   **Condition**: If **Switch** GP13 is HIGH.

**C. Musical Execution**
4.  **Tone A (Switch ON)**:
    *   Inside the second **If**: **Play** [500Hz, 800Hz]. **Wait** 0.5s.
5.  **Tone B (Switch OFF)**:
    *   Inside the second **Else**: **Play** [400Hz, 300Hz]. **Wait** 0.5s.

### 9. Execution Flow
1.  **Setup**: You slide the switch to the "A" position.
2.  **Action**: You press the doorbell.
3.  **Route**: The Pico sees the button is down. It then checks the switch. Since it is "A", it follows the high-pitched "Tone A" path.
4.  **Switch**: You move the slider to "B".
5.  **Action**: You press again. This time, the Pico follows the low-pitched "Tone B" path.
6.  **Result**: A doorbell that can be customized to the user's personality or seasonal preference.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
sw = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

def ring_a():
    bz.freq(800); bz.duty_u16(30000); utime.sleep(0.2)
    bz.freq(1000); bz.duty_u16(30000); utime.sleep(0.3)
    bz.duty_u16(0)

def ring_b():
    bz.freq(400); bz.duty_u16(30000); utime.sleep(0.2)
    bz.freq(300); bz.duty_u16(30000); utime.sleep(0.3)
    bz.duty_u16(0)

while True:
    if btn.value():
        if sw.value() == 1:
            print("Playing Tune A")
            ring_a()
        else:
            print("Playing Tune B")
            ring_b()
        utime.sleep(1) # Cooldown
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **No Cooldown**: If you don't use the `wait 1s` at the end, the tone will keep restarting hundreds of times while your finger is on the button, sounding like robot static.

### 12. Try This Next
*   **Preview Mode**: play a very short "chirp" of the selected tone every time the switch is moved, so the user knows what they just picked without having to press the main button.
*   **Three Tones**: use two switches to create four possible ringtone combinations.

---

## 1. Project 0264: Doorball Sequences

### 2. Learning Objective
Explore pattern-based security (The Secret Knock). Learn how to implement a system that monitors the timing of consecutive inputs and compares it to a predefined "Code" (Short-Short-Long), triggering an actuator (Servo) only if the rhythm is correct.

### 3. Concepts Introduced
*   **Temporal Pattern Matching**: checking the length of consecutive HIGH signals.
*   **Tolerance Windows**: allowing a user to be "close enough" (e.g. 0.2s vs 0.3s) without failing.
*   **Actuator Lockdown**: using code to keep a door locked until a mathematical condition is solved.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 Servo Motor + External Power
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Knock Button** | GP14 | Input pattern |
| **Door Lock** | GP15 | 0=Locked, 90=Open |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking state)
*   **from Time, drag `pico_time_ms`** (measuring presses)
*   **from Actuators, drag `pico_servo_write`** (unlock)
*   **from Logic, drag `controls_if`** (validating rhythm)

### 7. Variables
*   **press_time**: duration of current tap.
*   **knock_step**: tracking which part of the code we are on.

### 8. Step-by-Step Guide

**A. Monitoring Phase**
1.  **Wait for First Tap**:
    *   **Measure** GP14 Duration.
    *   If < 0.3s (Short): **Continue**. Else: **Restart**.

**B. Sequential Phase**
2.  **Wait for Second Tap**:
    *   **Measure** GP14 Duration.
    *   If < 0.3s (Short): **Continue**. Else: **Restart**.
3.  **Wait for Third Tap**:
    *   **Measure** GP14 Duration.
    *   If > 0.6s (Long): **SUCCESS**. Else: **Restart**.

**C. Execution Phase**
4.  **Unlock Door**:
    *   **Set** Servo (GP15) to 90 degrees.
    *   **Wait** 3 seconds.
    *   **Set** Servo to 0 degrees (Re-lock).

### 9. Execution Flow
1.  **Knock**: You tap the button quickly. The Pico writes "Short".
2.  **Verify**: You tap quickly again. "Short".
3.  **Hold**: You press and hold for one full second. "Long".
4.  **Unlock**: The Pico sees the pattern "Short-Short-Long". It acknowledges the code and swings the servo.
5.  **Result**: A biological "Key" that exists in your mind as a rhythm.

### 10. Generated Code
```python
import machine
import utime

servo = machine.PWM(machine.Pin(15))
servo.freq(50)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def get_press_duration():
    while btn.value() == 0: pass
    start = utime.ticks_ms()
    while btn.value() == 1: pass
    return utime.ticks_diff(utime.ticks_ms(), start)

while True:
    print("Enter Secret Knock...")
    # Step 1: Short
    if get_press_duration() < 300:
        print("Knock 1 OK")
        # Step 2: Short
        if get_press_duration() < 300:
            print("Knock 2 OK")
            # Step 3: Long
            if get_press_duration() > 600:
                print("ACCESS GRANTED")
                # Move servo (Duty 4000 to 8000 approx)
                servo.duty_u16(8000)
                utime.sleep(3)
                servo.duty_u16(4000)
                continue
    
    print("Wrong pattern. Lockdown.")
    utime.sleep(1)
```

### 11. Common Mistakes
*   **No Interval Check**: If you don't check for a pause between knocks, a human might accidentally merge two knocks together.
*   **Servo Jitter**: Always use an external battery for servos, as they can pull too much power from the Pico during a "Knock" sequence and cause a crash.

### 12. Try This Next
*   **Custom Code**: change the logic to Long-Short-Long.
*   **Failed Alert**: if someone misses the code 3 times, sound the buzzer for 10 seconds.

---

## 1. Project 0265: Interactive Doorball

### 2. Learning Objective
Explore user-interface timing (The Intercom Status). Learn how to implement "Permission Logic" where a visual signal (Green LED) tells the user when an external system is ready for input (Speaking/Talking), ensuring clear communication between people.

### 3. Concepts Introduced
*   **Turn-Taking Signals**: using light to coordinate social interaction.
*   **Active Window Duration**: providing a specific, timed period for a task.
*   **UX Design**: reducing "User Confusion" by clearly marking when an action is possible.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 Green LED + Resistor
*   1 Red LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Talk Button** | GP14 | Request to speak |
| **Ready LED (G)** | GP15 | "Speak Now" indicator |
| **Wait LED (R)** | GP13 | "Listen" indicator |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (detecting request)
*   **from Smart IO, drag `pico_gpio_write`** (switching LEDs)
*   **from Time, drag `pico_wait`** (talk duration)

### 7. Variables
*   **None**: this is a timed sequence machine.

### 8. Step-by-Step Guide

**A. Idle Phase**
1.  **Set Status**: **Turn ON** Red (GP13) and **Turn OFF** Green (GP15).
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Request Phase**
3.  **Check for Talk**:
    *   If **Button** GP14 is Pressed:
        *   **Print** "Intercom Request Received.".

**C. Execution Phase**
4.  **Open Mic**:
    *   **Turn OFF** Red LED.
    *   **Turn ON** Green LED.
    *   **Wait** 5 seconds.
    *   **Print** "Mircophone ACTIVE - Please Speak.".
5.  **Close Mic**:
    *   **Turn OFF** Green LED.
    *   **Turn ON** Red LED.
    *   **Print** "Talk window closed.".

### 9. Execution Flow
1.  **Wait**: The caller sees a Red light. They know they shouldn't speak yet.
2.  **Request**: The caller presses the button.
3.  **Signal**: The Red light vanishes and the Green light appears.
4.  **Interaction**: The caller sees the Green light and says "Hello?".
5.  **Finish**: After 5 seconds, the Green light disappears and Red comes back. The interaction is complete.
6.  **Result**: An organized, electronic system for managing turns in an intercom or gate system.

### 10. Generated Code
```python
from machine import Pin
import time

red = Pin(13, Pin.OUT)
green = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Initial state
red.value(1); green.value(0)

while True:
    if btn.value() == 1:
        # Switch to Talk mode
        red.value(0)
        green.value(1)
        print("--- SPEAKER ACTIVE: 5s ---")
        
        # Duration window
        time.sleep(5)
        
        # Return to Listen mode
        green.value(0)
        red.value(1)
        print("--- MIC CLOSED ---")
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **No Red LED**: If you don't use a Red LED to show the "Wait" state, the user won't know if the button press actually did anything. Always provide feedback for both "Ready" and "Not Ready".

### 12. Try This Next
*   **Warning Flash**: make the Green LED flash for the last 1 second to tell the user their time is almost up.
*   **Extending Time**: if the button is pressed AGAIN while the Green LED is on, add 5 more seconds to the timer.

---
