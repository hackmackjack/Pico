# 🏁 Batch 1: Hello World & Digital Outputs (001-010)
*Focus: Logic, Loops, Wait, and GPIO Write.*

---

## 1️⃣ Project 001: Hello World
### 2️⃣ Learning Objective
Learn to use this feature with the Pico.

### 3️⃣ Concepts Introduced
*   Basic Electronics
*   Programming Logic

### 4️⃣ Hardware Required
*   Raspberry Pi Pico

### 5️⃣ Wiring / Interfaces
*   Standard Setup

### 6️⃣ Blocks Used

### 7️⃣ Variables & State
*   **val:** Generic variable for data.

### 8️⃣ Block Logic
1. Run Loop.
2. Do action.
3. Wait.

### 9️⃣ Execution Flow (Plain English)
The program runs in a continuous loop.

### 🔟 Generated Code (Reference Only)
```python
import time

# Initialize Hardware (Reference)
i2c = I2C(0, sda=Pin(0), scl=Pin(1)); oled = SSD1306_I2C(128, 64, i2c)

# Main Logic (See Block Logic)
while True:
    # Logic from Section 8
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes
*   **Console Hidden**: Forgetting to open the Serial Console/Repl view to see the output.
*   **Text Errors**: Trying to print a variable name instead of a "String" (forgetting quotes).

### 1️⃣2️⃣ Try This Next
*   **Personalize**: Change the text to say "Hello [Your Name]".
*   **Story**: Use three log blocks to tell a short 3-line story with delays between them.

---



## 1️⃣ Project 002: Toggle Logic (Latch)
### 2️⃣ Learning Objective
Create a 'Toggle Switch' behavior using a momentary button.

### 3️⃣ Concepts Introduced
*   Latching Logic
*   Variables
*   State Memory

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   LED (GP15)

### 5️⃣ Wiring / Interfaces
*   Button One Side -> GP14
*   Button Other Side -> 3.3V
*   LED Anode -> GP15
*   LED Cathode -> GND

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic
*   **Block:** `If [Button] then...`
🔹 **Set Variable**
*   **Category:** Variables
*   **Block:** `set [state] to [not state]`
🔹 **Set Pin**
*   **Category:** Pico GPIO
*   **Block:** `set Pin [15] to [state]`
🔹 **Wait Until**
*   **Category:** Control
*   **Block:** `wait until [not Button]`

### 7️⃣ Variables & State
*   state: Boolean (True/False) to remember if LED is ON or OFF.

### 8️⃣ Block Logic
1. **Initialization**: Set `state` to False.
2. **Main Loop**:
    *   **Check Input**: IF Button (GP14) is PRESSED:
        *   **Toggle**: Set `state` = NOT `state`.
        *   **Output**: distinct Set LED (GP15) to `state`.
        *   **Debounce/Wait**: Wait until Button is RELEASED (to prevent rapid toggling).
    *   **Wait**: Small delay (0.01s).

### 9️⃣ Execution Flow (Plain English)
The distinct feature here is the 'Latch'. We don't just turn the LED on *while* the button is held. Instead, when we detect a press, we flip the value of our `state` variable. We then wait for the user to let go of the button so we don't flip it back immediately.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

state = False

while True:
    if btn.value() == 1:
        state = not state      # Toggle
        led.value(state)       # Update LED
        
        # Wait for release (Primitive Debounce)
        while btn.value() == 1:
            time.sleep(0.01)
            
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wiring**: Check polarity.

### 1️⃣2️⃣ Try This Next
*   Add a second button.

---


## 1️⃣ Project 003: Counter Loop
### 2️⃣ Learning Objective
Count how many times a button has been pressed and display it.

### 3️⃣ Concepts Introduced
*   Incrementing
*   Variables
*   Serial Output

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)

### 5️⃣ Wiring / Interfaces
*   Button -> GP14
*   Button -> 3.3V

### 6️⃣ Blocks Used
🔹 **Change Variable**
*   **Category:** Variables
*   **Block:** `change [count] by [1]`
🔹 **Print**
*   **Category:** Text
*   **Block:** `print [count]`
🔹 **Wait Utnil**
*   **Category:** Control
*   **Block:** `wait until [not Button]`

### 7️⃣ Variables & State
*   count: Integer to store the number of presses.

### 8️⃣ Block Logic
1. **Init**: Set `count` = 0.
2. **Loop**:
    *   IF Button is PRESSED:
        *   Add 1 to `count`.
        *   Print `count` to Console.
        *   Wait until Button is RELEASED.

### 9️⃣ Execution Flow (Plain English)
Each time you click, the variable increases by one. We use the 'Wait Until Not Button' block to ensure one click equals exactly one number count.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

while True:
    if btn.value() == 1:
        count += 1
        print("Count:", count)
        
        while btn.value() == 1:
            time.sleep(0.01)
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wiring**: Check polarity.

### 1️⃣2️⃣ Try This Next
*   Add a second button.

---


## 1️⃣ Project 004: Random Decision Maker
### 2️⃣ Learning Objective
Use randomness to make a Yes/No decision (Coin Toss).

### 3️⃣ Concepts Introduced
*   Random Numbers
*   Boolean Logic
*   Probability

### 4️⃣ Hardware Required
*   Pico
*   Button (GP14)
*   Red LED (GP15)
*   Green LED (GP16)

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   Red LED -> GP15
*   Green LED -> GP16

### 6️⃣ Blocks Used
🔹 **Random Integer**
*   **Category:** Math
*   **Block:** `random integer from [0] to [1]`
🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `if [val] = [1] do... else...`

### 7️⃣ Variables & State
*   decision: Integer (0 or 1).

### 8️⃣ Block Logic
1. **Loop**:
    *   IF Button Pressed:
        *   Set `decision` to Random(0, 1).
        *   IF `decision` == 1:
            *   Turn Green LED ON, Red OFF.
            *   Print "YES".
        *   ELSE:
            *   Turn Red LED ON, Green OFF.
            *   Print "NO".
        *   Wait 1 second (for drama).
        *   Turn both OFF.

### 9️⃣ Execution Flow (Plain English)
The computer picks a number. Since we only pick 0 or 1, it's a 50/50 chance, just like a coin flip.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_green = machine.Pin(16, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)

while True:
    if btn.value() == 1:
        # Drama
        led_green.value(0)
        led_red.value(0)
        time.sleep(0.3)
        
        decision = random.randint(0, 1)
        
        if decision == 1:
            led_green.value(1)
            print("YES")
        else:
            led_red.value(1)
            print("NO")
            
        time.sleep(1)
        led_green.value(0)
        led_red.value(0)
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wiring**: Check polarity.

### 1️⃣2️⃣ Try This Next
*   Add a second button.

---


## 1️⃣ Project 005: Simple State Machine
### 2️⃣ Learning Objective
Cycle through different modes (Off -> Low -> High -> Off) with one button.

### 3️⃣ Concepts Introduced
*   State Machines
*   Modulo Math
*   Modes

### 4️⃣ Hardware Required
*   Pico
*   Button (GP14)
*   LED (GP15)

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14
*   LED -> GP15

### 6️⃣ Blocks Used
🔹 **Change Variable**
*   **Category:** Variables
*   **Block:** `change [mode] by [1]`
🔹 **If**
*   **Category:** Logic
*   **Block:** `if [mode] > [2] set [mode] to [0]`

### 7️⃣ Variables & State
*   mode: 0, 1, or 2.

### 8️⃣ Block Logic
1. **Init**: Mode = 0.
2. **Loop**:
    *   IF Button Pressed:
        *   Mode = Mode + 1.
        *   IF Mode > 2: Mode = 0.
        *   Wait until Released.
    *   **Output Handler**:
        *   IF Mode == 0: LED Off.
        *   IF Mode == 1: LED Blink Slow.
        *   IF Mode == 2: LED On.

### 9️⃣ Execution Flow (Plain English)
We separate the 'Input' (changing the mode) from the 'Output' (what the LEDs do). This is the foundation of clean archiitecture.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
mode = 0

while True:
    # Input
    if btn.value() == 1:
        mode += 1
        if mode > 2:
            mode = 0
        print("Mode:", mode)
        while btn.value() == 1: time.sleep(0.01) # Wait release
        
    # Output
    if mode == 0:
        led.value(0)
    elif mode == 1:
        led.toggle()
        time.sleep(0.1) # Fast blink
    elif mode == 2:
        led.value(1)
        
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wiring**: Check polarity.

### 1️⃣2️⃣ Try This Next
*   Add a second button.

---


## 1️⃣ Project 006: Debounce Logic (Soft)
### 2️⃣ Learning Objective
Fix 'bouncy' buttons using software timers.

### 3️⃣ Concepts Introduced
*   Signal Noise
*   Debouncing
*   Timing

### 4️⃣ Hardware Required
*   Pico
*   Button (GP14)

### 5️⃣ Wiring / Interfaces
*   Btn -> GP14

### 6️⃣ Blocks Used
🔹 **Wait**
*   **Category:** Control
*   **Block:** `wait [0.05] seconds`
🔹 **If**
*   **Category:** Logic
*   **Block:** `if [Button] (Check Again)`

### 7️⃣ Variables & State
*   None

### 8️⃣ Block Logic
1. **Loop**:
    *   IF Button Pressed:
        *   Wait 50ms (Let signal settle).
        *   IF Button STILL Pressed:
            *   Register Valid Click.
            *   Print 'Click'.

### 9️⃣ Execution Flow (Plain English)
Mechanical buttons vibrate when pressed, creating multiple fake signals in milliseconds. By waiting a tiny bit and checking again, we ignore the noise.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        time.sleep(0.05) # Debounce Time
        if btn.value() == 1:
            print("Valid Click")
            while btn.value() == 1: pass # Wait for release
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wiring**: Check polarity.

### 1️⃣2️⃣ Try This Next
*   Add a second button.

---


## 1️⃣ Project 007: Sequence Timer
### 2️⃣ Learning Objective
Learn to create timed sequences using loops and delays to control multiple outputs.

### 3️⃣ Concepts Introduced
*   Sequential Logic
*   Timing Control
*   Pattern Creation
*   Loop Counters

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   3x LEDs (Red on GP15, Yellow on GP16, Green on GP17)
*   3x 220Ω Resistors

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground |

### 6️⃣ Blocks Used
🔹 **Forever Loop**
*   **Category:** Loops
*   **Block:** `forever do`

🔹 **Set Pin**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH/LOW]`

