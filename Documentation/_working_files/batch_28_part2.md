
## 1. Project 0276: Smart Reaction Game Switch

### 2. Learning Objective
Explore haptic-reflex measurement (The Vibration Cue). Learn how to use a vibration motor (or a low-frequency buzzer pulse) as the signal for a high-speed reaction test, demonstrating that humans often react faster to physical touch than to visual or auditory signals.

### 3. Concepts Introduced
*   **Haptic Stimulus**: using physical vibration to communicate a trigger to the user.
*   **Proprioceptive Response**: the brain's ability to react to movement against the skin.
*   **Rapid Pin Modulation**: toggling a motor for a short duration to create a distinct pulse.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Vibration Motor (or Passive Buzzer)
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Haptic Motor** | GP15 | "Vibrate" signal |
| **Action Btn** | GP14 | Capture response |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Motor)
*   **from Time, drag `pico_time_ms`** (measuring speed)
*   **from Time, drag `pico_wait`** (randomized delay)
*   **from Variables, drag `variables_set`** (tracking time)

### 7. Variables
*   **start_t, end_t**: timestamps.
*   **haptic_speed**: calculated milliseconds.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Anticipation Phase**:
    *   **Wait** random (2 to 4) seconds.

**B. Stimulus Phase**
3.  **Pulse the Motor**:
    *   **Set** GP15 -> HIGH.
    *   **Set** `start_t` = **Time** `pico_time_ms`.

**C. Detection Phase**
4.  **Wait for Response**:
    *   Repeat-until **Button** GP14 is Pressed.
    *   **Set** `end_t` = **Time** `pico_time_ms`.
    *   **Set** GP15 -> LOW.

**D. Scoring Phase**
5.  **Output Data**:
    *   **Set** `haptic_speed` = `end_t` - `start_t`.
    *   **Print** "Haptic Reaction: ", `haptic_speed`, "ms".

### 9. Execution Flow
1.  **Wait**: You hold the button or the breadboard.
2.  **Trigger**: The board suddenly vibrates in your hand.
3.  **Action**: You mash the button instantly.
4.  **Math**: The Pico calculates the time (likely under 200ms).
5.  **Result**: You see your score. Most people find they are 20-30ms faster with vibration than with a light!
6.  **Outcome**: Understanding different sensory pathways in the human nervous system.

### 10. Generated Code
```python
from machine import Pin
import time
import urandom

vib = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print("Hold the board... waiting for vibration.")
    time.sleep(urandom.randint(2, 4))
    
    # PULSE
    vib.value(1)
    t1 = time.ticks_ms()
    
    # Poll for response
    while btn.value() == 0: pass
    
    t2 = time.ticks_ms()
    vib.value(0)
    
    print("Vibration Reaction: " + str(time.ticks_diff(t2, t1)) + "ms")
    time.sleep(2)
```

### 11. Common Mistakes
*   **Motor Drain**: A vibration motor can draw a lot of current. If the Pico resets when it vibrates, you may need a transistor or a small battery to power the motor safely.

### 12. Try This Next
*   **Double Pulse**: vibrate once (distraction), then wait exactly 0.5s and vibrate again (the real trigger).
*   **Vibration Strength**: try to use PWM (Project 0232) to vary how "Strong" the vibration is and see if you react faster to stronger tickles.

---

## 1. Project 0277: Reaction Game Alarm System

### 2. Learning Objective
Explore vigilance monitoring (The Sleepy Driver Alarm). Learn how to implement a safety system that monitors for a specific user action within a "Time-Out" window (1.0 second), triggering a high-priority audible alarm if the user fails to respond.

### 3. Concepts Introduced
*   **Vigilance Testing**: measuring the ability to maintain attention over time.
*   **Time-Out Logic**: using code to trigger an event if *nothing* happens for too long.
*   **Emergency Overrides**: playing a loud buzzer only when a "Safety Window" is missed.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED (Signal)
*   1 Button (Check-in)
*   1 Loud Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Check LED** | GP15 | Prompt for response |
| **Wake Button** | GP14 | Driver reset |
| **Loud Siren** | GP13 | Emergency alert |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating failure)
*   **from Time, drag `pico_time_ms`** (window tracking)
*   **from Actuators, drag `pico_buzzer_pitch`** (alarm)

