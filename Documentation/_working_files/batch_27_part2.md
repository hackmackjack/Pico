
## 1. Project 0266: Smart Doorball Switch

### 2. Learning Objective
Explore rate-limited automatic triggering (The Doormat Sensor). Learn how to implement a system that detects a continuous input (someone standing on a mat) but restricts the output response (Ringing the bell) to once per a specific interval, preventing "Harmonic Stalling" or repetitive noise.

### 3. Concepts Introduced
*   **Rate Limiting**: restricting how often an event can fire regardless of how many times it is triggered.
*   **Tactile Pressure Sensing**: using a large-area contact (Switch) to detect a person's presence.
*   **Cooldown Timers**: using a variable or wait block to ensure "Silence" after an action.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (Simulating a pressure-sensitive mat)
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Doormat Button** | GP14 | Triggered by feet |
| **System Buzzer** | GP15 | Alert output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking the mat)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)
*   **from Actuators, drag `pico_buzzer_off`** (silence)
*   **from Time, drag `pico_wait`** (cooldown period)

### 7. Variables
*   **None**: the sequential wait provides the rate limit.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Wait for Weight**:
    *   If **Button** GP14 is Pressed:
        *   **Print** "Person detected on doormat.".

**B. Execution Phase**
3.  **Ring the Alarm**:
    *   Inside the **If** block, **Set** Buzzer to 1000Hz (BEEP!).
    *   From **Time**, **Wait** 0.5s.
    *   **Set** Buzzer to OFF.

**C. Rate Limiting Phase**
4.  **Enforce Cooldown**:
    *   After the ring finishes, **Wait** 30 seconds.
    *   *Note: Even if the person stays on the mat for 2 full minutes, the bell will only ring once every 30s.*
5.  **Status**: **Print** "Doormat cooldown complete. Ready.".

### 9. Execution Flow
1.  **Input**: A person stands on the mat.
2.  **Action**: The Pico sees the button is down. It rings the buzzer for a split second.
3.  **Lockdown**: The Pico hits the 30-second "Wait" block. It is now "blind" to the button.
4.  **Ignore**: For the next 29 seconds, the buzzer stays silent even though someone is still standing there.
5.  **Reset**: Once the 30s are up, the loop restarts and it is ready to ring again if someone is still there.
6.  **Result**: An intelligent doorbell that doesn't annoy the user if a guest stands still for too long.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

mat = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = PWM(Pin(15))

while True:
    if mat.value() == 1:
        # Ring once
        bz.freq(1000); bz.duty_u16(32768); time.sleep(0.5)
        bz.duty_u16(0)
        
        print("Someone is at the door! Ringing once.")
        
        # RATE LIMIT WAIT
        # The Pico does nothing else for 30s
        time.sleep(30)
        print("Sensor armed and ready.")
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Short Cooldown**: If you set the cooldown to 1 second, it will sound like a broken siren when a heavy package is left on the mat. Use 30-60s for real front doors.

### 12. Try This Next
*   **Variable Cooldown**: add a switch (Project 0206) to choose between 10s and 60s cooldown depending on how busy the house is.
*   **Night Mode**: use an LDR so the doormat only rings during the day and only flashes a light at night.

---

## 1. Project 0267: Doorball Alarm System

### 2. Learning Objective
Explore security state validation (The Forced Entry Detection). Learn how to create a "Dual-Input" system that compares the state of a door sensor (Reed Switch) against the state of a "Permission" system (Unlock Button) to detect an unauthorized opening.

### 3. Concepts Introduced
*   **Unauthorized State**: When a physical action happens without the correct software permission.
*   **Reed Switch Interaction**: Using magnetism to detect if a door is physically open or closed.
*   **Precedence Logic**: checking if "Condition A" happened BEFORE "Condition B".

### 4. Hardware Required
*   Raspberry Pi Pico
*   Reed Switch (Magnetic Door Sensor)
*   1 Button (The Unlock Permission)
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Reed Switch** | GP14 | Closed = Safe, Open = Breach |
| **Unlock Button** | GP13 | Press to authorize entry |
| **Alarm Buzzer** | GP15 | Intruders only |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking permission)
*   **from Logic, drag `controls_if`** (evaluating breach)
*   **from Smart IO, drag `pico_gpio_read`** (read sensor)

