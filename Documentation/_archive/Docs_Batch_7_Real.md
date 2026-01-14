
# 🏁 Batch 7: Doorbells 1

## 1️⃣ Project 0061: Introduction to Doorbells
### 2️⃣ Learning Objective
Create a simple signaling device. You will connect a button and a buzzer to make a basic doorbell that sounds when pressed.

### 3️⃣ Concepts Introduced
*   **Auditory Feedback**: Using sound to confirm input.
*   **Momentary Switch**: The sound only plays while the button is held (or triggered once per press).

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Active Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [15] to [High]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Pressed: Buzzer ON.
    *   ELSE: Buzzer OFF.

### 9️⃣ Execution Flow (Plain English)
When the visitor presses the button, the circuit closes, and the buzzer gets power. When they let go, the buzzer stops.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)
while True:
    if btn.value():
        buzz.value(1)
    else:
        buzz.value(0)
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Active vs Passive**: This code works best with an Active Buzzer (just needs power). A Passive buzzer will just click; it needs a frequency (PWM).
*   **Polarity**: Buzzers have a + side.

### 1️⃣2️⃣ Try This Next
*   **Latch**: Make it ring for 1 second even if the button is just tapped.

---

## 1️⃣ Project 0062: Blinking Doorbell (Deaf Aid)
### 2️⃣ Learning Objective
Accessibility focus. Add a visual indicator (Light) for the hearing impaired alongside the sound.

### 3️⃣ Concepts Introduced
*   **Dual Output**: Triggering two different actuators (Light + Sound) from one event.
*   **Accessibility**: Designing for all users.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Buzzer**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |
| **LED** | GP14 |

### 6️⃣ Blocks Used
🔹 **Set Pin**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   Buzzer ON.
        *   LED ON.
    *   ELSE:
        *   Buzzer OFF.
        *   LED OFF.

### 9️⃣ Execution Flow (Plain English)
The doorbell now provides multi-sensory feedback. The light turns on exactly when the sound plays.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(14, machine.Pin.OUT)
while True:
    if btn.value():
        buzz.value(1)
        led.value(1)
    else:
        buzz.value(0)
        led.value(0)
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Current Draw**: Don't power a massive floodlight directly from the pin. Use a small LED.

### 1️⃣2️⃣ Try This Next
*   **Flash**: Make the light blink while the buzzer is solid.

---

## 1️⃣ Project 0063: Manual Doorbell Control (Tone)
### 2️⃣ Learning Objective
Control pitch manually. Button A makes a High tone (Front Door), Button B makes a Low tone (Back Door).

### 3️⃣ Concepts Introduced
*   **Distinction**: Identifying the source of an event.
*   **Frequency**: Pitch of sound.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**
*   **Passive Buzzer** (Required for tones)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Play Tone**
*   **Category:** Music
*   **Block:** `play tone [1000] Hz`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Btn A: Play 1000Hz.
    *   ELSE IF Btn B: Play 500Hz.
    *   ELSE: Stop Sound.

### 9️⃣ Execution Flow (Plain English)
The user can distinguish which door is ringing based on the sound. High pitch = Front, Low pitch = Back.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.PWM(machine.Pin(15))
while True:
    if btnA.value():
        buzz.freq(1000)
        buzz.duty_u16(32768)
    elif btnB.value():
        buzz.freq(500)
        buzz.duty_u16(32768)
    else:
        buzz.duty_u16(0)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Passive Requirement**: This project fails with an Active Buzzer (it will just squeak).

### 1️⃣2️⃣ Try This Next
*   **Ding Dong**: Make Button A trigger a sequence "High-Low".

---

## 1️⃣ Project 0064: Doorbell Sequences (Ding Dong)
### 2️⃣ Learning Objective
Automate a sound pattern. A single press triggers a "Ding-Dong" sequence (Two notes with sustain).

### 3️⃣ Concepts Introduced
*   **Sustain**: Holding a note for a duration.
*   **Decay**: (Simulated) Stopping the note.
*   **Non-Blocking vs Blocking**: This simple version "blocks" (pauses) while playing.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Function** (Optional, or linear code)

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   Play 800Hz (Ding) for 0.5s.
        *   Play 600Hz (Dong) for 1.0s.
        *   Silence.

### 9️⃣ Execution Flow (Plain English)
You don't hold the button for a Ding-Dong. A quick tap runs the whole show.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.PWM(machine.Pin(15))
while True:
    if btn.value():
        # Ding
        buzz.freq(800)
        buzz.duty_u16(32768)
        time.sleep(0.5)
        # Dong
        buzz.freq(600)
        buzz.duty_u16(32768)
        time.sleep(1.0)
        # Off
        buzz.duty_u16(0)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Spamming**: If you press the button repeatedly, it ignores you until the first Ding-Dong finishes (Blocking Code). This is usually desired behavior for doorbells.

