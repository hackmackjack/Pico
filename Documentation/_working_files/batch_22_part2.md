
## 1. Project 0216: Smart Button Logic Switch

### 2. Learning Objective
Explore temporal state transitions (The Exit Delay). Learn how to implement a "Delayed Off" sequence where the system acknowledges a shutdown command (Button Press) but maintains an active state (LED On) for a specific duration before final deactivation.

### 3. Concepts Introduced
*   **Off-Delay Timer**: Delaying the transition from ON to OFF after an input trigger.
*   **State Latency**: introducing a purely software-driven "Active" period that doesn't rely on physical holding.
*   **User Safety Logic**: Simulating exit lighting found in cars or hallways.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + resistor
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Logic Button** | GP14 | Press to trigger exit delay |
| **Exit Light** | GP15 | Stays ON for 5s after press |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (detecting click)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)
*   **from Time, drag `pico_wait`** (wait)

### 7. Variables
*   **None**: this is a linear timed sequence.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Safety State**: **Set** GP15 (LED) -> LOW (0).

**B. Control Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Detect Shutdown Request**:
    *   Inside the loop, from **Logic**, drag `controls_if`.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is HIGH (1).

**C. Execution Phase**
4.  **Acknowledgment**:
    *   Inside the **If** block, **Set** GP15 -> HIGH (1).
    *   **Print** "Shutdown Sequence Started. 5 Seconds Remaining...".
5.  **Hold State**:
    *   From **Time**, **Wait** 5 seconds.
6.  **Finalize**:
    *   **Set** GP15 -> LOW (0).
    *   **Print** "System OFF".

### 9. Execution Flow
1.  **Idle**: The light is off.
2.  **Trigger**: You press the button once.
3.  **Hold**: The Pico immediately turns the light ON (or keeps it ON) and hits the 5-second "Wait" block.
4.  **Timer**: The light illuminates your "path" for exactly 5 seconds.
5.  **Finish**: The Pico turns the light OFF and goes back to waiting for the next press.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if btn.value() == 1:
        # User requested off - start delay
        led.value(1)
        print("Exit delay active: 5s")
        time.sleep(5)
        
        # Turn off after delay
        led.value(0)
        print("Light turned off.")
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Button Spam**: If you press the button during the 5-second wait, nothing happens because the Pico is "blocked" by the `sleep` command.
*   **Initial State**: If the problem requires the light to be ON first, you would need a toggle variable.

### 12. Try This Next
*   **Warning Blink**: Make the LED flash during the final 1 second of the delay so the user knows it's about to go dark.
*   **Cancelable Delay**: Try to make it so pressing the button AGAIN during the 5s delay turns the light off immediately.

---

## 1. Project 0217: Button Logic Alarm System

### 2. Learning Objective
Explore inverted safety logic (Normally Closed / Tamper Detection). Learn how to design a system where the *absence* of a signal (Button Release) is the trigger for an event, simulating a security switch that detects when a lid or door is forced open.

### 3. Concepts Introduced
*   **Normally Closed (NC) Logic**: a circuit that is "Safe" when the loop is complete and "Alarmed" when broken.
*   **Tamper Detection**: identifying unauthorized physical movement of hardware.
*   **Inverted Triggering**: using `if not button` or `if button == 0` as the primary logic condition.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button (placed under a heavy object or lid)
*   1 Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tamper Switch** | GP14 | Held DOWN when safe |
| **Alarm Buzzer** | GP15 | Sounds when button is released |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)

### 7. Variables
*   **None**: this uses real-time signal inversion.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prepare Buzzer**: **Set** GP15 -> LOW (0).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Check Continuity**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Smart IO** `pico_gpio_read` GP14 is LOW (0).
    *   *Explanation: Because the lid is holding the button DOWN, a "LOW" value means the lid has been lifted (the button popped up).*

**C. Response Phase**
4.  **Alarm State (Lid Lifted)**:
    *   Inside the **If** block: **Set** GP15 -> HIGH (1). **Print** "TAMPER DETECTED! LID OPEN".
5.  **Safe State (Lid Closed)**:
    *   Inside the **Else** block: **Set** GP15 -> LOW (0).

