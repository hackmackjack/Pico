
# BATCH 28: Reaction Game 2 (Projects 0271-0280)

## 1. Project 0271: Introduction to Reaction Game

### 2. Learning Objective
Explore acoustic-reflex measurement (Sound Start). Learn how to implement a system that uses an audio cue (Beep) as the signal for a high-speed reaction test, allowing for comparison between auditory and visual reaction speeds.

### 3. Concepts Introduced
*   **Auditory Stimulus**: using sound as the trigger for a user action.
*   **Latency Measurement**: calculating the time between a beep and a button press.
*   **Reaction Windows**: the temporal period during which a user's input is valid.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Pushbutton
*   Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Reaction Button** | GP14 | Capture press |
| **System Buzzer** | GP15 | Start signal |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Time, drag `pico_wait`** (randomized delay)
*   **from Time, drag `pico_time_ms`** (measuring speed)
*   **from Actuators, drag `pico_buzzer_pitch`** (auditory cue)
*   **from Logic, drag `controls_if`** (evaluating result)

### 7. Variables
*   **start_t, end_t**: timestamps for math.
*   **speed**: final reaction score.

### 8. Step-by-Step Guide

**A. Preparation Phase**
1.  **Randomize Start**:
    *   **Print** "Game starting... Get ready for the Beep!".
    *   From **Math**, **Wait** a random (2 to 5) seconds.

**B. Stimulus Phase**
2.  **Sound the Alarm**:
    *   **Set** Buzzer to 1000Hz.
    *   **Set** `start_t` = **Time** `pico_time_ms`.

**C. Detection Phase**
3.  **Wait for User**:
    *   Wait until **Button** GP14 is Pressed.
    *   **Set** `end_t` = **Time** `pico_time_ms`.
    *   **Set** Buzzer to OFF.

**D. Scoring Phase**
4.  **Calculate Results**:
    *   **Set** `speed` = `end_t` - `start_t`.
    *   **Print** "Reaction Time: ", `speed`, "ms".
    *   **Wait** 2s before the game restarts.

### 9. Execution Flow
1.  **Anticipation**: You sit in silence for 3.4 seconds. Your ears are alert.
2.  **Trigger**: The buzzer beeps.
3.  **Action**: You smash the button.
4.  **Math**: The Pico calculates that 215 milliseconds passed.
5.  **Result**: You see your score on the screen and try to beat it next time.
6.  **Outcome**: Understanding how our brain processes sound faster than light.

### 10. Generated Code
```python
import machine
import utime
import urandom

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bz = machine.PWM(machine.Pin(15))

while True:
    print("Wait for the BEEP...")
    utime.sleep(urandom.randint(2, 5))
    
    # Stimulus
    bz.freq(1000); bz.duty_u16(32768)
    t1 = utime.ticks_ms()
    
    # Wait for press
    while btn.value() == 0:
        pass
    
    t2 = utime.ticks_ms()
    bz.duty_u16(0)
    
    # Calculate
    score = utime.ticks_diff(t2, t1)
    print("Reaction: " + str(score) + "ms")
    
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Cheating**: If the user holds the button down *before* the beep, your code might record a 0ms reaction. You should add a check: if button is down before the beep, print "FALSE START!".

### 12. Try This Next
*   **Pitch Variation**: make the beep a random frequency every time.
*   **Visual vs Audio**: switch between a Red LED and a Buzzer and see which one you are faster at responding to.

---

## 1. Project 0272: Blinking Reaction Game

### 2. Learning Objective
Explore selective attention (Flash Distraction). Learn how to implement a game that uses "Distractor" signals (Wrong colors) to test the user's focus, ensuring they only react to the "Target" signal (Green) while ignoring others.

### 3. Concepts Introduced
*   **Selective Response**: suppressing an action in response to a non-target stimulus.
*   **Distractor Signals**: random events intended to cause a "False Start".
*   **Conditional Validation**: only checking the timer if the target condition is met.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Red LED (Distractor)
*   Green LED (Target)
*   Pushbutton
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Target LED (G)** | GP15 | Press on this |
| **Fake LED (R)** | GP14 | IGNORE THIS |
| **Action Btn** | GP13 | Input sensor |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating color)
*   **from Math, drag `math_random_int`** (picking event)
*   **from Smart IO, drag `pico_gpio_write`** (set LED)

### 7. Variables
*   **event_type**: choice between Red, Green, or "No Light".

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Distraction Phase**
2.  **Roll the Dice**:
    *   **Set** `event_type` = **Math** `random integer from 1 to 3`.
3.  **Execute Event**:
    *   If `event_type` is 1 (RED):
        *   **Flashing** Red for 0.5s. **Continue Loop.**
    *   If `event_type` is 2 (NO LIGHT):
        *   **Wait** 1s. **Continue Loop.**
    *   If `event_type` is 3 (GREEN):
        *   **GO TO SIGNAL PHASE**.

**C. Signal Phase**
4.  **Launch Target**:
    *   **Set** Green (GP15) -> HIGH.
    *   **Start** timer.

**D. Validation Phase**
5.  **Check Press**:
    *   If Button pressed: **Print** "Success!".
    *   If Button was pressed during a Red flash: **Print** "PENALTY: WRONG LIGHT!".

### 9. Execution Flow
1.  **Wait**: You watch the LEDs. Red flashes. You hold your finger steady.
2.  **Distract**: Red flashes again. You almost press but stop.
3.  **Target**: Green lights up!
4.  **Action**: You mash the button.
5.  **Result**: The Pico acknowledges you only reacted to the correct "Target" stimulus.
6.  **Outcome**: Improved mental focus and selective motor control.

### 10. Generated Code
```python
import machine
import utime
import urandom

