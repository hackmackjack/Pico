
## 1. Project 0206: Smart LED Patterns Switch

### 2. Learning Objective
Explore exclusive channel selection. Learn how to use a physical slide switch to toggle between two distinct groups of hardware (Group A vs Group B), ensuring only one side is active at a time.

### 3. Concepts Introduced
*   **Logical Exclusivity**: designing a system where two states cannot be active simultaneously.
*   **Hard-Switched States**: Using an input as a permanent mode selector rather than a temporary trigger.
*   **Group Organization**: logically bundling multiple outputs into a single "Bank".

### 4. Hardware Required
*   Raspberry Pi Pico
*   Slide Switch
*   4 LEDs + Resistors
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Group A (LED 1&2)** | GP15, GP14 | Active when Switch is Left |
| **Group B (LED 3&4)** | GP13, GP12 | Active when Switch is Right |
| **Slide Switch** | GP11 | Input source |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)

### 7. Variables
*   **None**: The direct pin state of the switch drives the execution branches.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Pins**: Ensure all 4 LEDs are initialized to LOW (0).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Detect Mode**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP11 is HIGH (1) (e.g., Switch Left).

**C. Execution Phase**
4.  **Activate Group A**:
    *   Inside the **If** block:
    *   **Set** GP15 -> HIGH (1).
    *   **Set** GP14 -> HIGH (1).
    *   **Set** GP13 -> LOW (0).
    *   **Set** GP12 -> LOW (0).
5.  **Activate Group B**:
    *   Inside the **Else** block (e.g., Switch Right):
    *   **Set** GP15 -> LOW (0).
    *   **Set** GP14 -> LOW (0).
    *   **Set** GP13 -> HIGH (1).
    *   **Set** GP12 -> HIGH (1).

### 9. Execution Flow
1.  **Read**: The Pico checks the physical position of the slide switch.
2.  **Logic**: If current is flowing through GP11, it follows the "If" branch.
3.  **Output**: The first two LEDs light up, while the others are turned off to ensure exclusivity.
4.  **Change**: When the user slides the switch, the Pico enters the "Else" branch on the very next cycle.
5.  **Result**: A reliable mode selector that manages multiple hardware channels instantly.

### 10. Generated Code
```python
from machine import Pin
import time

# Inputs
sw = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Groups
bank_a = [Pin(15, Pin.OUT), Pin(14, Pin.OUT)]
bank_b = [Pin(13, Pin.OUT), Pin(12, Pin.OUT)]

while True:
    if sw.value() == 1:
        # Bank A ON
        bank_a[0].value(1); bank_a[1].value(1)
        bank_b[0].value(0); bank_b[1].value(0)
    else:
        # Bank B ON
        bank_a[0].value(0); bank_a[1].value(0)
        bank_b[0].value(1); bank_b[1].value(1)
    
    time.sleep(0.1) # Fast polling
```

### 11. Common Mistakes
*   **Floating State**: If you don't use the `else` block to turn the *other* group off, you will eventually end up with all 4 LEDs on.
*   **Wiring**: ensuring the common pin of the switch is connected to 3.3V correctly.

### 12. Try This Next
*   **Blink Modes**: instead of static ON/OFF, make Group A blink fast and Group B blink slow.
*   **Third State**: If using a 3-position switch, add an `else if` to have a "Center-Off" mode.

---

## 1. Project 0207: LED Patterns Alarm System

### 2. Learning Objective
Explore persistent state logic (The SR Latch). Learn how to create an alarm that "Persistence" through an event—triggering once and staying active until a secondary, deliberate "Reset" signal is received.

### 3. Concepts Introduced
*   **Latching State**: A variable that stays True until forced to False.
*   **Trigger vs. Reset**: Distinguishing between an input that starts a process and one that stops it.
*   **State Machines**: A simple logic flow with two distinct modes (Armed vs Tripped).

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Trigger and Reset)
*   1 Red LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Trigger Button** | GP14 | Starts the alarm |
| **Reset Button** | GP13 | Clears the alarm |
| **Alarm LED** | GP15 | Stays ON when tripped |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)

