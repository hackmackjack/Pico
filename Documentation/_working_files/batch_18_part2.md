
## Project 0175: Interactive Stopwatch

### 1. Learning Objective
Explore non-blocking readouts. Learn how to implement a "Lap Timer" where a user can capture specific time splits without interrupting the flow of the main counter.

### 2. Concepts Introduced
*   **Lap Splitting**: Capturing a snapshot of a variable while it continues to change.
*   **Non-Blocking Logic**: ensuring an input action (button press) doesn't stop the overall system clock.
*   **Event Logging**: Using the console to record a history of specific moments.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button (Lap/Split)
*   10k Ohm pull-down resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Lap Button** | GP14 | Press to record a split time |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait for ... seconds)

### 6. Variables
*   **master_time**: Total seconds since the program started.
*   **lap_count**: Number of laps recorded.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Values**:
    *   From **Variables**, **Set** `master_time` = 0.
    *   **Set** `lap_count` = 0.
    *   **Print** "Stopwatch Running... Press button for LAPS".

**B. Monitoring Phase**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Detect Lap Request**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True.
    *   **Action**:
        *   **Set** `lap_count` = `lap_count` + 1.
        *   From **Text**, **Print** "LAP ", `lap_count`, ": ", `master_time`, " s".
        *   **Wait** 0.3 seconds (Debounce to prevent multiple lap logs for one press).

**C. Continuous Clock Phase**
4.  **Increment Master Clock**:
    *   From **Variables**, **Set** `master_time` = `master_time` + 1.
    *   From **Text**, **Print** "Running: ", `master_time`.
    *   **Wait** 1 second.

### 8. Execution Flow
1.  **Count**: The Pico increments `master_time` every second and prints the running total.
2.  **Trigger**: The user presses the button at exactly 12 seconds.
3.  **Snapshot**: The code captures the number "12" and prints `LAP 1: 12 s`.
4.  **Continuity**: The master clock DOES NOT WAIT; it proceeds to 13, 14, 15...
5.  **Result**: A physical log of sub-durations within a single long period.

### 9. Generated Code
```python
from machine import Pin
import time

# Setup
btn_lap = Pin(14, Pin.IN, Pin.PULL_DOWN)
master_time = 0
lap_count = 0

print("Stopwatch Running... Press button for LAPS")

while True:
    # Check for Split/Lap
    if btn_lap.value():
        lap_count += 1
        print(">>> LAP " + str(lap_count) + " Split: " + str(master_time) + "s")
        time.sleep(0.3) # Debounce
        
    # Standard time increment
    master_time += 1
    print("Running: " + str(master_time))
    
    # Wait for the next tick
    # Note: Complex code might use ticks_ms for better accuracy
    time.sleep(1)
```

### 10. Common Mistakes
*   **Button Blocking**: If you put a long `wait` inside the button IF block (e.g., 2 seconds), you will miss the next second of the master clock. Keep split-time processing fast.
*   **Debounce Speed**: If 0.3s is too fast, you might get two lap logs for one tap.

### 11. Try This Next
*   **Fast Laps**: Change the resolution to 0.1s so you can record laps within milliseconds of each other.
*   **Gap Calculator**: Calculate the difference between the current lap and the previous lap to see how fast you were.

---

## Project 0176: Smart Stopwatch Switch

### 1. Learning Objective
Learn about idle timeouts and state-dependent resets. Understand how to track "System Inactivity" and automatically return the program to a zero-state if no user interaction occurs.

### 2. Concepts Introduced
*   **Inactivity Timer**: A hidden counter that tracks how long since the last input.
*   **Auto-Reset**: Self-cleaning logic that prevents old data from persisting.
*   **Nested Timing**: Managing a main operation (Stopwatch) and a secondary monitoring task (Inactivity) simultaneously.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button (Start/Stop/Interact)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Action Button** | GP14 | Resets the inactivity timer |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **timer_val**: Current stopwatch value.
*   **idle_sec**: Seconds passed since the timer was last stopped.
*   **is_running**: State flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup Variables**:
    *   **Set** `timer_val` = 0.
    *   **Set** `idle_sec` = 0.
    *   **Set** `is_running` = False.

**B. Control Phase (Loop)**
2.  **Monitor Interaction**:
    *   From **Loops**, drag `pico_forever`.
    *   If **Button** GP14 is pressed:
        *   **Toggle** `is_running`. (Flip between True and False).
        *   **Set** `idle_sec` = 0. (Activity reset!)
        *   **Wait** 0.3s.

**C. Operation Phase**
3.  **Running Logic**:
    *   If `is_running` == True:
        *   **Set** `timer_val` = `timer_val` + 1.
        *   **Print** "Time: ", `timer_val`.
        *   **Wait** 1 second.
