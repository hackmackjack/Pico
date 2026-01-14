# 📘 Pico 2500: Batch 30 - Morse Code 2 (Projects 0291-0300)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Apply  
**Theme:** Communication, Encoding & Decoding

---

## 1️⃣ Project 0291: Full Alphabet Encoder

### 2️⃣ Learning Objective
Turn text strings into Morse Code sequences, handling the complete A-Z alphabet using a dictionary lookup.

### 3️⃣ Concepts Introduced
*   Dictionaries (Key-Value Pairs)
*   String Iteration
*   Data Encoding
*   Lookup Tables

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   LED (GP15)
*   Buzzer (GP14)

### 8️⃣ Step-by-Step Guide
**Logic:**
1. Define `MORSE_CODE = {'A': '.-', 'B': '-...', ...}`
2. Function `encode(text)`:
   - For each char in text:
     - Find code in dictionary.
     - Flash/Beep the code.

### 10️⃣ Generated Code
```python
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

def flash_char(code):
    for symbol in code:
        led.on()
        if symbol == '.':
            time.sleep(0.2)
        elif symbol == '-':
            time.sleep(0.6)
        led.off()
        time.sleep(0.2) # Intra-char gap

message = "HELLO PICO"
for char in message:
    if char in MORSE_CODE:
        flash_char(MORSE_CODE[char])
        time.sleep(0.6) # Letter gap
```

---

## 1️⃣ Project 0292: Morse Decoder (Input)

### 2️⃣ Learning Objective
Translate physical button presses *back* into letters by measuring how long the button is held.

### 3️⃣ Concepts Introduced
*   Pulse Width Measurement
*   Thresholding (Short vs Long)
*   Input Decoding
*   Reverse Lookup

### 8️⃣ Step-by-Step Guide
**Logic:**
1. If Button Pressed: Record `start`.
2. On Release: `duration = now - start`.
3. If duration < 200ms: Dot.
4. If duration > 200ms: Dash.
5. If silence > 1000ms: End of Letter -> Decode.

### 10️⃣ Generated Code
```python
current_symbol = ""

while True:
    if btn.value():
        start = time.ticks_ms()
        while btn.value(): pass # Wait release
        duration = time.ticks_diff(time.ticks_ms(), start)
        
        if duration < 250:
            current_symbol += "."
            print(".", end="")
        else:
            current_symbol += "-"
            print("-", end="")
            
        last_press = time.ticks_ms()
        
    # Timeout check for end of letter
    if len(current_symbol) > 0 and \
       time.ticks_diff(time.ticks_ms(), last_press) > 1000:
           # Find letter in dictionary (reverse search)
           found = False
           for letter, code in MORSE_CODE.items():
               if code == current_symbol:
                   print(f" [{letter}]")
                   found = True
                   break
           if not found: print(" ?")
           current_symbol = ""
```

---

## 1️⃣ Project 0293: International Standards (Timing)

### 2️⃣ Learning Objective
Refine timing to strict International Morse Code standards (1 unit = dot, 3 units = dash, 7 units = word gap).

### 3️⃣ Concepts Introduced
*   Standardization
*   Unit Time
*   Precise Timing

### 10️⃣ Generated Code
```python
UNIT = 0.1 # Seconds (Speed base)

def play(code):
    for symbol in code:
        led.on()
        if symbol == '.': time.sleep(UNIT)
        else: time.sleep(UNIT * 3)
        led.off()
        time.sleep(UNIT) # Inter-element gap
```

---

## 1️⃣ Project 0294: Light & Sound Sync

### 2️⃣ Learning Objective
Synchronize an LED flash and a Buzzer tone perfectly so they start and stop at the exact same instant.

### 10️⃣ Generated Code
```python
def signal_on():
    led.value(1)
    buzzer.duty_u16(32768)

def signal_off():
    led.value(0)
    buzzer.duty_u16(0)

# Use these functions inside the loop
```

---

## 1️⃣ Project 0295: Message Queue System

### 2️⃣ Learning Objective
Type a long message into the Python console (input), store it, and then transmit it automatically.

### 3️⃣ Concepts Introduced
*   Input Buffers
*   Queues
*   Asynchronous Processing

### 10️⃣ Generated Code
```python
# Non-blocking check for input? 
# MicroPython input() blocks. 
# We'll stick to blocking input for simplicity.

msg = input("Type message to send: ").upper()
print(f"Sending: {msg}")
send_morse(msg) # Uses logic from 0291
print("Done.")
```

---

## 1️⃣ Project 0296: Morse Keyboard Input

### 2️⃣ Learning Objective
Use two buttons: Button A for Dot, Button B for Dash. This is faster than one button.

### 3️⃣ Concepts Introduced
*   Twin-Paddle Keyer Logic
*   iambic Keying (Advanced)

### 10️⃣ Generated Code
```python
if btn_dot.value():
    current_symbol += "."
    play_sound(DOT_LEN)

if btn_dash.value():
    current_symbol += "-"
    play_sound(DASH_LEN)
```

---

## 1️⃣ Project 0297: Variable Speed (WPM)

### 2️⃣ Learning Objective
Add a potentiometer to adjust the transmission speed (Words Per Minute) in real-time.

### 10️⃣ Generated Code
```python
wpm_pot = ADC(Pin(26))

def get_unit_time():
    # Map 0-65535 to 5-30 WPM
    wpm = 5 + (wpm_pot.read_u16() / 65535) * 25
    # Standard formula: T = 1200 / WPM (ms)
    unit = 1.2 / wpm 
    return unit

# Use get_unit_time() in loops
```

---

## 1️⃣ Project 0298: Training Game

### 2️⃣ Learning Objective
The Pico flashes a random letter. The user must guess it (Type it or check a chart).

### 3️⃣ Concepts Introduced
*   Educational Tools
*   Random Selection
*   Drills

### 10️⃣ Generated Code
```python
letters = list(MORSE_CODE.keys())
target = random.choice(letters)

print("Guess the letter...")
play_morse(MORSE_CODE[target])

guess = input("What was it? ").upper()
if guess == target:
    print("Correct!")
else:
    print(f"Wrong. It was {target}")
```

---

## 1️⃣ Project 0299: Wireless Chat (UART)

### 2️⃣ Learning Objective
Connect two Picos via wires (TX/RX). Typing on one PC makes the other Pico flash/beep.

### 3️⃣ Concepts Introduced
*   UART Communication
*   Telegraphy

### 10️⃣ Generated Code
```python
uart = UART(0, 9600)

while True:
    if uart.any():
        char = uart.read(1).decode().upper()
        if char in MORSE_CODE:
            play(MORSE_CODE[char])
```

---

## 1️⃣ Project 0300: Morse Communication Station

### 2️⃣ Learning Objective
The Final Project for Level 2. A complete "Telegraph Station".

### 3️⃣ Features
1. **Mode:** Send (Key) or Receive (Decode).
2. **Speed:** Adjustable WPM.
3. **Display:** Shows decoded text on LCD/OLED.
4. **Network:** Connects to other stations.

### 10️⃣ Summary
Combines:
- Decoder Logic (0292)
- Display Logic (Previous batches)
- Tuning Pot (0297)
- Dual-Paddle Input (0296)

---

**Batch 30 Complete & Fixed.**
