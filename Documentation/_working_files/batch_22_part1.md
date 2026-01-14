
# BATCH 22: Button Logic 2 (Projects 0211-0220)

## 1. Project 0211: Introduction to Button Logic

### 2. Learning Objective
Explore real-time input polling. Learn how to monitor the state of a digital input pin and provide immediate textual feedback to the console, observing how microcontrollers execute code thousands of times per second.

### 3. Concepts Introduced
*   **Digital Input Polling**: Continuously reading a pin to detect changes.
*   **Serial Terminal Communication**: Sending text from the Pico to the computer screen.
*   **Logical States**: understanding how "High" (1) translates to the word "Pressed".

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Input Button** | GP14 | Monitored via Serial console |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_text_print`** (print to console)

### 7. Variables
*   **None**: this project uses direct conditional checks.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Check Input**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).

**B. Feedback Phase**
3.  **Handle Pressed State**:
    *   Inside the **If** block:
    *   From **Smart IO**, drag `pico_text_print` and set text to "Pressed".
4.  **Handle Released State**:
    *   Inside the **Else** block:
    *   From **Smart IO**, drag `pico_text_print` and set text to "Released".

**C. Timing Phase**
5.  **Pace the Output**:
    *   From **Time**, **Wait** 0.1 seconds (to prevent the console from scrolling too fast to read).

### 9. Execution Flow
1.  **Read**: The Pico checks if the button is sending a signal to GP14.
2.  **Decide**: If the button is pushed, the code path follows the "If" branch.
3.  **Command**: The Pico sends the characters "P-r-e-s-s-e-d" back up the USB cable.
4.  **Wait**: The Pico idles for 100 milliseconds to give the user time to read.
5.  **Result**: A real-time log of the user's physical interaction with the hardware.

### 10. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        print("Pressed")
    else:
        print("Released")
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Pull-Down**: If the button isn't grounded when released, the pin will "float" and print "Pressed" randomly.
*   **No Wait**: Without a wait block, the Pico will print "Released" 10,000 times per second, which can crash some basic terminal programs.

### 12. Try This Next
*   **Change Text**: make it say "Button Active" and "Button Quiet".
*   **LED Sync**: turn on an LED when it prints "Pressed".

---

## 1. Project 0212: Blinking Button Logic

### 2. Learning Objective
Explore Edge Detection (One-Shot Logic). Learn how to write code that detects the *moment* a button is pressed and performs an action exactly once, even if the button is held down for a long time.

### 3. Concepts Introduced
*   **Rising Edge Detection**: triggering an event specifically when a signal changes from LOW to HIGH.
*   **Blocking Wait-Until**: pausing code execution until a physical condition is met.
*   **Input Debouncing (Software)**: ignoring accidental fast vibrations from a mechanical switch.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + Resistor
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Trigger Button** | GP14 | Single-activation switch |
| **Flash LED** | GP15 | Blinks once per press |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `pico_wait_until`** (wait until Pin is HIGH)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: the sequential flow handles the state logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare LED**: **Set** GP15 -> LOW (0).

**B. Capture Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Wait for Finger**:
    *   Inside the loop, from **Loops**, drag `pico_wait_until`.
    *   **Condition**: Pin GP14 is HIGH (1).

**C. Execution Phase**
4.  **Perform Single Action**:
    *   From **Smart IO**, **Set** GP15 -> HIGH (1).
    *   From **Time**, **Wait** 0.1 seconds.
    *   **Set** GP15 -> LOW (0).

**D. Release Protection Phase**
5.  **Wait for Release**:
    *   From **Loops**, drag `pico_wait_until`.
    *   **Condition**: Pin GP14 is LOW (0).
    *   *Note: This prevents the loop from restarting while your finger is still on the button.*

### 9. Execution Flow
1.  **Halt**: The Pico stops at Step 3, doing nothing but watching the button.
2.  **Trigger**: You press the button. The Pico moves to Step 4.
3.  **Action**: The LED flashes for 100ms.
4.  **Halt Again**: The Pico stops at Step 5. Even if you hold the button for 10 minutes, it won't move.
5.  **Finish**: You let go. The Pico finishes the loop and goes back to Step 1, ready for the next press.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    # 1. Wait for press
    while btn.value() == 0:
        pass
        
    # 2. Action
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    
    # 3. Wait for release
    while btn.value() == 1:
        pass
```

### 11. Common Mistakes
*   **Missing Release Wait**: If you forget Step 5, the LED will blink continuously as long as you hold the button, which defeats "One-Shot" logic.
*   **Wait in Loop**: If you use a `sleep` instead of a `wait_until`, you might miss the button press if it's very quick.

