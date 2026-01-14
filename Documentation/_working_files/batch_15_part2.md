
## Project 0146: Smart Smart Fan Switch

### 1. Learning Objective
Combine environmental monitoring with mechanical output. Learn how to implement a thermostat system where a "Target" temperature dictates the operational state of a fan.

### 2. Concepts Introduced
*   **Thermostatic Control**: Automating a cooling device based on ambient temperature.
*   **Setpoint/Target**: Using a variable to define the desired environmental state.
*   **Closed-Loop Logic (Simplified)**: A system that responds to changes in the data it is monitoring.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Internal or External Temperature Sensor (e.g. DHT11 or Internal ADC4)
*   DC Fan Motor + Driver
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Temp Sensor** | Internal / GP16 | Reads room temperature |
| **Fan Control** | GP15 | Turns on/off based on heat |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (if/else)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **target_temp**: The threshold above which the fan starts (25.0).
*   **current_temp**: Live reading from the sensor.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Target**:
    *   From **Variables**, **Set** `target_temp` = 25.0.

**B. Monitoring Phase**
2.  **Start Main Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Read Living Data**:
    *   From **Variables**, **Set** `current_temp` = **Sensors** `pico_read_temp`.

**C. Control Logic Phase**
4.  **Compare and Actuate**:
    *   From **Logic**, drag a `controls_if` block with an **else** slot.
    *   **Condition**: If `current_temp` > `target_temp`.
5.  **Cooling (ON)**:
    *   Inside the If:
    *   From **Smart IO**, **Set** GP15 (Fan) -> HIGH.
    *   From **Text**, **Print** "Too Hot! Fan ON".
6.  **Resting (OFF)**:
    *   Inside the Else:
    *   From **Smart IO**, **Set** GP15 (Fan) -> LOW.
    *   From **Text**, **Print** "Comfortable. Fan OFF".

7.  **Add Delay**:
    *   From **Time**, **Wait** 1 second to prevent the motor from rapid toggling at the boundary.

### 8. Execution Flow
1.  **Sense**: The Pico checks the room temperature.
2.  **Logic**: If the air is 26C (Above the 25C target), the fan starts spinning.
3.  **Result**: If the room is already cool (e.g., 22C), the fan stays off to save power.
4.  **Feedback**: The console displays the decision for the user.

### 9. Generated Code
```python
from machine import Pin, ADC
import time

fan = Pin(15, Pin.OUT)
sensor = ADC(4)
conv = 3.3 / 65535

# User preference
target_temp = 25.0

while True:
    read = sensor.read_u16() * conv
    current_temp = 27 - (read - 0.706) / 0.001721
    
    if current_temp > target_temp:
        fan.value(1)
        print("Cooling... Current: " + str(current_temp))
    else:
        fan.value(0)
        print("Idle. Current: " + str(current_temp))
        
    time.sleep(1)
```

### 10. Common Mistakes
*   **Single Threshold**: Using only one number for ON/OFF will cause the fan to flicker every second if the temp stays exactly at 25.0C.
*   **Wrong Operator**: Ensure you use `>` (Greater Than) and not `<`. A fan should turn on when it is HOT.

### 11. Try This Next
*   **User Adjustable Target**: Add two buttons (Temp+ and Temp-) to change the `target_temp` while the program is running.
*   **Variable Speed Cooling**: Use PWM to make the fan spin FASTER the hotter it gets beyond the target.

---

## Project 0147: Smart Fan Alarm System

### 1. Learning Objective
Learn about mechanical safety and protection logic. Understand how to implement "Jam Detection" using a simulated feedback signal to protect a motor from burning out when it is obstructed.

### 2. Concepts Introduced
*   **Fault Detection**: identifying when a physical system is not behaving as intended.
*   **Emergency Shutdown**: Immediately cutting power to prevent hardware damage.
*   **State Conflict Logic**: Reacting to a scenario where an output is "HIGH" but an error signal is also "HIGH".

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor + Driver
*   1 Button (Simulating a "Stall/Jam" sensor)
*   1 Red LED (Fault indicator)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Error Button** | GP14 | Press to simulate a jam |
| **Fault LED** | GP13 | Lights up on error |
| **Fan Pin** | GP15 | Normal control pin |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Variables, drag `variables_set`** (set variable to)

