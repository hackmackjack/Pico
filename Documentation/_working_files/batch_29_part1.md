
# BATCH 29: Counting Machine 2 (Projects 0281-0290)

## 1. Project 0281: Introduction to Counting Machine

### 2. Learning Objective
Explore parity visualization (The Modulus Light). Learn how to use the "Remainder" (Modulus %) operator to distinguish between Even and Odd numbers, creating a binary visual feedback system for a sequential counter.

### 3. Concepts Introduced
*   **Modulo Arithmetic**: Calculating the remainder after division (e.g. `5 % 2 = 1`).
*   **Parity Detection**: using math to identify "Evens" (0 remainder) vs "Odds" (1 remainder).
*   **Visual Patterns**: creating a blinking sequence where the light is only active on specific steps.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED
*   1 Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Count Button** | GP14 | Increments variable |
| **Parity LED** | GP15 | Lights up on EVENS |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (storing count)
*   **from Math, drag `math_modulo`** (checking remainder)
*   **from Logic, drag `controls_if`** (evaluating parity)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)

### 7. Variables
*   **current_val**: Integer tracking total button presses.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Counters**: **Set** `current_val` = 0.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Handle Inputs**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `current_val` = `current_val` + 1.
        *   **Print** "Step: ", `current_val`.
        *   **Wait** 0.3s (Debounce).

**C. Math Phase (Parity)**
4.  **Evaluate Evenness**:
    *   If **Math** (`current_val` % 2) == 0:
        *   **Set** LED (GP15) -> HIGH (Even number).
    *   Else:
        *   **Set** LED -> LOW (Odd number).

### 9. Execution Flow
1.  **Start**: Value is 0. 0 is even. Light is ON.
2.  **First Press**: Value is 1. 1 divided by 2 has a remainder of 1. Light turns OFF.
3.  **Second Press**: Value is 2. 2 divided by 2 has a remainder of 0. Light turns ON.
4.  **Result**: The LED blinks every other time you press the button, visualizing the odd/even pattern.
5.  **Outcome**: Understanding how computers use simple math to categorize data.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

count = 0

while True:
    if btn.value() == 1:
        count += 1
        print("Count: " + str(count))
        
        # Check Parity (Even/Odd)
        if count % 2 == 0:
            led.value(1)
            print("Status: EVEN")
        else:
            led.value(0)
            print("Status: ODD")
            
        time.sleep(0.3) # Wait for release
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Variable Scope**: Ensure your `count` variable is defined *above* the loop, otherwise it will reset to 0 every time the loop repeats.

### 12. Try This Next
*   **Every Third**: change the math to `% 3`. Now the light will only turn on for 3, 6, 9...
*   **Double Flash**: make the LED flash twice for even numbers and stay off for odd numbers.

---

## 1. Project 0282: Blinking Counting Machine

### 2. Learning Objective
Explore milestone markers (The Decade Counter). Learn how to implement a base-10 counting logic where a visual "Mark" (Blue LED Flash) occurs at every multiple of ten, simulating industrial counters that track batches.

### 3. Concepts Introduced
*   **Milestone Logic**: triggering a special event when a specific threshold (e.g. 10) is hit.
*   **Resetting Patterns**: maintaining a primary count while executing secondary alerts.
*   **Batch Tracking**: grouped counting logic.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Blue LED + Resistor
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Product Btn** | GP14 | Each "Product" made |
| **Decade LED (B)** | GP15 | Flashes every 10 items |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking count)
*   **from Math, drag `math_modulo`** (checking for 10)
*   **from Logic, drag `controls_if`** (evaluating milestone)
*   **from Smart IO, drag `pico_gpio_write`** (flashing)

### 7. Variables
*   **batch_count**: integer tracking total inputs.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Capture Action**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `batch_count` = `batch_count` + 1.
        *   **Print** "Item #", `batch_count`.

