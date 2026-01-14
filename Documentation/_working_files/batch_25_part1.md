
# BATCH 25: Traffic Lights 2 (Projects 0241-0250)

## 1. Project 0241: Introduction to Traffic Lights

### 2. Learning Objective
Explore safety-critical initialization (The All-Red Start). Learn why industrial systems must enter a "Known Safe State" upon power-up before beginning their operational loops, ensuring no conflicting signals are active during start-up.

### 3. Concepts Introduced
*   **Safety Interlocks**: preventing overlapping Green states in an intersection.
*   **Boot Sequences**: logic that runs only once before entering the `forever` loop.
*   **State Conflict Management**: ensuring that if power is lost, the system resets to "Stop" (Red) for all directions.

### 4. Hardware Required
*   Raspberry Pi Pico
*   4 Red LEDs (representing North, South, East, West)
*   4 resistors
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **North Red** | GP15 | Safety group A |
| **South Red** | GP14 | Safety group A |
| **East Red** | GP13 | Safety group B |
| **West Red** | GP12 | Safety group B |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (safety duration)

### 7. Variables
*   **None**: this is a linear startup routine.

### 8. Step-by-Step Guide

**A. Safety Start Phase (Setup)**
1.  **Impose Red State**:
    *   **Set** GP15 -> HIGH.
    *   **Set** GP14 -> HIGH.
    *   **Set** GP13 -> HIGH.
    *   **Set** GP12 -> HIGH.
2.  **Wait for Stabilization**:
    *   From **Time**, **Wait** 3 seconds.
    *   **Print** "Initialization Complete. Intersection Secure.".

**B. Operational Phase (Loop)**
3.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
4.  **Simulate Operation**: (For this intro, just show that the lights are active).
    *   **Set** GP15/GP14 -> LOW (allowing North/South to proceed).
    *   **Wait** 2s.
    *   **Return** to Red.

### 9. Execution Flow
1.  **Boot**: The moment the Pico gets power, all 4 Red LEDs light up instantly.
2.  **Dwell**: The Pico waits for 3 seconds. This ensures that any cars in the intersection from a previous power-cut have time to clear or notice the new signal.
3.  **Active**: Only after the 3 seconds does the code enter the cycle to let cars through.
4.  **Result**: A professional-grade fail-safe start sequence.

### 10. Generated Code
```python
from machine import Pin
import time

# Defining the 4 Red LEDs
north_r = Pin(15, Pin.OUT)
south_r = Pin(14, Pin.OUT)
east_r = Pin(13, Pin.OUT)
west_r = Pin(12, Pin.OUT)

# --- SAFETY STARTUP ---
print("SYSTEM START: SECURING INTERSECTION")
north_r.value(1); south_r.value(1); east_r.value(1); west_r.value(1)
time.sleep(3) # Ensure all traffic stops
print("SYSTEM OPERATIONAL")

while True:
    # Example cycle start
    north_r.value(0); south_r.value(0) # N/S Go
    time.sleep(5)
    
    north_r.value(1); south_r.value(1) # N/S Stop
    time.sleep(5)
```

### 11. Common Mistakes
*   **Starting with Green**: If you put the "Green" command at the very top of your code, you might cause an accident if the power flickers while cars are already crossing.
*   **Pin Floating**: Always use `pico_gpio_write` to explicitly set the start state.

### 12. Try This Next
*   **Buzzer Chirp**: play a short beep at the end of the 3-second safety window to signal the intersection is now live.
*   **Master Switch**: add a physical switch that forces the system back into "All Red" mode at any time.

---

## 1. Project 0242: Blinking Traffic Lights

### 2. Learning Objective
Explore preemption overrides (The Emergency Flash). Learn how to implement an interrupt-style button that instantly halts the normal traffic sequence and forces a high-visibility warning state (Blinking Red) to allow emergency vehicles to pass safely.

### 3. Concepts Introduced
*   **Priority Preemption**: using an input sensor to cancel low-priority tasks (Regular Traffic) for high-priority ones (Ambulance).
*   **Warning Patterns**: using 0.2s blinks to signal "Caution" or "Stop".
*   **Global Overrides**: logic that affects every LED in the system simultaneously.

