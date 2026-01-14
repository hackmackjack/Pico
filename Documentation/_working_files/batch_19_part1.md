
# BATCH 19: Kitchen Timer 1 (Projects 0181-0190)

## Project 0181: Introduction to Kitchen Timer

### 1. Learning Objective
Learn the fundamentals of countdown logic. Understand how to decrement a variable over time and trigger a specific action (a "Ding" signal) when the counter reaches zero.

### 2. Concepts Introduced
*   **Variable Decrementation**: Using `value = value - 1` to count backwards.
*   **Termination Logic**: Comparing a variable to zero to end an operation.
*   **Time Delays**: Controlling the pace of a countdown using 1-second intervals.

### 3. Hardware Required
*   Raspberry Pi Pico

### 4. Wiring / Interfaces
*   **Internal**: Uses USB Serial for console output. No external components needed for basic logic.

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Math, drag `math_arithmetic`** (subtraction block)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait for ... seconds)

### 6. Variables
*   **timer_count**: Stores the remaining seconds for the countdown.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Position**:
    *   From **Variables**, drag the `variables_set` block.
    *   **Set** the variable name to `timer_count` and the value to 10.

**B. Countdown Phase**
2.  **Create Main Loop**:
    *   From **Loops**, drag the `pico_forever` block.
3.  **Check Counter Status**:
    *   Inside the loop, from **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If `timer_count` > 0.
4.  **Decrement Logic**:
    *   Inside the **If** block:
    *   **Print** "Time Remaining: ", `timer_count`.
    *   **Set** `timer_count` = `timer_count` - 1.
    *   From **Time**, **Wait** 1 second.

**C. Trigger Phase**
5.  **Finish Signal**:
    *   Inside the **Else** block (when count is 0):
    *   **Print** "Ding! Time is up!".
    *   **Wait** 0.1 seconds (to prevent constant printing).

### 8. Execution Flow
1.  **Start**: The Pico sets the clock to 10 seconds.
2.  **Loop**: The Pico checks if time is left.
3.  **Tick**: Every second, it subtracts 1 and tells the user the update.
4.  **Stop**: When it hits 0, it skips the subtraction and prints the final alarm message.

### 9. Generated Code
```python
import machine
import utime

# Setup
timer_count = 10

while True:
    if timer_count > 0:
        print("Time Remaining: " + str(timer_count))
        timer_count = timer_count - 1
        utime.sleep(1)
    else:
        print("Ding! Time is up!")
        utime.sleep(1) # Wait after finishing
```

### 10. Common Mistakes
*   **Wait Position**: If you put the `wait` outside the `if` block, the "Ding" message will only appear once per second, but the code might print it multiple times if you don't use the else block correctly.
*   **Negative Count**: If you don't check for `> 0`, the timer will count 0, -1, -2... infinitely.

### 11. Try This Next
*   **Longer Timer**: Change the initial value to 60 for a 1-minute timer.
*   **Visual Alert**: Add an LED that flashes on every "Tick".

---

## Project 0182: Blinking Kitchen Timer

### 1. Learning Objective
Explore persistent alert states. Learn how to transition from a countdown "Operation State" into a continuous "Alarm State" that requires user interaction (a button press) to dismiss.

### 2. Concepts Introduced
*   **Persistent Alarm State**: Staying in a mode until an external event occurs.
*   **Dismissal Logic**: using a digital input to "acknowledge" and clear an alert.
*   **Rapid Toggling**: Using fast visual blinks to represent urgency.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Red LED + Resistor
*   1 Button + Resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Alarm LED** | GP15 | Flashes when timer hits 0 |
| **Dismiss Button** | GP14 | Press to stop the flashing |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **current_time**: The countdown value.
*   **alarm_on**: A Boolean flag (True/False) to track if we should be flashing.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Values**:
    *   **Set** `current_time` = 5.
    *   **Set** `alarm_on` = False.

**B. Countdown Phase**
2.  **Timer Loop**:
    *   From **Loops**, drag `pico_forever`.
    *   If `current_time` > 0:
        *   **Print** `current_time`.
        *   **Set** `current_time` = `current_time` - 1.
        *   **Wait** 1 second.
    *   Else (If 0 reached):
        *   **Set** `alarm_on` = True.

**C. Alarm and Dismiss Phase**
3.  **Flash and Check**:
    *   If `alarm_on` == True:
        *   **Set** GP15 (LED) -> HIGH, **Wait** 0.1s, **Set** GP15 -> LOW, **Wait** 0.1s.
        *   If **Smart IO** `pico_gpio_read` GP14 is True (Button Pressed):
            *   **Set** `alarm_on` = False.
            *   **Set** `current_time` = 5 (Reset for next round).
            *   **Print** "Alarm Dismissed.".

