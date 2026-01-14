
## Project 0184: Kitchen Timer Sequences

### 1. Learning Objective
Explore progressive audio feedback. Learn how to trigger different acoustic patterns (beeps) as a countdown approaches its limit, providing a "Heads-up" to the user before the final alarm.

### 2. Concepts Introduced
*   **Progressive Signaling**: Increasing the frequency or complexity of an alarm as an event gets closer.
*   **Threshold Triggering**: Activating specific code blocks when a variable passes a certain value (e.g., 10 or 5).
*   **Acoustic Patterns**: Using short delays and buzzer tones to represent different states.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer (Active or Passive)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+)** | GP15 | Audio output pin |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **sec**: The current countdown time (initial: 15).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start Time**:
    *   From **Variables**, **Set** `sec` = 15.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Decrement Logic**:
    *   **Set** `sec` = `sec` - 1.
    *   **Print** "Seconds to Go: ", `sec`.

**C. Sequence Triggering Phase**
4.  **The 10-Second Warning**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `sec` == 10.
    *   **Action**: **Set** Buzzer (GP15) -> HIGH, **Wait** 0.1s, **Set** Buzzer -> LOW. (One Beep).
5.  **The 5-Second Warning**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `sec` == 5.
    *   **Action**: **Set** Buzzer (GP15) -> HIGH, **Wait** 0.1s, **Set** Buzzer -> LOW, **Wait** 0.1s, **Set** Buzzer -> HIGH, **Wait** 0.1s, **Set** Buzzer -> LOW. (Double Beep).

**D. Final Finish Phase**
6.  **The Final Alarm**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `sec` == 0.
    *   **Action**: **Set** Buzzer (GP15) -> HIGH (Continuous Tone).
7.  **Clock Pace**:
    *   Ensure there is a **Wait** 1 second block at the end of the loop to keep the timing accurate.

### 8. Execution Flow
1.  **Routine**: The timer counts 15, 14, 13, 12, 11... silently.
2.  **Early Warning**: At 10, the buzzer gives a single "chirp" to get the user's attention.
3.  **Critical Warning**: At 5, the buzzer chirps twice, signaling that the timer is almost done.
4.  **Final**: At 0, the buzzer turns on and stays on, indicating the task (cooking) is finished.

### 9. Generated Code
```python
from machine import Pin
import time

buzzer = Pin(15, Pin.OUT)
sec = 15

while True:
    if sec > 0:
        sec -= 1
        print("Time: " + str(sec))
        
        # Pre-Alarm logic
        if sec == 10:
            buzzer.value(1)
            time.sleep(0.1)
            buzzer.value(0)
            print("10s Warning!")
            
        if sec == 5:
            for _ in range(2):
                buzzer.value(1)
                time.sleep(0.1)
                buzzer.value(0)
                time.sleep(0.1)
            print("5s Warning!!")
            
        time.sleep(1)
        
    else:
        # Final Alarm
        buzzer.value(1)
        print("DING! TIME UP!")
        time.sleep(1)
```

### 10. Common Mistakes
*   **Logic Order**: If you put the `sec == 0` check before the subtraction, the buzzer might trigger at the "1" mark instead of the "0" mark.
*   **Passive Buzzer**: ensure you are using an Active buzzer (it makes sound with simple 3.3V power). If using Passive, you need PWM blocks.

### 11. Try This Next
*   **Volume Ramp**: If using PWM, make the beeps louder as the count gets lower.
*   **LED Sync**: Flash a Yellow LED with the 10s warning and a Red LED with the final alarm.

---

## Project 0185: Interactive Kitchen Timer

### 1. Learning Objective
Implement logic for state preservation (Pause/Resume). Learn how to use a toggle variable to "freeze" a value and prevent the decrement logic from firing without resetting the timer itself.

### 2. Concepts Introduced
*   **Pause Logic**: Creating a condition that must be met for a counter to advance.
*   **State Persistence**: Keeping the value of a variable safe during an "Idle" or "Paused" mode.
*   **User Interrupts**: Using a button to toggle between an Active and Inactive state.

### 3. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   10k Ohm pull-down resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Control Button** | GP14 | Single press Toggles PAUSE/RESUME |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **time_left**: Remaining seconds.
*   **is_paused**: Boolean (True/False) toggle.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial State**:
    *   **Set** `time_left` = 30.
    *   **Set** `is_paused` = False (Starts running).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Detect Toggle**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True.
    *   **Action**: 
        *   **Set** `is_paused` = NOT `is_paused`. (Flip the switch).
        *   From **Text**, **Print** "State changed. Paused: ", `is_paused`.
        *   **Wait** 0.3 seconds (Debounce).

**C. Conditional Logic Phase**
4.  **Count Only if Active**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `is_paused` == False AND `time_left` > 0.
    *   **Action**:
        *   **Set** `time_left` = `time_left` - 1.
        *   **Print** "Running: ", `time_left`.
        *   **Wait** 1 second.
5.  **Wait during Pause**:
    *   Else If `is_paused` == True:
        *   **Print** "STALLED at: ", `time_left`.
        *   **Wait** 1 second.

