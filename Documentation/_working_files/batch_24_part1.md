
# BATCH 24: Simple Motors 2 (Projects 0231-0240)

## 1. Project 0231: Introduction to Simple Motors

### 2. Learning Objective
Explore H-Bridge polarity control (Motor Direction). Learn how to use a motor driver to switch the flow of current, allowing a DC motor to rotate both Clockwise (Forward) and Counter-Clockwise (Backward) via software commands.

### 3. Concepts Introduced
*   **H-Bridge Principles**: Using logic pins to control high-current power flow.
*   **Bi-directional Rotation**: Swapping positive and negative terminals internally.
*   **Neutral State (Brake/Coast)**: Stopping a motor by removing power or shorting terminals.

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Motor
*   H-Bridge Motor Driver (e.g., L298N or MX1508)
*   External Power Supply (6-12V)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Input 1 (IN1)** | GP15 | Controls Direction A |
| **Motor Input 2 (IN2)** | GP14 | Controls Direction B |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (duration control)

### 7. Variables
*   **None**: this is a fixed execution sequence.

### 8. Step-by-Step Guide

**A. Forward Phase**
1.  **Spin Forward**:
    *   **Set** GP15 -> HIGH (1).
    *   **Set** GP14 -> LOW (0).
    *   From **Time**, **Wait** 2 seconds.

**B. Stop Phase**
2.  **Cut Power**:
    *   **Set** GP15 -> LOW (0).
    *   **Set** GP14 -> LOW (0).
    *   **Wait** 1 second.

**C. Backward Phase**
3.  **Reverse Polarity**:
    *   **Set** GP15 -> LOW (0).
    *   **Set** GP14 -> HIGH (1).
    *   **Wait** 2 seconds.

**D. Loop Phase**
4.  **Finish**: **Wait** 1 second before the loop restarts.

### 9. Execution Flow
1.  **Forward**: The Pico tells the driver to put + on wire A and - on wire B. The motor spins forward.
2.  **Wait**: The motor works for 2 seconds.
3.  **Idle**: Both pins are off. The motor coasts to a stop.
4.  **Reverse**: The Pico tells the driver to put - on wire A and + on wire B. The motor spins the other way.
5.  **Result**: Full directional control of a high-power actuator.

### 10. Generated Code
```python
from machine import Pin
import time

# Pins for Motor A
m1 = Pin(15, Pin.OUT)
m2 = Pin(14, Pin.OUT)

while True:
    # Forward
    m1.value(1); m2.value(0)
    time.sleep(2)
    
    # Stop
    m1.value(0); m2.value(0)
    time.sleep(1)
    
    # Backward
    m1.value(0); m2.value(1)
    time.sleep(2)
    
    # Stop
    m1.value(0); m2.value(0)
    time.sleep(1)
```

### 11. Common Mistakes
*   **Power Supply**: Don't try to power a DC motor directly from the Pico pins; it will damage the board. Always use a motor driver and a battery pack.
*   **Common Ground**: Ensure the battery's negative terminal is connected to the Pico's GND pin.

### 12. Try This Next
*   **Fast Flips**: remove the "Stop" waits and see how the motor reacts to instant direction changes.
*   **Speed Control**: try to use PWM instead of simple HIGH/LOW to make the motor spin slower.

---

## 1. Project 0232: Blinking Simple Motors

### 2. Learning Objective
Explore speed modulation via PWM (Pulse Width Modulation). Learn how to vary the "Average" power delivered to a motor to control its speed (Slow vs. Fast) and observe the physical and relationship between duty cycle and kinetic energy.

### 3. Concepts Introduced
*   **PWM Speed Control**: Rapidly turning a motor ON and OFF to simulate lower voltages.
*   **Switching Frequency**: noticing how the motor "whines" at different frequencies.
*   **Inertia**: how the motor's weight helps it stay spinning during the "OFF" parts of the pulse.