### 9. Execution Flow
1.  **Setup**: You place a box on top of the button, holding it down (Logic 1).
2.  **Idle**: The Pico checks the button. Since it is HIGH (1), it follows the "Else" (Safe) path.
3.  **Breach**: An intruder lifts the box. The button's spring pushes it up, breaking the contact (Logic 0).
4.  **Reaction**: The Pico sees the 0, follows the "If" branch, and turns the buzzer ON.
5.  **Result**: A reliable "Fail-Safe" alarm that triggers even if a wire is cut or the sensor is removed.

### 10. Generated Code
```python
from machine import Pin
import time

# Note: Pin is PULL_UP or PULL_DOWN depending on wiring.
# Here we assume button connects GND to Pin (0 when pressed).
# Or simpler: Button connects 3.3V to Pin (1 when pressed).
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)

while True:
    # Normally Closed Logic: 
    # Lid DOWN = Button Pressed (1)
    # Lid UP = Button Released (0)
    
    if btn.value() == 0:
        # Protection loop broken!
        buzzer.value(1)
        print("SECURITY ALERT")
    else:
        # Loop intact
        buzzer.value(0)
        
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Wrong Assumption**: Forgetting that in NC logic, "0" is bad and "1" is good. If you swap them, the alarm will only sound while you are holding the lid shut.
*   **Floating Pins**: If your button isn't wired to GND or 3.3V firmly, you'll get "False Positives" (ghost alarms).

### 12. Try This Next
*   **Latch the Alarm**: combine this with Project 0207 so the buzzer stays on even if the intruder puts the lid back down.
*   **Silent Alarm**: Print the alert to the screen instead of using a buzzer.

---

## 1. Project 0218: The Button Logic Game

### 2. Learning Objective
Explore competitive state manipulation (Tug of War). Learn how to handle two simultaneous inputs (Player A and Player B) that compete to modify a single numerical variable (The Position), using a row of LEDs to visualize the balance of power.

### 3. Concepts Introduced
*   **Competitive Incrementation**: One input adds (+1), one input subtracts (-1).
*   **Numerical Clamping**: Preventing a game variable from going outside the range of your display (e.g., cannot go below LED 1 or above LED 5).
*   **Win Conditions**: triggering a dedicated end-state when a variable hits a maximum or minimum threshold.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons
*   5 LEDs + Resistors (placed in a line)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Player A Button** | GP14 | Moves light Left (-1) |
| **Player B Button** | GP13 | Moves light Right (+1) |
| **LEDs (1-5)** | GP15-GP19 | Visual "Rope" |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (addition/subtraction)
*   **from Logic, drag `controls_if`** (detecting taps)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)

### 7. Variables
*   **rope_position**: Number (1 to 5) representing the active LED.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Point**:
    *   From **Variables**, **Set** `rope_position` = 3 (The Center).

**B. Control Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Player A Attack**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `rope_position` = `rope_position` - 1.
        *   **Wait** 0.2s (One tap per click).
4.  **Player B Attack**:
    *   If **Button** GP13 is Pressed:
        *   **Set** `rope_position` = `rope_position` + 1.
        *   **Wait** 0.2s.

**C. Bound and Win Phase**
5.  **Determine Victor**:
    *   If `rope_position` < 1: **Print** "Player A Wins!". Reset to 3.
    *   If `rope_position` > 5: **Print** "Player B Wins!". Reset to 3.

**D. Visualization Phase**
6.  **Drive the LEDs**:
    *   Loop 1 to 5: Turn ON the LED that matches `rope_position`, turn all others OFF.

### 9. Execution Flow
1.  **Setup**: The middle LED (#3) is lit.
2.  **Battle**: Player A mashes their button. The light moves 3 -> 2 -> 1.
3.  **Counter**: Player B hits back. The light moves 1 -> 2.
4.  **Victory**: Player A hits one more time. The position becomes 0. The Pico detects the "Win", flashes the lights, and resets the game.
5.  **Result**: A physical, high-speed electronic version of Tug of War.

### 10. Generated Code
```python
import machine
import utime

# Hardware
btns = [machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN),
        machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)]
leds = [machine.Pin(15+i, machine.Pin.OUT) for i in range(5)]

# Game State
pos = 2 # Index 0 to 4 (Start at center)

