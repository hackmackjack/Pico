
# BATCH 15: Smart Fan 1 (Projects 0141-0150)

## Project 0141: Introduction to Smart Fan

### 1. Learning Objective
Learn the fundamentals of motor actuation using a Raspberry Pi Pico. Understand how to control a high-current device like a fan motor through a driver module by toggling a digital output pin.

### 2. Concepts Introduced
*   **Motor Actuation**: Using electrical signals to create mechanical movement.
*   **Motor Drivers**: Understanding why motors need a driver module (they draw more current than the Pico can provide directly).
*   **Digital Control**: Using HIGH and LOW signals to start and stop a device.

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor (5V or 12V)
*   Motor Driver Module (e.g., L298N, MOS module, or Transistor circuit)
*   External Power Source (appropriate for the fan)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Driver IN** | GP15 | Controls fan state |
| **Motor Driver VCC** | External | Power source for the fan |
| **Motor Driver GND** | GND | Common ground with Pico |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: This project uses direct pin control.

### 7. Step-by-Step Guide

**A. Setup Phase**
1.  **Initialize Fan Pin**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 as OUTPUT -> LOW.

**B. Control Phase**
2.  **Create Main Loop**:
    *   From **Loops**, drag `pico_forever` and snap it below setup.
3.  **Turn Fan ON**:
    *   Inside the loop, from **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> HIGH.
4.  **Wait for Observation**:
    *   From **Time**, drag `pico_wait` -> 3 seconds.
5.  **Turn Fan OFF**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> LOW.
6.  **Wait for Stop**:
    *   From **Time**, drag `pico_wait` -> 3 seconds.

### 8. Execution Flow
1.  **Start**: The Pico initializes GP15 to LOW, ensuring the fan is stopped.
2.  **Loop**: The program enters an infinite loop.
3.  **Active**: GP15 goes HIGH, the driver sends power to the motor, and the fan spins.
4.  **Pause**: The fan runs for 3 seconds.
5.  **Idle**: GP15 goes LOW, the driver cuts power, and the fan slows to a stop.
6.  **Pause**: The fan remains off for 3 seconds before repeating.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure the pin connected to the motor driver
fan_pin = Pin(15, Pin.OUT)

while True:
    # Set the pin HIGH to spin the fan
    fan_pin.value(1)
    print("Fan ON")
    time.sleep(3)
    
    # Set the pin LOW to stop the fan
    fan_pin.value(0)
    print("Fan OFF")
    time.sleep(3)
```

### 10. Common Mistakes
*   **Wiring Directly to Pico**: Never connect a motor directly to the Pico pins; it will draw too much current and damage the board.
*   **Shared Ground**: Forgetting to connect the external power's GND to the Pico's GND will prevent the control signal from working.
*   **Driver Polarity**: Check the motor driver datasheet to ensure you are using the correct input pins.

### 11. Try This Next
*   **Change Timing**: Reduce the wait times to 1 second to see how fast the motor can react.
*   **Manual Trigger**: Add a button to turn the fan on only when pressed.

---

## Project 0142: Blinking Smart Fan

### 1. Learning Objective
Apply timing sequences to mechanical hardware. Learn how to simulate environmental effects like "Wind Gusts" by alternating motor states at different intervals.

### 2. Concepts Introduced
*   **Asymmetric Timing**: Using different durations for the "ON" and "OFF" states.
*   **Simulation**: Using simple logic to mimic complex natural phenomena (like a breeze).
*   **Mechanical Latency**: Observing how it takes time for a motor to reach full speed and come to a stop.

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor
*   Motor Driver Module
*   External Power Source
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0141)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: This project uses direct pin control.

### 7. Step-by-Step Guide

**A. Control Phase**
1.  **Create Main Structure**:
    *   From **Loops**, drag `pico_forever`.
2.  **Trigger the Gust (ON)**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> HIGH.
3.  **Hold Gust Duration**:
    *   From **Time**, drag `pico_wait` -> 2 seconds.
4.  **Trigger the Calm (OFF)**:
    *   From **Smart IO**, drag `pico_gpio_write`.
    *   **Set** GP15 -> LOW.
5.  **Hold Calm Duration**:
    *   From **Time**, drag `pico_wait` -> 5 seconds.

### 8. Execution Flow
1.  **Loop**: The fan activates for a short "gust" of 2 seconds.
2.  **Silence**: The fan deactivated for a longer "calm" period of 5 seconds.
3.  **Result**: The intermittent airflow simulates a natural breeze rather than a constant industrial fan.

### 9. Generated Code
```python
from machine import Pin
import time

