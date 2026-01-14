# 📘 Pico 2500: Batch 25 - Traffic Lights 2 (Projects 0241-0250)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Advanced Traffic Control Systems

---

## 1️⃣ Project 0241: Multi-State Traffic Light

### 2️⃣ Learning Objective
Implement a standard traffic light cycle (Red -> Green -> Yellow) using a state machine approach to manage timing and transitions accurately.

### 3️⃣ Concepts Introduced
*   Finite State Machines (FSM)
*   Transition States (Yellow)
*   Timing Sequences
*   Safety Delays
*   Visual Signaling Standards

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Red LED (GP15)
*   Yellow LED (GP16)
*   Green LED (GP17)
*   3× 220Ω Resistors
*   Breadboard & Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Connection |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Cathodes** | GND | Common Ground |

### 6️⃣ Blocks Used
🔹 **Digital Write** - LED Control
🔹 **Time Delay** - State Duration
🔹 **Functions** - State Definitions

### 7️⃣ Variables & State
*   **currentState**: String - "RED", "GREEN", "YELLOW"
*   **timer**: Number - Duration counter

### 8️⃣ Step-by-Step Guide
**A. Initialization Phase**
1. Configure GP15, 16, 17 as OUPUT
2. Turn all LEDs OFF initially
3. Define timing constants: RED_TIME=5s, GREEN_TIME=4s, YELLOW_TIME=2s

**B. Main Loop Phase**
1. **Red State:**
   - Turn RED ON (others OFF)
   - Wait 5 seconds
2. **Green State:**
   - Turn GREEN ON (others OFF)
   - Wait 4 seconds
3. **Yellow State:**
   - Turn YELLOW ON (others OFF)
   - Wait 2 seconds
4. Repeat loop

### 9️⃣ Execution Flow (Plain English)
The system cycles endlessly. It starts showing RED to stop traffic. Then it switches to GREEN to allow movement. Before going back to RED, it briefly shows YELLOW to warn drivers to slow down. This "Green -> Yellow -> Red" transitions are crucial for safety; we never jump straight from Green to Red!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

red = Pin(15, Pin.OUT)
yellow = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)

def set_lights(r, y, g):
    red.value(r)
    yellow.value(y)
    green.value(g)

print("Traffic Light System Active")

while True:
    # 1. STOP (Red)
    print("State: RED (Stop)")
    set_lights(1, 0, 0)
    time.sleep(5)
    
    # 2. GO (Green)
    print("State: GREEN (Go)")
    set_lights(0, 0, 1)
    time.sleep(4)
    
    # 3. CAUTION (Yellow)
    print("State: YELLOW (Slow)")
    set_lights(0, 1, 0)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wrong Sequence**: Standard is G->Y->R, not R->Y->G (in most countries).
*   **Timing Too Short**: Yellow needs to be visible (2s minimum).
*   **Wiring Mix-up**: Check which pin is which color!

### 1️⃣2️⃣ Try This Next
*   **Red-Yellow Prep**: Add a "Red+Yellow" state before Green (common in UK/Europe).
*   **Blinking Green**: Blink green before turning yellow.

---

## 1️⃣ Project 0242: Pedestrian Crossing Button

### 2️⃣ Learning Objective
Add an interactive "Press to Walk" button that requests a safe crossing interval, interrupting the normal traffic flow.

### 3️⃣ Concepts Introduced
*   User Requests
*   Interrupt Handling (IRQ)
*   Priority Logic
*   Request Flag/Queuing
*   Pedestrian Signals

### 4️⃣ Hardware Required
*   Traffic Lights (Previous setup)
*   Pedestrian Button (GP14)
*   Walk LED (White/Blue - GP18)
*   Don't Walk LED (Red - GP19)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Ped Button** | GP14 |
| **Walk LED** | GP18 |
| **Stop LED** | GP19 |

### 6️⃣ Blocks Used
🔹 **Interrupts** - Button monitoring
🔹 **Logic** - Check request flag
🔹 **Functions** - Walk cycle

### 7️⃣ Variables & State
*   **pedestrianRequested**: Boolean - True if someone pressed button
*   **isSafeToWalk**: Boolean - Traffic is stopped

### 8️⃣ Step-by-Step Guide
**A. Init**
1. Setup LEDs and Button (with Pull-Down)
2. Attach Interrupt to Button -> set `pedestrianRequested = True`

**B. Loop**
1. Run Normal Traffic Cycle (Green->Yellow->Red)
2. **Crucial Check:** During RED state, check `if pedestrianRequested`:
   - Keep Traffic RED
   - Turn Walk LED ON
   - Wait 5 seconds
   - Blink Walk LED (hurry up)
   - Turn Walk OFF, Don't Walk ON
   - Reset `pedestrianRequested = False`
3. Resume Traffic flow

### 9️⃣ Execution Flow
The traffic light usually ignores the button. But when the button is pressed, the system "remembers" it. The next time the traffic light turns RED (stopping cars), it sees the memory flag is set. It then activates the specialized "Walk" sequence for pedestrians before letting cars go again.

