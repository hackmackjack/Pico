## 1️⃣ Project 0291: Full Alphabet Encoder

### 2️⃣ Learning Objective
Turn text strings into Morse Code sequences, handling the complete A-Z alphabet using a dictionary lookup.

### 3️⃣ Concepts Introduced
*   Dictionaries (Key-Value Pairs)
*   String Iteration
*   Data Encoding
*   Lookup Tables
*   Buzzer Control (PWM)

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   LED
*   Buzzer

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |
| **Buzzer** | GP14 |

### 6️⃣ Blocks Used
🔹 **Dictionary / Map**
🔹 **For Loop (String)**
🔹 **Wait (Time)**
🔹 **Pin (Output)**

### 7️⃣ Variables
*   **MORSE_CODE**: Dictionary mapping letters to dot-dash strings.
*   **message**: The string variable holding the text to encode.
*   **char**: The current character being processed in the loop.

### 8️⃣ Step-by-Step Guide
1. Create Dictionary `MORSE_CODE` with 'A'-'Z' mappings.
2. Define variable `message` with the text to send (e.g., "HELLO").
3. Loop through each `char` in `message`.
4. Validate if `char` exists in Dictionary.
5. If yes, call `flash_char()` to pulse LED/Buzzer based on dots/dashes.
6. Wait 0.6 seconds (Letter Gap) to separate characters.

### 9️⃣ Execution Flow
1. **Start**: Initialize hardware (LED, Buzzer) and Dictionary.
2. **Input**: Hardcoded string or User Input.
3. **Process**: Iterate string -> Lookup conversion -> Generate Signals.
4. **End**: Message transmission complete.

### 10️⃣ Generated Code
```python
from machine import Pin, PWM
import time

led = Pin(15, Pin.OUT)
buzzer = PWM(Pin(14))

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
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        
        if symbol == '.':
            time.sleep(0.2)
        elif symbol == '-':
            time.sleep(0.6)
            
        led.off()
        buzzer.duty_u16(0)
        time.sleep(0.2) # Intra-char gap

message = "HELLO PICO"
for char in message:
    if char in MORSE_CODE:
        flash_char(MORSE_CODE[char])
        time.sleep(0.6) # Letter gap
```

### 11️⃣ Common Mistakes
*   **Timing Off**: Not waiting long enough between letters allows them to blend into one long mess.
*   **Case Sensitivity**: Python dictionaries are case-sensitive. "a" is not "A". Always `.upper()` your input.

### 12️⃣ Try This Next
*   **Add Numbers**: Extend the dictionary to include 0-9.
*   **Input Mode**: Change the `message` variable to use `input()` so you can type any text.

---
### ✅ Audit Status
- Standard Version: v1.2.0
- Schema Check: PASS
- Code ↔ Wiring: PASS
- Hardware Match: PASS
- Last Reviewed: 2025-12-21
---
