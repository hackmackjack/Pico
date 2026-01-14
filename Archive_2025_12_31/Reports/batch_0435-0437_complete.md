# Projects 0435-0440 Completion - Elite Standard v2.0

## Project 0435: Interactive Simple Motors

### 1. Project Info
**Title**: Interactive Simple Motors (Temp Fan)
**Category**: Sensors & Motors

### 2. Learning Objective
Implement temperature-based fan speed control with curve logic. You will learn about piecewise linear mapping and thermal management automation.

### 3. Concepts Introduced
*   **Thermal Control**: Fan speed follows temperature curve
*   **Piecewise Mapping**: Different behaviors in different ranges
*   **Cooling Automation**: Self-regulating thermal system

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **Temperature Sensor** (DHT22 or DS18B20)
*   **DC Fan**
*   **Motor Driver** or Transistor

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | GP2 | Digital input |
| **Fan PWM** | GP15 | Speed control |

### 6. Blocks Used
*   **from Sensors, drag `read_temperature`** (get current temp)
*   **from Logic, drag `if_compare`** (range detection)
*   **from Math, drag `map_range`** (temp to speed)
*   **from Smart IO, drag `pico_pwm_write`** (control fan)

### 7. Variables
*   **temperature**: Current temp in Celsius
*   **fanSpeed**: PWM duty cycle (0-100%)

### 8. Step-by-Step Guide

**A. Initialization**
*   From **Sensors**, configure temp sensor on GP2
*   From **Smart IO**, configure GP15 as PWM output

**B. Main Loop**
*   From **Sensors**, read temperature value
*   From **Logic**, check temperature range:
    *   If temp < 25°C: set fanSpeed = 0% (off)
    *   Else if 25°C ≤ temp ≤ 30°C: map [25-30] to [0-100]%
    *   Else (temp > 30°C): set fanSpeed = 100% (max)
*   From **Smart IO**, apply fanSpeed to PWM
*   From **Time**, wait 2 seconds

### 9. Execution Flow
Below 25°C, fan is off. Between 25-30°C, fan speed increases linearly (each degree adds 20% speed). Above 30°C, fan runs at maximum. System automatically adjusts cooling based on thermal load.

### 10. Generated Code
```python
import machine
import time

# Simplified temp reading (replace with actual sensor)
def read_temp():
    return 27  # Example

fan = machine.PWM(machine.Pin(15))
fan.freq(25000)

while True:
    temp = read_temp()
    
    if temp < 25:
        fan_speed = 0
    elif temp <= 30:
        fan_speed = int((temp - 25) / 5 * 100)
    else:
        fan_speed = 100
    
    duty = int(fan_speed / 100 * 65535)
    fan.duty_u16(duty)
    time.sleep(2)
```

### 11. Common Mistakes
*   **Fan always off**: Check temp sensor calibration
*   **Too aggressive**: Widen temperature range (20-35°C) for smoother curve

### 12. Try This Next
*   **Hysteresis**: Add 2°C dead band to prevent rapid on/off cycling
*   **PID Control**: Implement proportional-integral-derivative for precise temp regulation

---

## Project 0436: Smart Simple Motors Switch

### 1. Project Info
**Title**: Smart Simple Motors Switch (Remote Stop)
**Category**: Safety & Automation

### 2. Learning Objective
Implement emergency motor kill switch with remote control capability. You will learn about safety-critical interrupt systems.

### 3. Concepts Introduced
*   **Remote Kill Switch**: Instant power cutoff via wireless command
*   **Emergency Stop**: Safety-critical fast response
*   **Fail-Safe Design**: Default to stopped state

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **IR Receiver** or Button
*   **DC Motor**
*   **Motor Driver**

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stop Button** | GP14 | PULL_DOWN, emergency input |
| **Motor Enable** | GP15 | PWM control |
| **Motor IN1/IN2** | GP16/17 | Direction |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read stop button)
*   **from Logic, drag `if_compare`** (emergency detection)
*   **from Smart IO, drag `pico_pwm_write`** (motor control)
*   **from Variables, drag `set_variable`** (track safety state)

### 7. Variables
*   **motorActive**: Boolean motor state
*   **emergencyStop**: Boolean stop flag

### 8. Step-by-Step Guide

**A. Initialization**
*   From **Smart IO**, configure GP14 as input (PULL_DOWN)
*   From **Smart IO**, configure GP15-17 for motor control
*   From **Variables**, set motorActive = True (running)