🔹 **Wait**
*   **Category:** Smart IO  
*   **Block:** `wait [1] [seconds]`

🔹 **Log/Print**
*   **Category:** Smart IO
*   **Block:** `log/print [message]`

### 7️⃣ Variables & State
*   **None required** (uses direct sequential control)

### 8️⃣ Block Logic

**A. Initialization Phase**
*   None required (LEDs initialize to LOW)

**B. Main Loop Phase**
1. Print "Sequence Start"
2. Turn Red LED ON (GP15 HIGH)
3. Wait 1 second
4. Turn Red LED OFF (GP15 LOW)
5. Turn Yellow LED ON (GP16 HIGH)
6. Wait 1 second
7. Turn Yellow LED OFF (GP16 LOW)
8. Turn Green LED ON (GP17 HIGH)
9. Wait 1 second
10. Turn Green LED OFF (GP17 LOW)
11. Wait 2 seconds (pause between sequences)
12. Loop repeats

**C. Event / Condition Handling**
*   None (pure time-based sequence)

### 9️⃣ Execution Flow (Plain English)
The program creates a traffic light-like sequence that repeats forever. Each LED lights up for exactly 1 second before the next one activates. After all three LEDs have flashed, there's a 2-second pause before the sequence restarts. This demonstrates precise timing control.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