### 🔟 Generated Code
```python
from machine import Pin
import time

# Traffic
red = Pin(15, Pin.OUT)
yellow = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)

# Pedestrian
walk_led = Pin(18, Pin.OUT)
stop_led = Pin(19, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

ped_request = False

def request_crossing(pin):
    global ped_request
    ped_request = True
    print(">> Pedestrian Button Pressed!")

button.irq(trigger=Pin.IRQ_RISING, handler=request_crossing)

def traffic_cycle():
    global ped_request
    
    # GREEN
    red.value(0); yellow.value(0); green.value(1)
    stop_led.value(1); walk_led.value(0)
    time.sleep(4)
    
    # YELLOW
    green.value(0); yellow.value(1)
    time.sleep(2)
    
    # RED
    yellow.value(0); red.value(1)
    
    # CHECK PEDESTRIAN
    if ped_request:
        print(">> Pedestrian Crossing Active")
        stop_led.value(0); walk_led.value(1) # WALK
        time.sleep(4)
        
        # Blink warning
        for _ in range(3):
            walk_led.toggle()
            time.sleep(0.5)
            
        walk_led.value(0); stop_led.value(1) # DONT WALK
        ped_request = False
    else:
        time.sleep(2) # Normal red time if no one waiting

while True:
    traffic_cycle()
```

---

## 1️⃣ Project 0243: Emergency Vehicle Override

### 2️⃣ Learning Objective
Simulate a system that clears traffic immediately when an emergency vehicle approaching signal involves detected.

### 3️⃣ Concepts Introduced
*   Priority Interrupt (High Level)
*   State Override
*   System Reset
*   Emergency Protocols
*   Audible Warnings

### 4️⃣ Hardware Required
*   Traffic setup
*   Emergency Switch (GP20)
*   Buzzer (GP21)

### 8️⃣ Step-by-Step Guide
**A. Normal Operation**
Loop standard lights.
**B. Emergency Trigger**
1. Read Emergency Switch continuously.
2. If Switch == HIGH:
   - **Abort** current cycle immediately
   - Turn Traffic RED immediately
   - Sound Buzzer (Siren)
   - Wait until Switch == LOW
   - Reset cycle safely

### 10️⃣ Generated Code
```python
from machine import Pin
import time

# ... (LED definitions)
emergency_sw = Pin(20, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(21, Pin.OUT)

def emergency_mode():
    print("!!! EMERGENCY OVERRIDE !!!")
    # Immediate Red
    green.value(0); yellow.value(0); red.value(1)
    
    while emergency_sw.value():
        buzzer.toggle()
        time.sleep(0.2)
    
    print("Emergency Cleared - Resuming")
    buzzer.value(0)
    time.sleep(1)

while True:
    if emergency_sw.value():
        emergency_mode()
    else:
        # Normal cycle logic here...
        # Note: In real code, we'd check switch inside each sleep
        # or use interrupts to break the sleep loop.
        pass # (Placeholder)
```

---

## 1️⃣ Project 0244: Two-Way Intersection

### 2️⃣ Learning Objective
Coordinate two sets of traffic lights (North-South and East-West) so they never show green simultaneously.

### 3️⃣ Concepts Introduced
*   Intersection Logic
*   Mutual Exclusion (Mutex)
*   Deadlock Prevention
*   "All-Red" Clearance Interval

### 4️⃣ Hardware Required
*   Set A (NS): R/Y/G (GP15-17)
*   Set B (EW): R/Y/G (GP18-20)

### 8️⃣ Step-by-Step Guide
**Cycle Definition:**
1. **NS Green / EW Red**: Cars flow North-South. (5s)
2. **NS Yellow / EW Red**: NS warning. (2s)
3. **All Red**: Safety buffer! (1s) - *Crucial for clearing intersection*
4. **EW Green / NS Red**: Cars flow East-West. (5s)
5. **EW Yellow / NS Red**: EW warning (2s)
6. **All Red**: Safety buffer. (1s)

### 10️⃣ Generated Code
```python
# Helper to set detailed states
def set_intersection(ns_state, ew_state):
    # Unpack tuples (r,y,g)
    ns_r, ns_y, ns_g = ns_state
    ew_r, ew_y, ew_g = ew_state
    
    # Set NS Pins (15-17)
    Pin(15, Pin.OUT).value(ns_r)
    Pin(16, Pin.OUT).value(ns_y)
    Pin(17, Pin.OUT).value(ns_g)
    
    # Set EW Pins (18-20)
    Pin(18, Pin.OUT).value(ew_r)
    Pin(19, Pin.OUT).value(ew_y)
    Pin(20, Pin.OUT).value(ew_g)

# Colors: (R, Y, G)
RED = (1,0,0); YEL = (0,1,0); GRN = (0,0,1)

while True:
    # NS Go
    set_intersection(GRN, RED)
    time.sleep(5)
    
    # NS Yield
    set_intersection(YEL, RED)
    time.sleep(2)
    
    # Safety
    set_intersection(RED, RED)
    time.sleep(1)
    
    # EW Go
    set_intersection(RED, GRN)
    time.sleep(5)
    
    # EW Yield
    set_intersection(RED, YEL)
    time.sleep(2)
    
    # Safety
    set_intersection(RED, RED)
    time.sleep(1)
```