# Configure the fan control pin
fan = Pin(15, Pin.OUT)

while True:
    # Gust phase
    fan.value(1)
    print("Gust blowing...")
    time.sleep(2)
    
    # Calm phase
    fan.value(0)
    print("Quiet air...")
    time.sleep(5)
```

### 10. Common Mistakes
*   **Short Gusts**: If the gust is too short (e.g., 0.2s), the motor might not even have time to start spinning meaningfully.
*   **Wrong Intervals**: Ensure the "ON" time is shorter than the "OFF" time to properly simulate a gusty day.

### 11. Try This Next
*   **Randomized Winds**: Use a math block to set the wait times to a random value between 1 and 10 seconds.
*   **Variable Gust Strength**: If using a PWM driver, try setting different speeds for different gusts.

---

## Project 0143: Manual Smart Fan Control

### 1. Learning Objective
Learn the fundamentals of Pulse Width Modulation (PWM) for speed control. Understand how to use a physical slide switch to select between different speed presets.

### 2. Concepts Introduced
*   **PWM (Pulse Width Modulation)**: Rapidly toggling a pin to simulate different voltage levels and control motor speed.
*   **Switch States**: Reading a multi-state input to drive logic.
*   **Duty Cycle**: The percentage of time a signal is "ON" (0% = OFF, 100% = Full Speed).

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor
*   PWM-capable Motor Driver (like MOSFET or L298N)
*   Slide Switch (or 2-position toggle)
*   10k Ohm pull-down resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Switch Pin 1 (LOW)** | GP14 | Connect with pull-down |
| **Switch Pin 2 (HIGH)** | GP13 | Connect with pull-down |
| **Fan PWM IN** | GP15 | Must be a PWM-capable pin |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty)
*   **from Logic, drag `controls_if`** (if/else if/else)

### 6. Variables
*   **speed_mode**: Stores the value read from the switch.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup PWM**:
    *   From **Smart IO**, drag `pico_pwm_write`.
    *   **Set** GP15 duty to 0.

**B. Monitoring Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Detect Switch Position**:
    *   From **Logic**, drag `controls_if` with an **else if** extension.
    *   **Condition 1**: If `pico_gpio_read` GP14 is HIGH (Left position).
    *   **Condition 2**: If `pico_gpio_read` GP13 is HIGH (Right position).

**C. Control Phase**
4.  **Set Low Speed**:
    *   Inside the first **If**:
    *   From **Smart IO**, drag `pico_pwm_write`. **Set** GP15 duty to 300 (roughly 30%).
5.  **Set High Speed**:
    *   Inside the **Else If**:
    *   From **Smart IO**, drag `pico_pwm_write`. **Set** GP15 duty to 1023 (100%).
6.  **Set Off State**:
    *   Inside the **Else** (center or disconnected position):
    *   **Set** GP15 duty to 0.

### 8. Execution Flow
1.  **Monitor**: The Pico checks which button/pin on the slide switch is active.
2.  **Low Mode**: If the left pin is HIGH, the Pico sends a 30% power signal (quick pulses) to the fan.
3.  **High Mode**: If the right pin is HIGH, the Pico sends a continuous 100% power signal.
4.  **Idle**: If no pin is HIGH, the PWM is shut off, and the fan stops.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

# Configure PWM for fan
fan_pwm = PWM(Pin(15))
fan_pwm.freq(1000)

# Configure switch inputs
sw_low = Pin(14, Pin.IN, Pin.PULL_DOWN)
sw_high = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    if sw_low.value() == 1:
        # 30% Duty Cycle (Approx 19660 out of 65535 in MicroPython)
        fan_pwm.duty_u16(19660)
        print("Mode: LOW SPEED")
    elif sw_high.value() == 1:
        # 100% Duty Cycle
        fan_pwm.duty_u16(65535)
        print("Mode: HIGH SPEED")
    else:
        # Off
        fan_pwm.duty_u16(0)
        
    time.sleep(0.1)
```