### 8. Execution Flow
1.  **Count**: The Pico counts down from 5 to 0.
2.  **Trigger**: Once it hits 0, it flips the `alarm_on` switch to True.
3.  **Urgency**: The Pico ignores the timer and starts flashing the Red LED very fast.
4.  **Action**: The user presses the button.
5.  **Reset**: The flashing stops, and the timer resets to 5, ready to be used again.

### 9. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

timer = 5
alarm = False

while True:
    if timer > 0:
        print("Counting: " + str(timer))
        timer -= 1
        time.sleep(1)
        if timer == 0:
            alarm = True
            
    if alarm:
        # Rapid Flash
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)
        
        # Check Dismissal
        if btn.value() == 1:
            alarm = False
            timer = 5 # Optional reset
            print("Dismissed.")
            time.sleep(0.5)
```

### 10. Common Mistakes
*   **Blocking Flash**: If the flash `wait` is too long, the button press might be "missed" while the loop is sleeping. Keep the flash intervals short.
*   **No Flag**: If you don't use the `alarm_on` variable, the LED might only flash once and then stop.

### 11. Try This Next
*   **Beep Signal**: Add a Buzzer that chirps along with the LED.
*   **Snooze**: Make the button pause the alarm for 30 seconds before it starts flashing again.

---

## Project 0183: Manual Kitchen Timer Control

### 1. Learning Objective
Manage separate "Setup" and "Run" phases in a program. Learn how to use buttons to configure a variable (adding minutes) before initiating the main operation (counting down).

### 2. Concepts Introduced
*   **Mode Switching**: Transitioning from a configuration mode to an operational mode.
*   **Accumulation Logic**: Adding chunks of time (60 seconds) with each button press.
*   **Start/Stop Triggers**: Using a dedicated button to launch a sequence.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Add, Start)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A (Add)** | GP14 | Adds 60 seconds each click |
| **Button B (Start)** | GP13 | Begins the countdown |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (addition, subtraction)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **total_sec**: The counter value being configured.
*   **is_running**: State flag.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialize Values**:
    *   **Set** `total_sec` = 0.
    *   **Set** `is_running` = False.

**B. Configuration Phase (Loop)**
2.  **Monitor Buttons**:
    *   From **Loops**, drag `pico_forever`.
    *   If **Button A** (GP14) is Pressed AND `is_running` is False:
        *   **Set** `total_sec` = `total_sec` + 60.
        *   **Print** "Timer set to: ", `total_sec`, " seconds".
        *   **Wait** 0.3s (Debounce).
    
    *   If **Button B** (GP13) is Pressed:
        *   **Set** `is_running` = True.
        *   **Print** "COUNTDOWN STARTING!".

**C. Operation Phase**
3.  **Run Countdown**:
    *   If `is_running` is True and `total_sec` > 0:
        *   **Set** `total_sec` = `total_sec` - 1.
        *   **Print** "Seconds Left: ", `total_sec`.
        *   **Wait** 1 second.
    *   If `total_sec` == 0 and `is_running` is True:
        *   **Print** "TIMER FINISHED".
        *   **Set** `is_running` = False.

### 8. Execution Flow
1.  **Collect**: The user taps Button A three times. The Pico adds 60 + 60 + 60 = 180 seconds.
2.  **Confirm**: The Pico reports the current setting after each tap.
3.  **Launch**: The user presses Button B. The configuration stops.
4.  **Act**: The Pico counts down from 180 until it hits zero.
5.  **Finish**: The system resets to a ready state for a new kitchen task.

### 9. Generated Code
```python
from machine import Pin
import time

btn_add = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_start = Pin(13, Pin.IN, Pin.PULL_DOWN)

total_sec = 0
running = False

while True:
    # Setup Phase
    if not running:
        if btn_add.value():
            total_sec += 60
            print("Time +1 min: " + str(total_sec//60) + "m")
            time.sleep(0.3)
            
        if btn_start.value() and total_sec > 0:
            running = True
            print("STARTING")
            time.sleep(0.3)
            
    # Run Phase
    if running:
        if total_sec > 0:
            print("Time Left: " + str(total_sec) + "s")
            total_sec -= 1
            time.sleep(1)
        else:
            print("!!! DONE !!!")
            running = False
            
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **Zero Start**: If you press Start when the timer is at 0, nothing will happen. Add a check `if total_sec > 0` before starting.
*   **Multiple Starts**: If you don't use the `running` flag correctly, pressing Start twice might mess up the countdown calculation.

### 11. Try This Next
*   **Subtract Button**: Add Button C to remove 10 seconds if you made a mistake.
*   **Stop Button**: Make Button B act as a "Cancel" if pressed while the timer is already running.

---