### 7. Variables
*   **door_unlocked**: Boolean tracking if the resident authorized the opening.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Handle Authorization**:
    *   If **Button** GP13 (Unlock) is Pressed:
        *   **Set** `door_unlocked` = True.
        *   **Wait** 5 seconds (The "Safe" window to enter).
        *   **Set** `door_unlocked` = False.

**B. Detection Phase**
3.  **Check for Entry**:
    *   If **Reed Switch** GP14 is OPEN (Lid/Door opened):
        *   If `door_unlocked` is False:
            *   **START ALARM!** **Set** Buzzer -> HIGH.
            *   **Print** "SECURITY BREACH! FORCED ENTRY!".
        *   Else:
            *   **Print** "Authorized entry detected. System OK.".

### 9. Execution Flow
1.  **Normal**: You press the "Unlock" button. The Pico sets a variable to "True" for 5 seconds. You open the door. The Pico sees it is authorized. Everything is fine.
2.  **Breach**: An intruder pries the door open without pressing the button.
3.  **Logic**: The Pico sees the door is OPEN but the variable is still FALSE.
4.  **Reaction**: The alarm triggers immediately.
5.  **Result**: A smart security system that can tell the difference between a resident and a thief.

### 10. Generated Code
```python
from machine import Pin
import time

door = Pin(14, Pin.IN, Pin.PULL_UP) # Closed to GND = 0
btn = Pin(13, Pin.IN, Pin.PULL_DOWN)
siren = Pin(15, Pin.OUT)

is_safe = False

while True:
    # 1. Listen for resident button
    if btn.value() == 1:
        print("Entry authorized for 5s...")
        is_safe = True
        # Resident has 5s to open door
        # In a real app, this would be non-blocking
        
    # 2. Check door status
    # Assuming door open = 1 (PULL_UP logic)
    if door.value() == 1:
        if not is_safe:
            print("--- ALARM ---")
            siren.value(1)
        else:
            print("Welcome home.")
            is_safe = False # Reset after entry
            
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Blocking Auth**: In the simple logic above, if you press the button, the Pico might "Wait" for 5 seconds. If the intruder breaks in DURING those 5 seconds, they might not be detected! It's better to use timestamps (Project 0219).

### 12. Try This Next
*   **Latch the Siren**: make it so you need a secret button (Project 0264) to turn the alarm back off.

---

## 1. Project 0268: The Doorball Game

### 2. Learning Objective
Explore high-speed duration measurement (Ding-Dong Ditch). Learn how to implement a game that uses the Pico's internal clock to measure the exact millisecond duration of a button press, rewarding "Ninja" speed.

### 3. Concepts Introduced
*   **Impulse Measurement**: measuring very short events (less than 100ms).
*   **Human Reaction Time**: understanding the limits of physical speed.
*   **Threshold Feedback**: using different sound effects to signal "Success" or "Failure".

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Game Button** | GP14 | Measure tap length |
| **Result Speaker** | GP15 | Beeps for Ninja/Caught |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Time, drag `pico_time_ms`** (timestamping)
*   **from Variables, drag `variables_set`** (storing duration)
*   **from Logic, drag `controls_if`** (evaluating speed)

### 7. Variables
*   **t1, t2**: start and end timestamps.
*   **press_len**: total time in milliseconds.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Wait for Touch**:
    *   Repeat-until **Button** GP14 is Pressed.
    *   **Set** `t1` = **Time** `pico_time_ms`.

**B. Release Phase**
3.  **Wait for Let-Go**:
    *   Repeat-until **Button** GP14 is Released.
    *   **Set** `t2` = **Time** `pico_time_ms`.

**C. Scoring Phase**
4.  **Calculate Speed**:
    *   **Set** `press_len` = `t2` - `t1`.
    *   **If** `press_len` < 100 (milliseconds):
        *   **Print** "NINJA! Time: ", `press_len`, "ms".
        *   Play High Tone.
    *   **Else**:
        *   **Print** "CAUGHT! Time: ", `press_len`, "ms".
        *   Play Low Tone.

### 9. Execution Flow
1.  **Interaction**: You try to tap the button as fast as humanly possible.
2.  **Timing**: The Pico records 60ms between the down-click and the up-click.
3.  **Verdict**: Since 60 < 100, you are a "Ninja". The Pico rewards you with a victory chirp.
4.  **Result**: An interactive speed-training game.

### 10. Generated Code
```python
import machine
import utime

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bz = machine.PWM(machine.Pin(15))