### 10. Common Mistakes
*   **PWM Frequency**: If the frequency is too low, you might hear a "whine" from the motor. Keep it around 1000Hz.
*   **Duty Cycle Range**: Different libraries use different ranges (0-255, 0-1023, or 0-65535). Ensure your values match the expected range for your block.

### 11. Try This Next
*   **3-Speed Fan**: Add a third switch pin or a button system to include a "Medium" (60%) setting.
*   **Visual Speed**: Add a different color LED for each speed mode.

---

## Project 0144: Smart Fan Sequences

### 1. Learning Objective
Explore advanced PWM automation. Learn how to create a "Ramped Acceleration" sequence by programmatically incrementing the motor speed over time.

### 2. Concepts Introduced
*   **Acceleration Ramping**: Smoothly increasing power to avoid mechanical stress and simulate powerful engine startup.
*   **For Loops**: Using iterative logic to change a value in sequence.
*   **Linear Interpolation**: Moving from Point A (0%) to Point B (100%) through intermediate steps.

### 3. Hardware Required
*   Raspberry Pi Pico
*   DC Fan Motor
*   PWM Motor Driver
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
*(Same as Project 0143)*

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (count up)
*   **from Smart IO, drag `pico_pwm_write`** (set PWM duty)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **speed**: The current PWM value during the ramp-up.

### 7. Step-by-Step Guide

**A. Startup Phase**
1.  **Initialize**: Start a `pico_forever` loop.

**B. Ramp-Up Phase**
2.  **Create Sequence**:
    *   From **Loops**, drag the `controls_repeat_ext` block (Count with `speed` from 0 to 1023).
3.  **Apply Speed**:
    *   Inside the for loop, drag `pico_pwm_write`.
    *   **Set** GP15 duty to the variable `speed`.
4.  **Set Ramp Timing**:
    *   From **Time**, drag `pico_wait` -> 0.01 seconds. (This defines how smooth/slow the ramp is).

**C. Full Speed Phase**
5.  **Hold Power**:
    *   Snap a `pico_wait` -> 5 seconds below the for loop (to enjoy the full speed).

**D. Shutdown Phase**
6.  **Cut Power**:
    *   From **Smart IO**, drag `pico_pwm_write`. **Set** GP15 duty to 0.
7.  **Reset Interval**:
    *   Snap a `pico_wait` -> 2 seconds before the loop starts again.

### 8. Execution Flow
1.  **Increment**: The variable `speed` starts at 0 and adds 1 in every tiny step.
2.  **Update**: The fan receives slightly more power every 10 milliseconds.
3.  **Acceleration**: To the observer, the fan sounds like it is "winding up" smoothly over several seconds.
4.  **Cooldown**: Once full speed is reached, it runs for a while and then stops to repeat.

### 9. Generated Code
```python
from machine import Pin, PWM
import time

fan = PWM(Pin(15))
fan.freq(1000)

while True:
    print("Spinning up...")
    # Ramp from 0 to 65535 (standard 16-bit PWM in MicroPython)
    for speed in range(0, 65536, 500):
        fan.duty_u16(speed)
        time.sleep(0.05)
        
    print("Full Speed reached!")
    time.sleep(5)
    
    fan.duty_u16(0)
    print("Shutting down")
    time.sleep(2)
```

