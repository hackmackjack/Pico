
## Project 0156: Smart Robotic Arm Basics Switch

### 1. Learning Objective
Explore heliotropic behavior (tracking light). Learn how to compare data from two analog light sensors (LDRs) and use the difference to drive a servo motor in the direction of the brightest light.

### 2. Concepts Introduced
*   **Differential Sensing**: Comparing two inputs to determine a direction.
*   **Heliotropic Tracking**: The ability of a system to turn toward a light source (like a sunflower).
*   **Dynamic Correction**: Continuously adjusting an output to minimize the "error" between two sensors.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   2 Photoresistors (LDRs)
*   2x 10k Ohm resistors (for voltage dividers)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR Left** | GP26 (ADC0) | Measures left-side intensity |
| **LDR Right** | GP27 (ADC1) | Measures right-side intensity |
| **Servo Signal** | GP15 | Moves arm left or right |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Math, drag `math_arithmetic`** (addition, subtraction)

### 6. Variables
*   **val_left**, **val_right**: Raw readings from the LDRs.
*   **pos**: Current angle of the servo.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start at Center**:
    *   From **Variables**, **Set** `pos` = 90.
    *   From **Actuators**, **Set** GP15 angle to `pos`.

**B. Detection Phase**
2.  **Monitor the Light**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `val_left` = **Sensors** `pico_analog_read` GP26.
    *   **Set** `val_right` = **Sensors** `pico_analog_read` GP27.

**C. Decision Phase**
3.  **Check for Brightest Side**:
    *   From **Logic**, drag a nested IF structure (`controls_if`).
4.  **Case 1: Light is on Left**:
    *   **Condition**: If `val_left` > (`val_right` + 50) AND `pos` > 0. (The +50 adds a small "Deadzone" to prevent jitters).
    *   **Action**: **Set** `pos` = `pos` - 5.
5.  **Case 2: Light is on Right**:
    *   **Condition**: If `val_right` > (`val_left` + 50) AND `pos` < 180.
    *   **Action**: **Set** `pos` = `pos` + 5.

**D. Update Phase**
6.  **Move Arm**:
    *   From **Actuators**, **Set** GP15 angle to `pos`.
7.  **Settle**:
    *   From **Time**, **Wait** 0.05 seconds.

### 8. Execution Flow
1.  **Monitor**: The Pico constantly reads both light sensors.
2.  **Analyze**: It compares the values. If the left sensor is significantly brighter, it realizes the light has moved.
3.  **Correct**: The servo "steps" 5 degrees to the left.
4.  **Balance**: Eventually, both sensors see the same brightness, and the arm stops, pointing directly at the flashlight.

### 9. Generated Code
```python
import machine
import utime

# Setup
ldr_left = machine.ADC(26)
ldr_right = machine.ADC(27)
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

pos = 90
set_angle(pos)

while True:
    l_read = ldr_left.read_u16()
    r_read = ldr_right.read_u16()
    
    # +500 to add a deadzone to prevent jittering (MicroPython 16-bit ADC)
    if l_read > (r_read + 3000) and pos > 0:
        pos -= 2
    elif r_read > (l_read + 3000) and pos < 180:
        pos += 2
        
    set_angle(pos)
    utime.sleep(0.05)
```

### 10. Common Mistakes
*   **Deadzone Missing**: Without the small buffer (e.g. +50), the arm will shake back and forth forever as sensors are never 100% equal.
*   **Wiring Swap**: IF the arm moves away from the light, swap your Left/Right variables in the code.

### 11. Try This Next
*   **Solar Tracker**: Move the LDRs onto the servo arm itself so they rotate WITH the arm for perfect tracking!
*   **Night Mode**: If both LDRs see "Dark" (low values), make the arm return to 90 degrees automatically.

---

## Project 0157: Robotic Arm Basics Alarm System

### 1. Learning Objective
Combine scanning motion (Radar) with distance sensing. Learn how to create a "Guard Dog" system that actively monitors its environment by swiveling a sensor and reacting to intruders.