### 7. Variables
*   **missed_window**: Boolean tracking if the driver is "asleep".

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Periodic Check**:
    *   **Wait** 10 seconds.
    *   **Turn ON** LED (GP15).
    *   **Set** `start_t` = **Time** `pico_time_ms`.

**B. Evaluation Phase**
3.  **The Window**:
    *   Check for **Button** GP14 for exactly 1.0 seconds.
    *   If **Button** is Pressed:
        *   **Turn OFF** LED. **Print** "Driver Alert. Continuing...".
    *   Else (Time ran out):
        *   **Go to Alarm Phase**.

**C. Alarm Phase**
4.  **WAKE UP!**:
    *   **Set** Buzzer to 2000Hz (BEEP BEEP!).
    *   **Print** "EMERGENCY: DRIVER INACTIVE. SOUNDING ALARM.".
    *   Wait until button is eventually pressed to silence.

### 9. Execution Flow
1.  **Normal**: Every 10 seconds, the Blue LED lights up. You tap the button within 1s. The Pico is happy.
2.  **Fatigue**: You miss the light. 1 full second passes.
3.  **Reaction**: The Pico sees the empty window. It immediately triggers the 2000Hz siren.
4.  **Safety**: The noise wakes you up. You hit the button to stop the noise.
5.  **Result**: A smart car safety feature that prevents accidents by monitoring driver attentiveness.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = PWM(Pin(13))

while True:
    # 1. Wait
    print("Monitoring driver...")
    time.sleep(5) # Shorter for testing
    
    # 2. Trigger Check
    led.value(1)
    t1 = time.ticks_ms()
    hit = False
    
    # Check for 1 second
    while time.ticks_diff(time.ticks_ms(), t1) < 1000:
        if btn.value():
            hit = True
            break
        time.sleep(0.01)
        
    led.value(0)
    
    if not hit:
        # FAILED TO RESPOND
        print("!!! DRIVER ASLEEP !!!")
        while btn.value() == 0:
            bz.freq(2000); bz.duty_u16(40000); time.sleep(0.1)
            bz.duty_u16(0); time.sleep(0.1)
        
    time.sleep(1)
```

### 11. Common Mistakes
*   **Window too Short**: if the window is 0.2s, a normal human might be marked as "Asleep" just for blinking. 1.0s is the industrial standard for alertness checks.

### 12. Try This Next
*   **Slower Alarm**: make the alarm get progressively louder if they don't press the button.
*   **Logging**: count how many times they "fell asleep" and print it.

---

## 1. Project 0278: The Reaction Game Game

### 2. Learning Objective
Explore multi-input arbitration (The Duel). Learn how to implement a shared trigger where the system monitors two independent inputs simultaneously and uses logic to identify and announce the specific winner, handling simultaneous "Ties" fairly.

### 3. Concepts Introduced
*   **Interrupt-style Polling**: checking multiple pins in a single fast loop.
*   **Priority Resolution**: deciding who was "First" in a competitive environment.
*   **Simultaneous Handling**: logic that accounts for two inputs arriving in the same microsecond.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Player A and Player B)
*   1 Center LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Center Light** | GP15 | Start signal |
| **Player A Btn** | GP14 | Left Side |
| **Player B Btn** | GP13 | Right Side |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating winner)
*   **from Time, drag `pico_wait`** (randomized start)
*   **from Smart IO, drag `pico_gpio_write`** (signal start)

### 7. Variables
*   **winner**: String ("A", "B", or "Tie").

### 8. Step-by-Step Guide

**A. Preparation Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Anticipation**:
    *   **Wait** 2 to 5 seconds.
    *   **Turn ON** LED (GP15).

**B. Resolution Phase**
3.  **The Race**:
    *   Inside a "Wait-Until" loop:
    *   If **Button A** is Down AND **Button B** is Down:
        *   **Set** `winner` = "TIE! DRAW YOUR SWORDS!".
        *   **Break** loop.
    *   Else If **Button A** is Down:
        *   **Set** `winner` = "PLAYER A WINS!".
        *   **Break** loop.
    *   Else If **Button B** is Down:
        *   **Set** `winner` = "PLAYER B WINS!".
        *   **Break** loop.

**C. Reward Phase**
4.  **Declare Victor**:
    *   **Turn OFF** LED.
    *   **Print** `winner`.
    *   **Wait** 3s before next duel.

### 9. Execution Flow
1.  **Standoff**: Two players sit with fingers poised.
2.  **Draw**: The light flashes.
3.  **Clash**: Player A is slightly faster.
4.  **Logic**: The Pico sees Pin 14 go HIGH during its scan. It immediately stops looking and records "A" as the victor.
5.  **Result**: An electronic referee that is 100% fair and immune to human bias.

### 10. Generated Code
```python
from machine import Pin
import time
import urandom

