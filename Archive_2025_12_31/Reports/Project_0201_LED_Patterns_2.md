# 🏁 Batch 21: LED Patterns 2 (0201-0210)
*Focus: Advanced LED Control, Pattern Variables, Multi-LED Sequences*

---

## 1️⃣ Project 0201: Introduction to LED Patterns (Level 2)

### 2️⃣ Learning Objective
Learn to create dynamic LED patterns using variables to control timing and sequences, building on basic GPIO control from Batch 1.

### 3️⃣ Concepts Introduced
*   Variable-Controlled Timing
*   Pattern Sequencing
*   Multi-LED Coordination
*   Loop-Based Animation
*   Speed Control Variables

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x LEDs (Red on GP15, Yellow on GP16, Green on GP17, Blue on GP18)
*   4x 220Ω Resistors
*   Breadboard
*   Jumper Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED Anode** | GP15 | Via 220Ω Resistor |
| **Yellow LED Anode** | GP16 | Via 220Ω Resistor |
| **Green LED Anode** | GP17 | Via 220Ω Resistor |
| **Blue LED Anode** | GP18 | Via 220Ω Resistor |
| **All LED Cathodes** | GND | Common Ground Rail |

### 6️⃣ Blocks Used

🔹 **Create Variable**
*   **Category:** Variables
*   **Block:** `set [speed] to [0.3]`

🔹 **Forever Loop**
*   **Category:** Loops
*   **Block:** `forever do`

🔹 **Repeat Loop**
*   **Category:** Loops
*   **Block:** `repeat [4] times`

🔹 **GPIO Write**
*   **Category:** Smart IO
*   **Block:** `set Pin [15] to [HIGH (1)]`

🔹 **Wait**
*   **Category:** Smart IO
*   **Block:** `wait [speed] [seconds]`

🔹 **Print**
*   **Category:** Smart IO
*   **Block:** `log/print [message]`

### 7️⃣ Variables & State
*   **speed**: Number (seconds) - Controls animation speed (default 0.3s)
*   **pattern**: String - Current pattern name (e.g., "wave", "chase", "blink")
*   **ledPins**: List - Array of LED pin numbers [15, 16, 17, 18]

### 8️⃣ Block Logic

**A. Initialization Phase**
1. Create variable `speed` and set to `0.3`
2. Print "LED Pattern Demo - Level 2"
3. Print "Speed: 0.3s per step"

**B. Main Loop Phase**
1. **Forever do:**
   
   **Pattern 1: Wave Effect (Left to Right)**
   - Print "Pattern: Wave →"
   - FOR each LED (GP15 → GP16 → GP17 → GP18):
     - Turn LED ON
     - Wait `speed` seconds
     - Turn LED OFF
   - Wait `speed` seconds (gap between patterns)
   
   **Pattern 2: Wave Effect (Right to Left)**
   - Print "Pattern: Wave ←"
   - FOR each LED (GP18 → GP17 → GP16 → GP15):
     - Turn LED ON
     - Wait `speed` seconds
     - Turn LED OFF
   - Wait `speed` seconds
   
   **Pattern 3: Alternating Pairs**
   - Print "Pattern: Alternating"
   - Repeat 3 times:
     - Turn Red + Green ON (GP15 + GP17)
     - Turn Yellow + Blue OFF (GP16 + GP18)
     - Wait `speed` seconds
     - Turn Red + Green OFF
     - Turn Yellow + Blue ON
     - Wait `speed` seconds
   - Wait `speed` seconds
   
   **Pattern 4: All Blink**
   - Print "Pattern: All Blink"
   - Repeat 3 times:
     - Turn ALL LEDs ON
     - Wait `speed` seconds
     - Turn ALL LEDs OFF
     - Wait `speed` seconds

**C. Event / Condition Handling**
*   None (automatic pattern cycling)

### 9️⃣ Execution Flow (Plain English)
The program creates four distinct LED patterns that repeat continuously. Unlike Batch 1 projects that used fixed timing, this project introduces a `speed` variable that controls all animation timing from one place. This makes it easy to speed up or slow down the entire show without changing every delay value.