---

## 1️⃣ Project 0245: Adaptive Timing (Sensor-Based)

### 2️⃣ Learning Objective
Adjust Green light duration dynamically based on how many cars are waiting (using sensors).

### 3️⃣ Concepts Introduced
*   Dynamic Timing
*   Sensor Input (Simulation)
*   Efficiency Algorithms
*   Smart Traffic Management

### 4️⃣ Hardware Required
*   Traffic Lights
*   2x IR Obstacle Sensors (GP26, GP27) representing "Car Sensors"

### 8️⃣ Step-by-Step Guide
**Logic:**
1. Before turning NS Green, check NS Sensor.
2. If Sensor ACTIVE (Car waiting):
   - Set Green Time = **8 seconds** (Long)
   - Print "Heavy Traffic!"
3. If Sensor CLEAR:
   - Set Green Time = **3 seconds** (Short)
   - Print "Light Traffic"
4. Repeat logic for EW side.

### 10️⃣ Generated Code
```python
north_sensor = Pin(26, Pin.IN)

while True:
    # Determining duration
    duration = 3 # Minimum
    if north_sensor.value() == 0: # Active LOW usually
        print("North Traffic Detected! Extending Green.")
        duration = 8
        
    set_lights(0,0,1) # Green
    time.sleep(duration)
    # ... Rest of cycle
```

---

## 1️⃣ Project 0246: Four-Way Intersection with Turn Arrows

### 2️⃣ Learning Objective
Simulate a complex 4-way junction including "Protected Left Turn" phases.

### 3️⃣ Concepts Introduced
*   Turn Signals
*   Complex Phasing
*   Phased Arrays
*   Traffic Engineering

### 4️⃣ Hardware Required
*   4 Directions (N, S, E, W)
*   Each: Red, Yellow, Green, **Blue** (Turn Arrow)

### 9️⃣ Execution Flow
1. **N/S Left Turns Only** (Green Arrows)
2. **N/S Straight** (Green Balls)
3. **N/S Yellow**
4. **All Red**
5. **E/W Left Turns Only**
6. **E/W Straight**
7. **E/W Yellow**
8. **All Red**

---

## 1️⃣ Project 0247: Night Mode (Flashing Yellow)

### 2️⃣ Learning Objective
Implement a power-saving "Night Mode" where main roads flash yellow and side roads flash red.

### 3️⃣ Concepts Introduced
*   Operating Modes
*   Blinking Patterns
*   Low-Power logic
*   RTC (Time) basics

### 10️⃣ Generated Code
```python
is_night = False # Toggle this via a button or RTC

while True:
    if is_night:
        # Flashing Yellow (Caution)
        yellow.toggle()
        red.value(0); green.value(0)
        time.sleep(0.5)
    else:
        # Normal Logic
        pass
```

---

## 1️⃣ Project 0248: Countdown Timer Display

### 2️⃣ Learning Objective
Integrate a 7-segment display (TM1637) to show drivers exactly how many seconds until the light changes.

### 3️⃣ Concepts Introduced
*   User Interfaces
*   Countdown Logic
*   Display Drivers
*   Synchronization

### 4️⃣ Hardware
*   TM1637 Display (CLK=GP2, DIO=GP3)

### 10️⃣ Generated Code
```python
import tm1637
display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

green_time = 9

# Green State with Countdown
set_lights(0,0,1)
for i in range(green_time, 0, -1):
    display.number(i)
    time.sleep(1)
```

---

## 1️⃣ Project 0249: Smart City Integration (UART)

### 2️⃣ Learning Objective
Connect two separate intersections via serial wire so they synchronize their cycles ("Green Wave").

### 3️⃣ Concepts Introduced
*   Distributed Systems
*   UART Communication
*   Master/Slave capability
*   Synchronization Signals

### 10️⃣ Generated Code
```python
uart = machine.UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Master Pico:
# At start of cycle:
uart.write('SYNC')

# Slave Pico:
while True:
    if uart.any():
        msg = uart.read()
        if 'SYNC' in msg:
            start_cycle()
```

---

## 1️⃣ Project 0250: Master Traffic Control System

### 2️⃣ Learning Objective
Combine ALL features into one massive system.

### 3️⃣ Features
1. **Modes:** Auto, Manual, Night, Emergency
2. **Inputs:** Pedestrian buttons, Car sensors, Emergency switch
3. **Outputs:** 4-Way Lights, Walk Signals, Countdown, Buzzer
4. **Logic:** Adaptive timing with overrides.

### 10️⃣ Code Strategy
Use a State Machine architecture:
*   `State = NORMAL` -> Check sensors -> Run Lights
*   `State = PEDESTRIAN` -> Run Walk Cycle
*   `State = EMERGENCY` -> Hold All Red
*   `State = NIGHT` -> Flash Yellow

---

**Batch 25 Complete & Fixed.**