### 2. Concepts Introduced
*   **Active Scanning**: Moving a sensor to increase its field of vision.
*   **Radar Logic**: Correlating a specific distance reading with a known angle.
*   **Intrusion Detection**: Triggering an alarm based on proximity during a scan.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Ultrasonic Distance Sensor (HC-SR04)
*   Servo Motor
*   Buzzer
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo PWM** | GP15 | Rotates the sensor |
| **Ultrasonic Echo** | GP14 | Reads return pulse |
| **Ultrasonic Trig** | GP13 | Sends trigger pulse |
| **Buzzer (+)** | GP12 | Sound alarm |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_ultrasonic_read`** (read distance)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Loops, drag `controls_repeat_ext`** (count up/down)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)

### 6. Variables
*   **dist**: Reading from the ultrasonic sensor.
*   **angle**: Current sweep position.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Alarm**:
    *   **Set** GP12 (Buzzer) -> LOW.

**B. Scanning Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Sweep Right (0 to 180)**:
    *   From **Loops**, drag `controls_repeat_ext` (count with `angle` from 0 to 180).
    *   Inside:
        *   **Move Servo**: **Set** GP15 angle to `angle`.
        *   **Check Distance**: **Set** `dist` = **Sensors** `pico_ultrasonic_read`.
        *   **Detect Intruder**:
            *   From **Logic**, drag `controls_if`.
            *   **Condition**: If `dist` < 20.
            *   **Action**: **Set** GP12 (Buzzer) -> HIGH, **Wait** 0.1s, **Set** GP12 -> LOW.
        *   **Pause for Scan**: **Wait** 0.05 seconds.

4.  **Sweep Left (180 to 0)**:
    *   From **Loops**, drag a second `controls_repeat_ext` (count with `angle` from 180 to 0).
    *   Repeat the same Servo and Distance logic from Step 3 inside this loop.

### 8. Execution Flow
1.  **Motion**: The ultrasonic sensor (mounted on the servo) rotates slowly from left to right.
2.  **Ping**: At every 5 degrees of rotation, it "pings" to measure distance.
3.  **Trigger**: If an object (like a hand) is seen within 20cm at ANY angle, the buzzer chirps.
4.  **Result**: The system creates a 180-degree safety zone around the Pico.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# 🆘 Placeholder for Ultrasonic helper (Standard logic)
def get_distance(trig, echo):
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    while echo.value() == 0:
        signaloff = time.ticks_us()
    while echo.value() == 1:
        signalon = time.ticks_us()
    timepassed = signalon - signaloff
    return (timepassed * 0.0343) / 2

# Hardware Setup
servo = PWM(Pin(15))
servo.freq(50)
trig = Pin(13, Pin.OUT)
echo = Pin(14, Pin.IN)
buzzer = Pin(12, Pin.OUT)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

while True:
    # Right Sweep
    for a in range(0, 181, 10):
        set_angle(a)
        d = get_distance(trig, echo)
        if d < 20:
            print("Intruder at " + str(a) + " deg!")
            buzzer.value(1)
            time.sleep(0.1)
            buzzer.value(0)
        time.sleep(0.05)
        
    # Left Sweep
    for a in range(180, -1, -10):
        set_angle(a)
        d = get_distance(trig, echo)
        if d < 20:
            buzzer.value(1)
            time.sleep(0.1)
            buzzer.value(0)
        time.sleep(0.05)
```

### 10. Common Mistakes
*   **Sensor Noise**: Ultrasonic sensors can give "ghost" readings if moving too fast. Keep the scan slow.
*   **Power Conflict**: Beeping the buzzer while moving a servo can cause a voltage drop. Power them separately if possible.

### 11. Try This Next
*   **Directional Lock**: If an intruder is found, make the servo STOP and point directly at them until they move away.
*   **Indicator LED Bar**: Use a row of LEDs that light up based on which "Zone" the intruder is in (Left, Center, Right).

---

## Project 0158: The Robotic Arm Basics Game

### 1. Learning Objective
Learn about mechanical energy and timing (Catapult logic). Understand how to use variable speed loops to simulate "Charging" (Potential energy) and "Firing" (Kinetic energy) with a servo.

### 2. Concepts Introduced
*   **Velocity Variance**: Changing how fast a motor moves based on the current state.
*   **Charge/Release Cycle**: A core game mechanic where holding a button increases intensity.
*   **Safety Limits**: Ensuring the firing mechanism doesn't destroy the servo housing.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Button
*   Lightweight spoon taped to the servo arm
*   Small paper ball or pom-pom

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fire Button** | GP14 | Hold to charge, release to fire |
| **Servo PWM** | GP15 | Thrower arm |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/else)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **charge_level**: Current retracted position of the arm.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Rest Position**:
    *   **Set** GP15 angle to 90 (Fire position).

**B. Monitoring Phase**
2.  **Start Game Loop**: From **Loops**, drag `pico_forever`.
3.  **Check Variable Logic**:
    *   From **Logic**, drag `controls_if` with **else** slot.
    *   **Condition**: If `pico_gpio_read` GP14 is True (Button Held).

**C. Charging Phase**
4.  **Pull Back Slowly**:
    *   Inside the **If**:
    *   From **Logic**, drag a nested IF: If `charge_level` > 0.
    *   **Action**: **Set** `charge_level` = `charge_level` - 5.
    *   **Apply**: **Set** GP15 angle to `charge_level`.
    *   **Wait**: 0.05 seconds.

