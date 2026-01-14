
# 🏁 Batch 10: Morse Code 1

## 1️⃣ Project 0091: Introduction to Morse Code
### 2️⃣ Learning Objective
"SOS". The universal distress signal. Flash the LED: 3 Short flashes (...), 3 Long flashes (---), 3 Short flashes (...).

### 3️⃣ Concepts Introduced
*   **Time Encoding**: Using duration to convey meaning (Short vs Long).
*   **International Protocol**: Standardized signals.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED** (Onboard or External)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 (or Onboard) |

### 6️⃣ Blocks Used
🔹 **Function** (Optional)
🔹 **Wait**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   **S**: Blink Short, Short, Short.
    *   **O**: Blink Long, Long, Long.
    *   **S**: Blink Short, Short, Short.
    *   Wait 3s (Inter-word gap).

### 9️⃣ Execution Flow (Plain English)
... --- ... (Pause).

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
# Dot duration
UNIT = 0.2

while True:
    # S (...)
    for i in range(3):
        led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)
    time.sleep(UNIT*2) # Letter gap
    
    # O (---)
    for i in range(3):
        led.value(1); time.sleep(UNIT*3); led.value(0); time.sleep(UNIT)
    time.sleep(UNIT*2)
    
    # S (...)
    for i in range(3):
        led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)
        
    time.sleep(3) # Word gap
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Spacing**: The silence between dots (1 unit), letters (3 units), and words (7 units) is key to legibility.

### 1️⃣2️⃣ Try This Next
*   **Sound**: Add a buzzer in parallel.

---

## 1️⃣ Project 0092: Blinking Morse Code (Telegraph)
### 2️⃣ Learning Objective
Manual signaling. The LED lights up while the button is pressed. Tap "HELLO".

### 3️⃣ Concepts Introduced
*   **Manual keying**: Human input control.

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
🔹 **Set Pin**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button: LED ON.
    *   ELSE: LED OFF.

### 9️⃣ Execution Flow (Plain English)
Simple pass-through. You are the operator.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    if btn.value():
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.01) # Ultra fast response
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Latency**: Do not put long `sleep()` commands in the loop; it will feel laggy.

### 1️⃣2️⃣ Try This Next
*   **Recording**: Save the timing of your presses to a list.

---

## 1️⃣ Project 0093: Manual Morse Code Control (Dual Key)
### 2️⃣ Learning Objective
Simplified input. Button A plays a Dot (fixed time). Button B plays a Dash (fixed time).

### 3️⃣ Concepts Introduced
*   **Quantization**: Forcing input to fixed values (perfect timing every time).

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn A (Dot)** | GP10 |
| **Btn B (Dash)** | GP11 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else If**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Btn A: Beep 0.2s.
    *   IF Btn B: Beep 0.6s.

### 9️⃣ Execution Flow (Plain English)
Typing Morse code like a keyboard. Left, Right, Left, Left.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
dot = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
dash = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)
UNIT = 0.2

while True:
    if dot.value():
        buzz.value(1); time.sleep(UNIT); buzz.value(0); time.sleep(UNIT)
        while dot.value(): pass # Single fire
    elif dash.value():
        buzz.value(1); time.sleep(UNIT*3); buzz.value(0); time.sleep(UNIT)
        while dash.value(): pass
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Debounce**: Essential here so you don't fire "Dot Dot" on one press.

### 1️⃣2️⃣ Try This Next
*   **Combo**: Hold A+B to play a Word Spacer.

---

## 1️⃣ Project 0094: Morse Code Sequences (Word Builder)
### 2️⃣ Learning Objective
Sequence library. Define functions for letters. Spell words.

### 3️⃣ Concepts Introduced
*   **Abstraction**: Treating a complex pattern (Dot-Dash) as a simple object ("A").

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Function** with parameter (advanced) OR separate functions `flash_A()`, `flash_B()`.

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Functions**:
    *   `dot()`: ON 1u, OFF 1u.
    *   `dash()`: ON 3u, OFF 1u.
    *   `flash_A()`: dot(), dash().
*   **Main**:
    *   flash_C(), flash_A(), flash_B().

### 9️⃣ Execution Flow (Plain English)
The Pico spells "CAB" over and over.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
UNIT = 0.2

def dot():
    led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)

def dash():
    led.value(1); time.sleep(UNIT*3); led.value(0); time.sleep(UNIT)

def char_gap():
    time.sleep(UNIT*2)

while True:
    # C (-.-.)
    dash(); dot(); dash(); dot(); char_gap()
    # A (.-)
    dot(); dash(); char_gap()
    # B (-...)
    dash(); dot(); dot(); dot(); char_gap()
    
    time.sleep(UNIT*7) # Word gap
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Tedious**: Writing out every letter is slow. Project 100 solves this.