led = Pin(15, Pin.OUT)
p1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
p2 = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    print("READY... SET...")
    led.value(0)
    time.sleep(urandom.randint(2, 5))
    
    # GO!
    led.value(1)
    winner = ""
    
    while True:
        v1 = p1.value()
        v2 = p2.value()
        
        if v1 and v2:
            winner = "TIE!"
            break
        elif v1:
            winner = "PLAYER 1"
            break
        elif v2:
            winner = "PLAYER 2"
            break
        time.sleep_us(100) # Fast scan
        
    led.value(0)
    print("Result: " + winner)
    time.sleep(3)
```

### 11. Common Mistakes
*   **False Start**: If you don't check for button presses *before* the light turns on, players might just hold the button down to trick the system. Always clear the input states before the "GO" signal.

### 12. Try This Next
*   **Reaction Score**: print exactly how many milliseconds separated the two players (e.g. "A won by 15ms!").
*   **Series Game**: play to "Best of 3 wins".

---

## 1. Project 0279: Automated Reaction Game

### 2. Learning Objective
Explore predictive synchronization (The Anticipation Test). Learn how to implement a system that generates a steady rhythmic pulse and then challenges the user to "Predict" the next beat, testing the brain's internal clock and pattern-internalization.

### 3. Concepts Introduced
*   **Synchronization Errors**: measuring the difference between a user's press and a "Virtual" clock pulse.
*   **Rhythmic Entrainment**: the brain's ability to lock onto a steady tempo.
*   **Invisible Triggers**: performing an action based on a calculated time rather than a physical sensor.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Metro LED** | GP15 | Pattern signal |
| **Sync Btn** | GP14 | User prediction |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking rhythm)
*   **from Logic, drag `controls_if`** (evaluating sync)
*   **from Time, drag `pico_time_ms`** (measuring offset)

### 7. Variables
*   **tempo**: 1000ms.
*   **error**: difference between expected beat and actual press.

### 8. Step-by-Step Guide

**A. Calibration Phase**
1.  **Set Tempo**: **Turn ON** LED for 0.1s every 1.0 second.
2.  **Run Pattern**: Do this 5 times so the user hears/sees the steady beat.

**B. Silent Phase**
3.  **Stop Stimulus**:
    *   **Keep** the LED OFF.
    *   **Calculate** when the next "Pulse" SHOULD have happened (e.g. at 6.0 seconds).

**C. Anticipation Phase**
4.  **Capture Prediction**:
    *   Wait for **Button** GP14.
    *   **Compare** button press time to the "Virtual Pulse" time.
5.  **Score**:
    *   If `error` < 50ms: **Success!** "YOU ARE A HUMAN CLOCK!".
    *   Else: "Too early/late by ", `error`, "ms".

### 9. Execution Flow
1.  **Watch**: The light blinks 1-2-3-4-5.
2.  **Predict**: The light stops. In your head, you count "6!".
3.  **Action**: You press the button on exactly "6".
4.  **Math**: The Pico was silently counting too. It compares your "6" to its "6".
5.  **Result**: You see how perfectly your "Internal Clock" matches the computer's clock.

### 10. Generated Code
```python
import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

tempo = 1000 # 1 second beat