**D. Firing Phase**
5.  **Snap Forward Fast**:
    *   Inside the **Else** (Button Released):
    *   From **Logic**: If `charge_level` < 90.
    *   **Action**: **Set** GP15 angle to 90 (The 'Fire' spot).
    *   **Set** `charge_level` = 90.
    *   **Wait**: 1 second (Reset period).

### 8. Execution Flow
1.  **Prepare**: Put a ball in the spoon.
2.  **Charge**: Hold the button. The spoon pulls back slowly (90... 80... 70...).
3.  **Aim**: Let go when you've reached the desired power level.
4.  **Fire**: The servo snaps to the 90-degree position at maximum speed, launching the ball.
5.  **Result**: The faster the "snap", the further the ball flies.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Hardware
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
servo = PWM(Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

charge = 90
set_angle(charge)

while True:
    if btn.value() == 1:
        # CHARGING: Move back slowly
        if charge > 10:
            charge -= 2
            set_angle(charge)
            print("Charging... " + str(charge))
            time.sleep(0.02)
    else:
        # FIRING: If we were pulled back, snap forward!
        if charge < 85:
            print("FIRE!")
            set_angle(90) # Max speed jump
            charge = 90
            time.sleep(1) # Cooldown
            
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **Mechanical Collision**: Ensure the spoon doesn't hit the table when pulling back.
*   **Charging Too Fast**: If the pull-back is too fast, you won't have time to "aim" your shot.

### 11. Try This Next
*   **Power LED**: Use a row of 3 LEDs that light up as you charge (Green = Low, Yellow = Med, Red = Max).
*   **Auto-Fire**: Make it fire automatically after holding for exactly 3 seconds.

---

## Project 0159: Automated Robotic Arm Basics

### 1. Learning Objective
Understand basic vector path execution (Plotting). Learn how to coordinate two servos (X and Y axles) to move a marker in a specific shape like a "V".

### 2. Concepts Introduced
*   **Multi-Axis Plotting**: Using two motors to create a 2D coordinate system.
*   **Path Planning**: defining a sequence of points (X, Y) to create a shape.
*   **Drawing Logic**: Understanding that every physical shape is just a list of timed motor commands.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 Servo Motors (Pan/Tilt or X/Y configuration)
*   Marker and paper

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo X (Horizontal)** | GP15 | Controls left-right |
| **Servo Y (Vertical)** | GP14 | Controls up-down (tip depth) |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Pre-programmed path.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Lift Pen**: **Set** GP14 (Y-Axis) to 0 (Up position).
2.  **Home X**: **Set** GP15 (X-Axis) to 90 (Center).
3.  **Wait**: 1 second.

**B. Drawing Sequence (The "V" Shape)**
4.  **Step 1: Position Start**:
    *   **Move X** to 45 (Top Left). **Wait** 0.5s.
5.  **Step 2: Lower Pen**:
    *   **Move Y** to 45 (Pen Down). **Wait** 0.5s.
6.  **Step 3: Draw to Bottom**:
    *   **Move X** to 90 (Center Bottom). **Wait** 1s.
7.  **Step 4: Draw to Finish**:
    *   **Move X** to 135 (Top Right). **Wait** 1s.
8.  **Step 5: Lift and Reset**:
    *   **Move Y** to 0 (Pen Up).
    *   **Move X** to 90. **Wait** 3 seconds before repeating.

### 8. Execution Flow
1.  **Hover**: The arm moves above the paper without touching it.
2.  **Touch**: The Y servo lowers the pen tip onto the page.
3.  **Slide**: The X servo moves slowly, dragging the pen at an angle.
4.  **Release**: The Y servo lifts the pen, completing the "V" shape.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# X = Side-to-side, Y = Pen Up/Down
x_servo = PWM(Pin(15))
y_servo = PWM(Pin(14))
x_servo.freq(50)
y_servo.freq(50)

def move(srv, angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    srv.duty_u16(duty)

while True:
    print("Preparing to draw 'V'")
    move(y_servo, 10) # LIFT
    move(x_servo, 45) # START X
    time.sleep(1)
    
    move(y_servo, 60) # TOUCH DOWN
    time.sleep(0.5)
    
    print("Drawing first stroke...")
    move(x_servo, 90) # SLIDE TO BOTTOM
    time.sleep(1)
    
    print("Drawing second stroke...")
    move(x_servo, 135) # SLIDE TO TOP RIGHT
    time.sleep(1)
    
    move(y_servo, 10) # LIFT PEN
    print("Finished.")
    time.sleep(3)
```

### 10. Common Mistakes
*   **Tip Drag**: If the Y servo doesn't lift high enough, it will leave a smear line when returning to the start.
*   **Servo Jumps**: Moving from 0 to 180 instantly can cause the pen to "skip". Use small steps for more complex drawings.

### 11. Try This Next
*   **Draw a Square**: Add more steps to X and Y to create a closed shape.
*   **Dashed Lines**: Rapidly move Y up and down while X is moving.

---

## Project 0160: Mastering Robotic Arm Basics

### 1. Learning Objective
Implement a "Teaching Mode" (Record/Playback). Learn how to use variables to store multiple historical positions and play them back in sequence to automate a task.

### 2. Concepts Introduced
*   **Data Recording**: Storing multiple snapshots of sensor data in real-time.
*   **Playback Logic**: Re-executing stored data through an output device.
*   **Array Management (Concept)**: Saving "Point 1", "Point 2", and "Point 3" into specific storage slots.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Servo Motor
*   Potentiometer (The "Teacher")
*   Button (The "Record" button)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Sets the training angle |
| **Record Button** | GP14 | Press to save a point |
| **Servo Signal** | GP15 | Mimics then plays back |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Actuators, drag `pico_servo_write`** (set Servo angle)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **p1, p2, p3**: Stored angle positions.
*   **points_saved**: Number of points currently recorded.
*   **live_angle**: The current position of the training knob.

### 7. Step-by-Step Guide

**A. Training Phase**
1.  **Monitor Teacher**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `live_angle` = Map **Sensors** `pico_analog_read` (GP26) from [0-1023] to [0-180].
    *   **Move Servo**: **Set** GP15 angle to `live_angle`.

2.  **Handle Record Clicks**:
    *   From **Logic**, drag `controls_if`. If **Button** GP14 is True (Pressed):
        *   If `points_saved` == 0: **Set** `p1` = `live_angle`, **Set** `points_saved` = 1.
        *   Else If `points_saved` == 1: **Set** `p2` = `live_angle`, **Set** `points_saved` = 2.
        *   Else If `points_saved` == 2: **Set** `p3` = `live_angle`, **Set** `points_saved` = 3.
        *   **Wait** 0.5s (Debounce).

**B. Playback Phase**
3.  **Trigger Automation**:
    *   If `points_saved` == 3:
        *   **Print** "Starting Playback Loop...".
        *   From **Loops**, drag `controls_repeat` (10 times).
            *   **Move to P1**. **Wait** 1s.
            *   **Move to P2**. **Wait** 1s.
            *   **Move to P3**. **Wait** 1s.
        *   **Set** `points_saved` = 0 (Reset for next training).

### 8. Execution Flow
1.  **Teach**: You move the knob. The arm follows. You press the button at 3 different spots.
2.  **Store**: The Pico remembers the 3 exact angles.
3.  **Run**: Once the 3rd point is saved, the Pico takes control!
4.  **Repeat**: The arm moves between the 3 saved spots automatically for 10 rounds.
5.  **Reset**: The system clears its memory and waits for you to teach a new routine.

### 9. Generated Code
```python
import machine
import utime

# Inputs / Outputs
pot = machine.ADC(26)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

p1 = p2 = p3 = 0
points_saved = 0

print("Teach Mode: Save 3 positions.")

while True:
    # Live Follow
    raw = pot.read_u16()
    live_angle = (raw / 65535) * 180
    set_angle(live_angle)
    
    # Recording Logic
    if btn.value() == 1:
        if points_saved == 0:
            p1 = live_angle
            print("Point 1 Saved: " + str(p1))
            points_saved = 1
        elif points_saved == 1:
            p2 = live_angle
            print("Point 2 Saved: " + str(p2))
            points_saved = 2
        elif points_saved == 2:
            p3 = live_angle
            print("Point 3 Saved: " + str(p3))
            points_saved = 3
        utime.sleep(0.5)
        
    # Playback Logic
    if points_saved == 3:
        print("PLAYING BACK SEQUENCE...")
        for _ in range(5):
            set_angle(p1)
            utime.sleep(1)
            set_angle(p2)
            utime.sleep(1)
            set_angle(p3)
            utime.sleep(1)
        points_saved = 0
        print("Teaching Mode Reset.")
        
    utime.sleep(0.01)
```

### 10. Common Mistakes
*   **Variable Overwrite**: Forgetting to check `points_saved` status will cause the button to overwrite Point 1 over and over.
*   **No Center Reset**: If you don't reset `points_saved` to 0, it will loop forever.

### 11. Try This Next
*   **Longer Memory**: Expand the code to store 10 points (using a list if your blocks support it).
*   **Variable Speed Playback**: Record how *fast* you moved between points and play that back too!

---
