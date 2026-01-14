import os

def build_batch59():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0581 = """
---

# Batch 59: Kitchen Timer 3

## 1. Project 0581: Introduction to Kitchen Timer

### 2. Learning Objective
Manipulate string output in the terminal to visualize the passage of time using symbols and automated line breaks.

### 3. Concepts Introduced
*   Console Formatting
*   Modulo for Layout (`% 10`)
*   String Concatenation
*   Temporal Sequencing

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Console** | USB | Serial Monitoring |

### 6. Blocks Used
*   **from Time, drag `pico_wait`** (Set to 1s)
*   **from Text, drag `print`**
*   **from Math, drag `modulo`**

### 7. Variables
*   **ticks**: Integer (Counter)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init Header**: Print "Timer Started". `ticks = 0`.

**B. Main Loop Phase**
2.  **Tick**:
    *   Increment `ticks` by 1.
3.  **Visual Update**:
    *   If `ticks` % 10 == 0:
        *   Print " (10s Mark)". (Automated newline).
    *   Else:
        *   Print "." (no newline).
4.  **Wait**:
    *   Wait 1 second.

### 9. Execution Flow
1.  **Start**: The system begins counting.
2.  **Process**: Every second, the Pico sends a single dot to the screen.
3.  **Condition**: The mathematical modulo (`%`) detects when 10 seconds have passed.
4.  **Formatting**: At the 10-second mark, the code forces a text label and a newline, making the long stream of dots easy to read.

### 10. Generated Code
```python
import time

count = 0
while True:
    count += 1
    if count % 10 == 0:
        print(" [10s]")
    else:
        # End='' prevents automatic newline
        print(".", end="")
    
    time.sleep(1)
```

### 11. Common Mistakes
*   **Implicit Newlines**: Most `print()` calls automatically move to the next line. Use the `end=""` parameter to keep dots on the same line.

### 12. Try This Next
*   **Minute Marker**: Change the logic to print "--- MINUTE ---" every 60 seconds.
"""

    p0582 = """
---

## 1. Project 0582: Blinking Kitchen Timer

### 2. Learning Objective
Create a visual "Urgency Sensor" that intelligently changes its notification frequency as a countdown timer approaches zero.

### 3. Concepts Introduced
*   State-Dependent Signaling
*   Frequency Scaling
*   Dynamic Thresholds
*   Visual Feedback Systems

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alert LED** | GP16 | Visual Warning |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`**
*   **from Time, drag `pico_wait`** (Dynamic variable)

### 7. Variables
*   **timer_val**: Integer (Seconds remaining)
*   **blink_speed**: Float (Delay)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16 as Output. `timer_val = 600` (10 minutes).

**B. Main Loop Phase**
2.  **Determine Urgency**:
    *   **If `timer_val` > 60**: Set `blink_speed` to 1.0 (Slow).
    *   **Else If `timer_val` > 0**: Set `blink_speed` to 0.1 (Fast).
    *   **Else (Time's Up)**: Set LED HIGH (Solid).
3.  **Execute Blink**:
    *   Turn LED ON, Wait `blink_speed`, Turn LED OFF, Wait `blink_speed`.
4.  **Decrement**:
    *   Subtract `blink_speed * 2` from the `timer_val`.

### 9. Execution Flow
1.  **Safety**: For the first 9 minutes, the LED pulses calmly once per second.
2.  **Alert**: When the timer enters the "Final Minute", the LED instantly switches to a rapid strobe.
3.  **Finish**: When the count hits zero, the LED stays on permanently like a signal flare.
4.  **Result**: The user can understand the priority of the timer just by looking at the lights.

### 10. Generated Code
```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
timer_s = 70 # Demo with 70 seconds

while timer_s >= 0:
    if timer_s > 60:
        # Slow
        led.on(); time.sleep(0.5); led.off(); time.sleep(0.5)
        timer_s -= 1
    elif timer_s > 0:
        # Fast
        led.on(); time.sleep(0.1); led.off(); time.sleep(0.1)
        timer_s -= 0.2
    else:
        # Time Up
        led.on()
        print("DING!")
        break
```

### 11. Common Mistakes
*   **Blocking Logic**: If you use `time.sleep(1)` for the blink, and then `timer -= 1`, the loop actually takes more than 1 second to run because of the extra logic.

### 12. Try This Next
*   **Buzzer escalate**: Beep only in the final 10 seconds.
"""

    p0583 = """
---

## 1. Project 0583: Manual Kitchen Timer Control

### 2. Learning Objective
Build a "Dial-and-Set" kitchen timer using a potentiometer to select a duration (0-60 minutes) and a button to begin the countdown.

### 3. Concepts Introduced
*   Analog Parameter Mapping
*   User UI (OLED Preview)
*   Lock-in State
*   Unit Scaling (Minutes/Seconds)

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer, Button, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Duration Knob**| GP26 (ADC) | Set minutes |
| **Start Button** | GP14 | Lock and Start |
| **OLED** | GP8/9 | Display |

### 6. Blocks Used
*   **from Display, drag `pico_oled_text`**
*   **from Math, drag `map_range`** (0-60m)
*   **from Loops, drag `repeat_until`**

### 7. Variables
*   **target_m**: Integer (Selected minutes)
*   **running**: Boolean

### 8. Step-by-Step Guide

**A. Selection Phase**
1.  **Preview Display**:
    *   Loop while `running` is FALSE:
        *   Map Pot value to 1-60.
        *   Show "SET: [val] MINS" on OLED.
        *   If Button GP14 pressed: `running = TRUE`.

**B. Countdown Phase**
2.  **Timer Loop**:
    *   Convert `target_m` to `seconds`.
    *   While `seconds` > 0:
        *   Show remaining time on OLED.
        *   Wait 1s.
        *   Subtract 1 from `seconds`.

**C. Finish Phase**
3.  **Alarm**: Show "DONE!" and Reset.

### 9. Execution Flow
1.  **Interact**: The user turns the dial. The OLED updates live with the intended duration.
2.  **Commit**: The user presses the button. The "Set" mode ends, and the "Run" mode begins.
3.  **Logic**: The Pico calculates the total seconds and counts down accurately.
4.  **Observer**: The knob no longer affects the time once the countdown has started (Lock-in).

### 10. Generated Code
```python
import machine, ssd1306, time

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pot = machine.ADC(26); btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# 1. SETTING
while not btn.value():
    m = int(pot.read_u16() * 60 / 65535) + 1
    oled.fill(0); oled.text(f"SET: {m} MINS", 20, 30); oled.show()
    time.sleep(0.1)

# 2. RUNNING
s = m * 60
while s > 0:
    oled.fill(0)
    oled.text(f"REMAINING: {s//60}m {s%60}s", 5, 30)
    oled.show()
    time.sleep(1)
    s -= 1

oled.fill(0); oled.text("DINNER READY!", 10, 30); oled.show()
```

### 11. Common Mistakes
*   **Scaling**: Forgetting that 1 minute = 60 seconds. Running a timer for "60 ticks" only lasts one minute!
*   **OLED Burn-in**: Displaying a static number for 60 minutes can damage OLEDs over years; consider turning the screen off between minutes.

### 12. Try This Next
*   **Cancel**: Use a long-press of the button to cancel the timer and return to setting mode.
"""

    p0584 = """
---

## 1. Project 0584: Kitchen Timer Sequences

### 2. Learning Objective
Programm a "Pomodoro Productivity Timer" that automatically sequences between Work periods (25m) and Break periods (5m).

### 3. Concepts Introduced
*   Multi-stage Sequences
*   Cyclic Automation
*   Workflow Management
*   Indicator Colors

### 4. Hardware Required
*   Raspberry Pi Pico
*   Green LED (Work)
*   Blue LED (Break)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Work LED** | GP16 | Green |
| **Break LED** | GP17 | Blue |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Loop 4 times)
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **sessions**: Integer (Session count)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO**: Setup GP16/17 for LEDs.

**B. Sequence Loop**
2.  **Phase 1 (Work)**:
    *   Turn GREEN ON, BLUE OFF.
    *   Print "Focus Time (25m)...".
    *   Wait 1500 seconds. (Demo: 10s).
3.  **Phase 2 (Break)**:
    *   Beep buzzer.
    *   Turn GREEN OFF, BLUE ON.
    *   Print "Rest Time (5m)...".
    *   Wait 300 seconds. (Demo: 5s).
4.  **Repeat**: Sequence repeats 4 times.

### 9. Execution Flow
1.  **Automation**: The Pico manages the user's schedule.
2.  **Focus**: The Green LED signals that it is time to work.
3.  **Rest**: The shift to Blue provides a clear visual prompt to stand up and stretch.
4.  **Efficiency**: By automating these transitions, the user doesn't need to manually reset the timer for every break.

### 10. Generated Code
```python
import machine, time

green = machine.Pin(16, machine.Pin.OUT)
blue = machine.Pin(17, machine.Pin.OUT)

for session in range(4):
    print(f"SESSION {session+1}: WORK")
    green.on(); blue.off()
    time.sleep(10) # 10s for demo (Real: 1500)
    
    print("SESSION BREAK")
    green.off(); blue.on()
    time.sleep(5) # 5s for demo (Real: 300)

green.off(); blue.off()
print("FULL FOCUS CYCLE COMPLETE.")
```

### 11. Common Mistakes
*   **Loop Length**: 25 minutes is a long time for a test. Use short times (seconds) when testing the logic, then swap back to minutes once verified.

### 12. Try This Next
*   **Long Break**: After 4 sessions, add a "Phase 3" that gives a 15-minute long break.
"""

    p0585 = """
---

## 1. Project 0585: Interactive Kitchen Timer

### 2. Learning Objective
Implement a "Preset Menu" where a single button tap cycles through three specific timer settings corresponding to egg sizes.

### 3. Concepts Introduced
*   Parameter Presets
*   Selection Logic
*   Cycle Management
*   User-Friendly Presets

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Size Toggle** | GP14 | Switch Small/Med/Large |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `if_elseif`**
*   **from Display, drag `pico_oled_text`**

### 7. Variables
*   **egg_mode**: Integer (0, 1, 2)
*   **timer_val**: Integer (Seconds)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Selection**: `egg_mode = 0`.

**B. Configuration Phase**
2.  **Monitor Input**:
    *   If GP14 is HIGH: `egg_mode = (egg_mode + 1) % 3`.
3.  **Map Mode to Time**:
    *   If `egg_mode` == 0: "Small (3m)", `timer_val = 180`.
    *   If `egg_mode` == 1: "Med (4m)", `timer_val = 240`.
    *   If `egg_mode` == 2: "Large (5m)", `timer_val = 300`.
4.  **Show Selection**: Update OLED with mode name.

### 9. Execution Flow
1.  **Choice**: Instead of setting a raw number, the user interacts with familiar categories.
2.  **Logic**: The Pico translates words like "Large" into the specific mathematical quantity required (300 seconds).
3.  **Refinement**: Using a single button for selection keeps the interface minimal and effective.

### 10. Generated Code
```python
import machine, time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
mode = 0 # 0:S, 1:M, 2:L

while True:
    if btn.value():
        mode = (mode + 1) % 3
        time.sleep(0.3)
        
    if mode == 0: print("SMALL - 3 MINS")
    elif mode == 1: print("MEDIUM - 4 MINS")
    else: print("LARGE - 5 MINS")
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Debounce**: Touching the button once might skip two modes without a 0.3s delay.

### 12. Try This Next
*   **Start Timer**: Use a LONG PRESS of the same button to lock and start the countdown.
"""

    p0586 = """
---

## 1. Project 0586: Smart Kitchen Timer Switch

### 2. Learning Objective
Create a "Safety Lock" that inhibits input from control buttons, preventing children or accidental bumps from changing the timer settings.

### 3. Concepts Introduced
*   Input Inhibition (Gating)
*   Safety Interlocks
*   Logical AND (Condition grouping)
*   System Locking

### 4. Hardware Required
*   Raspberry Pi Pico
*   Toggle Switch (Lock)
*   Push Button (Setting)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Lock Switch** | GP14 | ON = LOCKED |
| **Set Button** | GP15 | Setting Input |

### 6. Blocks Used
*   **from Logic, drag `and_operation`**
*   **from Logic, drag `not`**
*   **from Smart IO, drag `pico_gpio_read`**

### 7. Variables
*   **is_locked**: Boolean
*   **count**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: GP14/15 as Inputs.

**B. Monitoring Phase**
2.  **Check Lock State**:
    *   Set `is_locked` to state of Switch (GP14).
3.  **Evaluate Input**:
    *   If Button (GP15) is HIGH:
        *   **If `is_locked` is FALSE**:
            *   Accept Button! (Increment timer).
        *   **Else (LOCKED)**:
            *   Do nothing. (Maybe Beep buzzer error).

### 9. Execution Flow
1.  **Operational**: With the switch OFF, hitting the button adds time.
2.  **Protected**: The user flips the physical switch to ON.
3.  **Test**: Hitting the setting button now fails because the "Gating" logic (the `IF NOT LOCKED` check) returns false.
4.  **Purpose**: Ensures stability in busy environments.

### 10. Generated Code
```python
from machine import Pin
import time

lock = Pin(14, Pin.IN, Pin.PULL_DOWN)
adj = Pin(15, Pin.IN, Pin.PULL_DOWN)

timer_s = 0

while True:
    if adj.value():
        # Only allow change if lock is NOT active
        if not lock.value():
            timer_s += 10
            print(f"Time Set: {timer_s}s")
        else:
            print("LOCKED - CANNOT ADJUST")
        
        time.sleep(0.3)
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Logic Swap**: Thinking the switch is active when it's grounded. If you use `PULL_UP`, the logic is usually inverted.

### 12. Try This Next
*   **OLED Icon**: Display a "Padlock" symbol on the screen when the switch is ON.
"""

    p0587 = """
---

## 1. Project 0587: Kitchen Timer Alarm System

### 2. Learning Objective
Programm a "Persistent Alert Escalation" system that increases alarm volume or frequency if a user fails to acknowledge a finished timer.

### 3. Concepts Introduced
*   Escalation Logic
*   Duration Monitoring (Post-completion)
*   Signaling Intensity
*   Persistent Reminders

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alarm Buzzer**| GP15 | Graduated Volume/Speed |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Smart IO, drag `pico_buzzer_beep`**
*   **from Time, drag `pico_milliseconds`**

### 7. Variables
*   **overtime**: Integer (Seconds since finish)

### 8. Step-by-Step Guide

**A. Trigger Phase**
1.  **Complete**: Timer reaches zero.
2.  **Mark End**: Set `end_tick = current_ms`.

**B. Alarm Phase**
3.  **Monitor Neglect**:
    *   While Button NOT pressed:
        *   `overtime = current_ms - end_tick`.
        *   **Stage 1 (Normal)**: If `overtime` < 10s: Beep once every 1s.
        *   **Stage 2 (Angry)**: If `overtime` > 10s: Beep 5 times fast every 1s.
4.  **Acknowledgment**:
    *   Stop beeping when button hit.

### 9. Execution Flow
1.  **Done**: The timer finishes. A polite beep sounds.
2.  **Neglect**: The user is in another room and doesn't hear.
3.  **Logic**: The Pico notes that 10 seconds have passed without an "Arrival".
4.  **Escalate**: The beep frequency increases significantly to ensure it is heard, preventing food from burning or tasks being missed.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Starting state: Timer finished
print("TIMER DONE")
start_fault = time.ticks_ms()

while not btn.value():
    elap = time.ticks_diff(time.ticks_ms(), start_fault)
    
    if elap < 10000: # First 10 seconds
        buz.on(); time.sleep(0.1); buz.off()
        time.sleep(1)
    else: # After 10 seconds - ESCALATE
        for _ in range(5):
            buz.on(); time.sleep(0.05); buz.off(); time.sleep(0.05)
        time.sleep(0.5)

print("ACKNOWLEDGED. ALARM OFF.")
```

### 11. Common Mistakes
*   **No Exit**: Forgetting to check the button *inside* the alarm loop. If the loop is separate, you'll never be able to stop the noise.

### 12. Try This Next
*   **Pitch Shift**: Use PWM to make the buzzer's tone higher (more painful) during escalation.
"""

    p0588 = """
---

## 1. Project 0588: The Kitchen Timer Game

### 2. Learning Objective
Create a "Bomb Defuser" survival game where the user must disconnect a specific jumper wire before the timer hits 0.

### 3. Concepts Introduced
*   Continuity Sensing
*   Multiple Parallel Checks
*   Logic Traps (Speed multipliers)
*   High-Stakes Timing

### 4. Hardware Required
*   Raspberry Pi Pico
*   3x Jumper Wires
*   Buzzer, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Defuse Wire** | GP14 to GND | The correct one |
| **Trap Wire 1** | GP15 to GND | Causes speed up |
| **Trap Wire 2** | GP16 to GND | Causes speed up |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (with Pull-Up)
*   **from Time, drag `pico_wait`**
*   **from Display, drag `pico_oled_text`**

### 7. Variables
*   **bomb_ticks**: Integer (Remaining time)
*   **speed**: Float (0.1 to 1.0)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure**: Set GP14-16 as Inputs with **PULL-UP**. (They are LOW when plugged into GND).
2.  **Reset**: `ticks = 100`, `speed = 1.0`.

**B. Game Loop Phase**
3.  **Check Wires**:
    *   If GP14 is HIGH (Unplugged): "DEFUSED!". Stop.
    *   If GP15 is HIGH (Trap): set `speed = 0.2`. (Runs 5x faster).
    *   If GP16 is HIGH (Trap): set `speed = 0.5`. (Runs 2x faster).
4.  **Ticker**:
    *   `ticks = ticks - 1`.
    *   Display `ticks` on OLED.
    *   Wait `speed` seconds.
5.  **Failure**:
    *   If `ticks` == 0: "BOOM!".

### 9. Execution Flow
1.  **Action**: The timer counts down on the OLED.
2.  **Detection**: The Pico monitors the "Continuity" (connection to ground).
3.  **Interaction**: User pulls a wire.
4.  **Judge**: If the correct wire is pulled, the loop breaks—game won. If a trap is pulled, the "Wait" duration decreases, making the numbers count down much faster!

### 10. Generated Code
```python
import machine, time

# Pull UP means value is 1 when DISCONNECTED
wires = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in [14, 15, 16]]
timer = 20
spd = 1.0

while timer > 0:
    # Check CORRECT wire (14)
    if wires[0].value() == 1:
        print("DEFUSED! SYSTEM SAFE.")
        break
    
    # Check TRAP wires (15, 16)
    if wires[1].value() == 1: spd = 0.2
    if wires[2].value() == 1: spd = 0.5
    
    print(f"BOMB: {timer}...")
    time.sleep(spd)
    timer -= 1

if timer == 0: print("--- BOOM ---")
```

### 11. Common Mistakes
*   **Not using Pull-Up**: A disconnected wire "floats" and will give random 1/0 values. Always use a internal pull-up/down.

### 12. Try This Next
*   **Random Defuse**: In the start phase, pick a random pin from 14-16 to be the "Safe" one, so the player can't memorize the answer.
"""

    p0589 = """
---

## 1. Project 0589: Automated Kitchen Timer

### 2. Learning Objective
Programm a "Motion-Sensitive Safety Light" that turns on for 5 minutes and restarts the timer every time new movement is detected.

### 3. Concepts Introduced
*   Retriggerable Timers
*   PIR Integration
*   Event-based Reset
*   Duration Persistence

### 4. Hardware Required
*   Raspberry Pi Pico
*   PIR Motion Sensor
*   Relay/LED (The Light)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **PIR Signal** | GP14 | Motion Detect |
| **Light Relay** | GP16 | Energy Control |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `if_else`**
*   **from Sensors, drag `pico_pir_motion`**

### 7. Variables
*   **off_time**: Integer (Timestamp)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (Input), GP16 (Output).

**B. Detection Phase**
2.  **Watch for Movement**:
    *   If GP14 is HIGH:
        *   Turn Light ON.
        *   **Reset Deadline**: `off_time = current_ms + 10000` (Demo: 10 seconds).

**C. Timer Phase**
3.  **Evaluate Expiry**:
    *   If `current_ms` > `off_time`:
        *   Turn Light OFF.

### 9. Execution Flow
1.  **Event**: Person walks into the room.
2.  **Activation**: The PIR detects movement. The Light turns on.
3.  **Scheduling**: The computer schedules a "Turn Off" time 10 seconds in the future.
4.  **Refresh**: If the person moves again at second 8, the "Turn Off" time is moved forward another 10 seconds.
5.  **Shutdown**: Only when the room has been silent and still for a full 10 seconds does the light finally cut power.

### 10. Generated Code
```python
import machine, time

pir = machine.Pin(14, machine.Pin.IN)
light = machine.Pin(16, machine.Pin.OUT)

deadline = 0

while True:
    # 1. Look for motion
    if pir.value():
        light.on()
        # Set turn-off for 10s from now
        deadline = time.ticks_ms() + 10000 
        print("Motion detected - Timer Reset.")
        
    # 2. Look at clock
    if time.ticks_ms() > deadline:
        if light.value():
            print("System Idle - Powering Down.")
            light.off()
            
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **PIR Warmup**: PIR sensors need ~30 seconds of quiet after power-on to calibrate. Moving during this time will cause false detections.

### 12. Try This Next
*   **Daylight Sensor**: Only turn on the light if it's DARK (Light Sensor < 1000) AND motion is detected.
"""

    p0590 = """
---

## 1. Project 0590: Mastering Kitchen Timer

### 2. Learning Objective
Utilize the Pico's internal Real-Time Clock (RTC) to schedule events based on absolute wall-clock time (e.g., sounding an alarm at exactly 17:00).

### 3. Concepts Introduced
*   Real-Time Clock (RTC)
*   Datetime Tuples
*   Absolute vs Relative Time
*   Scheduling Logic

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **USB/Pico** | - | Internal Clock |

### 6. Blocks Used
*   **from Time, drag `pico_rtc_set`** (Initialize current time)
*   **from Time, drag `pico_rtc_get`** (Read current time)
*   **from Logic, drag `and_operation`**

### 7. Variables
*   **hour, minute**: Integer

### 8. Step-by-Step Guide

**A. Synchronization Phase**
1.  **Set Current Time**: Use `RTC.datetime((YEAR, MON, DAY, 0, HOUR, MIN, SEC, 0))`.

**B. Scheduled Loop Phase**
2.  **Read Current Hour/Min**:
    *   From **Time**, drag `pico_rtc_get`.
3.  **Evaluate Target**:
    *   If `current_hour` == 17 **AND** `current_min` == 0:
        *   Trigger ALARM (Buzzer/LED).
        *   Wait 60s (to prevent the alarm from triggering 1000 times in that single minute).

### 9. Execution Flow
1.  **Memory**: The Pico keeps a list of numbers representing the current Date and Time.
2.  **Monitoring**: The code ignores the total "uptime" and focuses on the "Hour" and "Minute" numbers.
3.  **Match**: When the system's clock matches the programmed 5:00 PM target, the alarm triggers.
4.  **Stability**: This allows for "Breakfast" or "Daily" timers that don't depend on how long ago the user pressed a button.

### 10. Generated Code
```python
import machine, time

rtc = machine.RTC()
# (Year, Month, Day, Weekday, Hr, Min, Sec, Subsec)
# Manually sync to 4:59:50 PM
rtc.datetime((2023, 1, 1, 0, 16, 59, 50, 0))

while True:
    t = rtc.datetime()
    hr = t[4]
    mn = t[5]
    sc = t[6]
    
    print(f"Time: {hr:02}:{mn:02}:{sc:02}")
    
    # Alarm at 5 PM (17:00)
    if hr == 17 and mn == 0:
        print("!!! ALARM: GO HOME !!!")
        # Beep or Signal
        time.sleep(61) # Skip the rest of this minute
        
    time.sleep(1)
```

### 11. Common Mistakes
*   **Power Loss**: The internal RTC resets to default (e.g. 2021) if power is disconnected. (Solution: Use an external battery-backed DS3231 RTC module).

### 12. Try This Next
*   **Alarm Clock Menu**: Use buttons to set the target `alarm_hr` and `alarm_mn` variables instead of typing them in code.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0581 + p0582 + p0583 + p0584 + p0585 + p0586 + p0587 + p0588 + p0589 + p0590)
    
    print("Batch 59 (0581-0590) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch59()