**B. Milestone Phase**
3.  **Check for Decade**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Math** (`batch_count` % 10) == 0 AND `batch_count` > 0.
4.  **Signal Decade**:
    *   Inside the **If** block:
    *   **Set** Blue LED (GP15) -> HIGH. **Wait** 0.5s. **Set** LOW.
    *   **Print** "DECADE REACHED! BATCH COMPLETE.".

**C. Wait for release**:
5.  **Debounce**: **Wait** 0.3s to prevent skip-counting.

### 9. Execution Flow
1.  **Input**: You press the button 9 times. The blue LED stays OFF.
2.  **Action**: You press for the 10th time.
3.  **Logic**: `10 % 10` is exactly zero. The Pico triggers the milestone.
4.  **Reaction**: The Blue LED flashes brightly for half a second.
5.  **Resume**: At 11, it goes back to dark until 20.
6.  **Result**: An automated factory counter that signals when a "Pack of 10" is finished.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

count = 0

while True:
    if btn.value() == 1:
        count += 1
        print("Tracking: " + str(count))
        
        # Check for decade (10, 20, 30...)
        if count % 10 == 0:
            print("--- DECADE REACHED ---")
            # Blink pattern
            for _ in range(3):
                led.value(1); time.sleep(0.1)
                led.value(0); time.sleep(0.1)
        
        time.sleep(0.3) # Debounce
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Starting at Zero**: Since `0 % 10` is 0, the light might flash the moment you turn the Pico on. Always check `if count > 0` before running the modulo logic.

### 12. Try This Next
*   **Triple Signal**: Add a Red LED for Every 5 items and a Blue LED for Every 10.
*   **Buzzer Chirp**: add a short beep for every 10th item for audible confirmation.

---

## 1. Project 0283: Manual Counting Machine Control

### 2. Learning Objective
Explore configurable goal-seeking (The Target Counter). Learn how to use a Potentiometer as a "Hardware Variable" to set a dynamic target, comparing your manual count to this live goal to trigger a victory event.

### 3. Concepts Introduced
*   **Dynamic Goal Setting**: Using analog input to change the software's "Winning" condition.
*   **Real-time Comparison**: `current_count >= target_goal`.
*   **Interactive Fanfare**: using a multi-note sequence to reward user completion.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Potentiometer (Dial)
*   1 Pushbutton
*   1 Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Target Dial** | GP26 (ADC0) | Sets the goal (0-100) |
| **Count Button** | GP14 | Manual input |
| **Siren/Alert** | GP15 | Victory fanfare |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read Target)
*   **from Logic, drag `controls_if`** (evaluating goal)
*   **from Math, drag `math_map`** (converting 65535 to 100)
*   **from Actuators, drag `pico_buzzer_pitch`** (fanfare)

### 7. Variables
*   **target**: the goal set by the user.
*   **current**: the progress made so far.

### 8. Step-by-Step Guide

**A. Setup Phase**
1.  **Set Target**:
    *   **Set** `target` = **Math** map (**Sensors** `pico_analog_read` GP26) from 0-65535 to 0-100.
    *   **Print** "Today's Goal: ", `target`, " clicks.".

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Handle Inputs**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `current` = `current` + 1.
        *   **Print** "Progress: ", `current`, " / ", `target`.
        *   **Wait** 0.3s.

**C. Victory Phase**
4.  **Evaluate Success**:
    *   If `current` >= `target`:
        *   **Print** "GOAL REACHED! CONGRATULATIONS!".
        *   **Call** `buzzer_fare`: [500Hz, 700Hz, 900Hz].
        *   **Set** `current` = 0 (Restart).

### 9. Execution Flow
1.  **Configure**: You turn the dial to the middle. The screen says "Goal: 50".
2.  **Effort**: You press the button 50 times.
3.  **Verification**: After the 50th click, the Pico sees that `current (50)` is equal to `target (50)`.
4.  **Reward**: The buzzer plays a high-pitched victory song.
5.  **Result**: An interactive fitness or task tracker where you can choose your own difficulty.