### 6. Variables
*   **system_fault**: A Boolean that locks the system down once an error occurs.
*   **jam_detected**: Reading from the simulated sensor switch.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize Pins**:
    *   **Set** GP15 (Fan) and GP13 (Error LED) to LOW.
2.  **Clear Faults**:
    *   From **Variables**, **Set** `system_fault` = False.

**B. Alarm Phase**
3.  **Monitor Jam Sensor**:
    *   From **Loops**, drag `pico_forever`.
    *   Inside: **Set** `jam_detected` = **Smart IO** `pico_gpio_read` GP14.
4.  **Detect Conflict**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `jam_detected` == HIGH (Simulating the fan being stuck).
5.  **Shutdown Sequence**:
    *   Inside the If:
    *   From **Variables**, **Set** `system_fault` = True.
    *   From **Smart IO**, **Set** GP15 (Fan) -> LOW (Safety Cutoff).
    *   From **Smart IO**, **Set** GP13 (LED) -> HIGH (Visual Alarm).

**C. Normal Operation Phase**
6.  **Check for Healthy State**:
    *   Add another `controls_if`.
    *   **Condition**: If `system_fault` == False.
    *   **Inside**: **Set** GP15 -> HIGH (Normal operation).

### 8. Execution Flow
1.  **Normal**: The fan spins because `system_fault` is False.
2.  **Trigger**: You press the button (Simulating a rock in the fan blades).
3.  **Protect**: The Pico immediately cuts power to the motor and turns on the Red LED.
4.  **Lock**: Even if you let go of the button, the fan stays OFF until you reset the program. This protects the motor from restarting while still jammed.

### 9. Generated Code
```python
from machine import Pin
import time

fan = Pin(15, Pin.OUT)
error_led = Pin(13, Pin.OUT)
jam_sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)

system_active = True

while True:
    if jam_sensor.value() == 1:
        # Emergency Shutdown
        system_active = False
        fan.value(0)
        error_led.value(1)
        print("ERROR: FAN JAMMED! SHUTTING DOWN FOR SAFETY.")
        
    if system_active:
        # Normal running
        fan.value(1)
        error_led.value(0)
    
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **Auto-Restart**: If you don't use a "lock" variable like `system_fault`, the fan will start spinning the moment the button is released, which is dangerous if the jam hasn't been cleared.
*   **Logic Order**: Ensure the shutdown logic can override the "Running" logic.

### 11. Try This Next
*   **Manual Reset**: Add a second button that purely "Resets" the `system_fault` back to False once the user has cleared the jam.
*   **Buzzer Alarm**: Add a buzzer that beeps an SOS pattern during the fault state.

---

## Project 0148: The Smart Fan Game

### 1. Learning Objective
Explore fluid dynamics and manual precision control. Learn how to use a Potentiometer to vary PWM duty cycles to achieve a specific physical result (balancing an object in the air).

### 2. Concepts Introduced
*   **Analog Manipulation**: Mapping a potentiometer's 0-1023 range directly to motor thrust.
*   **Equilibrium**: finding the exact power level where the force of air equals the force of gravity.
*   **Bernoulli Principle (Simple)**: Understanding how moving air can hold a ball in place.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Potentiometer (10k Ohm)
*   High-Speed DC Fan (Powerful enough to lift a ping pong ball)
*   PWM Motor Driver
*   Ping Pong Ball or lightweight Styrofoam ball
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Potentiometer OUT** | GP26 (ADC0) | Changes the speed |
| **Fan PWM IN** | GP15 | Controls the thrust |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty)
*   **from Math, drag `math_map`** (convert range)

### 6. Variables
*   **control_val**: The raw reading from the knob.
*   **fan_speed**: The calculated thrust level.

### 7. Step-by-Step Guide

**A. Monitoring Phase**
1.  **Read the Knob**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `control_val` = **Sensors** `pico_analog_read` GP26.

**B. Calculation Phase**
2.  **Scale the Input**:
    *   From **Math**, drag `math_map`.
    *   **Calculate**: Map `control_val` from [0-1023] to [300-1023] (We start at 30% because the fan won't spin below that).
    *   **Set** `fan_speed` to this result.

**C. Output Phase**
3.  **Drive the Fan**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   **Set** GP15 duty to `fan_speed`.

**D. Game Interaction**
4.  **Find the Balance**:
    *   Place the ball over the fan.
    *   Turn the knob slowly to see the ball rise and fall.
    *   **Goal**: Try to keep the ball floating exactly 5cm above the fan and hold it there for 10 seconds.

### 8. Execution Flow
1.  **Input**: User turns the potentiometer.
2.  **Translate**: The Pico converts the physical position of the knob into a digital power level.
3.  **Adjust**: The fan speed changes in real-time.
4.  **Physics**: The upward force of air creates a pocket of pressure that suspends the ball in mid-air.

### 9. Generated Code
```python
import machine
import utime

