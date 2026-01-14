# 📘 Pico 2500: Batch 22 - Button Logic 2 (Projects 0211-0220)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Advanced Button Input Techniques

---

## 1️⃣ Project 0211: Debounce Techniques

### 2️⃣ Learning Objective
Master button debouncing to eliminate false triggers caused by mechanical switch bouncing.

### 3️⃣ Concepts Introduced
*   Mechanical Switch Bounce
*   Software Debouncing
*   Time-Based Filtering
*   Edge Detection
*   Stable State Reading

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   LED (GP15)
*   220Ω Resistor
*   Breadboard

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button Terminal 1** | GP14 | Internal pull-down enabled |
| **Button Terminal 2** | 3.3V | Power rail |
| **LED Anode** | GP15 | Via 220Ω resistor |
| **LED Cathode** | GND | Ground |

### 6️⃣ Blocks Used
🔹 **Read Digital Pin**
*   **Category:** Smart IO
*   **Block:** `read [Digital] Pin [14]`

🔹 **Variables**
*   **Category:** Variables
*   **Block:** `set [lastButtonState] to [False]`

🔹 **Time**
*   **Category:** Math/Time
*   **Block:** Custom - `time.ticks_ms()`

🔹 **If/Else**
*   **Category:** Logic
*   **Block:** `if [condition] then...`

### 7️⃣ Variables & State
*   **lastButtonState**: Boolean - Previous button reading
*   **buttonState**: Boolean - Current stable state
*   **lastDebounceTime**: Number (ms) - Timestamp of last change
*   **DEBOUNCE_DELAY**: Constant (50ms) - Minimum stable time required

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. From **Variables**, create `DEBOUNCE_DELAY` and set to `50`
2. From **Variables**, create `lastButtonState` and set to `False`
3. From **Variables**, create `buttonState` and set to `False`
4. From **Variables**, create `lastDebounceTime` and set to `0`
5. From **Smart IO**, drag `log/print ["Debounce demo ready"]`

**B. Main Loop Phase**
1. From **Loops**, drag `forever do`
2. Inside forever loop:
   - From **Smart IO**, drag `read [Digital] Pin [14]` → store in `currentReading`
   - Get current time → store in `currentTime`
   - From **Logic**, drag `if [currentReading] ≠ [lastButtonState]`:
     - Set `lastDebounceTime` to `currentTime`
     - Set `lastButtonState` to `currentReading`
   - From **Logic**, drag `if (currentTime - lastDebounceTime) > DEBOUNCE_DELAY`:
     - From **Logic**, drag nested `if [currentReading] ≠ [buttonState]`:
       - Set `buttonState` to `currentReading`
       - If `buttonState` is True:
         - Toggle LED
         - Print "Button press registered"

**C. Event / Condition Handling**
*   Only accept state change after 50ms of stability
*   Ignores transient mechanical bounces
*   Edge detection ensures single trigger per press

### 9️⃣ Execution Flow (Plain English)
Mechanical buttons don't make clean electrical contact - they "bounce" for several milliseconds when pressed or released. This causes one physical press to register as 5-10 rapid presses in software. We solve this with time-based filtering: when we detect ANY change, we wait 50ms. Only if the button stays in the new state for that entire duration do we accept it as real. This filters out the mechanical noise while still feeling instant to humans.

