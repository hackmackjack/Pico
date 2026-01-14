
# 🏁 Batch 9: Counting Machine 1

## 1️⃣ Project 0081: Introduction to Counting Machine
### 2️⃣ Learning Objective
The "Counter". Create a variable `count = 0`. Press button -> Add 1. Print. Reset at 10.

### 3️⃣ Concepts Introduced
*   **Increment**: x = x + 1.
*   **Modulo/Reset**: Rolling over a value.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |

### 6️⃣ Blocks Used
🔹 **Change Variable**
🔹 **Print**

### 7️⃣ Variables & State
*   **count**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Pressed:
        *   `count` += 1.
        *   IF `count` >= 10: `count` = 0.
        *   Print `count`.
        *   Wait for Release.

### 9️⃣ Execution Flow (Plain English)
Click (1), Click (2)... Click (9), Click (0).

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0
while True:
    if btn.value():
        count += 1
        if count > 9: count = 0
        print("Count:", count)
        while btn.value(): time.sleep(0.01) # Debounce/Release
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Fast Count**: Without "Wait for Release", a single press counts 50 times.

### 1️⃣2️⃣ Try This Next
*   **Down**: Button B substracts.

---

## 1️⃣ Project 0082: Blinking Counting Machine (Visual Count)
### 2️⃣ Learning Objective
Feedback. If count is 3, blink 3 times.

### 3️⃣ Concepts Introduced
*   **Data Visualization**: Converting a number to physical events.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Repeat**

### 7️⃣ Variables & State
*   **count**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   `count` += 1.
        *   Loop `count` times:
            *   Blink LED.

### 9️⃣ Execution Flow (Plain English)
Press button. It calculates the new number, then flashes that many times to confirm.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
count = 0
while True:
    if btn.value():
        count += 1
        print("Count:", count)
        while btn.value(): pass
        # Blink it out
        for i in range(count):
            led.value(1); time.sleep(0.2); led.value(0); time.sleep(0.2)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Delay**: The button is unresponsive while it is blinking the count.

### 1️⃣2️⃣ Try This Next
*   **Binary**: Blink Long for 5, Short for 1. (Roman Numeral style?)

---

## 1️⃣ Project 0083: Manual Counting Machine Control (Up/Down)
### 2️⃣ Learning Objective
Bi-directional control. Button A (+1), Button B (-1).

### 3️⃣ Concepts Introduced
*   **Clamping**: Preventing values from going below min or above max.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |

### 6️⃣ Blocks Used
🔹 **If / Else If**

### 7️⃣ Variables & State
*   **count**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Btn A: `count`++.
    *   IF Btn B: `count`--.
    *   Limit `count` (0 to 10).

### 9️⃣ Execution Flow (Plain English)
Volume control logic. Up, Up, Down, Up.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0
while True:
    change = False
    if btnA.value():
        count += 1
        change = True
        while btnA.value(): pass
    
    if btnB.value():
        count -= 1
        change = True
        while btnB.value(): pass
        
    if change:
        if count < 0: count = 0
        print("Count:", count)
        
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Negative**: Without the check `if count < 0`, it would go -1, -2...

### 1️⃣2️⃣ Try This Next
*   **Servo**: Map the count 0-10 to Servo angle 0-180.

---

## 1️⃣ Project 0084: Counting Machine Sequences (Binary Display)
### 2️⃣ Learning Objective
Binary. Show 0-7 using 3 LEDs.

### 3️⃣ Concepts Introduced
*   **Bitwise Operation**: Checking individual bits (001, 010, 100).
*   **Binary Number System**: Base 2.

### 4️⃣ Hardware Required
*   **Pico**
*   **3 LEDs** (Bit0, Bit1, Bit2)
*   **Button**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Bit 0 (LSB)** | GP13 |
| **Bit 1** | GP14 |
| **Bit 2 (MSB)** | GP15 |

### 6️⃣ Blocks Used
🔹 **Remainder** (Modulo)
🔹 **Integer Division**