### 4. Hardware Required
*   Raspberry Pi Pico
*   DC Motor + Driver
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Drive A** | GP15 | PWM controlled speed |
| **Motor Drive B** | GP14 | Held LOW (0) |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_pwm_write`** (set Speed)
*   **from Time, drag `pico_wait`** (interval control)

### 7. Variables
*   **None**: this alternates between two fixed power levels.

### 8. Step-by-Step Guide

**A. Start Phase**
1.  **Configure Driver**: Ensure GP14 is strictly LOW to define one direction.
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Slow Phase**
3.  **Low Power Energy**:
    *   From **Actuators**, **Set** GP15 Speed to **25%**. 
    *   From **Time**, **Wait** 2 seconds.

**C. Fast Phase**
4.  **Full Power Energy**:
    *   From **Actuators**, **Set** GP15 Speed to **100%**.
    *   From **Time**, **Wait** 2 seconds.

### 9. Execution Flow
1.  **Read**: The Pico starts the loop.
2.  **Slow**: It sends power to the motor only 25% of the time. The motor spins with very little torque and a low hum.
3.  **Transition**: After 2 seconds, the Pico jumps to 100%.
4.  **Fast**: The motor receives continuous power. It spins at maximum RPM with a high-pitched whine.
5.  **Cycle**: This creates a "Loud/Quiet" or "Fast/Slow" pattern that repeats forever.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Motor pin with PWM capability
m_a = PWM(Pin(15))
m_b = Pin(14, Pin.OUT)

# Standard motor PWM frequency
m_a.freq(1000)
m_b.value(0)

while True:
    # 25% Speed (approx 16384 out of 65535)
    m_a.duty_u16(16383)
    print("Slow Mode")
    time.sleep(2)
    
    # 100% Speed
    m_a.duty_u16(65535)
    print("Fast Mode")
    time.sleep(2)
```

### 11. Common Mistakes
*   **Threshold of Motion**: Some motors won't move at all below 20% power because they can't overcome their own friction. If it just "hums" but doesn't spin, increase the slow speed to 35%.
*   **Wrong Pin**: Ensure you are applying PWM to the "Forward" pin while the "Backward" pin is grounded.

### 12. Try This Next
*   **Smooth Ramp**: create a loop that slowly increases speed from 0% to 100% over 10 seconds.
*   **Reverse Speed**: swap the pins and try running at 50% speed backwards.

---

## 1. Project 0233: Manual Simple Motors Control

### 2. Learning Objective
Explore differential steering (Tank Logic). Learn how to combine two independent motor controls with two physical buttons to create a remote control system where individual wheel power determines the vehicle's direction.

### 3. Concepts Introduced
*   **Differential Drive**: Steering by varying the relative speeds of left and right wheels.
*   **Interactive Actuation**: Linking software outputs directly to momentary button states.
*   **Straight-Line Coordination**: syncing two motors for forward motion.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Motors + 2 Drivers (or Dual Driver)
*   2 Buttons (Left/Right)
*   External Power Supply

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Left Motor** | GP15 | Forward Control |
| **Right Motor** | GP14 | Forward Control |
| **Button L** | GP13 | Primary Input |
| **Button R** | GP12 | Primary Input |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking inputs)
*   **from Smart IO, drag `pico_gpio_write`** (motor control)

### 7. Variables
*   **None**: this uses direct polling logic.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Left Side Control**
2.  **Check Button L**:
    *   If **Button** GP13 is Pressed: **Set** Left Motor (GP15) -> HIGH.
    *   Else: **Set** Left Motor -> LOW.

**C. Right Side Control**
3.  **Check Button R**:
    *   If **Button** GP12 is Pressed: **Set** Right Motor (GP14) -> HIGH.
    *   Else: **Set** Right Motor -> LOW.

### 9. Execution Flow
1.  **Push Left**: Only the left wheel spins. The robot pivots to the right (Stationary turn).
2.  **Push Right**: Only the right wheel spins. The robot pivots to the left.
3.  **Push Both**: Both wheels spin at the same speed. The robot moves straight forward.
4.  **Result**: A simple but effective way to navigate a robot using only your fingers.