### 1️⃣2️⃣ Try This Next
*   **Name**: Spell your own name.

---

## 1️⃣ Project 0095: Interactive Morse Code (Decoder)
### 2️⃣ Learning Objective
Listening test. Pico flashes a letter. You identify it.

### 3️⃣ Concepts Introduced
*   **Pattern Recognition**: Identifying temporal data.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED** (Signal)
*   **Btn A** ("It was A"), **Btn B** ("It was B")

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn A** | GP10 |
| **Btn B** | GP11 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Random**
🔹 **If / Else**

### 7️⃣ Variables & State
*   **letter**

### 8️⃣ Block Logic
*   **Loop**:
    *   `letter` = Random(1, 2) (1=A, 2=B).
    *   IF 1: Flash ".-". ELSE: Flash "-...".
    *   Wait for Input.
    *   Check Correctness.

### 9️⃣ Execution Flow (Plain English)
Flash... Flash-Flash-Flash. (That was B!). Press Right Button. Correct!

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
led = machine.Pin(15, machine.Pin.OUT)
btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
UNIT = 0.2

def play(timings):
    for t in timings:
        led.value(1); time.sleep(t*UNIT); led.value(0); time.sleep(UNIT)

while True:
    choice = random.randint(0, 1)
    if choice == 0: # A (.-)
        play([1, 3])
    else: # B (-...)
        play([3, 1, 1, 1])
        
    # Wait input
    guess = -1
    while guess == -1:
        if btnA.value(): guess = 0
        if btnB.value(): guess = 1
        
    if guess == choice:
        print("Correct!")
    else:
        print("Wrong!")
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Memory**: Users forget the flash sequence instantly. Provide a cheat sheet.

### 1️⃣2️⃣ Try This Next
*   **Full Alphabet**: S (Short short short) vs O (Long long long).

---

## 1️⃣ Project 0096: Smart Morse Code Switch (Optical Link)
### 2️⃣ Learning Objective
Transmitter and Receiver logic. Only works if aligned.

### 3️⃣ Concepts Introduced
*   **Optical Comms**: Li-Fi basics.
*   **Analog Thresholding**: Detecting the "On" pulse.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED** (Sender)
*   **LDR** (Receiver) - Can be on same board for testing.

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |
| **LDR** | GP26 |

### 6️⃣ Blocks Used
🔹 **Read Analog**

### 7️⃣ Variables & State
*   **light_val**

### 8️⃣ Block Logic
*   **Tx**: Flash SOS loop.
*   **Rx**:
    *   Read LDR.
    *   IF Val < Threshold (Bright): Print "1".
    *   ELSE: Print "0".

### 9️⃣ Execution Flow (Plain English)
Data flows through light. The console prints "1010100011101110111000101010".

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import _thread

# Threading allows Tx and Rx simultaneous simulation
led = machine.Pin(15, machine.Pin.OUT)
ldr = machine.ADC(26)

def tx_thread():
    while True:
        # SOS
        for t in [1,1,1, 3,3,3, 1,1,1]:
            led.value(1); time.sleep(0.2); led.value(0); time.sleep(0.2 if t==1 else 0.6)
        time.sleep(2)

_thread.start_new_thread(tx_thread, ())

while True:
    val = ldr.read_u16()
    # Simple threshold
    if val < 40000: # Light detected
        print("1", end="")
    else:
        print("_", end="")
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Threading**: Advanced concept. Alternatively, use two Picos.

### 1️⃣2️⃣ Try This Next
*   **Decoding**: Write code to detect pulse duration and turn "111000" back into "S".

---

## 1️⃣ Project 0097: Morse Code Alarm System (Silent)
### 2️⃣ Learning Objective
Covert notification. Visual alarm instead of audio.

### 3️⃣ Concepts Introduced
*   **Stealth**: Interface design for discretion.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Trigger)
*   **RED LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Wait Until**

### 7️⃣ Variables & State
*   **triggered**

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button: `triggered` = True.
    *   IF `triggered`:
        *   Flash "H" (....)
        *   Flash "E" (.)
        *   Flash "L" (.-..)
        *   Flash "P" (.--.)

### 9️⃣ Execution Flow (Plain English)
Bank teller presses hidden panic button. Under the desk, the LED silently pleads for help.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
trig = False
UNIT = 0.2
def dot(): led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)
def dash(): led.value(1); time.sleep(UNIT*3); led.value(0); time.sleep(UNIT)

while True:
    if btn.value(): trig = True
    
    if trig:
        # H
        dot(); dot(); dot(); dot(); time.sleep(UNIT*2)
        # E
        dot(); time.sleep(UNIT*2)
        # L
        dot(); dash(); dot(); dot(); time.sleep(UNIT*2)
        # P
        dot(); dash(); dash(); dot(); time.sleep(UNIT*2)
        time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Locked Loop**: Once triggered, it never stops. This is usually intended for alarms.