### 7️⃣ Variables & State
*   **count**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button: `count`++.
    *   **Display**:
        *   Bit0 = `count` % 2.
        *   Bit1 = (`count` // 2) % 2.
        *   Bit2 = (`count` // 4) % 2.
        *   Set LEDs to Bits.

### 9️⃣ Execution Flow (Plain English)
Press button: 000, 001, 010, 011, 100...

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led0 = machine.Pin(13, machine.Pin.OUT)
led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)
count = 0
while True:
    if btn.value():
        count = (count + 1) % 8
        while btn.value(): pass
        
    # Bit logic
    led0.value(count & 1)
    led1.value((count >> 1) & 1)
    led2.value((count >> 2) & 1)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Order**: LSB (Least Significant Bit) is the "1s" column. MSB is the "4s" column.

### 1️⃣2️⃣ Try This Next
*   **Hex**: Count to 15 with 4 LEDs.

---

## 1️⃣ Project 0085: Interactive Counting Machine (Step Counter)
### 2️⃣ Learning Objective
Pedometer. Use a Tilt Sensor.

### 3️⃣ Concepts Introduced
*   **Digital Sensor**: Tilt ball switch works like a button.
*   **Edge Detection**: Counting the *transition* from closed to open.

### 4️⃣ Hardware Required
*   **Pico**
*   **Tilt Sensor** (SW-520D)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Tilt Sensor** | GP10 |

### 6️⃣ Blocks Used
🔹 **If**

### 7️⃣ Variables & State
*   **steps**
*   **last_state**

### 8️⃣ Block Logic
*   **Loop**:
    *   `state` = Read Sensor.
    *   IF `state` != `last_state` AND `state` == 1:
        *   `steps` += 1.
    *   `last_state` = `state`.

### 9️⃣ Execution Flow (Plain English)
Shake the Pico. Does it rattle? Steps go up.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
tilt = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)
steps = 0
last_val = tilt.value()
while True:
    val = tilt.value()
    if val != last_val:
        if val == 1: # Transition
            steps += 1
            print("Steps:", steps)
        last_val = val
        time.sleep(0.1) # Debounce
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Orientation**: Tilt sensors only work if oriented vertically so gravity moves the ball.

### 1️⃣2️⃣ Try This Next
*   **Reset**: Add a button to zero the steps.

---

## 1️⃣ Project 0086: Smart Counting Machine Switch (Capacity)
### 2️⃣ Learning Objective
Limit monitoring. Count people. If > 5, Red Light.

### 3️⃣ Concepts Introduced
*   **Threshold Comparison**: Value > Max.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Red/Green LEDs**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Green** | GP14 |
| **Red** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else**

### 7️⃣ Variables & State
*   **people**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button: `people`++.
    *   IF `people` > 5:
        *   Red ON, Green OFF.
    *   ELSE:
        *   Green ON, Red OFF.

### 9️⃣ Execution Flow (Plain English)
Click, Green. Click, Green. ... Click (6), Red! Shop Full.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(15, machine.Pin.OUT)
grn = machine.Pin(14, machine.Pin.OUT)
people = 0
while True:
    if btn.value():
        people += 1
        print("People:", people)
        while btn.value(): pass
        
    if people > 5:
        red.value(1); grn.value(0)
    else:
        red.value(0); grn.value(1)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Reset**: How do people leave? You need a second button for "Exit".

### 1️⃣2️⃣ Try This Next
*   **Dual Counter**: Implement the Exit button.

---

## 1️⃣ Project 0087: Counting Machine Alarm System (Egg Timer)
### 2️⃣ Learning Objective
Set -> Run style. 1 press = 1 second. Then wait for it to run out.

### 3️⃣ Concepts Introduced
*   **Phase Logic**: Setup Phase vs Run Phase.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Repeat**

### 7️⃣ Variables & State
*   **timer_val**

### 8️⃣ Block Logic
*   **A. Setup**:
    *   While True:
        *   IF Button: `timer_val`++. Print.
        *   IF No Press for 3s: Break.
*   **B. Run**:
    *   Loop `timer_val` times: Wait 1s.
    *   Beep.

### 9️⃣ Execution Flow (Plain English)
Tap-Tap-Tap (3 seconds). Wait... (3s delay) -> Start 3s countdown -> BEEP.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)

timer = 0
last_act = time.ticks_ms()

# Setup Phase
print("Set Timer...")
while time.ticks_diff(time.ticks_ms(), last_act) < 3000:
    if btn.value():
        timer += 1
        print("Time:", timer)
        last_act = time.ticks_ms()
        while btn.value(): pass
    time.sleep(0.05)