### 12. Try This Next
*   **Double Blink**: Make the LED blink twice on a single press.
*   **Toggle Mode**: Create a system where one press turns the LED ON, and the NEXT press turns it OFF.

---

## 1. Project 0213: Manual Button Logic Control

### 2. Learning Objective
Explore Boolean logic gates (The AND Gate). Learn how to combine multiple input conditions into a single decision, requiring two physical events to happen concurrently for a result.

### 3. Concepts Introduced
*   **AND Logic**: An output is only HIGH if all inputs are HIGH.
*   **Condition Combining**: checking multiple pin values in one step.
*   **Redundancy**: Using two buttons as a "Safety" mechanism (e.g., preventing accidental motor starts).

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (A and B)
*   1 LED + resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Primary trigger |
| **Button B** | GP13 | Safety interlock |
| **Safety LED** | GP15 | Active only on A + B |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Logic, drag `logic_operation`** (AND)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)

### 7. Variables
*   **None**: this is a stateless combinational logic project.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Evaluate Safety**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**:
        *   From **Logic**, drag the `[ ] AND [ ]` block.
        *   Into the first slot: **Smart IO** `pico_gpio_read` GP14.
        *   Into the second slot: **Smart IO** `pico_gpio_read` GP13.

**B. Execution Phase**
3.  **Active State (Both Pressed)**:
    *   Inside the **If** block: **Set** GP15 -> HIGH (1).
4.  **Inactive State (Anything else)**:
    *   Inside the **Else** block: **Set** GP15 -> LOW (0).

### 9. Execution Flow
1.  **Case 1 (A only)**: Pico reads 1 and 0. AND logic says "No". LED OFF.
2.  **Case 2 (B only)**: Pico reads 0 and 1. AND logic says "No". LED OFF.
3.  **Case 3 (None)**: Pico reads 0 and 0. AND logic says "No". LED OFF.
4.  **Case 4 (Both)**: Pico reads 1 and 1. AND logic says "YES". LED turns ON.
5.  **Result**: A hardware "Interlock" that requires both hands to be occupied with buttons before the light activates.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn_a.value() == 1 and btn_b.value() == 1:
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.01) # Fast reaction
```

### 11. Common Mistakes
*   **OR vs AND**: using an OR block will make the LED turn on if *either* button is pressed, which is the opposite of the goal.
*   **Button Wiring**: If one button isn't connected to 3.3V, the AND condition can never be met.

### 12. Try This Next
*   **OR Gate**: Replace "AND" with "OR" so either button can turn the light on (like two light switches for one room).
*   **XOR Gate**: Try to make it so the LED turns on IF they are different (One is pressed, the other is not).

---

## 1. Project 0214: Button Logic Sequences

### 2. Learning Objective
Explore temporal validation (The Combo Lock). Learn how to implement a state sequence where inputs must be received in a specific order (A -> A -> B) over time to "Unlock" a success state.

### 3. Concepts Introduced
*   **Sequential Dependencies**: events that only matter if a previous event happened first.
*   **State Reset**: failing the sequence if the wrong input is detected mid-way.
*   **User Feedback (Win/Loss)**: using different colored LEDs to signal the result.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (A and B)
*   2 LEDs (Red and Green)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Sequence part 1 & 2 |
| **Button B** | GP13 | Sequence part 3 |
| **Green LED** | GP15 | Success |
| **Red LED** | GP12 | Failure |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `pico_wait_until`** (waiting for pulse)
*   **from Logic, drag `controls_if`** (validating each step)
*   **from Smart IO, drag `pico_gpio_write`** (signaling LEDs)

### 7. Variables
*   **None**: the sequential execution path acts as the memory.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear Status**: **Set** GP15 & GP12 -> LOW (0).

**B. Phase 1 (First A)**
2.  **Wait for Start**:
    *   **Wait until** GP14 or GP13 are HIGH.
    *   If GP13 was pressed (Button B): **Set** Red (GP12) ON for 1s, then **Restart**.
    *   If GP14 was pressed (Button A): **Continue** to next step.
    *   **Wait until** buttons are released.

**C. Phase 2 (Second A)**
3.  **Wait for Repeat**:
    *   **Wait until** GP14 or GP13 are HIGH.
    *   If GP13 was pressed (Button B): **Show Red**, then **Restart**.
    *   If GP14 was pressed (Button A): **Continue**.
    *   **Wait until** released.

**D. Phase 3 (Final B)**
4.  **Wait for Finish**:
    *   **Wait until** GP14 or GP13 are HIGH.
    *   If GP14 was pressed (Button A): **Show Red**, then **Restart**.
    *   If GP13 was pressed (Button B): **ACHIEVED SUCCESS**.

**E. Reward Phase**
5.  **Success Signal**:
    *   **Set** Green (GP15) -> HIGH. **Wait** 2s. **Set** LOW.

### 9. Execution Flow
1.  **A-A-B**: Correct! The Pico moves through all 3 "Wait" gates and lights the Green LED.
2.  **A-B-A**: Mistake! At the second gate, it expected A but got B. It triggers the Red LED and sends you back to the start.
3.  **Logic**: The sequence is verified over time because the Pico follows a top-to-bottom script.

### 10. Generated Code
```python
import machine
import utime