### 4. Hardware Required
*   Raspberry Pi Pico
*   3 Traffic LEDs (Red, Yellow, Green)
*   1 Emergency Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Traffic Red** | GP15 | Primary stop signal |
| **Emergency Btn** | GP14 | Siren detection trigger |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking for siren)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (blink rate)

### 7. Variables
*   **None**: this is a momentary override.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Detect Emergency**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Button** GP14 is Pressed.

**B. Override Phase (Flashing Red)**
3.  **Active Siren**:
    *   Inside the **If** block:
    *   **Set** GP15 -> HIGH. **Wait** 0.2s.
    *   **Set** GP15 -> LOW. **Wait** 0.2s.
    *   **Print** "EMERGENCY VEHICLE DETECTED - CLEARING ROAD".

**C. Normal Operation Phase**
4.  **No Siren**:
    *   Inside the **Else** block:
    *   Place your standard traffic light logic (Green/Yellow/Red).

### 9. Execution Flow
1.  **Normal**: The light is Green. Cars are moving.
2.  **Emergency**: you press the button.
3.  **Reaction**: The Green light immediately shuts off. The Red light starts flashing very fast.
4.  **Safety**: All cars stop because of the flashing red. The ambulance passes.
5.  **Recovery**: you release the button. The Pico resumes the normal Green/Yellow cycle.
6.  **Result**: A dynamic traffic system that reacts to life-saving events in real-time.

### 10. Generated Code
```python
from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(13, Pin.OUT)
siren_btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if siren_btn.value() == 1:
        # Emergency Flash
        green.value(0)
        red.value(1); time.sleep(0.2)
        red.value(0); time.sleep(0.2)
    else:
        # Simplified Normal Loop
        green.value(1); red.value(0); time.sleep(2)
        green.value(0); red.value(1); time.sleep(2)
```

### 11. Common Mistakes
*   **Slow Polling**: if your normal loop has a `wait 10 seconds` block, the Pico won't see the emergency button until the 10 seconds are over! To fix this, use a loop that checks the button every 0.01 seconds.

### 12. Try This Next
*   **Two-Way Flash**: make the Yellow light flash instead of the Red to signal a less urgent warning.
*   **Buzzer Siren**: add a buzzer that beeps at the same time the light flashes.

---

## 1. Project 0243: Manual Traffic Lights Control

### 2. Learning Objective
Explore remote flagging (The Construction Switch). Learn how to link a physical toggle switch directly to specific signal states, allowing a human operator to manually manage traffic flow around a temporary obstacle.

### 3. Concepts Introduced
*   **Manual Override**: removing autonomic timing in favor of human judgment.
*   **Binary States**: mapping a 2-position switch (Left vs. Right) to a 2-aspect light (Red vs. Green).
*   **Real-time Response**: instantaneous light changes with zero programmed delay.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Slide Switch
*   1 Red LED + 1 Green LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Slide Switch** | GP14 | Left = Go, Right = Stop |
| **Go (Green)** | GP15 | Construction Clear |
| **Stop (Red)** | GP13 | Construction Blocked |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating switch)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)

### 7. Variables
*   **None**: this is a direct input-to-output mapping.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Evaluate Toggle**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).

**B. "Go" Logic**
3.  **Active State (Green)**:
    *   Inside the **If** block:
    *   **Set** Green (GP15) -> HIGH.
    *   **Set** Red (GP13) -> LOW.
    *   **Print** "FLAGGER: GREEN - PROCEED".

**C. "Stop" Logic**
4.  **Inactive State (Red)**:
    *   Inside the **Else** block:
    *   **Set** Green (GP15) -> LOW.
    *   **Set** Red (GP13) -> HIGH.
    *   **Print** "FLAGGER: RED - STOP".

### 9. Execution Flow
1.  **Read**: The Pico checks the physical position of the switch.
2.  **Decision**: if the switch is sending 3.3V to GP14, the first block runs.
3.  **Action**: The Green LED lights up.
4.  **Control**: The human flagger sees a car coming they want to stop, and slides the switch the other way.
5.  **Result**: The Green light disappears and the Red light appears instantly, stopping the traffic.

