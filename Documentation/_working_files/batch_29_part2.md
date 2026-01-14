
## 1. Project 0286: Smart Counting Machine Switch

### 2. Learning Objective
Explore mathematical filtering (The Prime Counter). Learn how to implement software-level "Exclusion Rules" where a counter increment only triggers a response if the new value meets a complex mathematical criterion (Prime Status), demonstrating algorithmic data filtering.

### 3. Concepts Introduced
*   **Prime Number Logic**: identifying integers greater than 1 with no divisors other than 1 and themselves.
*   **Algorithmic Filtering**: using a `for` loop inside a conditional to check validity before output.
*   **Selective Reporting**: ignoring "noise" (composite numbers) to focus on "signals" (primes).

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Pushbutton
*   1 LED (Prime Indicator)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Number Btn** | GP14 | Increments the test value |
| **Prime LED** | GP15 | Validates the number |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (storing current number)
*   **from Logic, drag `controls_if`** (evaluating prime status)
*   **from Loops, drag `controls_repeat`** (checking divisors)

### 7. Variables
*   **num**: the number being tested.
*   **is_prime**: Boolean results.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Action**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `num` = `num` + 1.
        *   **Set** `is_prime` = True.

**B. Brain Phase (Filtering)**
3.  **Check for Primeness**:
    *   If `num` < 2: **Set** `is_prime` = False.
    *   Else:
        *   **Loop** `i` from 2 to (`num` - 1):
            *   If **Math** (`num` % `i`) == 0:
                *   **Set** `is_prime` = False. **Break**.

**C. Execution Phase**
4.  **Confirm to User**:
    *   If `is_prime` is True:
        *   **Print** "Number ", `num`, " is PRIME!".
        *   **Set** LED (GP15) -> HIGH.
    *   Else:
        *   **Print** "Number ", `num`, " is composite. Skipping...".
        *   **Set** LED -> LOW.

### 9. Execution Flow
1.  **Start**: num = 1. Not prime. LED off.
2.  **Press**: num = 2. The loop from 2 to 1 doesn't run. is_prime stays True. LED turns ON.
3.  **Press**: num = 3. 3%2 is not 0. is_prime stays True. LED stays ON.
4.  **Press**: num = 4. 4%2 is 0. is_prime becomes False. LED turns OFF.
5.  **Result**: The LED only stays on for the unique, non-divisible numbers in the series.
6.  **Outcome**: A smart counter that performs complex data analysis on every single click.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

num = 0

def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if btn.value() == 1:
        num += 1
        if check_prime(num):
            print(">>> " + str(num) + " IS PRIME <<<")
            led.value(1)
        else:
            print(str(num) + " - composite")
            led.value(0)
            
        time.sleep(0.3) # Debounce
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Missing 2**: People often forget that 2 is the only even prime number. Ensure your logic starts checking from 2 and handles it correctly.

### 12. Try This Next
*   **Fibonacci Counter**: change the filter so the LED only turns on for numbers in the Fibonacci sequence (1, 1, 2, 3, 5, 8...).

---

## 1. Project 0287: Counting Machine Alarm System

### 2. Learning Objective
Explore progressive urgency states (The Countdown to Destruction). Learn how to implement a reverse counter that triggers different hardware alerts at specific thresholds, simulating a safety system or a temporal warning before an event.

### 3. Concepts Introduced
*   **Reverse Accumulation**: Subtracting from a starting value (`Count = Count - 1`).
*   **Threshold States**: defining "Warning" vs "Danger" zones using multiple LEDs.
*   **Terminal Logic**: performing a final, non-reversible action when the count hits zero.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Yellow LED (Warning)
*   1 Red LED (Danger)
*   1 Buzzer (Alarm)
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Decrement Btn** | GP14 | Subtraction input |
| **Danger Zone** | GP15 | Red LED |
| **Warning Zone** | GP13 | Yellow LED |
| **Final Alarm** | GP12 | Buzzer |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (starting at 10)
*   **from Logic, drag `controls_if`** (multi-level if/else)
*   **from Smart IO, drag `pico_gpio_write`** (signaling)

### 7. Variables
*   **timer**: starts at 10. Decrements by 1.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup**: **Set** `timer` = 10. **Turn OFF** all alerts.

**B. Monitoring Phase (Loop)**
2.  **Handle Subtract**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `timer` = `timer` - 1. 
        *   **Wait** 0.3s.

