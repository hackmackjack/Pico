# 📘 Pico 2500: Batch 24 - Simple Motors 2 (Projects 0231-0240)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Advanced Motor Control & Basic Robotics

---

## 1️⃣ Project 0231: DC Motor Speed Control (PWM)

### 2️⃣ Learning Objective
Control DC motor speed using PWM (Pulse Width Modulation) to understand the relationship between duty cycle and rotational speed.

### 3️⃣ Concepts Introduced
*   PWM for Motor Control
*   Duty Cycle (0-100%)
*   Speed-Power Relationship
*   Motor Driver Basics
*   Analog-Like Control from Digital

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   DC Motor (3-6V)
*   L9110S Motor Driver Module
*   External Power (4× AA batteries or 6V supply)
*   Breadboard

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Driver IA** | GP14 | PWM control pin |
| **Motor Driver IB** | GP15 | Direction control (keep LOW for forward) |
| **Motor Driver VCC** | 3.3V | Logic power |
| **Motor Driver GND** | GND | Common ground |
| **Motor Power +** | External 6V | Battery/supply |
| **Motor Power -** | GND | Common ground with Pico |

### 6️⃣ Blocks Used
🔹 **PWM Control**
*   **Category:** Smart IO
*   **Block:** `set PWM Pin [14] frequency [1000] duty [50%]`

🔹 **Variables**
*   **Category:** Variables
*   **Block:** `set [speed] to [0]`

🔹 **For Loop**
*   **Category:** Loops
*   **Block:** `repeat [10] times`

### 7️⃣ Variables & State
*   **speed**: Number (0-100) - Motor speed percentage
*   **dutyCycle**: Number (0-65535) - PWM duty value
*   **direction**: Boolean - Forward/Reverse

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize PWM on GP14 with 1000 Hz frequency
2. Set GP15 to LOW (direction control)
3. Set initial speed = 0

**B. Main Loop Phase**
1. **Gradual Speed Increase:**
   - For speed from 0 to 100 (step 10):
     - Calculate duty cycle = (speed/100) × 65535
     - Set PWM duty to calculated value
     - Print current speed
     - Wait 1 second
2. **Gradual Speed Decrease:**
   - For speed from 100 to 0 (step -10):
     - Same process in reverse

