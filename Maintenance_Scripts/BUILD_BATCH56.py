import os

def build_batch56():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0551 = """
---

# Batch 56: Robotic Arm Basics 3

## 1. Project 0551: Introduction to Robotic Arm Basics

### 2. Learning Objective
Accurately position a servo motor to its center point (90 degrees) during the system's initialization phase to ensure a consistent starting state.

### 3. Concepts Introduced
*   Servo Homing (Initialization)
*   PWM Angle Mapping
*   Static Positioning
*   Calibration Basics

### 4. Hardware Required
*   Raspberry Pi Pico
*   SG90 or MG90S Servo
*   Jumper Wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo VCC** | 5V (VBUS) | Red Wire |
| **Servo GND** | GND | Brown/Black Wire |
| **Servo Signal** | GP16 | Orange/White Wire |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`** (Set target angle)
*   **from Smart IO, drag `pico_pwm_write`** (Underlying block)

### 7. Variables
*   **None**: Direct command project.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**: Initialize GP16 as a PWM output at 50Hz (frequency required for hobby servos).
2.  **Move to Center**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into `start` slot.
    *   Set Angle to 90.

**B. Main Loop Phase**
3.  **Hold Position**:
    *   Maintain the setup state. No further motion needed for this task.

### 9. Execution Flow
1.  **Start**: Pico powers up and sets GP16 to the correct frequency (50Hz).
2.  **Calculate**: The `pico_servo_angle` block calculates the correct pulse width for 90 degrees (typically 1.5ms).
3.  **Output**: The signal is sent to the servo controller.
4.  **Reaction**: The servo motor physically rotates the horn to its midpoint.

### 10. Generated Code
```python
import machine
import time

serv = machine.PWM(machine.Pin(16))
serv.freq(50)

# Move to exact center (90 deg)
# Duty calculation: 1.5ms pulse / 20ms period * 65535 total
center_duty = 4915 
serv.duty_u16(center_duty)

print("System Homing Complete. Angle: 90")
```

### 11. Common Mistakes
*   **Incorrect Frequency**: Using 1000Hz (standard LED PWM) instead of 50Hz. Servos will chatter or heat up.
*   **Power Supply**: Attempting to power multiple servos from the Pico's 3.3V pin. Use the 5V (VBUS) pin for better torque.

### 12. Try This Next
*   **Startup Sequence**: Instead of just snapping to 90, make the arm move from 0 to 180 and then back to 90 at startup to "stretch".
"""

    p0552 = """
---

## 1. Project 0552: Blinking Robotic Arm Basics

### 2. Learning Objective
Programm a continuous "Wave" motion by sweeping a servo motor between $0^{\circ}$ and $180^{\circ}$ using a timed loop.

### 3. Concepts Introduced
*   Mechanical Sweep
*   Motion Looping
*   Speed Control via Delays
*   Angular Boundaries

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo Signal** | GP16 | PWN Control |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`**
*   **from Time, drag `pico_wait`**
*   **from Loops, drag `pico_forever`**

### 7. Variables
*   **None**: Sequential command logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Init Servo on GP16.

**B. Main Loop Phase**
2.  **Move to Start**:
    *   From **Motors**, set `pico_servo_angle` to 0.
    *   From **Time**, wait 1 second.
3.  **Move to End**:
    *   From **Motors**, set `pico_servo_angle` to 180.
    *   From **Time**, wait 1 second.
4.  **Repeat**: Loop causes the arm to swing back and forth.

### 9. Execution Flow
1.  **Start**: Program initializes.
2.  **Action 1**: Signal pulse changes to 1.0ms; arm moves to $0^{\circ}$.
3.  **Delay**: System pauses to allow mechanical motion to finish.
4.  **Action 2**: Signal pulse changes to 2.0ms; arm moves to $180^{\circ}$.
5.  **Perception**: The arm appears to be "waving" hello endlessly.

### 10. Generated Code
```python
import machine
import time

srv = machine.PWM(machine.Pin(16))
srv.freq(50)

while True:
    # 0 Degrees
    srv.duty_u16(1638) 
    time.sleep(1)
    
    # 180 Degrees
    srv.duty_u16(8192)
    time.sleep(1)
```

### 11. Common Mistakes
*   **No Wait Time**: If you don't use `sleep()`, the code sends "Move to 180" immediately after "Move to 0". The servo won't have time to actually move before the next signal arrives.
*   **Boundaries**: Some cheap servos can't actually reach 180 and will strain. Try 10 to 170 instead.

### 12. Try This Next
*   **Double Speed**: Reduce `sleep(1)` to `sleep(0.5)` for a faster wave.
"""

    p0553 = """
---

## 1. Project 0553: Manual Robotic Arm Basics Control

### 2. Learning Objective
Implement "Direct Drive" control by mapping the analog voltage of a potentiometer to the physical angle of a servo motor.

### 3. Concepts Introduced
*   Analog-to-Digital Mapping
*   Servo Control Loop
*   Resolution Scaling
*   User Interaction

### 4. Hardware Required
*   Raspberry Pi Pico
*   10kΩ Potentiometer
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Input Controller |
| **Servo Signal** | GP16 | Output Actuator |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Math, drag `map_range`**
*   **from Motors, drag `pico_servo_angle`**

### 7. Variables
*   **control_val**: Integer (ADC Result)
*   **target_angle**: Integer (Mapped result)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**: ADC(26) and Servo(16).

**B. Main Loop Phase**
2.  **Read Knob**:
    *   Set `control_val` to `pico_adc_read` (GP26).
3.  **Map to Angle**:
    *   From **Math**, set `target_angle` to map `control_val` (0-65535) to range (0 to 180).
4.  **Apply Motion**:
    *   From **Motors**, set `pico_servo_angle` to `target_angle`.
5.  **Wait**:
    *   Wait 0.05s to keep the movement smooth.

### 9. Execution Flow
1.  **Sense**: Pico reads the knob's position (e.g., halfway turned = 32767).
2.  **Calculate**: $32767$ is mapped within the $0-180$ range, results in $90$.
3.  **Command**: Servo is told to go to $90^{\circ}$.
4.  **Observe**: As the user turns the knob, the servo's arm follows the rotation synchronously.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

while True:
    # Read 16-bit analog
    raw = pot.read_u16()
    
    # Map to 180 degrees
    # 0=1638 duty, 180=8192 duty
    angle = (raw * 180) // 65535
    duty = 1638 + int(angle * 6554 / 180)
    
    srv.duty_u16(duty)
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Jagged Motion**: Not adding a small `time.sleep` in the loop can cause the servo to "stutter" due to electrical noise in the potentiometer readings.

### 12. Try This Next
*   **Invert**: Swap the mapping (0 to 180) to (180 to 0) so the arm moves opposite to the knob.
"""

    p0554 = """
---

## 1. Project 0554: Robotic Arm Basics Sequences

### 2. Learning Objective
Design a multi-point biological "Pick and Place" sequence that moves the arm through specific industrial coordinates with pauses.

### 3. Concepts Introduced
*   Hard-coded Sequences
*   Sequential Logic
*   Coordinate-based Navigation
*   Timed Interruptions

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Mechanical Arm/Gripper

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pivoting Joint** | GP16 | Sequence Control |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`**
*   **from Time, drag `pico_wait`**
*   **from Text, drag `print`**

### 7. Variables
*   **None**: Command-driven automation.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Servo GP16.

**B. Main Loop Phase**
2.  **Step 1 (Rest)**:
    *   Angle: 0. Wait 1s. Print "Ready".
3.  **Step 2 (Pickup)**:
    *   Angle: 45. Wait 2s. Print "Lifting...".
4.  **Step 3 (Transport)**:
    *   Angle: 135. Wait 2s. Print "Moving...".
5.  **Step 4 (Dropoff)**:
    *   Angle: 180. Wait 1s. Print "Released".

### 9. Execution Flow
1.  **Start**: Arm is at zero.
2.  **Sequence**: The loop triggers distinct angular commands.
3.  **Automation**: The Pico holds each position for a specific time, simulating a robotic arm picking up a part and placing it elsewhere.
4.  **Repeat**: The process cycles back to "Ready".

### 10. Generated Code
```python
import machine
import time

srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(angle):
    duty = 1638 + int(angle * 6554 / 180)
    srv.duty_u16(duty)

while True:
    print("READY")
    move(0); time.sleep(1)
    
    print("PICKUP")
    move(45); time.sleep(2)
    
    print("DROPOFF")
    move(180); time.sleep(2)
```

### 11. Common Mistakes
*   **Fast Speeds**: The servo moves very quickly. Moving from 0 to 180 in one jump can vibrate the whole robot. (Solution: Use slow loops).

### 12. Try This Next
*   **Loop Increments**: Use a for-loop to move slowly from 45 to 180 so the "Transport" move is smooth.
"""

    p0555 = """
---

## 1. Project 0555: Interactive Robotic Arm Basics

### 2. Learning Objective
Create a "Teach and Play" mode where the arm records two keyframes (A and B) based on manual knob input and then plays them back on loop.

### 3. Concepts Introduced
*   Data Recording (Variables)
*   User-Defined Keyframes
*   State-based Logic (Rec vs Play)
*   Conditional Playback

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo, Potentiometer, Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Save Button** | GP14 | Press to record |
| **Servo** | GP16 | Output |
| **Pot** | GP26 | Teaching input |

### 6. Blocks Used
*   **from Variables, drag `set_variable`**
*   **from Logic, drag `if_else`**

### 7. Variables
*   **pos_a**: Integer (Saved angle 1)
*   **pos_b**: Integer (Saved angle 2)
*   **steps**: Integer (Count of saved points)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Inputs and Outputs.
2.  **State**: Set `steps` = 0.

**B. Teaching Phase**
3.  **Record Point A**:
    *   Loop until Button GP14 is pressed.
    *   Map Pot value to `pos_a`. Wait for release. `steps = 1`.
4.  **Record Point B**:
    *   Loop until Button GP14 is pressed.
    *   Map Pot value to `pos_b`. Wait for release. `steps = 2`.

**C. Playback Phase**
5.  **Loop Sequences**:
    *   If `steps` == 2:
        *   Move to `pos_a`. Wait 1s.
        *   Move to `pos_b`. Wait 1s.

### 9. Execution Flow
1.  **Interact**: User moves the arm with the knob to the first spot and hits "Save".
2.  **Store**: The Pico remembers the specific angle in a variable.
3.  **Repeat**: User moves to the second spot and hits "Save".
4.  **Automation**: The system stops listening to the knob and starts moving automatically between the two recorded points.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

# Record
print("Move to Point A and press Button...")
while not btn.value(): pass
pos_a = int(pot.read_u16() * 180 / 65535)
time.sleep(0.5)

print("Move to Point B and press Button...")
while not btn.value(): pass
pos_b = int(pot.read_u16() * 180 / 65535)
time.sleep(0.5)

# Playback
print("Playing back sequence...")
def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    move(pos_a); time.sleep(1)
    move(pos_b); time.sleep(1)
```

### 11. Common Mistakes
*   **No Release Check**: If you don't wait for the button to be released, one press might save both points A and B instantly.

### 12. Try This Next
*   **Multi-Point**: Use a List to store up to 10 points instead of just A and B.
"""

    p0556 = """
---

## 1. Project 0556: Smart Robotic Arm Basics Switch

### 2. Learning Objective
Implement a "Safety Light Curtain" using an IR breakbeam sensor to unconditionally stop robotic motion if an obstruction is detected.

### 3. Concepts Introduced
*   Emergency Stop (E-Stop)
*   Digital Interlocks
*   Safety Sensing
*   State Blocking

### 4. Hardware Required
*   Raspberry Pi Pico
*   IR Breakbeam Sensor (Emitter/Receiver)
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **IR Receiver** | GP14 | HIGH when beam is CLEAR |
| **Servo** | GP16 | Controlled Motion |

### 6. Blocks Used
*   **from Logic, drag `if_do`**
*   **from Smart IO, drag `pico_gpio_read`**

### 7. Variables
*   **is_safe**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**: GP14 (In/Pull-Up) and GP16 (Out).

**B. Main Loop Phase**
2.  **Monitor Perimeter**:
    *   Set `is_safe` to state of GP14.
3.  **Control Motion**:
    *   **If `is_safe` is TRUE**:
        *   Execute normal sweep (0 to 180).
    *   **Else (Beam Broken)**:
        *   Do NOT move. Print "SAFETY HALT!".
        *   Keep Servo at current position.

### 9. Execution Flow
1.  **Observe**: The arm sweeps back and forth while the IR beam is intact.
2.  **Interrupt**: A hand or object breaks the light beam.
3.  **Detection**: Digital Input on GP14 flips state.
4.  **Reaction**: The code skips the "Move" command entirely.
5.  **Result**: The arm freezes instantly until the path is cleared.

### 10. Generated Code
```python
import machine
import time

sensor = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

angle = 0
step = 5

while True:
    # Check Safety First
    if sensor.value(): # Beam is clear
        angle += step
        if angle >= 180 or angle <= 0: step *= -1
        move(angle)
    else:
        print("OBSTRUCTION DETECTED!")
        
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Pull Up/Down**: IR sensors often have "Open Collector" outputs. If you don't use `PULL_UP` in code, the "Clear" signal might never be detected correctly.

### 12. Try This Next
*   **Reset Requirement**: Instead of auto-restarting when clear, require a button press to acknowledge the safety stop.
"""

    p0557 = """
---

## 1. Project 0557: Robotic Arm Basics Alarm System

### 2. Learning Objective
Design a "Torque Protection" system that uses a potentiometer (simulating current draw/strain) to shut down the arm if it meets excessive physical resistance.

### 3. Concepts Introduced
*   Overload Simulation
*   Threshold Shutdowns
*   Resource Protection
*   Feedback Integration

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer (Load Simulator)
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Strain Sensor** | GP26 | Analog Load Sim |
| **Servo** | GP16 | Actuator |

### 6. Blocks Used
*   **from Logic, drag `if_do`** (Threshold check)
*   **from Smart IO, drag `pico_adc_read`**

### 7. Variables
*   **load**: Integer (0-65535)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP26 (In) and GP16 (Out).

**B. Main Loop Phase**
2.  **Monitor Strain**:
    *   Read `load` from Pot(26).
3.  **Evaluate Safety**:
    *   If `load` > 50000 (Simulating a jam):
        *   Turn OFF PWM.
        *   Print "OVERLOAD DETECTED - MOTOR DISABLED".
        *   Wait for manual reset or lower load.
    *   Else:
        *   Run normal sweep logic.

### 9. Execution Flow
1.  **Start**: Arm is moving.
2.  **Interaction**: User turns the "Load" knob to high (simulating the motor struggling).
3.  **Logic**: The Pico detects that the "Strain" has crossed the limit.
4.  **Reaction**: The PWM signal is killed to prevent burning out the motor.
5.  **Safety**: The motor remains inert until the "Load" is reduced.

### 10. Generated Code
```python
import machine
import time

strain_gauge = machine.ADC(26)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    load = strain_gauge.read_u16()
    
    if load > 50000:
        print("JAM DETECTED!")
        srv.duty_u16(0) # Stop motor
        time.sleep(1)
    else:
        # Simple sweep moves only when safe
        move(45); time.sleep(1)
        move(135); time.sleep(1)
```

### 11. Common Mistakes
*   **False Triggers**: If your limit is too low, the motor might "Overload" just from moving its own weight. (Solution: Calibrate the threshold).

### 12. Try This Next
*   **Indicator**: Add a Red LED that glows brighter as the "Strain" increases.
"""

    p0558 = """
---

## 1. Project 0558: The Robotic Arm Basics Game

### 2. Learning Objective
Programm a "Catapult" motion sequence that combines a slow, high-torque tensioning phase with a sudden, maximum-speed release phase.

### 3. Concepts Introduced
*   Variable Speed Phases
*   Mechanical Potential Energy
*   Ramped Motion (Slow pull)
*   Instantaneous state change (Fast release)

### 4. Hardware Required
*   Raspberry Pi Pico
*   High-Speed Servo (Metal Gear preferred)
*   Catapult Assembly

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Launch Joint** | GP16 | Tension control |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (Slow pull)
*   **from Time, drag `pico_wait`** (Hold and Fire)
*   **from Motors, drag `pico_servo_angle`**

### 7. Variables
*   **t**: Integer (Pull counter)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Servo GP16.

**B. Sequence Phase**
2.  **Tensioning (Slow)**:
    *   From **Loops**, `count_with` `t` from 0 to 90 (Step 1).
    *   Set Servo to `t`.
    *   Wait 0.05s. (This pull takes ~4.5 seconds).
3.  **Hold**:
    *   Wait 2s at 90. (Ready state).
4.  **FIRE (Fast)**:
    *   From **Motors**, set `pico_servo_angle` to 0.
    *   Wait **ZERO** seconds. (Let the servo move as fast as possible).
5.  **Cooldown**:
    *   Wait 5s for the project to reset.

### 9. Execution Flow
1.  **Start**: The arm begins a very slow crawling motion upward.
2.  **Potential**: This simulates stretching a rubber band or pulling a heavy spring.
3.  **Prime**: It reaches its peak and waits for the "Launch" command.
4.  **Release**: The PWM jumps instantly to the 0 position.
5.  **Action**: The servo snaps back at its maximum rated speed, launching the projectile.

### 10. Generated Code
```python
import machine
import time

srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    print("TENSIONING...")
    for t in range(0, 91):
        move(t)
        time.sleep(0.05)
        
    print("READY TO FIRE!")
    time.sleep(2)
    
    print("FIRE!")
    move(0) # Snap to start
    time.sleep(5) # Reset period
```

### 11. Common Mistakes
*   **Fast Tension**: If you use `move(90)` directly, there is no tension phase—just a flip. You MUST use a loop for the slow pull.
*   **Plastic Gears**: Repetitive "Fire" cycles at max speed can snap plastic gears. Do not do this too often.

### 12. Try This Next
*   **Trigger Button**: Only fire the catapult when a button is pressed.
"""

    p0559 = """
---

## 1. Project 0559: Automated Robotic Arm Basics

### 2. Learning Objective
Create a "Logical Routing" system where the arm moves to different bin positions based on input from a Color Sensor.

### 3. Concepts Introduced
*   Sensor-Aided Sorting
*   Decision Trees
*   Position-to-Category mapping
*   I2C Sensor Integration (Concept)

### 4. Hardware Required
*   Raspberry Pi Pico
*   Color Sensor (TCS34725 or simulated via 2 buttons)
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Color Trigger** | GP14 | HIGH = Blue, LOW = Red |
| **Servo** | GP16 | Sorting Arm |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Motors, drag `pico_servo_angle`**

### 7. Variables
*   **object_color**: Integer

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Init**: Hardware config. Move arm to 90 (Neutral).

**B. Main Loop Phase**
2.  **Scan for Object**:
    *   Read GP14 value.
3.  **Route Logic**:
    *   **If GP14 is HIGH (Detected Blue)**:
        *   Move Servo to 45 (Blue Bin).
        *   Wait 2s.
    *   **Else (Detected Red)**:
        *   Move Servo to 135 (Red Bin).
        *   Wait 2s.
4.  **Reset**:
    *   Move back to 90 (Neutral position).
    *   Wait 1s.

### 9. Execution Flow
1.  **Start**: Arm is waiting in the middle.
2.  **Detect**: A red object passes the sensor.
3.  **Evaluate**: The computer identifies the color and selects the "Red" command.
4.  **Sort**: The arm swings to the right, pushing the object into the correct bin.
5.  **Recovery**: The arm returns to the center to wait for the next item.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)
srv = PWM(Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    # Wait for sensor trigger
    if sensor.value():
        print("BLUE OBJECT")
        move(45)
    else:
        print("RED OBJECT")
        move(135)
        
    time.sleep(2)
    move(90) # Back to center
    time.sleep(1)
```

### 11. Common Mistakes
*   **Flicker Logic**: Checking the sensor so fast that the arm starts moving before the object is fully in place. Add a "Settle Delay".

### 12. Try This Next
*   **Counter**: Every time an object is sorted Red, increment a `red_count` variable and print it.
"""

    p0560 = """
---

## 1. Project 0560: Mastering Robotic Arm Basics

### 2. Learning Objective
Coordinate two independent servo joints (Shoulder and Elbow) to work together to reach specific points in 2D space.

### 3. Concepts Introduced
*   Multi-Joint Control
*   2-Axis Movement
*   Coordinated Steps
*   Spatial Planning

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x Servo Motors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Shoulder Joint** | GP16 | Base movement |
| **Elbow Joint** | GP17 | Extension movement |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`** (Use twice)
*   **from Time, drag `pico_wait`**
*   **from Functions, drag `to_procedure`**

### 7. Variables
*   **None**: Procedure-based control.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Config**: Init GP16/17 (PWM 50Hz).

**B. Define Movement Patterns**
2.  **Create "Home" Step**: Set both to 90.
3.  **Create "Extend" Step**: Set Shoulder to 120, Elbow to 45.
4.  **Create "Retract" Step**: Set Shoulder to 60, Elbow to 135.

**C. Main Loop Phase**
5.  **Sequence Execution**:
    *   Call Home. Wait 1s.
    *   Call Extend. Wait 1s.
    *   Call Retract. Wait 1s.

### 9. Execution Flow
1.  **Start**: Both joints move to a default middle position.
2.  **Extension**: The base moves forward while the second joint bends out, reaching for an object.
3.  **Retraction**: Both joints pull back simultaneously.
4.  **Benefit**: Controlling two joints allows the robot to reach a wide area of the table instead of just a single line.

### 10. Generated Code
```python
import machine
import time

s1 = machine.PWM(machine.Pin(16)); s1.freq(50)
s2 = machine.PWM(machine.Pin(17)); s2.freq(50)

def set_arm(joint1, joint2):
    d1 = 1638 + int(joint1 * 6554 / 180)
    d2 = 1638 + int(joint2 * 6554 / 180)
    s1.duty_u16(d1)
    s2.duty_u16(d2)

while True:
    print("POS: HOME")
    set_arm(90, 90); time.sleep(1)
    
    print("POS: REACH")
    set_arm(120, 45); time.sleep(1)
    
    print("POS: TUCK")
    set_arm(60, 135); time.sleep(1)
```

### 11. Common Mistakes
*   **Joint Conflict**: Moving both servos to positions where the mechanical arms hit each other. Always check the physical range of motion before setting the numbers.

### 12. Try This Next
*   **Square Walk**: Find 4 pairs of coordinates that make the tip move in a square shape.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0551 + p0552 + p0553 + p0554 + p0555 + p0556 + p0557 + p0558 + p0559 + p0560)
    
    print("Batch 56 (0551-0560) appended with Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch56()
