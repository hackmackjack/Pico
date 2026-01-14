
# BATCH 16: Robotic Arm Basics 1 (Projects 0151-0160)

## Project 0151: Introduction to Robotic Arm Basics

### 1. Learning Objective
Understand how to control the position of a servo motor using a Raspberry Pi Pico. Learn the relationship between PWM signals and servo angles (0 to 180 degrees).

### 2. Concepts Introduced
*   **Servo Motor Control**: Using pulse length to set a precise mechanical angle.
*   **Positional Actuation**: moving to specific coordinates rather than just spinning like a DC motor.
*   **Staging**: Testing basic movement ranges before building complex structures.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor (e.g., SG90)
*   Jumper wires (Male to Male or Male to Female)
*   Breadboard (optional)

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo Signal** | GP15 | PWM signal pin |
| **Servo VCC** | 3.3V / 5V | Power (use 5V for more torque if available) |
| **Servo GND** | GND | Ground connection |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_servo_write`** (set Servo GP... angle to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: This project uses direct angle commands.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialize Servo**:
    *   No specific init block is required for basic servo usage in most Blockly environments, as the write block handles initialization.

**B. Control Phase**
2.  **Create Main Structure**:
    *   From **Loops**, drag the `pico_forever` block.
3.  **Command Position 0 (Home)**:
    *   Inside the loop, from **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin to GP15 and Angle to 0.
4.  **Add Delay**:
    *   From **Time**, drag `pico_wait` -> 1 second.
5.  **Command Position 90 (Center)**:
    *   From **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin to GP15 and Angle to 90.
6.  **Add Delay**:
    *   **Wait** 1 second.
7.  **Command Position 180 (Full)**:
    *   From **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin to GP15 and Angle to 180.
8.  **Add Delay**:
    *   **Wait** 1 second.

### 8. Execution Flow
1.  **Home**: The servo arm moves to the 0-degree limit and holds.
2.  **Wait**: Program pauses so the user can verify the position.
3.  **Center**: The servo moves to the middle (90 degrees).
4.  **Full**: The servo moves to the opposite limit (180 degrees).
5.  **Repeat**: The arm returns to 0 and cycles through the positions.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Configure PWM for Servo on GP15
servo = PWM(Pin(15))
servo.freq(50)

def set_angle(angle):
    # Standard SG90 servo pulse: 0.5ms (0 deg) to 2.5ms (180 deg)
    # duty_u16 range: 0 to 65535
    # 0.5ms = 1638, 2.5ms = 8192 approx
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

while True:
    print("Moving to 0 degrees")
    set_angle(0)
    time.sleep(1)
    
    print("Moving to 90 degrees")
    set_angle(90)
    time.sleep(1)
    
    print("Moving to 180 degrees")
    set_angle(180)
    time.sleep(1)
```

### 10. Common Mistakes
*   **Weak Power Supply**: If the Pico reboots when the servo moves, it's drawing too much current from USB. Use an external 5V battery pack for the servo VCC.
*   **Pin Conflict**: Ensure the pin used (GP15) is not being used for other purposes in your circuit.
*   **Angle Limits**: Some "180 degree" servos only reach 170. Don't force them past their physical stop.

### 11. Try This Next
*   **Precision Steps**: Command 0, 45, 90, 135, 180 to see quarter-turns.
*   **Sweep Speed**: Reduce the wait time to 0.1s to see how the motor handles rapid commands.

---

## Project 0152: Blinking Robotic Arm Basics

### 1. Learning Objective
Learn how to create recognizable gestures with a robotic arm. Understand how rapid, repetitive positional commands can simulate human-like movements like "Waving".

### 2. Concepts Introduced
*   **Gesture Animation**: Using range-of-motion to communicate a message.
*   **Repetition**: Cycling through a small set of angles to create a continuous action.
*   **Mechanical Timing**: Adjusting speed to make the movement look natural.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Cardboard cut into a hand shape
*   Tape or glue to attach the hand to the servo horn

### 4. Wiring / Interfaces
*(Same as Project 0151)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_servo_write`** (set Servo GP... angle to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Direct angle control.

### 7. Step-by-Step Guide

**A. Control Phase**
1.  **Create Main Loop**:
    *   From **Loops**, drag `pico_forever`.
2.  **Wave Left**:
    *   Inside the loop, from **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin -> GP15, Angle -> 45.
3.  **Short Wait**:
    *   From **Time**, drag `pico_wait` -> 0.3 seconds.
4.  **Wave Right**:
    *   From **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin -> GP15, Angle -> 135.
5.  **Short Wait**:
    *   **Wait** 0.3 seconds.

### 8. Execution Flow
1.  **Angle 1**: The hand moves to the 45-degree mark (Left).
2.  **Pause**: Briefly stays there so the movement is visible.
3.  **Angle 2**: The hand swings to the 135-degree mark (Right).
4.  **Result**: The hand appears to be waving "Hello" to the user.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Servo Setup
servo = PWM(Pin(15))
servo.freq(50)

def move_servo(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

while True:
    # Hello wave: 45 to 135 degrees
    move_servo(45)
    time.sleep(0.3)
    move_servo(135)
    time.sleep(0.3)
```