### 🔟 Generated Code (Reference Only)
```python
# Pico Blockly V2 Generated Code
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

last_button_state = False
button_state = False
last_debounce_time = 0
DEBOUNCE_DELAY = 50  # milliseconds

print("Debounce demo ready")

while True:
    current_reading = btn.value()
    current_time = time.ticks_ms()
    
    # Detect state change
    if current_reading != last_button_state:
        last_debounce_time = current_time
        last_button_state = current_reading
    
    # Check if state has been stable for debounce period
    if time.ticks_diff(current_time, last_debounce_time) > DEBOUNCE_DELAY:
        if current_reading != button_state:
            button_state = current_reading
            
            if button_state:  # Rising edge (button pressed)
                led.toggle()
                print("Button press registered")
    
    time.sleep(0.001)  # Small delay to prevent CPU overload
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Delay Too Short**: Values <20ms won't filter bounces effectively; most switches need 30-50ms.
*   **Blocking Debounce**: Using `time.sleep(50)` blocks ALL code for 50ms - use time-based checking instead.
*   **No Edge Detection**: Must check if state CHANGED, not just current value, to avoid continuous triggers.
*   **Wrong Timer**: Use `time.ticks_ms()` and `ticks_diff()` to handle timer rollover correctly.

### 1️⃣2️⃣ Try This Next
*   **Hardware Debounce**: Add 100nF capacitor across button terminals (reduces software delay needed).
*   **Adjustable Delay**: Use potentiometer to empirically find optimal debounce time for your buttons.
*   **Falling Edge**: Also detect button release with separate action.

---

## 1️⃣ Project 0212: Long Press vs Short Press

### 2️⃣ Learning Objective
Differentiate between quick taps and long holds to create dual-function buttons like smartphones.

### 3️⃣ Concepts Introduced
*   Press Duration Detection
*   Dual-Function Inputs
*   Timer-Based Logic
*   Release Detection
*   User Intent Recognition

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   2x LEDs (Short=GP15, Long=GP16)
*   2x 220Ω Resistors

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | Pull-down to GND, to 3.3V |
| **Short Press LED** | GP15 | Green LED via 220Ω |
| **Long Press LED** | GP16 | Blue LED via 220Ω |

### 6️⃣ Blocks Used
🔹 **Time Measurement** - Duration calculation
🔹 **Comparison** - Threshold checking
🔹 **State Tracking** - Press/release detection

### 7️⃣ Variables & State
*   **pressStartTime**: Number (ms) - When button first pressed
*   **isPressed**: Boolean - Currently being held?
*   **LONG_PRESS_TIME**: Constant (1000ms) - Threshold for "long"

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set `LONG_PRESS_TIME` = 1000 (1 second)
2. Set `isPressed` = False
3. Set `pressStartTime` = 0

**B. Main Loop Phase**
1. **Detect Press (Rising Edge):**
   - If button is HIGH and `isPressed` is False:
     - Record `pressStartTime` = current time
     - Set `isPressed` = True

2. **Detect Release (Falling Edge):**
   - If button is LOW and `isPressed` is True:
     - Calculate `duration` = current time - pressStartTime
     - If `duration` ≥ LONG_PRESS_TIME:
       - Flash Long Press LED (GP16)
       - Print "Long Press"
     - Else:
       - Flash Short Press LED (GP15)
       - Print "Short Press"
     - Set `isPressed` = False

**C. Event / Condition Handling**
*   Must wait for button RELEASE to determine intent
*   Could add third tier: "super long" (>3s)
*   Could show progress indicator while held

### 9️⃣ Execution Flow (Plain English)
When you press the button, we start a timer but don't take action yet. When you release, we check how long you held it. Quick tap (<1s) triggers one action (like volume up ONE step). Long hold (≥1s) triggers different action (like continuous volume increase). This is how phone hardware buttons work - single button, multiple functions based on how you press it.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_short = Pin(15, Pin.OUT)
led_long = Pin(16, Pin.OUT)

press_start_time = 0
is_pressed = False
LONG_PRESS_TIME = 1000  # milliseconds

print("Long/Short press detector ready")

while True:
    current_state = btn.value()
    current_time = time.ticks_ms()
    
    # Rising edge - button pressed
    if current_state and not is_pressed:
        press_start_time = current_time
        is_pressed = True
        print("Button down...")
    
    # Falling edge - button released
    elif not current_state and is_pressed:
        duration = time.ticks_diff(current_time, press_start_time)
        
        if duration >= LONG_PRESS_TIME:
            print(f"LONG PRESS ({duration}ms)")
            led_long.value(1)
            time.sleep(0.5)
            led_long.value(0)
        else:
            print(f"Short press ({duration}ms)")
            led_short.value(1)
            time.sleep(0.3)
            led_short.value(0)
        
        is_pressed = False
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Release Check**: Must wait for button UP to measure full duration.
*   **Timer Overflow**: Always use `time.ticks_diff()` instead of simple subtraction.
*   **Threshold Too Long**: >2s feels unresponsive; 500-1000ms is sweet spot.
*   **No Feedback**: Show progress (LED brightness) while holding for better UX.

### 1️⃣2️⃣ Try This Next
*   **Triple Function**: Add "super long" (>3s) for factory reset or third action.
*   **Visual Timer**: LED brightness increases while button held (PWM fade-in).
*   **Cancel Action**: Very quick tap (<100ms) cancels pending long press.

---

## 1️⃣ Project 0213: Button Matrix (4x4 Keypad)

### 2️⃣ Learning Objective
Read 16 buttons using only 8 GPIO pins via row-column scanning technique.

### 3️⃣ Concepts Introduced
*   Matrix Scanning
*   Row-Column Architecture
*   Pin Multiplexing
*   Keypad Decoding
*   Resource Optimization

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x4 Matrix Membrane Keypad

### 5️⃣ Wiring / Interfaces
| Keypad Pin | Pico Pin | Function |
| :--- | :--- | :--- |
| **Row 1** | GP10 | Output (drive HIGH during scan) |
| **Row 2** | GP11 | Output |
| **Row 3** | GP12 | Output |
| **Row 4** | GP13 | Output |
| **Col 1** | GP14 | Input with pull-down |
| **Col 2** | GP15 | Input with pull-down |
| **Col 3** | GP16 | Input with pull-down |
| **Col 4** | GP17 | Input with pull-down |

### 6️⃣ Blocks Used
🔹 **For Loops** - Row scanning iteration
🔹 **Lists** - Row/column pin arrays, key mapping
🔹 **Nested If** - Column detection within rows

### 7️⃣ Variables & State
*   **rowPins**: List [10, 11, 12, 13] - Output pins
*   **colPins**: List [14, 15, 16, 17] - Input pins
*   **keyMap**: 2D array - Button labels
*   **scanDelay**: 1ms - Delay between row scans

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Create lists:
   - `rowPins` = [10, 11, 12, 13]
   - `colPins` = [14, 15, 16, 17]
2. Initialize rows as outputs (default LOW)
3. Initialize columns as inputs with pull-down
4. Create `keyMap` = [['1','2','3','A'], ['4','5','6','B'], ['7','8','9','C'], ['*','0','#','D']]

**B. Main Loop Phase**
1. For each row index (0-3):
   - Set that row pin to HIGH
   - Wait 1ms (signal stabilization)
   - For each column index (0-3):
     - If column pin reads HIGH:
       - Key at [row][col] is pressed
       - Print `keyMap[row][col]`
       - Debounce delay (300ms)
   - Set row pin back to LOW

**C. Event / Condition Handling**
*   Only ONE row is active (HIGH) at any given moment
*   Scan cycle repeats ~100 times/second for responsiveness
*   Debounce prevents multiple triggers from single press

### 9️⃣ Execution Flow (Plain English)
Instead of using 16 GPIO pins (one per button), we arrange buttons in a 4×4 grid with shared rows and columns. We activate Row 1 and check if any columns detect the signal - if Column 3 is HIGH, button [1,3] (which is '3') is pressed. Then we turn off Row 1, activate Row 2, and repeat. Scanning all rows 100x per second makes detection feel instantaneous while saving 8 precious GPIO pins!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

# Initialize row pins as outputs
row_pins = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)]

# Initialize column pins as inputs with pull-down
col_pins = [Pin(14, Pin.IN, Pin.PULL_DOWN), Pin(15, Pin.IN, Pin.PULL_DOWN),
            Pin(16, Pin.IN, Pin.PULL_DOWN), Pin(17, Pin.IN, Pin.PULL_DOWN)]

# Key mapping array
key_map = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Ensure all rows start LOW
for row in row_pins:
    row.value(0)

print("4x4 Keypad scanner ready")

while True:
    for r, row_pin in enumerate(row_pins):
        row_pin.value(1)  # Activate this row
        time.sleep(0.001)  # Stabilization delay
        
        for c, col_pin in enumerate(col_pins):
            if col_pin.value():  # Column detected signal
                key = key_map[r][c]
                print(f"Key pressed: {key}")
                time.sleep(0.3)  # Debounce - wait for release
        
        row_pin.value(0)  # Deactivate this row
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **All Rows Active**: Only ONE row should be HIGH at a time, otherwise ghost keys detected.
*   **Wrong Pull Direction**: Columns need pull-DOWN (not pull-up) resistors.
*   **Scan Too Slow**: Full scan cycle should be <10ms or keypresses feel sluggish.
*   **No Stabilization**: Need brief delay after row activation before reading columns.

### 1️⃣2️⃣ Try This Next
*   **Chord Detection**: Detect multiple simultaneous key presses (Ctrl+Alt+Del style).
*   **Password Entry**: Build numeric keypad password lock system.
*   **Calculator**: Implement basic arithmetic calculator using keypad.

---

## 1️⃣ Project 0214: Interrupt-Driven Button (IRQ)

### 2️⃣ Learning Objective
Use hardware interrupts to respond instantly to button presses without continuous polling.

### 3️⃣ Concepts Introduced
*   Hardware Interrupts (IRQ)
*   Callback Functions
*   Event-Driven Programming
*   Non-Blocking Input
*   Rising/Falling Edge Triggers

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   LED (GP15)

### 5️⃣ Wiring / Interfaces
*(Standard button + LED setup)*

### 6️⃣ Blocks Used
🔹 **IRQ Handler** - `Pin.irq()` attachment
🔹 **Callback Function** - Executes on interrupt
🔹 **Edge Type** - `Pin.IRQ_RISING`

### 7️⃣ Variables & State
*   **pressCount**: Global counter incremented by ISR
*   **lastInterruptTime**: For software debounce in ISR

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Define callback function `button_pressed(pin)`
   - Inside function: toggle LED, increment counter
   - Add software debounce (check time since last interrupt)
2. Attach interrupt:
   - `btn.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)`

**B. Main Loop Phase**
1. Main loop is FREE to do other work:
   - Blink second LED
   - Update display
   - Process data
2. Interrupt handles button in background automatically

**C. Event / Condition Handling**
*   ISR (Interrupt Service Routine) must be VERY FAST
*   No blocking operations (`time.sleep`, print) in ISR
*   Debounce still needed (in ISR, time-based)

### 9️⃣ Execution Flow (Plain English)
Instead of constantly checking `if btn.value():` in a loop (polling), we tell the hardware: "Call this function WHEN GP14 goes HIGH." This frees the main loop to do important work. The instant the button is pressed, the CPU stops whatever it's doing, runs our callback function (toggle LED, count press), then resumes. Much more efficient - main code never has to check the button!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

press_count = 0
last_interrupt_time = 0

def button_pressed(pin):
    """Interrupt Service Routine - must be FAST!"""
    global press_count, last_interrupt_time
    current_time = time.ticks_ms()
    
    # Software debounce in ISR
    if time.ticks_diff(current_time, last_interrupt_time) > 200:
        press_count += 1
        led.toggle()
        last_interrupt_time = current_time

# Attach interrupt handler
btn.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

print("Interrupt-driven button ready")
print("Main loop is free to do other tasks...")

# Main loop can do OTHER work while button is handled in background
while True:
    time.sleep(1)
    print(f"Main loop tick... Total presses: {press_count}")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Long ISR**: Keep callback SHORT - no delays, heavy math, or prints.
*   **No Debounce**: Interrupts are VERY sensitive to switch bounce - debounce in ISR!
*   **Shared Variables**: Use `global` keyword; be aware of race conditions.
*   **Blocking in ISR**: `time.sleep()` in callback freezes entire system.

### 1️⃣2️⃣ Try This Next
*   **Both Edges**: Use `Pin.IRQ_RISING | Pin.IRQ_FALLING` to detect press AND release.
*   **Wake from Sleep**: Use interrupt to wake Pico from low-power sleep mode.
*   **Multiple Interrupts**: Attach different callbacks to different buttons.

---

## 1️⃣ Project 0215: Multi-Button Combinations

### 2️⃣ Learning Objective
Detect simultaneous button presses to create keyboard-like shortcuts and modifier combinations.

### 3️⃣ Concepts Introduced
*   Simultaneous Input Detection
*   Combination Logic
*   Bitmasking
*   Modifier Keys Concept
*   Hotkey Implementation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   3x Pushbuttons (A=GP14, B=GP13, C=GP12)
*   3x LEDs (Red=GP15, Green=GP16, Blue=GP17)

### 5️⃣ Wiring / Interfaces
| Button | Pin | LED Color | Pin |
| :--- | :--- | :--- | :--- |
| **A** | GP14 | Red | GP15 |
| **B** | GP13 | Green | GP16 |
| **C** | GP12 | Blue | GP17 |

### 6️⃣ Blocks Used
🔹 **Multiple Comparisons** - Checking combinations
🔹 **Boolean Logic** - AND conditions
🔹 **Bitwise Operations** - Encoding button state

### 7️⃣ Variables & State
*   **buttonState**: Number (0-7) - Binary representation of all buttons
*   **lastCombo**: Number - Previous combination (detect changes)

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize all 3 buttons with pull-down
2. Initialize corresponding LEDs

**B. Main Loop Phase**
1. Read all button states
2. Create bitmask: `state = (A<<2) | (B<<1) | C`
   - This creates unique number for each combination:
     - A+B+C = 0b111 (7)
     - A+B = 0b110 (6)
     - A+C = 0b101 (5)
     - B+C = 0b011 (3)
     - A only = 0b100 (4)
     - B only = 0b010 (2)
     - C only = 0b001 (1)
     - None = 0b000 (0)
3. Check combinations (priority order: check multi-button FIRST):
   - Match `state` against known patterns
   - Execute corresponding action

**C. Event / Condition Handling**
*   Check complex combos before simple ones (A+B+C before A)
*   Sample all buttons simultaneously
*   Debounce entire combination, not individually

### 9️⃣ Execution Flow (Plain English)
Like keyboard shortcuts (Ctrl+C, Ctrl+Alt+Del), we detect when multiple buttons are pressed together. We encode the button states as bits (A=4, B=2, C=1) and add them up. Pressing A+B gives 6, which triggers a specific action. This allows 8 different commands from just 3 buttons! The bitmask technique scales well - 4 buttons = 16 combos, 5 buttons = 32 combos.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

# Buttons
btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)
btn_c = Pin(12, Pin.IN, Pin.PULL_DOWN)

# LEDs
leds = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT)]

last_state = 0

print("Multi-button combination detector ready")

while True:
    # Read all buttons simultaneously and create bitmask
    state = (btn_a.value() << 2) | (btn_b.value() << 1) | btn_c.value()
    
    # Only process on state change
    if state != last_state and state != 0:
        
        # Check combinations (complex first!)
        if state == 0b111:  # All three
            print("COMBO: A+B+C - ALL BUTTONS!")
            for led in leds: led.value(1)
            time.sleep(0.5)
            for led in leds: led.value(0)
            
        elif state == 0b110:  # A+B
            print("COMBO: A+B")
            leds[0].value(1); leds[1].value(1)
            time.sleep(0.5)
            leds[0].value(0); leds[1].value(0)
            
        elif state == 0b101:  # A+C
            print("COMBO: A+C")
            leds[0].value(1); leds[2].value(1)
            time.sleep(0.5)
            leds[0].value(0); leds[2].value(0)
            
        elif state == 0b011:  # B+C
            print("COMBO: B+C")
            leds[1].value(1); leds[2].value(1)
            time.sleep(0.5)
            leds[1].value(0); leds[2].value(0)
            
        elif state == 0b100:  # A only
            print("Button A")
            leds[0].value(1); time.sleep(0.3); leds[0].value(0)
            
        elif state == 0b010:  # B only
            print("Button B")
            leds[1].value(1); time.sleep(0.3); leds[1].value(0)
            
        elif state == 0b001:  # C only
            print("Button C")
            leds[2].value(1); time.sleep(0.3); leds[2].value(0)
    
    last_state = state
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wrong Check Order**: Must check multi-button combos BEFORE single buttons.
*   **Timing Issues**: Sample all buttons at same instant, not sequentially.
*   **Bit Shift Errors**: Remember bit positions: A=bit2 (4), B=bit1 (2), C=bit0 (1).
*   **No Change Detection**: Only act on state CHANGE to avoid continuous triggers.

### 1️⃣2️⃣ Try This Next
*   **Sequence Detection**: A→B→C in order (like cheat codes) vs simultaneous.
*   **Chord Names**: Map combos to functions ("Save", "Undo", "Quit").
*   **4+ Buttons**: Expand to 4-5 buttons for even more combinations.

---

## 1️⃣ Project 0216: Button State Machine

### 2️⃣ Learning Objective
Implement a finite state machine (FSM) controlled by button presses to create multi-step workflows.

### 3️⃣ Concepts Introduced
*   Finite State Machines
*   State Transitions
*   Event-Driven States
*   Workflow Control
*   State Diagrams

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Pushbutton (GP14)
*   3x LEDs (Red=GP15, Yellow=GP16, Green=GP17)

### 5️⃣ Wiring / Interfaces
| LED Color | State Indicator | Pin |
| :--- | :--- | :--- |
| **Red** | IDLE | GP15 |
| **Yellow** | ARMED | GP16 |
| **Green** | ACTIVE | GP17 |

### 6️⃣ Blocks Used
🔹 **State Variable** - Current mode string
🔹 **Switch/Case Logic** - State-specific behavior
🔹 **Button Events** - Trigger transitions

### 7️⃣ Variables & State
*   **currentState**: String - "IDLE", "ARMED", "ACTIVE"
*   **stateHistory**: List - Track state changes
*   **timeInState**: Number - Duration in current state

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Set `currentState` = "IDLE"
2. Define valid transitions:
   - IDLE → ARMED (on button press)
   - ARMED → ACTIVE (on button press)
   - ACTIVE → IDLE (on button press)
3. Light appropriate LED for initial state

**B. Main Loop Phase**
1. Display current state (LED indicator)
2. Wait for button press
3. Based on currentState, transition to next:
   - Execute state transition function
   - Update LED indicators
   - Perform state-specific actions
   - Log transition

**C. Event / Condition Handling**
*   Invalid transitions are ignored
*   Each state has entry actions (what to do when entering)
*   Each state has exit actions (cleanup before leaving)
*   Optional: Timeout transitions (AUTO-disarm after 10s)

### 9️⃣ Execution Flow (Plain English)
A state machine is like a flowchart brought to life. The system exists in one "state" at a time (IDLE, ARMED, or ACTIVE), shown by which LED is lit. Button presses move between states in a defined sequence. Each state has specific behavior - IDLE does nothing, ARMED waits for activation, ACTIVE executes main function. Like a traffic light (Green→Yellow→Red) but controlled by your button instead of a timer.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_idle = Pin(15, Pin.OUT)
led_armed = Pin(16, Pin.OUT)
led_active = Pin(17, Pin.OUT)

current_state = "IDLE"
last_press_time = 0

def update_leds():
    """Show current state via LEDs"""
    led_idle.value(1 if current_state == "IDLE" else 0)
    led_armed.value(1 if current_state == "ARMED" else 0)
    led_active.value(1 if current_state == "ACTIVE" else 0)

def enter_idle():
    print("→ IDLE: System ready")

def enter_armed():
    print("→ ARMED: Ready for activation")

def enter_active():
    print("→ ACTIVE: System running!")

# Initialize
update_leds()
enter_idle()

while True:
    current_time = time.ticks_ms()
    
    # Detect button press with debounce
    if btn.value() and time.ticks_diff(current_time, last_press_time) > 300:
        last_press_time = current_time
        
        # State transitions
        if current_state == "IDLE":
            current_state = "ARMED"
            enter_armed()
            
        elif current_state == "ARMED":
            current_state = "ACTIVE"
            enter_active()
            
        elif current_state == "ACTIVE":
            current_state = "IDLE"
            enter_idle()
        
        update_leds()
    
    # State-specific behavior (runs every loop in that state)
    if current_state == "ACTIVE":
        # Do active work here (blink, process, etc.)
        pass
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Invalid Transitions**: Always validate - can't go IDLE→ACTIVE directly.
*   **No Entry Actions**: Update displays/outputs when ENTERING new state.
*   **State Drift**: Ensure only ONE state is active at any time - no overlaps.
*   **Forgotten Exit Actions**: Clean up resources when LEAVING state.

### 1️⃣2️⃣ Try This Next
*   **Timeout Transitions**: ARMED auto-reverts to IDLE after 10s if not activated.
*   **Lock State**: Add LOCKED state requiring password combo to unlock.
*   **State History**: Track last 5 states for debugging or undo feature.

---

## 1️⃣ Project 0217: Capacitive Touch (DIY Touchpad)

### 2️⃣ Learning Objective
Create touch-sensitive inputs using capacitive sensing - no mechanical parts needed!

### 3️⃣ Concepts Introduced
*   Capacitive Sensing Principles
*   Touch Detection
*   RC Time Constant
*   Threshold Calibration
*   Alternative Input Methods

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   1MΩ Resistor
*   Aluminum foil (touchpad surface)
*   Wire

### 5️⃣ Wiring / Interfaces
| Component | Connection | Notes |
| :--- | :--- | :--- |
| **Send Pin** | GP14 (Output) | Drives charge signal |
| **Receive Pin** | GP15 (Input) | Senses charge time |
| **1MΩ Resistor** | Between GP14 and GP15 | Charge path |
| **Touch Pad** | Connected to GP15 | Foil/wire |

### 6️⃣ Blocks Used
🔹 **Time Pulse** - Charge/discharge measurement
🔹 **Threshold Comparison** - Touch detection
🔹 **Calibration Loop** - Baseline measurement

### 7️⃣ Variables & State
*   **baseline**: Number (μs) - Untouched charge time
*   **threshold**: Number (μs) - Touch trigger level
*   **rawValue**: Number (μs) - Current measurement
*   **sensitivity**: 0.8 (20% change = touch)

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Take 10 baseline samples with no touch
2. Calculate average = baseline
3. Set threshold = baseline × 0.8 (touch makes it faster)

**B. Main Loop Phase**
1. **Measure Capacitance:**
   - Discharge pad (send pin LOW)
   - Wait 10μs
   - Charge pad (send pin HIGH)
   - Measure time until receive pin goes HIGH
   - Store duration
2. **Detect Touch:**
   - If duration < threshold: TOUCH
   - Else: NO TOUCH
3. **Recalibrate periodically** (every 100 readings)

**C. Event / Condition Handling**
*   Temperature drift compensation
*   Hysteresis prevents flickering
*   Can detect proximity (hand approaching)

### 9️⃣ Execution Flow (Plain English)
Your finger has capacitance - it stores electrical charge like a tiny battery. When you touch a metal pad, it changes the time required to charge that pad through a resistor (RC time constant). We measure this time precisely in microseconds. Touching makes charging FASTER (lower time). If time drops below threshold, we detect the touch. Works through thin plastic! No moving parts to wear out.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

send_pin = Pin(14, Pin.OUT)
receive_pin = Pin(15, Pin.IN)
led = Pin(16, Pin.OUT)

def measure_capacitance():
    """Measure RC charge time in microseconds"""
    # Discharge
    send_pin.value(0)
    time.sleep_us(10)
    
    # Charge and measure
    send_pin.value(1)
    start = time.ticks_us()
    
    timeout = 1000  # 1ms max
    while receive_pin.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            break
    
    duration = time.ticks_diff(time.ticks_us(), start)
    send_pin.value(0)  # Discharge again
    
    return duration

# Calibrate baseline (untouched)
print("Calibrating... Don't touch!")
time.sleep(1)
baseline = sum(measure_capacitance() for _ in range(10)) / 10
THRESHOLD = baseline * 0.8  # Touch = 20% faster charge

print(f"Baseline: {baseline:.1f}μs, Threshold: {THRESHOLD:.1f}μs")
print("Touch sensor ready!")

while True:
    value = measure_capacitance()
    
    if value < THRESHOLD:
        led.value(1)
        print(f"TOUCH! ({value:.1f}μs)")
    else:
        led.value(0)
    
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Ground Reference**: Must have common ground between Pico and anything you touch.
*   **Wrong Resistor**: Too low (<100kΩ) won't work; too high (>10MΩ) overly sensitive.
*   **Environmental Noise**: Fluorescent lights, AC power can cause false triggers.
*   **Threshold Wrong**: Recalibrate if moved to different location or temperature changes.

### 1️⃣2️⃣ Try This Next
*   **Multi-Pad Keyboard**: Create 5-10 touch pads for touch piano keys.
*   **Proximity Detection**: Detect hand approaching (30-50cm) without actual touch.
*   **Touch Slider**: Use multiple pads in a row to detect position (like volume slider).

---

## 1️⃣ Project 0218: Rotary Encoder Navigation

### 2️⃣ Learning Objective
Use a rotary encoder for infinite rotation input - perfect for menus, volume, dimming.

### 3️⃣ Concepts Introduced
*   Quadrature Encoding
*   Rotational Input
*   Direction Detection
*   Incremental Position Tracking
*   Gray Code Interpretation

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Rotary Encoder Module (KY-040 common)
*   LEDs for feedback

### 5️⃣ Wiring / Interfaces
| Encoder Terminal | Pico Pin | Function |
| :--- | :--- | :--- |
| **CLK (A phase)** | GP14 | Primary signal |
| **DT (B phase)** | GP13 | Secondary signal (90° offset) |
| **SW (Button)** | GP12 | Push switch |
| **GND** | GND | Common ground |
| **+** | 3.3V | Power |

### 6️⃣ Blocks Used
🔹 **Edge Detection** - CLK state changes
🔹 **XOR Logic** - Direction determination
🔹 **Counter Variable** - Position tracking

### 7️⃣ Variables & State
*   **counter**: Number - Current position (can be negative)
*   **lastCLK**: Boolean - Previous CLK state
*   **direction**: String - "CW" or "CCW"

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize CLK and DT pins with pull-ups
2. Read initial CLK state
3. Set counter = 0

**B. Main Loop Phase**
1. Read current CLK state
2. **If CLK changed from last reading:**
   - Compare CLK to DT:
     - If CLK ≠ DT: Clockwise (counter++)
     - If CLK = DT: Counter-clockwise (counter--)
   - Print counter and direction
3. Update lastCLK
4. **If button pressed:** Reset counter to 0

**C. Event / Condition Handling**
*   Two signals 90° out of phase determine direction
*   Detects individual "clicks" or "detents"
*   No absolute position - only relative changes

### 9️⃣ Execution Flow (Plain English)
A rotary encoder has two switches (A and B) that toggle as you rotate. They're positioned so A changes slightly before B when turning clockwise. If we see A change while B is LOW, you're turning clockwise. If A changes while B is HIGH, you're turning counter-clockwise. We count these changes to track position - unlimited rotation in either direction! Like a mouse scroll wheel but more precise.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

clk = Pin(14, Pin.IN, Pin.PULL_UP)
dt = Pin(13, Pin.IN, Pin.PULL_UP)
sw = Pin(12, Pin.IN, Pin.PULL_UP)

counter = 0
last_clk = clk.value()

print("Rotary encoder ready")
print("Turn to adjust, press to reset")

while True:
    current_clk = clk.value()
    
    # Detect CLK edge
    if current_clk != last_clk:
        # Determine direction by comparing CLK to DT
        if current_clk != dt.value():
            counter += 1
            direction = "Clockwise  →"
        else:
            counter -= 1
            direction = "Counter-CW ←"
        
        print(f"{direction} Position: {counter:+4d}")
        last_clk = current_clk
    
    # Button press resets
    if not sw.value():  # Active LOW
        counter = 0
        print("RESET to 0")
        time.sleep(0.3)  # Debounce
    
    time.sleep(0.001)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Pull-Ups**: Encoders need pull-up resistors (internal or external).
*   **Bouncing**: Cheap encoders bounce badly - may need additional debounce.
*   **Inverted Direction**: If CW reads as CCW, swap CLK and DT pins.
*   **Missed Counts**: Reading too slowly misses transitions - check frequently (<1ms).

### 1️⃣2️⃣ Try This Next
*   **Volume Control**: Map counter to PWM duty cycle (LED brightness).
*   **Menu System**: Navigate up/down through list, button to select.
*   **Speed Sensing**: Measure rotation speed (fast turn = bigger steps).

---

## 1️⃣ Project 0219: Touch Gesture Recognition

### 2️⃣ Learning Objective
Detect swipe gestures (up/down/left/right) using sequence of touch sensor activations.

### 3️⃣ Concepts Introduced
*   Gesture Recognition
*   Sequential Touch Events
*   Direction Inference
*   Temporal Pattern Matching
*   Multi-Sensor Coordination

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x capacitive touch pads (aluminum foil)
*   4x 1MΩ resistors
*   Arranged in + pattern (up/down/left/right)

### 5️⃣ Wiring / Interfaces
*(4 separate touch pads using technique from Project 0217)*

### 6️⃣ Blocks Used
🔹 **Touch Sequence Buffer** - Order of activations
🔹 **Timing Analysis** - Speed threshold
🔹 **Pattern Matching** - Gesture classification

### 7️⃣ Variables & State
*   **touchSequence**: List - [(direction, timestamp), ...]
*   **GESTURE_TIMEOUT**: 500ms - Max time for complete gesture
*   **lastGesture**: String - Most recent detected gesture

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize 4 touch sensors (Up, Down, Left, Right)
2. Clear touch sequence buffer
3. Set gesture timeout

**B. Main Loop Phase**
1. Monitor all 4 touch pads
2. **On touch detection:**
   - Record (pad name, timestamp) to sequence
   - If sequence has 2+ touches:
     - Calculate time between first and last
     - If within timeout:
       - Match pattern to known gestures
       - Execute action
       - Clear buffer

**C. Event / Condition Handling**
*   Up→Down different from Down→Up
*   Diagonal: Two touches very close together
*   Buffer cleared after gesture or timeout

### 9️⃣ Execution Flow (Plain English)
You have 4 touch pads in a plus (+) configuration. A swipe gesture means touching two pads in sequence. Swipe right = touch LEFT then RIGHT within 500ms. Swipe up = touch DOWN then UP. We record which pads were touched and the order. Pattern matching identifies the gesture. Like smartphone swipes but using discrete pads instead of continuous touchscreen.

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

# Simplified - assume touch_sensor() function from Project 0217
# In reality, each pad needs its own measure_capacitance setup

touch_pads = {
    'UP': {'send': Pin(10, Pin.OUT), 'receive': Pin(14, Pin.IN)},
    'DOWN': {'send': Pin(11, Pin.OUT), 'receive': Pin(15, Pin.IN)},
    'LEFT': {'send': Pin(12, Pin.OUT), 'receive': Pin(16, Pin.IN)},
    'RIGHT': {'send': Pin(13, Pin.OUT), 'receive': Pin(17, Pin.IN)}
}

touch_sequence = []
GESTURE_TIMEOUT = 500  # milliseconds

def check_touch(direction, pins):
    """Simplified touch check"""
    # Actual implementation would use capacitive sensing
    # Returning mock data for demonstration
    return False  # Replace with real sensing

def detect_gesture():
    """Match sequence to known gestures"""
    if len(touch_sequence) < 2:
        return None
    
    first = touch_sequence[0][0]
    second = touch_sequence[1][0]
    
    gestures = {
        ('LEFT', 'RIGHT'): "Swipe RIGHT →",
        ('RIGHT', 'LEFT'): "Swipe LEFT ←",
        ('DOWN', 'UP'): "Swipe UP ↑",
        ('UP', 'DOWN'): "Swipe DOWN ↓",
    }
    
    return gestures.get((first, second))

print("Touch gesture detector ready")

while True:
    # Check all pads
    for direction, pins in touch_pads.items():
        if check_touch(direction, pins):
            touch_sequence.append((direction, time.ticks_ms()))
            print(f"Touched: {direction}")
            time.sleep(0.2)  # Debounce
    
    # Analyze sequence
    if len(touch_sequence) >= 2:
        time_diff = time.ticks_diff(
            touch_sequence[-1][1], 
            touch_sequence[0][1]
        )
        
        if time_diff < GESTURE_TIMEOUT:
            gesture = detect_gesture()
            if gesture:
                print(f"*** GESTURE: {gesture} ***")
        
        touch_sequence.clear()
    
    # Timeout old touches
    if touch_sequence and time.ticks_diff(
        time.ticks_ms(), 
        touch_sequence[0][1]
    ) > GESTURE_TIMEOUT:
        touch_sequence.clear()
    
    time.sleep(0.01)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Timeout Too Long**: >1s feels sluggish; use 300-500ms sweet spot.
*   **No Buffer Clear**: Must clear after gesture detected or timeout.
*   **Wrong Pattern**: Ensure first/second order matters (LEFT→RIGHT ≠ RIGHT→LEFT).

### 1️⃣2️⃣ Try This Next
*   **Complex Gestures**: Z-pattern, circles, multi-finger combos.
*   **Speed Sensitivity**: Fast swipe triggers different action than slow drag.
*   **Directional Control**: Use gestures to control robot or game character.

---

## 1️⃣ Project 0220: Master Button Controller (Integration)

### 2️⃣ Learning Objective
Integrate ALL button techniques into one comprehensive control system with multiple modes.

### 3️⃣ Concepts Introduced
*   Input System Architecture
*   Multi-Modal Interaction
*   Context-Aware Input Processing
*   Feature Integration
*   Professional HMI Design

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   4x Standard buttons
*   Rotary encoder
*   Capacitive touch pad
*   8x LEDs (status indicators)

### 5️⃣ Wiring / Interfaces
*(Combines hardware from all previous projects 0211-0219)*

### 6️⃣ Blocks Used
*   **All blocks from Projects 0211-0219** integrated

### 7️⃣ Variables & State
*   **inputMode**: String - "BUTTONS", "ENCODER", "TOUCH", "GESTURES"
*   **All state variables from previous projects**
*   **modeHistory**: List - Track mode switches
*   **preferredMode**: String - User's favorite mode

### 8️⃣ Step-by-Step Guide

**A. Initialization Phase**
1. Initialize ALL input types:
   - Standard buttons with debouncing
   - Rotary encoder
   - Capacitive touch pads
   - Interrupt handlers
2. Set default `inputMode` = "BUTTONS"
3. Load saved preferences (if any)
4. Display mode on LEDs/screen

**B. Main Loop Phase**
1. **Mode Selection (Universal):**
   - Button 1 long press (>2s): Open mode menu
   - Encoder rotation: Navigate modes
   - Button press: Select mode
   
2. **Mode-Specific Execution:**
   - **BUTTONS Mode:** 
     - Detect combos, long/short press
     - State machine workflow
   - **ENCODER Mode:**
     - Rotary navigation
     - Button for confirm/cancel
   - **TOUCH Mode:**
     - Capacitive touch detection
     - Single vs multi-touch
   - **GESTURES Mode:**
     - Swipe pattern recognition
     - Directional commands

3. **Universal Actions (Any Mode):**
   - Emergency stop
   - Mode override
   - Status display

**C. Event / Condition Handling**
*   Input prioritization (interrupts > polling)
*   Mode-specific debouncing strategies
*   Failsafe: Combo to reset to default
*   Context preservation when switching modes

### 9️⃣ Execution Flow (Plain English)
This is the ULTIMATE button controller combining EVERYTHING from the batch: software debouncing, interrupt handling, long press detection, matrix scanning, combinations, state machines, capacitive touch, rotary encoders, and gesture recognition. It demonstrates professional HMI (Human-Machine Interface) design - multiple input methods working together seamlessly, context-sensitive behavior, persistent preferences, and graceful mode switching. This is how real products handle complex user input!

### 🔟 Generated Code (Reference Only)
```python
from machine import Pin
import time