**C. Brain Phase (The Warning Zones)**
3.  **Evaluate Thresholds**:
    *   If `timer` > 5: Keep all signals OFF.
    *   Else If `timer` > 2:
        *   **Set** Yellow LED (GP13) -> HIGH. **Print** "WARNING: LEVEL LOW".
    *   Else If `timer` > 0:
        *   **Set** Red LED (GP15) -> HIGH. **Print** "DANGER: CRITICAL LOW".
    *   Else (Limit reached):
        *   **Set** Buzzer -> HIGH. **Print** "SYSTEM SHUTDOWN ACTIVATED.".

### 9. Execution Flow
1.  **Start**: Timer is 10.
2.  **Decrement**: You press twice. Timer is 8. Nothing happens.
3.  **Warning**: You press until 5. The Yellow LED lights up. You know you are running out of "Time".
4.  **Panic**: You reach 2. The Red LED starts glowing. The situation is critical.
5.  **Final**: On the last press (0), the buzzer starts and doesn't stop.
6.  **Result**: An interactive countdown that communicates urgency through a multi-stage hardware interface.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

led_y = Pin(13, Pin.OUT)
led_r = Pin(15, Pin.OUT)
bz = PWM(Pin(12))
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

count = 10

while True:
    if btn.value() == 1:
        count -= 1
        print("T-Minus: " + str(count))
        
        # Urgency Logic
        if count > 5:
            pass # All safe
        elif count > 2:
            led_y.value(1) # Warning
        elif count > 0:
            led_r.value(1) # Danger
        else:
            # SHUTDOWN
            print("TERMINATED")
            while True:
                bz.freq(1000); bz.duty_u16(32768); time.sleep(0.1)
                bz.duty_u16(0); time.sleep(0.1)
                
        time.sleep(0.3)
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Zero Limit**: If you don't stop the counter at 0, your variable will go to -1, -2, etc., and the alarm might turn OFF because it's no longer "equal to 0". Always use an `else` or `< 1` check.

### 12. Try This Next
*   **Auto-Decrement**: make the timer go down by itself every 1 second, and use the button to "ADD" time (Project 0215).

---

## 1. Project 0288: The Counting Machine Game

### 2. Learning Objective
Explore bounded accumulation (The Blackjack Game). Learn how to create a game that uses a variable as a running total, adding random values and checking against a "Failure Condition" (Bust) after every action.

### 3. Concepts Introduced
*   **Running Accumulation**: `Total = Total + RandomValue`.
*   **Success Window**: Keeping a value between 0 and 21.
*   **Event Discrimination**: Using a single button for two different actions (e.g. Single Click for "Hit", Double Click for "Stay").

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Pushbutton
*   Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Hit/Stay Btn** | GP14 | Primary Interaction |
| **Speaker** | GP15 | Game feedback |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Math, drag `math_random_int`** (generating cards)
*   **from Variables, drag `variables_set`** (tracking total)
*   **from Logic, drag `controls_if`** (checking results)

### 7. Variables
*   **total_pts**: score for current hand.
*   **new_card**: value of newly drawn card (1-11).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Shuffle**: **Set** `total_pts` = 0. **Print** "New Game! Press to Hit.".

**B. "Hit" Phase (Round)**
2.  **Action**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `new_card` = **Math** `random 1 to 11`.
        *   **Set** `total_pts` = `total_pts` + `new_card`.
        *   **Print** "You drew a ", `new_card`, ". Total: ", `total_pts`.
        *   **Wait** 0.5s.

**C. Verification Phase**
3.  **Evaluate Hand**:
    *   If `total_pts` > 21:
        *   **Print** "BUST! You went over 21. Game Over.".
        *   **Play** Low Tone. **Set** `total_pts` = 0.
    *   If `total_pts` == 21:
        *   **Print** "BLACKJACK! YOU WIN!".
        *   **Play** High Fanfare. **Set** `total_pts` = 0.

### 9. Execution Flow
1.  **Draw**: You press the button. Pico says "4". Total is 4.
2.  **Draw**: You press again. Pico says "10". Total is 14.
3.  **Risk**: You press again. Pico says "8".
4.  **Verdict**: 14 + 8 = 22. 22 is greater than 21.
5.  **Result**: The Pico plays a "Sad" sound and tells you that you lost the game (Busted).
6.  **Outcome**: A fully functional probability game using only a single button and some variables.