# Run Phase
print("Starting...")
while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1
    
buzz.value(1); time.sleep(1); buzz.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Logic**: Exiting the setup loop requires a timeout.

### 1️⃣2️⃣ Try This Next
*   **Visual**: Flash the LED every second during countdown.

---

## 1️⃣ Project 0088: The Counting Machine Game (Guess Number)
### 2️⃣ Learning Objective
Match a hidden count. Random(1,5). User must press button match.

### 3️⃣ Concepts Introduced
*   **Equality Check**: Input == Target.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A (Count), B (Enter)**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn A** | GP10 |
| **Btn B** | GP11 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Random**

### 7️⃣ Variables & State
*   **target**
*   **guess**

### 8️⃣ Block Logic
*   **Loop**:
    *   `target` = Random(1, 5).
    *   Wait for B (Enter). While waiting:
        *   IF A: `guess`++.
    *   IF `guess` == `target`: Flash Green.

### 9️⃣ Execution Flow (Plain English)
Computer picks 3. I press A 3 times. I press B. Win!

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    target = random.randint(1, 5)
    guess = 0
    print("Guess 1-5")
    
    while not btnB.value():
        if btnA.value():
            guess += 1
            print("Pressed:", guess)
            while btnA.value(): pass
            
    if guess == target:
        print("WIN!")
        for i in range(5): led.toggle(); time.sleep(0.1)
    else:
        print("Lose. Was", target)
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Feedback**: Without an LED blinking for each press, users lose count.

### 1️⃣2️⃣ Try This Next
*   **Hot/Cold**: Blink fast if close, slow if far.

---

## 1️⃣ Project 0089: Automated Counting Machine (Coin Sorter)
### 2️⃣ Learning Objective
Magnitude counting. Distinguish signal size.

### 3️⃣ Concepts Introduced
*   **Analog Thresholding**: Small dip vs Big dip.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR + Light Source**
*   **Object**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 |

### 6️⃣ Blocks Used
🔹 **Read Analog**

### 7️⃣ Variables & State
*   **small_count**, **big_count**

### 8️⃣ Block Logic
*   **Loop**:
    *   `val` = Read LDR.
    *   IF `val` < 10000 (Big Block): `big_count`++. Wait Reset.
    *   ELSE IF `val` < 30000 (Small Block): `small_count`++. Wait Reset.

### 9️⃣ Execution Flow (Plain English)
Rolling a dime blocks a little light. Rolling a quarter blocks a lot.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
ldr = machine.ADC(26)
# Baseline is bright (~60000)
# Small obj dips to 30000
# Big obj dips to 10000
small = 0
big = 0
while True:
    val = ldr.read_u16()
    if val < 50000: # Something detected
        time.sleep(0.1) # Wait for full occlusion
        val = ldr.read_u16()
        if val < 15000:
            big += 1
            print("Big")
        else:
            small += 1
            print("Small")
        time.sleep(0.5) # Cooldown
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Shadows**: Ambient light ruins this. Use a cardboard tube.

### 1️⃣2️⃣ Try This Next
*   **Servo**: Send big coins left, small coins right.

---

## 1️⃣ Project 0090: Mastering Counting Machine (7-Segment)
### 2️⃣ Learning Objective
Lookup Tables. Map number to Segments.

### 3️⃣ Concepts Introduced
*   **Arrays**: Storing segment patterns.

### 4️⃣ Hardware Required
*   **Pico**
*   **Virtual 7-Seg**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **None** | (Console Sim) |

### 6️⃣ Blocks Used
🔹 **List**

### 7️⃣ Variables & State
*   **patterns[]**

### 8️⃣ Block Logic
*   **Loop**:
    *   For i 0 to 9:
        *   Print `patterns[i]`.

### 9️⃣ Execution Flow (Plain English)
Number 0 uses segments A,B,C,D,E,F. Number 1 uses B,C.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
# 0bGFEDCBA
patterns = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
for num in range(10):
    p = patterns[num]
    print(f"Number {num}: {bin(p)}")
    time.sleep(1)
```

### 🔟1️⃣ Common Mistakes & Debug Tips
*   **Hex/Bin**: Learning to convert 00111111 to 0x3F is a key skill.

### 1️⃣2️⃣ Try This Next
*   **Physical**: Wire up a real 7-segment display (requires 7 pins).

---