while True:
    print('Sequence Start')
    Pin(15, Pin.OUT).value(1)
    time.sleep(1)
    Pin(15, Pin.OUT).value(0)
    Pin(16, Pin.OUT).value(1)
    time.sleep(1)
    Pin(16, Pin.OUT).value(0)
    Pin(17, Pin.OUT).value(1)
    time.sleep(1)
    Pin(17, Pin.OUT).value(0)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes
*   **Wrong Pin Numbers**: Ensure LEDs are on GP15, GP16, GP17 (not GP25 which is the onboard LED).
*   **Resistor Values**: Using incorrect resistor values (too low) can damage LEDs.
*   **Cathode/Anode Confusion**: LEDs won't light if connected backwards.
*   **Timing Issues**: Make sure to use `sleep` (seconds) not `sleep_ms` if using the standard wait block.

### 1️⃣2️⃣ Try This Next
*   **Speed Control**: Add a button to switch between fast (0.5s) and slow (2s) sequences.
*   **Reverse Sequence**: Make the lights flash in reverse order (Green → Yellow → Red).
*   **Christmas Lights**: Add more LEDs and create alternating patterns (odd/even flashing).

---

## 1️⃣ Project 008: Password Check
### 2️⃣ Learning Objective
Implement basic security logic using button patterns to create a simple password system.