### 10. Generated Code
```python
import machine
import utime

pot = machine.ADC(machine.Pin(26))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bz = machine.PWM(machine.Pin(15))

count = 0

while True:
    # 1. Read Target (Map 0-65535 to 10-50 range for usability)
    target = int((pot.read_u16() / 65535) * 40) + 10
    
    # 2. Check Click
    if btn.value() == 1:
        count += 1
        print("Count: " + str(count) + " | Goal: " + str(target))
        
        # 3. Check Victory
        if count >= target:
            print("!!! GOAL REACHED !!!")
            # Fanfare
            for f in [600, 800, 1000]:
                bz.freq(f); bz.duty_u16(30000); utime.sleep(0.2)
            bz.duty_u16(0)
            count = 0 # Reset
            
        utime.sleep(0.3) # Debounce
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Variable Target**: If you let the target change *while* you are counting, you might "Win" just by turning the knob to a lower number. To fix this, you should lock the target once the counting starts!

### 12. Try This Next
*   **Lock Mode**: Add a second button. You must press it to "Submit" your goal before the counting button starts working.
*   **LED Bar**: if you have multiple LEDs, turn more on as you get closer to the target (Project 0284).

---

## 1. Project 0284: Counting Machine Sequences

### 2. Learning Objective
Explore data flow visualization (The Shift Register). Learn how to use a single counter variable to "Move" a lit LED through a bank of outputs, simulating how a computer processor shifts bits of information across its internal registers.

### 3. Concepts Introduced
*   **Shift Register Concepts**: data (the light) moving from position 1 to position 2 to position 3...
*   **Index-to-Pin Mapping**: using the `count` variable to select which specific GPIO to activate.
*   **End-of-Line Wrap**: resetting the count to 1 once the last LED is reached.

### 4. Hardware Required
*   Raspberry Pi Pico
*   8 LEDs (Any color)
*   1 Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1** | GP10 | First position |
| **LED 2** | GP11 | Second position |
| **...** | ... | ... |
| **LED 8** | GP17 | Last position |
| **Advance Btn**| GP14 | Move the bit |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking position)
*   **from Smart IO, drag `pico_gpio_write`** (complex addressing)
*   **from Time, drag `pico_wait`** (movement feel)

### 7. Variables
*   **ptr**: Integer (0-7) tracking the "Active Bit".

### 8. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialization**: **Set** `ptr` = 0.

**B. "Push" Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Wait for Push**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `ptr` = `ptr` + 1.
        *   **If** `ptr` > 7: **Set** `ptr` = 0 (Wrap back to start).

**C. Maintenance Phase (Display)**
4.  **Clear Old Bits**:
    *   **Turn OFF** all LEDs (GP10 to GP17).
5.  **Light New Bit**:
    *   **Set** Pin (`10 + ptr`) -> HIGH.
    *   **Wait** 0.3s.

### 9. Execution Flow
1.  **Start**: Only the first LED is lit.
2.  **Action**: You press the button.
3.  **Logic**: The pointer moves to "1".
4.  **Reaction**: LED 1 turns off and LED 2 turns on. The light "jumped" one space to the right.
5.  **Result**: You are physically moving a piece of "Electronic Data" through a wire-bus, just like a real computer.

### 10. Generated Code
```python
from machine import Pin
import time

# List of pins in order
led_pins = [10, 11, 12, 13, 14, 15, 16, 17] # Note: adjust if pins overlap
leds = [Pin(p, Pin.OUT) for p in led_pins]

btn = Pin(18, Pin.IN, Pin.PULL_DOWN)

pos = 0

while True:
    # 1. Update display
    for i in range(8):
        if i == pos:
            leds[i].value(1)
        else:
            leds[i].value(0)
            
    # 2. Check for shift
    if btn.value() == 1:
        pos += 1
        if pos > 7: pos = 0
        print("Bit Position: " + str(pos))
        time.sleep(0.3) # Debounce
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Ghosting**: if you don't turn OFF the old LED before turning on the new one, all the LEDs will eventually be ON. Ensure your code "Clears" the line every time.