led_r = machine.Pin(14, machine.Pin.OUT)
led_g = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    choice = urandom.randint(1, 3)
    
    if choice == 1:
        # DISTRACTOR
        led_r.value(1); utime.sleep(0.5); led_r.value(0)
        # If they press during Red, it's a fail
        if btn.value(): print("CAUGHT! You pressed on RED.")
        utime.sleep(urandom.randint(1, 2))
        
    elif choice == 2:
        # SILENCE
        utime.sleep(1)
        
    else:
        # TARGET
        led_g.value(1)
        t1 = utime.ticks_ms()
        while btn.value() == 0: pass
        t2 = utime.ticks_ms()
        led_g.value(0)
        print("Success! Time: " + str(utime.ticks_diff(t2, t1)) + "ms")
        utime.sleep(2)
```

### 11. Common Mistakes
*   **Simple Loops**: If your code just does `blink Red, blink Green`, the user will learn the pattern. You MUST use the `random` block to make the distractions unpredictable.

### 12. Try This Next
*   **Triple Threat**: add a Blue LED and say "Press Blue for half-points, Green for full points.".
*   **Buzzer distraction**: play a mean "Wrong" sound if they press during the Red flash.

---

## 1. Project 0273: Manual Reaction Game Control

### 2. Learning Objective
Explore state persistence (The High Score). Learn how to use variables to store the "Best" result across multiple game rounds, comparing the current performance to the historical record and updating it conditionally.

### 3. Concepts Introduced
*   **Record Keeping**: using a variable to hold the "Global Minimum" value.
*   **Conditional Update**: using `if NEW < BEST: BEST = NEW`.
*   **Victory Feedback**: playing a special animation when a new record is achieved.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   2 LEDs (Standard and "Record" indicator)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Action Btn** | GP14 | Capture speed |
| **New Record LED** | GP15 | Flash on best time |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking best time)
*   **from Logic, drag `controls_if`** (record comparison)
*   **from Math, drag `math_arithmetic`** (speed math)

### 7. Variables
*   **best_time**: Number tracking the lowest score across all rounds.
*   **current_time**: score for the current attempt.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Impossible Record**: From **Variables**, **Set** `best_time` = 9999.
    *   *Note: We start high so the first press is guaranteed to be a record.*

**B. Gameplay Phase (Loop)**
2.  **Run Round**:
    *   **Wait** random time. **Turn ON** light.
    *   Wait for **Button** GP14. **Stop** timer.
    *   **Set** `current_time` = calculated milliseconds.

**C. Scoring Phase**
3.  **Check for Record**:
    *   If **Logic** `current_time` < `best_time`:
        *   **Print** "NEW HIGH SCORE!".
        *   **Set** `best_time` = `current_time`.
        *   **Flash** LED (GP15) 10 times.
    *   Else:
        *   **Print** "Nice try. Current: ", `current_time`, " | Best: ", `best_time`.

### 9. Execution Flow
1.  **Start**: Best time is 9999.
2.  **Round 1**: You press in 300ms. 300 is less than 9999. The Pico flashes the "Record" light. `best_time` is now 300.
3.  **Round 2**: You press in 450ms. 450 is NOT less than 300. The light stays OFF.
4.  **Round 3**: You press in 250ms. 250 < 300. New record! Flashing lights!
5.  **Result**: A competitive game that keeps track of your improvement.

### 10. Generated Code
```python
import machine
import utime
import urandom

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_t = machine.Pin(15, machine.Pin.OUT) # Signal light
led_r = machine.Pin(13, machine.Pin.OUT) # Record light

