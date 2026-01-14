import os

def build_batch56_v2():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    p0551 = """
---

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
1.  **Configure Servo**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into `start` block.
    *   Set Pin to GP16 and Angle to 90.

**B. Main Loop Phase**
1.  **Maintain Position**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** below initialization.
2.  **Verify Angle**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into loop.
    *   Set Angle to 90.

### 9. Execution Flow
1.  **Start**: Pico powers up and sets GP16 to the correct frequency (50Hz).
2.  **Calculation**: The `pico_servo_angle` block calculates the correct pulse width for 90 degrees (typically 1.5ms).
3.  **Output**: The signal is sent to the servo controller.
4.  **Reaction**: The servo motor physically rotates the horn to its midpoint.
5.  **Repeat**: The loop ensures the PWM signal stays active, holding the motor at 90 degrees.

### 10. Generated Code
```python
import machine
import time

serv = machine.PWM(machine.Pin(16))
serv.freq(50)

# Move to exact center (90 deg)
# Duty calculation: 1.5ms pulse / 20ms period * 65535 total
while True:
    serv.duty_u16(4915) 
    time.sleep(0.1)
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
1.  **Setup Hardware**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into `start`.
    *   Set Pin to GP16 and Angle to 0.

**B. Main Loop Phase**
1.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Position One**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** into loop.
    *   Set Pin to GP16 and Angle to 0.
3.  **Wait**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below angle block.
    *   Set to 1 second.
4.  **Position Two**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** below wait block.
    *   Set Pin to GP16 and Angle to 180.
5.  **Wait**:
    *   From **Time**, drag `pico_wait`.
    *   **Snap** below second angle.
    *   Set to 1 second.

### 9. Execution Flow
1.  **Start**: Program initializes the PWM signal on GP16.
2.  **Action 1**: Signal pulse changes to 1.0ms; arm moves to $0^{\circ}$.
3.  **Delay**: System pauses for 1 second to allow mechanical motion to finish.
4.  **Action 2**: Signal pulse changes to 2.0ms; arm moves to $180^{\circ}$.
5.  **Delay**: System pauses again.
6.  **Perception**: The arm appears to be "waving" hello endlessly.

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
*   **No Wait Time**: If you don't use `wait()`, the code sends "Move to 180" immediately after "Move to 0". The servo won't have time to actually move before the next signal arrives.

### 12. Try This Next
*   **Double Speed**: Reduce `wait(1)` to `wait(0.5)` for a faster wave.
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
*   **pot_val**: Integer (ADC Result)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   From **Smart IO**, drag `pico_adc_read`.
    *   Set Pin to GP26.

**B. Main Loop Phase**
1.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Read Knob**:
    *   From **Variables**, set `pot_val` to **Smart IO** `pico_adc_read` GP26.
    *   **Snap** into loop.
3.  **Calculate Angle**:
    *   From **Motors**, drag `pico_servo_angle`.
    *   **Snap** below read block.
    *   Set Angle to **Math** `map_range`.
        *   Input Variable: `pot_val`, From: 0-65535, To: 0-180.
4.  **Wait**:
    *   From **Time**, wait 0.05 seconds for stability.

### 9. Execution Flow
1.  **Sense**: Pico reads the knob's position (e.g., halfway turned = 32767).
2.  **Process**: The system maps the 16-bit input range (0-65535) to the servo's degree range (0-180).
3.  **Decide**: $32767$ is mapped within the $0-180$ range, results in $90$.
4.  **Command**: Servo is told to move to $90^{\circ}$.
5.  **Output**: As the user turns the knob, the servo's arm follows the rotation synchronously.

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
    # Calculation: (raw / 65535) * 180
    angle = int(raw * 180 / 65535)
    
    # Standard duty: 1.0ms (1638) to 2.0ms (8192)
    duty = 1638 + int(angle * 6554 / 180)
    
    srv.duty_u16(duty)
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Jittery Motion**: Electrical noise in the pot can cause the servo to "vibrate". Adding a small `time.sleep` or a filter can help.

### 12. Try This Next
*   **Invert Control**: Swap the mapping (0 to 180) to (180 to 0) so the arm moves opposite to the knob.
"""

    p0554 = """
---

## 1. Project 0554: Robotic Arm Basics Sequences

### 2. Learning Objective
Design a multi-point "Pick and Place" sequence that moves the arm through specific industrial coordinates with pauses at each station.

### 3. Concepts Introduced
*   Coordinate-based Navigation
*   Sequential Logic
*   Industrial Automation
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
*   **None**: Sequential direct-execution logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Port**:
    *   From **Smart IO**, ensuring GP16 is ready for PWM.

**B. Main Loop Phase**
1.  **Create Sequence**:
    *   From **Loops**, drag `pico_forever`.
2.  **Move to Home**:
    *   From **Motors**, set `pico_servo_angle` GP16 to 0.
    *   **Snap** into loop.
    *   From **Time**, wait 1.0s.
3.  **Move to Pickup**:
    *   From **Motors**, set `pico_servo_angle` GP16 to 45.
    *   **Snap** below.
    *   From **Time**, wait 2.0s.
4.  **Move to Dropoff**:
    *   From **Motors**, set `pico_servo_angle` GP16 to 180.
    *   **Snap** below.
    *   From **Time**, wait 2.0s.

### 9. Execution Flow
1.  **Start**: Arm is at zero (neutral/home).
2.  **Sequence**: The loop triggers distinct angular commands.
3.  **Process**: The Pico holds each position for a specific time, simulating a robotic arm picking up a part and placing it elsewhere.
4.  **Repeat**: The process cycles back to "Home" to start the next pick.

### 10. Generated Code
```python
import machine
import time

srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move_arm(a):
    duty = 1638 + int(a * 6554 / 180)
    srv.duty_u16(duty)

while True:
    print("GOING HOME...")
    move_arm(0); time.sleep(1)
    
    print("READY FOR PICKUP...")
    move_arm(45); time.sleep(2)
    
    print("DROPPING OFF...")
    move_arm(180); time.sleep(2)
```

### 11. Common Mistakes
*   **Fast Speeds**: The servo moves very quickly. Moving from 0 to 180 in one jump can vibrate the whole robot. (Solution: Use slow loops).

### 12. Try This Next
*   **LED Indicators**: Turn on a Green LED when "Lifting" and a Red LED when "Moving".
"""

    p0555 = """
---

## 1. Project 0555: Interactive Robotic Arm Basics

### 2. Learning Objective
Create a "Teach and Play" mode where the arm records two keyframes based on manual knob input and then plays them back on loop.

### 3. Concepts Introduced
*   Data Recording (Variable Storage)
*   User-Defined Keyframes
*   Playback Logic
*   Conditional Playback

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo, Potentiometer, Button

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Save Button** | GP14 | Press to record |
| **Control Knob**| GP26 | Teaching input |
| **Joint Servo** | GP16 | Actuator |

### 6. Blocks Used
*   **from Variables, drag `set_variable`**
*   **from Logic, drag `if_else`**
*   **from Math, drag `map_range`**

### 7. Variables
*   **pos_a**: Integer (Saved angle 1)
*   **pos_b**: Integer (Saved angle 2)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   Setup Button GP14 (In), Pot GP26 (In), Servo GP16 (Out).

**B. Main Loop Phase**
1.  **Create Teacher**:
    *   From **Loops**, drag `pico_forever`.
2.  **Monitor Button**:
    *   From **Logic**, if GP14 (Button) is HIGH:
        *   **Action**: From **Variables**, set `pos_a` to **Math** `map_range` `pico_adc_read` 26.
        *   Wait 2s.
        *   **Action**: From **Variables**, set `pos_b` to **Math** `map_range` `pico_adc_read` 26.
        *   Wait 2s.
3.  **Enter Playback**:
    *   From **Loops**, repeat 10 times:
        *   Set Servo to `pos_a`. Wait 1s.
        *   Set Servo to `pos_b`. Wait 1s.

### 9. Execution Flow
1.  **Interact**: User moves the arm with the knob to the first spot and hits "Save".
2.  **Output**: The Pico remembers the specific angle in variable `pos_a`.
3.  **Interact**: User moves to the second spot and hits "Save".
4.  **Repeat**: The system stops listening to the knob and starts moving automatically between the two recorded points for a demonstration cycle.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

# Record State
print("MOVE TO POINT A & PRESS BUTTON")
while not btn.value(): move(pot.read_u16() * 180 / 65535)
pos_a = int(pot.read_u16() * 180 / 65535)
time.sleep(1)

print("MOVE TO POINT B & PRESS BUTTON")
while not btn.value(): move(pot.read_u16() * 180 / 65535)
pos_b = int(pot.read_u16() * 180 / 65535)
time.sleep(1)

# Playback State
while True:
    move(pos_a); time.sleep(1)
    move(pos_b); time.sleep(1)
```

### 11. Common Mistakes
*   **Variable Scope**: If variables are only set inside a local block, they might not be accessible during playback. Ensure they are global.

### 12. Try This Next
*   **Add "Stop"**: Use another button to interrupt the playback and re-enter "Teach" mode.
"""

    p0556 = """
---

## 1. Project 0556: Smart Robotic Arm Basics Switch

### 2. Learning Objective
Implement a "Safety Light Curtain" using an IR breakbeam sensor to unconditionally stop robotic motion if an obstruction is detected.

### 3. Concepts Introduced
*   Emergency Stop (E-Stop)
*   Breakbeam Sensing
*   Safety Interlocks
*   State Blocking

### 4. Hardware Required
*   Raspberry Pi Pico
*   IR Breakbeam Sensor
*   Servo Motor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Safety Beam** | GP14 | HIGH when path CLEAR |
| **Robotic Joint**| GP16 | Actuator |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_read`**
*   **from Motors, drag `pico_servo_angle`**

### 7. Variables
*   **is_clear**: Boolean (Safety status)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure IO**:
    *   Set GP14 (IR) and GP16 (Servo).

**B. Main Loop Phase**
1.  **Create Monitor**:
    *   From **Loops**, drag `pico_forever`.
2.  **Safety Check**:
    *   From **Variables**, set `is_clear` to **Smart IO** `pico_gpio_read` GP14.
    *   **Snap** into loop.
3.  **Evaluate Risk**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `is_clear` is TRUE:
        *   **Action**: From **Motors**, set `pico_servo_angle` (Run normal sweep).
    *   **Else (OBSTRUCTED!)**:
        *   **Action**: Set `pico_servo_angle` to current fixed point.
        *   **Action**: From **Text**, print "SAFETY HALT!".

### 9. Execution Flow
1.  **Start**: The arm sweeps back and forth while the IR beam is intact.
2.  **Interact**: A hand or object breaks the light beam.
3.  **Detection**: Digital Input on GP14 flips from HIGH to LOW.
4.  **Decide**: The `if_else` condition switches to the "Else" (Safety) block.
5.  **Output**: All motion commands are ignored. The arm freezes instantly.
6.  **Repeat**: Once the path is cleared, the arm resumes its sequence.

### 10. Generated Code
```python
import machine
import time

beam = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    if beam.value():
        # NORMAL OPERATION
        move(45); time.sleep(1)
        move(135); time.sleep(1)
    else:
        # EMERGENCY STOP
        print("STOPPED - PATH BLOCKED")
        time.sleep(0.1)
```

### 11. Common Mistakes
*   **Polling Speed**: If your "Normal Operation" has long `sleep` times, the safety check will be slow to respond. (Advanced: Use interrupts for instant stop).

### 12. Try This Next
*   **Reset Requirement**: Instead of auto-restarting when clear, require a button press to acknowledge the safety stop.
"""

    p0557 = """
---

## 1. Project 0557: Robotic Arm Basics Alarm System

### 2. Learning Objective
Design a "Torque Protection" system that uses a potentiometer (simulating current draw) to shut down the arm if physical resistance is too high.

### 3. Concepts Introduced
*   Overload Simulation
*   Threshold Shutdowns
*   Current Feedback
*   System Resilience

### 4. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer (Load Sim)
*   Servo Motor
*   Buzzer

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Strain Gauge** | GP26 | Analog Load Sim |
| **Servo Output** | GP16 | Actuator |
| **Fault Alarm**  | GP12 | Buzzer |

### 6. Blocks Used
*   **from Smart IO, drag `pico_adc_read`**
*   **from Logic, drag `if_else`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **current_load**: Integer (Simulation value)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep Hardware**:
    *   Set ADC 26, Servo 16, GPIO 12.

**B. Main Loop Phase**
1.  **Create Monitor**:
    *   From **Loops**, drag `pico_forever`.
2.  **Measure Strain**:
    *   From **Variables**, set `current_load` to **Smart IO** `pico_adc_read` GP26.
    *   **Snap** into loop.
3.  **Evaluate Safety**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `current_load` > 50000 (Simulating a jam):
        *   **Action**: From **Smart IO**, set GP16 (Servo) to 0 (Power off).
        *   **Action**: Set Buzzer GP12 to HIGH.
        *   **Action**: Print "JAM DETECTED - CUTTING POWER".
    *   **Else (Normal)**:
        *   **Action**: Move Servo GP16.
        *   **Action**: Set Buzzer GP12 to LOW.

### 9. Execution Flow
1.  **Start**: Arm is moving.
2.  **Interaction**: User turns the "Load" knob high (simulating resistance).
3.  **Process**: The Pico detects that the "Strain" has crossed the safety limit.
4.  **Decide**: The computer decides the motor is in danger of burning out.
5.  **Output**: PWM signal is immediately stopped. The buzzer sounds.
6.  **Recovery**: Once the user reduces the "Load" knob, the system resets to normal.

### 10. Generated Code
```python
import machine
import time

gauge = machine.ADC(26)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)
buz = machine.Pin(12, machine.Pin.OUT)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    load = gauge.read_u16()
    
    if load > 50000:
        print("JAM!!!")
        srv.duty_u16(0) # Stop motor
        buz.on()
    else:
        buz.off()
        # Do movement
        move(0); time.sleep(1)
        move(180); time.sleep(1)
```

### 11. Common Mistakes
*   **Threshold Sensitivity**: If the limit is too low, the arm might "Stop" just from its own weight while moving.

### 12. Try This Next
*   **Indicator LED**: Pulse an LED when load is > 30000 as a "Warning" before the full shutdown.
"""

    p0558 = """
---

## 1. Project 0558: The Robotic Arm Basics Game

### 2. Learning Objective
Programm a "Catapult" sequence that combines a slow tensioning phase (ramped servo motion) with a high-speed release phase.

### 3. Concepts Introduced
*   Variable Speed Phases
*   Mechanical Potential Energy
*   Release Latency
*   Speed Ramping

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor (Metal Gear preferred)
*   Catapult assembly

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Arm Joint**    | GP16 | Tension control |

### 6. Blocks Used
*   **from Loops, drag `count_with`** (Slow pull)
*   **from Motors, drag `pico_servo_angle`** (Fast snap)
*   **from Text, drag `print`**

### 7. Variables
*   **stretch**: Integer (Angle counter)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Homing**:
    *   Set Servo GP16 to 0.

**B. Main Loop Phase**
1.  **Create Game Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Slow Tension**:
    *   From **Loops**, drag `count_with`.
    *   **Snap** into loop.
    *   Set Variable `stretch`, From 0, To 90, Step 1.
    *   From **Motors**, set Servo GP16 to `stretch`.
    *   From **Time**, wait 0.05s.
3.  **Hold**:
    *   From **Time**, wait 2s.
    *   From **Text**, print "LOCKED AND LOADED...".
4.  **FIRE**:
    *   From **Motors**, set Servo GP16 to 0. (Instant snap back).
    *   From **Text**, print "FIRE!".
5.  **Rest**:
    *   Wait 5s before next shot.

### 9. Execution Flow
1.  **Process**: The arm begins a very slow crawling motion (Tensioning).
2.  **Output**: This simulates stretching a spring or rubber band mechanical force.
3.  **Output**: After the 2-second hold, the signal instantly changes to 0.
4.  **Actuation**: The servo "snaps" back at full manufacturer speed.
5.  **Result**: Projectile launched.
6.  **Reset**: System enters a long cooldown before repeating.

### 10. Generated Code
```python
import machine
import time

srv = machine.PWM(machine.Pin(16)); srv.freq(50)
def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    print("TENSIONING...")
    for stretch in range(0, 91, 1):
        move(stretch)
        time.sleep(0.05)
    
    print("READY...")
    time.sleep(2)
    
    print("FIRE!")
    move(0)
    time.sleep(5)
```

### 11. Common Mistakes
*   **Nylon Gears**: Repetitive high-speed "snap" releases can strip plastic gears. Use metal-geared servos for catapult projects.

### 12. Try This Next
*   **Target Bell**: Set up a buzzer that rings if you hit a target (Simulate with a button).
"""

    p0559 = """
---

## 1. Project 0559: Automated Robotic Arm Basics

### 2. Learning Objective
Create a "Logical Routing" system where the arm moves objects to different locations based on input from a simulated color sensor.

### 3. Concepts Introduced
*   Decision Trees
*   Routing Logic
*   Position-to-State mapping
*   Automated Sorting

### 4. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Switch (Color Simulator)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Object Type**  | GP14 | Trigger Input |
| **Sorter Arm**   | GP16 | Actuator |

### 6. Blocks Used
*   **from Logic, drag `if_else`**
*   **from Motors, drag `pico_servo_angle`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   **is_blue**: Boolean (Simulated detection)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Neutral**:
    *   From **Motors**, drag `pico_servo_angle` GP16 to 90.
    *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Create Sorter**:
    *   From **Loops**, drag `pico_forever`.
2.  **Check Input**:
    *   From **Variables**, set `is_blue` to **Smart IO** `pico_gpio_read` GP14.
    *   **Snap** into loop.
3.  **Sorted Route**:
    *   From **Logic**, drag `if_else`.
    *   **Condition**: If `is_blue` is TRUE:
        *   **Action**: From **Motors**, set Servo to 45 (Blue Bin).
        *   From **Time**, wait 2s.
    *   **Else**:
        *   **Action**: From **Motors**, set Servo to 135 (Red Bin).
        *   From **Time**, wait 2s.
4.  **Return**:
    *   From **Motors**, set Servo to 90.
    *   Wait 1s.

### 9. Execution Flow
1.  **Start**: Arm is waiting in neutral center position.
2.  **Sense**: An object passes. GP14 is triggered (e.g., HIGH for blue).
3.  **Process**: The `if_else` decides which coordinate to use.
4.  **Output**: The arm swings to the correct "Bin" side.
5.  **Output**: The arm returns to center to wait for the next part.

### 10. Generated Code
```python
import machine
import time

sensor = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
srv = machine.PWM(machine.Pin(16)); srv.freq(50)

def move(a): srv.duty_u16(1638 + int(a * 6554 / 180))

while True:
    if sensor.value():
        print("ROUTING: BLUE BIN")
        move(45)
    else:
        print("ROUTING: RED BIN")
        move(135)
    
    time.sleep(2)
    move(90) # Return to neutral
    time.sleep(1)
```

### 11. Common Mistakes
*   **Timing Collision**: If the next object arrives before the arm returns to 90, the sorting will fail.

### 12. Try This Next
*   **3rd Bin**: Use two switches to create four possible routing locations (Binary selection).
"""

    p0560 = """
---

## 1. Project 0560: Mastering Robotic Arm Basics

### 2. Learning Objective
Coordinate two independent servo joints (Shoulder and Elbow) to work together to reach specific points in spatial coordinates.

### 3. Concepts Introduced
*   Multi-Joint Coordination
*   Degree-of-Freedom (DOF)
*   Spatial Mapping
*   Function Blocks

### 4. Hardware Required
*   Raspberry Pi Pico
*   2x SG90 Servos

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Shoulder Jt**  | GP16 | Base Elevation |
| **Elbow Jt**     | GP17 | Extension |

### 6. Blocks Used
*   **from Motors, drag `pico_servo_angle`** (Used twice)
*   **from Time, drag `pico_wait`**
*   **from Functions, drag `to_procedure`**

### 7. Variables
*   **None**: Procedure-based command logic.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup Hardware**:
    *   Configure Servo 1 (GP16) and Servo 2 (GP17).

**B. Main Loop Phase**
1.  **Create Routine**:
    *   From **Functions**, define a new procedure `GoToHome`.
    *   From **Motors**, set GP16 to 90 AND GP17 to 90.
2.  **Define Point A**:
    *   From **Functions**, define `GoToReach`.
    *   From **Motors**, set GP16 to 45 (Down) AND GP17 to 180 (Extend).
3.  **Execute Pattern**:
    *   From **Loops**, drag `pico_forever`.
    *   **Snap** into entry point.
    *   **Action**: From **Functions**, call `GoToHome`.
    *   Wait 2s.
    *   **Action**: From **Functions**, call `GoToReach`.
    *   Wait 2s.

### 9. Execution Flow
1.  **Start**: Two independent PWM streams are initialized.
2.  **Process**: The system calls the "Home" function. Both joints move simultaneously to center.
3.  **Delay**: System holds for 2 seconds.
4.  **Process**: The system calls the "Reach" function. The base drops while the arm extends outward.
5.  **Output**: Complex 2-joint motion allows the arm to cover a wide physical radius.
6.  **Repeat**: The arm returns to home and cycles.

### 10. Generated Code
```python
import machine
import time

s1 = machine.PWM(machine.Pin(16)); s1.freq(50)
s2 = machine.PWM(machine.Pin(17)); s2.freq(50)

def move_joints(a1, a2):
    d1 = 1638 + int(a1 * 6554 / 180)
    d2 = 1638 + int(a2 * 6554 / 180)
    s1.duty_u16(d1)
    s2.duty_u16(d2)

while True:
    print("POSITION: HOME")
    move_joints(90, 90); time.sleep(2)
    
    print("POSITION: REACH")
    move_joints(45, 180); time.sleep(2)
```

### 11. Common Mistakes
*   **Mechanical Collision**: If you set angles that cause the arm to hit its own frame, the servos will buzz and heat up. Test limits carefully.

### 12. Try This Next
*   **Mirror Mode**: Add two pots (GP26, GP27) to manually control both joints at the same time.
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(p0551 + p0552 + p0553 + p0554 + p0555 + p0556 + p0557 + p0558 + p0559 + p0560)
    
    print("Batch 56 (0551-0560) appended with Strict Elite Standard v2.0.")

if __name__ == "__main__":
    build_batch56_v2()