**B. Main Loop**
*   From **Smart IO**, read stop button state
*   From **Logic**, if button pressed:
    *   Set emergencyStop = True
    *   Set motorActive = False
    *   From **Smart IO**, set PWM to 0 (instant stop)
*   Else if not stopped:
    *   From **Smart IO**, normal motor operation

### 9. Execution Flow
Motor runs normally until stop button pressed. Button press immediately cuts power (within one loop cycle, <50ms). Once stopped, motor stays off until manual reset/restart.

### 10. Generated Code
```python
import machine
import time

stop_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor_pwm = machine.PWM(machine.Pin(15))
motor_pwm.freq(1000)

motor_active = True

while True:
    if stop_btn.value() == 1:
        motor_active = False
        motor_pwm.duty_u16(0)
        print("EMERGENCY STOP!")
    elif motor_active:
        motor_pwm.duty_u16(32768)  # 50% speed
    
    time.sleep(0.01)  # Fast response
```

### 11. Common Mistakes
*   **Slow response**: Use short delay (<50ms) for safety
*   **No visual feedback**: Add LED to indicate stopped state

### 12. Try This Next
*   **Wireless**: Use IR receiver for remote emergency stop
*   **Dual redundancy**: Require two independent stop signals for extra safety

---

## Project 0437: Simple Motors Alarm System

### 1. Project Info
**Title**: Simple Motors Alarm System (Door Lock)
**Category**: Safety & Automation

### 2. Learning Objective
Create electronic deadbolt using servo with password protection. You will learn about electromechanical security and authentication.

### 3. Concepts Introduced
*   **Servo Deadbolt**: Physical locking mechanism
*   **Password Protection**: Authentication before unlock
*   **Lock States**: Secure (90°) vs Open (0°)

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **Servo Motor**
*   **2 Buttons** (Lock, Unlock)
*   **Keypad** (optional for password)

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo** | GP15 | Lock actuator |
| **Lock Button** | GP14 | Immediate lock |
| **Unlock Button** | GP13 | Requires password |

### 6. Blocks Used
*   **from Smart IO, drag `servo_write`** (move deadbolt)
*   **from Smart IO, drag `pico_gpio_read`** (read buttons)
*   **from Variables, drag `set_variable`** (password check)
*   **from Logic, drag `if_compare`** (authentication)

### 7. Variables
*   **isLocked**: Boolean lock state
*   **password**: Stored PIN code
*   **userInput**: Entered code

### 8. Step-by-Step Guide

**A. Initialization**
*   From **Smart IO**, configure servo on GP15
*   From **Variables**, set password = "1234"
*   From **Variables**, set isLocked = False

**B. Main Loop**
*   **Lock Action**:
    *   If Lock button pressed:
        *   From **Smart IO**, move servo to 90° (locked)
        *   Set isLocked = True
*   **Unlock Action**:
    *   If Unlock button pressed:
        *   Prompt for password (via serial/keypad)
        *   From **Logic**, if userInput == password:
            *   From **Smart IO**, move servo to 0° (unlocked)
            *   Set isLocked = False

### 9. Execution Flow
Anyone can lock (press button → servo rotates to 90°). To unlock requires correct password entry, then servo returns to 0°. Provides basic electronic security.

### 10. Generated Code
```python
import machine
import time

servo = machine.PWM(machine.Pin(15))
servo.freq(50)
lock_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
unlock_btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

password = "1234"
is_locked = False

def set_angle(angle):
    duty = int((angle / 180) * 5000 + 2500)
    servo.duty_u16(duty)

while True:
    if lock_btn.value() == 1:
        set_angle(90)
        is_locked = True
        print("LOCKED")
        time.sleep(0.5)
    
    if unlock_btn.value() == 1:
        user_input = input("Enter password: ")
        if user_input == password:
            set_angle(0)
            is_locked = False
            print("UNLOCKED")
        else:
            print("WRONG PASSWORD")
        time.sleep(0.5)
    
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Password in code**: Use encrypted storage in production
*   **No timeout**: Add auto-lock after 30 seconds for security

### 12. Try This Next
*   **RFID**: Replace password with card authentication
*   **Multi-factor**: Require card AND PIN code

---

[Projects 0438-0440 continue...]

**Generated**: Projects 0435-0437 complete (3/6 remaining in batch)
**Next**: Generate 0438 (Crane Game), 0439 (Auto-Level), 0440 (Stepper Motor)
