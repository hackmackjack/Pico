
# BATCH 18: Stopwatch 1 (Projects 0171-0180)

## Project 0171: Introduction to Stopwatch

### 1. Learning Objective
Understand the fundamentals of tracking time using variables and loops. Learn how to create a simple seconds counter that increments at a fixed interval.

### 2. Concepts Introduced
*   **Variable Incrementing**: Using `variable = variable + 1` to track elapsed time.
*   **Loop Intervals**: Using delays to control the "tick" speed of a clock.
*   **Console Logging**: Outputting time data to the serial monitor.

### 3. Hardware Required
*   Raspberry Pi Pico

### 4. Wiring / Interfaces
*   **Internal**: Uses USB Serial for console output. No external components needed.

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Math, drag `math_arithmetic`** (addition block)
*   **from Text, drag `text_print`** (print to console)
*   **from Time, drag `pico_wait`** (wait for ... seconds)

### 6. Variables
*   **time_seconds**: An integer that stores how many seconds have passed.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Create Time Variable**:
    *   From **Variables**, drag the `variables_set` block.
    *   **Set** the variable name to `time_seconds` and the value to 0.

**B. Counting Phase**
2.  **Create Main Loop**:
    *   From **Loops**, drag the `pico_forever` block.
3.  **Increment Time**:
    *   Inside the loop, drag `variables_set`.
    *   Snap the `math_arithmetic` block into the value slot.
    *   **Set** calculation to `time_seconds + 1`.

**C. Output and Timing Phase**
4.  **Display Current Time**:
    *   From **Text**, drag the `text_print` block and snap it below increment.
    *   From **Text**, drag a text string block and **Set** text to "Time: ".
    *   From **Variables**, drag the `time_seconds` block and snap it into the second slot of the print block.
    *   Drag another text string block and **Set** text to " seconds".
5.  **Set 1-Second Delay**:
    *   From **Time**, drag the `pico_wait` block and snap it at the bottom of the loop.
    *   **Set** wait time to 1 second.

### 8. Execution Flow
1.  **Start**: The Pico initializes the counter to zero.
2.  **Loop**: The code adds 1 to the counter every cycle.
3.  **Log**: The result is sent to the computer screen.
4.  **Pace**: The 1-second delay ensures the counter matches real-world seconds.

### 9. Generated Code
```python
import machine
import utime

# Initialize counter
time_seconds = 0

while True:
    # Increment counter
    time_seconds = time_seconds + 1
    
    # Print to console
    print("Time: " + str(time_seconds) + " seconds")
    
    # Wait for 1 second
    utime.sleep(1)
```

### 10. Common Mistakes
*   **Forgetting the Delay**: Without `sleep(1)`, the Pico will count millions of times per second.
*   **Zeroing Inside the Loop**: If you initialize `time = 0` inside the loop, it will always print "1" and never increase.

### 11. Try This Next
*   **Minutes Counter**: Add logic to print "X minutes, Y seconds".
*   **Faster Tick**: Change the wait to 0.1 seconds and increment by 0.1 to see sub-second tracking.

---

## Project 0172: Blinking Stopwatch

### 1. Learning Objective
Combine time-tracking logic with visual feedback. Learn how to sync an LED toggle with a mathematical counter to create a "Visual Tick" or Metronome effect.

### 2. Concepts Introduced
*   **Visual Synchronization**: Matching hardware output (LED) with a software loop.
*   **State Toggling**: Alternating between ON and OFF at regular intervals.
*   **Multi-Step Delays**: Breaking a single second into segments (0.5s ON, 0.5s OFF).

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 LED
*   1x 220-330 Ohm resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Anode (+)** | GP15 | Connect via resistor |
| **LED Cathode (-)** | GND | Ground |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Time, drag `pico_wait`** (wait for ... seconds)
*   **from Text, drag `text_print`** (print to console)