### 3️⃣ Concepts Introduced
*   Pattern Matching
*   String Comparison
*   Security Logic
*   User Input Validation
*   Feedback Systems

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   Green LED (GP16) - Access Granted
*   Red LED (GP15) - Access Denied
*   2x 220Ω Resistors

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button One Terminal** | GP14 | Internal pull-down enabled |
| **Button Other Terminal** | 3.3V | Power rail |
| **Green LED Anode** | GP16 | Via 220Ω Resistor |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Both LED Cathodes** | GND | Common Ground |

### 6️⃣ Blocks Used
🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [password] to [1 2 3]`

🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [input] to [empty text]`

🔹 **Read Digital Pin**
*   **Category:** Smart IO
*   **Block:** `read [Digital] Pin [14]`

🔹 **Text Join**
*   **Category:** Text
*   **Block:** `create text with [input] [1]`

🔹 **Compare**
*   **Category:** Logic
*   **Block:** `[input] = [password]`

🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `if [condition] then... else...`

🔹 **Wait**
*   **Category:** Smart IO
*   **Block:** `wait [0.3] [seconds]`

### 7️⃣ Variables & State
*   **password**: String - Stores the correct pattern ("123")
*   **input**: String - Accumulates button presses (starts empty)
*   **presses**: Number - Counts button clicks (0-3)

### 8️⃣ Block Logic

**A. Initialization Phase**
1. Set `password` to "123"
2. Set `input` to "" (empty string)
3. Set `presses` to 0
4. Print "Enter 3-digit code"

**B. Main Loop Phase**
1. **Forever do:**
   - Check if Button (GP14) is pressed
   - IF pressed:
     - Add "1" to `input` string
     - Increment `presses` by 1
     - Print current `input`
     - Wait until button released
     - Wait 0.3s (debounce)

**C. Event / Condition Handling**
1. **After 3 presses:**
   - IF `input` equals `password`:
     - Turn Green LED ON (GP16)
     - Print "ACCESS GRANTED"
     - Wait 2 seconds
     - Turn Green LED OFF
   - ELSE:
     - Turn Red LED ON (GP15)
     - Print "ACCESS DENIED"
     - Wait 2 seconds
     - Turn Red LED OFF
   - Reset `input` to ""
   - Reset `presses` to 0

### 9️⃣ Execution Flow (Plain English)
The program waits for the user to press a button 3 times. Each press adds a "1" to the input string. After 3 presses, it compares the input ("111", "11", etc.) to the password ("123"). If they match, a green LED lights up for 2 seconds. If they don't match, a red LED warns of failed access. The system then resets for another attempt.