### 10. Common Mistakes
*   **Ramping Too Fast**: If the delay is too small (e.g., 0.001s), the ramp will be so fast it sounds like a normal ON signal.
*   **Step Size**: If you increment by 1 each time up to 65535, it will take a long time. Use a larger 'step' (like +500) for faster ramping.

### 11. Try This Next
*   **Ramp Down**: Create a second for loop below the first one that counts down from 1023 to 0 for a smooth stop.
*   **Interactive Ramp**: Only start the spin-up sequence when a button is pressed.

---

## Project 0145: Interactive Smart Fan

### 1. Learning Objective
Explore audio-based control (Biometrics/Environment). Learn how to use a sound sensor as a digital toggle switch to turn a mechanical device ON and OFF.

### 2. Concepts Introduced
*   **Sound Sensing**: Using a microphone module to detect sharp audio peaks (claps).
*   **Toggling Logic**: Changing a state (Boolean) from ON to OFF every time a trigger occurs.
*   **Sensory Input vs. Command**: Translating a sudden noise into a persistent action.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor Module (KY-038 or similar with Digital Output)
*   DC Fan Motor + Driver
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sound Sensor DO** | GP14 | Responds to noise |
| **Fan Control IN** | GP15 | Turns motor on/off |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **fan_state**: A True/False value representing if the fan should be running.
*   **noise_detected**: Stores the current signal from the sound sensor.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize State**:
    *   From **Variables**, **Set** `fan_state` = False.
    *   **Set** GP15 -> LOW.

**B. Detection Phase**
2.  **Monitor the Mic**:
    *   From **Loops**, drag `pico_forever`.
    *   **Set** `noise_detected` = **Smart IO** `pico_gpio_read` GP14.

**C. Toggle Phase**
3.  **Detect Clap**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `noise_detected` == HIGH.
4.  **Flip the Switch**:
    *   Inside the If:
    *   From **Variables**, **Set** `fan_state` = **Logic** `not` `fan_state`.
5.  **Prevent Double-Triggers**:
    *   From **Time**, drag `pico_wait` -> 0.5 seconds. (Crucial to prevent the echo from being seen as a second clap).

**D. Action Phase**
6.  **Drive Fan**:
    *   Snap a `pico_gpio_write` GP15.
    *   **Set** value to the variable `fan_state`.

### 8. Execution Flow
1.  **Listen**: The microphone waits for a sharp sound.
2.  **Trigger**: When you clap, GP14 pulses HIGH.
3.  **Calculate**: The Pico sees `fan_state` is currently False, so it flips it to True.
4.  **Actuate**: GP15 turns on the fan.
5.  **Repeat**: If you clap again, it flips back to False, and the fan stops.

### 9. Generated Code
```python
from machine import Pin
import time

# Hardware setup
mic = Pin(14, Pin.IN)
fan = Pin(15, Pin.OUT)

# System state
fan_on = False

while True:
    if mic.value() == 1:
        # Toggle state
        fan_on = not fan_on
        print("Clap detected! Fan State: " + str(fan_on))
        
        # Actuate
        fan.value(fan_on)
        
        # Debounce/Cooldown delay
        time.sleep(0.5)
        
    time.sleep(0.01)
```

### 10. Common Mistakes
*   **No Cooldown**: If you don't use the 0.5s wait after a clap, the motor's own startup noise or the clap's echo will immediately toggle the fan back off.
*   **Sensitivity**: Many sound sensors have a small potentiometer on them. If it doesn't work, turn the screw until the sensor's LED only flashes when you make noise.

### 11. Try This Next
*   **2-Clap Command**: Update the logic to only toggle if it hears TWO claps within a second.
*   **Sound-Activated Timer**: Make the fan turn on for 30 seconds when it hears a noise, then turn off automatically.

---