# Setup
btn_a = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn_b = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
green = machine.Pin(15, machine.Pin.OUT)
red = machine.Pin(12, machine.Pin.OUT)

def wait_for_input():
    while True:
        if btn_a.value(): return "A"
        if btn_b.value(): return "B"
        utime.sleep(0.01)

def wait_for_release():
    while btn_a.value() or btn_b.value():
        utime.sleep(0.01)

while True:
    red.value(0); green.value(0)
    print("Enter Code: A - A - B")
    
    # Step 1
    if wait_for_input() == "A":
        wait_for_release()
        # Step 2
        if wait_for_input() == "A":
            wait_for_release()
            # Step 3
            if wait_for_input() == "B":
                print("UNLOCKED")
                green.value(1); utime.sleep(2)
                continue
    
    # If any step failed
    print("WRONG CODE")
    red.value(1); utime.sleep(1)
    wait_for_release()
```

### 11. Common Mistakes
*   **Missing Releaser**: Without `wait_for_release`, the Pico is so fast it will register one long press of Button A as all two "A" parts of the code instantly.
*   **Infinite Red**: If you don't turn the Red LED off at the start of the loop, it will stay on forever after the first mistake.

### 12. Try This Next
*   **Change Code**: Modify the IF statements to require B-A-B-A.
*   **Buzzer Entry**: play a short "beep" sound every time a button is pressed so you know the Pico heard you.

---

## 1. Project 0215: Interactive Button Logic

### 2. Learning Objective
Explore accumulation and absolute reset. Learn how to use one input to increment a numerical variable (The Counter) and a separate dedicated input to overwrite that variable back to zero (The Clear Button).

### 3. Concepts Introduced
*   **Variable Accumulation**: Adding to a stored value (`count = count + 1`).
*   **Priority Overwrite**: Resetting a value regardless of its previous state.
*   **User Visualization**: Printing the running total to the Serial monitor.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Add and Reset)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Btn Add (+)** | GP14 | Increments count |
| **Btn Reset (0)** | GP13 | Clears count |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking buttons)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Variables, drag `variables_get`** (read variable)
*   **from Math, drag `math_arithmetic`** (addition)
*   **from Smart IO, drag `pico_text_print`** (print)

### 7. Variables
*   **total_count**: Integer tracking current presses.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start Point**: From **Variables**, **Set** `total_count` = 0.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Handle Accumulation**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `total_count` = `total_count` + 1.
        *   **Print** "Added! Current Total: ", `total_count`.
        *   **Wait** 0.3s (Debounce).
4.  **Handle Reset**:
    *   If **Button** GP13 is Pressed:
        *   **Set** `total_count` = 0.
        *   **Print** "COUNTER RESET TO ZERO".
        *   **Wait** 0.3s.

### 9. Execution Flow
1.  **Click**: You hit the Add button. The Pico adds 1 to the current 0.
2.  **Log**: The screen says "Total: 1".
3.  **Click-Click**: You hit it twice more. Screen says "Total: 2", then "Total: 3".
4.  **Clear**: You hit the Reset button. The Pico immediately destroys the number 3 and replaces it with 0.
5.  **Result**: An interactive scoreboard or tally counter.

### 10. Generated Code
```python
from machine import Pin
import time

btn_add = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_clr = Pin(13, Pin.IN, Pin.PULL_DOWN)

total_count = 0

print("Ready. Press GP14 to count, GP13 to reset.")

while True:
    # Increment
    if btn_add.value() == 1:
        total_count = total_count + 1
        print("Count: " + str(total_count))
        time.sleep(0.3) # Debounce
        
    # Reset
    if btn_clr.value() == 1:
        total_count = 0
        print("--- RESET ---")
        time.sleep(0.3) # Debounce
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Exponential Addition**: if you forget the `wait` (debounce) block, one quick finger tap will count as 5 or 6 presses.
*   **Wrong Operator**: Ensure you use `count + 1` and not just `set count to 1`.

### 12. Try This Next
*   **Countdown**: add a third button on GP12 that subtracts 1 from the count.
*   **Score Target**: make an LED blink when the count reaches specifically "10".

---