# Setup Potentiometer and Fan
pot = machine.ADC(26)
fan = machine.PWM(machine.Pin(15))
fan.freq(1000)

print("Game: Hover Ball! Balance the ball in the air.")

while True:
    # Read knob (0-65535 in MicroPython ADC)
    raw_val = pot.read_u16()
    
    # Map to 30%-100% duty cycle
    # Lower than 20000 often doesn't have enough torque to lift anything
    out_val = int((raw_val / 65535) * (65535 - 20000) + 20000)
    
    fan.duty_u16(out_val)
    
    # Fast updates for smooth control
    utime.sleep(0.01)
```

### 10. Common Mistakes
*   **Weak Fan**: A standard PC fan might only lift a tiny scrap of paper. Ensure your fan and power supply can handle the weight of the ball.
*   **Static Initial Value**: If you map from 0, the fan will hum but stay still until you turn the knob significantly. Start your mapping at the fan's "Spin Threshold".

### 11. Try This Next
*   **Distance Sensor**: Add an Ultrasonic sensor. Use logic to automatically adjust the fan speed to keep the ball at exactly 10cm without the user touching the knob (Automation!).

---

## Project 0149: Automated Smart Fan

### 1. Learning Objective
Orchestrate multi-motor interaction. Learn how to combine a Servo motor (Positional control) with a DC Fan motor (Velocity control) to create a complex "Oscillating Fan" system.

### 2. Concepts Introduced
*   **Dual-Axis Motion**: One motor provides function (Spin), while the other provides coverage (Sweep).
*   **Servo Control**: Using PWM pulses to set a specific angle (0-180 degrees).
*   **Asynchronous-like behavior**: Keeping the fan spinning at a constant speed while the servo moves in steps.

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor + Driver
*   Servo Motor (SG90 or similar)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Fan Pin** | GP15 | Spining the blades |
| **Servo Pin** | GP14 | Sweeping the neck |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (count up/down)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Actuators, drag `pico_servo_write`** (set servo angle)

### 6. Variables
*   **angle**: The current position of the fan's "neck".

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start the Fan**:
    *   From **Smart IO**, **Set** GP15 -> HIGH (Fan ON).

**B. Sweep Phase (0 to 180)**
2.  **Pan Right**:
    *   From **Loops**, drag `controls_repeat_ext`. **Set** `angle` from 0 to 180.
3.  **Move Servo**:
    *   Inside: from **Actuators**, **Set** GP14 angle to `angle`.
    *   From **Time**, **Wait** 0.02 seconds (Slow smooth sweep).

**C. Sweep Phase (180 to 0)**
4.  **Pan Left**:
    *   From **Loops**, drag a second `controls_repeat_ext`. **Set** `angle` from 180 down to 0.
5.  **Move Servo**:
    *   Inside: from **Actuators**, **Set** GP14 angle to `angle`.
    *   **Wait** 0.02 seconds.

### 8. Execution Flow
1.  **Start**: The fan begins spinning immediately.
2.  **Right**: The servo turns slowly from the far left to the far right.
3.  **Left**: The servo reverses and sweeps back.
4.  **Loop**: The fan provides a continuous "washing" effect of air across the room.

### 9. Generated Code
```python
import machine
import utime

# Hardware Setup
fan = machine.Pin(15, machine.Pin.OUT)
servo = machine.PWM(machine.Pin(14))
servo.freq(50)

# Function to set angle easily
def set_servo_angle(angle):
    duty = int(((angle / 180) * 2 + 0.5) / 20 * 65535)
    servo.duty_u16(duty)

fan.value(1) # Fan ON

