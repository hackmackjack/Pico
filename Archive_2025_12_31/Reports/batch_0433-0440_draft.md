# Projects 0433-0440: Simple Motors Batch - Full Elite Standard v2.0 Documentation

## Project 0433: Manual Simple Motors Control

### 1. Project Info
**Title**: Manual Simple Motors Control  
**Category**: Motors & Motion  
**Difficulty**: 3

### 2. Learning Objective
Implement smooth analog motor speed control using slide potentiometer. You will learn about PWM duty cycle mapping and linear motor control.

### 3. Concepts Introduced
*   **PWM Slider**: Potentiometer provides 0-100% speed control
*   **Linear Control**: Smooth analog input to motor speed mapping
*   **Variable Speed**: Continuous adjustment from stop to full power

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **Slide Potentiometer**
*   **DC Motor**
*   **Motor Driver** (L293D)

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Slide Pot** | GP26 (ADC0) | Speed input |
| **Motor Enable (PWM)** | GP15 | Speed control |
| **Motor IN1** | GP16 | Direction |
| **Motor IN2** | GP17 | Direction |

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`** (read pot position)
*   **from Math, drag `map_range`** (pot to PWM duty)
*   **from Smart IO, drag `pico_pwm_write`** (control motor speed)

### 7. Variables
*   **potValue**: ADC reading (0-65535)
*   **motorSpeed**: Mapped PWM duty cycle (0-100%)

### 8. Step-by-Step Guide

**A. Initialization**
*   From **Smart IO**, configure GP26 as ADC input
*   From **Smart IO**, configure GP15 as PWM, GP16/17 as OUTPUT
*   From **Smart IO**, set direction (IN1=HIGH, IN2=LOW for forward)

**B. Main Loop**
*   From **Smart IO**, read analog value from GP26
*   From **Math**, map value [0-65535] to [0-100]% duty cycle  
*   From **Smart IO**, set PWM duty on GP15 to mapped value
*   From **Time**, wait 0.05 seconds

### 9. Execution Flow
Left position (0V) = motor stopped. Middle position = 50% speed. Right position (3.3V) = full speed. Smooth linear response allows precise control.

### 10. Generated Code
```python
import machine
import time

pot = machine.ADC(26)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)
in1 = machine.Pin(16, machine.Pin.OUT, value=1)
in2 = machine.Pin(17, machine.Pin.OUT, value=0)

while True:
    pot_val = pot.read_u16()
    duty = pot_val  # Direct mapping
    pwm.duty_u16(duty)
    time.sleep(0.05)
```

### 11. Common Mistakes
*   **Motor doesn't move**: Check motor driver wiring and power supply
*   **Jerky motion**: Add small capacitor across pot for noise filtering

### 12. Try This Next
*   **Reverse**: Add button to toggle direction (swap IN1/IN2)
*   **Dead Zone**: Ignore values <10% to prevent stalling

---

## Project 0434: Simple Motors Sequences

### 1. Project Info
**Title**: Simple Motors Sequences  
**Category**: Motors & Motion

### 2. Learning Objective
Create automated shaking motion using servo oscillation for laboratory mixing applications.

### 3. Concepts Introduced
*   **Servo Oscillation**: Rapid back-and-forth movement
*   **Agitation Logic**: Mechanical mixing through motion
*   **Position Sequencing**: Alternating between two angles

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **Servo Motor** (SG90 or similar)

### 5. Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Servo Signal** | GP15 | PWM control |
| **Servo Power** | VBUS (5V) | External power recommended |

### 6. Blocks Used
*   **from Smart IO, drag `servo_write`** (set angle)
*   **from Loops, drag `pico_repeat`** (10 oscillations)
*   **from Time, drag `pico_wait`** (position hold time)

### 7. Variables
*   **shakeCycles**: 10 repetitions
*   **angleA**: +45 degrees
*   **angleB**: -45 degrees

### 8. Step-by-Step Guide

**A. Initialization**
*   From **Smart IO**, configure GP15 for servo control

**B. Main Loop**
*   From **Loops**, repeat 10 times:
    *   From **Smart IO**, move servo to +45°
    *   From **Time**, wait 0.2 seconds
    *   From **Smart IO**, move servo to -45°
    *   From **Time**, wait 0.2 seconds
*   From **Smart IO**, return to 0° (center)

### 9. Execution Flow
Servo rapidly alternates between +45° and -45° ten times (creates shaking motion), then returns to center. Total shake time: 4 seconds.

### 10. Generated Code
```python
import machine
import time

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def set_angle(angle):
    # Convert angle (-90 to +90) to duty cycle
    duty = int((angle + 90) / 180 * 5000 + 2500)
    servo.duty_u16(duty)

for _ in range(10):
    set_angle(45)
    time.sleep(0.2)
    set_angle(-45)
    time.sleep(0.2)

set_angle(0)
```

### 11. Common Mistakes
*   **Servo jitters**: Ensure stable power supply (use external 5V)
*   **Limited range**: Calibrate duty cycle values for your specific servo

### 12. Try This Next
*   **Variable speed**: Increase wait time every cycle (slow down)
*   **Random shake**: Use random angles instead of fixed ±45°

---

[Projects 0435-0440 continue in same format...]

**SUMMARY**: Generated complete Elite Standard documentation for Projects 0433-0434.  
**Remaining in batch**: Projects 0435-0440 (6 more to generate)
**Total in batch**: 8 projects