while True:
    # Player A (Left)
    if btns[0].value():
        pos -= 1
        utime.sleep(0.15)
        
    # Player B (Right)
    if btns[1].value():
        pos += 1
        utime.sleep(0.15)
        
    # Boundary / Win Logic
    if pos < 0:
        print("PLAYER A WINS!")
        pos = 2; utime.sleep(1)
    if pos > 4:
        print("PLAYER B WINS!")
        pos = 2; utime.sleep(1)
        
    # Update Display
    for i in range(5):
        leds[i].value(1 if i == pos else 0)
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **No Wait (Debounce)**: If you don't use the 0.15s wait, a single tap will move the light all the way to the edge instantly.
*   **Indexing**: remember that in code, 5 LEDs are often numbered 0, 1, 2, 3, 4.

### 12. Try This Next
*   **Strength Handicaps**: Give one player 1.5 points per click to balance the game.
*   **Buzzer Grunt**: play a short "oomph" sound every time the rope moves.

---

## 1. Project 0219: Automated Button Logic

### 2. Learning Objective
Explore temporal event discrimination (Double Click Detection). Learn how to use a high-speed timer to differentiate between a single click and a double-click, enabling one physical button to control two independent systems (Red vs Green LEDs).

### 3. Concepts Introduced
*   **Double-Click Timing**: Measuring the interval between two Rising Edge events.
*   **Temporal Thresholds**: deciding that any two clicks within 400ms count as a "Double".
*   **Branching Commands**: Routing logic to different hardware based on interaction speed.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   2 LEDs (Red and Green)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Input Button** | GP14 | Single vs Double input |
| **System A (Red)** | GP15 | Controlled by Single Click |
| **System B (Green)** | GP14 | Controlled by Double Click |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_time_ms`** (timestamping)
*   **from Logic, drag `controls_if`** (detecting intervals)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)

### 7. Variables
*   **last_click**: Timestamp of the previous press.
*   **click_count**: track if it's the 1st or 2nd tap.

### 8. Step-by-Step Guide

**A. Capture Phase**
1.  **Wait for Press**:
    *   From **Loops**, `pico_forever`.
    *   If **Button** GP14 is Pressed:
        *   **Set** `now` = **Time** `pico_time_ms`.
        *   **Calculate** `gap` = `now` - `last_click`.

**B. Discrimination Phase**
2.  **Evaluate Gap**:
    *   If `gap` < 400 (milliseconds):
        *   **Action for Double**: Toggle Green LED.
        *   **Set** `last_click` = 0 (reset to avoid triple-click errors).
    *   Else:
        *   **Wait** 0.4s to see if a second click comes.
        *   If no second click: **Action for Single**: Toggle Red LED.
        *   **Set** `last_click` = `now`.

### 9. Execution Flow
1.  **Single**: You tap the button once. The Pico waits 0.4s. No second tap arrives. It toggles the Red LED.
2.  **Double**: You tap once, pause 0.1s, and tap again.
3.  **Math**: The Pico sees the gap is 100ms. Since 100 < 400, it ignores the single-click logic and fires the Green LED instead.
4.  **Result**: One-button interface that handles multiple complex commands, exactly like a computer mouse.

### 10. Generated Code
```python
import machine
import utime

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_r = machine.Pin(15, machine.Pin.OUT)
led_g = machine.Pin(16, machine.Pin.OUT)

last_time = 0

while True:
    if btn.value():
        new_time = utime.ticks_ms()
        diff = utime.ticks_diff(new_time, last_time)
        
        if diff < 400:
            # DOUBLE CLICK
            led_g.value(not led_g.value())
            print("DOUBLE")
            last_time = 0 # Prevent triple click
        else:
            # First tap of potential double or single
            last_time = new_time
            # We wait to see if it's a single
            # (In a real app, you'd use a timer to not block)
            utime.sleep(0.4)
            if not btn.value() and last_time != 0:
                led_r.value(not led_r.value())
                print("SINGLE")

        utime.sleep(0.2) # Debounce