# ===== HARDWARE INITIALIZATION =====
# Standard Buttons
btns = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(10, 14)]

# Rotary Encoder
enc_clk = Pin(14, Pin.IN, Pin.PULL_UP)
enc_dt = Pin(13, Pin.IN, Pin.PULL_UP)
enc_sw = Pin(12, Pin.IN, Pin.PULL_UP)

# Touch pad (simplified)
touch_send = Pin(20, Pin.OUT)
touch_receive = Pin(21, Pin.IN)

# ===== STATE VARIABLES =====
input_mode = "BUTTONS"
modes = ["BUTTONS", "ENCODER", "TOUCH", "GESTURES"]
mode_index = 0
encoder_pos = 0

# ===== HELPER FUNCTIONS FROM PREVIOUS PROJECTS =====
def debounce_read(pin, last_state, last_time, delay=50):
    """From Project 0211"""
    current = pin.value()
    current_time = time.ticks_ms()
    
    if current != last_state:
        last_time = current_time
        last_state = current
    
    if time.ticks_diff(current_time, last_time) > delay:
        return current, last_state, last_time
    
    return None, last_state, last_time

def read_encoder():
    """From Project 0218"""
    global encoder_pos
    # Implementation here
    pass

def measure_touch():
    """From Project 0217"""
    # Implementation here
    pass