### 10. Common Mistakes
*   **Hand Too Heavy**: If the cardboard hand is too large/heavy, the servo might struggle or move slowly. Keep it small and lightweight.
*   **Wait Too Long**: If the wait is 1s, the wave will look very robotic and slow. 0.2s-0.4s is the "natural" waving speed.

### 11. Try This Next
*   **Slow Wave**: Increase the wait to 1 second for a "Sleepy Wave".
*   **Speedy Wave**: Decrease the wait to 0.1s for an "Excited Wave".

---

## Project 0153: Manual Robotic Arm Basics Control

### 1. Learning Objective
Implement direct analog control of a robotic joint. Learn how to "Map" a sensor range (0-1023) to a physical angle range (0-180) for 1-to-1 movement tracking.

### 2. Concepts Introduced
*   **Scaling/Mapping**: Converting values from one scale (the knob) to another (the motor).
*   **Analog Input**: capturing continuous data from a potentiometer.
*   **Real-Time Tracking**: Minimizing delay between user input and mechanical response.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Potentiometer (10k Ohm)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer OUT** | GP26 (ADC0) | Varies from 0 to 3.3V |
| **Servo Signal** | GP15 | Follows the knob position |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Math, drag `math_map`** (map value from ... to ...)
*   **from Variables, drag `variables_set`** (set variable to)

### 6. Variables
*   **knob_val**: The raw 0-1023 reading from the potentiometer.
*   **servo_angle**: The calculated 0-180 angle.

### 7. Step-by-Step Guide

**A. Data Acquisition Phase**
1.  **Read the Knob**:
    *   From **Loops**, drag `pico_forever`.
    *   From **Variables**, drag `variables_set`. **Set** `knob_val` = **Sensors** `pico_analog_read` GP26.

**B. Mapping Phase**
2.  **Convert Range**:
    *   From **Math**, drag the `math_map` block and snap it into a `variables_set` block.
    *   **Set** `servo_angle` to **Map** `knob_val` from [0 to 1023] into [0 to 180].

**C. Output Phase**
3.  **Drive the Servo**:
    *   From **Actuators**, drag `pico_servo_write`.
    *   **Set** Pin -> GP15 and Angle -> the variable `servo_angle`.
4.  **Add Tiny Delay**:
    *   From **Time**, **Wait** 0.05 seconds (for smoother movement and to prevent CPU flooding).

### 8. Execution Flow
1.  **Input**: The user rotates the physical knob.
2.  **Calculation**: The Pico sees a value like 512 (halfway) and maps it to 90 degrees (halfway).
3.  **Command**: The Pico tells the servo to go to 90 degrees.
4.  **Result**: The servo arm mimics the exact position of the knob in real-time.

### 9. Generated Code
```python
import machine
import utime

# Setup Pot and Servo
pot = machine.ADC(26)
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

while True:
    # Read knob (0-65535 in MicroPython)
    raw = pot.read_u16()
    
    # Scale to 0-180
    # (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    angle = (raw / 65535) * 180
    
    set_angle(angle)
    utime.sleep(0.05)
```

### 10. Common Mistakes
*   **Inverted Mapping**: If the arm moves left when you turn the knob right, reverse the mapping: Map from [0-1023] to [180-0].
*   **Jitter**: If the arm shakes, add a small wait (0.1s) or check your breadboard connections for loose grounds.

### 11. Try This Next
*   **Limited Range**: Map the knob [0-1023] to only [0-45] degrees for "Micro-Control".
*   **Inverted Control**: Use TWO servos and make one move the opposite way of the first.

---

## Project 0154: Robotic Arm Basics Sequences

### 1. Learning Objective
Orchestrate multi-axis coordination. Learn how to sequence multiple motors to perform a complex, multi-step task like "Pick and Place".