### 1️⃣2️⃣ Try This Next
*   **Westminster Chime**: The classic 4-note school bell pattern.

---

## 1️⃣ Project 0065: Interactive Doorbell (Hold-to-Ring)
### 2️⃣ Learning Objective
Feedback loop. The bell rings, but only as long as you hold it? No, that's Project 61. Let's make it smarter: The bell rings for a minimum of 2 seconds, but if you hold it longer, it keeps ringing.

### 3️⃣ Concepts Introduced
*   **Minimum Run Time**: Ensuring a short tap creates a full signal.
*   **Extension**: Extending the signal if input persists.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **While Loop**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   Buzzer ON.
        *   Wait 2s (Minimum Ring).
        *   WHILE Button is Still Pressed: Wait 0.1s.
        *   Buzzer OFF.

### 9️⃣ Execution Flow (Plain English)
A tap gives a 2s ring. A long press gives a long ring (2s + extra). It never cuts off early.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)
while True:
    if btn.value():
        buzz.value(1)
        time.sleep(2) # Minimum
        while btn.value(): # Extension
            time.sleep(0.1)
        buzz.value(0)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Stuck**: If the button breaks (fails closed), the bell never stops.

### 1️⃣2️⃣ Try This Next
*   **Timeout**: Force stop after 10 seconds even if button is held (Prankster protection).

---

## 1️⃣ Project 0066: Smart Doorbell Switch (Secret Knock)
### 2️⃣ Learning Objective
Pattern recognition. The door only unlocks (Green LED) if the button is pressed 3 times quickly.

### 3️⃣ Concepts Introduced
*   **Counter**: Counting events within a window.
*   **Timing Window**: Resetting count if too slow.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Green LED** (Lock)
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Green LED** | GP14 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Count**
🔹 **Timer**

### 7️⃣ Variables & State
*   **pressCount**
*   **lastPressTime**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Pressed:
        *   `pressCount` += 1.
        *   Beep (Ack).
        *   Reset 2s timer.
    *   IF `pressCount` == 3:
        *   Unlock (Green LED ON).
        *   Play Melody.
        *   Reset Count.
    *   IF Timer Expired:
        *   Reset Count.

### 9️⃣ Execution Flow (Plain English)
Tap-Tap-Tap -> Open. Tap... Tap... (too slow) -> Reset.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
lock = machine.Pin(14, machine.Pin.OUT)
buzz = machine.Pin(15, machine.Pin.OUT)
count = 0
last_time = 0
while True:
    if btn.value():
        count += 1
        buzz.value(1); time.sleep(0.1); buzz.value(0)
        last_time = time.ticks_ms()
        while btn.value(): time.sleep(0.05) # Debounce release
    
    # Check Success
    if count >= 3:
        lock.value(1)
        buzz.value(1); time.sleep(0.5); buzz.value(0)
        time.sleep(2)
        lock.value(0)
        count = 0
        
    # Check Timeout (2 seconds)
    if count > 0 and time.ticks_diff(time.ticks_ms(), last_time) > 2000:
        count = 0 # Reset
        buzz.value(1); time.sleep(0.5); buzz.value(0) # Fail beep
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Debounce**: Essential. Without waiting for release, one press reads as 50 presses.

### 1️⃣2️⃣ Try This Next
*   **Rhythm**: Require Short-Short-Long.

---

## 1️⃣ Project 0067: Doorbell Alarm System (Prop Alarm)
### 2️⃣ Learning Objective
State monitoring. Use a Reed Switch to detect an open door. If open > 10s, alarm.

### 3️⃣ Concepts Introduced
*   **Reed Switch**: Magnetic sensor.
*   **Time-Delayed Trigger**: Action after X seconds of condition.

### 4️⃣ Hardware Required
*   **Pico**
*   **Reed Switch (+ Magnet)**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Reed Switch** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Wait Until**

### 7️⃣ Variables & State
*   **startTime**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Door Closed (Reed==1): `startTime` = Now.
    *   IF Door Open (Reed==0):
        *   IF (Now - `startTime`) > 10s: Beep.

### 9️⃣ Execution Flow (Plain English)
The system is happy as long as the door is closed. If it opens, a transparent timer starts. If the door closes, timer resets. If timer hits 10s, it complains.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
reed = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP) # Reeds usually connect to GND
buzz = machine.Pin(15, machine.Pin.OUT)
open_start = 0
is_open = False
while True:
    # Logic: Pin Low usually means Magnet Present (Closed), depending on wiring.
    # Let's assume PULL_UP, connect to GND. Low = Closed. High = Open.
    if reed.value() == 1: # Open
        if not is_open:
            open_start = time.ticks_ms()
            is_open = True
        elif time.ticks_diff(time.ticks_ms(), open_start) > 10000:
            buzz.value(1); time.sleep(0.1); buzz.value(0); time.sleep(0.1)
    else: # Closed
        is_open = False
        buzz.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Magnet Orientation**: Reed switches are directional. Test your magnet.

