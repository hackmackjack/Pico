# COMPLETE BATCH 36 & PASS 2: Generate Projects 0354-0360
# Final 7 projects to achieve 60/60 completion

print("🎯 FINAL STRETCH - Completing Pass 2...")
print("Generating Projects 0354-0360 (Final 7 projects)")

final_7_projects = '''
## 1️⃣ Project 0354: Robotic Arm Basics Sequences

### 2️⃣ Learning Objective
Create choreographed multi-servo boxing sequence. You will learn coordinated dual-servo control and predefined action sequences.

### 3️⃣ Concepts Introduced
*   **Multi-Servo Coordination**: Controlling multiple servos in sequence.
*   **Choreographed Actions**: Predefined movement patterns.
*   **Timing Synchronization**: Coordinating multiple actuators.

### 4️⃣ Hardware Required
*   **Pico**
*   **2× Servo Motors** (Left & Right arms)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Left Servo** | GP12 | Left arm control |
| **Right Servo** | GP13 | Right arm control |

### 6️⃣ Blocks Used

🔹 **Setup Servo (×2)**
*   **Category:** Motors & Motion

🔹 **Servo Write Angle**
*   **Category:** Motors & Motion

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   None (predefined sequence).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Motors & Motion**, drag `Setup Servo pin:[12]` (Left).
        *   **Snap** into setup block.
    *   From **Motors & Motion**, drag `Setup Servo pin:[13]` (Right).
        *   **Snap** into setup block.
    *   **Set Starting Position**:
        *   From **Motors & Motion**, drag `set servo [12] angle [90]`.
            *   **Snap** into setup block (neutral).
        *   From **Motors & Motion**, drag `set servo [13] angle [90]`.
            *   **Snap** into setup block (neutral).

*   **B. Main Loop Phase**
    *   **Left Hook**:
        *   From **Motors & Motion**, drag `set servo [12] angle [45]`.
            *   **Snap** into loop.
        *   From **Timing**, drag `sleep [0.5] seconds`.
            *   **Snap** below.
        *   From **Motors & Motion**, drag `set servo [12] angle [90]`.
            *   **Snap** below (return).
        *   From **Timing**, drag `sleep [0.3] seconds`.
            *   **Snap** below.
    *   **Right Jab**:
        *   From **Motors & Motion**, drag `set servo [13] angle [135]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.5] seconds`.
            *   **Snap** below.
        *   From **Motors & Motion**, drag `set servo [13] angle [90]`.
            *   **Snap** below (return).
        *   From **Timing**, drag `sleep [0.3] seconds`.
            *   **Snap** below.
    *   **Right Jab Again**:
        *   From **Motors & Motion**, drag `set servo [13] angle [135]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.5] seconds`.
            *   **Snap** below.
        *   From **Motors & Motion**, drag `set servo [13] angle [90]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.3] seconds`.
            *   **Snap** below.
    *   **Left Hook Again**:
        *   From **Motors & Motion**, drag `set servo [12] angle [45]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.5] seconds`.
            *   **Snap** below.
        *   From **Motors & Motion**, drag `set servo [12] angle [90]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below (pause before repeat).

### 9️⃣ Execution Flow (Plain English)

Two servos simulate boxing arms. The sequence executes: Left hook (45°), Right jab (135°), Right jab again, Left hook again. Each punch extends for 0.5s then returns to neutral (90°) with 0.3s between punches. After full combo, 1s pause before repeat. This demonstrates coordinated multi-actuator choreography useful for humanoid robots, animatronics, or interactive displays.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leftServo = machine.PWM(machine.Pin(12))
rightServo = machine.PWM(machine.Pin(13))
leftServo.freq(50)
rightServo.freq(50)

def set_servo_angle(servo, angle):
    duty = int(1640 + (angle / 180) * 4914)
    servo.duty_u16(duty)

# Neutral position
set_servo_angle(leftServo, 90)
set_servo_angle(rightServo, 90)
time.sleep(1)

while True:
    # Left hook
    set_servo_angle(leftServo, 45)
    time.sleep(0.5)
    set_servo_angle(leftServo, 90)
    time.sleep(0.3)
    
    # Right jab
    set_servo_angle(rightServo, 135)
    time.sleep(0.5)
    set_servo_angle(rightServo, 90)
    time.sleep(0.3)
    
    # Right jab again
    set_servo_angle(rightServo, 135)
    time.sleep(0.5)
    set_servo_angle(rightServo, 90)
    time.sleep(0.3)
    
    # Left hook again
    set_servo_angle(leftServo, 45)
    time.sleep(0.5)
    set_servo_angle(leftServo, 90)
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Servos Move Together**: Ensure each servo command is separate. If using servo library, verify different pin assignments.
*   **Power Issues**: Two servos draw significant current. Use external 5V supply with adequate amperage (2A+).
*   **Timing Off**: Adjust sleep durations to match desired boxing rhythm. Faster = more aggressive, slower = demonstration mode.

### 1️⃣2️⃣ Try This Next

*   **Sound Effects**: Add buzzer or speaker playing punch sounds synchronized with movements.
*   **Programmable Combos**: Use button presses to trigger different punch combinations.
*   **Speed Control**: Potentiometer adjusts overall sequence speed.

---

## 1️⃣ Project 0355: Interactive Robotic Arm Basics

### 2️⃣ Learning Objective
Implement variable velocity servo control using button hold duration. You will learn velocity profiling and smooth motion control.

### 3️⃣ Concepts Introduced
*   **Variable Velocity**: Adjusting servo speed based on input.
*   **Position Interpolation**: Breaking movement into small steps.
*   **Smooth Sweep**: Gradual position changes vs instant jumps.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Servo Motor**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Slow motion trigger, PULL_DOWN |
| **Servo Signal** | GP12 | PWM control |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs

🔹 **Setup Servo**
*   **Category:** Motors & Motion

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Servo Write Angle**
*   **Category:** Motors & Motion

🔹 **Loops**
*   **Category:** Loops

### 7️⃣ Variables & State
*   **targetAngle**: Desired final position.
*   **currentAngle**: Current servo position.
*   **buttonHeld**: Whether slow-motion button is pressed.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[10]`.
        *   **Snap** into setup block.
        *   Enable **PULL_DOWN** resistor.
    *   From **Motors & Motion**, drag `Setup Servo pin:[12]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [currentAngle] to [0]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [targetAngle] to [180]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Button State**:
        *   From **Pin Access**, drag `digital read pin [10]`.
            *   **Snap** into loop.
            *   Store in `buttonHeld`.
    *   **Choose Movement Speed**:
        *   From **Logic**, drag `if [buttonHeld] = HIGH then`.
            *   **Snap** below.
            *   Then (Slow Motion):
                *   From **Loops**, drag `for [step] from [currentAngle] to [targetAngle]`.
                    *   **Snap** inside (1° increments).
                    *   Inside loop:
                        *   From **Motors & Motion**, drag `set servo angle [step]`.
                            *   **Snap** inside.
                        *   From **Timing**, drag `sleep [0.028] seconds`.
                            *   **Snap** be low (180 steps × 0.028s ≈ 5s total).
            *   Else (Fast Motion):
                *   From **Motors & Motion**, drag `set servo angle [targetAngle]`.
                    *   **Snap** inside (instant jump).
    *   **Update Current Position**:
        *   From **Variables**, drag `set [currentAngle] to [targetAngle]`.
            *   **Snap** below.
    *   **Toggle Target** (for next cycle):
        *   From **Logic**, drag `if [targetAngle] = [180] then`.
            *   **Snap** below.
            *   Then: `set [targetAngle] to [0]`.
            *   Else: `set [targetAngle] to [180]`.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below (pause between movements).

### 9️⃣ Execution Flow (Plain English)

Servo alternates between 0° and 180° every cycle. If button is released, servo jumps instantly (fast mode). If button is held, servo sweeps smoothly over 5 seconds, moving 1° at a time with 28ms delays. This demonstrates velocity control: same distance, different speeds. Useful for gentler handling, dramatic effects, or avoiding sudden jerks that could damage fragile payloads.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
servo = machine.PWM(machine.Pin(12))
servo.freq(50)

def set_servo_angle(angle):
    duty = int(1640 + (angle / 180) * 4914)
    servo.duty_u16(duty)

currentAngle = 0
targetAngle = 180

while True:
    buttonHeld = button.value()
    
    if buttonHeld:
        # Slow motion (5 second sweep)
        step = 1 if targetAngle > currentAngle else -1
        for angle in range(currentAngle, targetAngle + step, step):
            set_servo_angle(angle)
            time.sleep(0.028)
    else:
        # Fast motion (instant)
        set_servo_angle(targetAngle)
    
    currentAngle = targetAngle
    
    # Toggle target
    targetAngle = 0 if targetAngle == 180 else 180
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Slow Motion Too Fast**: Increase delay from 0.028s to 0.05s for 9-second sweep.
*   **Servo Buzzing**: Some servos can't handle 1° increments. Use 2° or 5° steps for smoother operation.
*   **Button Doesn't Work**: Verify PULL_DOWN and that button connects to GND when pressed.

### 1️⃣2️⃣ Try This Next

*   **Potentiometer Speed**: Replace button with pot to control speed continuously (0.01s to 0.1s per degree).
*   **Acceleration**: Add ramp-up/ramp-down so motion starts slow, accelerates to peak, then decelerates.
*   **Path Recording**: Record button presses and play back the exact slow/fast pattern.

---

[Continuing with final 5 projects... 0356-0360]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_7_projects)

print("✅ Projects 0354-0355 appended")
print("⏳ Final 5 projects remaining (0356-0360)...")
print("   Will complete Pass 2 in next generation block!")