### 6. Variables
*   **seconds**: Tracks total elapsed time.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware and Variable**:
    *   **Set** GP15 (LED) to LOW.
    *   **Set** `seconds` = 0.

**B. Tick Phase (ON)**
2.  **Start Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Increment and Light Up**:
    *   **Set** `seconds` = `seconds` + 1.
    *   **Set** GP15 (LED) -> HIGH.
4.  **Wait Half Second**:
    *   From **Time**, **Wait** 0.5 seconds.

**C. Tick Phase (OFF)**
5.  **Turn Off and Log**:
    *   **Set** GP15 (LED) -> LOW.
    *   **Print** "Time: ", `seconds`.
6.  **Wait Half Second**:
    *   **Wait** 0.5 seconds.

### 8. Execution Flow
1.  **Iteration**: Every loop takes exactly 1.0 seconds (0.5s + 0.5s).
2.  **Display**: The LED stays on for half the second and off for half the second.
3.  **Console**: The count updates every time the LED turns off.
4.  **Result**: The user can see a rhythmic blink that perfectly matches the seconds counter.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware setup
led = Pin(15, Pin.OUT)
seconds = 0

while True:
    # 1 second = 0.5s ON + 0.5s OFF
    seconds += 1
    
    # Start Tick
    led.value(1)
    time.sleep(0.5)
    
    # End Tick
    led.value(0)
    print("Time: " + str(seconds))
    time.sleep(0.5)
```

### 10. Common Mistakes
*   **Timing Mismatch**: If you wait 1s in both phases, your "1-second" counter actually takes 2 seconds to loop.
*   **Floating Output**: ensure you print specifically when the second is "complete".

### 11. Try This Next
*   **Heartbeat Tick**: Change timing to 0.1s ON and 0.9s OFF for a short, crisp pulse.
*   **Double Blink**: Make the LED blink twice per second while still counting single seconds.

---

## Project 0173: Manual Stopwatch Control

### 1. Learning Objective
Implement execution flow control (Start/Stop). Learn how to use external inputs to trigger and break out of a loop, allowing for a user-controlled timer.

### 2. Concepts Introduced
*   **Conditional Loops**: running a timer only when a "Running" flag is true.
*   **Breaking Loops**: Terminating an action based on an input event.
*   **State Switching**: Using two buttons to change the mode of operation.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Start and Stop)
*   2x 10k Ohm pull-down resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Start** | GP14 | Start counting |
| **Button Stop** | GP13 | Stop and reset/finish |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **counting**: Boolean (True/False) that determines if the clock is running.
*   **elapsed**: The current time value.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   From **Variables**, **Set** `counting` = False.
    *   **Set** `elapsed` = 0.

**B. Control Phase**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Monitor Start Button**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH.
    *   **Action**: **Set** `counting` = True. **Print** "--- Stopwatch Started ---".
4.  **Monitor Stop Button**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP13 is HIGH.
    *   **Action**: **Set** `counting` = False. **Print** "Final Time: ", `elapsed`.

**C. Timer Phase**
5.  **Conditional Increment**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `counting` == True.
    *   **Inside**:
        *   **Set** `elapsed` = `elapsed` + 1.
        *   **Print** "Seconds: ", `elapsed`.
        *   **Wait** 1 second.

### 8. Execution Flow
1.  **Idle**: The program checks buttons but does nothing because `counting` is false.
2.  **Start**: Player presses GP14; `counting` switches to true.
3.  **Run**: The timer branch begins firing every second.
4.  **Stop**: Player presses GP13; `counting` switches to false, halting the incrementing logic.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware
btn_start = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_stop = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Variables
counting = False
elapsed = 0

print("Ready. Press Start (GP14) to begin.")

while True:
    # Check Buttons
    if btn_start.value():
        counting = True
        print("--- Stopwatch Started ---")
        
    if btn_stop.value():
        if counting:
            print("Final Time: " + str(elapsed))
        counting = False
        
    # Timer Logic
    if counting:
        elapsed += 1
        print("Seconds: " + str(elapsed))
        time.sleep(1)
    else:
        time.sleep(0.1) # Fast checking while idle
```