### 7. Variables
*   **alarm_tripped**: Boolean (True/False) that tracks if the siren is active.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup State**:
    *   From **Variables**, **Set** `alarm_tripped` = False.
    *   **Set** GP15 (LED) -> LOW (0).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Check for Breach**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).
    *   **Action**: **Set** `alarm_tripped` = True.

**C. Resolution Phase**
4.  **Check for Reset**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP13 is HIGH (1).
    *   **Action**: **Set** `alarm_tripped` = False.

**D. Outcome Phase**
5.  **Update Hardware**:
    *   From **Logic**, drag `controls_if` with **else**.
    *   **Condition**: If `alarm_tripped` == True.
    *   **Action**: **Set** GP15 -> HIGH (1).
    *   **Else**: **Set** GP15 -> LOW (0).

### 9. Execution Flow
1.  **Idle**: The Pico waits. `alarm_tripped` is false.
2.  **Trip**: A door opens, hitting the Trigger button for just a split second.
3.  **Latch**: The code sets `alarm_tripped` to true. Even though the button is now released, the variable stays true.
4.  **Respond**: The LED turns on and stays lit.
5.  **Reset**: The security guard presses the Reset button. `alarm_tripped` becomes false, and the LED turns off.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn_trigger = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_reset = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Internal State
alarm_active = False

while True:
    # Handle Trigger
    if btn_trigger.value() == 1:
        alarm_active = True
        print("ALARM TRIPPED!")
        
    # Handle Reset
    if btn_reset.value() == 1:
        alarm_active = False
        print("Alarm Cleared.")
        
    # Apply State to Hardware
    if alarm_active:
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Button Collision**: If both buttons are held at once, the code order determines the outcome (usually the second check, Reset, will win).
*   **No Variables**: Trying to do this without a variable (direct pin control) means the LED would only be on while the trigger is held, which isn't a persistent alarm.

### 12. Try This Next
*   **Audio Alarm**: add a buzzer that beeps only when the alarm is tripped.
*   **Tripped Indicator**: adding a Green LED that is ON when safe and turns OFF when the Red LED is tripped.

---

## 1. Project 0208: The LED Patterns Game

### 2. Learning Objective
Explore precision timing and input window detection. Learn how to implement "Stop the Light," where a user must synchronize a physical action (button press) with a specific state in a fast-moving sequence.

### 3. Concepts Introduced
*   **Target Calculation**: Checking if an input occurs during a specific sub-interval of a sequence.
*   **Game State Feedback**: providing immediate visual confirmation of Win/Loss.
*   **Variable Delays**: Speeding up the sequence as the player gets better.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   3 LEDs (e.g., Red, Yellow, Green)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1 (Side)** | GP15 | Normal light |
| **LED 2 (Middle)** | GP14 | THE TARGET LIGHT |
| **LED 3 (Side)** | GP13 | Normal light |
| **Input Button** | GP12 | Press to "Catch" the light |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (sequence loop)
*   **from Logic, drag `controls_if`** (checking if user caught it)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **current_led**: Tracks which of the 3 pins is currently ON.

### 8. Step-by-Step Guide

**A. Sequence Phase**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Define Sequence**:
    *   Create a list of pins [15, 14, 13].
    *   From **Loops**, drag a "for each item in list" or manual sequence:
        *   **Set** GP15 -> HIGH, others LOW. Wait 0.15s.
        *   **Set** GP14 -> HIGH, others LOW. Wait 0.15s.
        *   **Set** GP13 -> HIGH, others LOW. Wait 0.15s.

**B. Detection Phase**
3.  **Check for Button**:
    *   Inside each step, check: If **Button** GP12 is Pressed.
    *   If pressed during **Step 2** (GP14):
        *   **Print** "WINNER!".
        *   Flash all LEDs 5 times fast.
        *   Wait 2s.
    *   Else if pressed during Step 1 or 3:
        *   **Print** "MISS!".
        *   Keep all LEDs OFF for 1s.

### 9. Execution Flow
1.  **Run**: The lights cycle: 1... 2... 3... 1... 2... 3... very fast.
2.  **Target**: The middle light (GP14) is only on for 150 milliseconds.
3.  **Act**: The user taps the button.
4.  **Math**: If the tap happened during the 150ms window of GP14, the "Win" block fires.
5.  **Result**: An interactive skill game that tests human reaction speed.