### 1️⃣2️⃣ Try This Next
*   **Reset**: Add a secret combo to reset the alarm.

---

## 1️⃣ Project 0098: The Morse Code Game (Speed Typer)
### 2️⃣ Learning Objective
Reflex + Knowledge. System asks for "E". You must tap ".".

### 3️⃣ Concepts Introduced
*   **Reaction Limit**: Must answer within X seconds.

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
🔹 **Random**
🔹 **Timer**

### 7️⃣ Variables & State
*   **score**

### 8️⃣ Block Logic
*   **Loop**:
    *   Print "Dot".
    *   Wait 2s.
    *   Check if user tapped short.
    *   Print "Dash".
    *   Check if user tapped long.

### 9️⃣ Execution Flow (Plain English)
Console: "DOT!" User: *Tap*. Console: "DASH!" User: *Hold*.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    target = random.choice(["DOT", "DASH"])
    print(target)
    
    start = time.ticks_ms()
    duration = 0
    # Wait for press
    while time.ticks_diff(time.ticks_ms(), start) < 3000:
        if btn.value():
            # Measure hold time
            press_start = time.ticks_ms()
            while btn.value(): pass
            duration = time.ticks_diff(time.ticks_ms(), press_start)
            break
            
    if duration == 0:
        print("Too slow!")
    elif target == "DOT" and duration < 300:
        print("Success!")
    elif target == "DASH" and duration > 300:
        print("Success!")
    else:
        print("Fail! Duration was", duration)
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Timing**: Defining the line between Dot/Dash (e.g. 300ms) takes practice.

### 1️⃣2️⃣ Try This Next
*   **Letters**: Ask for "A". User must input "Dot-Space-Dash".

---

## 1️⃣ Project 0099: Automated Morse Code (Beacon)
### 2️⃣ Learning Objective
Periodic task. Run every 10 seconds. Sleep in between.

### 3️⃣ Concepts Introduced
*   **Low Power Design**: Sleeping when not active.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Sleep**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Flash ID (1 = .----).
    *   Sleep 10s.

### 9️⃣ Execution Flow (Plain English)
Flash...... (Sleep Zzz)...... Flash.....

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
UNIT = 0.2

while True:
    # 1 (.----)
    # Dot
    led.value(1); time.sleep(UNIT); led.value(0); time.sleep(UNIT)
    # 4 Dashes
    for i in range(4):
        led.value(1); time.sleep(UNIT*3); led.value(0); time.sleep(UNIT)
        
    print("Sleeping...")
    time.sleep(10)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Deep Sleep**: `time.sleep()` is not deep sleep, but it's the blocking simulation of it.

### 1️⃣2️⃣ Try This Next
*   **Counter**: Beacon "1", then "2", then "3"...

---

## 1️⃣ Project 0100: Mastering Morse Code (Translator)
### 2️⃣ Learning Objective
The Text-to-Speech engine of dots.

### 3️⃣ Concepts Introduced
*   **Dictionaries (Map)**: Key-Value pairs ('A': '.-').
*   **String Iteration**: Processing text char by char.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Dictionary** (Advanced)
🔹 **For Loop (String)**

### 7️⃣ Variables & State
*   **morse_code{}**

### 8️⃣ Block Logic
*   Define Dictionary `{'A': '.-', 'B': '-...', ...}`.
*   Text = "HELLO".
*   For `char` in `text`:
    *   Get code (e.g., "....").
    *   For `symbol` in `code`:
        *   If '.': Beep Short. If '-': Beep Long.
    *   Wait Letter Gap.

### 9️⃣ Execution Flow (Plain English)
Input "SOS". Output: BeepBeepBeep... BEEEBEEEBEEE... BeepBeepBeep.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
buzz = machine.Pin(15, machine.Pin.OUT)
UNIT = 0.1

morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '0': '-----'
}

text = "HELLO PICO 100"

for char in text:
    char = char.upper()
    if char in morse:
        code = morse[char]
        for symbol in code:
            buzz.value(1)
            if symbol == '.': time.sleep(UNIT)
            else: time.sleep(UNIT*3)
            buzz.value(0)
            time.sleep(UNIT) # Symbol gap
        time.sleep(UNIT*2) # Finish letter gap (total 3)
    elif char == " ":
        time.sleep(UNIT*4) # Word gap (total 7)
        
    print(char, end="")
print("\nDone.")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Unknown Chars**: !?# will crash if not in dict. Use `.get(char, '')` to skip safely.

### 1️⃣2️⃣ Try This Next
*   **Input**: Use `input()` to allow user to type messages in the console.

---
