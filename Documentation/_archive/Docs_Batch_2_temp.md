
# 🏁 Batch 2: Button Logic 1

## 1️⃣ Project 0011: Introduction to Button Logic
### 2️⃣ Learning Objective
Learn to read a digital input signal. You will program the Pico to listen for a button press and acknowledge it by printing a message to the computer screen, introducing the concept of Input vs Output.

### 3️⃣ Concepts Introduced
*   **Digital Input**: Measuring if voltage is High (3.3V) or Low (0V).
*   **Polling**: Constantly checking a pin state in a loop.
*   **Edge Detection**: (Simplified) detecting the "Pressed" state.
*   **Console Output**: Using `print()` to debug.

### 4️⃣ Hardware Required
*   **Pico**
*   **Pushbutton**
*   **Micro-USB Cable**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Leg A** | GP14 | Control Pin |
| **Button Leg B** | 3.3V | Power (Active High) |

### 6️⃣ Blocks Used
🔹 **If**
*   **Category:** Logic
*   **Block:** `if [Read Pin 14] then`

🔹 **Print**
*   **Category:** Text/Console
*   **Block:** `print [Click!]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   Set GP14 as Input with PULL_DOWN.
*   **B. Main Loop Phase**
    *   **Check**: "Is Button 14 Pressed?"
    *   **Action**: If Yes -> Print "Click!"
    *   **Wait**: Sleep 0.2s (Basic debounce/spam prevention).
*   **C. Event / Condition Handling**
    *   None.

### 9️⃣ Execution Flow (Plain English)
The Pico sits in a loop. Millions of times a second (slowed down by our wait block), it asks "Is pin 14 seeing 3.3 Volts?". If you press the button, the answer becomes Yes. The Pico then sends the text "Click!" up the USB cable to your screen.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        print("Click!")
        time.sleep(0.2) # Don't flood the console
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Spamming**: If you see "Click! Click! Click!" continuously when NOT pressing, your button might be wired to 3.3V permanently, or you forgot the Pull-Down resistor setting.
*   **No Text**: Make sure your "Serial Console" or "Repl" window is open.

### 1️⃣2️⃣ Try This Next
*   **Counter**: Create a variable `count`. Increment it every click. Print "Click #1", "Click #2".
*   **Release**: Print "Pressed" when down, and "Released" when you let go.

---

## 1️⃣ Project 0012: Blinking Button Logic
### 2️⃣ Learning Objective
Combine inputs and outputs to change system behavior. You will create a device that changes its blink speed based on user input, learning how conditional logic controls timing.

### 3️⃣ Concepts Introduced
*   **Variable Timing**: Changing the `sleep` duration dynamically.
*   **State-Dependent Behavior**: The system acts differently depending on valid inputs.

### 4️⃣ Hardware Required
*   **Pico**
*   **Pushbutton**
*   **Red LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic
*   **Block:** `if [Button] then... else...`

🔹 **Wait**
*   **Category:** Timing
*   **Block:** `sleep [X] seconds`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   Set LED Output, Button Input.
*   **B. Main Loop Phase**
    *   **Flash**: Turn LED ON.
    *   **Check**: IF Button is Pressed:
        *   Wait 0.1s (Fast Blink).
    *   **Else**:
        *   Wait 1.0s (Slow Blink).
    *   **Flash End**: Turn LED OFF.
    *   **Check Again**: (Same Logic for Off-Time or simplified). Wait X seconds.
*   **C. Event / Condition Handling**
    *   Polling inside the loop.

### 9️⃣ Execution Flow (Plain English)
The program turns the light on. It then asks "Is the button pressed?". If yes, it waits only a tiny moment (0.1s). If no, it waits a long moment (1.0s). Then it turns the light off and repeats the wait logic. This makes the blink "speed up" instantly when you hold the button.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    led.value(1)
    if btn.value():
        time.sleep(0.1)
    else:
        time.sleep(1.0)
        
    led.value(0)
    if btn.value():
        time.sleep(0.1)
    else:
        time.sleep(1.0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Laggy Response**: Because we wait *inside* the loop, if you press the button during the 1-second "Slow Wait", it won't speed up until that 1 second finishes. This is "Blocking Code".
*   **Sync**: Ensure you change both the ON and OFF times, otherwise it just blips weirdly.

### 1️⃣2️⃣ Try This Next
*   **Hyper Speed**: Make the fast blink 0.01s (almost solid on).
*   **Reverse**: Slow blink when pressed, Fast blink when released.

---

## 1️⃣ Project 0013: Manual Button Logic Control (Dead Man's Switch)
### 2️⃣ Learning Objective
Implement safety logic. You will build a system that requires constant human presence (holding a button) to remain "Safe", triggering an "Alarm" if released, mimicking train or machinery safety switches.

### 3️⃣ Concepts Introduced
*   **Fail-Safe**: Designing system defaults to be safe (or alarm) on failure.
*   **Inverted Logic**: Active = OK, Inactive = Danger.
*   **Timers**: Resetting a countdown.

### 4️⃣ Hardware Required
*   **Pico**
*   **Pushbutton**
*   **Green LED** (Safe)
*   **Red LED** (Alarm)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **Green LED** | GP15 |
| **Red LED** | GP16 |

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic
*   **Block:** `if [Button] then [Safe] else [Alarm]`

### 7️⃣ Variables & State
*   **releaseTime**: (Advanced) Timer tracking.

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   Setup Pins.
*   **B. Main Loop Phase**
    *   **Check**: IF Button Pressed:
        *   Green ON, Red OFF.
    *   **Else** (Button Released):
        *   Wait 1 Second (Grace Period).
        *   **Check Again**: IF Still Released:
            *   Green OFF, Red ON.
*   **C. Event / Condition Handling**
    *   None.

### 9️⃣ Execution Flow (Plain English)
As long as you hold the button, the Green light shines. If you let go, a hidden timer starts. If you don't press it again within 1 second, the Green light dies and the Red Alarm light flares up.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
green = machine.Pin(15, machine.Pin.OUT)
red = machine.Pin(16, machine.Pin.OUT)

while True:
    if btn.value():
        green.value(1)
        red.value(0)
    else:
        # Grace period
        time.sleep(1)
        if not btn.value(): # Check again
            green.value(0)
            red.value(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Instant Alarm**: Dealing with the logic to add the "1 Second Delay" can be tricky. Beginners often make it alarm immediately upon release.
*   **Flicker**: Ensure the Red light doesn't blip off every loop cycle.

### 1️⃣2️⃣ Try This Next
*   **Reset**: Make it require a separate "Reset Button" to turn off the Red Alarm once triggered.
*   **Buzzer**: Add sound to the Red Alarm.

---

## 1️⃣ Project 0014: Button Logic Sequences (Secret Code)
### 2️⃣ Learning Objective
Detect a sequence of specific events. You will create a combination lock that requires "A then B then A" to unlock, introducing the concept of State Machines (tracking progress).

### 3️⃣ Concepts Introduced
*   **State Tracking**: "I have seen the first button, waiting for second."
*   **Sequence Validation**: Checking order.
*   **Reset on Error**: If wrong button, start over.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**
*   **Green LED** (Unlock), **Red LED** (Error)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |
| **Green LED** | GP15 |
| **Red LED** | GP14 |

### 6️⃣ Blocks Used
🔹 **Variable**
*   **Category:** Variables
*   **Block:** `set [stage] to [0]`

🔹 **Wait Until**
*   **Category:** Control
*   **Block:** `wait until [Button Pressed]`

### 7️⃣ Variables & State
*   **stage**: Integer. 0=Start, 1=A pressed, 2=B pressed, 3=Unlock.

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   `stage` = 0.
*   **B. Main Loop Phase**
    *   **Wait for Input**: Wait for A or B press.
    *   **Logic**:
        *   If `stage` == 0 AND Input == A: `stage` = 1.
        *   Else If `stage` == 1 AND Input == B: `stage` = 2.
        *   Else If `stage` == 2 AND Input == A: `stage` = 3 (Unlock!).
        *   Else: Flash Red (Error), `stage` = 0.
    *   **Output**: If `stage` == 3, Green ON. Else Green OFF.
*   **C. Event / Condition Handling**
    *   Debouncing highly recommended here.

### 9️⃣ Execution Flow (Plain English)
The Pico acts like a safecracker. It starts at Stage 0. If you give it the right first number (A), it advances to Stage 1. If you give it the wrong number at any point, it gets angry (Red Flash) and resets to Stage 0. Only reaching Stage 3 opens the lock.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
green = machine.Pin(15, machine.Pin.OUT)
red = machine.Pin(14, machine.Pin.OUT)

stage = 0

while True:
    if stage == 3:
        green.value(1) # Unlocked
        continue       # Stay unlocked

    if btnA.value():
        if stage == 0: stage = 1
        elif stage == 2: stage = 3 # Win
        else: 
            stage = 0
            red.value(1); time.sleep(0.5); red.value(0)
        time.sleep(0.3) # Debounce
        
    if btnB.value():
        if stage == 1: stage = 2
        else: 
            stage = 0
            red.value(1); time.sleep(0.5); red.value(0)
        time.sleep(0.3) # Debounce
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Bouncing**: One press might be read as two interactions, skipping a stage. `time.sleep(0.3)` is crucial after every press.
*   **Reset**: Forget to reset `stage` to 0 on error? The lock becomes impossible to open.

### 1️⃣2️⃣ Try This Next
*   **Long Code**: Require 5 presses.
*   **Timeout**: If user waits > 5 seconds between presses, reset to 0.

---

## 1️⃣ Project 0015: Interactive Button Logic (Voting Machine)
### 2️⃣ Learning Objective
Count and store events. You will build a tally counter that tracks two separate values ("Cats" vs "Dogs") and reports the score, demonstrating variable incrementing.

### 3️⃣ Concepts Introduced
*   **Incrementing**: `x = x + 1`.
*   **Data Storage**: Variables hold values in RAM.
*   **String Formatting**: Combining text and numbers for output.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A (Cats), Button B (Dogs)**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |

### 6️⃣ Blocks Used
🔹 **Change Variable**
*   **Category:** Variables
*   **Block:** `change [cats] by 1`

🔹 **Create Text with**
*   **Category:** Text
*   **Block:** `create text "Cats:" + [cats]`

### 7️⃣ Variables & State
*   **cats**: Integer.
*   **dogs**: Integer.

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   `cats` = 0, `dogs` = 0.
*   **B. Main Loop Phase**
    *   IF Button A Pressed: Increment `cats`, Print Score, Wait 0.2s.
    *   IF Button B Pressed: Increment `dogs`, Print Score, Wait 0.2s.
*   **C. Event / Condition Handling**
    *   Debounce waits.

### 9️⃣ Execution Flow (Plain English)
The system sits idle. When you vote for Cats (Button A), it adds one to the Cat pile and announces the new score. Same for Dogs. The scores persist as long as power is on.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
cats = 0
dogs = 0

while True:
    if btnA.value():
        cats += 1
        print(f"Cats: {cats}, Dogs: {dogs}")
        time.sleep(0.3)
        
    if btnB.value():
        dogs += 1
        print(f"Cats: {cats}, Dogs: {dogs}")
        time.sleep(0.3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Double Counting**: If you press and score jumps by 2 or 3, increase the debounce delay (`time.sleep`).
*   **Lost Data**: Remember, if you unplug the Pico, the votes are lost (RAM is volatile).

### 1️⃣2️⃣ Try This Next
*   **Reset**: Add Button C to clear votes to 0-0.
*   **Winner**: If Cats > 10, print "Cats Win!" and end game.

---

## 1️⃣ Project 0016: Smart Button Logic Switch (3-Way)
### 2️⃣ Learning Objective
Implement a multi-state cycle controlled by a single input. You will change brightness levels with each click (Off -> Low -> High -> Off), learning typical efficient UI logic.

### 3️⃣ Concepts Introduced
*   **Modulo Operator**: (Optional/Advanced) logic to wrap `0,1,2 -> 0`.
*   **PWM (Pulse Width Modulation)**: Changing brightness.
*   **State Cycling**: Moving sequentially through a list of states.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **LED** (On PWM pin)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Set Analog/PWM**
*   **Category:** Pin Access
*   **Block:** `analog write Pin [15] value [X]`

### 7️⃣ Variables & State
*   **mode**: Integer (0, 1, 2).

### 8️⃣ Block Logic
*   **A. Initialization Phase**
    *   `mode` = 0.
*   **B. Main Loop Phase**
    *   **Input**: If Button Pressed (Debounced):
        *   Increment `mode`.
        *   If `mode` > 2, set `mode` = 0.
    *   **Output**:
        *   If `mode` == 0: Brightness = 0.
        *   If `mode` == 1: Brightness = 10000 (Low).
        *   If `mode` == 2: Brightness = 65000 (High).
*   **C. Event / Condition Handling**
    *   Detect click, not hold.

### 9️⃣ Execution Flow (Plain English)
Every time you click, the internal `mode` counter goes up by one. When it hits the limit, it wraps back to zero. The LED output continuously updates to match the current mode, giving the user control over brightness.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.PWM(machine.Pin(15))
led.freq(1000)
mode = 0

while True:
    if btn.value():
        mode += 1
        if mode > 2: mode = 0
        
        # Apply State
        if mode == 0: led.duty_u16(0)
        if mode == 1: led.duty_u16(10000)
        if mode == 2: led.duty_u16(65535)
        
        time.sleep(0.3) # Debounce
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **PWM Error**: Ensure the block you choose supports PWM (Analog Write). Standard "Set Pin High" cannot do 50% brightness.
*   **Mode confusion**: If it jumps randomly, likely debounce issues.

### 1️⃣2️⃣ Try This Next
*   **More Steps**: Off -> Low -> Med -> High -> Off.
*   **Smooth Fade**: Instead of jumping brightness, fade between the levels.

---

## 1️⃣ Project 0017: Button Logic Alarm System (Panic Button)
### 2️⃣ Learning Objective
Differentiate between a "Short Press" and a "Long Press". You will trigger an alarm only if the user **holds** the button for 3 seconds, a common pattern to prevents accidental triggers.

### 3️⃣ Concepts Introduced
*   **Time Measurement**: Recording `start_time` and `current_time`.
*   **Duration Logic**: `Duration = Current - Start`.
*   **Latching Alarm**: Once triggered, it stays on.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Red LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Timer / Time**
*   **Category:** Timing
*   **Block:** `get time (ms)`

### 7️⃣ Variables & State
*   **pressStartTime**: Stores when the button was first touched.
*   **alarmActive**: Boolean.

### 8️⃣ Block Logic
*   **A. Initialization**
    *   `alarmActive` = False.
*   **B. Main Loop**
    *   IF `alarmActive` is True:
        *   Blink Red LED (FOREVER Loop).
    *   IF Button Pressed:
        *   Wait 3 Seconds.
        *   IF Button STILL Pressed (Simple version):
            *   `alarmActive` = True.
*   **C. Events**
    *   (Advanced version uses actual timer math, simpler version just waits and checks again).

### 9️⃣ Execution Flow (Plain English)
To avoid false alarms (bumping the button), the system waits. If you press the button, it starts counting "1... 2... 3...". If you let go early, nothing happens. If you are still holding it at '3', it assumes an emergency and locks into Alarm Mode.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    if btn.value():
        # User pressed, verify duration
        start = time.ticks_ms()
        # Wait while holding..
        while btn.value():
             if time.ticks_diff(time.ticks_ms(), start) > 3000:
                 # 3s passed! ALARM!
                 while True: # Locked loop
                     led.value(1); time.sleep(0.1)
                     led.value(0); time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Sleeping**: If you use `time.sleep(3)` to check duration, the code freezes for 3s. The user can't do anything else. The `time.ticks_ms()` approach (non-blocking style) is better but harder for beginners. The simple sleep check is acceptable here.
*   **Reset**: You must unplug or hit RUN button to reset the alarm loop.

### 1️⃣2️⃣ Try This Next
*   **Warning**: Blink Yellow during the 3-second hold to warn the user "Alarm Imminent".
*   ** Silent**: Instead of LED, send a secret message over USB.

---

## 1️⃣ Project 0018: The Button Logic Game (Fastest Finger)
### 2️⃣ Learning Objective
Arbitrate between two competing inputs. You will build a system that determines which of two buttons was pressed first, locking out the loser.

### 3️⃣ Concepts Introduced
*   **Race Conditions**: Who got there first?
*   **Lockout**: Ignoring inputs after a state change.
*   **Fairness**: Polling inputs effectively.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**
*   **LED A, LED B**
*   **Start LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |
| **LED A** | GP14 |
| **LED B** | GP15 |
| **Start LED** | GP25 |

### 6️⃣ Blocks Used
🔹 **Break Loop**
*   **Category:** Loops
*   **Block:** `break` (Exit loop)

### 7️⃣ Variables & State
*   None needed if using code flow.

### 8️⃣ Block Logic
*   **A. Init**: All LEDs Off.
*   **B. Game**:
    *   Wait Random time.
    *   Turn Start LED ON.
    *   **Race Loop**:
        *   IF A Pressed: Turn A LED ON. Break Loop.
        *   IF B Pressed: Turn B LED ON. Break Loop.
    *   **End**: Wait 5s (Celebration), Reset.

### 9️⃣ Execution Flow (Plain English)
The system creates tension with a random delay. As soon as the Start Light fires, it enters a hyper-fast loop checking A then B. The moment it finds one pressed, it lights that player's victory lamp and *stops checking*, effectively ignoring the slower player.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
ledA = machine.Pin(14, machine.Pin.OUT)
ledB = machine.Pin(15, machine.Pin.OUT)
start = machine.Pin(25, machine.Pin.OUT)

while True:
    ledA.value(0); ledB.value(0); start.value(0)
    time.sleep(random.uniform(2,5))
    start.value(1)
    
    while True:
        if btnA.value():
            ledA.value(1)
            break
        if btnB.value():
            ledB.value(1)
            break
    
    time.sleep(4) # Show winner
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Bias**: If Player A is checked first in the loop, they have a *theoretical* advantage of a few microseconds. In Python on Pico, this is negligible (microseconds), but in high-speed hardware, it matters.
*   **Cheating**: Holding the button down before the light triggers guarantees a win. You need "False Start" logic to fix this (See Try Next).

### 1️⃣2️⃣ Try This Next
*   **Disqualify**: If button pressed *while* Start LED is off -> Loser.
*   **Scoreboard**: Keep tally of wins.

---

## 1️⃣ Project 0019: Automated Button Logic (Staircase Timer)
### 2️⃣ Learning Objective
Create a re-triggerable timer. You will build a light suitable for a staircase or hallway that stays on for a set time, but extends that time if the button is pressed again, ensuring no one is left in the dark.

### 3️⃣ Concepts Introduced
*   **Re-triggering**: Resetting a countdown to its maximum value.
*   **Countdown Loop**: Decrementing a timer.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **White LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Change Variable**
*   **Category:** Variables
*   **Block:** `change [timer] by -1`

### 7️⃣ Variables & State
*   **timeLeft**: Seconds remaining.

### 8️⃣ Block Logic
*   **A. Init**: `timeLeft` = 0.
*   **B. Loop**:
    *   IF Button Pressed: Set `timeLeft` = 10.
    *   IF `timeLeft` > 0:
        *   LED ON.
        *   Wait 1s.
        *   Change `timeLeft` by -1.
    *   ELSE:
        *   LED OFF.

### 9️⃣ Execution Flow (Plain English)
Imagine a bucket of water with a hole (the timer leaking away). Every time you press the button, you refill the bucket to the top (10s). The light stays on as long as there is water. This ensures continuous light for continuous activity.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
timeLeft = 0

while True:
    if btn.value():
        timeLeft = 10 # Refill
        
    if timeLeft > 0:
        led.value(1)
        timeLeft -= 0.1 # Decrement (using small steps for responsiveness)
        time.sleep(0.1)
    else:
        led.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Unresponsive**: If you use `time.sleep(1)` inside the decrement loop, the button check only happens once a second. You have to hold the button for a full second to trigger it. Fast loops (0.1s) make the button feel responsive.

### 1️⃣2️⃣ Try This Next
*   **Warning Dim**: PWM fade out the light during the last 2 seconds.
*   **Longer**: 60 seconds (Real world use).

---

## 1️⃣ Project 0020: Mastering Button Logic (Software Debounce)
### 2️⃣ Learning Objective
Solve a physical hardware imperfection with software. Real switches have springy contacts that "bounce" (connect/disconnect rapidly) when pressed. You will write code to filter this noise for a clean signal.

### 3️⃣ Concepts Introduced
*   **Signal Noise**: Inspecting raw input.
*   **Filtering**: Filtering out high-frequency changes.
*   **Reliability**: Making robust systems.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |

### 6️⃣ Blocks Used
🔹 **Wait**
*   **Category:** Timing
*   **Block:** `sleep [0.05] s`

### 7️⃣ Variables & State
*   **count**: To prove the button is bouncing (or fixed).

### 8️⃣ Block Logic
*   **A. Init**: `count` = 0.
*   **B. Loop**:
    *   IF Button Pressed:
        *   Wait 0.05s (Let the bouncing settle).
        *   IF Button STILL Pressed (It wasn't just noise):
            *   Increment Count.
            *   Print Count.
            *   Wait until Released.
*   **C. Events**: None.

### 9️⃣ Execution Flow (Plain English)
When the Pico sees a signal, it doesn't trust it immediately. It waits 50 milliseconds (a long time for a spark, short for a human). If the signal is still there, it accepts it as a genuine press.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

while True:
    if btn.value():
        time.sleep(0.05) # Debounce Wait
        if btn.value():  # Verify
            count += 1
            print(f"Click {count}")
            while btn.value(): # Wait for release
                time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Too Long**: If debounce > 0.1s, the button feels "sluggish".
*   **Too Short**: If < 0.01s, it may still bounce. 20-50ms is the sweet spot.

### 1️⃣2️⃣ Try This Next
*   **Hardware Fix**: Add a 1uF capacitor across the button to fix it physically. Compare results.

---
