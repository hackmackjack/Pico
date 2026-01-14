
## 1. Project 0236: Smart Simple Motors Switch

### 2. Learning Objective
Explore contact-based obstacle avoidance (The Bumper Car). Learn how to use a limit switch to detect a physical collision and trigger an "Escape Sequence" involving reversing and randomized turning to navigate around obstacles.

### 3. Concepts Introduced
*   **Collision Detection**: Using a digital input as a tactile sensor.
*   **Escape Behavior**: a sequence of actions that override the normal "Forward" state.
*   **Random Walk**: Using random numbers to choose a new heading, preventing the robot from getting stuck in a corner loop.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Robot Chassis (2 Motors)
*   Limit Switch (or Button wired as a bumper)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Bumper Switch** | GP13 | Detects hit (HIGH) |
| **Motor L** | GP15 | Left wheel drive |
| **Motor R** | GP14 | Right wheel drive |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating sensor)
*   **from Math, drag `math_random_int`** (picking turn duration)
*   **from Smart IO, drag `pico_gpio_write`** (motor control)

### 7. Variables
*   **turn_time**: Number representing how long to spin after a hit.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Cruise Control**:
    *   Initialize both motors to HIGH (Forward).

**B. Detection Phase**
3.  **Check for Impact**:
    *   If **Button** GP13 (Bumper) is Pressed:
        *   **Print** "CRASH! Initiating Escape...".
        *   **Stop** all motors for 0.1s.

**C. Escape Phase**
4.  **Reverse**:
    *   **Set** Motors to REVERSE (Switch pins or use driver reverse command).
    *   **Wait** 1 second.
5.  **Calculate Turn**:
    *   **Set** `turn_time` = **Math** `random integer from 200 to 1000` (milliseconds).
6.  **Pivot**:
    *   **Set** Motor L -> FORWARD, Motor R -> REVERSE.
    *   **Wait** `turn_time` ms.

**D. Recovery Phase**
7.  **Resume**: Loop back to Step 2 to continue driving forward.

### 9. Execution Flow
1.  **Search**: The robot drives forward until it hits a chair leg.
2.  **Contact**: The bumper switch clicks.
3.  **Back-up**: The robot immediately reverses for 1s to give itself space.
4.  **Pivot**: It spins right for a random amount of time (e.g., 0.6s).
5.  **New Path**: It starts driving forward again on its new heading.
6.  **Result**: An autonomous vehicle that can explore a room without getting stuck.

### 10. Generated Code
```python
import machine
import utime
import urandom

# Wheels
l_fwd = machine.Pin(15, machine.Pin.OUT)
l_rev = machine.Pin(16, machine.Pin.OUT)
r_fwd = machine.Pin(14, machine.Pin.OUT)
r_rev = machine.Pin(17, machine.Pin.OUT)

# Bumper
bump = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

def drive_fwd():
    l_fwd.value(1); l_rev.value(0); r_fwd.value(1); r_rev.value(0)

def drive_rev():
    l_fwd.value(0); l_rev.value(1); r_fwd.value(0); r_rev.value(1)

def spin_right():
    l_fwd.value(1); l_rev.value(0); r_fwd.value(0); r_rev.value(1)

def stop():
    l_fwd.value(0); l_rev.value(0); r_fwd.value(0); r_rev.value(0)

while True:
    drive_fwd()
    
    if bump.value():
        stop()
        utime.sleep(0.2)
        
        # Escape sequence
        drive_rev()
        utime.sleep(1)
        
        spin_right()
        utime.sleep_ms(urandom.randint(300, 1000))
        
        stop()
        utime.sleep(0.1)
```

### 11. Common Mistakes
*   **No Randomization**: If the turn is always 1 second, the robot might get stuck bouncing between two parallel walls in a never-ending loop. Randomizing the turn ensures it eventually breaks free.
*   **Mechanical Delay**: If you don't stop the motor for a split second before reversing, the sudden change in current can blow a fuse or cause the Pico to glitch.

### 12. Try This Next
*   **Double Bumper**: add a left bumper and a right bumper. If the left one hits, turn right. If the right one hits, turn left.
*   **Buzzer Grumble**: make the robot beep sadly every time it hits a wall.

---

## 1. Project 0237: Simple Motors Alarm System

### 2. Learning Objective
Explore motor health monitoring (Stall Detection). Learn how to simulate and handle a "Stall" event where the motor is commanded to move but is physically blocked, using visual alerts to signal a potential hardware failure.

