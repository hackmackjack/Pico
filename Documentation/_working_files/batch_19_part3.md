
## Project 0187: Kitchen Timer Alarm System

### 1. Learning Objective
Explore multi-sensor safety logic. Learn how to combine a simple timer with a simulated "Smoke Detector" (Gas sensor or button) to create a system that upgrades a standard "Ding" into an emergency siren if danger is detected.

### 2. Concepts Introduced
*   **Emergency Upgrade**: changing the behavior of an alarm based on secondary sensor input.
*   **Siren Logic**: Using rapid frequency shifts (if using PWM) or rapid on/off cycling to represent danger.
*   **Interlock Logic**: Requiring multiple conditions (Timer = 0 AND Sensor = High) for a specific outcome.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   Gas Sensor (MQ-2) or 1 Button (Simulating a smoke alarm)
*   1 Red LED
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Smoke Sensor** | GP14 | HIGH = Smoke detected |
| **Alarm Buzzer** | GP15 | Safety Siren |
| **Status LED** | GP13 | Flashes red on danger |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **timer**: Remaining seconds (init 10).
*   **smoke_danger**: Boolean result from the sensor.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   **Set** `timer` = 10.
    *   **Set** `smoke_danger` = False.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Count Down**:
    *   If `timer` > 0:
        *   **Set** `timer` = `timer` - 1.
        *   **Print** "Seconds till done: ", `timer`.
        *   **Wait** 1 second.

**C. Safety Check Phase**
4.  **Detect Smoke**:
    *   **Set** `smoke_danger` = **Smart IO** `pico_gpio_read` GP14.
5.  **Determine Alarm Type**:
    *   If `timer` == 0:
        *   If `smoke_danger` == True:
            *   **Print** "!!! FIRE DETECTED !!! BURNT TOAST ALARM !!!".
            *   From **Loops**, drag a repeat (10 times loop).
                *   **Set** GP15 (Buzzer) -> HIGH, **Wait** 0.05s, **Set** GP15 -> LOW, **Wait** 0.05s. (Aggressive siren).
                *   **Set** GP13 (LED) -> HIGH, **Wait** 0.05s, **Set** GP13 -> LOW.
        *   Else (If no smoke):
            *   **Print** "Food is ready! Ding!".
            *   **Set** GP15 (Buzzer) -> HIGH, **Wait** 2s, **Set** GP15 -> LOW. (Friendly beep).

### 8. Execution Flow
1.  **Routine**: The timer counts 10, 9, 8...
2.  **Check**: At 0, the Pico looks at Pin 14.
3.  **Safe**: If you didn't burn anything, the buzzer makes a single long, calm sound.
4.  **Danger**: If the smoke sensor is active (or you hold the button), the buzzer goes into "Siren Mode," beeping frantically like a fire alarm.
5.  **Result**: An intelligent kitchen assistant that knows the difference between a cooked meal and a kitchen fire.

### 9. Generated Code
```python
from machine import Pin
import time

siren = Pin(15, Pin.OUT)
sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(13, Pin.OUT)

timer = 10

while True:
    if timer > 0:
        timer -= 1
        print("T-Minus: " + str(timer))
        time.sleep(1)
        
    if timer == 0:
        if sensor.value() == 1:
            print("FIRE FIRE FIRE!")
            # Emergency Siren
            for _ in range(50):
                siren.value(1)
                led.value(1)
                time.sleep(0.05)
                siren.value(0)
                led.value(0)
                time.sleep(0.05)
        else:
            print("Standard Finish.")
            siren.value(1)
            time.sleep(2)
            siren.value(0)
            
        # Reset for next round
        timer = 10
        time.sleep(2)
```

### 10. Common Mistakes
*   **Sequential Logic**: If you put the smoke check OUTSIDE the `timer == 0` block, it will siren even when you aren't cooking. ensure danger is only checked when it "matters" for a burnt toast alarm.
*   **Sensor Noise**: some gas sensors need 2 minutes to "Warm up" before they give accurate data.

