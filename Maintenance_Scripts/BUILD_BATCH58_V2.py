import os

def build_batch58_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0571 = """
---

# Batch 58: Stopwatch 3

## 1. Project 0571: Introduction to Stopwatch

### 2. Learning Objective
Utilize the internal system clock to measure and display the raw elapsed time in milliseconds since the Pico was powered on.

### 3. Concepts Introduced
*   System Ticks (`ticks_ms`)
*   Uptime Tracking
*   Linear Time scaling
*   Serial Output Formatting

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Console** | USB | Serial Monitoring |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`** (Get system run time)
*   **from Text, drag `print`**

### 7. Variables
*   **elapsed_time**: Integer (Current count)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Boot Header**:
    *   From **Text**, drag `print` "System clock starting...".
    *   **Snap** into `start` block.

**B. Main Loop Phase**
1.  **Read Clock**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** into entry.
2.  **Assign Value**:
    *   From **Variables**, set `elapsed_time` to **Time** `pico_milliseconds`.
    *   **Snap** into loop.
3.  **Display Status**:
    *   From **Text**, drag `print`.
    *   **Snap** below.
    *   Parameter: "Uptime: [elapsed_time] ms".
4.  **Frequency**:
    *   From **Time**, drag `pico_wait` 0.1s.

### 9. Execution Flow
1.  **Start**: The Pico begins its internal hardware counter.
2.  **Process**: Every 100 milliseconds, the code asks the CPU for the current "Tick" count.
3.  **Output**: The value is sent via USB to the terminal.
4.  **Repeat**: The number grows larger and larger as time passes.
5.  **Observation**: This represents the "Raw Data" used for all timing calculations.

### 10. Generated Code
```python
import time

while True:
    # Get raw ms since boot
    now = time.ticks_ms()
    print(f"PICO UPTIME: {now} ms")
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Overflow**: After ~25 days of continuous running, the `ticks_ms` counter will "wrap around" to zero. For most short projects, this is not an issue.

### 12. Try This Next
*   **Seconds Converter**: Use a Math block to divide the variable by 1000 to show "Seconds" instead of "MS".
"""

    p0572 = """
---

## 1. Project 0572: Blinking Stopwatch

### 2. Learning Objective
Create a "Running Indicator" that flashes an LED at a speed synchronized with the stopwatch—blinking once every exactly 1.0 seconds as the count increments.

### 3. Concepts Introduced
*   Visual Timekeeping
*   Second-boundary detection
*   State Synchronisation
*   Visual Pace

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Timer LED** | GP16 | Pace Flash |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Math, drag `modulo`** (Check remainder)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **tick_val**: Integer (Milliseconds)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Pin**:
    *   Init GP16 as Output.

**B. Main Loop Phase**
1.  **Track Time**:
    *   From **Loops**, drag `pico_forever`.
2.  **Update Count**:
    *   From **Variables**, set `tick_val` to **Time** `pico_milliseconds`.
    *   **Snap** into loop.
3.  **Find the Second**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If (`tick_val` % 1000) < 500:
        *   **Action**: From **Smart IO**, set GP16 HIGH.
    *   **Else**:
        *   **Action**: From **Smart IO**, set GP16 LOW.
4.  **Display**:
    *   Print `tick_val` / 1000.

### 9. Execution Flow
1.  **Start**: The timer begins at 0.
2.  **Process**: The system uses the "Modulo" ($1000$) to check how many milliseconds into the "current second" we are.
3.  **Output**: For the first half of every second ($0-499ms$), the LED is ON.
4.  **Output**: For the second half ($500-999ms$), the LED is OFF.
5.  **Observation**: This creates a perfect 1Hz pulse that is mathematically locked to the internal stopwatch data.

### 10. Generated Code
```python
import machine, time

led = machine.Pin(16, machine.Pin.OUT)

while True:
    now = time.ticks_ms()
    
    # Blink based on time math (no sleep needed for timing!)
    if (now % 1000) < 500:
        led.on()
    else:
        led.off()
        
    # Optional print for verification
    if now % 100 == 0:
        print(f"Time: {now/1000:.1f}s")
```

### 11. Common Mistakes
*   **Using Sleep**: If you use `time.sleep(1)` to blink, you can't read the buttons or do other math during that 1 second. Using `ticks_ms` lets the code run "instantly."

### 12. Try This Next
*   **Faster flash**: Change the modulo range to blink 5 times per second.
"""

    p0573 = """
---

## 1. Project 0573: Manual Stopwatch Control

### 2. Learning Objective
Build a "Lap Timer" where one button starts/stops the total clock and a second button prints the current "split" (Lap) time to the console.

### 3. Concepts Introduced
*   Difference Calculation ($Now - Last$)
*   Split-Time Logic
*   State Controls (Run/Pause)
*   Timestamp Storage

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Push Buttons

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Reset/Lap**  | GP14 | Split command |
| **Start/Stop** | GP15 | Master gate |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`**
*   **from Variables, drag `set_variable`**
*   **from Math, drag `subtraction`** (Deltas)

### 7. Variables
*   **start_tick**: Integer (Reference)
*   **lap_time**: Integer (Current delta)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Anchor**:
    *   From **Variables**, set `start_tick` to **Time** `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Monitor Actions**:
    *   From **Loops**, drag `pico_forever`.
2.  **Capture Lap**:
    *   From **Logic**, if Button GP14 is HIGH:
        *   **Action**: Set `lap_time` = **Time** `pico_milliseconds` - `last_lap_tick`.
        *   **Action**: From **Text**, print "LAP TIME: [lap_time] ms".
        *   **Action**: Set `last_lap_tick` = `current_ms`.
        *   Wait 0.3s.
3.  **Master Reset**:
    *   From **Logic**, if Button GP15 is HIGH:
        *   **Action**: Set `start_tick` = `current_ms`.
        *   Print "STOPWATCH CLEARED".

### 9. Execution Flow
1.  **Start**: The stopwatch begins at whatever time the "Anchor" was set.
2.  **Interaction**: User hits the "Lap" button while running.
3.  **Math**: The Pico subtracts the "Previous Lap Time" from the "Current Time."
4.  **Output**: The elapsed duration for *only that segment* is displayed.
5.  **Process**: The system updates the "Last Lap" variable to prepare for the *next* segment.
6.  **Repeat**: Allows an athlete or coder to see individual segment performance.

### 10. Generated Code
```python
from machine import Pin
import time

btn_lap = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_clr = Pin(15, Pin.IN, Pin.PULL_DOWN)

last_lap = time.ticks_ms()
start = time.ticks_ms()

while True:
    # Record current lap
    if btn_lap.value():
        now = time.ticks_ms()
        diff = time.ticks_diff(now, last_lap)
        print(f"Split: {diff} ms | Total: {time.ticks_diff(now, start)} ms")
        last_lap = now
        time.sleep(0.3)
        
    if btn_clr.value():
        start = time.ticks_ms()
        last_lap = start
        print("--- TIMER RESET ---")
        time.sleep(0.3)
```

### 11. Common Mistakes
*   **Subtraction Error**: Using `now - last` directly across long periods. Always use `time.ticks_diff()` to handle internal clock "wrap around" correctly.

### 12. Try This Next
*   **Multi-Lap**: Save the last 5 lap times in a list and print the "Fastest Lap" at the end.
"""

    p0574 = """
---

## 1. Project 0574: Stopwatch Sequences

### 2. Learning Objective
Programm a "Relay Race" tracker that automatically marks 4 distinct stages of 5 seconds each, signaling a "Runner Swap" with a buzzer.

### 3. Concepts Introduced
*   Stage Progression
*   Fixed-Interval Signaling
*   Duration Monitoring
*   Audible Feedback

### 4. Hardware Required
*   Raspberry Pi Pico
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Whistle** | GP15 | Phase change alert |

### 6. Blocks Used
*   **from Loops, drag `repeat`** (Count 4 runners)
*   **from Time, drag `pico_wait`**
*   **from Text, drag `print`**

### 7. Variables
*   **runner_num**: Integer (1-4)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare Start**:
    *   Set GP15 (Buzzer) to LOW.

**B. Main Loop Phase**
1.  **Race Loop**:
    *   From **Loops**, drag `repeat` 4 times.
2.  **Start Segment**:
    *   From **Variables**, set `runner_num` to loop index.
    *   From **Text**, print "RUNNER [runner_num] GO!".
    *   **Action**: From **Smart IO**, pulse GP15 (Buzzer) for 0.2s.
3.  **Wait Duration**:
    *   From **Time**, wait 5 seconds. (Simulating high speed runner).
4.  **Finish**:
    *   After 4 repeats, pulse GP15 for 1.0s.
    *   Print "RACE FINISHED".

### 9. Execution Flow
1.  **Start**: The buzzer beeps once. The terminal announces "Runner 1".
2.  **Process**: The system tracks a fixed 5-second "Stopwatch" period.
3.  **Transition**: At the end of the duration, the buzzer beeps again.
4.  **Repeat**: The logic iterates 4 times, simulating a full relay team effort.
5.  **Output**: A final long beep signals the race is over.
6.  **Utility**: Shows how stopwatch logic can be used to manage schedules.

### 10. Generated Code
```python
import machine
import time

buz = machine.Pin(15, machine.Pin.OUT)

for runner in range(1, 5):
    print(f"RUNNER {runner}: GO GO GO!")
    # Start whistle
    buz.on(); time.sleep(0.2); buz.off()
    
    # Track segment
    time.sleep(5)
    
# Finish whistle
print("--- RELAY COMPLETE ---")
buz.on(); time.sleep(1); buz.off()
```

### 11. Common Mistakes
*   **Blocking Code**: Since we use `time.sleep(5)`, we cannot "Stop" the race early with a button. The Pico is "blind" during the 5 seconds.

### 12. Try This Next
*   **Live Clock**: Print the remaining seconds in a `count_down` loop inside the race block.
"""

    p0575 = """
---

## 1. Project 0575: Interactive Stopwatch

### 2. Learning Objective
Build a "Reflex Speed Test" where a random LED flash triggers the user to hit a button; the Pico then measures the elapsed time in milliseconds.

### 3. Concepts Introduced
*   Reaction Latency
*   Event-based Start
*   Random Delays
*   Precision Timing

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED, Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Go Lamp**   | GP16 | Signal Light |
| **User Trigger**| GP14 | Reflex Button |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `random_integer`**
*   **from Loops, drag `repeat_until`**

### 7. Variables
*   **trigger_ms**: Integer (Moment LED turned on)
*   **reaction**: Integer (Final score)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set State**:
    *   From **Smart IO**, set GP16 (LED) to LOW.
    *   Wait for a "Get Ready" period.

**B. Main Loop Phase**
1.  **Wait Randomly**:
    *   From **Time**, drag `pico_wait`.
    *   Set to **Math** `random_integer` 1 to 5 seconds.
2.  **Flash Signal**:
    *   From **Smart IO**, set GP16 to HIGH.
    *   From **Variables**, set `trigger_ms` to `pico_milliseconds`.
3.  **Monitor Reflex**:
    *   From **Loops**, drag `repeat_until` GP14 (Button) is HIGH.
4.  **Calculate Result**:
    *   From **Variables**, set `reaction` to `pico_milliseconds` - `trigger_ms`.
    *   From **Text**, print "YOUR SPEED: [reaction] ms".
5.  **Reset**:
    *   Wait 2s and repeat.

### 9. Execution Flow
1.  **Start**: The user is waiting. The LED is off.
2.  **Suspense**: The clock waits a random amount of time (user can't guess).
3.  **Signal**: The LED snaps ON. The system records the current timestamp.
4.  **Sense**: The user hits the button as fast as possible.
5.  **Math**: The Pico subtracts the "Signal Time" from the "Press Time."
6.  **Output**: The difference (e.g., 250ms) is our reaction speed.

### 10. Generated Code
```python
from machine import Pin
import time
import random

led = Pin(16, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print("READY...")
    led.off()
    time.sleep(random.uniform(2, 5))
    
    print("GO!!!")
    led.on()
    start = time.ticks_ms()
    
    # Wait for button
    while not btn.value():
        pass
        
    score = time.ticks_diff(time.ticks_ms(), start)
    print(f"REACTION: {score} ms")
    led.off()
    time.sleep(2)
```

### 11. Common Mistakes
*   **Cheating**: If the user holds the button down *before* the LED flashes, the score will be 0ms. Use code to check if button is released *before* starting.

### 12. Try This Next
*   **False Start**: Print "CHEATER!" if the button is pressed while the LED is still OFF.
"""

    p0576 = """
---

## 1. Project 0576: Smart Stopwatch Switch

### 2. Learning Objective
Programm an "Inactivity Timeout" that monitors how long it has been since a button was pressed and turns off an LED if the "Idle time" exceeds 10 seconds.

### 3. Concepts Introduced
*   Inactivity Monitoring
*   Keep-Alive logic
*   Timestamp Clipping
*   Power Saving States

### 4. Hardware Required
*   Raspberry Pi Pico
*   User Input Button
*   Status LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **User Interaction**| GP14 | Reset idle clock |
| **System Power** | GP16 | Status Light |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Math, drag `subtraction`**
*   **from Variables, drag `set_variable`**

### 7. Variables
*   **last_action**: Integer (Timestamp)
*   **idle_ms**: Integer (Calculated delay)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start Anchor**:
    *   From **Variables**, set `last_action` to `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Sense Interaction**:
    *   From **Loops**, drag `pico_forever`.
2.  **Reset Idle**:
    *   From **Logic**, if GP14 (Button) is HIGH:
        *   **Action**: Set `last_action` to `pico_milliseconds`.
3.  **Calculate Idle**:
    *   From **Variables**, set `idle_ms` to `pico_milliseconds` - `last_action`.
    *   **Snap** into loop.
4.  **Evaluate Strategy**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `idle_ms` < 10000 (Within 10s):
        *   **Action**: Set GP16 (LED) HIGH (Active).
    *   **Else (IDLE)**:
        *   **Action**: Set GP16 (LED) LOW (Battery Save).

### 9. Execution Flow
1.  **Start**: System is active. LED is on.
2.  **Process**: The Pico checks the clock constantly.
3.  **Interaction**: If the user hits the button, the `last_action` timestamp is updated to "Now."
4.  **Decide**: If the gap between "Now" and `last_action` crosses 10,000ms, the system realizes the user has walked away.
5.  **Output**: The LED turns off to save power.
6.  **Restore**: Hitting the button at any time restarts the 10-second timer.

### 10. Generated Code
```python
import machine, time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

last_act = time.ticks_ms()

while True:
    # Reset on button
    if btn.value():
        last_act = time.ticks_ms()
        
    # Check idle duration
    idle = time.ticks_diff(time.ticks_ms(), last_act)
    
    if idle < 10000:
        led.on()
    else:
        led.off()
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Blocking Sleep**: If you use `time.sleep(10)` to wait for the timeout, the button won't work to "wake" the system up. Always use non-blocking `ticks_ms` for interactive timeouts.

### 12. Try This Next
*   **Warning Pulse**: Make the LED blink slowly when it gets to 8 seconds of idle.
"""

    p0577 = """
---

## 1. Project 0577: Stopwatch Alarm System

### 2. Learning Objective
Create a "Duration Safety Alarm" that sounds a buzzer if a specific operation (e.g., a fan running) lasts longer than a pre-defined safety limit (5 seconds).

### 3. Concepts Introduced
*   Operation Duration Monitoring
*   Safety Limit Enforcement
*   Audible Warnings
*   Conditional Fault States

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan (or LED)
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Operation Switch**| GP14 | Run command |
| **Buzzer Alarm**   | GP15 | Fault indicator |
| **Main Load**      | GP16 | Fan/Light |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Time, drag `pico_milliseconds`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **run_start**: Integer (Timestamp)
*   **is_running**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Defaults**:
    *   Set `is_running` to FALSE.

**B. Main Loop Phase**
1.  **Detect Start**:
    *   From **Logic**, if GP14 (Switch) is HIGH AND `is_running` is FALSE:
        *   **Action**: Set `run_start` = `pico_milliseconds`.
        *   **Action**: Set `is_running` = TRUE.
2.  **Detect Stop**:
    *   From **Logic**, if GP14 is LOW:
        *   **Action**: Set `is_running` = FALSE.
        *   **Action**: Set GP15 (Buzzer) LOW.
3.  **Evaluate Duration**:
    *   From **Logic**, if `is_running` is TRUE:
        *   **Action**: Set GP16 HIGH.
        *   **If (`pico_milliseconds` - `run_start`) > 5000**:
            *   **Action**: Set GP15 (Buzzer) HIGH.
            *   **Action**: Print "SAFETY LIMIT EXCEEDED!".

### 9. Execution Flow
1.  **Start**: User flips the switch to RUN.
2.  **Anchor**: The code captures the exact "Start" timestamp of the task.
3.  **Process**: The Pico monitors the duration live.
4.  **Sense**: If the switch stays ON for more than 5 seconds.
5.  **Output**: The buzzer screams to warn that the machine is running too long.
6.  **Recovery**: Once the user turns OFF the master switch, the alarm and machine both stop.

### 10. Generated Code
```python
import machine, time

sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.Pin(15, machine.Pin.OUT)
fan = machine.Pin(16, machine.Pin.OUT)

running = False
start_time = 0

while True:
    # 1. Start Detection
    if sw.value() and not running:
        running = True
        start_time = time.ticks_ms()
        
    # 2. End Detection
    if not sw.value():
        running = False
        fan.off()
        buz.off()
        
    # 3. Running Logic
    if running:
        fan.on()
        elapsed = time.ticks_diff(time.ticks_ms(), start_time)
        if elapsed > 5000:
            print("WARNING: TASK EXCEEDS SAFETY DURATION")
            buz.on()
            
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Missing Switch Check**: Forgetting to check `not running` when starting. This would reset the `start_time` every loop, meaning the 5-second alarm would never trigger!

### 12. Try This Next
*   **Kill Switch**: If the alarm lasts for more than 2 additional seconds, force the fan (GP16) to turn OFF automatically.
"""

    p0578 = """
---

## 1. Project 0578: The Stopwatch Game

### 2. Learning Objective
Programm a "Precision Clicker" game where the user must press a button to stop a hidden timer as close to exactly 1.000 milliseconds (1 second) as possible.

### 3. Concepts Introduced
*   Blind Timing (Mental clock)
*   Absolute Tolerance ($Target \pm Error$)
*   Feedback Scoring
*   Interaction Cycles

### 4. Hardware Required
*   Raspberry Pi Pico
*   Button, OLED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stop Button** | GP14 | Check timing |
| **OLED SDA**    | GP8 | Results Display |

### 6. Blocks Used
*   **from Display, drag `pico_oled_text`**
*   **from Math, drag `absolute_value`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **score_error**: Integer (How much off)
*   **is_playing**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set HUD**:
    *   From **Display**, `text` "Wait for GO...".

**B. Main Loop Phase**
1.  **Wait for Start**:
    *   Wait for Button GP14.
    *   From **Text**, print "TIMER RUNNING... PRESS NOW!".
    *   From **Variables**, set `start` to `pico_milliseconds`.
2.  **Catch User**:
    *   Wait for Button GP14 again (Second press).
    *   From **Variables**, set `stop` to `pico_milliseconds`.
3.  **Evaluate Accuracy**:
    *   `result = stop - start`.
    *   `score_error = absolute_value(result - 1000)`.
4.  **Display Grade**:
    *   From **Logic**, if `score_error` < 50: "LEGEND!".
    *   **Else If** `score_error` < 200: "GOOD JOB".
    *   **Else**: "TOO SLOW/FAST".
    *   From **Display**, show `result` and `Grade`.

### 9. Execution Flow
1.  **Start**: User clicks once to start the "invisible" clock.
2.  **Process**: The system tracks milliseconds in the background. No display is shown to keep it challenging.
3.  **Action**: User clicks again when they "think" one second has passed.
4.  **Math**: The Pico calculates the error (e.g., 1050ms = 50ms error).
5.  **Output**: The screen reveals the actual time and a motivational message.
6.  **Repeat**: Ready for the next attempt.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306, time

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    oled.fill(0); oled.text("TRICKY TIME", 20, 10); oled.text("PRESS to START", 10, 30); oled.show()
    while not btn.value(): pass # Wait for start
    time.sleep(0.3)
    
    start = time.ticks_ms()
    oled.fill(0); oled.text("RUNNING...", 10, 30); oled.show()
    
    while not btn.value(): pass # Wait for stop
    stop = time.ticks_ms()
    result = time.ticks_diff(stop, start)
    err = abs(result - 1000)
    
    oled.fill(0)
    oled.text(f"TIME: {result}ms", 10, 10)
    if err < 50: oled.text("GODLIKE!", 10, 40)
    elif err < 150: oled.text("GREAT", 10, 40)
    else: oled.text("TOO FAR!", 10, 40)
    oled.show()
    time.sleep(3)
```

### 11. Common Mistakes
*   **Debounce Error**: Without the `time.sleep(0.3)` after start, the same button press that starts the timer might immediately stop it (0ms score).

### 12. Try This Next
*   **Target Swap**: Randomize the target between 500ms and 2000ms each round.
"""

    p0579 = """
---

## 1. Project 0579: Automated Stopwatch

### 2. Learning Objective
Implement a "Usage Data Logger" that counts and displays how many seconds a specific device (LED) has been turned ON since boot.

### 3. Concepts Introduced
*   Cumulative Logging
*   Logic gating
*   Background Counters
*   Temporal Integration

### 4. Hardware Required
*   Raspberry Pi Pico
*   Switch, LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Load Switch** | GP14 | Monitor this |
| **Status LED**  | GP16 | Visual output |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Variables, drag `change_variable`**
*   **from Math, drag `addition`**

### 7. Variables
*   **total_seconds**: Integer (Accumulator)
*   **last_check**: Integer (Timestamp)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   Set `total_seconds = 0`.
    *   Set `last_check = current_ms`.

**B. Main Loop Phase**
1.  **Check Gate**:
    *   From **Loops**, drag `pico_forever`.
2.  **Sense Power**:
    *   From **Logic**, if GP14 (Switch) is HIGH:
        *   **Action**: From **Smart IO**, set GP16 HIGH (Device on).
        *   **Action**: If (`current_ms - last_check`) > 1000:
            *   **Change** `total_seconds` by 1.
            *   Set `last_check` = `current_ms`.
            *   Print "Cumulative Usage: [total_seconds]s".
    *   **Else**:
        *   Set GP16 LOW.

### 9. Execution Flow
1.  **Start**: The usage log is zero.
2.  **Action**: User turns the switch ON. The LED glows.
3.  **Process**: The Pico notices the switch is "Live."
4.  **Math**: Every time the internal clock moves forward by 1000ms, the system adds "1" to the lifetime log.
5.  **Output**: If the user runs the light for 10 seconds, turns it off, and then 10 more later, the display correctly shows "20s".
6.  **Repeat**: Ideal for tracking battery life or factory maintenance cycles.

### 10. Generated Code
```python
import machine, time

sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

total_s = 0
last_update = time.ticks_ms()

while True:
    if sw.value():
        led.on()
        # Has one second passed?
        if time.ticks_diff(time.ticks_ms(), last_update) >= 1000:
            total_s += 1
            last_update = time.ticks_ms()
            print(f"LIFETIME RUNTIME: {total_s} seconds")
    else:
        led.off()
        # Keeps last_update current so it doesn't "jump" when turned back on
        last_update = time.ticks_ms()
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Drift**: If you don't update `last_update` inside the `else` block, the very first second after you turn the switch back on will count incorrect time.

### 12. Try This Next
*   **Service Due**: Print a "SERVICE REQUIRED" message if `total_seconds` > 3600 (One hour of use).
"""

    p0580 = """
---

## 1. Project 0580: Mastering Stopwatch

### 2. Learning Objective
Programm a "Multitasking Scheduler" that uses independent stopwatch anchors to blink two different LEDs at different frequencies simultaneously without using `sleep()`.

### 3. Concepts Introduced
*   Non-blocking Scheduling
*   Dual Timeline Coordination
*   State Toggling
*   Pseudo-Parallelism

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x LEDs

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1 (Fast)** | GP16 | 200ms rate |
| **LED 2 (Slow)** | GP17 | 1000ms rate |

### 6. Blocks Used
*   **from Variables, drag `change_variable`**
*   **from Logic, drag `not`** (State flip)
*   **from Time, drag `pico_milliseconds`**

### 7. Variables
*   **timerA, timerB**: Integer (Anchors)
*   **stateA, stateB**: Boolean (ON/OFF)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Anchors**:
    *   Set `timerA = current_ms`, `timerB = current_ms`.
    *   Set `stateA = FALSE`, `stateB = FALSE`.

**B. Main Loop Phase**
1.  **Enter Scheduler**:
    *   From **Loops**, drag `pico_forever`.
2.  **Task A (Fast)**:
    *   If (`current_ms - timerA`) > 200:
        *   `stateA = NOT stateA`.
        *   Set GP16 to `stateA`.
        *   `timerA = current_ms`.
3.  **Task B (Slow)**:
    *   If (`current_ms - timerB`) > 1000:
        *   `stateB = NOT stateB`.
        *   Set GP17 to `stateB`.
        *   `timerB = current_ms`.

### 9. Execution Flow
1.  **Process**: The code loops at maximum speed (thousands of times per second).
2.  **Decide**: In every loop, it asks: "Has 200ms passed for LED 1?" and "Has 1000ms passed for LED 2?"
3.  **Output**: Usually, the answer is "No" for both.
4.  **Reaction**: If the clock hits 200ms, Task A flips its light and resets its specific stopwatch.
5.  **Reaction**: Task B continues to wait silently until its 1000ms goal is hit.
6.  **Observation**: Both LEDs blink independently, showing that the Pico can "Think" about multiple timelines at once.

### 10. Generated Code
```python
import machine, time

l1 = machine.Pin(16, machine.Pin.OUT)
l2 = machine.Pin(17, machine.Pin.OUT)

t1 = time.ticks_ms()
t2 = time.ticks_ms()
s1 = False; s2 = False

while True:
    now = time.ticks_ms()
    
    # Independent Task 1 (200ms)
    if time.ticks_diff(now, t1) > 200:
        s1 = not s1
        l1.value(s1)
        t1 = now
        
    # Independent Task 2 (1000ms)
    if time.ticks_diff(now, t2) > 1000:
        s2 = not s2
        l2.value(s2)
        t2 = now
```

### 11. Common Mistakes
*   **Inserting Sleep**: If you add `time.sleep(0.1)` anywhere in this loop, it will "Break" the coordination of both timers because the whole loop stops. This pattern MUST be 100% sleep-free.

### 12. Try This Next
*   **Three Timers**: Add a third LED that blinks every 3000ms.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0571 + p0572 + p0573 + p0574 + p0575 + p0576 + p0577 + p0578 + p0579 + p0580)
    
    print("Batch 58 (0571-0580) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch58_v2()