while True:
    # 1. Wait for touch
    while btn.value() == 0: pass
    t1 = utime.ticks_ms()
    
    # 2. Wait for release
    while btn.value() == 1: pass
    t2 = utime.ticks_ms()
    
    # 3. Score
    diff = utime.ticks_diff(t2, t1)
    
    if diff < 100:
        print("NINJA! " + str(diff) + "ms")
        bz.freq(2000); bz.duty_u16(30000); utime.sleep(0.1); bz.duty_u16(0)
    else:
        print("CAUGHT! " + str(diff) + "ms")
        bz.freq(200); bz.duty_u16(30000); utime.sleep(0.5); bz.duty_u16(0)
        
    utime.sleep(1) # Gap
```

### 11. Common Mistakes
*   **Slow Polling**: If you use a `time.sleep` block inside your loop, you might "miss" either the press or the release, making the game feel laggy. Always use empty `while` loops for high-speed measurement.

### 12. Try This Next
*   **Leaderboard**: Track your fastest tap ever and print "New High Score!" if you beat it.
*   **Difficulty Scaling**: reduce the Ninja limit from 100ms to 80ms to make it harder.

---

## 1. Project 0269: Automated Doorball

### 2. Learning Objective
Explore multi-actuator coordination (The Auto-Opener). Learn how to combine an input trigger (The Bell) with a timed sequence involving both audio and mechanical motion (Servo), creating a fully automated visitor greeting system.

### 3. Concepts Introduced
*   **Robotic Interaction Sequences**: performing a chain of events (Sound -> Wait -> Move -> Wait -> Move).
*   **Access Control**: using a servo as a mechanical latch or door opener.
*   **Timing Safety**: providing a "Clearance" window so the person has time to walk through before the lock engages.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 Buzzer
*   1 Servo Motor + External Power
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Doorbell** | GP14 | Guest request |
| **Servo (Gate)** | GP15 | Physical opener |
| **Alert Buzzer** | GP13 | Inside chime |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_buzzer_pitch`** (beep)
*   **from Actuators, drag `pico_servo_write`** (move motor)
*   **from Time, drag `pico_wait`** (sequencing)

### 7. Variables
*   **None**: this is a linear command sequence.

### 8. Step-by-Step Guide

**A. Trigger Phase**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Detect Visitor**:
    *   If **Button** GP14 is Pressed:
        *   **Set** Buzzer to 800Hz. **Wait** 0.5s. **Silence**.

**B. Sequence Phase**
3.  **Resident Response Delay**:
    *   **Wait** 2 seconds (Simulating the resident "checking" the camera).
4.  **Open Door**:
    *   From **Actuators**, **Set** Servo GP15 to 90 degrees.
    *   **Print** "Door UNLOCKED. Welcome!".
5.  **Entry Window**:
    *   From **Time**, **Wait** 5 seconds.

**C. Cleanup Phase**
6.  **Secure Door**:
    *   **Set** Servo to 0 degrees.
    *   **Print** "Door secured.".

### 9. Execution Flow
1.  **Request**: Guest presses the button. They hear a "Ping".
2.  **Grace**: The system waits for 2 seconds.
3.  **Action**: The lock clicks open and the servo swings the latch.
4.  **Entry**: The guest has 5 seconds to push the door open.
5.  **Lock**: The servo swings back, securing the door for next time.
6.  **Result**: An professional automated entry system for a smart home.