### 11. Try This Next
*   **Auto-Fan**: if smoke is detected, automatically turn on the "Smart Fan" from Project 0141 to clear the air.
*   **Critical Countdown**: if smoke is detected DURING the countdown, immediately skip to 0 and sound the siren.

---

## Project 0188: The Kitchen Timer Game

### 1. Learning Objective
Learn about input sequence validation under time pressure. Understand how to track a counter (Task Progress) while simultaneously managing a countdown (Game Time), simulating a "Defusal" or high-speed challenge.

### 2. Concepts Introduced
*   **Input Requirements**: confirming that a user has performed a specific number of actions.
*   **Time Pressure Logic**: terminating a game with a "Fail" state if tasks aren't completed by 0.
*   **Multi-Button Coordination**: Using two different inputs for different parts of the sequence.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (A and B)
*   10k Ohm resistors
*   Buzzer (for the "Explosion" sound)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Task 1 (Must press 5 times) |
| **Button B** | GP13 | Task 2 (Must press 2 times) |
| **Buzzer** | GP15 | Failsafe alarm |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Logic, drag `controls_if`** (checking progress)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **game_timer**: Seconds remaining until failure (init 30).
*   **presses_a**, **presses_b**: trackers for user progress.
*   **defused**: State flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Game Context**:
    *   **Set** `game_timer` = 30.
    *   **Set** `presses_a` = 0.
    *   **Set** `presses_b` = 0.
    *   **Print** "BOMB ARMED: 30s! Sequence: A x5, then B x2!".

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Track the Clock**:
    *   If `game_timer` > 0 and `defused` is False:
        *   **Set** `game_timer` = `game_timer` - 1.
        *   **Print** "DETONATION IN: ", `game_timer`.
        *   **Wait** 1 second.

**C. Player Interaction Phase**
4.  **Count A Presses**:
    *   If **Button A** (GP14) is Pressed AND `presses_a` < 5:
        *   **Set** `presses_a` = `presses_a` + 1.
        *   **Print** "Task A: ", `presses_a`, "/5".
        *   **Wait** 0.1s.
5.  **Count B Presses**:
    *   If **Button B** (GP13) is Pressed AND `presses_a` == 5 AND `presses_b` < 2:
        *   **Set** `presses_b` = `presses_b` + 1.
        *   **Print** "Task B: ", `presses_b`, "/2".
        *   **Wait** 0.1s.

**D. Outcome Phase**
6.  **Success**:
    *   If `presses_b` == 2:
        *   **Set** `defused` = True.
        *   **Print** "--- BOMB DEFUSED! GREAT JOB! ---".
7.  **Failure**:
    *   If `game_timer` == 0 and `defused` is False:
        *   **Print** "!!! BOOM !!! MISSION FAILED".
        *   **Set** GP15 (Buzzer) -> HIGH for 3 seconds.

### 8. Execution Flow
1.  **Tension**: The console counts down 30, 29, 28...
2.  **Task 1**: You tap Button A rapidly. The Pico keeps score.
3.  **Task 2**: Once A is done, you must switch to Button B.
4.  **Climax**: You finish Button B with 2 seconds to spare.
5.  **Result**: The timer stops, and victory is declared.