### 10. Generated Code
```python
import machine
import utime
import urandom

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bz = machine.PWM(machine.Pin(15))

score = 0

print("Welcome to Pico Blackjack!")

while True:
    if btn.value() == 1:
        card = urandom.randint(1, 11)
        score += card
        print("Drawn: " + str(card) + " | Total: " + str(score))
        
        if score > 21:
            print("BUST! Game Over.")
            bz.freq(200); bz.duty_u16(30000); utime.sleep(0.5); bz.duty_u16(0)
            score = 0
            print("New Game Starting...")
        elif score == 21:
            print("BLACKJACK! WINNER!")
            bz.freq(1000); bz.duty_u16(30000); utime.sleep(0.1); bz.freq(1200); utime.sleep(0.5); bz.duty_u16(0)
            score = 0
            print("New Game Starting...")
            
        utime.sleep(0.5) # Wait for release
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Variable Decay**: ensure the `score` variable is only reset to zero *after* the win/loss is printed, or it will look like you busted on a score of 0.

### 12. Try This Next
*   **Stay Button**: Add a second button. If you press it, the Pico reveals its own "Dealer Score" and tells you who was closer to 21 without busting.

---

## 1. Project 0289: Automated Counting Machine

### 2. Learning Objective
Explore directional entry/exit counting (The Traffic Counter). Learn how to use a pair of sensors in sequence to identify the direction of motion, incrementing a counter for "Entries" and decrementing for "Exits" to track total occupancy.

### 3. Concepts Introduced
*   **State Machine Sequence**: Identifying that A-then-B means "In", while B-then-A means "Out".
*   **Temporal Sequencing**: detecting which sensor was triggered first.
*   **Occupancy Tracking**: maintaining an accurate count of objects within a specific area.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 IR Break-beam Sensors (or Ultrasonic)
*   MCB (Micro Color Block) or LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sensor A (Outer)** | GP14 | First detection point |
| **Sensor B (Inner)** | GP13 | Second detection point |
| **Occupancy Light** | GP15 | ON if count > 0 |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking occupancy)
*   **from Logic, drag `controls_if`** (evaluating sequence)
*   **from Time, drag `pico_wait`** (grace period)

### 7. Variables
*   **on_site**: Integer tracking people inside.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Entry Logic**
2.  **Detect Forward Move**:
    *   If **Sensor A** (Outer) is Triggered:
        *   Wait for **Sensor B** (Inner) to be Triggered within 2 seconds.
        *   If Success:
            *   **Set** `on_site` = `on_site` + 1.
            *   **Print** "Person ENTERED. Total site count: ", `on_site`.

**C. Exit Logic**
3.  **Detect Reverse Move**:
    *   If **Sensor B** (Inner) is Triggered:
        *   Wait for **Sensor A** (Outer) to be Triggered within 2 seconds.
        *   If Success:
            *   **Set** `on_site` = `on_site` - 1.
            *   **Print** "Person EXITED. Total site count: ", `on_site`.

**D. Maintenance Phase**
4.  **Visualize Status**:
    *   If `on_site` > 0: **Set** LED (GP15) -> HIGH.
    *   Else: **Set** LED -> LOW.

### 9. Execution Flow
1.  **Entering**: You walk through the gate. You pass Sensor A first, then Sensor B. The Pico registers a (+1).
2.  **Tracking**: The display shows "1 person on site".
3.  **Exiting**: You walk back out. You hit Sensor B first, then A. The Pico registers a (-1).
4.  **Result**: The occupancy count returns to 0 and the light turns off.
5.  **Outcome**: A smart room system that knows exactly how many people are inside at any time.

### 10. Generated Code
```python
from machine import Pin
import time

s_outer = Pin(14, Pin.IN)
s_inner = Pin(13, Pin.IN)
led = Pin(15, Pin.OUT)

occupancy = 0