while True:
    print("Listen to the rhythm...")
    for _ in range(3):
        led.value(1); utime.sleep(0.1); led.value(0)
        utime.sleep(0.9)
        
    print("NOW PREDICT THE NEXT BEAT!")
    # We expect the next beat at exactly 'tempo' ms after the last one
    expect = utime.ticks_ms() + tempo
    
    # Wait for user input
    while btn.value() == 0: pass
    actual = utime.ticks_ms()
    
    diff = utime.ticks_diff(actual, expect)
    led.value(1); utime.sleep(0.1); led.value(0) # Flash to show the press
    
    print("Anticipation Error: " + str(diff) + "ms")
    if abs(diff) < 100:
        print("PERFECT SYNC!")
    
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Too Few Beeps**: If the Pico only blinks twice, the brain doesn't have enough time to "Lock on" to the rhythm. Always give at least 3-5 example pulses first.

### 12. Try This Next
*   **Acceleration**: Make the rhythm get faster and faster.
*   **Double Sync**: you have to press on the 7th AND 8th beat correctly.

---

## 1. Project 0280: Mastering Reaction Game

### 2. Learning Objective
Explore statistical processing (The Average Reaction). Learn how to use arithmetic variables to calculate the mathematical Mean (Average) of multiple data points, providing a more reliable measure of performance than a single "Lucky" attempt.

### 3. Concepts Introduced
*   **Data Aggregation**: summing multiple values into a single "Total" variable.
*   **Arithmetic Mean**: dividing the sum by the count (`Total / 5`).
*   **Statistical Variance**: noticing how reaction times fluctuate across different attempts.

### 4. Hardware Required
*   Raspberry Pi Pico
*   LED
*   Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Signal Light** | GP15 | Visual stimulus |
| **Response Btn** | GP14 | Data input |

### 6. Blocks Used
*   **from Loops, drag `controls_repeat`** (do 5 times)
*   **from Variables, drag `variables_set`** (tracking sum)
*   **from Math, drag `math_arithmetic`** (summing and dividing)
*   **from Smart IO, drag `pico_gpio_write`** (set Signal)

### 7. Variables
*   **total_time**: running sum of all scores.
*   **avg_score**: the final result.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Reset Stats**: **Set** `total_time` = 0.

**B. Data Collection Phase (Repeat 5)**
2.  **Run Round**:
    *   Wait random delay. **Turn ON** LED.
    *   Wait for **Button** GP14. **Stop** timer.
    *   **Set** `current_score` = milliseconds.
3.  **Accumulate**:
    *   **Set** `total_time` = `total_time` + `current_score`.
    *   **Print** "Round ", `count`, " complete.".

**C. Calculation Phase**
4.  **The Mean**:
    *   **Set** `avg_score` = `total_time` / 5.
5.  **Final Report**:
    *   **Print** "--- FINAL REPORT ---".
    *   **Print** "Total Time (Sum): ", `total_time`.
    *   **Print** "Average Reaction Speed: ", `avg_score`, "ms".

### 9. Execution Flow
1.  **Trial**: You play 5 rounds. Your scores are: 200, 250, 180, 220, 210.
2.  **Sum**: The Pico adds them up to get 1060.
3.  **Divide**: It divides 1060 by 5.
4.  **Result**: 212ms.
5.  **Outcome**: You now have a scientifically accurate "Baseline" for your reaction speed that ignores one really fast or one really slow click.

### 10. Generated Code
```python
import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

total = 0
rounds = 5

print("Starting 5-Round Baseline Test...")

for i in range(1, rounds + 1):
    utime.sleep(urandom.randint(1, 3))
    led.value(1)
    t1 = utime.ticks_ms()
    
    while btn.value() == 0: pass
    t2 = utime.ticks_ms()
    led.value(0)
    
    score = utime.ticks_diff(t2, t1)
    total += score
    print("Round " + str(i) + ": " + str(score) + "ms")
    utime.sleep(1)

avg = total / rounds
print("--- FINAL RESULT ---")
print("Total: " + str(total) + "ms")
print("AVERAGE: " + str(avg) + "ms")
```

### 11. Common Mistakes
*   **Integer Math**: Ensure your code uses decimals for the average so a score of 212.5 doesn't get rounded down to 212.
*   **No Reset**: if you don't reset `total` to 0, your next set of 5 rounds will be added to the previous set, resulting in a huge number!

### 12. Try This Next
*   **Compare to Best**: Print how far the average is from your "Best" single round.
*   **Rank System**: If average < 200ms print "Rank: Professional", if < 300ms "Rank: Amateur".

---