best_time = 9999

while True:
    utime.sleep(urandom.randint(1, 3))
    led_t.value(1)
    t1 = utime.ticks_ms()
    
    while btn.value() == 0: pass
    t2 = utime.ticks_ms()
    led_t.value(0)
    
    score = utime.ticks_diff(t2, t1)
    print("Time: " + str(score) + "ms")
    
    if score < best_time:
        best_time = score
        print("!!! NEW BEST RECORD !!!")
        # Record Animation
        for _ in range(5):
            led_r.value(1); utime.sleep(0.1); led_r.value(0); utime.sleep(0.1)
    
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Forgetting Initialization**: If you don't set `best_time` high at the start, the first press might not trigger the "New Record" flash, which feels confusing for the player.

### 12. Try This Next
*   **Serial Plotter**: Use the computer's graph view to see your reaction times improving over 10 rounds.
*   **Save to File**: Try to save the best time so it stays even if you unplug the Pico (Project 0293).

---

## 1. Project 0274: Reaction Game Sequences

### 2. Learning Objective
Explore rhythm replication (The Copy Cat). Learn how to implement a system that plays a sequence of sounds and then monitors the user's inputs to see if they can mimic the timing and duration of those sounds.

### 3. Concepts Introduced
*   **Array Comparison (Temporal)**: checking a sequence of time values against a target sequence.
*   **Tolerance/Error Margin**: Allowing the user to be "Close" to the rhythm without requiring mathematical perfection.
*   **Recording User Rhythm**: Using a list or variables to store multiple button press durations.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer
*   1 Button
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Speaker** | GP15 | Play the pattern |
| **Input Btn** | GP14 | Mimic the pattern |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_buzzer_pitch`** (output)
*   **from Variables, drag `variables_set`** (tracking pattern)
*   **from Logic, drag `controls_if`** (evaluating match)

### 7. Variables
*   **target_gap**: the time between Pico beeps.
*   **user_gap**: the time between user clicks.

### 8. Step-by-Step Guide

**A. Presentation Phase**
1.  **Play Rhythm**: 
    *   **Beep** once. **Wait** 0.5s. **Beep** once.
    *   **Set** `target_gap` = 500ms.
    *   **Print** "Pico: Click... Click. Your turn!".

**B. Recording Phase**
2.  **Wait for User 1**:
    *   Wait until **Button** GP14 Pressed/Released.
    *   **Set** `t1` = timestamp.
3.  **Wait for User 2**:
    *   Wait until **Button** GP14 Pressed.
    *   **Set** `t2` = timestamp.

**C. Validation Phase**
4.  **Compare**:
    *   **Set** `user_gap` = `t2` - `t1`.
    *   If **Math** `absolute(user_gap - target_gap)` < 100:
        *   **Print** "PERFECT RHYTHM MATCH!".
    *   Else:
        *   **Print** "Wrong timing. User: ", `user_gap`.

### 9. Execution Flow
1.  **Observe**: The Pico beeps: "B-Beb-B".
2.  **Mimic**: You try to click the button with the same rhythm.
3.  **Verify**: The Pico measures the gaps between your clicks. If you are within 100ms of its timing, you win.
4.  **Result**: An interactive musical game that tests memory and rhythmic coordination.

### 10. Generated Code
```python
import machine
import utime

bz = machine.PWM(machine.Pin(15))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# FIXED LEVEL: 0.5s gap
target = 500