### 3. Concepts Introduced
*   **Motor Stalling**: When an electric motor is blocked, causing it to consume high current without moving.
*   **Simulated Monitoring**: using timeouts to detect if a "Target" hasn't been reached.
*   **Safety Overrides**: automatically cutting power to hardware to prevent damage during a fault.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Motor + Driver
*   1 Red LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer/LED** | GP14 | Alarm Output |
| **Motor Enable** | GP15 | Primary Drive |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Logic, drag `controls_if`** (detecting stall)
*   **from Smart IO, drag `pico_gpio_write`** (shutting down)

### 7. Variables
*   **is_stalled**: Boolean tracking health.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Health**: From **Variables**, **Set** `is_stalled` = False.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Command Action**:
    *   Inside the loop, check if `is_stalled` is False.
    *   If False: **Set** Motor (GP15) -> HIGH.
    *   If True: **Set** Motor -> LOW. **Set** LED (GP14) -> HIGH (Alarm).

**C. Simulation/Trigger Phase**
4.  **Detect Stall**:
    *   *Note: In this elementary project, we simulate a stall detection using a button or a timer.*
    *   If a hidden sensor (or button) says the wheel stopped turning:
        *   **Set** `is_stalled` = True.
        *   **Print** "ENGINE STALL DETECTED. AUTO-SHUTDOWN INITIATED.".

**D. Manual Override**
5.  **Reset**: Add a logic block that sets `is_stalled` back to False if a "Reset" button is pushed.

### 9. Execution Flow
1.  **Normal**: The motor is spinning. The Red LED is OFF.
2.  **Incident**: A rope gets caught in the wheel. The motor stops.
3.  **Detection**: The Pico (simulated or real sensing) sees the motor is on but the speed is 0.
4.  **Action**: The Pico immediately cuts power to the motor so it doesn't burn out.
5.  **Alert**: The Red LED starts flashing, telling the human that maintenance is required.

### 10. Generated Code
```python
from machine import Pin
import time

# Motor and Signal
motor = Pin(15, Pin.OUT)
alarm = Pin(14, Pin.OUT)

# In this demo, we use a button to SIMULATE a stall sensor
stall_sensor = Pin(13, Pin.IN, Pin.PULL_DOWN)

system_active = True

while True:
    if system_active:
        motor.value(1)
        alarm.value(0)
        
        # Check if something is blocking the motor
        if stall_sensor.value() == 1:
            print("STALL! EMERGENCY STOP!")
            system_active = False
    else:
        # SHUTDOWN STATE
        motor.value(0)
        # Flash Alarm
        alarm.value(1); time.sleep(0.2); alarm.value(0); time.sleep(0.2)
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Ignoring the Stall**: If you leave a stalled motor ON, it will get very hot very quickly and might melt the plastic chassis or damage the driver chip.

### 12. Try This Next
*   **Auto-Restart**: try to wait 5 seconds and then attempt to spin the motor again automatically to see if the blockage cleared.

---

## 1. Project 0238: The Simple Motors Game

### 2. Learning Objective
Explore edge-containment logic (The Sumo Bot). Learn how to use a reflectance sensor (IR Line Sensor) to detect the edge of a game arena and implement "Boundary Rebound" logic to keep an autonomous robot inside a defined circle.

### 3. Concepts Introduced
*   **Infrared Reflectance**: Detecting the difference between a black surface (low bounce) and white surface (high bounce).
*   **Arena Awareness**: treating the physical floor as a logic boundary.
*   **Search and Destroy**: Combining boundary containment with forward aggression for a Sumo-style behavior.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Robot Chassis
*   1 IR TCRT5000 Line Sensor (Front Mounted)
*   Black floor with white tape ring

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **IR Sensor** | GP13 | High when over white line |
| **Motor L** | GP15 | Left wheel |
| **Motor R** | GP14 | Right wheel |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating edge)
*   **from Smart IO, drag `pico_gpio_write`** (set direction)
*   **from Time, drag `pico_wait`** (recovery time)

### 7. Variables
*   **None**: this is a reactive behavior project.

### 8. Step-by-Step Guide

**A. Aggression Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Attack Mode**:
    *   **Set** BOTH Motors -> HIGH (Push forward at full speed).

**B. Containment Phase**
3.  **Detect Boundary**:
    *   If **IR Sensor** GP13 is HIGH (White tape reached):
        *   **Stop** briefly.
        *   **Reverse** both motors for 0.5s.
        *   **Pivot** (L HIGH, R LOW) for 0.3s.

**C. Resume Phase**
4.  **Repeat**: the robot goes back to "Attack Mode" but in a new direction.

### 9. Execution Flow
1.  **Hunt**: The robot charges across the black arena looking for an opponent.
2.  **Edge**: It reaches the white tape boundary.
3.  **Panic**: The IR sensor triggers. The Pico immediately overrides the forward command.
4.  **Safety**: The robot backs away from the edge and turns.
5.  **Result**: The robot stays perfectly within the circle, never falling off the "Sumo Ring".

### 10. Generated Code
```python
from machine import Pin
import time

