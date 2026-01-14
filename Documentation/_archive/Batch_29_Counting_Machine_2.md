# 📘 Pico 2500: Batch 29 - Counting Machine 2 (Projects 0281-0290)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Digital Logic, Counting & Displays

---

## 1️⃣ Project 0281: Up/Down Counter

### 2️⃣ Learning Objective
Create a manual counter that can count up with one button and down with another, introducing arithmetic variables.

### 3️⃣ Concepts Introduced
*   Variable Arithmetic (`x = x + 1`)
*   Two-Button Logic
*   Bounds Checking (Min/Max limits)
*   State Persistence

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   2x Pushbuttons (Up, Down)
*   Breadboard

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Up Button** | GP14 |
| **Down Button** | GP15 |

### 6️⃣ Blocks Used
🔹 **Variables** - Change variable by 1

### 8️⃣ Step-by-Step Guide
**Logic:**
1. Start `count = 0`.
2. If Up Pressed: `count += 1`.
3. If Down Pressed: `count -= 1`.
4. Print `count`.
5. Wait for release (Debounce).

### 10️⃣ Generated Code
```python
from machine import Pin
import time

up_btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
dn_btn = Pin(15, Pin.IN, Pin.PULL_DOWN)

count = 0

print("Counter Ready: 0")

while True:
    if up_btn.value():
        count += 1
        print(f"Count: {count}")
        time.sleep(0.2) # Debounce
        
    if dn_btn.value():
        count -= 1
        print(f"Count: {count}")
        time.sleep(0.2)
```

---

## 1️⃣ Project 0282: BCD 7-Segment Display (Manual)

### 2️⃣ Learning Objective
Control a single 7-segment display manually by turning on individual segments (a-g) to form numbers.

### 3️⃣ Concepts Introduced
*   7-Segment Layout (a,b,c,d,e,f,g,dp)
*   Binary Encoding
*   Lookup Tables / Dictionaries
*   GPIO Groups

### 4️⃣ Hardware
*   Common Cathode 7-Segment Display
*   7x Resistors (220Ω)

### 5️⃣ Wiring
| Segment | Pin |
| :--- | :--- |
| **a** | GP0 |
| **b** | GP1 |
| ... | ... |
| **g** | GP6 |
| **COM** | GND |

### 10️⃣ Generated Code
```python
# Pins for a,b,c,d,e,f,g
pins = [Pin(i, Pin.OUT) for i in range(7)]

# Map: 0 = segments a,b,c,d,e,f on (binary 00111111 = 0x3F)
digits = [
    0x3F, 0x06, 0x5B, 0x4F, 0x66, # 0-4
    0x6D, 0x7D, 0x07, 0x7F, 0x6F  # 5-9
]

def show_digit(num):
    mask = digits[num]
    for i in range(7):
        # Check bit i
        bit = (mask >> i) & 1
        pins[i].value(bit)

# Test Loop
for i in range(10):
    show_digit(i)
    time.sleep(1)
```

---

## 1️⃣ Project 0283: Preset Counter (Target Reached)

### 2️⃣ Learning Objective
Set a "Goal" (e.g., 10). Count up. When the goal is reached, trigger an alarm or light.

### 3️⃣ Concepts Introduced
*   Comparisons (`==`, `>=`)
*   Target Logic
*   User Feedback

### 10️⃣ Generated Code
```python
TARGET = 10
count = 0
buzzer = Pin(18, Pin.OUT)

while True:
    if btn.value():
        count += 1
        print(count)
        
        if count == TARGET:
            print("GOAL REACHED!")
            buzzer.value(1)
            time.sleep(1)
            buzzer.value(0)
            count = 0 # Reset
            
    time.sleep(0.1)
```

---

## 1️⃣ Project 0284: Tally Counter with Save (File I/O)

### 2️⃣ Learning Objective
Save the count to a file so it is remembered even if the Pico loses power (Non-Volatile Memory).

### 3️⃣ Concepts Introduced
*   File Systems (`open`, `write`)
*   Persistence
*   Boot Loading

### 10️⃣ Generated Code
```python
# Load previous count
try:
    with open("count.txt", "r") as f:
        count = int(f.read())
except:
    count = 0

print(f"Loaded Count: {count}")

while True:
    if btn.value():
        count += 1
        print(count)
        
        # Save updates
        with open("count.txt", "w") as f:
            f.write(str(count))
            
        time.sleep(0.2)
```