### 10. Generated Code
```python
from machine import Pin
import time

# Inputs
btn_l = Pin(13, Pin.IN, Pin.PULL_DOWN)
btn_r = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Outputs (Forward Pins only for this demo)
mot_l = Pin(15, Pin.OUT)
mot_r = Pin(14, Pin.OUT)

while True:
    # Left Motor Control
    if btn_l.value() == 1:
        mot_l.value(1)
    else:
        mot_l.value(0)
        
    # Right Motor Control
    if btn_r.value() == 1:
        mot_r.value(1)
    else:
        mot_r.value(0)
        
    time.sleep(0.01) # Ultra-fast response
```

### 11. Common Mistakes
*   **Inversion**: If the robot turns Left when you press the Right button, you have swapped your motor wires or your button pins.
*   **Current Limit**: Running two motors at once takes a lot of battery. If the Pico restarts when you press both buttons, your batteries are too weak.

### 12. Try This Next
*   **Speed Buttons**: Add two more buttons that run the motors at 50% speed for "Precise" mode.
*   **Reverse Logic**: Add a third button that reverses BOTH motors to backup.

---

## 1. Project 0234: Simple Motors Sequences

### 2. Learning Objective
Explore open-loop path planning (The Figure 8). Learn how to program a precise sequence of timed motor activations to command a robot to perform complex geometric maneuvers without human intervention.

### 3. Concepts Introduced
*   **Dead Reckoning**: Predicting position based solely on time and speed.
*   **Sequencing Turns**: calculating the duration needed (e.g., 0.8s) to reach a 90-degree angle.
*   **Subroutine Execution**: repeating chunks of code for consistent path tracing.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Robot Chassis (2 Motors + Driver)
*   Floor space (preferably smooth)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Left Motor** | GP15 | Wheel A |
| **Right Motor** | GP14 | Wheel B |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set direction)
*   **from Time, drag `pico_wait`** (movement duration)

### 7. Variables
*   **None**: this is a hard-coded geometric routine.

### 8. Step-by-Step Guide

**A. Forward Maneuver**
1.  **Stage 1 (Straight)**:
    *   **Set** BOTH GP15 and GP14 -> HIGH.
    *   **Wait** 2 seconds.

**B. Turning Maneuver (Right)**
2.  **Stage 2 (Right Turn)**:
    *   **Set** GP15 -> HIGH. **Set** GP14 -> LOW.
    *   **Wait** 1 second (Adjust this until it makes a curved turn).

**C. Second Forward**
3.  **Stage 3 (Straight)**:
    *   **Set** BOTH HIGH.
    *   **Wait** 2 seconds.

**D. Turning Maneuver (Left)**
4.  **Stage 4 (Left Turn)**:
    *   **Set** GP15 -> LOW. **Set** GP14 -> HIGH.
    *   **Wait** 1 second.

**E. Loop**
5.  **Restart**: Place all blocks inside a `pico_forever` loop.

### 9. Execution Flow
1.  **Run**: The robot drives forward 2 meters.
2.  **Arc**: It swings to the right, tracing the first loop of the "8".
3.  **Connect**: It drives forward again.
4.  **Arc**: It swings to the left, completing the second loop.
5.  **Result**: Autonomous navigation based on calibrated time segments.

### 10. Generated Code
```python
from machine import Pin
import time

l_mot = Pin(15, Pin.OUT)
r_mot = Pin(14, Pin.OUT)

def go_straight(s):
    l_mot.value(1); r_mot.value(1); time.sleep(s)

def turn_right(s):
    # Pivot on right wheel
    l_mot.value(1); r_mot.value(0); time.sleep(s)

def turn_left(s):
    # Pivot on left wheel
    l_mot.value(0); r_mot.value(1); time.sleep(s)

def stop():
    l_mot.value(0); r_mot.value(0); time.sleep(1)

while True:
    print("Tracing Figure 8...")
    go_straight(2)
    turn_right(1.5) # Tune for curve
    go_straight(2)
    turn_left(1.5)  # Tune for curve
    stop()
```

### 11. Common Mistakes
*   **Surface Friction**: A 1-second turn on carpet will be much shorter than a 1-second turn on wood. You MUST recalibrate your wait times every time you move the robot.
*   **Battery Drain**: As the battery gets weaker, the robot will move slower and the "Figure 8" will get smaller or lopsided.