**Note**: This simplified version only detects presses, not patterns. A real password would use multiple buttons or timing to distinguish digits.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
password = "123"
input_str = ""
presses = 0

print("Enter 3-digit code")

while True:
    if btn.value() == 1:
        input_str += "1"
        presses += 1
        print("Input:", input_str)
        
        # Wait for button release
        while btn.value() == 1:
            time.sleep(0.01)
        time.sleep(0.3)  # Debounce
        
        # Check after 3 presses
        if presses >= 3:
            if input_str == password:
                Pin(16, Pin.OUT).value(1)  # Green LED
                print("ACCESS GRANTED")
                time.sleep(2)
                Pin(16, Pin.OUT).value(0)
            else:
                Pin(15, Pin.OUT).value(1)  # Red LED
                print("ACCESS DENIED")
                time.sleep(2)
                Pin(15, Pin.OUT).value(0)
            
            # Reset
            input_str = ""
            presses = 0
            print("Enter 3-digit code")
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes
*   **Button Pull Resistor**: Forgetting to enable pull-down causes random readings.
*   **String vs Number**: Comparing "123" (string) to 123 (number) will always fail.
*   **Debounce Missing**: Without debounce delay, one press = multiple registrations.
*   **LED Polarity**: Red and Green LEDs may have different forward voltages.

### 1️⃣2️⃣ Try This Next
*   **Multiple Buttons**: Use 3 different buttons for digits 1, 2, 3 to create real patterns.
*   **Timeout Feature**: Reset input if 5 seconds pass between presses.
*   **Lockout Mode**: After 3 failed attempts, disable system for 30 seconds.
*   **Secret Knock**: Use timing between presses as the password (rhythm-based).

---

## 1️⃣ Project 009: Reaction Game
### 2️⃣ Learning Objective
Measure human reaction time by tracking the delay between a stimulus (LED) and response (button press).

### 3️⃣ Concepts Introduced
*   Time Measurement
*   Millisecond Precision
*   Random Delays
*   Performance Metrics
*   Timestamp Arithmetic

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   LED (GP15)
*   220Ω Resistor

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button One Terminal** | GP14 | Internal pull-down enabled |
| **Button Other Terminal** | 3.3V | Power rail |
| **LED Anode** | GP15 | Via 220Ω Resistor |
| **LED Cathode** | GND | Ground |

### 6️⃣ Blocks Used
🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [startTime] to [0]`

🔹 **Math - Random**
*  **Category:** Math
*   **Block:** `random integer from [2] to [5]`

🔹 **Wait**
*   **Category:** Smart IO
*   **Block:** `wait [random delay] [seconds]`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH/LOW]`

🔹 **Time Function**
*   **Category:** Math (or create custom)
*   **Note:** Use Python `time.ticks_ms()` in code block

🔹 **GPIO Read**
*   **Category:** Smart IO
*   **Block:** `read [Digital] Pin [14]`

🔹 **Wait Until**
*   **Category:** Loops
*   **Block:** `wait until [Button Pressed]`

🔹 **Math - Subtraction**
*   **Category:** Math
*   **Block:** `[endTime] - [startTime]`

🔹 **Print**
*   **Category:** Smart IO
*   **Block:** `log/print [message]`

### 7️⃣ Variables & State
*   **startTime**: Number (milliseconds) - Records when LED turns on
*   **endTime**: Number (milliseconds) - Records when button is pressed
*   **reactionTime**: Number (milliseconds) - Calculated difference
*   **waitDelay**: Number (seconds) - Random delay before LED (2-5s)

### 8️⃣ Block Logic

**A. Initialization Phase**
1. Print "Reaction Time Game - Press button when LED lights!"
2. Set `startTime` to 0
3. Set `reactionTime` to 0

