# Generate Projects 0344-0348 (Batch 35 continuation)
# Cleaning Cycle, Proximity Blow, Safety Guard, Vibration Detect, Sail Boat Race

print("Generating Projects 0344-0348...")

projects_0344_0348 = '''
## 1️⃣ Project 0344: Smart Fan Sequences

### 2️⃣ Learning Objective
Create automated maintenance routine with timed sequences and direction reversals. You will learn sequential automation and H-Bridge direction control for practical applications.

### 3️⃣ Concepts Introduced
*   **Automated Sequences**: Predefined action chains.
*   **Bidirectional Cleaning**: Using direction reversal for thorough maintenance.
*   **Pause States**: Incorporating delays between operations.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Fan Motor**
*   **H-Bridge** (L298N or similar)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **H-Bridge IN1** | GP14 | Direction control A |
| **H-Bridge IN2** | GP15 | Direction control B |
| **H-Bridge ENA** | GP13 | PWM Enable (speed) |

### 6️⃣ Blocks Used

🔹 **Setup PWM & Pin**
*   **Category:** Outputs

🔹 **Digital Write & PWM Write**
*   **Category:** Pin Access

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   None (predefined sequence).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[13]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Outputs**, drag `Setup Pin:[14] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Outputs**, drag `Setup Pin:[15] as OUTPUT`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Step 1: Blow Dust (Forward Full Speed)**:
        *   From **Pin Access**, drag `set Pin [14] to [HIGH]`.
            *   **Snap** into loop.
        *   From **Pin Access**, drag `set Pin [15] to [LOW]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[65535]`.
            *   **Snap** below (full speed).
        *   From **Timing**, drag `sleep [5] seconds`.
            *   **Snap** below.
    *   **Step 2: Stop (Settle)**:
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[0]`.
            *   **Snap** below (motor off).
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.
    *   **Step 3: Suck Dust (Reverse Full Speed)**:
        *   From **Pin Access**, drag `set Pin [14] to [LOW]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `set Pin [15] to [HIGH]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[65535]`.
            *   **Snap** below (full speed reverse).
        *   From **Timing**, drag `sleep [5] seconds`.
            *   **Snap** below.
    *   **Step 4: Off (Complete)**:
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[0]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [10] seconds`.
            *   **Snap** below (wait before next cycle).

### 9️⃣ Execution Flow (Plain English)

The automated cleaning cycle runs in 4 steps: (1) Blow air forward at full speed for 5 seconds to dislodge dust. (2) Stop motor for 1 second to let dust settle. (3) Reverse motor to suck dust backward for 5 seconds. (4) Turn off completely. After 10 seconds, the cycle repeats. This bidirectional approach is more thorough than single-direction cleaning, mimicking commercial air purifiers.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

ena = machine.PWM(machine.Pin(13))
in1 = machine.Pin(14, machine.Pin.OUT)
in2 = machine.Pin(15, machine.Pin.OUT)

ena.freq(1000)

while True:
    # Step 1: Blow dust (forward)
    in1.high()
    in2.low()
    ena.duty_u16(65535)
    time.sleep(5)
    
    # Step 2: Stop
    ena.duty_u16(0)
    time.sleep(1)
    
    # Step 3: Suck dust (reverse)
    in1.low()
    in2.high()
    ena.duty_u16(65535)
    time.sleep(5)
    
    # Step 4: Off
    ena.duty_u16(0)
    time.sleep(10)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Motor Doesn't Reverse**: Verify H-Bridge direction pins (IN1/IN2) are swapped correctly between forward and reverse.
*   **Insufficient Power**: Ensure external power supply can provide enough current for full-speed operation (often 1-2A).
*   **Immediate Direction Change**: Never reverse direction without stopping first. This can damage motor/H-Bridge. Always insert 0.5-1s delay.

### 1️⃣2️⃣ Try This Next

*   **Button-Activated**: Instead of continuous loop, run cleaning cycle only when button pressed.
*   **Progressive Speed**: Ramp speed up/down gradually instead of instant full speed for smoother operation.
*   **Dustiness Sensor**: Use particulate sensor to trigger cleaning only when dust levels exceed threshold.

---

## 1️⃣ Project 0345: Interactive Smart Fan

### 2️⃣ Learning Objective
Create reactive force application using proximity sensing. You will learn sensor-actuator coupling and distance-based control logic.

### 3️⃣ Concepts Introduced
*   **Proximity Detection**: Using ultrasonic sensors for distance measurement.
*   **Reactive Control**: Actuator responds to sensor input.
*   **Threshold-Based Logic**: Binary decision from continuous sensor data.

### 4️⃣ Hardware Required
*   **Pico**
*   **Ultrasonic Sensor** (HC-SR04)
*   **DC Fan Motor**
*   **Motor Driver**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Ultrasonic TRIG** | GP16 | Trigger signal |
| **Ultrasonic ECHO** | GP17 | Echo response |
| **Motor Enable (PWM)** | GP14 | Fan control |

### 6️⃣ Blocks Used

🔹 **Setup Ultrasonic Sensor**
*   **Category:** Sensors

🔹 **Read Distance**
*   **Category:** Sensors

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **PWM Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **distance**: Measured distance in cm.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Sensors**, drag `Setup Ultrasonic TRIG:[16] ECHO:[17]`.
        *   **Snap** into setup block.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.

*   **B. Main Loop Phase**
    *   **Measure Distance**:
        *   From **Sensors**, drag `read ultrasonic distance`.
            *   **Snap** into loop.
            *   Store in `distance`.
    *   **React to Proximity**:
        *   From **Logic**, drag `if [distance] < [10] then`.
            *   **Snap** below.
            *   Then:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[65535]`.
                    *   **Snap** inside (fan ON - blow object away).
            *   Else:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[0]`.
                    *   **Snap** inside (fan OFF).
    *   From **Timing**, drag `sleep [0.1] seconds`.
        *   **Snap** below (100ms update rate).

### 9️⃣ Execution Flow (Plain English)

The ultrasonic sensor continuously measures distance. When an object comes within 10cm, the fan activates at full speed to blow it away. When the object moves back beyond 10cm, the fan turns off. This creates a reactive "force field" effect useful for hands-free object manipulation, touchless interfaces, or keeping workspace clear.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

# Ultrasonic sensor
trig = machine.Pin(16, machine.Pin.OUT)
echo = machine.Pin(17, machine.Pin.IN)

# Fan motor
fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

def read_distance():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = pulse_duration * 0.0343 / 2
    return distance

while True:
    distance = read_distance()
    
    if distance < 10:
        fan.duty_u16(65535)  # Blow away
    else:
        fan.duty_u16(0)  # Off
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Erratic Readings**: Ultrasonic sensors can glitch. Add averaging over 3-5 readings or ignore values >400cm (likely errors).
*   **Fan Doesn't Turn On**: Verify distance threshold (10cm). Print distance values to console to debug sensor readings.
*   **Fan Oscillates**: If object hovers at exactly 10cm, add hysteresis: turn ON at <10cm, turn OFF at >12cm.

### 1️⃣2️⃣ Try This Next

*   **Variable Speed**: Map distance (5-30cm) to fan speed (0-100%) for proportional response.
*   **Directional Blowing**: Use servo to aim fan toward detected object.
*   **Multi-Zone**: Multiple ultrasonic sensors create wider detection area.

---

## 1️⃣ Project 0346: Smart Smart Fan Switch

### 2️⃣ Learning Objective
Implement emergency stop safety system using touch sensing. You will learn safety-critical interrupt handling and fail-safe motor control.

### 3️⃣ Concepts Introduced
*   **Emergency Stop**: Immediate motor shutdown on safety trigger.
*   **Touch Sensing**: Capacitive or simple button-based contact detection.
*   **Safety Interrupt**: Highest-priority safety override.

### 4️⃣ Hardware Required
*   **Pico**
*   **Touch Sensor** (or button simulating touch)
*   **DC Fan Motor**
*   **Motor Driver**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Touch Sensor** | GP10 | Safety interrupt input, PULL_DOWN |
| **Motor Enable (PWM)** | GP14 | Fan control |

### 6️⃣ Blocks Used

🔹 **Setup Button**
*   **Category:** Inputs

🔹 **Setup PWM**
*   **Category:** Outputs

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **PWM Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **emergencyStop**: Safety flag indicating stop condition.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Inputs**, drag `Setup Button pin:[10]`.
        *   **Snap** into setup block.
        *   Enable **PULL_DOWN** resistor.
    *   From **Outputs**, drag `Setup PWM pin:[14]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Variables**, drag `set [emergencyStop] to [false]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Check Touch Sensor (Highest Priority)**:
        *   From **Pin Access**, drag `digital read pin [10]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [touch sensor] = HIGH then`.
            *   **Snap** below.
            *   Then:
                *   From **Variables**, drag `set [emergencyStop] to [true]`.
                    *   **Snap** inside.
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[0]`.
                    *   **Snap** below (IMMEDIATE STOP).
                *   From **Console**, drag `print [EMERGENCY STOP - Touch Detected!]`.
                    *   **Snap** below.
    *   **Normal Operation** (if not emergency):
        *   From **Logic**, drag `if not [emergencyStop] then`.
            *   **Snap** below.
            *   Then:
                *   From **Pin Access**, drag `PWM Write pin:[14] freq:[1000] duty:[49152]`.
                    *   **Snap** inside (fan runs at 75% normally).
    *   From **Timing**, drag `sleep [0.05] seconds`.
        *   **Snap** below (fast polling for safety).

### 9️⃣ Execution Flow (Plain English)

The fan runs at 75% speed during normal operation. Every 50ms, the system checks the touch sensor. If touched (simulating hand on fan cage), an emergency stop flag triggers immediately, motor shuts down, and an alert prints. The flag remains set, keeping the motor off until system reset. This demonstrates safety-first design where human contact always takes priority over operation.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

touchSensor = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
fan = machine.PWM(machine.Pin(14))
fan.freq(1000)

emergencyStop = False

while True:
    # Safety check (highest priority)
    if touchSensor.value():
        emergencyStop = True
        fan.duty_u16(0)
        print("EMERGENCY STOP - Touch Detected!")
    
    # Normal operation
    if not emergencyStop:
        fan.duty_u16(49152)  # 75% speed
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Emergency Stop Doesn't Work**: Verify touch sensor wiring and PULL_DOWN resistor. Sensor should read LOW when not touched, HIGH when touched.
*   **Can't Restart After Stop**: Current design latches emergency stop. To reset, add button to clear `emergencyStop` flag or power cycle.
*   **False Triggers**: If sensor is too sensitive, add debouncing or require touch for >100ms before triggering.

### 1️⃣2️⃣ Try This Next

*   **Reset Button**: Add separate button to clear emergency stop and resume operation.
*   **LED Indicators**: Green LED during normal operation, red LED during emergency stop.
*   **Gradual Stop**: Instead of instant off, ramp speed down over 1 second for smoother emergency stop.

---

[Continuing with 0347-0348...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(projects_0344_0348)

print("✅ Projects 0344-0346 appended")
print("⏳ Remaining: Projects 0347-0360 (14 projects)")
print("   Current total: 46/60 projects complete")