while True:
    print("Pico: Beep ... (0.5s) ... Beep")
    bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.1); bz.duty_u16(0)
    utime.sleep(0.5)
    bz.freq(1000); bz.duty_u16(20000); utime.sleep(0.1); bz.duty_u16(0)
    
    print("Now Copy Me!")
    
    # Measure User Gap
    # 1. Wait for first release
    while btn.value() == 0: pass
    while btn.value() == 1: pass
    t1 = utime.ticks_ms()
    
    # 2. Wait for second press
    while btn.value() == 0: pass
    t2 = utime.ticks_ms()
    
    user_gap = utime.ticks_diff(t2, t1)
    
    if abs(user_gap - target) < 150: # 150ms tolerance
        print("MATCH! Diff: " + str(user_gap))
    else:
        print("FAIL! You were at: " + str(user_gap) + "ms")
        
    utime.sleep(2)
```

### 11. Common Mistakes
*   **Too Strict**: If you don't use a "Tolerance" (e.g. within 100ms), it's nearly impossible for a human to win because our fingers aren't as precise as microchips.

### 12. Try This Next
*   **Length Copy**: change it so you have to copy the DURATION of the first beep (how long you hold the button).
*   **Variable Patterns**: make the Pico randomly choose between a Fast rhythm and a Slow rhythm.

---

## 1. Project 0275: Interactive Reaction Game

### 2. Learning Objective
Explore progressive difficulty scaling (Endurance Mode). Learn how to use a variable to store the "Level Delay" and decrease it at the end of every successful round, making the game increasingly difficult to sustain.

### 3. Concepts Introduced
*   **Iterative Difficulty**: reducing response windows per round.
*   **Fatigue Testing**: measuring how many correct actions can be performed as speed increases.
*   **Variable-Based Loops**: using a variable as the `wait` duration for a stimulus.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   1 LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Action Btn** | GP14 | Interaction sensor |
| **Stimulus LED** | GP15 | Visual trigger |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking round & speed)
*   **from Math, drag `math_arithmetic`** (decrementing delay)
*   **from Logic, drag `controls_if`** (checking success)

### 7. Variables
*   **delay_time**: starting at 1000ms, decreasing by 100ms per win.
*   **rounds**: count of successful taps.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Speed**: **Set** `delay_time` = 1.0 (seconds).
2.  **Start Counter**: **Set** `rounds` = 0.

**B. Gameplay Phase (Loop)**
3.  **Run Round**:
    *   **Wait** `delay_time` seconds.
    *   **Turn ON** LED (GP15).
4.  **Reaction window**:
    *   Wait for **Button** GP14.
    *   If pressed within `delay_time`:
        *   **Print** "Round Passed!".
        *   **Set** `rounds` = `rounds` + 1.
        *   **Set** `delay_time` = `delay_time` - 0.1.
    *   Else:
        *   **Print** "GAME OVER. Rounds completed: ", `rounds`.
        *   **Reset** Variables.

### 9. Execution Flow
1.  **Round 1**: You wait 1 second. The light turns on. You click. Success!
2.  **Round 2**: You wait only 0.9 seconds. Click. Success!
3.  **Round 5**: The light is turning on every half-second now. Your heart rate is increasing.
4.  **Round 10**: The light turns on every 0.1s. You miss.
5.  **Result**: The Pico tells you that your "Endurance Level" is 9. A perfect way to measure focus over time.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

speed = 1.0
score = 0

while True:
    print("Level: " + str(score) + " | Speed: " + str(speed) + "s")
    time.sleep(speed)
    
    led.value(1)
    
    # Reaction window is equal to current speed
    start = time.ticks_ms()
    hit = False
    while time.ticks_diff(time.ticks_ms(), start) < (speed * 1000):
        if btn.value():
            hit = True
            break
            
    led.value(0)
    
    if hit:
        score += 1
        speed -= 0.1 # Get faster
        if speed < 0.1: speed = 0.1 # Limit speed
        print("WIN!")
        time.sleep(1)
    else:
        print("TOTAL ROUNDS: " + str(score))
        score = 0
        speed = 1.0
        time.sleep(3)
```

### 11. Common Mistakes
*   **Negative Delays**: If you subtract 0.1 forever, your delay will eventually become a negative number, which will crash your code. Always use an `if speed < 0.1: speed = 0.1` block to prevent this.

### 12. Try This Next
*   **Round Multiplier**: every 5 rounds, play a victory sound and flash the lights.
*   **Dual-Life**: give the player 3 "Hearts". They only lose when all hearts are gone.

---