**B. Main Loop Phase**
1. **Forever do:**
   - Print "Get ready..."
   - Generate random delay: 2-5 seconds
   - Wait for that random duration
   - Turn LED ON (GP15 HIGH)
   - Record `startTime` = current time in milliseconds
   - Wait until Button (GP14) is pressed
   - Record `endTime` = current time in milliseconds
   - Turn LED OFF (GP15 LOW)
   
**C. Event / Condition Handling**
1. **Calculate Reaction Time:**
   - `reactionTime` = `endTime` - `startTime`
   - Print "Your reaction time:" + `reactionTime` + "ms"
   - Wait 2 seconds before next round

### 9️⃣ Execution Flow (Plain English)
The game starts with a random wait period (2-5 seconds) to prevent anticipation. Once the LED lights up, the system records the exact millisecond timestamp. It then waits for the user to press the button. When pressed, it calculates the difference between button press time and LED-on time, showing the user's reaction speed in milliseconds. A typical human reaction time is 200-300ms.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time
import random

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

print("Reaction Time Game - Press button when LED lights!")

while True:
    print("Get ready...")
    
    # Random delay to prevent anticipation
    wait_delay = random.randint(2, 5)
    time.sleep(wait_delay)
    
    # Turn on LED and start timer
    led.value(1)
    start_time = time.ticks_ms()
    
    # Wait for button press
    while btn.value() == 0:
        time.sleep(0.001)  # Small delay to prevent CPU overload
    
    # Record end time and turn off LED
    end_time = time.ticks_ms()
    led.value(0)
    
    # Calculate and display reaction time
    reaction_time = time.ticks_diff(end_time, start_time)
    print(f"Your reaction time: {reaction_time} ms")
    
    # Provide feedback
    if reaction_time < 200:
        print("Amazing! Pro reflexes!")
    elif reaction_time < 300:
        print("Excellent!")
    elif reaction_time < 500:
        print("Good job!")
    else:
        print("Keep practicing!")
    
    time.sleep(2)  # Pause before next round
```

### 1️⃣1️⃣ Common Mistakes
*   **Timer Overflow**: Use `time.ticks_diff()` instead of simple subtraction to handle timer rollover.
*   **No Random Delay**: Without randomization, users learn to anticipate and cheat.
*   **Button Held Down**: System should wait for button release before starting next round.
*   **Units Confusion**: Mixing seconds and milliseconds (1000ms = 1s).

### 1️⃣2️⃣ Try This Next
*   **Best Score Tracker**: Store and display the fastest reaction time achieved.
*   **Average Calculator**: Measure 5 attempts and show average performance.
*   **False Start Detection**: If button pressed before LED turns on, show "FALSE START!".
*   **Difficulty Levels**: Flash LED multiple times, user must press on specific flash.
*   **Two-Player Mode**: Two buttons, two LEDs - first to press wins!

---

## 1️⃣ Project 010: Morse Code
### 2️⃣ Learning Objective
Transmit the international distress signal (SOS) using Morse code with an LED, learning about communication protocols.

### 3️⃣ Concepts Introduced
*   Morse Code Standards
*   Communication Protocols
*   Timing Patterns
*   Loop-Based Sequences
*   International Standards (ITU)

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   LED (GP15)
*   220Ω Resistor

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Anode** | GP15 | Via 220Ω Resistor |
| **LED Cathode** | GND | Ground |

###  6️⃣ Blocks Used
🔹 **Forever Loop**
*   **Category:** Loops
*   **Block:** `forever do`

🔹 **Repeat**
*   **Category:** Loops
*   **Block:** `repeat [3] times`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH/LOW]`

🔹 **Wait**
*   **Category:** Smart IO
*   **Block:** `wait [0.2] [seconds]`

🔹 **Print**
*   **Category:** Smart IO
*   **Block:** `log/print ["S" or "O"]`