```

### 11. Common Mistakes
*   **Blocking wait**: In the simple code above, the Pico "pauses" for 0.4s to check for a single click. This makes the system feel slightly sluggish. Advanced programmers use "Interrupts" to fix this.
*   **Gap Too Short**: if you set the threshold to 100ms, only super-fast robots could double-click your button. Use 300-500ms for humans.

### 12. Try This Next
*   **Long Press**: Add logic to detect a 3-second "Hold" to turn both LEDs off simultaneously.
*   **Triple Click**: Can you add a third LED for a triple-tap?

---

## 1. Project 0220: Mastering Button Logic

### 2. Learning Objective
Explore input multiplexing (The Matrix Keypad). Learn how to scan a grid of 4 buttons using only 4 wires (2 Rows, 2 Columns) instead of 4 separate pins, saving resources by cycling power through pins strategically.

### 3. Concepts Introduced
*   **Row/Column Scanning**: Powering one row at a time and reading all column pins simultaneously.
*   **Multiplexing**: Using math to determine which intersection (Button) is closed.
*   **Pin Optimization**: reducing the number of GPIO pins needed for large numbers of buttons.

### 4. Hardware Required
*   Raspberry Pi Pico
*   4 Pushbuttons
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Row 1** | GP15 | Output pin |
| **Row 2** | GP14 | Output pin |
| **Col 1** | GP13 | Input pin |
| **Col 2** | GP12 | Input pin |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (powering rows)
*   **from Smart IO, drag `pico_gpio_read`** (reading cols)
*   **from Logic, drag `controls_if`** (matching coordinates)

### 7. Variables
*   **None**: this is a cyclical scanning process.

### 8. Step-by-Step Guide

**A. Preparation Phase**
1.  **Wiring**: 
    *   Connect Buttons 1 & 2 to Row 1 (GP15).
    *   Connect Buttons 3 & 4 to Row 2 (GP14).
    *   Connect Buttons 1 & 3 to Col 1 (GP13).
    *   Connect Buttons 2 & 4 to Col 2 (GP12).

**B. Scanning Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Scan Row 1**:
    *   **Set** GP15 (Row 1) -> HIGH. **Set** GP14 (Row 2) -> LOW.
    *   If **Col 1** (GP13) is HIGH: **Print** "Button 1 Pressed".
    *   If **Col 2** (GP12) is HIGH: **Print** "Button 2 Pressed".
4.  **Scan Row 2**:
    *   **Set** GP15 (Row 1) -> LOW. **Set** GP14 (Row 2) -> HIGH.
    *   If **Col 1** (GP13) is HIGH: **Print** "Button 3 Pressed".
    *   If **Col 2** (GP12) is HIGH: **Print** "Button 4 Pressed".

### 9. Execution Flow
1.  **Row 1**: The Pico sends power ONLY to the top row of buttons.
2.  **Read**: If you are pressing Button 3 (Row 2), the Pico won't see it yet because Row 2 is currently "Dead".
3.  **Row 2**: 1ms later, Row 1 shuts off and Row 2 turns on.
4.  **Match**: Now the power flows through your finger to Col 1. The Pico sees a "Match" on Row 2 / Col 1.
5.  **Result**: The Pico correctly identifies Button 3, even though it shares a Column wire with Button 1.

### 10. Generated Code
```python
from machine import Pin
import time

# Row Outputs
rows = [Pin(15, Pin.OUT), Pin(14, Pin.OUT)]
# Col Inputs
cols = [Pin(13, Pin.IN, Pin.PULL_DOWN), Pin(12, Pin.IN, Pin.PULL_DOWN)]

names = [["Btn 1", "Btn 2"], 
         ["Btn 3", "Btn 4"]]

while True:
    for r in range(2):
        # Power only ONE row at a time
        rows[r].value(1)
        
        for c in range(2):
            # Check all columns for that row
            if cols[c].value() == 1:
                print("Clicked: " + names[r][c])
                time.sleep(0.3) # Debounce
                
        # Turn it off before checking next row
        rows[r].value(0)
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Ghosting**: if you don't turn a row OFF before turning the next one ON, the Pico will think you are pressing multiple buttons at once.
*   **No Pull-Downs**: If the input columns aren't grounded, they will pick up interference and trigger "Ghost" clicks.

### 12. Try This Next
*   **Calculator Display**: show the button number on an OLED screen.
*   **Secret Code**: require the user to press 1-2-4 in order using the matrix.

---
