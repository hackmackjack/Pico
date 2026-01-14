import os

def build_batch55_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0541 = """
---

# Batch 55: Smart Fan 3

## 1. Project 0541: Introduction to Smart Fan

### 2. Learning Objective
Build a "Soft Start" motor controller that gradually increases fan speed from 0% to 100% using a PWM ramping sequence.

### 3. Concepts Introduced
*   PWM (Pulse Width Modulation)
*   Ramping/Duty Cycle Sweeping
*   Motor Inertia
*   Iterative Loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   Motor Driver (DRV8833)
*   DC Fan
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pico VBUS** | Motor VCC | 5V Power |
| **GND** | Motor GND | Ground |
| **Motor IN1** | GP16 | PWM Speed Control |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (for loops)
*   **from Smart IO, drag `pico_pwm_write`** (duty cycle control)
*   **from Time, drag `pico_wait`** (timing)

### 7. Variables
*   **fan_speed**: Integer (Target duty cycle value)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup PWM**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   **Snap** into `start` block.
    *   Set Pin to GP16 and Value to 0.

**B. Main Loop Phase**
1.  **Create Container**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Define Ramp**:
    *   From **Loops**, drag `count_with`.
    *   **Snap** into `pico_forever`.
    *   Set Variable to `fan_speed`, From 0, To 65000, Step 650.
3.  **Execute Speed**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   **Snap** into `count_with`.
    *   Set Pin to GP16 and Value to variable `fan_speed`.
4.  **Wait**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below PWM block.
    *   Set 0.1 seconds.

### 9. Execution Flow
1.  **Start**: The Pico initializes GP16 as a PWM channel.
2.  **Process**: The system enters a loop that counts upward.
3.  **Output**: Every 0.1 seconds, the "duty cycle" (power percentage) of the fan increases.
4.  **Process**: The fan motor overcomes initial friction and begins spinning slowly.
5.  **Output**: The fan reaches full velocity over roughly 10 seconds.
6.  **Repeat**: The process restarts from zero power.

### 10. Generated Code
```python
import machine
import time

# Initialize Fan on Pin 16
fan = machine.PWM(machine.Pin(16))
fan.freq(1000)

while True:
    # Ramp up from 0 to ~100%
    for fan_speed in range(0, 65536, 655):
        fan.duty_u16(fan_speed)
        time.sleep(0.1)
    
    # Hold for a moment before reset
    time.sleep(2)
```

### 11. Common Mistakes
*   **Step Size**: Using a step size too large (e.g., 30000) makes the fan snap to speed rather than ramp.
*   **Pin Mode**: Forgetting that DC motors require PWM blocks, not digital HIGH/LOW blocks, to change speed.

### 12. Try This Next
*   **Soft Stop**: Add another `count_with` block that goes from 65000 down to 0 after the ramp up.
"""

    p0542 = """
---

## 1. Project 0542: Blinking Smart Fan

### 2. Learning Objective
Control a fan to simulate "Gusty Winds" by alternating between a low baseline speed and random high-speed surges using probabilistic logic.

### 3. Concepts Introduced
*   Baseline Power
*   Random Surges
*   Probabilistic Wait
*   Natural Environment Simulation

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Motor Driver

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor IN** | GP16 | Speed control |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (timing variation)
*   **from Smart IO, drag `pico_pwm_write`** (power levels)
*   **from Time, drag `pico_wait`** (duration)

### 7. Variables
*   **wait_time**: Integer (Seconds between gusts)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_pwm_write` GP16 to 15000 (Low Breeze).

**B. Main Loop Phase**
1.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Set Baseline**:
    *   From **Smart IO**, drag `pico_pwm_write` GP16 to 15000.
    *   **Snap** into loop.
3.  **Wait for Gust**:
    *   From **Variables**, set `wait_time` to **Math** `random_integer` 1 to 5.
    *   From **Time**, drag `pico_wait` and set to variable `wait_time`.
    *   **Snap** below baseline.
4.  **Trigger Gust**:
    *   From **Smart IO**, drag `pico_pwm_write` GP16 to 65000 (Full Power).
    *   **Snap** below wait.
5.  **Wind Duration**:
    *   From **Time**, drag `pico_wait` 0.5 seconds.
    *   **Snap** below high power.

### 9. Execution Flow
1.  **Start**: The fan turns on at a gentle 20% speed.
2.  **Process**: The code calculates a random "peaceful" duration.
3.  **Delay**: The system maintains the low breeze for the random time.
4.  **Output**: Suddenly, the PWM jumps to 100% power.
5.  **Output**: The fan surges loudly for exactly half a second (the "Gust").
6.  **Repeat**: The fan returns to its baseline speed and waits for the next random surge.

### 10. Generated Code
```python
import machine
import time
import random

fan = machine.PWM(machine.Pin(16))
fan.freq(1000)

while True:
    # Baseline Breeze (20%)
    fan.duty_u16(15000)
    
    # Wait for random onset
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
    
    # Gust Surge (100%)
    print("Incoming Gust!")
    fan.duty_u16(65000)
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **No Baseline**: Setting the speed to 0 between gusts makes the project look like it's broken during the wait phase.
*   **Gust Duration**: Making the gust too long (e.g., 5 seconds) makes the fan feel like it has just changed speeds permanently.

### 12. Try This Next
*   **Variable Gusts**: Use the `random_integer` block to decide the power level of the gust (e.g., between 40000 and 65000).
"""

    p0543 = """
---

## 1. Project 0543: Manual Smart Fan Control

### 2. Learning Objective
Build a "3-Speed Selector" for a fan that cycles through Off, Low, Med, and High modes using a single button and state variables.

### 3. Concepts Introduced
*   State Cycles
*   Modulo Math (Wrap around)
*   User Input Interlocks
*   Selection Logic

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speed Button** | GP14 | Cycle Input |
| **Fan IN** | GP16 | Speed Output |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`** (Multi-choice)
*   **from Variables, drag `change_variable`** (Index increment)
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **fan_mode**: Integer (0, 1, 2, or 3)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset State**:
    *   From **Variables**, set `fan_mode` to 0.
    *   From **Smart IO**, set `pico_pwm_write` to 0.

**B. Main Loop Phase**
1.  **Monitor Button**:
    *   From **Loops**, drag `pico_forever`.
2.  **Detect Click**:
    *   From **Logic**, if GP14 (Button) is HIGH:
        *   **Action**: From **Variables**, change `fan_mode` by 1.
        *   **Action**: From **Time**, wait 0.3s (Debounce).
3.  **Boundary Control**:
    *   From **Logic**, if `fan_mode` > 3:
        *   **Action**: Set `fan_mode` to 0.
4.  **Execute Speeds**:
    *   From **Logic**, drag `if_elseif`.
    *   **If `fan_mode` == 1**: Set Pin 16 to 20000 (Low).
    *   **Else If `fan_mode` == 2**: Set Pin 16 to 40000 (Med).
    *   **Else If `fan_mode` == 3**: Set Pin 16 to 65000 (High).
    *   **Else**: Set Pin 16 to 0 (Off).

### 9. Execution Flow
1.  **Start**: The fan is stationary (Mode 0).
2.  **Sense**: The user presses the button.
3.  **Decide**: The variable `fan_mode` becomes 1.
4.  **Output**: The fan begins spinning at a low speed (30% power).
5.  **Process**: Repeated presses cycle the state until 3 (High).
6.  **Reset**: A further press triggers the boundary check, returning the mode to 0 (Off).

### 10. Generated Code
```python
from machine import Pin, PWM
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)

fan_mode = 0 # 0=Off, 1=Low, 2=Med, 3=High

while True:
    if btn.value():
        fan_mode = (fan_mode + 1) % 4
        print("Mode switched to:", fan_mode)
        time.sleep(0.3)
        
    if fan_mode == 1: fan.duty_u16(20000)
    elif fan_mode == 2: fan.duty_u16(40000)
    elif fan_mode == 3: fan.duty_u16(65000)
    else: fan.duty_u16(0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Debounce Missing**: Without the 0.3s wait, one button press might "skip" gears because the Pico is too fast.

### 12. Try This Next
*   **LED Feedback**: Add three LEDs that light up to show which gear is currently selected.
"""

    p0544 = """
---

## 1. Project 0544: Smart Fan Sequences

### 2. Learning Objective
Control a "Pedestal Fan Simulator" where a Servo motor rotates the base back and forth while a DC motor provides constant airflow.

### 3. Concepts Introduced
*   Compound Motion
*   Servo Sweeping
*   Coordinated Duty Cycles
*   Mechanical Panning

### 4. Hardware Required
*   Raspberry Pi Pico
*   SG90 Servo
*   DC Fan (Mounted on Servo)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pivot Servo** | GP15 | Panning Control |
| **Fan IN** | GP16 | Speed Control |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`** (0 to 180)
*   **from Smart IO, drag `pico_pwm_write`** (Fan speed)
*   **from Loops, drag `count_with`**

### 7. Variables
*   **pan_angle**: Integer (Current servo position)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Fan**:
    *   From **Smart IO**, drag `pico_pwm_write` Pin GP16 to 40000.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Create Container**:
    *   From **Loops**, drag `pico_forever`.
2.  **Pan Right**:
    *   From **Loops**, drag `count_with`.
    *   **Snap** into `pico_forever`.
    *   Set Variable to `pan_angle`, From 0, To 180, Step 5.
3.  **Execute Motion**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into `count_with`.
    *   Set Pin to GP15 and Angle to `pan_angle`.
    *   From **Time**, wait 0.05s.
4.  **Pan Left**:
    *   Repeat steps 2-3 with `count_with` going from 180 down to 0.

### 9. Execution Flow
1.  **Start**: The DC fan begins spinning at a steady 60% speed.
2.  **Process**: The system starts a loop to move the servo.
3.  **Output**: The servo motor pivots the fan 5 degrees every 50ms.
4.  **Sense**: The airflow is directed across the room in a sweeping pattern.
5.  **Reverse**: Once it reaches the 180-degree limit, the loop reverses direction.
6.  **Repeat**: The fan oscillates continuously until stopped.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Setup Fan
fan = PWM(Pin(16)); fan.freq(1000)
fan.duty_u16(40000)

# Setup Servo (Standard Mapping 1.0ms-2.0ms)
srv = PWM(Pin(15)); srv.freq(50)
def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    # Pan Right
    for angle in range(0, 181, 5):
        move(angle)
        time.sleep(0.05)
    # Pan Left
    for angle in range(180, -1, -5):
        move(angle)
        time.sleep(0.05)
```

### 11. Common Mistakes
*   **Current Draw**: A servo and a DC fan running at the same time can draw too much power from the 3.3V pin. Always use the 5V (VBUS) pin for motors.

### 12. Try This Next
*   **Variable Swing**: Add a potentiometer to change the speed of the sweep (The `time.sleep` value).
"""

    p0545 = """
---

## 1. Project 0545: Interactive Smart Fan

### 2. Learning Objective
Display a "Breath Triggered" fan system where blowing on a sound sensor activates the main fan for 5 seconds.

### 3. Concepts Introduced
*   Analog Noise Thresholds
*   Timed Triggers
*   Environment Interaction
*   Signal/Response logic

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor (Analog)
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Mic Sensor** | GP26 (ADC) | Sound input |
| **Main Fan** | GP16 | Speed output |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`** (Measure volume)
*   **from Logic, drag `if_else`** (Threshold)
*   **from Time, drag `pico_wait`** (Operation cycle)

### 7. Variables
*   **sound_vol**: Integer (0-65535)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   From **Smart IO**, ensure GP16 is set to 0.

**B. Main Loop Phase**
1.  **Monitor Sound**:
    *   From **Loops**, drag `pico_forever`.
2.  **Read Input**:
    *   From **Variables**, set `sound_vol` to **Smart IO** `pico_adc_read` GP26.
3.  **Check Breath**:
    *   From **Logic**, if `sound_vol` > 35000 (A loud blow):
        *   **Action**: From **Smart IO**, set GP16 (PWM) to 65000.
        *   **Action**: From **Time**, wait 5 seconds.
        *   **Action**: From **Smart IO**, set GP16 (PWM) to 0.
    *   **Else**:
        *   Set GP16 to 0.

### 9. Execution Flow
1.  **Start**: The fan is off. The Pico monitors the surrounding noise.
2.  **Sense**: The user blows into the microphone module.
3.  **Decide**: The analog voltage spikes, crossing the 35,000 threshold.
4.  **Output**: The fan snaps to 100% speed instantly.
5.  **Delay**: The system "holds" the power for exactly 5 seconds.
6.  **Shutdown**: The fan turns off and returns to "listening" mode.

### 10. Generated Code
```python
import machine
import time

mic = machine.ADC(26)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)

while True:
    vol = mic.read_u16()
    
    if vol > 35000:
        print("Breath Detected! Fan ACTIVE.")
        fan.duty_u16(65000)
        time.sleep(5)
        fan.duty_u16(0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Sensitivity**: Every room has different noise levels. If the fan turns on by itself, increase the 35,000 threshold to 45,000.

### 12. Try This Next
*   **Proportional Speed**: Instead of a flat 5 seconds, make the fan spin faster if the sound is louder.
"""

    p0546 = """
---

## 1. Project 0546: Smart Smart Fan Switch

### 2. Learning Objective
Implement an energy-saving "Sleep Timer" that runs the fan at a reduced speed (30%) for 10 seconds following a trigger event.

### 3. Concepts Introduced
*   Timer Durations
*   Energy Conservation
*   Sequential State Progress
*   Status Feedback

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sleep Button** | GP14 | Start countdown |
| **Fan Motor** | GP16 | Speed output |

### 6. Blocks Used
*   **from Time, drag `pico_wait`**
*   **from Smart IO, drag `pico_pwm_write`**
*   **from Text, drag `print`**

### 7. Variables
*   **None**: Sequential direct-execution logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Fan**:
    *   Ensure Pin 16 is initially 0.

**B. Main Loop Phase**
1.  **Monitor Start**:
    *   From **Loops**, drag `pico_forever`.
2.  **Wait for Request**:
    *   From **Logic**, if Button GP14 is HIGH:
        *   **Action**: From **Text**, print "Starting 10-second timer...".
        *   **Action**: From **Smart IO**, set GP16 (PWM) to 20000 (Quiet Mode).
        *   **Action**: From **Time**, wait 10 seconds.
        *   **Action**: From **Text**, print "Cooling complete. Powering down.".
        *   **Action**: From **Smart IO**, set GP16 to 0.

### 9. Execution Flow
1.  **Start**: The Pico waits for a manual command via the button.
2.  **Output**: Upon pressing, the fan begins spinning quietly.
3.  **Process**: The system enters a "blocking" wait state for 10 seconds.
4.  **Feedback**: The terminal reports the activity status to the user.
5.  **Shutdown**: Power is cut automatically after 100% of the duration has elapsed.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)

while True:
    if btn.value():
        print("NIGHT MODE: Running for 10s")
        fan.duty_u16(20000) # Quiet speed
        time.sleep(10)
        
        print("TIME EXPIRED: Shutting down.")
        fan.duty_u16(0)
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Blocking Error**: This code stops you from pressing the button again *during* the 10 seconds. If you want a "cancel" button, you need advanced non-blocking code.

### 12. Try This Next
*   **Visual Warning**: Flash a Red LED on the final 2 seconds of the timer to warn the user that shutdown is imminent.
"""

    p0547 = """
---

## 1. Project 0547: Smart Fan Alarm System

### 2. Learning Objective
Create a "Safety Lockout" system that disables the fan and sounds an alarm if a physical fault (e.g., a jammed blade) is detected by a sensor.

### 3. Concepts Introduced
*   Safety Latches
*   Fault Detection
*   Manual Reset logic
*   Priority Overrides

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   2x Buttons (Fault sim, Reset)
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fault Switch** | GP14 | Simulates jam |
| **Reset Switch** | GP15 | Clear error |
| **Fan Output** | GP16 | Main Actuator |
| **Alarm Buzzer** | GP12 | Sound alert |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Variables, drag `set_variable`** (Flag)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **is_stalled**: Boolean (Fault flag)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Clear Flags**:
    *   From **Variables**, set `is_stalled` to FALSE.
2.  **Init Buzz**:
    *   Set GP12 to LOW.

**B. Main Loop Phase**
1.  **Detect Jam**:
    *   From **Logic**, if Button GP14 is HIGH:
        *   **Action**: Set `is_stalled` to TRUE.
        *   **Action**: Print "CRITICAL FAULT DETECTED".
2.  **Manual Reset**:
    *   From **Logic**, if Button GP15 is HIGH:
        *   **Action**: Set `is_stalled` to FALSE.
        *   **Action**: Print "Safety Reset Success".
3.  **Safety Gate**:
    *   From **Logic**, if `is_stalled` is TRUE:
        *   **Action**: Set Fan (GP16) to 0.
        *   **Action**: Set Buzzer (GP12) to HIGH.
    *   **Else**:
        *   **Action**: Set Fan (GP16) to 30000 (Safe Run).
        *   **Action**: Set Buzzer (GP12) to LOW.

### 9. Execution Flow
1.  **Start**: The fan spins normally. The system is in "Green" status.
2.  **Sense**: Something blocks the fan (User hits Button 1).
3.  **Process**: The `is_stalled` variable flips to TRUE.
4.  **Reaction**: The code instantly kills the fan and starts the alarm.
5.  **Memory**: Even if Button 1 is released, the fan stays off (the variable "latches" the memory).
6.  **Restore**: The user must deliberately hit Button 2 (Reset) to clear the memory and restart the motor.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

fault_btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
reset_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)
buz = Pin(12, Pin.OUT)

is_stalled = False

while True:
    # 1. Check for Faults
    if fault_btn.value():
        is_stalled = True
    
    # 2. Check for Reset
    if reset_btn.value():
        is_stalled = False
        
    # 3. Apply Enforcement
    if is_stalled:
        fan.duty_u16(0)
        buz.on()
    else:
        fan.duty_u16(30000)
        buz.off()
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Latch**: Thinking checking `if fault_btn:` is enough. If you don't use a variable, the fan will start again as soon as the object is removed, which is dangerous!

### 12. Try This Next
*   **Strobe Warning**: Make the alarm buzzer beep (ON/OFF) rather than stay solid.
"""

    p0548 = """
---

## 1. Project 0548: The Smart Fan Game

### 2. Learning Objective
Programm a "Hover Challenge" where a potentiometer allows the user to balance a ping pong ball in mid-air by mapping analog data to fan lift.

### 3. Concepts Introduced
*   Physics-Based Control
*   Analog-to-Lift Mapping
*   Dynamic Equilibrium
*   User-in-the-loop logic

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan (Blowing UP)
*   10kΩ Potentiometer
*   Celluloid Ball (Ping Pong)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Hover Control**| GP26 (ADC) | Manual adjustment |
| **Fan Lift** | GP16 (PWM) | Airflow Output |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`** (Sense knob)
*   **from Math, drag `map_range`** (Convert to power)
*   **from Smart IO, drag `pico_pwm_write`** (Set speed)

### 7. Variables
*   **lift_power**: Integer (0-65535)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure ADC**:
    *   Set GP26 as Input.
2.  **Configure PWM**:
    *   Set GP16 to 1000Hz frequency.

**B. Main Loop Phase**
1.  **Create Container**:
    *   From **Loops**, drag `pico_forever`.
2.  **Sense User**:
    *   From **Variables**, set `lift_power` to **Smart IO** `pico_adc_read` GP26.
    *   **Snap** into loop.
3.  **Apply Force**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   Set Pin to GP16 and Value to variable `lift_power`.
    *   **Snap** below sensing.
4.  **Wait**:
    *   Wait 0.02s for smooth feedback.

### 9. Execution Flow
1.  **Start**: The fan sits still.
2.  **Interaction**: The user turns the potentiometer clockwise.
3.  **Process**: The Pico reads the higher voltage and increases the PWM duty cycle.
4.  **Output**: The fan spins faster, creating upward air pressure.
5.  **Reaction**: The ball lifts off. The user must carefully adjust the knob to keep the ball from flying out or falling down.
6.  **Balance**: The system achieves parity between gravity and air resistance.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)

while True:
    # Scale pot reading directly to fan speed
    pwr = pot.read_u16()
    fan.duty_u16(pwr)
    
    # Debug height estimate
    print(f"LIFT: {int(pwr/655)}%")
    time.sleep(0.02)
```

### 11. Common Mistakes
*   **Fan Polarity**: If the wires are backward, the fan will blow DOWN instead of UP, and the ball will never lift.

### 12. Try This Next
*   **Auto-Pilot**: Use an Ultrasonic sensor to measure height and make the fan auto-adjust to keep the ball centered.
"""

    p0549 = """
---

## 1. Project 0549: Automated Smart Fan

### 2. Learning Objective
Build a "Bathroom Exhaust" simulator that automatically activates the fan when humidity levels cross $70\%$ to prevent mold growth.

### 3. Concepts Introduced
*   Environmental Triggers
*   Health-Based Automation
*   Hysteresis (Basics)
*   Sensor Sampling intervals

### 4. Hardware Required
*   Raspberry Pi Pico
*   DHT11 or DHT22 Sensor
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT11 Data** | GP15 | Climate Sensor |
| **Exhaust Fan** | GP16 | Remediation |

### 6. Blocks Used
*   **from Sensors, drag `pico_dht_read`** (Measure air)
*   **from Logic, drag `greater_than`** (70% limit)
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **cur_humidity**: Integer (%)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**:
    *   Ensure Fan is initially OFF.

**B. Main Loop Phase**
1.  **Create Monitor Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Read Environment**:
    *   From **Sensors**, set `cur_humidity` to Humidity level.
    *   **Snap** into loop.
3.  **Evaluate Risk**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `cur_humidity` > 70:
        *   **Action**: From **Smart IO**, set GP16 to HIGH.
        *   Print "Damp air detected. Fan ON."
    *   **Else**:
        *   **Action**: From **Smart IO**, set GP16 to LOW.
4.  **Sample Frequency**:
    *   From **Time**, wait 2 seconds. (DHT sensors need rest).

### 9. Execution Flow
1.  **Start**: The Pico begins checking the room moisture every 2 seconds.
2.  **Sense**: A hot shower increases the room's relative humidity to 85%.
3.  **Decide**: The `cur_humidity` value crosses the "High" threshold.
4.  **Output**: The fan turns on to exhaust the damp air.
5.  **Recovery**: Once the air is dry (below 70%), the `if` condition fails.
6.  **Shutdown**: Power to the fan is cut automatically to save energy.

### 10. Generated Code
```python
import machine, dht, time

sensor = dht.DHT11(machine.Pin(15))
fan = machine.Pin(16, machine.Pin.OUT)

while True:
    try:
        sensor.measure()
        h = sensor.humidity()
        print(f"Humidity: {h}%")
        
        if h > 70:
            fan.on()
        else:
            fan.off()
            
    except OSError:
        print("Sensor Error")
        
    time.sleep(2)
```

### 11. Common Mistakes
*   **Fast Sampling**: Attempting to read DHT sensors 100 times per second. This will cause the sensor to return errors or heat up.

### 12. Try This Next
*   **Comfort Zone**: Only turn the fan off when humidity drops below 60% (preventing it from flickering at exactly 70%).
"""

    p0550 = """
---

## 1. Project 0550: Mastering Smart Fan

### 2. Learning Objective
Calculate the physical speed of a fan in Revolutions Per Minute (RPM) by monitoring the pulse frequency of its internal tachometer pin.

### 3. Concepts Introduced
*   Feedback Frequency
*   Pulse Counting
*   Mathematical Conversions
*   Microsecond Deltas

### 4. Hardware Required
*   Raspberry Pi Pico
*   3-wire or 4-wire PC Fan
*   External Power Supply (12V)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fan Tach** | GP14 | Pulse Input |
| **Fan PWM** | GP16 | Speed Drive |

### 6. Blocks Used
*   **from Time, drag `pico_milliseconds`** (Interval)
*   **from Logic, drag `repeat_until`** (Sampling window)
*   **from Math, drag `multiplication`**

### 7. Variables
*   **ticks**: Integer (Pulse count)
*   **rpm**: Float (Calculated velocity)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Drive Motor**:
    *   From **Smart IO**, set GP16 (PWM) to 40000 to get it spinning.
2.  **Reset Count**:
    *   Set `ticks` to 0.

**B. Measuring Phase**
1.  **Create 1-second Window**:
    *   Mark `start_time` = milliseconds.
2.  **Count In pulses**:
    *   Inside a loop, if GP14 changes from LOW to HIGH:
        *   **Action**: Change `ticks` by 1.
    *   Repeat until (`current_ms - start_time`) > 1000.
3.  **Convert to RPM**:
    *   From **Math**, set `rpm` to (`ticks` / 2) * 60.
    *   (Most PC fans pulse twice per full rotation).
4.  **Report**:
    *   From **Text**, print "Actual Speed: [rpm] RPM".
5.  **Reset**:
    *   Set `ticks` = 0 and repeat.

### 9. Execution Flow
1.  **Start**: The fan begins spinning at a standard test speed.
2.  **Sense**: As the fan turns, its internal Hall-Effect sensor sends digital pulses to GP14.
3.  **Process**: The Pico counts exactly how many pulses occur in one second.
4.  **Math**: It divides the count by 2 (full turn) and multiplies by 60 (to get a full minute).
5.  **Output**: The final RPM is displayed on the screen, showing the real physical results of the code.

### 10. Generated Code
```python
import machine, time

# Tach pin needs a Pull-Up as it is usually Open-Drain
tach = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)
fan.duty_u16(45000)

count = 0
def handle_pulse(pin):
    global count
    count += 1

# Using an Interrupt for accuracy
tach.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_pulse)

while True:
    count = 0 
    time.sleep(1) # Count for precisely one second
    
    # PC Fans: 2 pulses per revolution
    rpm = (count / 2) * 60
    print(f"RPM: {int(rpm)}")
```

### 11. Common Mistakes
*   **Polling Frequency**: Trying to count pulses in a normal `while True` loop. If the fan is fast (3000 RPM), it's pulsing 100 times/second—too fast for a normal loop to catch. Use an Interrupt (IRQ).

### 12. Try This Next
*   **Stall Alarm**: If the PWM is set to 60000 but the RPM remains 0, turn on a warning LED (The fan is stuck!).
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0541 + p0542 + p0543 + p0544 + p0545 + p0546 + p0547 + p0548 + p0549 + p0550)
    
    print("Batch 55 (0541-0550) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch55_v2()
