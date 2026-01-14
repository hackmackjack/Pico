import os

def build_batch58():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0571 = """
---

# Batch 58: Stopwatch 3

## 1. Project 0571: Introduction to Stopwatch

### 2. Learning Objective
Observe the internal system clock of the Raspberry Pi Pico by viewing the direct millisecond tick count since the device powered on.

### 3. Concepts Introduced
*   System Ticks (`ticks_ms`)
*   Uptime Tracking
*   Real-time Monitoring
*   Frequency of Output

### 4. Hardware Required
*   Raspberry Pi Pico

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MicroUSB** | - | Power and Data |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`** (Get raw clock)
*   **from Text, drag `print`**

### 7. Variables
*   **now**: Integer (Current tick count)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Monitor Connectivity**: Ensure the Pico is connected to your IDE (Thonny).

**B. Main Loop Phase**
2.  **Get Time**:
    *   From **Time**, set `now` to `pico_milliseconds`.
3.  **Report**:
    *   Print: "Milliseconds since boot: [now]".
4.  **Wait**:
    *   Wait 0.1 seconds (100ms) to avoid flooding the terminal.

### 9. Execution Flow
1.  **Start**: The Pico's internal hardware timer starts at zero on power-up.
2.  **Capture**: Every 100ms, the software takes a snapshot of that counter.
3.  **Output**: The number increases rapidly (1000 every second).
4.  **Benefit**: This number is the "heartbeat" used for all subsequent timing projects.

### 10. Generated Code
```python
import time

while True:
    # Get total ms since power on
    now = time.ticks_ms()
    print(f"Uptime ms: {now}")
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Thinking it's "Wall Time"**: This doesn't show the hour or date, just how long the Pico has been alive.
*   **Overflow**: After ~49 days, the `ticks_ms` counter wraps around. (Not an issue for most short projects).

### 12. Try This Next
*   **Convert to Seconds**: Divide the raw number by 1000 to see the uptime in seconds.
"""

    p0572 = """
---

## 1. Project 0572: Blinking Stopwatch

### 2. Learning Objective
Implement a "Non-blocking" LED blink using the system clock instead of `time.sleep()`, allowing the Pico to perform other tasks while timing.

### 3. Concepts Introduced
*   Non-blocking Timing
*   Asynchronous Logic
*   `ticks_diff` Pattern
*   Concurrency Basics

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP16 | Signal Output |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `if_do`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **last_time**: Integer (Previous tick record)
*   **led_state**: Boolean (Current ON/OFF)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: GP16 as Output.
2.  **Set Anchor**: `last_time = pico_milliseconds`.

**B. Main Loop Phase**
3.  **Check Elapsed Time**:
    *   From **Logic**, if (`pico_milliseconds` - `last_time`) > 500:
        *   **Action**: Flip `led_state` (NOT `led_state`).
        *   **Action**: Set GP16 to `led_state`.
        *   **Action**: `last_time = pico_milliseconds` (Reset anchor).
4.  **Parallel Progress**:
    *   Add a print block saying "System is checking other things...".
    *   Note how the print never stops, unlike `sleep()` which freezes everything.

### 9. Execution Flow
1.  **Start**: System notes the time.
2.  **Poll**: The loop runs thousands of times per second.
3.  **Condition**: In most loops, the "Elapsed" time is small (e.g., 2ms), so nothing happens.
4.  **Trigger**: Once 500ms have passed, the "IF" condition becomes true.
5.  **Output**: The LED toggles, and the cycle begins checking for the *next* 500ms.

### 10. Generated Code
```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
last_v = time.ticks_ms()
st = False

while True:
    # Check if 500ms passed since last 'v'
    if time.ticks_diff(time.ticks_ms(), last_v) > 500:
        st = not st
        led.value(st)
        last_v = time.ticks_ms()
    
    # This keeps running!
    print(".", end="") 
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Forgetting to Reset**: Not updating `last_time = pico_milliseconds` inside the loop. The LED will turn on once and never blink again because the difference will always stay > 500.

### 12. Try This Next
*   **Double Blink**: Add a second LED on GP17 that blinks every 250ms using a separate variable.
"""

    p0573 = """
---

## 1. Project 0573: Manual Stopwatch Control

### 2. Learning Objective
Develop a professional Lap Timer where pressing a button records the current elapsed time ("Spilt") without stopping the main clock.

### 3. Concepts Introduced
*   Relative Timing
*   Event Logging
*   Capture Logic
*   Formatting Sequences

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Lap Button** | GP14 | Trigger split time |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Text, drag `print`**
*   **from Variables, drag `change_variable`**

### 7. Variables
*   **start_time**: Integer
*   **lap_num**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP14 (Input/Pull-Down).
2.  **Init**: `lap_num = 1`, `start_time = pico_milliseconds`.

**B. Main Loop Phase**
3.  **Listen**:
    *   If GP14 is HIGH:
        *   Calculate `elapsed = (pico_milliseconds - start_time) / 1000`.
        *   Print: "Lap [lap_num]: [elapsed] seconds".
        *   Increment `lap_num` by 1.
        *   Wait 0.3s (Debounce).
4.  **Display**:
    *   Optionally print the running `current_time` to see the flow.

### 9. Execution Flow
1.  **Start**: The race begins.
2.  **Input**: User hits the button as a runner passes.
3.  **Process**: The Pico subtracts the "Starting Time" from the "Current Time".
4.  **Log**: It shows the seconds elapsed.
5.  **Continuity**: Because we didn't reset `start_time`, the prochain lap will show the total time from the very beginning.

### 10. Generated Code
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
start = time.ticks_ms()
count = 1

while True:
    if btn.value():
        # Current time minus start time
        now = time.ticks_diff(time.ticks_ms(), start)
        sec = now / 1000
        print(f"LAP {count}: {sec:.2f} s")
        count += 1
        time.sleep(0.3)
```

### 11. Common Mistakes
*   **Integer Overflow**: Using milliseconds directly for long races (hours) can result in very large numbers. Converting to seconds (`/ 1000`) helps readability.

### 12. Try This Next
*   **Reset Button**: Add a second button on GP15 that sets `start_time` back to the current time, restarting the stopwatch.
"""

    p0574 = """
---

## 1. Project 0574: Stopwatch Sequences

### 2. Learning Objective
Programm a "Relay Handoff" system where two separate runners are timed. Runner 1's timer stops exactly when Runner 2's timer begins.

### 3. Concepts Introduced
*   Cumulative Timing
*   Sequential States (A -> B -> Finish)
*   State Machine logic
*   Inter-state variables

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Buttons (Runner 1 Start, Runner 2 Start/Finish)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn 1** | GP14 | Handoff Trigger |
| **Btn 2** | GP15 | Finish Line |

### 6. Blocks Used
*   **from Logic, drag `if_else`** (Selection)
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `arithmetic`**

### 7. Variables
*   **time1, time2**: Float (Individual durations)
*   **state**: Integer (0=Ready, 1=R1 Running, 2=R2 Running, 3=Done)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware and State**: `state = 0`.

**B. Sequence Logic**
2.  **Phase 0 (Start)**: If Button 1 pressed: `state = 1`, `start = ms`.
3.  **Phase 1 (Handoff)**: If Button 1 pressed again:
    *   `time1 = (ms - start)`.
    *   `state = 2`.
    *   `start = ms`. (Start R2's clock immediately).
4.  **Phase 2 (Finish)**: If Button 2 pressed:
    *   `time2 = (ms - start)`.
    *   `state = 3`.
5.  **Phase 3 (Results)**:
    *   Print "R1: [time1], R2: [time2], Total: [time1 + time2]".

### 9. Execution Flow
1.  **Race Start**: Button 1 is hit. Runner 1 is in motion.
2.  **Hand-off**: Button 1 is hit again. Runner 1's duration is locked, and Runner 2's clock starts at that exact microsecond.
3.  **Finish**: Button 2 is hit. Both individual segments are now recorded.
4.  **Output**: The system sums the values for a final relay score.

### 10. Generated Code
```python
import machine
import time

b1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
b2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

state = 0 # 0:Ready, 1:R1, 2:R2, 3:Result
t1 = 0; t2 = 0; start = 0

while state < 3:
    if state == 0 and b1.value():
        start = time.ticks_ms()
        state = 1; time.sleep(0.3)
        print("Runner 1 GO!")
        
    if state == 1 and b1.value():
        t1 = time.ticks_diff(time.ticks_ms(), start)
        start = time.ticks_ms()
        state = 2; time.sleep(0.3)
        print("HANDOFF! Runner 2 GO!")
        
    if state == 2 and b2.value():
        t2 = time.ticks_diff(time.ticks_ms(), start)
        state = 3
        print("FINISH!")

if state == 3:
    print(f"R1: {t1/1000:.2f}s")
    print(f"R2: {t2/1000:.2f}s")
    print(f"TOTAL: {(t1+t2)/1000:.2f}s")
```

### 11. Common Mistakes
*   **Double Trigger**: Without `time.sleep(0.3)`, a single long button press might skip the Runner 1 phase and immediately enter Runner 2.

### 12. Try This Next
*   **OLED HUD**: Show the running clock live on a display so the runners know their current pace.
"""

    p0575 = """
---

## 1. Project 0575: Interactive Stopwatch

### 2. Learning Objective
Create a "Reflex Tester" that measures how many milliseconds it takes for a user to react to a visual cue (LED lighting up).

### 3. Concepts Introduced
*   Reaction Latency
*   Event Interrupting
*   Random Delays
*   Precision Delta math

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x LED
*   1x Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | : :--- |
| **Alert LED** | GP16 | Visual Trigger |
| **Response Btn**| GP14 | Reaction Input |

### 6. Blocks Used
*   **from Time, drag `pico_wait`** (Random duration)
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `repeat_until`**

### 7. Variables
*   **start_tick**: Integer
*   **reaction**: Float

### 8. Step-by-Step Guide

**A. Wait Phase**
1.  **Get Ready**: LED is OFF.
2.  **Hide the Start**: Wait random (2 to 5 seconds). (Prevent user from guessing).

**B. Action Phase**
3.  **Trigger**:
    *   Turn LED ON.
    *   Set `start_tick` to `pico_milliseconds`.
4.  **Listen**:
    *   Wait until GP14 is HIGH.
5.  **Calculate**:
    *   `reaction = (pico_milliseconds - start_tick)`.
6.  **Report**:
    *   Print "Reaction Time: [reaction] ms".
    *   If `reaction` < 250: Print "ELITE!". Else: Print "Try harder!".

### 9. Execution Flow
1.  **Suspense**: The system sits silently. The user's finger is on the button.
2.  **Flash**: The LED pops ON at an unpredictable moment.
3.  **Logic**: The moment the LED turns on, the stop-watch starts invisibly.
4.  **Input**: The user hits the button.
5.  **Output**: The duration is displayed instantly to the thousandth of a second.

### 10. Generated Code
```python
from machine import Pin
import time, random

led = Pin(16, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print("Wait for it...")
    led.off()
    time.sleep(random.uniform(2, 5))
    
    # TRIGGER
    start = time.ticks_ms()
    led.on()
    
    # Loop until button pressed
    while not btn.value():
        pass
        
    diff = time.ticks_diff(time.ticks_ms(), start)
    print(f"REACTION: {diff}ms")
    
    if diff < 200: print("SUPERHUMAN!")
    led.off()
    time.sleep(3) # Break before next round
```

### 11. Common Mistakes
*   **Anticipation**: Some users will spam the button. Add a check: `if button.value() == 1` while the LED is still OFF, they lose!

### 12. Try This Next
*   **False Start**: Print "CHEAT DETECTED" if the button is pressed before the LED turns on.
"""

    p0576 = """
---

## 1. Project 0576: Smart Stopwatch Switch

### 2. Learning Objective
Programm an "Inactivity Timeout" that automatically resets the menu system if no buttons are pressed for 10 seconds.

### 3. Concepts Introduced
*   User Idle Detection
*   Watchdog Timers (Software)
*   State Resets
*   Timestamp Comparisons

### 4. Hardware Required
*   Raspberry Pi Pico
*   Push Button
*   OLED Display

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Activity Btn**| GP14 | Resets the timer |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `greater_than`**
*   **from Display, drag `pico_oled_clear`**

### 7. Variables
*   **last_act**: Integer (Last touch time)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Touch**: `last_act = pico_milliseconds`.

**B. Monitoring Phase**
2.  **Check for Activity**:
    *   If GP14 is HIGH:
        *   `last_act = pico_milliseconds`.
3.  **Evaluate Timeout**:
    *   `idle_time = pico_milliseconds - last_act`.
    *   If `idle_time` > 10000 (10s):
        *   OLED Clear.
        *   Print "SESSION TIMEOUT - GOING HOME".
        *   Set menu state back to 0.

### 9. Execution Flow
1.  **Use**: The user interacts with the system. Every click "resets" the timeout variable to the present time.
2.  **Abandon**: The user walks away.
3.  **Ticker**: The loop keeps checking `Now - Last_Touch`.
4.  **Threshold**: Eventually, the math results in a number > 10000.
5.  **Shutdown**: The screen wipes, preventing sensitive info from staying visible or saving power.

### 10. Generated Code
```python
import machine, time, ssd1306

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

last_touch = time.ticks_ms()

while True:
    # Any press refreshes the timer
    if btn.value():
        last_touch = time.ticks_ms()
        oled.fill(0); oled.text("ACTIVE", 40, 30); oled.show()
        
    # Check if abandoned
    elapsed = time.ticks_diff(time.ticks_ms(), last_touch)
    if elapsed > 10000:
        oled.fill(0); oled.text("--- SLEEP ---", 25, 30); oled.show()
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Milliseconds vs Seconds**: Forgetting that 10 seconds is 10,000 in the `ticks_ms` scale.

### 12. Try This Next
*   **Visual Warning**: At 8 seconds of idle, start flashing the text "TIMEOUT SOON..." to warn the user.
"""

    p0577 = """
---

## 1. Project 0577: Stopwatch Alarm System

### 2. Learning Objective
Develop a industrial "Duration Limiter" that shuts down a machine (LED) and sounds an alarm (Buzzer) if a process takes longer than a safe 5-second limit.

### 3. Concepts Introduced
*   Safety Cutoffs
*   Duration Monitoring
*   Forced State Overrides
*   Bypassing Faults

### 4. Hardware Required
*   Raspberry Pi Pico
*   Button, LED, Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Work Button** | GP14 | Hold to run machine |
| **Machine LED** | GP16 | Visual power indicator |
| **Alarm Buzzer**| GP15 | Safety Warning |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Time, drag `pico_milliseconds`**

### 7. Variables
*   **on_start**: Float (When button was first held)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **GPIO Setup**: Input (Pull-Down), Outputs x2.

**B. Monitoring Phase**
2.  **Machine Check**:
    *   If GP14 is HIGH:
        *   **If first press**: Record `on_start = ms`.
        *   Calculate `held_for = ms - on_start`.
        *   If `held_for` < 5000: Set LED HIGH.
        *   Else: Set LED LOW, Set Buzzer HIGH. (SAFETY HALT).
    *   Else (Button released):
        *   Set LED LOW, Buzzer LOW. Clear `on_start`.

### 9. Execution Flow
1.  **Operation**: User holds the button to run the fan/LED "machine".
2.  **Tracking**: The system notes how long it has been running continuously.
3.  **Safe Zone**: Between 0 and 5 seconds, everything works normally.
4.  **Shutdown**: At 5.1 seconds, the computer decides the machine has been on for too long (risk of overheat) and cuts the power while sounding a beep.
5.  **Cooling**: User must release the button to reset the safety timer.

### 10. Generated Code
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)
buz = machine.Pin(15, machine.Pin.OUT)

start = 0

while True:
    if btn.value():
        if start == 0: start = time.ticks_ms()
        
        elapsed = time.ticks_diff(time.ticks_ms(), start)
        if elapsed < 5000:
            led.on()
            buz.off()
        else:
            # SAFETY SHUTDOWN
            led.off()
            buz.on()
    else:
        led.off(); buz.off(); start = 0
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Latch Failure**: If you don't reset `start = 0` when the button is released, the machine will start with 0 seconds remaining the next time it is used.

### 12. Try This Next
*   **Cooldown Period**: If a timeout occurs, prevent the machine from starting again for at least 10 seconds.
"""

    p0578 = """
---

## 1. Project 0578: The Stopwatch Game

### 2. Learning Objective
Create a high-precision "Stop at 10.00" game to practice microsecond timing logic and UI refresh synchronization.

### 3. Concepts Introduced
*   Human-Machine Precision
*   Real-time Counter View
*   Delta Calculation (`abs`)
*   Float String Formatting

### 4. Hardware Required
*   Raspberry Pi Pico
*   OLED Display
*   Stop Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stop Button** | GP14 | Lock the clock |
| **OLED SDA** | GP8 | I2C Data |

### 6. Blocks Used
*   **from Display, drag `pico_oled_text`**
*   **from Time, drag `pico_milliseconds`**
*   **from Math, drag `abs`** (Absolute difference)

### 7. Variables
*   **score**: Float (User's stop time)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep**: Init OLED. `start = ms`.

**B. Run Phase**
2.  **While** Button GP14 is NOT pressed:
    *   Show current `elapsed` time on screen with 2 decimal places.
3.  **Capture Phase**:
    *   The moment button is pressed, record `score = elapsed`.
4.  **Evaluate**:
    *   Calculate `diff = abs(10.00 - score)`.
    *   Show: "FINAL: [score]".
    *   Show: "ERROR: [diff]".
    *   Wait 5s.

### 9. Execution Flow
1.  **Activity**: The clock numbers fly by on the OLED ($0.01, 0.02...$).
2.  **Reflex**: The user tries to hit the button exactly when the screen says $10.00$.
3.  **Judge**: The Pico captures the time even if it's $10.0024$.
4.  **Score**: The system tells the user exactly how many fractions of a second they were off by.

### 10. Generated Code
```python
import machine, time, ssd1306

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    start = time.ticks_ms()
    while not btn.value():
        elap = time.ticks_diff(time.ticks_ms(), start) / 1000
        oled.fill(0)
        oled.text(f"TIME: {elap:.2f}", 20, 30)
        oled.show()
    
    # STOPPED
    final = time.ticks_diff(time.ticks_ms(), start) / 1000
    error = abs(10.00 - final)
    oled.fill(0)
    oled.text(f"SCORE: {final}", 10, 20)
    oled.text(f"ERR: {error:.3f}", 10, 40)
    oled.show()
    time.sleep(4)
```

### 11. Common Mistakes
*   **OLED Lag**: Refreshing the OLED takes time (~20ms). This means the time the user SEES might be slightly older than the time the button captures. (This adds difficulty to the game!).

### 12. Try This Next
*   **Hard Mode**: Make the clock disappear after 5 seconds, so the user has to count the remaining 5 seconds in their head.
"""

    p0579 = """
---

## 1. Project 0579: Automated Stopwatch

### 2. Learning Objective
Create a "Environmental Datalogger" that records a series of temperature readings at fixed intervals and reports the full dataset at the end of the session.

### 3. Concepts Introduced
*   Time-Series Data
*   Array Appending (Lists)
*   Fixed-Interval Sampling
*   Batch Reporting

### 4. Hardware Required
*   Raspberry Pi Pico
*   Internal/External Temp Sensor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **MicroUSB** | - | Data Output (csv format) |

### 6. Blocks Used
*   **from List, drag `append_to_list`**
*   **from Loops, drag `repeat`** (60 times)
*   **from Sensors, drag `pico_internal_temp`**

### 7. Variables
*   **log**: List (Collection of readings)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Log**: `log = create_empty_list`.

**B. Logging Phase**
2.  **Repeat 60 times**:
    *   Read current temperature.
    *   Append (temp) to `log`.
    *   Print: "Recording sample [count/60]".
    *   Wait 1 second.

**C. Reporting Phase**
3.  **Print Database**:
    *   Loop through `log` and print each value.
    *   Example: "Sample 23, Temp: 24.5C".

### 9. Execution Flow
1.  **Process**: The Pico sits for one minute, clicking a "snapshot" of the room every second.
2.  **Memory**: The data is and held in RAM as a list.
3.  **Visualization**: After 60 seconds, the device "dumps" all the info to the terminal.
4.  **Utility**: This allows a researcher to leave the Pico in a room and come back later to see the history of changes.

### 10. Generated Code
```python
import machine, time

log = []
adc = machine.ADC(4)

print("LOGGING STARTED - 60 SAMPLES")
for i in range(60):
    v = adc.read_u16() * (3.3/65535)
    t = 27 - (v - 0.706)/0.001721
    
    log.append(t)
    print(f"[{i+1}/60] Saved: {t:.2f}")
    time.sleep(1)

print("\\n--- DATA SUMMARY ---")
for idx, val in enumerate(log):
    print(f"T+{idx}s: {val:.2f}C")
```

### 11. Common Mistakes
*   **RAM Limits**: If you record every millisecond for an hour, the Pico will run out of memory and crash. Keep lists to reasonable sizes (a few hundred readings).

### 12. Try This Next
*   **Trigger Start**: Only start logging if the temperature rises above $30^{\circ}C$ (Event-triggered logging).
"""

    p0580 = """
---

## 1. Project 0580: Mastering Stopwatch

### 2. Learning Objective
Programm a "Software Scheduler" that manages three independent LEDs blinking at different, non-multiplicational frequencies simultaneously using only one timer-based loop.

### 3. Concepts Introduced
*   Multi-tasking Scheduling
*   Independent Timing Intervals
*   Delta Comparison (Tick difference)
*   Cooperative Processing

### 4. Hardware Required
*   Raspberry Pi Pico
*   3x LEDs

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1** | GP16 | 500ms Interval |
| **LED 2** | GP17 | 700ms Interval |
| **LED 3** | GP18 | 1100ms Interval |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`**
*   **from Logic, drag `if_do`** (Used 3 times independently)
*   **from Variables, drag `change_variable`** (3 last_time anchors)

### 7. Variables
*   **t1, t2, t3**: Integer (Timestamps)
*   **s1, s2, s3**: Boolean (States)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Anchors**: Set `t1, t2, t3` to current `pico_ms`.
2.  **GPIO**: GP16-18 as Outputs.

**B. Scheduler Loop**
3.  **Task 1 (500ms)**:
    *   If (`ms` - `t1`) > 500: Toggle LED1, `t1 = ms`.
4.  **Task 2 (700ms)**:
    *   If (`ms` - `t2`) > 700: Toggle LED2, `t2 = ms`.
5.  **Task 3 (1100ms)**:
    *   If (`ms` - `t3`) > 1100: Toggle LED3, `t3 = ms`.

### 9. Execution Flow
1.  **Concurrent Processing**: The loop is extremely fast ($<1$ms).
2.  **Selection**: In a single pass, the CPU might find that Task 1 is ready but Task 2 is not.
3.  **Coordination**: Since no `time.sleep()` blocks are used, all three LEDs blink "at the same time" without interfering with each other's schedules.
4.  **Complex Pattern**: The resulting combination of 500, 700, and 1100 makes the lights look almost musical/rhythmic.

### 10. Generated Code
```python
import machine, time

leds = [machine.Pin(i, machine.Pin.OUT) for i in [16, 17, 18]]
timers = [time.ticks_ms()] * 3
intervals = [500, 700, 1100]
states = [False] * 3

while True:
    now = time.ticks_ms()
    
    for i in range(3):
        if time.ticks_diff(now, timers[i]) > intervals[i]:
            states[i] = not states[i]
            leds[i].value(states[i])
            timers[i] = now
```

### 11. Common Mistakes
*   **Using Sleep**: Adding even a tiny `time.sleep(0.1)` at the bottom of the loop will "skew" the timing of all three LEDs, making them increasingly inaccurate over time.

### 12. Try This Next
*   **Add a Sensor**: Add a fourth "task" that reads a temperature sensor every 2 seconds without slowing down the blinking LEDs.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0571 + p0572 + p0573 + p0574 + p0575 + p0576 + p0577 + p0578 + p0579 + p0580)
    
    print("Batch 58 (0571-0580) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch58()
