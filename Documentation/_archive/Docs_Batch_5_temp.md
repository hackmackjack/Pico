
# 🏁 Batch 5: Traffic Lights 1

## 1️⃣ Project 0041: Introduction to Traffic Lights
### 2️⃣ Learning Objective
Control a complex multi-LED module. You will replicate a standard traffic signal cycle (Green-Yellow-Red), implementing safety delays critical for real-world intersections.

### 3️⃣ Concepts Introduced
*   **State Cycling**: Fixed order of operations.
*   **Safety Critical Systems**: Understanding why timing matters (Red overlap).

### 4️⃣ Hardware Required
*   **Pico**
*   **Traffic Light Module** (or 3 separate LEDs: R, Y, G)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Red LED** | GP13 |
| **Yellow LED** | GP14 |
| **Green LED** | GP15 |
| **GND** | GND |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [13] to [High]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   **Green**: G=High, Y=Low, R=Low. Wait 5s.
    *   **Yellow**: G=Low, Y=High, R=Low. Wait 2s.
    *   **Red**: G=Low, Y=Low, R=High. Wait 5s.

### 9️⃣ Execution Flow (Plain English)
The standard American sequence: Cars go (Green), Cars caution (Yellow), Cars stop (Red). The system loops forever.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

red = machine.Pin(13, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

while True:
    # Green
    red.value(0); yel.value(0); grn.value(1)
    time.sleep(5)
    # Yellow
    grn.value(0); yel.value(1)
    time.sleep(2)
    # Red
    yel.value(0); red.value(1)
    time.sleep(5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Overlap**: Don't leave Green on when turning Red on.

### 1️⃣2️⃣ Try This Next
*   **Short Green**: Simulate a busy road vs side road (Long Green vs Short Green).

---

## 1️⃣ Project 0042: Blinking Traffic Lights (Maintenance)
### 2️⃣ Learning Objective
Simulate failure modes or special states. Flashing Yellow indicates "Proceed with Caution".

### 3️⃣ Concepts Introduced
*   **Indication**: Using blink patterns to communicate status.

### 4️⃣ Hardware Required
*   **Pico**
*   **Traffic Light Module**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Yellow** | GP14 |

### 6️⃣ Blocks Used
🔹 **Loop**
*   **Category:** Loops

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Yellow ON. Wait 0.5s.
    *   Yellow OFF. Wait 0.5s.
    *   (Red and Green stay OFF).

### 9️⃣ Execution Flow (Plain English)
Simple blink on the center light.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
yel = machine.Pin(14, machine.Pin.OUT)

while True:
    yel.value(1)
    time.sleep(0.5)
    yel.value(0)
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Ghosting**: Ensure other pins are Low.

### 1️⃣2️⃣ Try This Next
*   **Time of Day**: Run normal cycle for 20s, then blink mode for 10s.

---

## 1️⃣ Project 0043: Manual Traffic Control (Police Override)
### 2️⃣ Learning Objective
Interrupt a cycle for manual control. A "Police" button forces all lights Red immediately.

### 3️⃣ Concepts Introduced
*   **Interrupts/Procedures**: (Conceptually). Breaking normal flow.
*   **Priority**: Safety overrides convenience.

### 4️⃣ Hardware Required
*   **Pico**
*   **Traffic Light**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button (Police): All Red.
    *   ELSE: Normal Cycle (Green -> Yellow -> Red).

### 9️⃣ Execution Flow (Plain English)
If the button is held, the traffic light hangs on Red. As soon as released, it resumes/restarts the cycle.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(13, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

def set_lights(r, y, g):
    red.value(r); yel.value(y); grn.value(g)

while True:
    if btn.value():
        # Police Override (All Red)
        set_lights(1, 0, 0)
        time.sleep(0.1) # Fast checking
    else:
        # Normal Cycle (Time-sliced check)
        # Green
        set_lights(0, 0, 1)
        for _ in range(50): # 5 seconds
            if btn.value(): break
            time.sleep(0.1)
        if btn.value(): continue
        
        # Yellow
        set_lights(0, 1, 0)
        for _ in range(20): # 2 seconds
            if btn.value(): break
            time.sleep(0.1)
        if btn.value(): continue

        # Red
        set_lights(1, 0, 0)
        for _ in range(50): # 5 seconds
            if btn.value(): break
            time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Responsiveness**: With `time.sleep(5)`, checking the button won't work well. You need to loop `check button` 50 times with `sleep(0.1)`.

### 1️⃣2️⃣ Try This Next
*   **Radio Control**: Use a second Pico to trigger the Red Light remotely.

---

## 1️⃣ Project 0044: Traffic Sequences (UK Standard)
### 2️⃣ Learning Objective
Implement specific regional standards. UK Sequence: Red -> Red+Yellow -> Green -> Yellow -> Red.

### 3️⃣ Concepts Introduced
*   **Compound States**: Two discrete outputs active simultaneously.
*   **Preparation**: Alerting drivers to get ready.

### 4️⃣ Hardware Required
*   **Pico**
*   **Traffic Light**

### 5️⃣ Wiring / Interfaces
(Same)

### 6️⃣ Blocks Used
🔹 **Set Pin**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Red ON. Wait.
    *   Red ON + Yellow ON. Wait 1s.
    *   Green ON (Red/Yel OFF). Wait.
    *   Yellow ON (Grn OFF). Wait.

### 9️⃣ Execution Flow (Plain English)
The weird step is "Red+Yellow". It means "Get ready to go". Green means go. Yellow means stop if safe.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

red = machine.Pin(13, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

while True:
    # Red
    red.value(1); yel.value(0); grn.value(0)
    time.sleep(3)
    
    # Red + Yellow
    yel.value(1) 
    time.sleep(1)
    
    # Green
    red.value(0); yel.value(0); grn.value(1)
    time.sleep(5)
    
    # Yellow
    grn.value(0); yel.value(1)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Forget Red**: When turning on Yellow for the transition, don't turn off Red yet!

### 1️⃣2️⃣ Try This Next
*   **Drag Strip**: Pre-stage lights.

---

## 1️⃣ Project 0045: Interactive Traffic (Pedestrian)
### 2️⃣ Learning Objective
Demand-based actuation. The light stays Green for cars forever *until* a walker presses the button.

### 3️⃣ Concepts Introduced
*   **State Retention**: Staying in one state until an event.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Crosswalk)
*   **Traffic Light**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |

### 6️⃣ Blocks Used
🔹 **Wait Until**
*   **Category:** Control
*   **Block:** `wait until [Button]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Green ON.
    *   **Wait Until** Button Pressed.
    *   Yellow ON. Wait 2s.
    *   Red ON. Wait 5s (Walk).
    *   (Loop restarts -> Green).

### 9️⃣ Execution Flow (Plain English)
Cars flow freely. A person arrives and requests a slot. The light changes safely to let them cross, then returns to car-priority mode.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(13, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

while True:
    # Green
    red.value(0); grn.value(1); yel.value(0)
    
    # Wait for pedestrian
    if btn.value():
        # Cycle
        time.sleep(0.5) # Reaction
        grn.value(0); yel.value(1)
        time.sleep(2)
        yel.value(0); red.value(1)
        time.sleep(5) # Walk
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Instant Change**: Don't go Green->Red instantly. Use Yellow. Apps like Waze/Google Maps depend on safe transitions.

### 1️⃣2️⃣ Try This Next
*   **Walk Light**: Add a separate White LED for the "Walk" icon.

---

## 1️⃣ Project 0046: Smart Traffic Switch (Night Mode)
### 2️⃣ Learning Objective
Day/Night cycle behaviors. Use LDR to switch between Full Cycle (Day) and Blinking Yellow (Night).

### 3️⃣ Concepts Introduced
*   **Modes**: Major operational states.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR**
*   **Traffic Light**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 |

### 6️⃣ Blocks Used
🔹 **If / Else**

### 7️⃣ Variables & State
*   **light**: Analog value.

### 8️⃣ Block Logic
*   **Loop**:
    *   If Light > Threshold (Day):
        *   Run Sequence Step (or full sequence).
    *   Else (Night):
        *   Blink Yellow.

### 9️⃣ Execution Flow (Plain English)
The Pico checks the sun. If up -> Traffic duty. If down -> Caution mode.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

ldr = machine.ADC(26)
red = machine.Pin(13, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

NIGHT_THRESHOLD = 20000

while True:
    if ldr.read_u16() > NIGHT_THRESHOLD:
        # Day Mode
        red.value(0); yel.value(0); grn.value(1)
        time.sleep(3)
        grn.value(0); yel.value(1)
        time.sleep(1)
        yel.value(0); red.value(1)
        time.sleep(3)
    else:
        # Night Mode
        red.value(0); grn.value(0)
        yel.toggle()
        time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Blocking**: If you run the full sequence using `sleep(5)`, the Pico can't check if it got dark until the sequence finishes.

### 1️⃣2️⃣ Try This Next
*   **Timer**: Use RTC (Real Time Clock) instead of light sensor.

---

## 1️⃣ Project 0047: Traffic Alarm (Red Light Camera)
### 2️⃣ Learning Objective
Violation detection. If the button (Car) is pressed while the Red Light is active, trigger a "Flash".

### 3️⃣ Concepts Introduced
*   **Conditional Logic AND State**: IF (Car present AND Red Light active).

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Under road loop)
*   **Traffic Light**
*   **White LED** (Camera)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Camera** | GP16 |

### 6️⃣ Blocks Used
🔹 **And**
*   **Category:** Logic
*   **Block:** `[Button] AND [isRed]`

### 7️⃣ Variables & State
*   **isRed**: Boolean.

### 8️⃣ Block Logic
*   **Loop**:
    *   **Logic**: Update Lights. Set `isRed` = True/False.
    *   **Check Violations**:
        *   IF `isRed` AND `Button` (Car):
            *   Flash Camera LED 3 times.

### 9️⃣ Execution Flow (Plain English)
The system knows the rules (Red = Stop). It watches the road. If a car breaks the rule, it gathers evidence (Flash).

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

car_sensor = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
camera = machine.Pin(16, machine.Pin.OUT)
red = machine.Pin(13, machine.Pin.OUT)

def check_violation():
    if car_sensor.value():
        for _ in range(3):
            camera.value(1); time.sleep(0.05)
            camera.value(0); time.sleep(0.05)

while True:
    # Red Phase (Checking violations)
    red.value(1)
    for _ in range(50):
        check_violation()
        time.sleep(0.1)
    red.value(0)
    
    # Just sleep through Green/Yellow (No violations possible)
    time.sleep(5) 
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Grace Period**: Real cameras give 0.1s grace.

### 1️⃣2️⃣ Try This Next
*   **Ticket**: Print "$100 Fine" to console.

---

## 1️⃣ Project 0048: The Traffic Game (Drag Race)
### 2️⃣ Learning Objective
Reaction timer. Wait for Green, then measure time to press.

### 3️⃣ Concepts Introduced
*   **Stopwatch**: Counting ticks.

### 4️⃣ Hardware Required
*   **Pico**
*   **Traffic Light**
*   **Button**

### 5️⃣ Wiring / Interfaces
(Standard)

### 6️⃣ Blocks Used
🔹 **Timer**

### 7️⃣ Variables & State
*   **reactionTime**.

### 8️⃣ Block Logic
*   **Seq**:
    *   Pre-stage (Yel).
    *   Stage (Yel).
    *   GO (Green). Start Timer.
    *   Wait for Button. Stop Timer.
    *   Print Time.

### 9️⃣ Execution Flow (Plain English)
Drivers watch the tree. Yellow... Yellow... GREEN! Stomp the gas (Button).

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
grn = machine.Pin(15, machine.Pin.OUT)
yel = machine.Pin(14, machine.Pin.OUT)

while True:
    grn.value(0); yel.value(0)
    
    # Random Wait
    time.sleep(random.uniform(2, 5))
    
    # Tree
    yel.value(1); time.sleep(0.5); yel.value(0); time.sleep(0.5)
    yel.value(1); time.sleep(0.5); yel.value(0)
    
    # GO
    grn.value(1)
    start = time.ticks_ms()
    while not btn.value():
        pass
    diff = time.ticks_diff(time.ticks_ms(), start)
    print(f"Reaction: {diff} ms")
    grn.value(0)
    time.sleep(3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Redlight**: Pressing before Green = Disqualified.

### 1️⃣2️⃣ Try This Next
*   **2 Player**: Two lanes.

---

## 1️⃣ Project 0049: Automated Traffic (Sensor)
### 2️⃣ Learning Objective
Ultrasonic car detection. Green only when car pulls up.

### 3️⃣ Concepts Introduced
*   **Presence Detection**: Replacing buttons with distance sensors.

### 4️⃣ Hardware Required
*   **Pico**
*   **HC-SR04**
*   **Traffic Light**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Trig** | GP16 |
| **Echo** | GP17 |

### 6️⃣ Blocks Used
🔹 **Distance**
*   **Category:** Sensors

### 7️⃣ Variables & State
*   **dist**.

### 8️⃣ Block Logic
*   **Loop**:
    *   Red ON.
    *   **Wait**: Until Distance < 10cm.
    *   Green ON (10s).
    *   Red ON.

### 9️⃣ Execution Flow (Plain English)
The light sleeps on Red. When a car pulls up close (10cm), it wakes up and gives a green light.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

trig = machine.Pin(16, machine.Pin.OUT)
echo = machine.Pin(17, machine.Pin.IN)
red = machine.Pin(13, machine.Pin.OUT)
grn = machine.Pin(15, machine.Pin.OUT)

def measure():
    trig.low(); time.sleep_us(2)
    trig.high(); time.sleep_us(10); trig.low()
    while echo.value() == 0: pass
    start = time.ticks_us()
    while echo.value() == 1: pass
    return (time.ticks_diff(time.ticks_us(), start)) * 0.0343 / 2

while True:
    # Idle Red
    red.value(1); grn.value(0)
    
    if measure() < 10: # Car detected
        red.value(0); grn.value(1)
        time.sleep(5)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Echo**: HC-SR04 needs 5V but logic is 3.3V. Use resistors? (Usually fine on Pico for short duration, but voltage divider recommended).

### 1️⃣2️⃣ Try This Next
*   **Timeout**: If car leaves, turn Red early.

---

## 1️⃣ Project 0050: Mastering Traffic (Cross Traffic)
### 2️⃣ Learning Objective
Manage two intersecting flows. 2 Traffic lights must be perfectly synced.

### 3️⃣ Concepts Introduced
*   **Synchronization**: Shared state.
*   **Deadlock Prevention**.

### 4️⃣ Hardware Required
*   **Pico**
*   **2x Traffic Module**

### 5️⃣ Wiring / Interfaces
*   Light 1: GP10-12
*   Light 2: GP13-15

### 6️⃣ Blocks Used
🔹 **Functions**
*   **Category:** Functions
*   **Block:** `setNorth[Green]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   North Green / West Red. Wait 5s.
    *   North Yellow / West Red. Wait 2s.
    *   North Red / West Red (All Stop - Safety). Wait 1s.
    *   North Red / West Green. Wait 5s.
    *   North Red / West Yellow. Wait 2s.
    *   North Red / West Red. Wait 1s.

### 9️⃣ Execution Flow (Plain English)
The most critical part is the "All Red" phase. Before West turns Green, North must be fully stopped. This 1-second buffer prevents T-bone crashes if someone runs a late yellow.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

# North
n_red = machine.Pin(10, machine.Pin.OUT)
n_yel = machine.Pin(11, machine.Pin.OUT)
n_grn = machine.Pin(12, machine.Pin.OUT)
# West
w_red = machine.Pin(13, machine.Pin.OUT)
w_yel = machine.Pin(14, machine.Pin.OUT)
w_grn = machine.Pin(15, machine.Pin.OUT)

def set_lights(n, w):
    # n/w tuples: (r, y, g)
    n_red.value(n[0]); n_yel.value(n[1]); n_grn.value(n[2])
    w_red.value(w[0]); w_yel.value(w[1]); w_grn.value(w[2])

while True:
    # N: Green, W: Red
    set_lights((0,0,1), (1,0,0))
    time.sleep(5)
    
    # N: Yellow, W: Red
    set_lights((0,1,0), (1,0,0))
    time.sleep(2)
    
    # All Red
    set_lights((1,0,0), (1,0,0))
    time.sleep(1)
    
    # N: Red, W: Green
    set_lights((1,0,0), (0,0,1))
    time.sleep(5)
    
    # N: Red, W: Yellow
    set_lights((1,0,0), (0,1,0))
    time.sleep(2)
    
    # All Red
    set_lights((1,0,0), (1,0,0))
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Green/Green**: Never allow both Green.

### 1️⃣2️⃣ Try This Next
*   **Turn Arrow**: Add a left turn arrow phase.

---