l_mot = Pin(15, Pin.OUT)
r_mot = Pin(14, Pin.OUT)
ir_sensor = Pin(13, Pin.IN)

while True:
    # Check if we hit the edge
    if ir_sensor.value() == 1:
        # WHITE LINE DETECTED - ABORT!
        l_mot.value(0); r_mot.value(0) # Stop
        time.sleep(0.1)
        
        # Backup and turn
        # (Assuming 1=Rev for your driver)
        # Note: adjust pin logic for your specific driver wiring
        print("Edge detected! Moving back.")
        time.sleep(0.5) 
        
        # Random spin
        l_mot.value(1); r_mot.value(0)
        time.sleep(0.4)
    else:
        # CLEAR - CHARGE!
        l_mot.value(1); r_mot.value(1)
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Sensor Height**: If the IR sensor is too high off the floor, it won't see the line. It should be 3-5mm from the surface.
*   **Inverted Logic**: Some sensors show 1 for black and 0 for white. Test your sensor with the `print` block first!

### 12. Try This Next
*   **Opponent Detection**: add an Ultrasonic sensor. If it sees an object, go 100% speed. Otherwise, go 50% speed to save battery.

---

## 1. Project 0239: Automated Simple Motors

### 2. Learning Objective
Explore closed-loop path following (The Line Follower). Learn how to use a pair of IR sensors to detect deviations from a path and implement corrective steering to keep a robot centered on a black line.

### 3. Concepts Introduced
*   **Dual-Sensor Logic**: Comparing two inputs to decide which way to steer.
*   **Closed-Loop Control**: the robot's current action is based on its immediate sensor feedback.
*   **Corrective Steering**: turning towards the sensor that "sees" the line to bring it back under the center.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Robot Chassis
*   2 IR Line Sensors (Left and Right)
*   Black electrical tape on white floor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **IR Left** | GP13 | High when on line |
| **IR Right** | GP12 | High when on line |
| **Motor L** | GP15 | Drive wheel |
| **Motor R** | GP14 | Drive wheel |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating both eyes)
*   **from Smart IO, drag `pico_gpio_write`** (corrective steering)

### 7. Variables
*   **None**: dynamic reactive logic.

### 8. Step-by-Step Guide

**A. Center Logic**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Evaluate Path**:
    *   If **Both** GP13 and GP12 are LOW (Still in the white center, line between them):
        *   **Set** Both Motors HIGH (Forward).

**B. Corrective Logic (Off-Path)**
3.  **Correct Left**:
    *   Else If **Left Sensor** (GP13) is HIGH (Hit the line):
        *   **Set** Motor L -> LOW, Motor R -> HIGH (Turn Left strongly to find the center again).
4.  **Correct Right**:
    *   Else If **Right Sensor** (GP12) is HIGH (Hit the line):
        *   **Set** Motor L -> HIGH, Motor R -> LOW (Turn Right).

**C. Lost Logic**
5.  **Total Loss**:
    *   Else (If both hit or neither hit for a long time): **Stop** or slow down.

### 9. Execution Flow
1.  **Drive**: The robot straddles the line.
2.  **Turn**: The line curves to the left. The robot goes straight and the Left Sensor hits the line.
3.  **Fixed**: The Pico sees the Left hit. It stops the Left wheel. The Right wheel pushes the robot's nose to the left.
4.  **Center**: Once both sensors are over white again, the robot resumes forward travel.
5.  **Result**: An autonomous vehicle that follows a complex race track.

### 10. Generated Code
```python
from machine import Pin
import time

l_mot = Pin(15, Pin.OUT)
r_mot = Pin(14, Pin.OUT)

sensor_l = Pin(13, Pin.IN)
sensor_r = Pin(12, Pin.IN)

while True:
    # 0 = White, 1 = Black Line
    l = sensor_l.value()
    r = sensor_r.value()
    
    if l == 0 and r == 0:
        # On course (between lines)
        l_mot.value(1); r_mot.value(1)
    elif l == 1:
        # Straying Right - Turn Left!
        l_mot.value(0); r_mot.value(1)
    elif r == 1:
        # Straying Left - Turn Right!
        l_mot.value(1); r_mot.value(0)
    else:
        # T-Junction or error
        l_mot.value(0); r_mot.value(0)
        
    time.sleep(0.01) # Fast checking
```