### 10. Generated Code
```python
from machine import Pin
import time

sw = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_g = Pin(15, Pin.OUT)
led_r = Pin(13, Pin.OUT)

while True:
    if sw.value() == 1:
        # Construction Go
        led_g.value(1)
        led_r.value(0)
    else:
        # Construction Stop
        led_g.value(0)
        led_r.value(1)
        
    time.sleep(0.05) # Fast response for flagger
```

### 11. Common Mistakes
*   **Yellow Light**: In manual construction flagging, there is often no Yellow light. This can be dangerous for fast cars! To fix this, use a 3-position switch to include a Yellow warning state.
*   **Inverted Wiring**: ensuring the "Go" side of the switch actually turns on the Green LED.

### 12. Try This Next
*   **Two-Way Flagging**: give TWO people switches. The Red light only turns OFF if BOTH people say the road is clear (Project 0213).

---

## 1. Project 0244: Traffic Lights Sequences

### 2. Learning Objective
Explore temporal phase insertion (The Turn Arrow). Learn how to modify a standard 3-state sequence to include a special "Priority Phase" (Blue LED) that acts as a protected left-turn signal before the main traffic group is allowed to move.

### 3. Concepts Introduced
*   **Phase Logic**: dividing a cycle into sub-segments (Turn phase vs. Straight phase).
*   **Extended Sequences**: moving from 3 states to 4 or 5 states.
*   **Protected Movement**: giving one group of cars priority before the rest.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Red, Yellow, Green LEDs
*   1 Blue LED (Turn Arrow)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Stop (Red)** | GP15 | State 1 |
| **Go (Green)** | GP14 | State 3 |
| **Caution (Yellow)** | GP13 | State 4 |
| **Arrow (Blue)** | GP12 | State 2 (Protected Turn) |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (complex sequencing)
*   **from Time, drag `pico_wait`** (interval control)

### 7. Variables
*   **None**: this is a time-driven machine.

### 8. Step-by-Step Guide

**A. Phase 1 (Stop)**
1.  **Red State**: **Set** Red HIGH. All others LOW. **Wait** 3s.

**B. Phase 2 (Protected Turn)**
2.  **Arrow State**:
    *   **Keep** Red HIGH (to stop oncoming cars).
    *   **Set** Blue (Arrow) HIGH.
    *   **Wait** 3 seconds.
    *   **Set** Blue LOW.

**C. Phase 3 (Main Flow)**
3.  **Green State**:
    *   **Set** Red LOW.
    *   **Set** Green HIGH.
    *   **Wait** 5 seconds.

**D. Phase 4 (Caution)**
4.  **Yellow State**:
    *   **Set** Green LOW.
    *   **Set** Yellow HIGH.
    *   **Wait** 2 seconds.
5.  **Restart**: Sequence loops back to Red.

### 9. Execution Flow
1.  **Red**: Everyone waits.
2.  **Blue**: The Red light stays ON, but the Blue "Arrow" appears. Only the cars turning left can move.
3.  **Green**: The Blue arrow disappears and the Red light turns OFF. All cars can now go straight.
4.  **Yellow**: Warning period.
5.  **Result**: A professional traffic intersection that can handle turning lanes safely.

### 10. Generated Code
```python
from machine import Pin
import time

led_r = Pin(15, Pin.OUT)
led_g = Pin(14, Pin.OUT)
led_y = Pin(13, Pin.OUT)
led_b = Pin(12, Pin.OUT) # Arrow

while True:
    # 1. Stop
    print("NORTH: STOP")
    led_r.value(1); led_g.value(0); led_y.value(0); led_b.value(0)
    time.sleep(3)
    
    # 2. Turn Priority
    print("NORTH: LEFT TURN ONLY")
    led_b.value(1) # Keep Red ON for safety
    time.sleep(3)
    led_b.value(0)
    
    # 3. Main Green
    print("NORTH: GO STRAIGHT")
    led_r.value(0); led_g.value(1)
    time.sleep(5)
    
    # 4. Yellow
    print("NORTH: CAUTION")
    led_g.value(0); led_y.value(1)
    time.sleep(2)
```