### 9. Generated Code
```python
from machine import Pin
import time

btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)

timer = 30
a_count = 0
b_count = 0
defused = False

while True:
    if not defused and timer > 0:
        # User input handling (Non-blocking)
        if btn_a.value() and a_count < 5:
            a_count += 1
            print("Button A: {}/5".format(a_count))
            time.sleep(0.2)
            
        if btn_b.value() and a_count == 5 and b_count < 2:
            b_count += 1
            print("Button B: {}/2".format(b_count))
            time.sleep(0.2)
            
        if b_count == 2:
            defused = True
            print("DEFUSED!")
            
        # Time management
        # We use a small tick (0.1s) and count 10 of them for a second
        # to keep button response fast.
        pass 

    # Simplified Loop for teaching
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **Blocking Sleep**: If you use `time.sleep(1)` inside the loop, the buttons will feel "Broken" because they only work during that tiny split second of checking. Use smaller 0.1s ticks.
*   **Order**: ensure you can't start Button B until A is finished!

### 11. Try This Next
*   **Random Sequence**: After 5 successful defusals, make the Pico pick a random number of presses for A and B.
*   **Panic Mode**: At 5 seconds left, make the buzzer "Tick" faster.

---

## Project 0189: Automated Kitchen Timer

### 1. Learning Objective
Explore analog configuration interfaces. Learn how to "Map" a potentiometer's 270-degree rotation (0-1023) to a specific time range (0 to 60 minutes) for a traditional manual dial experience.

### 2. Concepts Introduced
*   **Analog Input Mapping**: scaling raw voltage into a human-meaningful duration.
*   **Real-Time UI Updates**: reflecting the current dial position on the console or display immediately.
*   **Coarse vs. Fine Control**: Understanding that a small knob movement represents a large time jump in a 60-minute range.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer (10k Ohm)
*   1 Button (Start)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Duration Dial** | GP26 (ADC0) | Turns to set time |
| **Start Button** | GP14 | Press to begin countdown |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_map`** (convert range)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **knob_val**: raw analog reading.
*   **set_minutes**: the selected duration.
*   **timer_running**: state flag.

### 7. Step-by-Step Guide

**A. Selection Phase**
1.  **Read the Dial**:
    *   From **Loops**, drag `pico_forever`.
    *   If `timer_running` is False:
        *   **Set** `knob_val` = **Sensors** `pico_analog_read` GP26.
        *   From **Math**, **Map** [0 to 1023] into [0 to 60].
        *   **Set** `set_minutes` to this result.
        *   **Print** "Dial points to: ", `set_minutes`, " minutes".

**B. Launch Phase**
2.  **Start the Timer**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `timer_running` = True.
        *   **Set** `total_seconds` = `set_minutes` * 60.

**C. Countdown Phase**
3.  **Run the Clock**:
    *   If `timer_running` is True:
        *   If `total_seconds` > 0:
            *   **Set** `total_seconds` = `total_seconds` - 1.
            *   **Print** "Time Remaining: ", `total_seconds`, " s".
            *   **Wait** 1 second.
        *   Else:
            *   **Print** "TIME'S UP! Dials reset.".
            *   **Set** `timer_running` = False.

### 8. Execution Flow
1.  **Wiggle**: You turn the potentiometer. The console shows "10m... 25m... 45m...".
2.  **Aim**: You stop exactly at 30 minutes.
3.  **Lock**: You hit the button. The dial is now "ignored" so knocking it won't change your cooking time.
4.  **Tick**: The Pico counts down from 1800 seconds (30 mins).
5.  **Finish**: Once done, the dial is unlocked so you can set your next timer.

### 9. Generated Code
```python
import machine
import utime

pot = machine.ADC(26)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

running = False
duration_m = 0
sec_left = 0

while True:
    if not running:
        # Selection Mode
        raw = pot.read_u16()
        duration_m = int((raw / 65535) * 60) # 0 to 60 minutes
        print("Set Time: " + str(duration_m) + " minutes")
        
        if btn.value():
            sec_left = duration_m * 60
            running = True
            print("TIMER LOCKED: START!")
            utime.sleep(0.5)
            
    if running:
        # Active Mode
        if sec_left > 0:
            sec_left -= 1
            m = sec_left // 60
            s = sec_left % 60
            print("REMAINING: {:02d}:{:02d}".format(m, s))
            utime.sleep(1)
        else:
            print("DING!")
            running = False
            
    utime.sleep(0.1)
```