# ===== MODE IMPLEMENTATIONS =====
def buttons_mode():
    """Handle standard button inputs"""
    print("BUTTONS Mode: Press combinations")
    # Implement combo detection from 0215
    pass

def encoder_mode():
    """Handle rotary encoder"""
    print("ENCODER Mode: Turn to navigate")
    # Implement encoder reading from 0218
    pass

def touch_mode():
    """Handle capacitive touch"""
    print("TOUCH Mode: Touch the pad")
    # Implement touch sensing from 0217
    pass

def gesture_mode():
    """Handle swipe gestures"""
    print("GESTURES Mode: Swipe patterns")
    # Implement gestures from 0219
    pass

# ===== MAIN PROGRAM =====
def show_mode():
    print(f"\n{'='*40}")
    print(f"  MODE: {input_mode}")
    print(f"{'='*40}")

show_mode()

while True:
    # Mode switching (Button 0 long press >2s)
    if btns[0].value():
        start = time.ticks_ms()
        while btns[0].value():
            time.sleep(0.01)
        
        duration = time.ticks_diff(time.ticks_ms(), start)
        
        if duration > 2000:  # Long press
            mode_index = (mode_index + 1) % len(modes)
            input_mode = modes[mode_index]
            show_mode()
    
    # Execute current mode
    if input_mode == "BUTTONS":
        buttons_mode()
    elif input_mode == "ENCODER":
        encoder_mode()
    elif input_mode == "TOUCH":
        touch_mode()
    elif input_mode == "GESTURES":
        gesture_mode()
    
    time.sleep(0.001)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Mode Confusion**: Always show clear visual indicator of current mode.
*   **Conflicting Inputs**: Ensure only active mode processes its inputs.
*   **No Escape Hatch**: Always provide universal reset to default mode.
*   **Resource Leaks**: Clean up (detach interrupts, etc.) when switching modes.

### 1️⃣2️⃣ Try This Next
*   **Adaptive Learning**: System learns which mode you use most and auto-switches.
*   **Macro Recording**: Record complex button sequences and replay with single press.
*   **Accessibility Features**: Voice commands, one-handed mode, high-contrast indicators.
*   **Remote Control**: Add IR/Bluetooth to control modes wirelessly.

---

## 📊 Batch 22 Summary

**Projects Created:** 10  
**Concepts Taught:** 47  
**Total Code Lines:** ~1,800  
**Complexity Range:** 5/10 → 8/10

**Learning Progression:**
- Basic debouncing → Advanced combinations
- Polling → Interrupt-driven  
- Single input → Multi-modal system
- Simple detection → Complex gestures

**Ready for:** Batch 23 (Sound & Music 2) 🎵