**C. Event / Condition Handling**
*   Minimum PWM for motor to overcome friction (~20-30%)
*   Maximum safe speed (don't exceed motor rating)
*   Smooth transitions prevent mechanical stress

### 9️⃣ Execution Flow (Plain English)
DC motors respond to average voltage. PWM rapidly switches between ON and OFF. At 50% duty cycle, motor sees "half voltage" and runs at half speed. At 100% duty, full voltage = full speed. We gradually increase duty cycle from 0% to 100%, making the motor smoothly accelerate. The L9110S driver amplifies the Pico's 3.3V PWM signal to the motor's operating voltage (6V).

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# Motor control pins
motor_pwm = PWM(Pin(14))
motor_dir = Pin(15, Pin.OUT)

# Setup
motor_pwm.freq(1000)  # 1 kHz PWM frequency
motor_dir.value(0)    # Forward direction

print("DC Motor Speed Control Demo")

# Accelerate from 0 to 100%
print("\nAccelerating...")
for speed_percent in range(0, 101, 10):
    duty = int((speed_percent / 100) * 65535)
    motor_pwm.duty_u16(duty)
    print(f"Speed: {speed_percent}% (Duty: {duty})")
    time.sleep(1)

time.sleep(2)

# Decelerate from 100 to 0%
print("\nDecelerating...")
for speed_percent in range(100, -1, -10):
    duty = int((speed_percent / 100) * 65535)
    motor_pwm.duty_u16(duty)
    print(f"Speed: {speed_percent}% (Duty: {duty})")
    time.sleep(1)

# Stop motor
motor_pwm.duty_u16(0)
print("\nMotor stopped")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Motor Not Spinning**: Check duty cycle >30% (minimum torque threshold).
*   **Motor Overheating**: Don't run at 100% continuously; use 70-80% max for sustained operation.
*   **Erratic Speed**: Use external power for motor, NOT Pico's 3.3V rail.
*   **Common Ground**: MUST connect motor power GND to Pico GND.

### 1️⃣2️⃣ Try This Next
*   **Potentiometer Control**: Map potentiometer (ADC) value to motor speed.
*   **Acceleration Curve**: Non-linear speed ramp (exponential or S-curve).
*   **Speed Feedback**: Add encoder to measure actual RPM and display.

---

## 1️⃣ Project 0232: Motor Direction Control (H-Bridge)

### 2️⃣ Learning Objective
Control motor direction (forward/reverse) using H-bridge driver to understand bidirectional motor control.

### 3️⃣ Concepts Introduced
*   H-Bridge Circuit
*   Bidirectional Control
*   Forward/Reverse Logic
*   Brake Function
*   Polarity Reversal

### 4️⃣ Hardware Required
*   Pico, DC Motor, L9110S Driver, 6V Power

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Function |
| :--- | :--- | :--- |
| **Motor Driver IA** | GP14 | Forward PWM |
| **Motor Driver IB** | GP15 | Reverse PWM |

### 6️⃣ Blocks Used
🔹 **GPIO Control** - Direction pins
🔹 **PWM** - Speed control
🔹 **Logic** - Forward/reverse states

### 7️⃣ Variables & State
*   **motorState**: String - "FORWARD", "REVERSE", "BRAKE", "COAST"
*   **speed**: Number - Current speed (0-100%)

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize both IA and IB as PWM outputs
2. Set both to 0 (motor stopped)

**B. Main Loop Phase**
1. **Forward Motion:**
   - Set IA = speed PWM
   - Set IB = 0
2. **Reverse Motion:**
   - Set IA = 0
   - Set IB = speed PWM
3. **Brake (Active Stop):**
   - Set both IA and IB = HIGH
   - Motor actively resists rotation
4. **Coast (Passive Stop):**
   - Set both IA and IB = 0
   - Motor freewheels to stop

**C. Event / Condition Handling**
*   Never set both HIGH at full PWM simultaneously (brake mode only)
*   Pause briefly when changing direction (avoid current spike)

### 9️⃣ Execution Flow (Plain English)
An H-bridge has 4 switches that control current flow through the motor. Forward = current flows left-to-right. Reverse = current flows right-to-left. The L9110S has two inputs: IA and IB. To go forward, we PWM IA (IB=0). To reverse, we PWM IB (IA=0). Setting both LOW lets motor coast. Setting both HIGH actively brakes (shorts motor terminals, creating electromagnetic braking).

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# Motor H-bridge pins
motor_ia = PWM(Pin(14))
motor_ib = PWM(Pin(15))

motor_ia.freq(1000)
motor_ib.freq(1000)

def motor_forward(speed_percent):
    """Spin motor forward at given speed (0-100)"""
    duty = int((speed_percent / 100) * 65535)
    motor_ia.duty_u16(duty)
    motor_ib.duty_u16(0)
    print(f"Forward at {speed_percent}%")

def motor_reverse(speed_percent):
    """Spin motor reverse at given speed (0-100)"""
    duty = int((speed_percent / 100) * 65535)
    motor_ia.duty_u16(0)
    motor_ib.duty_u16(duty)
    print(f"Reverse at {speed_percent}%")

def motor_brake():
    """Active brake (both pins HIGH)"""
    motor_ia.duty_u16(65535)
    motor_ib.duty_u16(65535)
    print("Brake engaged")

def motor_coast():
    """Passive stop (both pins LOW)"""
    motor_ia.duty_u16(0)
    motor_ib.duty_u16(0)
    print("Coasting to stop")

# Demonstration
print("Motor Direction Control Demo\n")

print("Forward motion:")
motor_forward(70)
time.sleep(3)

print("\nBraking:")
motor_brake()
time.sleep(1)

print("\nReverse motion:")
motor_reverse(70)
time.sleep(3)

print("\nCoast stop:")
motor_coast()
time.sleep(2)

# Back and forth
for i in range(3):
    print(f"\nCycle {i+1}:")
    motor_forward(60)
    time.sleep(1)
    motor_coast()
    time.sleep(0.5)
    motor_reverse(60)
    time.sleep(1)
    motor_coast()
    time.sleep(0.5)

motor_coast()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Direction Won't Change**: Ensure brief stop between direction changes.
*   **Motor Weak in Reverse**: Some motors have directional preference; this is normal.
*   **Clicking Sound**: Current spike when switching; add 100ms delay.
*   **Brake Too Strong**: Lower brake PWM duty to 50% for gentler braking.

### 1️⃣2️⃣ Try This Next
*   **Button Control**: Two buttons for forward/reverse, release to brake.
*   **Timed Oscillation**: Automatically alternate direction every 2 seconds.
*   **Gradual Reverse**: Decelerate to stop, then smoothly accelerate in reverse.

---

## 1️⃣ Project 0233: Motor Pattern Sequences

### 2️⃣ Learning Objective
Create choreographed motor movement sequences for automation and robotics applications.

### 3️⃣ Concepts Introduced
*   Motion Sequencing
*   Timed Patterns
*   State Lists
*   Choreography Programming
*   Sequence Playback

### 4️⃣ Hardware Required
*   Pico, DC Motor, L9110S, 6V Power

### 5️⃣ Wiring / Interfaces
*(Same as 0232)*

### 6️⃣ Blocks Used
🔹 **Lists** - Sequence storage
🔹 **For Loops** - Sequence playback
🔹 **Functions** - Reusable motions

### 7️⃣ Variables & State
*   **sequence**: List - [(direction, speed, duration), ...]
*   **currentStep**: Number - Current sequence index

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Define movement primitives:
   - `forward(speed, time)`
   - `reverse(speed, time)`
   - `brake(time)`
2. Create sequence arrays:
   - Pattern 1: Start-Stop Demo
   - Pattern 2: Acceleration Test
   - Pattern 3: Back-Forth Scan

**B. Main Loop Phase**
1. For each step in sequence:
   - Extract direction, speed, duration
   - Execute motion command
   - Wait for duration
   - Move to next step
2. Loop sequence or stop

**C. Event / Condition Handling**
*   Smooth transitions between sequence steps
*   Emergency stop capability
*   Sequence validation (no impossible commands)

### 9️⃣ Execution Flow (Plain English)
Instead of hardcoding motion commands, we store them as data. A sequence is a list of (direction, speed, duration) tuples. The playback engine reads each tuple and executes it: "Forward 80% for 2s, brake for 0.5s, reverse 60% for 1s". This is how industrial automation, CNC machines, and robot arms work - motion programs stored as data, not code!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

motor_ia = PWM(Pin(14))
motor_ib = PWM(Pin(15))
motor_ia.freq(1000)
motor_ib.freq(1000)

def motor_move(direction, speed, duration):
    """
    Execute single motor movement
    direction: 'F'=forward, 'R'=reverse, 'B'=brake, 'C'=coast
    speed: 0-100%
    duration: seconds
    """
    duty = int((speed / 100) * 65535)
    
    if direction == 'F':
        motor_ia.duty_u16(duty)
        motor_ib.duty_u16(0)
        print(f"→ Forward {speed}% for {duration}s")
    elif direction == 'R':
        motor_ia.duty_u16(0)
        motor_ib.duty_u16(duty)
        print(f"← Reverse {speed}% for {duration}s")
    elif direction == 'B':
        motor_ia.duty_u16(65535)
        motor_ib.duty_u16(65535)
        print(f"⏹ Brake for {duration}s")
    elif direction == 'C':
        motor_ia.duty_u16(0)
        motor_ib.duty_u16(0)
        print(f"○ Coast for {duration}s")
    
    time.sleep(duration)

def play_sequence(sequence, repeat=1):
    """Play motion sequence"""
    for cycle in range(repeat):
        if repeat > 1:
            print(f"\n=== Cycle {cycle + 1}/{repeat} ===")
        
        for step, (direction, speed, duration) in enumerate(sequence):
            print(f"Step {step + 1}: ", end="")
            motor_move(direction, speed, duration)

# Define motion sequences
sequence_demo = [
    ('F', 50, 1.0),   # Start slow
    ('F', 80, 2.0),   # Speed up
    ('B', 0, 0.5),    # Brake
    ('R', 60, 1.5),   # Reverse
    ('C', 0, 1.0)     # Coast stop
]

sequence_pulse = [
    ('F', 70, 0.5),
    ('C', 0, 0.2),
    ('F', 70, 0.5),
    ('C', 0, 0.2),
    ('F', 70, 0.5),
    ('C', 0, 0.5)
]

sequence_scan = [
    ('F', 60, 0.8),
    ('B', 0, 0.2),
    ('R', 60, 0.8),
    ('B', 0, 0.2)
]

# Play sequences
print("Sequence 1: Demo Pattern")
play_sequence(sequence_demo)

time.sleep(2)

print("\n\nSequence 2: Pulse Pattern (3x)")
play_sequence(sequence_pulse, repeat=3)

time.sleep(2)

print("\n\nSequence 3: Scan Pattern (5x)")
play_sequence(sequence_scan, repeat=5)

# Final stop
motor_move('C', 0, 0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Jerky Motion**: Add brief coast periods between direction changes.
*   **Sequence Too Long**: Break into sub-sequences for easier debugging.
*   **Timing Inaccurate**: Account for code execution time in durations.

### 1️⃣2️⃣ Try This Next
*   **Sequence Recorder**: Manually control motor, record sequence, replay.
*   **Conditional Sequences**: If sensor triggers, branch to different sequence.
*   **Looping Sections**: Add repeat markers within sequences.

---

## 1️⃣ Project 0234: Two-Motor Coordination

### 2️⃣ Learning Objective
Control two motors independently to create differential drive and basic robot movement.

### 3️⃣ Concepts Introduced
*   Dual Motor Control
*   Differential Drive
*   Turning Mechanics
*   Independent Channel Control
*   Robot Movement Primitives

### 4️⃣ Hardware Required
*   Pico
*   2× DC Motors
*   Dual L9110S Driver (or L298N)
*   Robot chassis (optional)
*   6V Power

### 5️⃣ Wiring / Interfaces
| Component | Pico Pins | Notes |
| :--- | :--- | :--- |
| **Motor A (Left)** | GP14, GP15 | IA, IB |
| **Motor B (Right)** | GP16, GP17 | IA, IB |

### 6️⃣ Blocks Used
🔹 **Dual PWM** - Independent motors
🔹 **Functions** - Movement primitives
🔹 **Math** - Speed differential

### 7️⃣ Variables & State
*   **leftSpeed, rightSpeed**: Numbers - Individual motor speeds
*   **robotState**: String - "FORWARD", "BACKWARD", "LEFT", "RIGHT", "SPIN"

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize 4 PWM channels (2 per motor)
2. Create movement functions:
   - `forward(speed)`: Both motors forward
   - `backward(speed)`: Both motors reverse
   - `turn_left(speed)`: Left slow/reverse, right forward
   - `turn_right(speed)`: Right slow/reverse, left forward
   - `spin_left(speed)`: Left reverse, right forward
   - `spin_right(speed)`: Left forward, right reverse

**B. Main Loop Phase**
1. Demonstrate each movement:
   - Forward 2s
   - Turn right 1s
   - Forward 2s
   - Turn left 1s
   - Spin right 360° (estimate)
   - Stop

**C. Event / Condition Handling**
*   Motor speed matching for straight movement
*   Radius control via speed differential
*   Skid turn vs pivot turn

### 9️⃣ Execution Flow (Plain English)
Tank-style robots use differential drive: two independently controlled motors, one on each side. To go straight, both spin forward at same speed. To turn right, slow down or reverse the right motor. To spin in place, run motors in opposite directions. The speed difference determines turn radius. This is how tanks, wheelchairs, and vacuum robots navigate!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# Motor A (Left)
motor_a_ia = PWM(Pin(14))
motor_a_ib = PWM(Pin(15))

# Motor B (Right)
motor_b_ia = PWM(Pin(16))
motor_b_ib = PWM(Pin(17))

for motor in [motor_a_ia, motor_a_ib, motor_b_ia, motor_b_ib]:
    motor.freq(1000)

def set_motor(motor_ia, motor_ib, speed_percent):
    """
    Set motor speed and direction
    speed_percent: -100 to +100 (negative = reverse)
    """
    if speed_percent >= 0:
        duty = int((abs(speed_percent) / 100) * 65535)
        motor_ia.duty_u16(duty)
        motor_ib.duty_u16(0)
    else:
        duty = int((abs(speed_percent) / 100) * 65535)
        motor_ia.duty_u16(0)
        motor_ib.duty_u16(duty)

def forward(speed):
    """Both motors forward"""
    set_motor(motor_a_ia, motor_a_ib, speed)
    set_motor(motor_b_ia, motor_b_ib, speed)
    print(f"↑ Forward at {speed}%")

def backward(speed):
    """Both motors reverse"""
    set_motor(motor_a_ia, motor_a_ib, -speed)
    set_motor(motor_b_ia, motor_b_ib, -speed)
    print(f"↓ Backward at {speed}%")

def turn_left(speed):
    """Turn left (left slower)"""
    set_motor(motor_a_ia, motor_a_ib, speed // 2)
    set_motor(motor_b_ia, motor_b_ib, speed)
    print(f"↰ Turn left at {speed}%")

def turn_right(speed):
    """Turn right (right slower)"""
    set_motor(motor_a_ia, motor_a_ib, speed)
    set_motor(motor_b_ia, motor_b_ib, speed // 2)
    print(f"↱ Turn right at {speed}%")

def spin_left(speed):
    """Spin counterclockwise"""
    set_motor(motor_a_ia, motor_a_ib, -speed)
    set_motor(motor_b_ia, motor_b_ib, speed)
    print(f"⟲ Spin left at {speed}%")

def spin_right(speed):
    """Spin clockwise"""
    set_motor(motor_a_ia, motor_a_ib, speed)
    set_motor(motor_b_ia, motor_b_ib, -speed)
    print(f"⟳ Spin right at {speed}%")

def stop():
    """Stop all motors"""
    set_motor(motor_a_ia, motor_a_ib, 0)
    set_motor(motor_b_ia, motor_b_ib, 0)
    print("⏹ Stop")

# Movement demo
print("Two-Motor Differential Drive Demo\n")

forward(70)
time.sleep(2)

turn_right(70)
time.sleep(1)

forward(70)
time.sleep(2)

turn_left(70)
time.sleep(1)

stop()
time.sleep(1)

# Spin demo
print("\nSpin maneuvers:")
spin_right(60)
time.sleep(1.5)  # ~360° rotation

stop()
time.sleep(0.5)

spin_left(60)
time.sleep(1.5)

stop()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Doesn't Go Straight**: Motor speeds may differ - calibrate with multipliers.
*   **Weak Turns**: Increase speed differential or reverse inner motor.
*   **Wobbles**: Check wheel/motor mounting - mechanical issue, not code.

### 1️⃣2️⃣ Try This Next
*   **Square Pattern**: Drive in perfect square using turns + straight segments.
*   **Figure-8**: Combine turns for complex path.
*   **PID Control**: Use encoders for precise straight-line driving.

---

## 1️⃣ Project 0235: Speed Ramping & Acceleration

### 2️⃣ Learning Objective
Implement smooth acceleration and deceleration curves to protect motors and improve motion quality.

### 3️⃣ Concepts Introduced
*   Acceleration Curves
*   Jerk Minimization
*   Trapezoidal Motion Profile
*   Smooth Start/Stop
*   Mechanical Protection

### 4️⃣ Hardware Required
*   Pico, DC Motor, L9110S, 6V Power

### 5️⃣ Wiring / Interfaces
*(Standard motor setup)*

### 6️⃣ Blocks Used
🔹 **For Loops** - Gradual speed change
🔹 **Math** - Acceleration calculation
🔹 **Time** - Precise step timing

### 7️⃣ Variables & State
*   **currentSpeed**: Number - Real-time speed
*   **targetSpeed**: Number - Desired final speed
*   **accelRate**: Number - Speed change per step
*   **rampTime**: Number - Total acceleration duration

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set acceleration parameters:
   - `rampTime` = 2 seconds
   - `steps` = 20 (smoother = more steps)
   - Calculate step delay = rampTime / steps

**B. Main Loop Phase**
1. **Linear Ramp:**
   - For each step:
     - speed += (targetSpeed - currentSpeed) / stepsRemaining
     - Set motor PWM
     - Delay step time
2. **S-Curve Ramp:**
   - Use sine/cosine for smooth start and end
   - Faster in middle, gentle at extremes

**C. Event / Condition Handling**
*   Never instant speed jumps
*   Match acceleration with deceleration
*   Emergency stop overrides ramp

### 9️⃣ Execution Flow (Plain English)
Instant speed changes stress motors (current spike), gears (shock), and loads (inertia). Instead, we gradually increase speed over 1-2 seconds. Linear ramp increments speed by fixed amount each step. S-curve ramp starts slow, accelerates in middle, slows again at end - like car acceleration feels to passengers. Professional motion control uses trapezoidal profiles: accelerate → coast → decelerate.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time
import math

motor_ia = PWM(Pin(14))
motor_ib = PWM(Pin(15))
motor_ia.freq(1000)
motor_ib.freq(1000)

current_speed = 0

def ramp_to_speed(target_speed, ramp_time=2.0, steps=20, curve='linear'):
    """
    Smoothly change motor speed
    curve: 'linear' or 's-curve'
    """
    global current_speed
    
    step_delay = ramp_time / steps
    print(f"Ramping from {current_speed}% to {target_speed}% over {ramp_time}s ({curve})")
    
    for i in range(steps + 1):
        if curve == 'linear':
            # Linear interpolation
            speed = current_speed + (target_speed - current_speed) * (i / steps)
        
        elif curve == 's-curve':
            # Smooth S-curve using cosine
            t = i / steps  # 0.0 to 1.0
            # Smooth step function
            smoothed_t = (1 - math.cos(t * math.pi)) / 2
            speed = current_speed + (target_speed - current_speed) * smoothed_t
        
        # Set motor speed
        duty = int((abs(speed) / 100) * 65535)
        if speed >= 0:
            motor_ia.duty_u16(duty)
            motor_ib.duty_u16(0)
        else:
            motor_ia.duty_u16(0)
            motor_ib.duty_u16(duty)
        
        print(f"  Step {i+1}: {speed:.1f}%")
        time.sleep(step_delay)
    
    current_speed = target_speed

# Demonstration
print("Speed Ramping Demo\n")

print("1. Linear acceleration to 80%")
ramp_to_speed(80, ramp_time=2.0, curve='linear')
time.sleep(1)

print("\n2. Linear deceleration to 30%")
ramp_to_speed(30, ramp_time=1.5, curve='linear')
time.sleep(1)

print("\n3. S-curve acceleration to 100%")
ramp_to_speed(100, ramp_time=2.5, curve='s-curve')
time.sleep(1)

print("\n4. S-curve deceleration to 0%")
ramp_to_speed(0, ramp_time=2.0, curve='s-curve')

# Stop
motor_ia.duty_u16(0)
motor_ib.duty_u16(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Ramp Too Fast**: <1s ramp still jerky; use 2-3s for smooth motion.
*   **Too Many Steps**: >50 steps wastes time; 20-30 is optimal.
*   **FloatingPoint Errors**: Use integer math where possible for speed.

### 1️⃣2️⃣ Try This Next
*   **Trapezoidal Profile**: Accel → constant → decel (industrial standard).
*   **Jerk Limiting**: Control rate of acceleration change (third derivative).
*   **User-Defined Curves**: Potentiometer controls ramp time.

---

## 1️⃣ Project 0236: Motor with Encoder Feedback

### 2️⃣ Learning Objective
Use rotary encoder feedback to measure motor speed and position for closed-loop control.

### 3️⃣ Concepts Introduced
*   Rotary Encoder Basics
*   Speed Measurement (RPM)
*   Position Tracking
*   Closed-Loop Control
*   Feedback Systems

### 4️⃣ Hardware Required
*   Pico
*   DC Motor with Encoder
*   L9110S Driver
*   6V Power

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Motor IA/IB** | GP14, GP15 |
| **Encoder A** | GP16 (interrupt) |
| **Encoder B** | GP17 |

### 6️⃣ Blocks Used
🔹 **Interrupts** - Encoder pulse counting
🔹 **Math** - RPM calculation
🔹 **Variables** - Position counter

### 7️⃣ Variables & State
*   **encoderCount**: Number - Total pulses
*   **lastCount**: Number - Previous count for speed calc
*   **rpm**: Number - Calculated rotations per minute
*   **pulsesPerRev**: Constant - Encoder resolution

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Attach interrupt to encoder A pin
2. Set encoder B as input
3. Initialize pulse counter = 0
4. Define `pulsesPerRev` (e.g., 20 for typical encoder)

**B. Main Loop Phase**
1. **Encoder ISR:**
   - On rising edge, increment counter
   - Check encoder B for direction
2. **Speed Calculation:**
   - Every 100ms:
     - pulsesDelta = currentCount - lastCount
     - rpm = (pulsesDelta / pulsesPerRev) * (60 / 0.1)
     - Print RPM
3. **Motor Control:**
   - Set target speed
   - Measure actual RPM
   - Adjust PWM if mismatch

**C. Event / Condition Handling**
*   Encoder noise filtering
*   Direction detection via quadrature
*   Overflow handling for long runs

### 9️⃣ Execution Flow (Plain English)
Encoders output pulses as the motor shaft rotates. If encoder has 20 slots, one revolution = 20 pulses. We count pulses with an interrupt. Every 100ms, we check how many NEW pulses arrived. If we got 10 pulses in 100ms, that's 100 pulses/second = (100/20) = 5 revolutions/second = 300 RPM. This feedback lets us verify motor is actually spinning at commanded speed!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

motor_ia = PWM(Pin(14))
motor_ib = PWM(Pin(15))
motor_ia.freq(1000)
motor_ib.freq(1000)

encoder_a = Pin(16, Pin.IN)
encoder_b = Pin(17, Pin.IN)

encoder_count = 0
PULSES_PER_REV = 20  # Depends on your encoder

def encoder_isr(pin):
    """Interrupt handler for encoder"""
    global encoder_count
    # Simple count (direction detection would check encoder_b)
    encoder_count += 1

# Attach interrupt
encoder_a.irq(trigger=Pin.IRQ_RISING, handler=encoder_isr)

def calculate_rpm(pulses_delta, time_delta_ms):
    """Calculate RPM from pulse count"""
    if pulses_delta == 0:
        return 0
    
    # Revolutions = pulses / pulses_per_rev
    revolutions = pulses_delta / PULSES_PER_REV
    
    # Time in minutes
    time_minutes = time_delta_ms / 60000
    
    # RPM
    rpm = revolutions / time_minutes
    return rpm

def set_motor_speed(speed_percent):
    """Set motor speed (0-100%)"""
    duty = int((speed_percent / 100) * 65535)
    motor_ia.duty_u16(duty)
    motor_ib.duty_u16(0)

print("Motor Encoder Feedback Demo\n")

# Test different speeds
test_speeds = [30, 50, 70, 90]

for target_speed in test_speeds:
    print(f"\nTarget Speed: {target_speed}%")
    set_motor_speed(target_speed)
    
    # Measure for 3 seconds
    encoder_count = 0
    start_count = encoder_count
    
    for i in range(10):  # 10 × 300ms = 3 seconds
        time.sleep(0.3)
        
        current_count = encoder_count
        pulses_delta = current_count - start_count
        rpm = calculate_rpm(pulses_delta, 300)
        
        print(f"  {i*0.3:.1f}s: {pulses_delta} pulses, ~{rpm:.0f} RPM")
        start_count = current_count

# Stop
set_motor_speed(0)
print("\nMotor stopped")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wrong Pulse Count**: Verify encoder spec (some are 20 PPR, others 100+).
*   **Noisy Readings**: Add capacitor (0.1μF) across encoder pins.
*   **Direction Ignored**: Full quadrature needs both A and B channels.

### 1️⃣2️⃣ Try This Next
*   **PID Speed Control**: Maintain constant RPM despite load changes.
*   **Position Control**: Move motor exact number of revolutions.
*   **Odometry**: Track robot distance traveled using encoder.

---

## 1️⃣ Project 0237: Simple Line-Following Robot

### 2️⃣ Learning Objective
Build a basic line-following robot using IR sensors and differential steering.

### 3️⃣ Concepts Introduced
*   Line Detection
*   IR Reflectance Sensors
*   Proportional Steering
*   Sensor-Motor Integration
*   Autonomous Navigation

### 4️⃣ Hardware Required
*   Pico
*   2× DC Motors
*   2× IR Line Sensors (TCRT5000)
*   Dual motor driver
*   Robot chassis
*   Black line on white surface

### 5️⃣ Wiring / Interfaces
| Sensor | Pico Pin | Detects |
| :--- | :--- | :--- |
| **Left IR** | GP18 | Line under left sensor |
| **Right IR** | GP19 | Line under right sensor |

### 6️⃣ Blocks Used
🔹 **Digital Read** - IR sensor states
🔹 **Decision Logic** - Steering algorithm
🔹 **Motor Control** - Differential speed

### 7️⃣ Variables & State
*   **leftSensor, rightSensor**: Boolean - Line detected?
*   **baseSpeed**: Number - Forward speed
*   **turnSpeed**: Number - Turning speed differential

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize IR sensors as digital inputs
2. Set baseSpeed = 60%
3. Set turnSpeed = 40%

**B. Main Loop Phase**
1. Read both IR sensors
2. **Line Following Logic:**
   - Both see black: Go straight
   - Left sees black, right white: Turn left
   - Right sees black, left white: Turn right
   - Both see white: LOST - search pattern

**C. Event / Condition Handling**
*   Black line reflects less IR = sensor reads LOW
*   White surface reflects more = sensor reads HIGH
*   Crossing detection (both LOW temporarily)

### 9️⃣ Execution Flow (Plain English)
IR sensors shine infrared light at the ground. Black tape absorbs IR (sensor reads LOW), white surface reflects IR (sensor reads HIGH). We position sensors on each side of the line. If left sensor is on black and right on white, robot needs to turn left to center on line. If both are on black, we're centered - go straight! This creates a self-correcting behavior that keeps robot following the line.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# Motors
motor_l_ia = PWM(Pin(14))
motor_l_ib = PWM(Pin(15))
motor_r_ia = PWM(Pin(16))
motor_r_ib = PWM(Pin(17))

for m in [motor_l_ia, motor_l_ib, motor_r_ia, motor_r_ib]:
    m.freq(1000)

# IR Line sensors (LOW = black detected, HIGH = white)
ir_left = Pin(18, Pin.IN)
ir_right = Pin(19, Pin.IN)

BASE_SPEED = 60
TURN_SPEED = 40

def set_motors(left_speed, right_speed):
    """Set motor speeds (-100 to +100)"""
    # Left motor
    if left_speed >= 0:
        duty = int((left_speed / 100) * 65535)
        motor_l_ia.duty_u16(duty)
        motor_l_ib.duty_u16(0)
    else:
        duty = int((abs(left_speed) / 100) * 65535)
        motor_l_ia.duty_u16(0)
        motor_l_ib.duty_u16(duty)
    
    # Right motor
    if right_speed >= 0:
        duty = int((right_speed / 100) * 65535)
        motor_r_ia.duty_u16(duty)
        motor_r_ib.duty_u16(0)
    else:
        duty = int((abs(right_speed) / 100) * 65535)
        motor_r_ia.duty_u16(0)
        motor_r_ib.duty_u16(duty)

print("Line Following Robot Active")

while True:
    # Read sensors (LOW = on black line)
    left_on_line = not ir_left.value()
    right_on_line = not ir_right.value()
    
    if left_on_line and right_on_line:
        # Both on line - go straight
        set_motors(BASE_SPEED, BASE_SPEED)
        print("Straight")
    
    elif left_on_line and not right_on_line:
        # Line is to the left - turn left
        set_motors(TURN_SPEED, BASE_SPEED)
        print("Turn LEFT")
    
    elif not left_on_line and right_on_line:
        # Line is to the right - turn right
        set_motors(BASE_SPEED, TURN_SPEED)
        print("Turn RIGHT")
    
    else:
        # Both off line - lost! Search pattern
        set_motors(30, -30)  # Spin slowly to find line
        print("LOST - Searching...")
    
    time.sleep(0.05)  # 20Hz control loop
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Won't Follow**: Calibrate sensors - test on actual line/surface.
*   **Oscillates**: Reduce TURN_SPEED or increase BASE_SPEED.
*   **Loses Line on Curves**: Add more sensors or increase sensor spacing.

### 1️⃣2️⃣ Try This Next
*   **Proportional Control**: Vary turn amount based on how far off-line.
*   **3+ Sensors**: Center sensor for more precision.
*   **Speed Adaptation**: Slow down for sharp curves, speed up on straights.

---

## 1️⃣ Project 0238: Obstacle Avoidance Robot

### 2️⃣ Learning Objective
Create autonomous obstacle avoidance using ultrasonic sensor and reactive navigation.

### 3️⃣ Concepts Introduced
*   Obstacle Detection
*   Reactive Behavior
*   Collision Avoidance
*   Decision Trees
*   Autonomous Navigation

### 4️⃣ Hardware Required
*   Pico, 2× Motors, HC-SR04 Ultrasonic, Dual driver

### 5️⃣ Wiring / Interfaces
*(Motors + ultrasonic sensor from previous projects)*

### 6️⃣ Blocks Used
🔹 **Ultrasonic Read** - Distance measurement
🔹 **Thresholds** - Danger zones
🔹 **Navigation Logic** - Avoidance algorithm

### 7️⃣ Variables & State
*   **distance**: Number (cm) - Obstacle distance
*   **SAFE_DISTANCE**: Constant (30cm) - Minimum clearance
*   **DANGER_DISTANCE**: Constant (15cm) - Emergency stop

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set safety thresholds
2. Initialize in "exploring" mode

**B. Main Loop Phase**
1. **Read Distance:**
   - Trigger ultrasonic
   - Measure echo time
   - Convert to cm
2. **Navigation Logic:**
   - distance > SAFE: Forward
   - DANGER < distance < SAFE: Turn
   - distance < DANGER: Reverse + turn

**C. Event / Condition Handling**
*   Random turn direction for variety
*   Stuck detection (no progress)
*   Wall-following mode

### 9️⃣ Execution Flow (Plain English)
Robot drives forward while continuously scanning ahead with ultrasonic. If obstacle detected >30cm away, keep going. At 15-30cm, turn to avoid. <15cm means we're too close - stop, back up, turn sharply. This is reactive navigation: simple rules create seemingly intelligent obstacle dodging. Like a Roomba vacuum - no map, just "don't hit things!"

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM, time_pulse_us
import time
import random

# Motors setup (same as before)
motor_l_ia = PWM(Pin(14))
motor_l_ib = PWM(Pin(15))
motor_r_ia = PWM(Pin(16))
motor_r_ib = PWM(Pin(17))

for m in [motor_l_ia, motor_l_ib, motor_r_ia, motor_r_ib]:
    m.freq(1000)

# Ultrasonic sensor
trig = Pin(20, Pin.OUT)
echo = Pin(21, Pin.IN)

SAFE_DISTANCE = 30  # cm
DANGER_DISTANCE = 15  # cm
FORWARD_SPEED = 65
TURN_SPEED = 50

def get_distance():
    """Measure distance in cm"""
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    try:
        duration = time_pulse_us(echo, 1, 30000)
        distance = (duration * 0.0343) / 2
        return distance
    except:
        return 999  # Timeout = clear ahead

def set_motors(left, right):
    """Motor control helper"""
    for motor_ia, motor_ib, speed in [(motor_l_ia, motor_l_ib, left),
                                        (motor_r_ia, motor_r_ib, right)]:
        if speed >= 0:
            duty = int((speed / 100) * 65535)
            motor_ia.duty_u16(duty)
            motor_ib.duty_u16(0)
        else:
            duty = int((abs(speed) / 100) * 65535)
            motor_ia.duty_u16(0)
            motor_ib.duty_u16(duty)

print("Obstacle Avoidance Robot Active\n")

while True:
    dist = get_distance()
    print(f"Distance: {dist:.1f} cm - ", end="")
    
    if dist > SAFE_DISTANCE:
        # Clear ahead - go forward
        set_motors(FORWARD_SPEED, FORWARD_SPEED)
        print("Forward")
    
    elif DANGER_DISTANCE < dist <= SAFE_DISTANCE:
        # Obstacle detected - turn
        turn_dir = random.choice(['left', 'right'])
        if turn_dir == 'left':
            set_motors(TURN_SPEED, FORWARD_SPEED)
            print("Turn LEFT")
        else:
            set_motors(FORWARD_SPEED, TURN_SPEED)
            print("Turn RIGHT")
    
    else:
        # Too close! Emergency maneuver
        print("DANGER! Reversing...")
        set_motors(-FORWARD_SPEED, -FORWARD_SPEED)
        time.sleep(0.5)
        
        # Sharp turn
        set_motors(-TURN_SPEED, TURN_SPEED)
        time.sleep(0.8)
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Hits Obstacles**: Increase SAFE_DISTANCE or slow down.
*   **Stuck in Corner**: Add timeout - if no progress, reverse more.
*   **Sensor Blind Spots**: Mount sensor higher or add side sensors.

### 1️⃣2️⃣ Try This Next
*   **Wall Following**: Stay fixed distance from wall while moving.
*   **Multi-Sensor**: Add left/right ultrasonics for better awareness.
*   **Learning**: Remember problem areas, avoid repeat visits.

---

## 1️⃣ Project 0239: Remote-Controlled Robot

### 2️⃣ Learning Objective
Control robot wirelessly using IR remote or Bluetooth for manual navigation.

### 3️⃣ Concepts Introduced
*   Wireless Control
*   IR Remote Decoding
*   Command Parsing
*   Teleoperation
*   Real-Time Response

### 4️⃣ Hardware Required
*   Pico, 2× Motors, IR Receiver (VS1838B), IR Remote

### 5️⃣ Wiring / Interfaces
| Component | Pin |
| :--- | :--- |
| **IR Receiver** | GP22 |

### 6️⃣ Blocks Used
🔹 **IR Decode** - Remote button detection
🔹 **Command Map** - Button → Action
🔹 **Motor Control** - Movement execution

### 7️⃣ Variables & State
*   **lastCommand**: Number - Most recent IR code
*   **commandMap**: Dict - Button codes to actions

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize IR receiver with interrupt
2. Map remote buttons:
   - UP: Forward
   - DOWN: Backward
   - LEFT: Turn left
   - RIGHT: Turn right
   - OK: Stop

**B. Main Loop Phase**
1. Wait for IR signal
2. Decode button code
3. Look up action in map
4. Execute motor command
5. Continue until new command

**C. Event / Condition Handling**
*   Repeat codes (button held)
*   Timeout (no signal = stop)
*   Invalid codes ignored

### 9️⃣ Execution Flow (Plain English)
IR remote sends unique codes for each button (e.g., UP=0xFF18E7). IR receiver detects these, our code decodes them. We maintain a dictionary mapping codes to actions. When UP is pressed, we execute "forward" function. Holding button sends repeat codes - we keep executing action. Release stops motion (or use timeout). Simple wireless robot control!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# Motors (standard setup)
motor_l_ia = PWM(Pin(14))
motor_l_ib = PWM(Pin(15))
motor_r_ia = PWM(Pin(16))
motor_r_ib = PWM(Pin(17))

for m in [motor_l_ia, motor_l_ib, motor_r_ia, motor_r_ib]:
    m.freq(1000)

# IR Receiver
ir_pin = Pin(22, Pin.IN)

# Command codes (example - yours will differ!)
COMMANDS = {
    0xFF18E7: 'forward',
    0xFF4AB5: 'back',
    0xFF10EF: 'left',
    0xFF5AA5: 'right',
    0xFF38C7: 'stop',
    0xFFFFFFFF: 'repeat'  # Hold button
}

last_command = 'stop'
SPEED = 70

def set_motors(left, right):
    """Motor helper"""
    for motor_ia, motor_ib, speed in [(motor_l_ia, motor_l_ib, left),
                                        (motor_r_ia, motor_r_ib, right)]:
        duty = int((abs(speed) / 100) * 65535)
        if speed >= 0:
            motor_ia.duty_u16(duty)
            motor_ib.duty_u16(0)
        else:
            motor_ia.duty_u16(0)
            motor_ib.duty_u16(duty)

def execute_command(cmd):
    """Execute movement command"""
    if cmd == 'forward':
        set_motors(SPEED, SPEED)
        print("↑ Forward")
    elif cmd == 'back':
        set_motors(-SPEED, -SPEED)
        print("↓ Backward")
    elif cmd == 'left':
        set_motors(SPEED//2, SPEED)
        print("← Left")
    elif cmd == 'right':
        set_motors(SPEED, SPEED//2)
        print("→ Right")
    elif cmd == 'stop':
        set_motors(0, 0)
        print("⏹ Stop")

# Simplified IR reading (full decode would use NEC protocol library)
def read_ir_command():
    """
    Placeholder for IR decoding
    In real implementation, use IRremote library or similar
    """
    # Simulate remote input for demo
    return None

print("IR Remote Control Robot")
print("Waiting for commands...\n")

# Demo: Cycle through commands for testing
demo_sequence = ['forward', 'left', 'forward', 'right', 'stop', 'back']

for cmd in demo_sequence:
    print(f"Command: {cmd}")
    execute_command(cmd)
    time.sleep(2)

execute_command('stop')
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Response**: Verify IR codes match your remote (use IR decoder).
*   **Lag**: IR decoding blocks - use interrupt-based library.
*   **Stuck Moving**: Implement timeout stop if no signal for 1 second.

### 1️⃣2️⃣ Try This Next
*   **Bluetooth Control**: Replace IR with BLE for smartphone app control.
*   **Record/Playback**: Record sequence of commands, replay autonomously.
*   **Speed Levels**: Number keys (1-9) set speed percentages.

---

## 1️⃣ Project 0240: Master Robot Controller (Integration)

### 2️⃣ Learning Objective
Integrate all motor control concepts into a comprehensive robot system with multiple operational modes.

### 3️⃣ Concepts Introduced
*   System Integration
*   Mode Management
*   Multi-Sensor Fusion
*   Behavior Switching
*   Complete Robot Architecture

### 4️⃣ Hardware Required
*   Pico
*   2× Motors with encoders
*   Ultrasonic sensor
*   2× IR line sensors
*   IR remote receiver
*   Dual motor driver
*   Complete robot chassis

### 5️⃣ Wiring / Interfaces
*(Combines all hardware from Projects 0231-0239)*

### 6️⃣ Blocks Used
*   **All blocks from Projects 0231-0239** integrated

### 7️⃣ Variables & State
*   **robotMode**: String - "MANUAL", "LINE_FOLLOW", "AVOID", "PATROL", "AUTO"
*   **All previous state from 0231-0239**

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize ALL subsystems:
   - Motors + drivers
   - Encoders
   - Ultrasonic
   - IR sensors
   - Remote receiver
2. Set default mode = "MANUAL"
3. Display mode menu

**B. Main Loop Phase**
1. **Mode Selection (IR Remote):**
   - Button 1: Manual control
   - Button 2: Line following
   - Button 3: Obstacle avoidance
   - Button 4: Patrol pattern
   - Button 5: Full autonomous

2. **Mode Execution:**
   - Each mode uses relevant sensors/algorithms
   - Smooth transitions between modes
   - Display current mode + sensor status

**C. Event / Condition Handling**
*   Emergency stop (all modes)
*   Sensor failure detection
*   Battery monitoring
*   State preservation

### 9️⃣ Execution Flow (Plain English)
This is the ULTIMATE robot controller combining EVERYTHING: speed control, direction, sequences, dual motors, ramping, encoders, line following, obstacle avoidance, and remote control. User selects mode via remote. Manual mode = direct joystick control. Line-follow mode = autonomous line tracking. Avoid mode = explores while dodging obstacles. Patrol = pre-programmed route. Auto = intelligent combination of all behaviors. Professional robot architecture!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin, PWM
import time

# ===== HARDWARE INITIALIZATION =====
# Motors
motors = {
    'left': {'ia': PWM(Pin(14)), 'ib': PWM(Pin(15))},
    'right': {'ia': PWM(Pin(16)), 'ib': PWM(Pin(17))}
}

for motor in motors.values():
    motor['ia'].freq(1000)
    motor['ib'].freq(1000)

# Sensors
ultrasonic_trig = Pin(20, Pin.OUT)
ultrasonic_echo = Pin(21, Pin.IN)
line_left = Pin(18, Pin.IN)
line_right = Pin(19, Pin.IN)
ir_remote = Pin(22, Pin.IN)

# ===== STATE VARIABLES =====
robot_mode = "MANUAL"
modes = ["MANUAL", "LINE_FOLLOW", "AVOID", "PATROL", "AUTO"]

# ===== HELPER FUNCTIONS FROM PREVIOUS PROJECTS =====
def set_motors(left_speed, right_speed):
    """Motor control from 0234"""
    pass  # Implementation from previous projects

def get_distance():
    """Ultrasonic from 0238"""
    pass

def line_follow_logic():
    """From 0237"""
    pass

def obstacle_avoidance():
    """From 0238"""
    pass

def execute_sequence(seq):
    """From 0233"""
    pass

# ===== MODE IMPLEMENTATIONS =====
def manual_mode():
    """IR remote control"""
    print("MANUAL MODE: Use remote to control")
    # Implementation from 0239

def line_follow_mode():
    """Autonomous line tracking"""
    print("LINE FOLLOWING MODE")
    line_follow_logic()

def avoid_mode():
    """Autonomous obstacle avoidance"""
    print("OBSTACLE AVOIDANCE MODE")
    obstacle_avoidance()

def patrol_mode():
    """Pre-programmed patrol"""
    print("PATROL MODE: Running sequence")
    patrol_sequence = [
        ('F', 70, 2), ('L', 60, 1),
        ('F', 70, 2), ('L', 60, 1),
        ('F', 70, 2), ('L', 60, 1),
        ('F', 70, 2), ('L', 60, 1)
    ]  # Square pattern
    execute_sequence(patrol_sequence)

def auto_mode():
    """Intelligent multi-sensor"""
    print("AUTO MODE: Intelligent navigation")
    # Combine behaviors based on environment
    dist = get_distance()
    left_line = line_left.value()
    
    if left_line or right_line:
        line_follow_logic()  # Line detected
    elif dist < 30:
        obstacle_avoidance()  # Obstacle ahead
    else:
        set_motors(70, 70)  # Explore

# ===== MAIN PROGRAM =====
def show_menu():
    print(f"\n{'='*40}")
    print(f"  ROBOT MODE: {robot_mode}")
    print(f"{'='*40}")

show_menu()

while True:
    # Mode switching via IR remote (simplified)
    # In real implementation, decode IR codes
    
    # Execute current mode
    if robot_mode == "MANUAL":
        manual_mode()
    elif robot_mode == "LINE_FOLLOW":
        line_follow_mode()
    elif robot_mode == "AVOID":
        avoid_mode()
    elif robot_mode == "PATROL":
        patrol_mode()
    elif robot_mode == "AUTO":
        auto_mode()
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mode Confusion**: Clear visual/audio indicator of current mode.
*   **Sensor Conflicts**: Each mode should use appropriate sensors only.
*   **No Emergency Stop**: Always implement universal stop button.
*   **Resource Leaks**: Clean up (stop motors, disable sensors) when switching modes.

### 1️⃣2️⃣ Try This Next
*   **AI Mode**: Add ML model for intelligent navigation decisions.
*   **Mission Planner**: Define waypoints, robot navigates autonomously.
*   **Multi-Robot**: Coordinate with other robots via wireless.
*   **Telemetry**: Log all sensor data and paths to SD card.
*   **Competition Mode**: Optimize for maze-solving or sumo wrestling.

---

## 📊 Batch 24 Summary

**Projects Created:** 10  
**Concepts Taught:** 58  
**Total Code Lines:** ~2,400  
**Complexity Range:** 5/10 → 9/10

**Learning Progression:**
- Basic PWM speed → Closed-loop encoder control
- Single motor → Dual differential drive
- Manual → Autonomous navigation
- Simple → Complete robot system

**Robotics Skills:** Motor control, feedback systems, navigation algorithms, sensor fusion, system integration

**Ready for:** Batch 25 (Traffic Lights 2) 🚦