4.  **Stopped / Idle Logic**:
    *   Else (If stopped):
        *   **Set** `idle_sec` = `idle_sec` + 1.
        *   If `idle_sec` >= 10:
            *   **Set** `timer_val` = 0.
            *   **Set** `idle_sec` = 0.
            *   **Print** "Idle Timeout: Counter Reset to Zero".
        *   **Wait** 1 second.

### 8. Execution Flow
1.  **Interact**: User starts the timer. It counts 1, 2, 3...
2.  **Stop**: User stops the timer at 15. It stays at 15.
3.  **Monitor**: Behind the scenes, the `idle_sec` counter starts ticking 1, 2, 3...
4.  **Threshold**: If the user doesn't press Start again before `idle_sec` hits 10, the "15" is wiped out.
5.  **Restart**: The system returns to a clean slate (0) automatically.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

# State
timer_val = 0
idle_sec = 0
is_running = False

while True:
    # Interaction check
    if btn.value():
        is_running = not is_running
        idle_sec = 0
        print("Toggled! Running: " + str(is_running))
        time.sleep(0.3)
        
    if is_running:
        timer_val += 1
        print("Time: " + str(timer_val))
    else:
        # Idle tracking
        idle_sec += 1
        if idle_sec >= 10:
            if timer_val > 0:
                timer_val = 0
                print("Idle Timeout! Resetting...")
            idle_sec = 0
            
    time.sleep(1)
```

### 10. Common Mistakes
*   **Idle Reset**: Forgetting to set `idle_sec = 0` when the button is pressed will cause a reset to occur 10 seconds after the VERY FIRST stop, regardless of when you last touched it.
*   **Wait Timing**: Since both branches wait 1s, the logic stays in sync with real-time.

### 11. Try This Next
*   **Visual Warning**: Make an LED blink faster as the 10-second timeout approaches.
*   **OLED HUD**: Show "RESET IN: X seconds" on the screen when the timer is stopped.

---

## Project 0177: Stopwatch Alarm System

### 1. Learning Objective
Learn about safety ceilings and upper-limit enforcement. Understand how to trigger a critical alert (Buzzer) when a specific time duration is exceeded, simulating an industrial or kitchen safety timeout.

### 2. Concepts Introduced
*   **Threshold Alarms**: Activating a high-frequency alert based on a value limit.
*   **Lockdown State**: Stopping an operation and requiring attention once an error or timeout occurs.
*   **Audio Feedback**: Using a buzzer to signal a non-visual "Time's Up" event.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer (Active or Passive)
*   1 Button (Reset/Stop)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+)** | GP15 | Alarm output |
| **Stop Button** | GP14 | Mutes alarm and resets |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **t**: Elapsed seconds.
*   **alarm_triggered**: State flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Alarm Ready**:
    *   **Set** `t` = 0.
    *   **Set** `alarm_triggered` = False.
    *   **Set** GP15 (Buzzer) to LOW.

**B. Monitoring Phase (Loop)**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.
3.  **Check for Overtime**:
    *   If `alarm_triggered` == False:
        *   **Set** `t` = `t` + 1.
        *   **Print** "Counter: ", `t`.
        *   If `t` >= 60:
            *   **Set** `alarm_triggered` = True.
            *   **Print** "!!! TIME LIMIT EXCEEDED !!!".
4.  **Sound Alarm**:
    *   If `alarm_triggered` == True:
        *   From **Smart IO**, **Set** GP15 (Buzzer) -> HIGH.
        *   **Wait** 0.2s.
        *   **Set** GP15 (Buzzer) -> LOW.
        *   **Wait** 0.2s. (Beeping effect).

**C. Reset Phase**
5.  **Mute the Alarm**:
    *   If **Button** GP14 is pressed:
        *   **Set** `alarm_triggered` = False.
        *   **Set** `t` = 0.
        *   **Set** GP15 (Buzzer) -> LOW.
        *   **Print** "Alarm Muted. Restarting...".

### 8. Execution Flow
1.  **Monitor**: The Pico counts up second by second.
2.  **Compare**: It checks if the count has reached 60 (the safety limit).
3.  **Trigger**: Once 60 is hit, the count stops, and the buzzer starts beeping rapidly.
4.  **Reaction**: The alarm will not stop until the user physically presses the Reset button.
5.  **Result**: An effective "Dead Man's Switch" or safety timer.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware
buzzer = Pin(15, Pin.OUT)
btn_reset = Pin(14, Pin.IN, Pin.PULL_DOWN)

# State
count = 0
alarm_active = False

while True:
    if not alarm_active:
        count += 1
        print("Progress: " + str(count) + " / 60")
        if count >= 60:
            alarm_active = True
        time.sleep(1)
    else:
        # Alarm Beeping
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        time.sleep(0.1)
        
        # Check for Reset
        if btn_reset.value():
            alarm_active = False
            count = 0
            print("Reset detected.")
            time.sleep(0.5)
```