### 1️⃣2️⃣ Try This Next
*   **Chime**: Beep once immediately on open (Entry Chime), then Alarm after 60s.

---

## 1️⃣ Project 0068: The Doorbell Game (Trick or Treat)
### 2️⃣ Learning Objective
Randomization. Pressing the button gives a random sound result.

### 3️⃣ Concepts Introduced
*   **Random Choice**: Selecting 1 of N options.
*   **Gamification**: Making inputs fun.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Random Integer**

### 7️⃣ Variables & State
*   **outcome**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   `outcome` = Random(1, 2).
        *   IF 1: Play "Yay" (High rise).
        *   IF 2: Play "Boo" (Low fall).

### 9️⃣ Execution Flow (Plain English)
Digital Russian Roulette. You press the doorbell. 50% chance of a nice ring, 50% chance of a fart noise.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.PWM(machine.Pin(15))
def play(f, d):
    buzz.freq(int(f)); buzz.duty_u16(32768); time.sleep(d); buzz.duty_u16(0)
while True:
    if btn.value():
        outcome = random.randint(1, 2)
        if outcome == 1:
            # Treat
            play(800, 0.1); play(1000, 0.2)
        else:
            # Trick
            play(200, 0.5)
        time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Seed**: MicroPython seeds random on boot, but sometimes it repeats patterns.

### 1️⃣2️⃣ Try This Next
*   **Lights**: Add Red (Trick) and Green (Treat) LEDs.

---

## 1️⃣ Project 0069: Automated Doorbell (Presence)
### 2️⃣ Learning Objective
Touchless entry. Use Ultrasonic sensor to detect a visitor.

### 3️⃣ Concepts Introduced
*   **Proximity**: Distance < X.
*   **Dwell**: Person must stay for Y seconds (avoids triggers by passing cats).

### 4️⃣ Hardware Required
*   **Pico**
*   **HC-SR04**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Trig** | GP16 |
| **Echo** | GP17 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Distance**

### 7️⃣ Variables & State
*   **dist**

### 8️⃣ Block Logic
*   **Loop**:
    *   `dist` = Read Distance.
    *   IF `dist` < 50cm:
        *   Wait 2s.
        *   Check `dist` again.
        *   IF `dist` < 50cm: Ring Bell.

### 9️⃣ Execution Flow (Plain English)
If someone stands close (within 50cm) and stays there for 2 seconds, the doorbell rings itself.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
trig = machine.Pin(16, machine.Pin.OUT)
echo = machine.Pin(17, machine.Pin.IN)
buzz = machine.Pin(15, machine.Pin.OUT)
def get_dist():
    trig.low(); time.sleep_us(2)
    trig.high(); time.sleep_us(10); trig.low()
    while echo.value() == 0: pass
    start = time.ticks_us()
    while echo.value() == 1: pass
    return (time.ticks_diff(time.ticks_us(), start)) * 0.0343 / 2
while True:
    if get_dist() < 50:
        time.sleep(2) # Verify presence
        if get_dist() < 50:
            buzz.value(1); time.sleep(0.5); buzz.value(0)
            time.sleep(5) # Cooldown
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Reflections**: Soft clothes absorb sound. Ultrasonic sensors struggle with sweaters.

### 1️⃣2️⃣ Try This Next
*   **Range**: Adjust threshold to 100cm.

---

## 1️⃣ Project 0070: Mastering Doorbell (Wireless Sim)
### 2️⃣ Learning Objective
Simulation of a wireless system. Separate Input (Button) and Output (LED) logic entirely to mimic a transmitter/receiver.

### 3️⃣ Concepts Introduced
*   **Decoupling**: The button doesn't turn on the LED; it sends a "message" (variable). The LED watches the "message".

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Tx)
*   **LED** (Rx)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Variable**

### 7️⃣ Variables & State
*   **signal_active**

### 8️⃣ Block Logic
*   **Loop**:
    *   **Tx Logic**: IF Button -> `signal_active` = True. ELSE False.
    *   **Rx Logic**: IF `signal_active` -> LED ON. ELSE OFF.

### 9️⃣ Execution Flow (Plain English)
Conceptually, we break the wire. The button updates a cloud variable. The LED reads the cloud variable. In this single-pico sim, the variable is just in RAM.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
signal_active = False
while True:
    # Tx Code
    if btn.value():
        signal_active = True
    else:
        signal_active = False
        
    # Rx Code (Could be on another Pico)
    if signal_active:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Pointless?**: On one board, this looks redundant. But it prepares you for MQTT/WiFi logic where Tx and Rx are miles apart.

### 1️⃣2️⃣ Try This Next
*   **Latency**: Add a random 0.5s delay to simulate bad WiFi.

---