while True:
    # Sweep 0 to 180
    for pos in range(0, 181, 2):
        set_servo_angle(pos)
        utime.sleep(0.05)
        
    # Sweep 180 to 0
    for pos in range(180, -1, -2):
        set_servo_angle(pos)
        utime.sleep(0.05)
```

### 10. Common Mistakes
*   **Power Loading**: Running a Servo and a powerful Fan from the Pico's USB power can cause the board to reboot. Always use an external 5V supply for the motors.
*   **Sweep Speed**: If you don't include a `wait` in the loops, the fan will whip left and right instantly, which could damage the servo gears.

### 11. Try This Next
*   **Paused Sweep**: Add a 1-second delay at exactly 0, 90, and 180 degrees.
*   **Selectable Oscillation**: Add a button to "Lock" the fan at its current angle (turn off the oscillation but keep the spin).

---

## Project 0150: Mastering Smart Fan

### 1. Learning Objective
Explore Proportional Control (Introduction to PID logic). Learn how to map a temperature range to a variable speed range, creating a fan that "thinks" and adjusts its power precisely based on the need.

### 2. Concepts Introduced
*   **Proportional Speed Control**: The output is mathematically "Proportional" to the input error or value.
*   **Slope Calculation**: Determining how much to change speed for every 1 degree of temperature change.
*   **Dynamic Efficiency**: Saving power and reducing noise by only running the fan as fast as necessary.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Internal or External Temp Sensor
*   PWM Motor Driver + Fan Motor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0146 - Thermostat)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty)
*   **from Math, drag `math_map`** (linear scaling)
*   **from Variables, drag `variables_set`** (set variable to)

### 6. Variables
*   **t**: Live temperature.
*   **s**: Calculated speed (Duty Cycle).

### 7. Step-by-Step Guide

**A. Monitoring Phase**
1.  **Sample Environment**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `t` = **Sensors** `pico_read_temp`.

**B. Brain Phase (The Math)**
2.  **Calculate Effort**:
    *   If `t` < 25: **Set** `s` = 0 (Total stop).
    *   If `t` > 35: **Set** `s` = 1023 (100% blast).
    *   If `t` is BETWEEN 25 and 35:
        *   From **Math**, drag `math_map`.
        *   **Apply**: Map `t` from [25 to 35] into [200 to 1023]. (This creates the smooth ramp).

**C. Drive Phase**
3.  **Update Output**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   **Set** GP15 duty to the variable `s`.
4.  **Log Data**:
    *   From **Text**, **Print** "Temp: ", `t`, " | Power: ", `s`.

### 8. Execution Flow
1.  **Idle**: At 24C, the fan is silent and still.
2.  **Start**: At 26C, the fan spins very slowly and quietly.
3.  **React**: At 30C, the fan is at roughly 50% power, providing moderate cooling.
4.  **Critical**: At 36C, the fan is roaring at maximum speed to combat the heat.

### 9. Generated Code
```python
import machine
import utime

# Setup
sensor = machine.ADC(4)
fan = machine.PWM(machine.Pin(15))
fan.freq(1000)
c_factor = 3.3 / 65535

while True:
    # Read Temp
    reading = sensor.read_u16() * c_factor
    t = 27 - (reading - 0.706) / 0.001721
    
    # Logic: 25-35C maps to 0-65535 duty
    if t < 25:
        speed = 0
    elif t > 35:
        speed = 65535
    else:
        # Linear Proportion
        speed = int((t - 25) / (35 - 25) * 65535)
        
    fan.duty_u16(speed)
    print(f"Room: {t:.2f}C | Fan Power: {(speed/65535)*100:.1f}%")
    
    utime.sleep(1)
```

### 10. Common Mistakes
*   **Linear Start**: Fans usually need a "kickstart" (e.g. at least 20-30% duty) to overcome friction. If your mapping starts at 0, the fan might just hum without spinning until it hits 28C.
*   **Update Frequency**: Don't update the PWM value 1000 times a second if the temperature only changes every few minutes. 1Hz (once per second) is plenty.

### 11. Try This Next
*   **Exponential Ramp**: Change the math so the fan speed grows much faster as it gets closer to 35C (Square the result before mapping).
*   **Averaging**: Read the temperature 5 times and use the *average* value to make the fan speed changes even smoother.

---