while True:
    # 1. Entry Check
    if s_outer.value() == 0: # Object detected
        # Wait for inner sensor to trigger
        start = time.ticks_ms()
        ok = False
        while time.ticks_diff(time.ticks_ms(), start) < 2000:
            if s_inner.value() == 0:
                ok = True
                break
        if ok:
            occupancy += 1
            print("ENTERED: " + str(occupancy))
            time.sleep(1) # Prevent re-trigger
            
    # 2. Exit Check
    if s_inner.value() == 0:
        start = time.ticks_ms()
        ok = False
        while time.ticks_diff(time.ticks_ms(), start) < 2000:
            if s_outer.value() == 0:
                ok = True
                break
        if ok:
            occupancy -= 1
            if occupancy < 0: occupancy = 0
            print("EXITED: " + str(occupancy))
            time.sleep(1)
            
    # 3. Light Status
    if occupancy > 0: led.value(1)
    else: led.value(0)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Missing Timeout**: If you don't use a "Wait 2 seconds" window, the computer might wait FOREVER for the second sensor to trigger, effectively breaking the whole machine.

### 12. Try This Next
*   **Max Capacity**: make the buzzer beep if the occupancy count exceeds 5 people.
*   **Speed Check**: use the time between A and B to calculate how fast the person was walking.

---

## 1. Project 0290: Mastering Counting Machine

### 2. Learning Objective
Explore dynamic data visualization (The OLED Growth Chart). Learn how to map a numerical variable (The Count) to physical coordinate geometry (y-axis) on a digital screen, creating a bar chart that grows in size as you accumulate data.

### 3. Concepts Introduced
*   **Dynamic Scaling**: adjusting the height of a graphical element based on variable value.
*   **Coordinate Systems**: understanding (x, y) placement on a 128x64 OLED screen.
*   **Canvas Clearing**: erasing the old bar before drawing the new, taller one to animate the growth.

### 4. Hardware Required
*   Raspberry Pi Pico
*   I2C OLED Display (128x64)
*   1 Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **SDA / SCL** | GP0, GP1 | OLED Communication |
| **Input Button** | GP14 | Item trigger |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Displays, drag `pico_oled_rect`** (draw the bar)
*   **from Variables, drag `variables_set`** (tracking count)
*   **from Smart IO, drag `pico_gpio_read`** (read button)
*   **from Displays, drag `pico_oled_clear`** (screen reset)

### 7. Variables
*   **count**: total items.
*   **bar_height**: the Y-dimension of the rectangle.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Connect Screen**: Initialize the OLED on I2C0.
2.  **Zero State**: **Set** `count` = 0.

**B. Data Phase (Loop)**
3.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
4.  **Capture Action**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `count` = `count` + 1.
        *   **Set** `bar_height` = `count` * 2 (Scaling factor of 2).

**C. Visualization Phase**
5.  **Refresh Screen**:
    *   From **Displays**, **Clear Screen**.
    *   **Draw Text**: "Total items: " + `count` at (0, 0).
    *   **Draw Rectangle**:
        *   X: 40, Y: (64 - `bar_height`).
        *   Width: 20.
        *   Height: `bar_height`.
6.  **Apply**: **Show Display**. **Wait** 0.1s.

### 9. Execution Flow
1.  **Start**: Screen is empty. Count is 0.
2.  **Click**: You press once. The Pico calculates height = 2. It draws a tiny 2-pixel tall line at the bottom.
3.  **Progress**: You press 20 times. Height is now 40 pixels.
4.  **Result**: The screen shows a thick vertical bar that has literally "Grown" taller with your efforts.
5.  **Outcome**: Learning how to turn abstract numbers into understandable visual information.

### 10. Generated Code
```python
import machine
import ssd1306 # Standard library
import utime

# OLED and Button
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

count = 0

while True:
    if btn.value() == 1:
        count += 1
        # Draw Updated Chart
        oled.fill(0)
        oled.text("COUNT: " + str(count), 0, 0)
        
        # Draw Bar (starts from bottom Y=63)
        h = count * 2
        if h > 50: h = 50 # Cap at screen top
        oled.rect(50, 64-h, 20, h, 1) # x, y, w, h, color
        oled.show()
        
        utime.sleep(0.2)
        
    utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Y-Axis Direction**: On most OLEDs, Y=0 is the TOP of the screen. To make a bar grow from the BOTTOM, you must calculate the starting Y point as `64 - height`.
*   **Scale Overload**: If you click 100 times, the bar will go off the top of the screen. Make sure to use a `limit` or `map` block to keep the bar inside the 64-pixel limit.

### 12. Try This Next
*   **Multi-Bar**: add a second button and draw a second bar next to the first one to compare two different counts!
*   **Horizontal Bar**: change the logic to make the bar grow from Left to Right.

---