### 11. Common Mistakes
*   **Turning off Red**: If you turn the Red LED off *while* the Blue Arrow is on, you might accidentally signal cars in other lanes that they can move too. Always double-check which lights stay on together.

### 12. Try This Next
*   **Flashing Arrow**: make the Blue LED flash for the last 1 second of its turn to warn drivers it's ending.
*   **Pedestrian Walk**: add a White LED that turns on only if a button is pressed (from Project 0192).

---

## 1. Project 0245: Interactive Traffic Lights

### 2. Learning Objective
Explore acoustic penalty logic (Noise Control). Learn how to use a Sound Sensor to detect excessive ambient noise (Honking) and implement a software "Penalty" where the traffic light stays Red for a longer duration to discourage noise pollution.

### 3. Concepts Introduced
*   **Threshold Detection**: triggering an event when sound volume exceeds a set level.
*   **Dynamic Wait Times**: Using an IF statement to choose between `wait 5s` and `wait 10s`.
*   **Feedback/Punishment Loop**: using software to influence human behavior.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor Module (Digital or Analog)
*   Traffic Lights (Red, Green)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Noise Sensor** | GP14 | Detects loud Volume |
| **Red Light** | GP15 | "Penalty" Indicator |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (storing penalty state)
*   **from Sensors, drag `pico_analog_read`** (read noise)
*   **from Logic, drag `controls_if`** (checking noise level)

### 7. Variables
*   **is_too_loud**: Boolean tracking current street noise.
*   **wait_time**: Number of seconds the Red light will stay on.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Monitor the Street**:
    *   **Set** `noise_level` = **Sensors** `pico_analog_read` GP14.

**B. Brain Phase (The Penalty)**
3.  **Define Normalcy**:
    *   From **Variables**, **Set** `wait_time` = 5.
4.  **Apply Penalty**:
    *   If `noise_level` > 80% (High volume):
        *   **Print** "TOO LOUD! EXTENDING RED LIGHT.".
        *   **Set** `wait_time` = 15.

**C. Execution Phase**
5.  **Perform Light Cycle**:
    *   **Set** Red (GP15) -> HIGH.
    *   **Wait** `wait_time` seconds.
    *   **Set** Green -> HIGH.
    *   **Wait** 5 seconds.

### 9. Execution Flow
1.  **Quiet Street**: The Pico sees low noise. It sets the timer to 5s. The intersection moves quickly.
2.  **Honk**: You blow a whistle near the sensor. The Pico detects the spike.
3.  **Reaction**: The code immediately overwrites the variable with "15".
4.  **Result**: The drivers are forced to wait three times longer as a "penalty" for being loud.
5.  **Outcome**: Smart city logic that manages environment through automated response.

### 10. Generated Code
```python
import machine
import utime

# Noise sensor and light
mic = machine.ADC(machine.Pin(26))
led_r = machine.Pin(15, machine.Pin.OUT)
led_g = machine.Pin(14, machine.Pin.OUT)

while True:
    # 1. Check for bad behavior
    noise = mic.read_u16()
    
    red_duration = 5 # Standard
    if noise > 40000: # Significant noise
        print("Noise detected! Applying 15s penalty.")
        red_duration = 15
        
    # 2. Execute
    led_r.value(1); led_g.value(0)
    utime.sleep(red_duration)
    
    led_r.value(0); led_g.value(1)
    utime.sleep(5)
```

### 11. Common Mistakes
*   **Sensitivity**: If your threshold is too low, the sound of a passing breeze might trigger the 15-second penalty. Always calibrate your "Loud" level first.
*   **Blocking Sleep**: If you check the noise only once at the start of the Red phase, you might miss a honk that happens 1 second later.

### 12. Try This Next
*   **Noise Count**: instead of one honk, make it so the penalty only applies if there are 3 honks in 5 seconds.
*   **Display Decibels**: print the raw noise value to the screen every second.

---