### 10. Generated Code
```python
import machine
import utime

# Hardware
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
siren = machine.PWM(machine.Pin(13))
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_lock(angle):
    # Standard 0-180 logic (approx 2000 to 8000 duty)
    duty = int((angle / 180) * 6000 + 2000)
    servo.duty_u16(duty)

while True:
    if btn.value() == 1:
        # 1. Signal
        siren.freq(800); siren.duty_u16(32768); utime.sleep(0.5)
        siren.duty_u16(0)
        
        # 2. Greeting Delay
        utime.sleep(2)
        
        # 3. Open
        print("DOOR OPENED")
        set_lock(90)
        
        # 4. Entry Time
        utime.sleep(5)
        
        # 5. Close
        print("DOOR SECURED")
        set_lock(0)
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Servo Power**: if the Pico reboots every time the door tries to open, your servo is "starving" for power. Connect the Servo "VCC" pin to an external battery or the VBUS pin of the Pico (if plugged into USB).

### 12. Try This Next
*   **PIR Opener**: instead of a button, use a motion sensor (Project 0236) to open the door automatically when someone approaches.
*   **Buzzer Countdown**: beep the buzzer during the 5s entry window to warn the person the door is about to lock.

---

## 1. Project 0270: Mastering Doorball

### 2. Learning Objective
Explore non-contact proximity detection (The "Invisible" Doorbell). Learn how to use distance data from an ultrasonic sensor to detect an approaching guest and implement a "Silent" doorbell that only alerts the resident via light and a soft tone.

### 3. Concepts Introduced
*   **Invisible Triggers**: triggering events without the user having to touch any hardware.
*   **Distance Zones**: defining "Far" (nothing), "Near" (Alert 1), and "Very Near" (Bell ring).
*   **Zero-Infection Interfaces**: understanding why "No-Touch" buttons are preferred in public spaces.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Ultrasonic Sensor (HC-SR04)
*   LED
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Trig / Echo** | GP14, 13 | Visitor detector |
| **Alert LED** | GP15 | Silent notification |
| **Alert Buzzer** | GP12 | Residents chime |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_ultrasonic_dist`** (detecting guest)
*   **from Logic, drag `controls_if`** (evaluating zone)
*   **from Actuators, drag `pico_buzzer_pitch`** (chime)

### 7. Variables
*   **dist**: distance of target in cm.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Scan the Porch**:
    *   **Set** `dist` = **Sensors** `pico_ultrasonic_dist` GP14/13.

**B. Zone Logic**
3.  **In Range (10-30cm)**:
    *   If `dist` < 30:
        *   **Set** LED (GP15) -> HIGH.
        *   **Print** "Visitor detected in approach zone.".
4.  **Activation (< 10cm)**:
    *   If `dist` < 10:
        *   **Set** Buzzer to 800Hz. **Wait** 0.1s. **Silence**.
        *   **Print** "DOORBELL TRIGGERED (TOUCHLESS)".
        *   **Wait** 3 seconds (to prevent double-rings).

**C. Idle Phase**
5.  **Off-Target**:
    *   Else: **Set** LED LOW.

### 9. Execution Flow
1.  **Approach**: You walk toward the sensor. At 25cm, the Blue LED turns on. You know the system "sees" you.
2.  **Wave**: You put your hand close (8cm) to the sensor.
3.  **Ring**: The buzzer inside the house sounds a "Ding".
4.  **Result**: You rang the doorbell without touching a single button, making it clean and futuristic.

### 10. Generated Code
```python
import machine
import utime

# Sensor
trig = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(13, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
bz = machine.PWM(machine.Pin(12))

def get_dist():
    trig.low(); utime.sleep_us(2); trig.high(); utime.sleep_us(10); trig.low()
    while echo.value() == 0: pass
    t1 = utime.ticks_us()
    while echo.value() == 1: pass
    t2 = utime.ticks_us()
    return (utime.ticks_diff(t2, t1) * 0.0343) / 2

while True:
    d = get_dist()
    
    if d < 10:
        # Ring!
        led.value(1)
        bz.freq(800); bz.duty_u16(32768); utime.sleep(0.5)
        bz.duty_u16(0)
        print("TOUCHLESS RING")
        utime.sleep(3) # Anti-retrigger
    elif d < 30:
        # Warning/Detection
        led.value(1)
        print("Approach detected")
    else:
        led.value(0)
        
    utime.sleep(0.1)
```

### 11. Common Mistakes
*   **Sensor Noise**: In a busy hallway, random objects might trigger the "Touchless" doorbell. Ensure the sensor is shielded or angled correctly so it only sees the intended area.

### 12. Try This Next
*   **Automatic Hand Sanitizer**: connect a motor (Project 0231) to a pump that dispenses soap every time someone "Rings" the touchless bell.

---
