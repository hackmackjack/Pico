import os

def build_batch55():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0541 = """
---

# Batch 55: Smart Fan 3

## 1. Project 0541: Introduction to Smart Fan

### 2. Learning Objective
Implement a "Soft Start" feature by gradually increasing the fan's speed from 0% to 100% in controlled increments using PWM.

### 3. Concepts Introduced
*   PWM (Pulse Width Modulation)
*   Ramping/Duty Cycle Sweeping
*   Motor Inertia Management
*   Incremental Loops

### 4. Hardware Required
*   Raspberry Pi Pico
*   Motor Driver (DRV8833 or similar)
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pico VBUS** | Motor VCC | Power Fan |
| **GND** | Motor GND | Shared Ground |
| **Motor IN1** | GP16 | PWM Control |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (Scale 0 to 65000)
*   **from Smart IO, drag `pico_pwm_write`** (Set speed)
*   **from Time, drag `pico_wait`** (Control ramp speed)

### 7. Variables
*   **fan_speed**: Integer (Target PWM duty cycle)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**: Set GP16 at 1000Hz frequency.

**B. Main Loop Phase**
2.  **Start Ramp**:
    *   From **Loops**, drag `count_with`.
    *   Set variable `fan_speed`, Range 0 to 65000, Step 650.
3.  **Apply Speed**:
    *   From **Smart IO**, set GP16 (PWM) to `fan_speed`.
4.  **Wait**:
    *   From **Time**, wait 0.1 seconds.
5.  **Hold**:
    *   Once at 100% (65000), wait 2 seconds, then reset.

### 9. Execution Flow
1.  **Start**: Pico initializes the PWM hardware.
2.  **Iterate**: The code begins a loop that increases the "duty cycle" (the amount of time power is ON).
3.  **Actuation**: The motor starts with tiny pulses and gradually receives longer pulses as the loop progresses.
4.  **Output**: The fan spins up smoothly from a standstill to full speed without a sudden current draw.
5.  **Repeat**: The sequence restarts after a short delay.

### 10. Generated Code
```python
import machine
import time

fan = machine.PWM(machine.Pin(16))
fan.freq(1000)

while True:
    # Ramp Up
    for duty in range(0, 65536, 655):
        fan.duty_u16(duty)
        time.sleep(0.1)
    
    # Stay at Full for a moment
    time.sleep(2)
```

### 11. Common Mistakes
*   **Frequency Logic**: Using a frequency that is too low (e.g., 50Hz) might make the motor whine or vibrate. Use 1000Hz+ for DC motors.
*   **Wait Time**: If the wait time is 0, the ramp happens so fast the fan essentially just "snaps" to full speed.

### 12. Try This Next
*   **Ramp Down**: After reaching 100%, add another loop that counts from 65000 back to 0.
"""

    p0542 = """
---

## 1. Project 0542: Blinking Smart Fan

### 2. Learning Objective
Create a "Gust Mode" simulator where the fan runs at a steady low speed but occasionally surges to maximum power at random intervals.

### 3. Concepts Introduced
*   Probabilistic Logic
*   Transient Loading
*   Environment Simulation (Wind)
*   Baseline vs Peak states

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Motor Driver

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor IN** | GP16 | Speed control |

### 6. Blocks Used
*   **from Math, drag `random_integer`** (Decide timing)
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **is_gusting**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init PWM**: Set GP16 to 1000Hz.

**B. Main Loop Phase**
2.  **Steady State**:
    *   From **Smart IO**, set GP16 (PWM) to 15000 (roughly 20% speed).
3.  **Roll the Dice**:
    *   Wait random duration (1 to 5 seconds).
4.  **Activate Gust**:
    *   Print "Incoming Wind Gust!".
    *   From **Smart IO**, set GP16 (PWM) to 65000 (Full power).
    *   Wait 0.5 seconds.
5.  **Return**:
    *   Set GP16 back to 15000.

### 9. Execution Flow
1.  **Observe**: The fan provides a gentle constant breeze.
2.  **Decide**: The processor picks a random "quiet" period.
3.  **Surge**: Suddenly, the fan speeds up to 100% for a very short burst (0.5s).
4.  **Settle**: The fan immediately returns to its baseline "breeze" speed.
5.  **Wait**: The cycle repeats with a different random delay each time.

### 10. Generated Code
```python
import machine
import time
import random

fan = machine.PWM(machine.Pin(16))
fan.freq(1000)

while True:
    # Baseline Breeze
    fan.duty_u16(15000)
    
    # Wait for random onset
    time.sleep(random.uniform(1, 4))
    
    # Gust Surge
    print("GUST!")
    fan.duty_u16(65000)
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Gust duration**: Making the gust too long (e.g., 10 seconds) makes it feel like a permanent speed change rather than a gust. Keep it under 1 second.

### 12. Try This Next
*   **Variable Gusts**: Instead of always 100%, make the gust speed also random (e.g., between 40,000 and 65,000).
"""

    p0543 = """
---

## 1. Project 0543: Manual Smart Fan Control

### 2. Learning Objective
Implement a multi-state gear system where a single button cycle the fan through "Low", "Medium", "High", and "Off" positions.

### 3. Concepts Introduced
*   State Cycle (Counter Loops)
*   Modulo for Wrap-around
*   Discrete Power Levels
*   User Input Interfaces

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Push Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Selector Button** | GP14 | Cycle speeds |
| **Fan Control** | GP16 | PWM Output |

### 6. Blocks Used
*   **from Logic, drag `if_elseif`** (Multi-state check)
*   **from Variables, drag `change_variable`** (State = State + 1)
*   **from Math, drag `modulo`** (0-3 wrap)

### 7. Variables
*   **mode**: Integer (0, 1, 2, or 3)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Button (Input/Pull-Down), Fan (PWM Output).
2.  **Reset Mode**: Set `mode` to 0.

**B. Main Loop Phase**
3.  **Check Click**:
    *   If GP14 is HIGH:
        *   Increment `mode` by 1.
        *   If `mode` > 3: Set `mode` to 0.
        *   Wait 0.3s (Debounce).
4.  **Set Speed Based on Mode**:
    *   **If mode = 1**: Set PWM to 20000 (Low).
    *   **Else If mode = 2**: Set PWM to 40000 (Medium).
    *   **Else If mode = 3**: Set PWM to 65000 (High).
    *   **Else (mode = 0)**: Set PWM to 0 (Off).

### 9. Execution Flow
1.  **Start**: The fan is stationary (Mode 0).
2.  **Input**: User presses the button once.
3.  **Logic**: The `mode` becomes 1. The code matching mode 1 activates the "Low" PWM signal.
4.  **Cycle**: Repeated presses move the state from $1 \Rightarrow 2$ (Med), $2 \Rightarrow 3$ (High), and finally $3 \Rightarrow 0$ (Off).
5.  **Feedback**: The visual speed of the fan changes instantly with each click.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)

mode = 0 # 0=Off, 1=Low, 2=Med, 3=High

while True:
    if button.value():
        mode = (mode + 1) % 4
        print("Mode switched to:", mode)
        time.sleep(0.3)
        
    if mode == 1: fan.duty_u16(20000)
    elif mode == 2: fan.duty_u16(40000)
    elif mode == 3: fan.duty_u16(65000)
    else: fan.duty_u16(0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Modulo Confusion**: Using `% 3` instead of `% 4`. If modes are 0,1,2,3... you have 4 states. `% 3` would only reach 0,1,2.
*   **Floating State**: Not using `else` for mode 0—this might keep the fan at High even if you return to mode 0.

### 12. Try This Next
*   **LED Indicators**: Add 3 LEDs that light up to show which gear is currently selected.
"""

    p0544 = """
---

## 1. Project 0544: Smart Fan Sequences

### 2. Learning Objective
Create a compound motion system where a Servo motor pan-oscillates while a DC fan provides airflow, simulating a pedestal oscillating fan.

### 3. Concepts Introduced
*   Compound Motion
*   Servo Integration
*   Coordinated Timing
*   Mechanical Sweep Logic

### 4. Hardware Required
*   Raspberry Pi Pico
*   SG90 Servo (Base)
*   DC Fan (Mounted on Servo)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo Signal** | GP15 | Panning control |
| **Fan IN** | GP16 | Speed control |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`** (0 to 180)
*   **from Loops, drag `count_with`** (Slow sweep)
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **angle**: Integer (Current pan position)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Motors**: Setup Servo on GP15 and Fan on GP16.
2.  **Power On**: Set Fan to constant medium speed (30000).

**B. Main Loop Phase**
3.  **Sweep Right**:
    *   From **Loops**, `count_with` `angle` from 0 to 180 (Step 2).
    *   Set Servo to `angle`.
    *   Wait 0.02s.
4.  **Sweep Left**:
    *   From **Loops**, `count_with` `angle` from 180 to 0 (Step 2).
    *   Set Servo to `angle`.
    *   Wait 0.02s.

### 9. Execution Flow
1.  **Start**: The fan begins spinning independently.
2.  **Move**: The servo motor receives a sequence of angle updates (0, 2, 4...).
3.  **Pan**: Because the fan is glued/mounted to the servo horn, the air stream sweeps across the room.
4.  **Inertia Control**: Small waits between angle steps ensure the servo moves smoothly rather than jerkily.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Helper for Servo (Standard PWM)
srv = PWM(Pin(15)); srv.freq(50)
def set_angle(a):
    duty = int(1638 + (a * 6554 / 180))
    srv.duty_u16(duty)

fan = PWM(Pin(16)); fan.freq(1000)
fan.duty_u16(40000) # Steady Breeze

while True:
    # Right
    for a in range(0, 181, 2):
        set_angle(a)
        time.sleep(0.02)
    # Left
    for a in range(180, -1, -2):
        set_angle(a)
        time.sleep(0.02)
```

### 11. Common Mistakes
*   **Current Limit**: Running a DC fan and a Servo at the same time might exceed the current limit of the Pico's 5V pin. Use an external battery for the motors if they jitter.

### 12. Try This Next
*   **Dynamic Speed**: Slow the fan down when it's at the edges (0 and 180) and speed it up when it's facing center (90).
"""

    p0545 = """
---

## 1. Project 0545: Interactive Smart Fan

### 2. Learning Objective
Develop an "Air-to-Air" switch where blowing into a microphone or a small secondary fan triggers the main DC fan to start.

### 3. Concepts Introduced
*   Analog Sensing (Noise/Wind)
*   Input-Triggered Feedback
*   Calibration Thresholds
*   Signal Processing (Envelope)

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor or Wind Sensor (Analog)
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Wind Sensor** | GP26 (ADC) | Measure air pressure/sound |
| **Fan IN** | GP16 | Main output |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Logic, drag `greater_than`** (Detect blow)
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **breath**: Integer (Analog input level)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Init ADC(26) and PWM(16).

**B. Main Loop Phase**
2.  **Monitor "Breath"**:
    *   Set `breath` to `pico_adc_read` (GP26).
3.  **Trigger logic**:
    *   If `breath` > 40000 (Adjust for your sensor):
        *   Turn Fan ON (Full Speed).
        *   Wait 3 seconds.
    *   Else:
        *   Turn Fan OFF.

### 9. Execution Flow
1.  **Start**: The system is quiet. The main fan is off.
2.  **Sense**: The user blows sharply on the sensor.
3.  **Threshold**: The analog voltage spikes due to the vibration/pressure.
4.  **Reaction**: The code detects this jump and turns the main fan on for a multi-second timer.
5.  **Stop**: Once the timer ends, the fan shuts off until another breath is detected.

### 10. Generated Code
```python
import machine
import time

sensor = machine.ADC(26)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)

while True:
    val = sensor.read_u16()
    
    if val > 35000: # Threshold for 'blowing'
        print("Breath Detected! Fan ACTIVE.")
        fan.duty_u16(65000)
        time.sleep(3) # Run for 3 seconds
    else:
        fan.duty_u16(0)
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Threshold Sensitivity**: Ambient room noise might trigger the sensor. Always print your sensor values to the terminal first to find the "Silent" vs "Blow" numbers.

### 12. Try This Next
*   **Proportional blow**: The harder you blow, the faster the main fan runs (Proportional Control).
"""

    p0546 = """
---

## 1. Project 0546: Smart Smart Fan Switch

### 2. Learning Objective
Integrate a "Sleep Timer" function that runs the fan for a set duration after a button press and then enters an energy-saving "Off" state automatically.

### 3. Concepts Introduced
*   Timer-based Shutoff
*   Blocking vs Non-blocking Delays
*   Status Reporting
*   Power Saving

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan
*   Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Start Button** | GP14 | Start Timer |
| **Fan IN** | GP16 | Main output |

### 6. Blocks Used
*   **from Time, drag `pico_wait`** (Controlled duration)
*   **from Logic, drag `if_do`**
*   **from Text, drag `print`**

### 7. Variables
*   **None**: Direct sequential control.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: Button (In), Fan (Out).

**B. Main Loop Phase**
2.  **Idle Check**: Wait for GP14 to be HIGH.
3.  **Execution Phase**:
    *   Print "Timer Started - Cooling for 10 seconds".
    *   Turn Fan ON (Medium).
    *   **Wait** 10 seconds (Simulating 30 minutes).
4.  **Auto-Stop**:
    *   Print "Time Up. Shutting down."
    *   Turn Fan OFF.
5.  **Resume**: Loop returns to step 2 to wait for next button press.

### 9. Execution Flow
1.  **Ready**: System waits in a low-power "check" loop.
2.  **Trigger**: User hits the "Nap" button.
3.  **Active**: The fan provides airflow for the specified duration.
4.  **Monitoring**: The code effectively "counts down" by waiting.
5.  **Shutoff**: Once the time expires, the fan ceases, ensuring it doesn't run all night if not needed.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)

while True:
    if btn.value():
        # Start Timer
        fan.duty_u16(30000)
        print("Fan Active for 10 seconds...")
        time.sleep(10) # Simple blocking logic
        
        # Shut down
        fan.duty_u16(0)
        print("Shutdown Complete.")
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Blocking Error**: Using `time.sleep(10)` means the button won't work to *cancel* the timer once it starts. (Advanced: Use a while loop with a break condition).

### 12. Try This Next
*   **Add Cancel**: Make it so if you press the button AGAIN while it's running, it stops early.
"""

    p0547 = """
---

## 1. Project 0547: Smart Fan Alarm System

### 2. Learning Objective
Design a safety "Lockout" system that monitors for hardware faults (simulated by a button) and disables the fan until a manual reset is performed.

### 3. Concepts Introduced
*   Fault Detection
*   Lockout States (Latches)
*   Manual Reset logic
*   Safety Protocols

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Push Buttons (Fault, Reset)
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fault Sensor** | GP14 | Simulates Overheat |
| **Reset Switch** | GP15 | Safety Reset |
| **Fan IN** | GP16 | Output |

### 6. Blocks Used
*   **from Variables, drag `set_variable`** (Flag state)
*   **from Logic, drag `if_else`**

### 7. Variables
*   **system_fault**: Boolean (Latch)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: 2 Buttons (Inputs), Fan (Output).
2.  **Clear Flags**: `system_fault = FALSE`.

**B. Main Loop Phase**
3.  **Monitor Fault**:
    *   If GP14 is HIGH:
        *   `system_fault = TRUE`.
        *   Turn Fan OFF immediately.
4.  **Monitor Reset**:
    *   If GP15 is HIGH:
        *   `system_fault = FALSE`. (Only if conditions safe).
5.  **Control Logic**:
    *   If `system_fault` is FALSE:
        *   Allow Fan to run (Normal).
    *   Else:
        *   Keep Fan OFF and Print "FAULT DETECTED - RESTART REQUIRED".

### 9. Execution Flow
1.  **Observe**: Fan runs normally.
2.  **Detect**: Overheat occurs (Button 1 pressed).
3.  **Lockdown**: The `system_fault` flag turns TRUE. The fan stops.
4.  **Memory**: Even if the overheat button is released, the fan **stays off** because the variable is still "True".
5.  **Restore**: The system only returns to work when a second, deliberate "Reset" button is hit.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

fault_btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
reset_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)
fan = PWM(Pin(16)); fan.freq(1000)

faulted = False

while True:
    # 1. Fault check
    if fault_btn.value():
        faulted = True
        print("!!! OVERHEAT FAULT !!!")
        
    # 2. Reset check
    if reset_btn.value():
        faulted = False
        print("System Reset.")
        
    # 3. Execution
    if not faulted:
        fan.duty_u16(30000)
    else:
        fan.duty_u16(0)
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Missing Latch**: If you don't use the `system_fault` variable and just check `if button pressed: fan.off()`, the fan will start again as soon as the button is released—this is UNSAFE. Real cooling systems must be manually reset.

### 12. Try This Next
*   **Audible Alarm**: Add a buzzer that sounds continuously as long as the system is in the "Fault" state.
"""

    p0548 = """
---

## 1. Project 0548: The Smart Fan Game

### 2. Learning Objective
Build a "Hover Challenge" where the user must adjust a potentiometer to balance a light object (like a ping pong ball) at a specific height in an airstream.

### 3. Concepts Introduced
*   User-in-the-Loop Control
*   Analog-to-PWM mapping
*   Aerodynamics Basics
*   Equilibrium and Balance

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Fan (Blowing UP)
*   10kΩ Potentiometer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Hover Control** | GP26 (ADC) | Adjust speed |
| **Fan IN** | GP16 | Speed output |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Math, drag `map_range`**
*   **from Smart IO, drag `pico_pwm_write`**

### 7. Variables
*   **knob_val**: Integer (0-65535)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: ADC(26) and PWM(16).

**B. Main Loop Phase**
2.  **Read Knob**:
    *   Set `knob_val` to `pico_adc_read` (GP26).
3.  **Control Hover**:
    *   From **Smart IO**, set GP16 (PWM) to `knob_val`.
4.  **Challenge**:
    *   Try to find the exact PWM value where the ball stays perfectly still in mid-air.
    *   Print to screen: "Current Lift Power: [knob_val]".

### 9. Execution Flow
1.  **Input**: User turns the potentiometer.
2.  **Conversion**: The analog voltage is read by the Pico.
3.  **Actuation**: The fan speed changes proportionally to the knob.
4.  **Reaction**: The air pressure pushes the ball upward.
5.  **Skill**: The user must provide enough power to resist gravity, but not so much that the ball flies out of the tube.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)

while True:
    reading = pot.read_u16()
    
    # Map reading directly to fan strength
    fan.duty_u16(reading)
    
    # Visual check
    print(f"Lift: {int(reading/655)}%")
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **PWM Minimum**: Most fans won't spin below a certain PWM (e.g., 10000). If the knob is at 0, the ball will just sit on the fan.
*   **Sensor Noise**: Small jitters in the knob might cause the ball to wobble. (Solution: See Project 0539 "Smoothing").

### 12. Try This Next
*   **Target Game**: Draw a line on the tube and see how long you can keep the ball perfectly centered on the line.
"""

    p0549 = """
---

## 1. Project 0549: Automated Smart Fan

### 2. Learning Objective
Create an automated environment controller that independently activates an exhaust fan when relative humidity levels exceed a safe threshold ($70\%$).

### 3. Concepts Introduced
*   Environmental Thresholds
*   Sensor Libraries (DHT11)
*   Automated Remediation
*   Wait Sampling (Don't check every microsecond)

### 4. Hardware Required
*   Raspberry Pi Pico
*   DHT11 or DHT22 Sensor
*   DC Fan

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT11 Data** | GP15 | Humidity sensor |
| **Fan IN** | GP16 | Exhaust output |

### 6. Blocks Used
*   **from Sensors, drag `pico_dht_read`** (Measure humidity)
*   **from Logic, drag `greater_than`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **current_hum**: Integer (0-100%)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config Hardware**: GP15 (Sensor), GP16 (Fan).

**B. Main Loop Phase**
2.  **Sample Room**:
    *   From **Sensors**, set `current_hum` to Humidity check.
3.  **Evaluate Moisture**:
    *   From **Logic**, drag `if_else`.
    *   Condition: `current_hum` > 70.
4.  **Control**:
    *   **If High**: Turn Fan ON (Exhaust moisture).
    *   **Else**: Turn Fan OFF (Conservation).
5.  **Sleep**: Wait 2s (DHT sensors need time between reads).

### 9. Execution Flow
1.  **Monitor**: Pico checks the moisture in the air every few seconds.
2.  **Compare**: It compares the room's humidity against the setpoint (70).
3.  **Action**: If the air is "Damp", the fan is triggered to blow it out.
4.  **Shutoff**: Once the room is dry enough, the fan turns off automatically.

### 10. Generated Code
```python
import machine
import dht
import time

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
        print("Sensor read error.")
        
    time.sleep(2)
```

### 11. Common Mistakes
*   **Check frequency**: Reading a DHT11 more than once per second will lead to errors or overheating the sensor.
*   **Incorrect Logic**: Turning the fan ON when humidity is LOW (unless it's a humidifier project).

### 12. Try This Next
*   **Multi-Trigger**: Make the fan turn on if it's too HOT OR too HUMID.
"""

    p0550 = """
---

## 1. Project 0550: Mastering Smart Fan

### 2. Learning Objective
Learn to read hardware feedback by calculating the Revolutions Per Minute (RPM) of a fan using its internal Tachometer (Hall-Effect) pulse.

### 3. Concepts Introduced
*   Feedback Frequency
*   Pulse Counting
*   Math-to-RPM conversion
*   Microsecond Timing (`ticks_us`)

### 4. Hardware Required
*   Raspberry Pi Pico
*   3-wire or 4-wire PC Fan (with Tach Pin)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fan Tach** | GP14 | Input (Hall pulse) |
| **Fan IN** | GP16 | PWM speed |

### 6. Blocks Used
*   **from Time, drag `pico_microseconds`**
*   **from Variables, drag `change_variable`**
*   **from Math, drag `multiplication`**

### 7. Variables
*   **pulses**: Integer (Count of ticks)
*   **rpm**: Integer (Final calculated value)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: GP14 (In/Pull-Up), GP16 (PWM).
2.  **Start Fan**: Set PWM to 50% so we have speed to measure.

**B. Measurement Phase**
3.  **Timed Window**:
    *   Record `start_time` = milliseconds.
    *   **Loop** for 1000ms:
        *   If GP14 goes from LOW to HIGH: `pulses = pulses + 1`.
4.  **Calculate RPM**:
    *   PC fans typically output 2 pulses per revolution.
    *   `rpm = (pulses / 2) * 60`.
5.  **Report**:
    *   Print to terminal: "Current RPM: [rpm]".
6.  **Reset**: `pulses = 0`.

### 9. Execution Flow
1.  **Spin**: The fan turns, and its internal magnet passes a sensor.
2.  **Tick**: Every time the magnet passes, a pulse is sent to GP14.
3.  **Count**: The Pico counts how many pulses occur in exactly one second.
4.  **Formula**: It divides by 2 (full turn) and multiplies by 60 (to get a full minute).
5.  **Verify**: The user can see if the fan is actually spinning at the rate promised by the software.

### 10. Generated Code
```python
import machine
import time

tach = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
fan = machine.PWM(machine.Pin(16)); fan.freq(1000)
fan.duty_u16(30000) # Run at half speed

count = 0
def pulse_handler(pin):
    global count
    count += 1

# Using an Interrupt for accuracy
tach.irq(trigger=machine.Pin.IRQ_FALLING, handler=pulse_handler)

while True:
    count = 0
    time.sleep(1) # Count for 1 second
    
    # 2 pulses = 1 rev
    revolutions_per_sec = count / 2
    rpm = revolutions_per_sec * 60
    
    print(f"Fan Speed: {int(rpm)} RPM")
```

### 11. Common Mistakes
*   **Poll Rate**: Trying to count pulses using `if button.value == 1` in a standard loop. If the fan is fast (3000 RPM), it's pulsing 100 times per second—the standard loop is often too slow to catch them all. Use an Interrupt (IRQ).

### 12. Try This Next
*   **Stall Detect**: If PWM is > 0 but RPM is 0, sound an alarm (The fan is stuck or broken!).
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0541 + p0542 + p0543 + p0544 + p0545 + p0546 + p0547 + p0548 + p0549 + p0550)
    
    print("Batch 55 (0541-0550) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch55()