### 10. Common Mistakes
*   **Infinite Alarm**: If you don't provide a button to reset `alarm_triggered`, the only way to stop the beeping is to pull the battery.
*   **Passive vs Active Buzzer**: A passive buzzer needs PWM to sound. Use an active buzzer (which beeps when given a simple HIGH signal) for this specific block logic.

### 11. Try This Next
*   **Dual Alert**: Add a Red LED that flashes along with the buzzer.
*   **Variable Warning**: Make the buzzer chirp once every 10 seconds (10, 20, 30...) before the final alarm at 60.

---

## Project 0178: The Stopwatch Game

### 1. Learning Objective
Explore internal perception of time. Learn how to implement a "Blind Count" logic where the display is hidden, requiring the user to rely on their own internal clock to match a target duration exactly.

### 2. Concepts Introduced
*   **Stealth Counting**: Running logic in the background without user-facing updates.
*   **Target Matching**: Comparing a hidden variable to a specific goal (10.0).
*   **Score Calculation**: Determining the "Error Offset" (How far off was the user?).

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   OLED Display (to reveal results)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stop Button** | GP14 | User's guess button |
| **OLED (I2C)** | GP0/GP1 | Only shows "X" during game |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (precision wait)
*   **from Displays, drag `pico_oled_text`** (show result)
*   **from Logic, drag `controls_if`** (checking result)

### 6. Variables
*   **internal_sec**: Hidden counter.
*   **is_playing**: Game state.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Game Ready**:
    *   From **Displays**, `pico_oled_clear`.
    *   **Print** to OLED: "GAME: STOP AT 10", "Press to START".
2.  **Wait for Start**:
    *   Repeat-until Button GP14 is Pressed.

**B. Blind Phase**
3.  **Hide the Time**:
    *   **Clear** OLED. Draw a single "???" in the center.
    *   Snap `pico_oled_show`.
4.  **Start Hidden Clock**:
    *   **Set** `internal_sec` = 0.
    *   **Set** `is_playing` = True.
    *   From **Loops**, Repeat-until Button GP14 is Pressed.
        *   **Set** `internal_sec` = `internal_sec` + 0.1.
        *   **Wait** 0.1 seconds. (Smaller steps for better precision).

**C. Reveal Phase**
5.  **Calculate Difference**:
    *   From **Math**, calculate `diff` = 10.0 - `internal_sec`.
6.  **Display Verdict**:
    *   **Clear** OLED.
    *   **Print** to OLED: "Actual: ", `internal_sec`.
    *   **Print** to OLED: "Error: ", `diff`.
    *   If `diff` < 0.5: **Print** "EXPERT!".
    *   Else: **Print** "Try Again!".
7.  **Finalize**: `pico_oled_show`. **Wait** 5 seconds.

### 8. Execution Flow
1.  **Ready**: The user prepares and hits start.
2.  **Go**: The screen goes blank. The Pico starts counting silently in 0.1s increments.
3.  **Guess**: After counting to 10 in their head, the user hits the button.
4.  **Reveal**: The Pico shows exactly how much time really passed (e.g., 9.4 seconds).
5.  **Score**: The user sees their error of 0.6 seconds and tries to improve.

### 9. Generated Code
```python
import machine
import utime
import ssd1306

# Hardware
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    oled.fill(0)
    oled.text("STOP AT 10", 25, 20)
    oled.text("TAP TO START", 15, 40)
    oled.show()
    
    # Wait for start
    while btn.value() == 0:
        utime.sleep(0.01)
    utime.sleep(0.5) # Prevent double click
    
    # Blind Count
    oled.fill(0)
    oled.text("???", 55, 30)
    oled.show()
    
    start_time = utime.ticks_ms()
    while btn.value() == 0:
        utime.sleep(0.01)
        
    end_time = utime.ticks_ms()
    actual = utime.ticks_diff(end_time, start_time) / 1000
    
    # Reveal
    oled.fill(0)
    oled.text("Actual: " + str(actual), 10, 10)
    error = abs(10.0 - actual)
    oled.text("Error: " + str(round(error, 2)), 10, 30)
    
    if error < 0.5:
        oled.text("EXCELLENT!", 20, 50)
    else:
        oled.text("TOO FAST/SLOW", 10, 50)
        
    oled.show()
    utime.sleep(5)
```

### 10. Common Mistakes
*   **Integer Math**: If you use `10 - internal_sec` and `internal_sec` is 9.9, you might get 0 instead of 0.1 depending on the language. Use float types for time.
*   **Double-Click**: pressing the button too fast at the start might immediately stop the game. Use a small `wait` after the start press.

### 11. Try This Next
*   **Audio Guide**: Play a click sound every second for the first 3 seconds to help the player find the rhythm.
*   **Penalty Zone**: If they stop after 15 seconds, make the buzzer sound an "Epic Fail" noise.

---