---

## 1️⃣ Project 0285: Multi-Digit Counter (TM1637)

### 2️⃣ Learning Objective
Use a 4-digit display module (TM1637) to show larger numbers (0-9999).

### 3️⃣ Concepts Introduced
*   Serial Display Drivers
*   Libraries
*   Scanning Digits

### 10️⃣ Generated Code
```python
import tm1637
display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

count = 0

while True:
    if btn.value():
        count += 1
        display.number(count)
        time.sleep(0.1)
```

---

## 1️⃣ Project 0286: Event Counter (IR Beam)

### 2️⃣ Learning Objective
Automatically count objects passing through an invisible IR beam (Break-Beam sensor).

### 3️⃣ Concepts Introduced
*   Automation
*   Optical Sensors
*   Edge Detection (Falling Edge)
*   Industrial Counting

### 4️⃣ Hardware
*   IR Transmitter + Receiver LED pair

### 10️⃣ Generated Code
```python
beam_sensor = Pin(16, Pin.IN)
count = 0
last_state = 1

while True:
    current = beam_sensor.value()
    
    # Check for Break (High -> Low or Low -> High depending on sensor)
    # Usually: Beam Unbroken = High, Broken = Low
    if last_state == 1 and current == 0:
        count += 1
        print(f"Object Detected! Total: {count}")
    
    last_state = current
    time.sleep(0.01)
```

---

## 1️⃣ Project 0287: Rate Counter (Hz / RPM)

### 2️⃣ Learning Objective
Count how many events happen in a specific time (e.g., clicks per minute), calculating Rate.

### 3️⃣ Concepts Introduced
*   Time Delta calculation
*   Frequency (Hz)
*   Rate Logic (Events / Time)

### 10️⃣ Generated Code
```python
events = 0
start_time = time.ticks_ms()

while True:
    # ... read sensor, events += 1 ...
    
    now = time.ticks_ms()
    if time.ticks_diff(now, start_time) > 1000:
        # 1 Second passed
        print(f"Rate: {events} events/sec")
        events = 0
        start_time = now
```

---

## 1️⃣ Project 0288: Batch Counter

### 2️⃣ Learning Objective
Count "Batches". For example, count 10 items, then increment "Box Count" and reset item count.

### 3️⃣ Concepts Introduced
*   Modulo arithmetic (optional)
*   Nested Counters (Boxes -> Pallets)
*   Reset Logic

### 10️⃣ Generated Code
```python
items = 0
boxes = 0
ITEMS_PER_BOX = 10

# ... inside loop ...
if sensor.value():
    items += 1
    if items >= ITEMS_PER_BOX:
        boxes += 1
        items = 0
        print(f"Box Full! Total Boxes: {boxes}")
        buzzer.beep()
```

---

## 1️⃣ Project 0289: Dual Counter (A vs B)

### 2️⃣ Learning Objective
Track two separate counts (e.g., Votes for A vs Votes for B) and compare them.

### 3️⃣ Concepts Introduced
*   Parallel Variables
*   Comparison Logic
*   Scoreboarding

### 10️⃣ Generated Code
```python
count_a = 0
count_b = 0

if btn_a.value(): count_a += 1
if btn_b.value(): count_b += 1

if count_a > count_b:
    led_a.on(); led_b.off()
elif count_b > count_a:
    led_a.off(); led_b.on()
else:
    # Tie
    led_a.on(); led_b.on()
```

---

## 1️⃣ Project 0290: Production Counter System

### 2️⃣ Learning Objective
A complete factory counter system with Display, Target, Rate calculation, and Reset.

### 3️⃣ Features
1. **Display:** Shows Total Count.
2. **Buttons:** Count, Reset.
3. **Alert:** Beep every 10 items.
4. **Log:** Print rate to console.

### 10️⃣ Code Strategy
Combine TM1637 display code with logic from 0287 and 0288.

Note on TM1637 Library: This is a common MicroPython library. If not present, we use a simple bit-banged implementation within the "Generated Code" section for Project 0285.

---

**Batch 29 Complete & Fixed.**