### 7️⃣ Variables & State
*   **UNIT**: Constant = 0.2 seconds (base timing unit for dots/dashes)
*   **DOT_TIME**: 1 UNIT (0.2s)
*   **DASH_TIME**: 3 UNITs (0.6s)
*   **SYMBOL_GAP**: 1 UNIT (0.2s between dots/dashes in same letter)
*   **LETTER_GAP**: 3 UNITs (0.6s between letters)
*   **WORD_GAP**: 7 UNITs (1.4s between words)

### 8️⃣ Block Logic

**A. Initialization Phase**
*   None required (LED starts OFF)

**B. Main Loop Phase**
1. **Forever do:**
   
   **First 'S' (dot-dot-dot):**
   - Repeat 3 times:
     - LED ON
     - Wait 0.2s (dot duration)
     - LED OFF
     - Wait 0.2s (symbol gap)
   - Wait 0.4s (letter gap = 3 units - 1 already waited)
   - Print "S"
   
   **'O' (dash-dash-dash):**
   - Repeat 3 times:
     - LED ON
     - Wait 0.6s (dash duration)
     - LED OFF
     - Wait 0.2s (symbol gap)
   - Wait 0.4s (letter gap)
   - Print "O"
   
   **Second 'S' (dot-dot-dot):**
   - Same as first S
   - Wait 1.4s (word gap before repeating SOS)

**C. Event / Condition Handling**
*   None (automatic continuous transmission)

### 9️⃣ Execution Flow (Plain English)
The program continuously transmits the SOS distress signal in Morse code. Morse code uses dots (short flashes) and dashes (long flashes) to represent letters:
- **S** = three dots (· · ·)
- **O** = three dashes (– – –)
- **S** = three dots (· · ·)

Each dot lasts 0.2 seconds, each dash lasts 0.6 seconds (3x dot length). There's a 0.2s gap between symbols within a letter, 0.6s between letters, and 1.4s before repeating the message.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

led = Pin(15, Pin.OUT)

# Morse Code Timing (ITU Standard)
UNIT = 0.2  # Base timing unit in seconds

def dot():
    """Transmit a Morse code dot"""
    led.value(1)
    time.sleep(UNIT)
    led.value(0)
    time.sleep(UNIT)  # Gap between symbols

def dash():
    """Transmit a Morse code dash"""
    led.value(1)
    time.sleep(UNIT * 3)
    led.value(0)
    time.sleep(UNIT)  # Gap between symbols

def letter_S():
    """Transmit letter S: dot-dot-dot"""
    for _ in range(3):
        dot()
    time.sleep(UNIT * 2)  # Letter gap (total 3 units, 1 already waited)
    print("S")

def letter_O():
    """Transmit letter O: dash-dash-dash"""
    for _ in range(3):
        dash()
    time.sleep(UNIT * 2)  # Letter gap
    print("O")

def transmit_SOS():
    """Transmit complete SOS signal"""
    letter_S()
    letter_O()
    letter_S()
    time.sleep(UNIT * 7)  # Word gap

print("Transmitting SOS in Morse Code...")
print("S = dot-dot-dot | O = dash-dash-dash")

while True:
    transmit_SOS()
```

### 1️⃣1️⃣ Common Mistakes
*   **Timing Ratios Wrong**: Dash MUST be exactly 3x dot length (ITU standard).
*   **Missing Gaps**: Forgetting gaps between symbols makes letters unreadable.
*   **Too Fast**: Standard Morse speed is ~20 words/minute; slower is better for learning.
*   **LED Resistor**: Omitting resistor can damage LED or Pico pin.

### 1️⃣2️⃣ Try This Next
*   **Full Alphabet**: Implement all 26 letters A-Z in Morse code (use lists/dictionaries).
*   **Text Input**: User types message, Pico transmits it in Morse.
*   **Receive Mode**: Use LDR sensor to detect Morse flashes and decode them.
*   **Audio Version**: Replace LED with piezo buzzer for sound-based Morse.
*   **Adjustable Speed**: Add button to switch between slow (beginners) and fast (experts) transmission.
*   **Learn Mode**: Display dot/dash pattern on LCD while transmitting.

---

