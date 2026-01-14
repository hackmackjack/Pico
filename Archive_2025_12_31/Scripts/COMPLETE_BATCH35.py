# COMPLETE BATCH 35: Generate Projects 0347-0350
# Vibration Detect, Sail Boat Race, Timer Button, RPM Sync

print("Completing Batch 35 with Projects 0347-0350...")

projects_0347_0350 = '''
## 1️⃣ Project 0347: Smart Fan Alarm System

### 2️⃣ Learning Objective
Detect mechanical faults using accelerometer vibration sensing. You will learn fault detection and automatic system shutdown for safety.

### 3️⃣ Concepts Introduced
*   **Vibration Detection**: Using accelerometer to detect abnormal motion.
*   **Fault Detection**: Identifying mechanical failures before catastrophic damage.
*   **Automatic Shutdown**: Safe system termination on fault detection.

### 4️⃣ Hardware Required
*   **Pico**
*   **Accelerometer** (ADXL345 or MPU6050)
*   **DC Fan Motor**
*   **Motor Driver**
*   **Red LED**
*   **220Ω Resistor**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accelerometer SDA** | GP0 | I2C data |
| **Accelerometer SCL** | GP1 | I2C clock |
| **Motor Enable (PWM)** | GP14 | Fan control |
| **Red LED** | GP15 | Fault indicator via 220Ω |

### 6️⃣ Blocks Used

🔹 **Setup I2C & Accelerometer**
*   **Category:** Sensors/Communication

🔹 **Read Accelerometer**
*   **Category:** Sensors

🔹 **Setup PWM & Pin**
*   **Category:** Outputs

### 7️⃣ Variables & State
*   **accelX, accelY, accelZ**: Acceleration readings on 3 axes.
*   **vibrationLevel**: Calculated vibration magnitude.
*   **faultDetected**: System fault flag.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Sensors**, drag `Setup Accelerometer I2C:[0]`.
        *   **Snap** into setup block.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Outputs**, drag `Setup Pin:[15] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [faultDetected] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Read Accelerometer** (if not faulted):
        *   From **Logic**, drag `if not [faultDetected] then`.
            *   **Snap** into loop.
            *   Then:
                *   From **Sensors**, drag `read accelerometer`.
                    *   **Snap** inside.
                    *   Store X, Y, Z in respective variables.
                *   **Calculate Vibration Magnitude**:
                    *   From **Math**, drag `sqrt([accelX]² + [accelY]² + [accelZ]²)`.
                        *   **Snap** below.
                        *   Store in `vibrationLevel`.
    *   **Check Fault Condition**:
        *   From **Logic**, drag `if [vibrationLevel] > [20] then`.
            *   **Snap** below (threshold for abnormal vibration).
            *   Then:
                *   From **Variables**, drag `set [faultDetected] to [true]`.
                    *   **Snap** inside.
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[0]`.
                    *   **Snap** below (SHUTDOWN MOTOR).
                *   From **Pin Access**, drag `set Pin [15] to [HIGH]`.
                    *   **Snap** below (Red LED ON).
                *   From **Console**, drag `print [FAULT: High Vibration Detected! Motor Shutdown.]`.
                    *   **Snap** below.
    *   **Normal Operation**:
        *   From **Logic**, drag `if not [faultDetected] then`.
            *   **Snap** below.
            *   Then:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[49152]`.
                    *   **Snap** inside (75% speed normally).
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The fan runs at 75% speed while the accelerometer continuously monitors vibration. If the combined acceleration magnitude exceeds threshold (20 m/s² indicating unbalanced fan, loose mount, or bearing failure), the system immediately shuts down the motor, lights the red LED, and prints a fault message. The fault latches, requiring power cycle or reset. This prevents damaged fan from destroying itself or causing injury.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import math
from adxl345 import ADXL345  # Accelerometer library

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
accel = ADXL345(i2c)

fan = machine.PWM(machine.Pin(14))
fan.freq(1000)
redLED = machine.Pin(15, machine.Pin.OUT)

faultDetected = False

while True:
    if not faultDetected:
        x, y, z = accel.read()
        vibrationLevel = math.sqrt(x**2 + y**2 + z**2)
        
        if vibrationLevel > 20:
            faultDetected = True
            fan.duty_u16(0)
            redLED.high()
            print("FAULT: High Vibration Detected! Motor Shutdown.")
    
    if not faultDetected:
        fan.duty_u16(49152)
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **False Alarms**: If vibration threshold triggers during normal operation, increase threshold or average readings over 5 samples.
*   **Accelerometer Not Responding**: Verify I2C connections and address. Use I2C scan to confirm device presence.
*   **Can't Clear Fault**: Add reset button to clear `faultDetected` flag and allow restart after fixing mechanical issue.

### 1️⃣2️⃣ Try This Next

*   **Vibration Logging**: Record max vibration over time to track degradation.
*   **Graduated Response**: Reduce speed when vibration is moderate, shutdown only when severe.
*   **Frequency Analysis**: Use FFT to detect specific imbalance frequencies (e.g., 1x RPM = imbalance, 2x = misalignment).

---

## 1️⃣ Project 0348: The Smart Fan Game

### 2️⃣ Learning Objective
Create interactive wind propulsion game using servo-mounted fan. You will learn multi-actuator coordination and analog input mapping.

### 3️⃣ Concepts Introduced
*   **Multi-Actuator Control**: Coordinating motor and servo simultaneously.
*   **Analog-to-Servo Mapping**: Converting potentiometer position to servo angle.
*   **Wind Propulsion**: Using airflow as force for mechanical interaction.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Fan Motor**
*   **Servo Motor** (for fan direction)
*   **Potentiometer**
*   **Motor Driver**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer** | GP26 (ADC0) | Analog input for steering |
| **Servo** | GP12 | Fan direction control |
| **Motor Enable (PWM)** | GP14 | Fan speed |

### 6️⃣ Blocks Used

🔹 **Setup ADC**
*   **Category:** Inputs

🔹 **Setup Servo**
*   **Category:** Motors & Motion

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **Read Analog**
*   **Category:** Pin Access

🔹 **Servo Write Angle**
*   **Category:** Motors & Motion

### 7️⃣ Variables & State
*   **potValue**: Raw potentiometer reading (0-65535).
*   **servoAngle**: Calculated servo angle (0-180°).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup ADC pin:[26]`.
        *   **Snap** into setup block.
    *   From **Motors & Motion**, drag `Setup Servo pin:[12]`.
        *   **Snap** into setup block.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.

*   **B. Main Loop Phase**
    *   **Read Potentiometer (Steering)**:
        *   From **Pin Access**, drag `read analog pin [26]`.
            *   **Snap** into loop.
            *   Store in `potValue`.
    *   **Map to Servo Angle**:
        *   From **Math**, drag `map [potValue] from [0] to [65535] → [0] to [180]`.
            *   **Snap** below.
            *   Store in `servoAngle`.
    *   **Set Servo Direction**:
        *   From **Motors & Motion**, drag `set servo angle [servoAngle]`.
            *   **Snap** below.
    *   **Run Fan at Constant Speed**:
        *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[49152]`.
            *   **Snap** below (75% constant speed).
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below (50ms update).

### 9️⃣ Execution Flow (Plain English)

The fan runs at constant 75% speed while mounted on a servo. Player turns the potentiometer to steer the fan direction (0-180°). The goal is to aim airflow at a small boat in water trough to push it toward finish line. Left turn on pot aims fan left, right turn aims right. This teaches coordinated control where one actuator creates force (fan) and another directs it (servo).

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

pot = machine.ADC(26)
servo = machine.PWM(machine.Pin(12))
servo.freq(50)  # Standard servo frequency

fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

def set_servo_angle(angle):
    # Map 0-180° to servo duty cycle (1000-9000 for typical servos)
    duty = int(1000 + (angle / 180) * 8000)
    servo.duty_u16(duty)

while True:
    potValue = pot.read_u16()
    servoAngle = int(potValue * 180 / 65535)
    
    set_servo_angle(servoAngle)
    
    fan.duty_u16(49152)  # Constant fan speed
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Servo Jitters**: If servo shakes, add smoothing by averaging multiple pot readings or limiting angle change rate.
*   **Fan Overpowers Boat**: Reduce fan speed or increase distance. Game should require precise aiming, not brute force.
*   **Servo Range Wrong**: Calibrate servo min/max angles. Some servos use 500-2500μs pulse width instead of standard 1000-9000.

### 1️⃣2️⃣ Try This Next

*   **Speed Control**: Add second potentiometer for fan speed, giving player full wind control.
*   **Obstacle Course**: Add floating obstacles requiring precise navigation.
*   **Time Trial**: Track completion time, display on OLED screen.

---

## 1️⃣ Project 0349: Automated Smart Fan

### 2️⃣ Learning Objective
Implement add-on timer logic with multiple button presses extending runtime. You will learn accumulative timing and real-time duration tracking.

### 3️⃣ Concepts Introduced
*   **Add-On Timer**: Extending run time with additional inputs.
*   **Runtime Tracking**: Monitoring elapsed time during operation.
*   **Time Extension Logic**: Accumulating time from multiple triggers.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **DC Fan Motor**
*   **Motor Driver**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Timer add/start button, PULL_DOWN |
| **Motor Enable (PWM)** | GP14 | Fan control |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **Time Functions**
*   **Category:** Timing

🔹 **Digital Read**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **remainingTime**: Seconds left to run.
*   **lastButtonState**: For debouncing.
*   **running**: Fan operational state.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[10]`.
        *   **Snap** into setup block.
        *   Enable **PULL_DOWN** resistor.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Variables**, drag `set [remainingTime] to [0]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [running] to [false]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [lastButtonState] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check Button Press** (rising edge):
        *   From **Pin Access**, drag `digital read pin [10]`.
            *   **Snap** into loop.
            *   Store in `currentButtonState`.
        *   From **Logic**, drag `if ([currentButtonState] = HIGH) AND ([lastButtonState] = LOW) then`.
            *   **Snap** below.
            *   Then:
                *   From **Variables**, drag `change [remainingTime] by [60]`.
                    *   **Snap** inside (add 1 minute).
                *   From **Variables**, drag `set [running] to [true]`.
                    *   **Snap** below.
                *   From **Console**, drag `print [+1 minute added. Total: {remainingTime}s]`.
                    *   **Snap** below.
    *   **Update Button State**:
        *   From **Variables**, drag `set [lastButtonState] to [currentButtonState]`.
            *   **Snap** below.
    *   **Run Fan if Time Remaining**:
        *   From **Logic**, drag `if [running] AND ([remainingTime] > [0]) then`.
            *   **Snap** below.
            *   Then:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[65535]`.
                    *   **Snap** inside (fan ON).
                *   From **Variables**, drag `change [remainingTime] by [-1]`.
                    *   **Snap** below (decrement per second).
            *   Else:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[0]`.
                    *   **Snap** inside (fan OFF).
                *   From **Variables**, drag `set [running] to [false]`.
                    *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below (1Hz update).

### 9️⃣ Execution Flow (Plain English)

Press button to start fan with 1-minute timer. Each subsequent press during operation adds another minute. The fan runs continuously while time remains, decrementing every second. When time reaches zero, fan stops. For example: Press once = 60s. Press again at 40s remaining = 100s total (40+60). This mimics kitchen timers with add-time functionality.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

remainingTime = 0
running = False
lastButtonState = False

while True:
    currentButtonState = button.value()
    
    # Detect button press (rising edge)
    if currentButtonState and not lastButtonState:
        remainingTime += 60
        running = True
        print(f"+1 minute added. Total: {remainingTime}s")
    
    lastButtonState = currentButtonState
    
    # Fan control
    if running and remainingTime > 0:
        fan.duty_u16(65535)
        remainingTime -= 1
    else:
        fan.duty_u16(0)
        running = False
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Time Decrements Too Fast**: Ensure sleep is exactly 1 second. If processing takes time, use time tracking instead of simple sleep.
*   **Button Adds Time Even When OFF**: This is by design. To prevent, only add time if `running = True`.
*   **Countdown Not Visible**: Add OLED display showing remaining time in MM:SS format.

### 1️⃣2️⃣ Try This Next

*   **Countdown Display**: Show remaining time on 7-segment display or OLED.
*   **Variable Add-Time**: Long press adds 5 minutes instead of 1.
*   **Pause Feature**: Second button pauses/resumes without losing time.

---

## 1️⃣ Project 0350: Mastering Smart Fan

### 2️⃣ Learning Objective
Synchronize two motors using encoder feedback and PID control. You will learn closed-loop motor control and dual-motor coordination.

### 3️⃣ Concepts Introduced
*   **RPM Measurement**: Using encoders to measure rotation speed.
*   **Dual-Motor Synchronization**: Ensuring two motors run at identical speeds.
*   **Feedback Control**: Adjusting motor based on measured performance.

### 4️⃣ Hardware Required
*   **Pico**
*   **2× DC Fan Motors with Encoders**
*   **2× Motor Drivers**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fan A PWM** | GP14 | Speed control Motor A |
| **Fan B PWM** | GP15 | Speed control Motor B |
| **Encoder A** | GP16 | Interrupt for Fan A RPM |
| **Encoder B** | GP17 | Interrupt for Fan B RPM |

### 6️⃣ Blocks Used

🔹 **Setup PWM (×2)**
*   **Category:** Outputs

🔹 **Setup Interrupt Pins**
*   **Category:** Inputs

🔹 **PWM Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **countA, countB**: Encoder pulse counts.
*   **rpmA, rpmB**: Calculated RPM for each motor.
*   **speedA, speedB**: PWM duty cycles.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Outputs**, drag `Setup PWM pin:[15]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Inputs**, drag `Setup Interrupt pin:[16]` (Encoder A).
        *   **Snap** into setup block.
        *   Set trigger to **RISING** edge.
        *   Attach interrupt handler to increment `countA`.
    *   From **Inputs**, drag `Setup Interrupt pin:[17]` (Encoder B).
        *   **Snap** into setup block.
        *   Set trigger to **RISING** edge.
        *   Attach interrupt handler to increment `countB`.
    *   From **Variables**, drag `set [speedA] to [49152]`.
        *   **Snap** into setup block (start at 75%).
    *   From **Variables**, drag `set [speedB] to [49152]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Calculate RPM** (every 1 second):
        *   From **Math**, drag `[countA] * 60`.
            *   **Snap** into loop.
            *   Store in `rpmA` (assuming 1 pulse/rev, measured over 1s).
        *   From **Math**, drag `[countB] * 60`.
            *   **Snap** below.
            *   Store in `rpmB`.
        *   Reset counters: `countA = 0`, `countB = 0`.
    *   **Synchronization Logic**:
        *   From **Logic**, drag `if [rpmA] > [rpmB] then`.
            *   **Snap** below.
            *   Then: From **Variables**, drag `change [speedA] by [-328]`.
                *   **Snap** inside (slow down A by ~0.5%).
        *   From **Logic**, drag `else if [rpmA] < [rpmB] then`.
            *   **Snap** below.
            *   Then: From **Variables**, drag `change [speedB] by [-328]`.
                *   **Snap** inside (slow down B).
    *   **Apply Speeds**:
        *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[speedA]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `PWM Write pin:[15] freq:[1000] duty:[speedB]`.
            *   **Snap** below.
    *   From **Console**, drag `print [Motor A: {rpmA} RPM, Motor B: {rpmB} RPM]`.
        *   **Snap** below.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The system runs two fans and measures their RPM using encoders. Every second, it calculates each motor's speed and compares them. If Motor A is faster, it reduces A's PWM slightly. If B is faster, it reduces B's PWM. Over multiple iterations, this closes the speed gap, achieving synchronization. This is useful for dual-fan cooling systems, conveyor belts, or robotic drivetrains requiring matched speeds.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

# Motors
fanA = machine.PWM(machine.Pin(14))
fanB = machine.PWM(machine.Pin(15))
fanA.freq(1000)
fanB.freq(1000)

# Encoders
countA = 0
countB = 0

def encoder_a_handler(pin):
    global countA
    countA += 1

def encoder_b_handler(pin):
    global countB
    countB += 1

encoderA = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
encoderB = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
encoderA.irq(trigger=machine.Pin.IRQ_RISING, handler=encoder_a_handler)
encoderB.irq(trigger=machine.Pin.IRQ_RISING, handler=encoder_b_handler)

speedA = 49152
speedB = 49152

while True:
    # Calculate RPM
    rpmA = countA * 60
    rpmB = countB * 60
    countA = 0
    countB = 0
    
    # Sync logic
    if rpmA > rpmB:
        speedA -= 328
    elif rpmA < rpmB:
        speedB -= 328
    
    # Apply speeds
    fanA.duty_u16(speedA)
    fanB.duty_u16(speedB)
    
    print(f"Motor A: {rpmA} RPM, Motor B: {rpmB} RPM")
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Encoders Not Counting**: Verify interrupt setup and wiring. Use LED to visually confirm encoder pulses.
*   **Diverging Speeds**: If motors drift apart instead of sync, increase correction factor (change 328 to 656).
*   **Oscillation**: If speeds oscillate around target, reduce correction factor for smoother convergence.

### 1️⃣2️⃣ Try This Next

*   **PID Control**: Implement proper PID (Proportional-Integral-Derivative) for faster, stable sync.
*   **Target RPM**: Allow user to set desired RPM via potentiometer, sync both motors to that target.
*   **Load Compensation**: Vary load on one motor (add resistance), verify system compensates automatically.

---

'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(projects_0347_0350)

print("✅ BATCH 35 COMPLETE! Projects 0347-0350 appended")
print("🎉 Smart Fan 2 (Batch 35) fully generated: Projects 0341-0350")
print("")
print("📊 Progress Update:")
print("   Completed: 50/60 projects (Pass 2)")
print("   Remaining: 10 projects (Batch 36: Robotic Arm 2, Projects 0351-0360)")
print("")
print("✅ Ready to generate Batch 36 to complete Pass 2!")