The wave patterns create a "traveling light" effect by turning LEDs on and off in sequence. The alternating pattern splits the LEDs into two groups that blink opposite to each other. The final pattern flashes all LEDs together. After completing all four patterns, the cycle repeats.

**Key Advancement from Batch 1:** Using variables for timing control demonstrates how to make code more flexible and maintainable.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin, PWM, ADC, time_pulse_us
import time

# LED Pin Setup
led_red = Pin(15, Pin.OUT)
led_yellow = Pin(16, Pin.OUT)
led_green = Pin(17, Pin.OUT)
led_blue = Pin(18, Pin.OUT)

# Control Variables
speed = 0.3  # Seconds per animation step
led_pins = [15, 16, 17, 18]

print("LED Pattern Demo - Level 2")
print(f"Speed: {speed}s per step")

while True:
    # Pattern 1: Wave Right
    print("Pattern: Wave →")
    for pin in [15, 16, 17, 18]:
        Pin(pin, Pin.OUT).value(1)
        time.sleep(speed)
        Pin(pin, Pin.OUT).value(0)
    time.sleep(speed)
    
    # Pattern 2: Wave Left
    print("Pattern: Wave ←")
    for pin in [18, 17, 16, 15]:
        Pin(pin, Pin.OUT).value(1)
        time.sleep(speed)
        Pin(pin, Pin.OUT).value(0)
    time.sleep(speed)
    
    # Pattern 3: Alternating Pairs
    print("Pattern: Alternating")
    for _ in range(3):
        led_red.value(1)
        led_green.value(1)
        led_yellow.value(0)
        led_blue.value(0)
        time.sleep(speed)
        
        led_red.value(0)
        led_green.value(0)
        led_yellow.value(1)
        led_blue.value(1)
        time.sleep(speed)
    
    # All OFF between patterns
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(0)
    led_blue.value(0)
    time.sleep(speed)
    
    # Pattern 4: All Blink
    print("Pattern: All Blink")
    for _ in range(3):
        led_red.value(1)
        led_yellow.value(1)
        led_green.value(1)
        led_blue.value(1)
        time.sleep(speed)
        
        led_red.value(0)
        led_yellow.value(0)
        led_green.value(0)
        led_blue.value(0)
        time.sleep(speed)
```

### 1️⃣1️⃣ Common Mistakes
*   **Forgetting to Turn LEDs OFF**: Each pattern should clean up by turning all LEDs off before the next pattern starts.
*   **Mixed Pin Numbers**: Ensure GP15-18 are used consistently; don't confuse with physical pin numbers.
*   **Speed = 0**: Setting speed to 0 causes instant transitions (invisible to human eye).
*   **Current Limit**: Running all 4 LEDs at once may draw ~80mA total; ensure adequate power supply.
*   **Breadboard Connections**: Check common ground rail is properly connected to Pico GND.

### 1️⃣2️⃣ Try This Next
*   **Speed Control Button**: Add a button on GP14 that cycles between slow (0.5s), medium (0.3s), and fast (0.1s) speeds.
*   **Random Colors**: Use `random.choice([15,16,17,18])` to light random LEDs instead of patterns.
*   **Knight Rider Effect**: Create a bouncing back-and-forth pattern with a "tail" effect.
*   **Binary Counter**: Display numbers 0-15 in binary using the 4 LEDs (15=1111, 10=1010, etc.).
*   **Music Sync**: Flash LEDs in rhythm to a simple melody from the buzzer.
*   **POV Display**: Speed up to create persistence-of-vision text/shapes when waved rapidly.

---

## 📊 Project Metadata
- **Batch:** 21
- **Theme:** LED Patterns 2
- **Grade Level:** 3-5 (Elementary)
- **Bloom's Level:** Remember/Understand
- **Complexity:** 4/10 (Intermediate Beginner)
- **Build Time:** 15-20 minutes
- **Concepts from Batch 1 Used:** GPIO write, loops, wait, variables (Projects 001-007)
- **New Concepts:** Variable-controlled timing, complex pattern sequences
- **Next Project Preview:** 0202 will add button control to change patterns on demand