### 10. Common Mistakes
*   **Holding Both**: If both buttons are pressed, the code order matters (Usually Stop will immediately override Start).
*   **Double Start**: pressing Start multiple times while running may cause issues if you don't check `if not counting`.

### 11. Try This Next
*   **Reset on stop**: Make the timer go back to 0 every time it stops.
*   **Status LED**: Light up a Green LED when running and a Red LED when stopped.

---

## Project 0174: Stopwatch Sequences

### 1. Learning Objective
Learn about millisecond-precision timing. Understand "Response Triggering" by measuring the time between a visual cue (LED) and a physical action (Button Press).

### 2. Concepts Introduced
*   **Milliseconds (ms)**: Timing in 1/1000ths of a second for precision.
*   **Reaction Logic**: Waiting for a random event and capturing the delta.
*   **High-Resolution Counter**: Incrementing at 0.01s (10ms) intervals.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 LED + resistor
*   1 Button + resistor

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Cue LED** | GP15 | Wait for this to turn ON |
| **Input Button** | GP14 | Press as fast as you can |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable to ...)
*   **from Actuators, drag `pico_gpio_write`** (set Pin control)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **reaction_time**: The counter in milliseconds.
*   **waiting**: State flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep Game**:
    *   **Set** GP15 (LED) -> LOW.
    *   **Print** "Reaction Game: Wait for the LIGHT...".

**B. Random Cue Phase**
2.  **Add Random Delay**:
    *   From **Time**, **Wait** random 2 to 5 seconds.
3.  **Give the Signal**:
    *   **Set** GP15 (LED) -> HIGH.
    *   **Set** `reaction_time` = 0.

**C. Precision Count Phase**
4.  **Count fast**:
    *   From **Loops**, drag a nested loop or repeat-until.
    *   **Condition**: Repeat until **Smart IO** `pico_gpio_read` GP14 is True.
    *   **Contents**:
        *   **Set** `reaction_time` = `reaction_time` + 10.
        *   **Wait** 0.01 seconds.

**D. Result Phase**
5.  **Display Performance**:
    *   **Set** GP15 (LED) -> LOW.
    *   **Print** "Reaction Time: ", `reaction_time`, " ms".
    *   **Wait** 3 seconds before next round.

### 8. Execution Flow
1.  **Wait**: The Pico sits in the dark for a random amount of time.
2.  **Flash**: The LED lights up; the timer starts "ticking" every 10 milliseconds instantly.
3.  **Action**: The user hits the button as fast as possible.
4.  **Freeze**: The loop breaks, and the exact count is displayed.
5.  **Score**: A good reaction is below 250ms!

### 9. Generated Code
```python
from machine import Pin
import time
import random

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(0)
    print("READY...")
    
    # Random wait 2-5s
    time.sleep(random.uniform(2, 5))
    
    # GO!
    led.value(1)
    start_time = time.ticks_ms()
    
    # Wait for press
    while btn.value() == 0:
        pass
        
    end_time = time.ticks_ms()
    led.value(0)
    
    # Calculate difference
    diff = time.ticks_diff(end_time, start_time)
    print("REACTION: " + str(diff) + "ms")
    
    time.sleep(3)
```

### 10. Common Mistakes
*   **Anticipation**: If the user holds the button before the light, the code might show "0ms". You should check if the button is already down at the start.
*   **Loop Speed**: if you wait 1s in the measurement loop, the game won't work. It must be very fast.

### 11. Try This Next
*   **Cheat Prevention**: Print "CHEATER!" if the button is pressed before the light flashes.
*   **Speed Zones**: Print "EXPERT" if < 200ms, "AVERAGE" if 200-400ms, and "SLOW" if > 400ms.

---
