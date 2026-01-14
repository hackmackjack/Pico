import os

def build_batch59_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0581 = """
---

# Batch 59: Kitchen Timer 3

## 1. Project 0581: Introduction to Kitchen Timer

### 2. Learning Objective
Manipulate string output in the terminal to visualize the passage of time using symbols and automated line breaks.

### 3. Concepts Introduced
*   Console Formatting
*   Modulo for Layout
*   Temporal Sequencing
*   Character Streams

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
1.  **Init Header**:
    *   From **Text**, drag `print` "Timer Started...".
    *   **Snap** into `start`.
2.  **Reset Counter**:
    *   From **Variables**, set `ticks` to 0.

**B. Main Loop Phase**
1.  **Tick**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Variables**, change `ticks` by 1.
2.  **Visual Update**:
    *   From **Logic**, if (`ticks` % 10) == 0:
        *   **Action**: From **Text**, print " (10s Mark)". 
    *   **Else**:
        *   **Action**: From **Text**, print "." (without newline).
3.  **Wait**:
    *   From **Time**, drag `pico_wait` 1.0s.

### 9. Execution Flow
1.  **Start**: The system begins counting.
2.  **Process**: Every second, the Pico sends a single dot to the screen.
3.  **Condition**: The mathematical modulo (`%`) detects when 10 seconds have passed.
4.  **Formatting**: At the 10-second mark, the code forces a text label and a newline, making the long stream of dots easy to read.
5.  **Output**: Creates a visual rhythm in the terminal.

### 10. Generated Code
```python
import time

count = 0
while True:
    count += 1
    # Check if 10 seconds have passed for formatting
    if count % 10 == 0:
        print(" [10s]")
    else:
        # Standard dot on same line
        print(".", end="")
    
    time.sleep(1)
```

### 11. Common Mistakes
*   **Implicit Newlines**: Most `print()` calls in MicroPython automatically move to the next line. Using `end=""` ensures dots stay together.

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
*   High-Priority Alerting
*   Visual Thresholds

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alert LED** | GP16 | Urgency signal |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`**
*   **from Time, drag `pico_wait`** (Set variable duration)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **timer_val**: Integer (Seconds remaining)
*   **blink_speed**: Float (Wait duration)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Time**:
    *   From **Variables**, set `timer_val` to 15 (Demo seconds).

**B. Main Loop Phase**
1.  **Evaluate Urgency**:
    *   From **Loops**, drag `pico_forever`.
2.  **Select Pace**:
    *   From **Logic**, drag `if_elseif`.
    *   **If `timer_val` > 10**: `blink_speed = 1.0`.
    *   **Else If `timer_val` > 0**: `blink_speed = 0.2`.
    *   **Else**: `blink_speed = 0`.
3.  **Blink**:
    *   From **Smart IO**, set GP16 HIGH. Wait `blink_speed`.
    *   From **Smart IO**, set GP16 LOW. Wait `blink_speed`.
4.  **Decrement**:
    *   From **Variables**, change `timer_val` by -1.

### 9. Execution Flow
1.  **Start**: The user sees a slow, calm LED blink.
2.  **Process**: The system tracks the remaining time.
3.  **Selection**: When the timer crosses the "Danger" threshold ($10s$), the `blink_speed` variable is updated.
4.  **Output**: The LED instantly switches to a rapid strobe, creating psychological urgency.
5.  **Steady State**: At zero, the LED stays on permanently.
6.  **Utility**: Essential for kitchen tasks where you might be across the room.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(16, Pin.OUT)
timer = 15

while timer >= 0:
    if timer > 10:
        # Slow
        wait = 0.5
    elif timer > 0:
        # Fast
        wait = 0.1
    else:
        # Solid
        led.on(); break
        
    led.on(); time.sleep(wait)
    led.off(); time.sleep(wait)
    timer -= (wait * 2)
```

### 11. Common Mistakes
*   **Math Error**: If you wait for 0.5s and then 0.5s, 1.0 seconds have passed. Be sure your subtraction matches your wait times!

### 12. Try This Next
*   **Audible Beep**: Add a buzzer that only beeps during the "Fast" phase.
"""

    p0583 = """
---

## 1. Project 0583: Manual Kitchen Timer Control

### 2. Learning Objective
Build a "Dial-and-Set" kitchen timer using a potentiometer to select a duration (0-60 minutes) and a button to begin the countdown.

### 3. Concepts Introduced
*   Analog Parameter Selection
*   State Lock-in
*   User UI Updates
*   Conversion (Mins to Secs)

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer, Button, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Duration Knob**| GP26 (ADC) | Setting input |
| **Start Button** | GP14 | Start command |
| **OLED SDA**    | GP8 | UI display |

### 6. Blocks Used
*   **from Display, drag `pico_oled_text`**
*   **from Math, drag `map_range`** (0 to 60)
*   **from Loops, drag `repeat_until`**

### 7. Variables
*   **selected_m**: Integer (UI value)
*   **is_running**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Mode**:
    *   From **Variables**, set `is_running` to FALSE.

**B. Configuration Phase**
1.  **Select Duration**:
    *   From **Loops**, repeat until GP14 (Button) is HIGH.
2.  **Update UI**:
    *   From **Variables**, set `selected_m` to **Math** `map_range` `pico_adc_read` (1 to 60).
    *   From **Display**, `clear`, then `text` "SET: [selected_m] MINS", then `show`.

**C. Active Phase**
1.  **Commit**:
    *   From **Text**, print "TIMER STARTED".
2.  **Count Down**:
    *   From **Loops**, repeat `selected_m` * 60 times.
    *   From **Time**, wait 1.0s.
    *   Show remaining time on OLED.

### 9. Execution Flow
1.  **Sense**: The user rotates the knob. The OLED shows the "Proposed" time instantly.
2.  **Decide**: The user is happy with 5 minutes and hits the button.
3.  **Process**: The `repeat_until` loop breaks. The system calculates the total seconds.
4.  **Process**: The knob is now ignored (Lock-in).
5.  **Output**: The countdown proceeds on screen.
6.  **Termination**: The screen shows "FINISH" and beeps.

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
    oled.text(f"TIME: {s//60}m {s%60}s", 10, 30)
    oled.show()
    time.sleep(1); s -= 1

oled.fill(0); oled.text("DINNER READY!", 10, 30); oled.show()
```

### 11. Common Mistakes
*   **No Exit**: If you don't use `repeat_until` or a `while not button` loop, the program will try to start the timer while you are still trying to set it.

### 12. Try This Next
*   **Cancel Button**: Use a second button to stop the timer and return to the setting menu immediately.
"""

    p0584 = """
---

## 1. Project 0584: Kitchen Timer Sequences

### 2. Learning Objective
Programm a "Pomodoro Productivity System" that sequences between Work (25m) and Break (5m) periods using color-coded LED signals.

### 3. Concepts Introduced
*   Multi-State Sequences
*   Cyclic Workflows
*   User-Coded Timelines
*   Visual Mode Cues

### 4. Hardware Required
*   Raspberry Pi Pico
*   Green LED (Work)
*   Blue LED (Break)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Concentrate** | GP16 | Green Status |
| **Relax**       | GP17 | Blue Status |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Cycle count)
*   **from Smart IO, drag `pico_gpio_write`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **round**: Integer (Iterative counter)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   Set GP16/17 as Outputs.

**B. Sequence Phase**
1.  **Master Loop**:
    *   From **Loops**, repeat 4 times.
2.  **Work Period**:
    *   From **Smart IO**, set GP16 HIGH, GP17 LOW.
    *   From **Text**, print "FOCUS TIME (25 MINS)".
    *   From **Time**, wait 1500s (Demo: 10s).
3.  **Break Period**:
    *   From **Smart IO**, set GP16 LOW, GP17 HIGH.
    *   From **Text**, print "BREAK TIME (5 MINS)".
    *   From **Time**, wait 300s (Demo: 5s).

### 9. Execution Flow
1.  **Start**: The Green LED turns on. The user is instructed to focus.
2.  **Process**: The Pico tracks a long duration (25 minutes).
3.  **Transition**: At the end, it flips to Blue and alerts the user to rest.
4.  **Repeat**: The logic forces a productive 50/50 balance.
5.  **Termination**: After the 4th cycle, both LEDs turn off.
6.  **Utility**: Automates the management of human attention spans.

### 10. Generated Code
```python
import machine, time

green = machine.Pin(16, machine.Pin.OUT)
blue = machine.Pin(17, machine.Pin.OUT)

for loop in range(4):
    print(f"CYCLE {loop+1}: FOCUS")
    green.on(); blue.off()
    time.sleep(10) # 10s for demo
    
    print("CYCLE BREAK: REST")
    green.off(); blue.on()
    time.sleep(5) # 5s for demo

green.off(); blue.off()
print("FULL DAY COMPLETE.")
```

### 11. Common Mistakes
*   **Duration Testing**: Waiting 25 actual minutes to see if your code works. Always use small numbers (e.g., 5s, 10s) until you are sure the sequence is right, then change to 1500s.

### 12. Try This Next
*   **Buzzer Entry**: Blow a "Whistle" (Buzzer) for 1 second every time a transition occurs.
"""

    p0585 = """
---

## 1. Project 0585: Interactive Kitchen Timer

### 2. Learning Objective
Create an "Egg Preset Selector" where a single button cycle chooses between Small (3m), Medium (4m), and Large (5m) timer settings.

### 3. Concepts Introduced
*   Selection Presets
*   Parameter Switching
*   Menu Indexing
*   User-Friendly UI

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Select Button** | GP14 | Cycle presets |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `if_elseif`**
*   **from Display, drag `pico_oled_text`**

### 7. Variables
*   **egg_type**: Integer (0 to 2)
*   **timer_val**: Integer (Seconds)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Anchor**:
    *   From **Variables**, set `egg_type` to 0.

**B. Configuration Phase**
1.  **Input Loop**:
    *   From **Loops**, repeat until button *released*.
2.  **Cycle Mode**:
    *   From **Logic**, if Button GP14 is HIGH:
        *   **Action**: From **Variables**, increment `egg_type` by 1.
        *   **Action**: From **Time**, wait 0.3s (Debounce).
3.  **Map Mode**:
    *   If `egg_type` > 2: Set to 0.
    *   From **Logic**, drag `if_elseif`.
    *   If 0: "Small (3m)", Set `timer_val` = 180.
    *   If 1: "Medium (4m)", Set `timer_val` = 240.
    *   If 2: "Large (5m)", Set `timer_val` = 300.
4.  **Show**:
    *   Update OLED with name and time.

### 9. Execution Flow
1.  **Start**: Default mode is "Small Egg."
2.  **Interact**: User clicks the button once.
3.  **Process**: The `egg_type` value changes to 1.
4.  **Logic**: The computer looks at its map and sees 1 = 240 seconds.
5.  **Output**: The OLED displays "MIDDLE EGG - 4 MINS".
6.  **Utility**: Simplifies complex timing into recognizable user outcomes (Cooking presets).

### 10. Generated Code
```python
import machine, time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
mode = 0

while True:
    if btn.value():
        mode = (mode + 1) % 3
        time.sleep(0.3)
        
    if mode == 0:   print("SMALL EGG (3m)")
    elif mode == 1: print("MEDIUM EGG (4m)")
    else:           print("LARGE EGG (5m)")
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Variable Name**: Using different names for the same mode in different logic blocks. Be consistent (e.g., always use `mode`).

### 12. Try This Next
*   **Soft vs Hard**: Add another button to choose between Soft Boiled and Hard Boiled for each size.
"""

    p0586 = """
---

## 1. Project 0586: Smart Kitchen Timer Switch

### 2. Learning Objective
Implement a "Hardware Child Lock" where the timer's start/reset button is software-disabled unless a physical security switch is in the "Enabled" position.

### 3. Concepts Introduced
*   Logical Gating (AND)
*   Safety Interlocks
*   Input Inhibition
*   Permission Checking

### 4. Hardware Required
*   Raspberry Pi Pico
*   Toggle Switch (Lock)
*   Push Button (Action)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Lock Switch** | GP14 | ON = SAFE |
| **Start Button**| GP15 | User input |

### 6. Blocks Used
*   **from Logic, drag `and_operation`**
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Text, drag `print`**

### 7. Variables
*   **None**: Direct gate logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: GP14 (Lock) and GP15 (Action) as Inputs.

**B. Main Loop Phase**
1.  **Monitor Pad**:
    *   From **Loops**, drag `pico_forever`.
2.  **Check Permission**:
    *   From **Logic**, if (GP15 is HIGH) **AND** (GP14 is HIGH):
        *   **Action**: From **Text**, print "Command accepted. Timer started.".
        *   **Action**: Perform task.
    *   **Else If** (GP15 is HIGH) **AND** (GP14 is LOW):
        *   **Action**: From **Text**, print "LOCKED! Check child-safety switch.".
        *   **Action**: From **Time**, wait 0.5s.

### 9. Execution Flow
1.  **Start**: The system is listening to both inputs.
2.  **Interact**: User hits "Start" while the switch is OFF.
3.  **Decide**: The `AND` condition fails because both inputs must be true.
4.  **Output**: A warning is shown, but no action is taken.
5.  **Interact**: User flips the safety switch and hits "Start."
6.  **Decide**: Both conditions are TRUE.
7.  **Output**: The command executes. Practical for kitchen safety.

### 10. Generated Code
```python
from machine import Pin
import time

lock = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn.value():
        if lock.value():
            print("ACCESS GRANTED.")
            time.sleep(1)
        else:
            print("SYSTEM LOCKED.")
            time.sleep(1)
            
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Wiring polarity**: If the switch is physically ON but returns LOW (PULL_UP), the logic will be backward. Invert the check if needed.

### 12. Try This Next
*   **Buzzer rejection**: Make an annoying sound if the button is pressed while locked.
"""

    p0587 = """
---

## 1. Project 0587: Kitchen Timer Alarm System

### 2. Learning Objective
Programm an "Alarm Escalation" system where a buzzer beeps faster and louder as the time since the timer finished increases.

### 3. Concepts Introduced
*   Fault Intensity Escalation
*   Post-Event Monitoring
*   Frequency Shifting
*   Persistent Alerts

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alarm Buzzer**| GP15 | Graduated signal |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `if_elseif`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **overtime**: Integer (ms since zero)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Anchor End**:
    *   From **Variables**, set `end_tick` to `pico_milliseconds`.

**B. Alarm Phase**
1.  **Maintain Alert**:
    *   From **Loops**, drag `pico_forever`.
2.  **Calculate Neglect**:
    *   From **Variables**, set `overtime` to `pico_milliseconds` - `end_tick`.
3.  **Evaluate Frequency**:
    *   From **Logic**, drag `if_elseif`.
    *   **If `overtime` < 10000**: Beep once every 1s.
    *   **Else If `overtime` < 30000**: Beep 5 times fast every 1s.
    *   **Else**: Beep continuously.
4.  **Execute Sound**:
    *   From **Smart IO**, turn GP15 ON/OFF based on above logic.

### 9. Execution Flow
1.  **Start**: The timer hits zero.
2.  **Output**: A polite beep signals the user.
3.  **Process**: If the user doesn't turn it off, the `overtime` variable continues to grow.
4.  **Reaction**: After 10 seconds, the frequency increases significantly to capture attention.
5.  **Reaction**: If neglected for 30 seconds, it shifts to a continuous tone to ensure it cannot be ignored.
6.  **Utility**: Prevents food from burning even if the user is preoccupied.

### 10. Generated Code
```python
import machine, time

buz = machine.Pin(15, machine.Pin.OUT)
finish_time = time.ticks_ms()

while True:
    elap = time.ticks_diff(time.ticks_ms(), finish_time)
    
    if elap < 10000:
        # Polite
        buz.on(); time.sleep(0.1); buz.off(); time.sleep(0.9)
    elif elap < 30000:
        # Urgent
        for _ in range(3):
            buz.on(); time.sleep(0.05); buz.off(); time.sleep(0.05)
        time.sleep(0.5)
    else:
        # Continuous
        buz.on()
```

### 11. Common Mistakes
*   **Infinite beeping**: Not including a way to "Stop" the loop inside the alarm phase. The user needs a button to acknowledge.

### 12. Try This Next
*   **PWM Pitch**: Make the pitch of the buzzer go HIGHER as it gets more urgent.
"""

    p0588 = """
---

## 1. Project 0588: The Kitchen Timer Game

### 2. Learning Objective
Create a "Bomb Defuser" game where the user must disconnect a specific jumper wire before a countdown hits zero; disconnecting the wrong one causes the timer to speed up.

### 3. Concepts Introduced
*   Continuity Sensing
*   Logic Traps
*   High-Stakes Timing
*   Pin State Detection

### 4. Hardware Required
*   Raspberry Pi Pico
*   3x Jumper Wires
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Defuse Pin**  | GP14 | Safe wire |
| **Trap Pin 1**  | GP15 | Fast penalty |
| **Trap Pin 2**  | GP16 | Fast penalty |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`**
*   **from Smart IO, drag `pico_gpio_read`** (Pull Up)
*   **from Text, drag `print`**

### 7. Variables
*   **speed**: Float (Seconds of delay)
*   **ticks**: Integer (Remaining)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Inputs**:
    *   Set GP14-16 as Inputs with **PULL-UP**.
2.  **Reset Game**:
    *   Set `ticks = 20`, `speed = 1.0`.

**B. Game Loop Phase**
1.  **Check Wire Status**:
    *   **Logic**: If GP14 is HIGH (Pulled out):
        *   **Action**: Print "SAFE!". Stop.
    *   **Logic**: If GP15 or 16 are HIGH:
        *   **Action**: Set `speed = 0.2`.
        *   **Action**: Print "MALFUNCTION - SPEED UP!".
2.  **Tick Clock**:
    *   From **Variables**, change `ticks` by -1.
    *   From **Text**, print "REMAINING: [ticks]".
3.  **Delay**:
    *   From **Time**, wait `speed` seconds.
4.  **Boom**:
    *   If `ticks` == 0: Print "BOOM".

### 9. Execution Flow
1.  **Start**: The numbers count down slowly (1 per second).
2.  **Interact**: User pulls a wire (it becomes HIGH because it's no longer grounded).
3.  **Process**: The Pico checks: "Is this Pin 14?"
4.  **Reaction**: If yes, the code ends immediately—victory.
5.  **Penalty**: If no, the `speed` variable is crushed from 1.0 down to 0.2.
6.  **Observation**: The timer now counts down 5 times faster, increasing panic.

### 10. Generated Code
```python
from machine import Pin
import time

# VALUE is 0 when PLUGGED IN (GND), 1 when PULLED OUT (Pull-Up)
defuse = Pin(14, Pin.IN, Pin.PULL_UP)
traps = [Pin(15, Pin.IN, Pin.PULL_UP), Pin(16, Pin.IN, Pin.PULL_UP)]

timer = 20
spd = 1.0

while timer > 0:
    # 1. WIN?
    if defuse.value():
        print("SYSTEM DEFUSED. SUCCESS.")
        break
    
    # 2. PENALTY?
    if any(t.value() for t in traps):
        spd = 0.2
        print("!!! WARNING: SPEED INCREASE !!!")
        
    print(f"SECONDS: {timer}")
    time.sleep(spd)
    timer -= 1

if timer == 0: print("GAME OVER - BOOM")
```

### 11. Common Mistakes
*   **No Pull-Up**: A disconnected pin without a pull-up doesn't know if it's 1 or 0 (it floats). Always enable the resistor.

### 12. Try This Next
*   **Random Defuse**: Use code at startup to pick which of the three pins (14, 15, or 16) is the "Safe" one.
"""

    p0589 = """
---

## 1. Project 0589: Automated Kitchen Timer

### 2. Learning Objective
Programm a "Hands-Free Lighting" system where a PIR sensor turns on a kitchen light for 10 seconds and resets the countdown every time fresh motion is detected.

### 3. Concepts Introduced
*   Retriggerable Timers
*   Motion-to-Power logic
*   Persistence intervals
*   Sensor Refresh

### 4. Hardware Required
*   Raspberry Pi Pico
*   PIR Motion Sensor
*   LED/Relay

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motion Sense**| GP14 | PIR Signal |
| **Pantry Light**| GP16 | Switch Actuator |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **expiry_tick**: Integer (Future timestamp)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial**:
    *   Set GP16 to LOW. Set `expiry_tick = 0`.

**B. Main Loop Phase**
1.  **Watch Movement**:
    *   From **Loops**, drag `pico_forever`.
2.  **Detect Motion**:
    *   From **Logic**, if GP14 (PIR) is HIGH:
        *   **Action**: Set GP16 HIGH.
        *   **Action**: Set `expiry_tick` = `pico_milliseconds` + 10000.
    *   **Else**:
        *   Do nothing.
3.  **Evaluate Time**:
    *   From **Logic**, if `pico_milliseconds` > `expiry_tick`:
        *   **Action**: Set GP16 LOW.

### 9. Execution Flow
1.  **Start**: The light is off.
2.  **Sense**: Someone walks into the pantry. The PIR sends a HIGH signal.
3.  **Process**: The code schedules the light to turn off exactly 10 seconds from "Now."
4.  **Persistence**: The person keeps moving as they look for ingredients.
5.  **Condition**: Each movement resets the "Off Time" to 10 seconds in the future.
6.  **Termination**: Only when the room has been completely still for 10 seconds does the light turn off.

### 10. Generated Code
```python
import machine, time

pir = machine.Pin(14, machine.Pin.IN)
led = machine.Pin(16, machine.Pin.OUT)

deadline = 0

while True:
    if pir.value():
        led.on()
        deadline = time.ticks_ms() + 10000 # 10s from now
        
    if time.ticks_ms() > deadline:
        led.off()
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **PIR Lag**: Most PIR sensors have a physical "Hold" time (a orange dial). If that's set to 5 minutes, your code won't see any resets until that 5 minutes is over.

### 12. Try This Next
*   **Soft Dim**: Use PWM to slowly fade the light out over 2 seconds instead of snapping off.
"""

    p0590 = """
---

## 1. Project 0590: Mastering Kitchen Timer

### 2. Learning Objective
Utilize the Pico's internal Real-Time Clock (RTC) to schedule events based on absolute wall-clock time (e.g., sounding an alarm at exactly 17:00).

### 3. Concepts Introduced
*   Real-Time Clock (RTC)
*   Absolute vs Relative Time
*   Tuple Unpacking
*   24-Hour Scheduling

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **System Time** | - | Internal Clock |
| **Alarm**       | GP15 | Output Signal |

### 6. Blocks Used
*   **from Time, drag `pico_rtc_get`** (Read clock)
*   **from Time, drag `pico_rtc_set`** (Configure current time)
*   **from Logic, drag `and_operation`**

### 7. Variables
*   **hour**: Integer (0-23)
*   **minute**: Integer (0-59)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set "Now"**:
    *   Config RTC to (2025, 12, 31, 16, 59, 50). (Simulating 4:59:50 PM).

**B. Main Loop Phase**
1.  **Read Ticks**:
    *   From **Loops**, drag `pico_forever`.
2.  **Pull Time**:
    *   From **Variables**, set `hour` and `minute` to **Time** `pico_rtc_get`.
3.  **Check Schedule**:
    *   From **Logic**, if (`hour` is 17) **AND** (`minute` is 0):
        *   **Action**: From **Smart IO**, pulse GP15 (Buzzer) for 1s.
        *   **Action**: Wait 60s (to avoid repeating the alarm 60 times in that minute).

### 9. Execution Flow
1.  **Start**: The computer knows it's almost 5:00 PM.
2.  **Process**: The system ignores its "Switch" status and looks only at the world clock.
3.  **Condition**: The hour and minute match the targets.
4.  **Reaction**: The alarm sounds immediately.
5.  **Output**: Provides a reliable "Oven Timer" that knows the exact time of day.
6.  **Utility**: Essential for any device that must coordinate with human schedules.

### 10. Generated Code
```python
import machine, time

rtc = machine.RTC()
# Year, Month, Day, Weekday, Hr, Min, Sec, Sub
rtc.datetime((2025, 12, 31, 0, 16, 59, 50, 0))

while True:
    now = rtc.datetime()
    hr, mn = now[4], now[5]
    
    print(f"CLOCK: {hr:02}:{mn:02}")
    
    if hr == 17 and mn == 0:
        print("DING! ALARM TRIGGERED.")
        # Trigger and skip the rest of the minute
        time.sleep(61)
        
    time.sleep(1)
```

### 11. Common Mistakes
*   **Power Loss**: The internal RTC resets to its default (usually year 2021) if power is disconnected unless an external battery is used.

### 12. Try This Next
*   **Day of Week**: Change the logic so the alarm only works on "Weekdays" (Indexes 0 to 4).
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0581 + p0582 + p0583 + p0584 + p0585 + p0586 + p0587 + p0588 + p0589 + p0590)
    
    print("Batch 59 (0581-0590) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch59_v2()