### 12. Try This Next
*   **The Square**: Change the sequence to: Forward 2s, Sharp Turn 0.5s (4 times).
*   **The S-Curve**: constantly vary the speeds of the two motors using PWM inside a loop.

---

## 1. Project 0235: Interactive Simple Motors

### 2. Learning Objective
Explore phototaxis (Light Following). Learn how to create an autonomous feedback loop where two Light Sensors (LDRs) serve as "Eyes" for the robot, causing it to balance motor speeds to dynamically track a flashlight beam.

### 3. Concepts Introduced
*   **Analog Feedback Loops**: adjusting motor power based on varying sensor voltages.
*   **Phototaxis**: movement of an organism/robot in response to light.
*   **Differential Scaling**: Making a motor "push harder" when its side of the robot is dark to steer back toward the light.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Robot Chassis
*   2 Photoresistors (LDRs)
*   2 10k Resistors
*   Flashlight

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR Left** | GP26 (ADC0) | Left Eye |
| **LDR Right** | GP27 (ADC1) | Right Eye |
| **Motor L** | GP15 | Controlled by Right eye |
| **Motor R** | GP14 | Controlled by Left eye |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read Light)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Actuators, drag `pico_pwm_write`** (set Motor Speed)

### 7. Variables
*   **left_light**, **right_light**: raw sensor values.
*   **speed_L**, **speed_R**: calculated motor duty cycles.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Read Ambient Light**:
    *   **Set** `left_light` = **Sensors** `pico_analog_read` GP26.
    *   **Set** `right_light` = **Sensors** `pico_analog_read` GP27.

**B. Logic Phase (Feedback)**
3.  **Determine Navigation**:
    *   If `left_light` is much brighter than `right_light`:
        *   **Set** Motor R speed HIGH. **Set** Motor L speed LOW. (This swings the robot Left).
    *   Else if `right_light` is brighter:
        *   **Set** Motor L speed HIGH. **Set** Motor R speed LOW. (Swings Right).
    *   Else (balanced):
        *   Both motors HIGH.

### 9. Execution Flow
1.  **Center**: Light is shining from directly in front. Both "Eyes" see equal brightness. Both motors push equally. The robot drives forward.
2.  **Deviation**: You move the flashlight to the left. The Left Eye sees 80% light, Right Eye only 20%.
3.  **Adjustment**: The code detects the imbalance. It slows down the Left wheel and speeds up the Right wheel.
4.  **Result**: The robot pivots until the light is centered again. It successfully "Hunts" the light across the room.

### 10. Generated Code
```python
import machine
import utime

# Eyes
eye_l = machine.ADC(machine.Pin(26))
eye_r = machine.ADC(machine.Pin(27))

# Wheels
mot_l = machine.PWM(machine.Pin(15))
mot_r = machine.PWM(machine.Pin(14))
mot_l.freq(1000); mot_r.freq(1000)

while True:
    # Get light levels (0-65535)
    val_l = eye_l.read_u16()
    val_r = eye_r.read_u16()
    
    # Brain: If left is bright, turn left!
    # To turn left, Right wheel must push HARDER than Left wheel.
    if val_l > val_r + 5000: # Significant difference
        mot_l.duty_u16(20000) # Slow
        mot_r.duty_u16(60000) # Fast
    elif val_r > val_l + 5000:
        mot_l.duty_u16(60000) # Fast
        mot_r.duty_u16(20000) # Slow
    else:
        # Both fast forward
        mot_l.duty_u16(40000)
        mot_r.duty_u16(40000)
        
    utime.sleep(0.1)
```

### 11. Common Mistakes
*   **Room Light**: if the room is naturally very bright, the small difference from a flashlight might not be detectable. You may need to shield your LDRs with "blinkers" (small tubes) to make them directional.
*   **Cross-Wiring**: If the robot runs away from the light, simply swap the speed commands in your `if` logic.

### 12. Try This Next
*   **Light Fleeing**: Swap the logic so the robot hides in the darkest corner of the room when it sees light.
*   **Proportional Drive**: instead of IF/ELSE, make the speed *exactly* proportional to the light reading for a smoother "Organic" movement.

---