### 12. Try This Next
*   **Auto-Shift**: make the LED move by itself every 1 second, and use the button to change the *direction* (Left-to-Right vs Right-to-Left).
*   **Trail**: leave the previous LED on at 10% brightness to create a "Tail" effect.

---

## 1. Project 0285: Interactive Counting Machine

### 2. Learning Objective
Explore cyclic event counting (The Manual RPM Counter). Learn how to use an analog sensor (Potentiometer) as a virtual "Rotary Switch" and implement a timer to measure how many cycles (knob rotations) a human can perform within a fixed 10-second window.

### 3. Concepts Introduced
*   **Crossing Detection**: counting an event only when an analog signal passes a midpoint (e.g. 32768).
*   **Hysteresis (Concept)**: Ensuring the signal "Goes back below" before counting a new rotation.
*   **Temporal Stress-test**: using a fixed countdown to create a high-speed challenge.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Potentiometer (Dial)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Rotation Switch** | GP26 (ADC0) | Input source |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Time, drag `pico_time_ms`** (window tracking)
*   **from Variables, drag `variables_set`** (tracking state)
*   **from Logic, drag `controls_if`** (evaluating crossing)
*   **from Sensors, drag `pico_analog_read`** (read dial)

### 7. Variables
*   **rev_count**: number of spins.
*   **is_high**: Boolean tracking if the knob is currently past the halfway mark.
*   **time_left**: remaining game time.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Board**: **Set** `rev_count` = 0.
2.  **Start Countdown**: **Start** 10-second timer.

**B. Monitoring Phase (The Spin)**
3.  **Detect Rising Edge**:
    *   If **ADC** GP26 > 40000 AND `is_high` is False:
        *   **Set** `is_high` = True.
        *   **Set** `rev_count` = `rev_count` + 1.
        *   **Print** "Spin detected! Total: ", `rev_count`.

**C. Reset Phase**
4.  **Detect Reset**:
    *   If **ADC** GP26 < 20000:
        *   **Set** `is_high` = False (Ready for next rotation).

**D. Completion Phase**
5.  **Finish**: 
    *   Once 10 seconds pass:
    *   **Print** "TIME UP! Your Score: ", `rev_count`, " spins.".
    *   **Calculate** RPM: (`rev_count` * 6).

### 9. Execution Flow
1.  **Action**: You start spinning the knob as fast as you can.
2.  **Logic**: Every time the metal wiper inside the knob passes 40,000, the Pico counts "One".
3.  **Security**: You must turn it back below 20,000 before it will count again. This prevents someone from "Wiggling" the knob at the 40k mark to cheat.
4.  **Result**: After 10 seconds, the Pico stops and tells you exactly how many full revolutions you completed.
5.  **Outcome**: A "Human RPM" meter that tests wrist speed.

### 10. Generated Code
```python
import machine
import utime

pot = machine.ADC(machine.Pin(26))
count = 0
is_high = False

print("READY... SPIN THE KNOB!")
utime.sleep(1)
print("GO! (10 Seconds)")

start_time = utime.ticks_ms()

# 10s Loop
while utime.ticks_diff(utime.ticks_ms(), start_time) < 10000:
    val = pot.read_u16()
    
    # Logic: detect a full rotation (Pass 50k then back to 10k)
    if val > 50000 and not is_high:
        is_high = True
        count += 1
        print("X", end="")
        
    if val < 10000 and is_high:
        is_high = False
        
    utime.sleep_ms(1)

rpm = count * 6
print("\nFINISHED!")
print("Total Spins: " + str(count))
print("Estimated RPM: " + str(rpm))
```

### 11. Common Mistakes
*   **No Hysteresis**: If you don't require the signal to drop back to 10000 before counting again, the computer might count 50 "spins" in a single second just because your hand was shaky near the limit.

### 12. Try This Next
*   **Buzzer Click**: Make the buzzer "Click" every time a spin is counted so it feels like a real ratchet.
*   **Reverse Count**: Make it so you have to spin Clockwise, then Counter-Clockwise to get 1 point.

---