### 11. Common Mistakes
*   **Speed too High**: If the robot is too fast, its momentum will carry it across the line before the sensors can react. Use a slower speed (PWM 50%) for the best tracking.
*   **Sensor Spacing**: If the sensors are wider than the line, it works. If they are closer than the width of the line, the logic must be inverted.

### 12. Try This Next
*   **PID Control**: instead of ON/OFF, try to vary the motor speed *partially* for a smoother wiggle-free path.

---

## 1. Project 0240: Mastering Simple Motors

### 2. Learning Objective
Explore rotational velocity measurement (The Speedometer). Learn how to use an optical interrupt sensor (Encoder) to count wheel revolutions and use a high-speed timer to calculate the actual RPM (Revolutions Per Minute) of a motor.

### 3. Concepts Introduced
*   **Rotary Encoding**: converting mechanical motion into digital pulses.
*   **Pulse Counting**: using a variable as an accumulator for high-speed events.
*   **Speed Math**: `RPM = (Pulses / Holes_Per_Rev) * 60`.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Motor with Slotted Encoder Wheel
*   Infrared Speed Sensor (Opto-coupler)
*   External Power

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor PWM** | GP15 | Drives the wheel |
| **Encoder Pin** | GP13 | Input pulse |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (reset counter)
*   **from Loops, drag `pico_wait`** (sampling window)
*   **from Logic, drag `controls_if`** (detecting pulse)
*   **from Math, drag `math_arithmetic`** (RPM calculation)

### 7. Variables
*   **pulse_count**: integer tracking encoder ticks.
*   **rpm**: final calculated speed.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target Speed**: **Set** Motor (GP15) to 50% power.
2.  **Prep Counter**: **Set** `pulse_count` = 0.

**B. Sampling Phase**
3.  **Start Timing Window**:
    *   From **Loops**, run a "Repeat for 1 second" loop (or use a 1s wait with background counting).
    *   Inside: Every time **GP13** goes from LOW to HIGH:
        *   **Set** `pulse_count` = `pulse_count` + 1.

**C. Math Phase**
4.  **Calculate RPM**:
    *   *Assumes encoder wheel has 20 holes.*
    *   **Set** `rpm` = (`pulse_count` / 20) * 60.
5.  **Log Data**:
    *   **Print** "Wheel Speed: ", `rpm`, " RPM".

**D. Clear Phase**
6.  **Reset**: **Set** `pulse_count` = 0 and restart the 1-second window.

### 9. Execution Flow
1.  **Motion**: The wheel spins. The encoder disk breaks the IR beam 20 times every turn.
2.  **Count**: For one full second, the Pico watches the pin and counts every "break".
3.  **Calculate**: It counted 40 pulses. 40 / 20 = 2 turns per second. 2 * 60 = 120 RPM.
4.  **Result**: You have a digital dashboard showing exactly how fast your robot is moving.

### 10. Generated Code
```python
import machine
import utime

# Motor
motor = machine.PWM(machine.Pin(15))
motor.freq(1000); motor.duty_u16(30000)

# Sensor
encoder = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    count = 0
    start_time = utime.ticks_ms()
    
    # 1-second measuring window
    # Note: Complex apps use interrupts, this is a simplified polling version
    last_state = 0
    while utime.ticks_diff(utime.ticks_ms(), start_time) < 1000:
        current_state = encoder.value()
        # Edge Detection
        if current_state == 1 and last_state == 0:
            count += 1
        last_state = current_state
        utime.sleep_us(100) # Fast poll
        
    # RPM Calculation: (pulses/20 holes) * 60 seconds
    rpm = (count / 20) * 60
    print("RPM: " + str(rpm) + " | Pulses: " + str(count))
```

### 11. Common Mistakes
*   **Window too Short**: if you only measure for 0.1s, your count will be very low (e.g., 2 or 3), making the RPM estimate very inaccurate. 1.0s is a good balance.
*   **Polling Speed**: if your code is doing other things, it might miss a pulse while the wheel is spinning fast.

### 12. Try This Next
*   **Distance Tracker**: calculate the wheel's circumference and convert RPM into "Meters per Second".
*   **Cruise Control**: Try to adjust the motor PWM dynamically to keep the RPM exactly at 100, even if you push against the wheel.

---