### 8. Execution Flow
1.  **Run**: The timer counts 30, 29, 28...
2.  **Interrupt**: The user needs to step away and presses the button at 25.
3.  **Hold**: The Pico sees `is_paused` is now True. It stops subtracting from `time_left`.
4.  **Resume**: The user returns and presses the button again.
5.  **Continue**: The Pico sees `is_paused` is False and resumes at 25, 24, 23...

### 9. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
time_left = 30
is_paused = False

print("Timer Started: 30s. Press button to PAUSE.")

while True:
    # Check for Pause Command
    if btn.value():
        is_paused = not is_paused
        print("PAUSE TOGGLED. Status: " + str(is_paused))
        time.sleep(0.3)
        
    # Progress only if not paused
    if not is_paused and time_left > 0:
        time_left -= 1
        print("Seconds: " + str(time_left))
        time.sleep(1)
    elif time_left == 0:
        print("DONE!")
        time.sleep(1)
    else:
        # Paused state loop
        time.sleep(0.1)
```

### 10. Common Mistakes
*   **Sleep Mismatch**: If you wait 1s in the pause check and 1s in the countdown, your clock will feel very laggy and may miss button presses. Keep the check loop fast.
*   **Variable Scope**: ensure `is_paused` is defined before the while loop starts.

### 11. Try This Next
*   **Pause LED**: Light up a Yellow LED ONLY when the timer is paused.
*   **Fast Forward**: Add an extra button to "Fast Forward" the timer by skipping 5 seconds.

---

## Project 0186: Smart Kitchen Timer Switch

### 1. Learning Objective
Explore non-contact interaction (Gestures). Learn how to use a Light Sensor (LDR) as a "Motion Trigger" to start a timer, allowing for a hygienic interface in a kitchen environment.

### 2. Concepts Introduced
*   **Touchless Triggers**: Initiating an action without physical contact.
*   **Threshold Detection (ADC)**: recognizing a drop in light when a hand shadows the sensor.
*   **State Locking**: Ensuring a wave starts the timer once but doesn't keep resetting it.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Photoresistor (LDR)
*   10k Ohm resistor (for voltage divider)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR Output** | GP26 (ADC0) | Hand shadow triggers timer |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Text, drag `text_print`** (print)

### 6. Variables
*   **ldr_raw**: current light level.
*   **timer_val**: countdown (starting at 180s/3 mins).
*   **is_active**: logic flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Values**:
    *   **Set** `timer_val` = 180.
    *   **Set** `is_active` = False.

**B. Detection Phase (Loop)**
2.  **Monitor Light levels**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `ldr_raw` = **Sensors** `pico_analog_read` GP26.
3.  **Detect Wave**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `ldr_raw` < 400 (This means it is dark - your hand is over it) AND `is_active` is False.
    *   **Action**: 
        *   **Set** `is_active` = True.
        *   **Print** "HAND WAVE DETECTED. 3-Minute Timer STARTED!".
        *   **Wait** 1 second (To let hand move away).

**C. Execution Phase**
4.  **Run the Clock**:
    *   Add an IF: If `is_active` is True and `timer_val` > 0.
        *   **Set** `timer_val` = `timer_val` - 1.
        *   **Print** "Remaining: ", `timer_val`.
        *   **Wait** 1 second.
5.  **Finish**:
    *   If `timer_val` == 0 and `is_active` is True:
        *   **Print** "Time's up! Wash your hands!".
        *   **Set** `is_active` = False.

### 8. Execution Flow
1.  **Wait**: The Pico sits ready. The LDR sees normal room brightness (around 700-800).
2.  **Wave**: You sweep your hand over the sensor. The value drops to 200.
3.  **Lock**: The Pico recognizes the drop and locks into "Active" mode.
4.  **Count**: The 3-minute (180s) timer begins.
5.  **Result**: You have a functioning timer that you never had to touch with sticky fingers.

### 9. Generated Code
```python
import machine
import utime

# Setup ADC for LDR
ldr = machine.ADC(26)
timer_val = 180
active = False

print("READY. Wave over sensor to start 3min timer.")

while True:
    read = ldr.read_u16()
    
    # 0-65535 range. 10000 is a good "Shadow" threshold
    if read < 10000 and not active:
        active = True
        print("GESTURE START!")
        utime.sleep(1) # Let hand pass
        
    if active:
        if timer_val > 0:
            timer_val -= 1
            print("T-Minus: " + str(timer_val) + "s")
            utime.sleep(1)
        else:
            print("DING DING DING!")
            active = False
            timer_val = 180 # Reset
            
    utime.sleep(0.1)
```

### 10. Common Mistakes
*   **Light Sensitivity**: Room light changes. A cloud passing by might trigger your timer. Ensure your threshold is set low enough that only a close-up shadow triggers it.
*   **Constant Reset**: If you don't use `not active`, holding your hand over the sensor might keep resetting the timer to 180.

### 11. Try This Next
*   **Double Wave**: Make it require TWO waves within 2 seconds to prevent accidental starts.
*   **Brightness Feedback**: Use an LED that gets brighter as the room gets darker so you can find the sensor at night.

---