### 10. Common Mistakes
*   **Dial Jitter**: Analog values sometimes bounce (e.g., 29 to 30 to 29). During configuration, your console might spam messages. Only print if the value has changed.
*   **Math**: ensure you convert minutes to seconds for the internal countdown, or your 30-minute timer will finish in 30 seconds!

### 11. Try This Next
*   **OLED Support**: Show a circular "progress bar" on the OLED that matches the potentiometer's position.
*   **Click-to-Stop**: If the timer is running, make the button "Stop" and "Cancel" it immediately.

---

## Project 0190: Mastering Kitchen Timer

### 1. Learning Objective
Explore concurrency and time-slicing. Learn how to manage two independent timers (e.g., Oven and Stove) simultaneously using a single loop, ensuring both decrement and alert accurately without blocking each other.

### 2. Concepts Introduced
*   **Parallel Tracking**: Managing multiple distinct data sets (Timer A vs Timer B).
*   **Time Multiplexing**: Updating multiple values in one cycle of the processor.
*   **User Priority**: defining how to display multiple statuses on one limited screen/console.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Reset A, Reset B)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Reset A** | GP14 | Resets Timer A |
| **Reset B** | GP13 | Resets Timer B |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Text, drag `text_print`** (print)
*   **from Logic, drag `controls_if`** (checking both timers)

### 6. Variables
*   **timer_a**, **timer_b**: Individual counters.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup Times**:
    *   **Set** `timer_a` = 20.
    *   **Set** `timer_b` = 45.

**B. Processing Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Process Timer A**:
    *   If `timer_a` > 0:
        *   **Set** `timer_a` = `timer_a` - 1.
    *   If **Button A** is pressed:
        *   **Set** `timer_a` = 20.

4.  **Process Timer B**:
    *   If `timer_b` > 0:
        *   **Set** `timer_b` = `timer_b` - 1.
    *   If **Button B** is pressed:
        *   **Set** `timer_b` = 45.

**C. Reporting Phase**
5.  **Merged Display**:
    *   From **Text**, drag `text_print`.
    *   **Format**: "OVEN (A): ", `timer_a`, " | STOVE (B): ", `timer_b`.
6.  **Clock Pace**:
    *   **Wait** 1 second. (Crucial! this 1s period handles both timers at once).

### 8. Execution Flow
1.  **Sync**: The Pico loop starts.
2.  **Step A**: Timer A goes from 20 to 19.
3.  **Step B**: Timer B goes from 45 to 44.
4.  **Show**: The user sees both updates at the same time on the same line.
5.  **Restart**: User finishes eggs and hits Button B. Timer B jumps back to 45, while Timer A continues undisturbed at 12, 11...
6.  **Result**: True multi-tasking on a single microcontroller.

### 9. Generated Code
```python
from machine import Pin
import time

btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Starting times
oven = 20
stove = 45

while True:
    # Logic Oven
    if oven > 0:
        oven -= 1
    if btn_a.value():
        oven = 20
        print("Oven Reset")
        
    # Logic Stove
    if stove > 0:
        stove -= 1
    if btn_b.value():
        stove = 45
        print("Stove Reset")
        
    # Joint Status
    status = "OVEN: {} | STOVE: {}".format(oven, stove)
    print(status)
    
    if oven == 0: print("!!! OVEN DONE !!!")
    if stove == 0: print("!!! STOVE DONE !!!")
    
    time.sleep(1)
```

### 10. Common Mistakes
*   **Serial Wait**: If you use TWO `wait 1 second` blocks (one for each timer), your time will pass half as fast as real life! Only use ONE main delay at the end of the shared loop.
*   **Status Overload**: Printing too many messages can make it hard to read. Use the `format` or concatenated string method to keep info on one line.

### 11. Try This Next
*   **Dual Buzzer**: Make the buzzer beep differently for Oven (Short chirp) vs Stove (Long beep).
*   **OLED Split**: Divide the OLED screen into two halves, displaying Timer A on the top and Timer B on the bottom.

---