### 10. Generated Code
```python
import machine
import utime

# Hardware
leds = [machine.Pin(15, machine.Pin.OUT), 
        machine.Pin(14, machine.Pin.OUT), 
        machine.Pin(13, machine.Pin.OUT)]
btn = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    for i in range(3):
        # Light up the current LED
        for j in range(3):
            leds[j].value(1 if i == j else 0)
            
        # Check for button press in a small loop to catch it
        start_wait = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_wait) < 150:
            if btn.value():
                if i == 1: # Middle LED is index 1
                    print("YOU WIN!")
                    for _ in range(5):
                        for l in leds: l.value(1)
                        utime.sleep(0.05)
                        for l in leds: l.value(0)
                        utime.sleep(0.05)
                else:
                    print("TOO EARLY/LATE")
                    utime.sleep(1)
                utime.sleep(1) # Gap between games
```

### 11. Common Mistakes
*   **Long Delays**: If you use a single `time.sleep(0.15)` block, the Pico is "blind" to the button while it sleeps. You must use a tight checking loop (like the one in the code above) to catch the press.

### 12. Try This Next
*   **Difficulty Scaling**: every time you win, reduce the wait time from 150ms to 130ms.
*   **Score Tracker**: count how many wins you can get in a row before missing once.

---

## 1. Project 0209: Automated LED Patterns

### 2. Learning Objective
Explore proportional brightness control (Ambient Match). Learn how to use a Light Sensor (LDR) to read environmental data and map it directly to an LED's PWM duty cycle to create "Self-Adjusting" lighting.

### 3. Concepts Introduced
*   **Analog Input Calibration**: converting a raw light value into a percentage.
*   **Pulse Width Modulation (PWM)**: Simulating different brightness levels on a digital pin.
*   **Proportional Logic**: designing a relationship where "More Light outside = More Light on the Pico".

### 4. Hardware Required
*   Raspberry Pi Pico
*   Photoresistor (LDR)
*   10k Ohm resistor (Voltage Divider)
*   1 LED + resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Light Sensor** | GP26 (ADC0) | Measures room light |
| **Output LED** | GP15 | Adjusted via PWM |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_map`** (convert range)
*   **from Actuators, drag `pico_pwm_write`** (set Brightness)

### 7. Variables
*   **light_level**: raw value from the sensor.
*   **led_brightness**: calculated duty cycle.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**: Initialize GP15 for PWM output.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Read Ambient Light**:
    *   Inside the loop, **Set** `light_level` = **Sensors** `pico_analog_read` GP26.

**C. Translation Phase**
4.  **Map the values**:
    *   From **Math**, drag the `math_map` block.
    *   **Input**: `light_level`.
    *   **Settings**: From [0 to 1023] (or internal 65535) to [0 to 100%].
    *   **Set** `led_brightness` = this result.

**D. Execution Phase**
5.  **Drive the Hardware**:
    *   From **Actuators**, **Set** GP15 (LED) Brightness to `led_brightness`.
6.  **Pace**: **Wait** 0.1 seconds (smooth but fast updates).

### 9. Execution Flow
1.  **Read**: The Pico sees the sun is shining brightly (High ADC value).
2.  **Math**: The mapping block converts this "Bright" reading into a "100%" brightness request.
3.  **Act**: The LED turns on full power so it can be seen under the sun.
4.  **Change**: You put your hand over the sensor. The Pico sees "Dark" (Low ADC).
5.  **Dim**: The mapping block requests "10%". The LED dims instantly so it doesn't hurt your eyes in the dark.

### 10. Generated Code
```python
import machine
import utime

# Hardware
ldr = machine.ADC(machine.Pin(26))
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    # Read (0-65535)
    raw_val = ldr.read_u16()
    
    # Map raw value to PWM duty cycle
    # In bright light, we want high brightness.
    # Adjust thresholds based on your room's baseline.
    duty = int(raw_val)
    
    # Clamp to ensure it stays in range
    if duty > 65535: duty = 65535
    if duty < 0: duty = 0
    
    led.duty_u16(duty)
    
    # Status
    # print("Light: " + str(raw_val) + " -> Power: " + str(duty))
    utime.sleep(0.1)