### 2. Concepts Introduced
*   **Multi-Servo Control**: Managing two independent joints (Base and Claw).
*   **Sequence Planning**: Breaking down a task into ordered logical steps.
*   **Synchronization**: ensuring one movement finishes before the next starts (using delays).

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Servo Motors
*   Robotic Arm kit (or just two servos glued together)

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo 1 (Base)** | GP15 | Rotates the entire arm |
| **Servo 2 (Claw)** | GP14 | Opens and closes the gripper |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_servo_write`** (set Servo GP... angle to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Direct sequence control.

### 7. Step-by-Step Guide

**A. Definition Phase**
1.  **Define States**: 
    *   Claw Open = 0 degrees.
    *   Claw Closed = 90 degrees.
    *   Base Left = 0 degrees.
    *   Base Right = 180 degrees.

**B. Logic Sequencing Phase**
2.  **Start Loop**: From **Loops**, drag `pico_forever`.
3.  **Step 1: Open Claw**:
    *   From **Actuators**, **Set** GP14 (Claw) -> 0.
    *   **Wait** 1 second.
4.  **Step 2: Rotate Base to Load**:
    *   From **Actuators**, **Set** GP15 (Base) -> 0.
    *   **Wait** 1 second.
5.  **Step 3: Close Claw**:
    *   From **Actuators**, **Set** GP14 (Claw) -> 90.
    *   **Wait** 1 second.
6.  **Step 4: Rotate Base to Unload**:
    *   From **Actuators**, **Set** GP15 (Base) -> 180.
    *   **Wait** 1 second.
7.  **Step 5: Release**:
    *   From **Actuators**, **Set** GP14 (Claw) -> 0.
    *   **Wait** 2 seconds (to show it finished).

### 8. Execution Flow
1.  **Prep**: The arm opens its claw and moves to the first position.
2.  **Action**: The claw closes (simulating picking up an object).
3.  **Transport**: The base rotates 180 degrees to the "delivery" zone.
4.  **Drop**: The claw opens, dropping the object.
5.  **Return**: The loop restarts from the beginning.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Setup Servos
base = PWM(Pin(15))
claw = PWM(Pin(14))
base.freq(50)
claw.freq(50)

def set_angle(srv, angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    srv.duty_u16(duty)

while True:
    print("Opening Claw")
    set_angle(claw, 0)
    time.sleep(1)
    
    print("Rotating to Pick position")
    set_angle(base, 0)
    time.sleep(1)
    
    print("Closing Claw (Pick)")
    set_angle(claw, 90)
    time.sleep(1)
    
    print("Rotating to Place position")
    set_angle(base, 180)
    time.sleep(1)
    
    print("Opening Claw (Drop)")
    set_angle(claw, 0)
    time.sleep(2)
```

### 10. Common Mistakes
*   **Collision**: Ensure the claw doesn't hit the table or the arm base when rotating.
*   **Wait Times**: If your servos are slow, you need longer `wait` blocks. If you don't wait, the commands will tangle up.

### 11. Try This Next
*   **Add Elevation**: Use a third servo for the arm "Height" to pick things up from the floor and put them on a box.
*   **Speed Control**: Try to make the rotation move in tiny steps (like Project 0144) for a smoother look.

---

## Project 0155: Interactive Robotic Arm Basics

### 1. Learning Objective
Explore incremental positioning (Jogging). Learn how to use buttons to adjust an angle step-by-step rather than jumping to fixed positions.

### 2. Concepts Introduced
*   **Increment/Decrement**: Adding or subtracting from a variable value.
*   **Boundary Clamping**: Constraining a value to stay within a range (0 to 180).
*   **Digital Input Filtering**: Using buttons to drive numerical changes.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   2 Buttons (Left, Right)
*   2x 10k Ohm pull-down resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Left** | GP14 | Subtracts 10 degrees |
| **Button Right** | GP13 | Adds 10 degrees |
| **Servo Signal** | GP15 | Current position |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Math, drag `math_arithmetic`** (addition, subtraction)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)

### 6. Variables
*   **pos**: Current angle of the servo (initialized to 90).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Center**:
    *   From **Variables**, drag `variables_set`. **Set** `pos` = 90.
    *   From **Actuators**, **Set** GP15 angle to `pos`.

**B. Control Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Handle Right Button (+10)**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP13 is True AND `pos` < 180.
    *   **Action**: **Set** `pos` = `pos` + 10.
4.  **Handle Left Button (-10)**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is True AND `pos` > 0.
    *   **Action**: **Set** `pos` = `pos` - 10.

**C. Update Phase**
5.  **Drive Motor**:
    *   From **Actuators**, **Set** GP15 angle to the variable `pos`.
6.  **Add Response Delay**:
    *   From **Time**, drag `pico_wait` -> 0.1 seconds. (This determines how fast the arm "steps" when you hold the button).

### 8. Execution Flow
1.  **Start**: The arm moves to the center (90).
2.  **Input**: You tap the Right button.
3.  **Check**: The Pico confirms that 90 is less than 180.
4.  **Tick**: The variable `pos` becomes 100.
5.  **Move**: The servo clicks into the 100-degree spot.
6.  **Stop**: If you reach 180, the button press does nothing, protecting the motor.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Hardware setup
btn_left = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_right = Pin(13, Pin.IN, Pin.PULL_DOWN)
servo = PWM(Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

pos = 90
set_angle(pos)

while True:
    if btn_right.value() == 1 and pos < 180:
        pos += 10
        print("Position: " + str(pos))
        set_angle(pos)
        time.sleep(0.15) # Delay for smooth stepping
        
    if btn_left.value() == 1 and pos > 0:
        pos -= 10
        print("Position: " + str(pos))
        set_angle(pos)
        time.sleep(0.15)
        
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **No Boundaries**: If you don't check `pos < 180`, the variable will go to 200, 210, etc., but the servo will just stay stuck at its limit. It takes many button presses to "get back" once you go over.
*   **Rapid Cycling**: Without the 0.1s wait, a single tap might add 50 degrees because the code loops so fast.

### 11. Try This Next
*   **Fine Jogging**: Change the step to +1 and -1 for extremely precise control.
*   **Status Display**: If you have an LED, make it flash only when you hit the 0 or 180 limit.

---