```

### 11. Common Mistakes
*   **Inversion**: If the LED gets BRIGHTER when it's DARK, it's acting as a night-light. To fix this, swap the map outputs: from [0-65535] to [100%-0%].
*   **ADC Pin**: Only pins 26, 27, and 28 support analog reading.

### 12. Try This Next
*   **Night Light Mode**: Swap the logic so the LED is only ON when the room is dark.
*   **Transition Smoothing**: create a variable that slowly crawls towards the target brightness instead of jumping instantly.

---

## 1. Project 0210: Mastering LED Patterns

### 2. Learning Objective
Explore temporal-spatial illusions (Persistence of Vision - POV). Learn how to flash a row of LEDs at extremely high speeds (milliseconds) so that they appear to "Draw" a shape or letter in mid-air when physically waved.

### 3. Concepts Introduced
*   **Persistence of Vision**: How the human eye creates a continuous image from fast flashes.
*   **Column Scanning**: Drawing one vertical line of an image at a time.
*   **Timing Criticality**: Using the smallest possible delays (e.g. 5-10ms) for high-speed synchronization.

### 4. Hardware Required
*   Raspberry Pi Pico
*   5 LEDs + Resistors (placed in a strict vertical row)
*   Hands (to wave the wand)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Row (Top to Bottom)** | GP15, 14, 13, 12, 11 | The "Pixel" Column |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait_ms`** (wait in milliseconds)

### 7. Variables
*   **None**: All pixel patterns are explicitly coded in the timing sequence.

### 8. Step-by-Step Guide

**A. Define the Character (e.g., Letter 'H')**
1.  **Column 1 (Full Bar)**:
    *   **Set** ALL LEDs (15, 14, 13, 12, 11) -> HIGH.
    *   **Wait** 5 milliseconds.
2.  **Column 2 (Middle Only)**:
    *   **Set** GP13 -> HIGH, others LOW.
    *   **Wait** 5 milliseconds.
3.  **Column 3 (Full Bar)**:
    *   **Set** ALL LEDs -> HIGH.
    *   **Wait** 5 milliseconds.

**B. Define the Frame Gap**
4.  **Separator**:
    *   **Set** ALL LEDs -> LOW.
    *   **Wait** 20 milliseconds.

**C. Play Loop**
5.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
6.  Inside the loop, place the steps for Columns 1, 2, 3, and the Gap.

### 9. Execution Flow
1.  **Static**: While sitting still, the LEDs look like they are just flashing randomly and very fast.
2.  **Motion**: The user holds the breadboard and waves it quickly from left to right.
3.  **Persistence**: Because the LEDs change state while they are physically moving through space, your eyes "smear" the flashes into a single horizontal image.
4.  **Result**: The letter "H" appears floating in the air.

### 10. Generated Code
```python
from machine import Pin
import time

# Vertical LED strip
pixels = [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT), 
          Pin(12, Pin.OUT), Pin(11, Pin.OUT)]

def set_col(p1, p2, p3, p4, p5):
    pixels[0].value(p1)
    pixels[1].value(p2)
    pixels[2].value(p3)
    pixels[3].value(p4)
    pixels[4].value(p5)
    time.sleep_ms(5)

while True:
    # Drawing 'H'
    set_col(1, 1, 1, 1, 1) # Full line
    set_col(0, 0, 1, 0, 0) # Middle dot
    set_col(1, 1, 1, 1, 1) # Full line
    
    # Drawing 'I'
    set_col(0, 0, 0, 0, 0) # Gap
    set_col(1, 0, 0, 0, 1) # Top and Bottom
    set_col(1, 1, 1, 1, 1) # Center stem
    set_col(1, 0, 0, 0, 1) # Top and Bottom
    
    # Reset
    set_col(0, 0, 0, 0, 0)
    time.sleep_ms(30) # Wait before repeating word
```

### 11. Common Mistakes
*   **Too Slow**: If you wait 50ms instead of 5ms, you will just see a series of dots instead of a connected image.
*   **Wobble**: You must wave the Pico at a consistent speed for the image to look correctly proportioned.

### 12. Try This Next
*   **Custom Shapes**: draw a smiley face by mapping out a 5x5 grid.
*   **Speed Switch**: add a button that switches between 5ms, 10ms, and 15ms so you can match the speed to different arm-waving strengths.

---
