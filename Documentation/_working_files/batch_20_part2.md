
## Project 0196: Smart Metronome Switch

### 1. Learning Objective
Explore output routing and conditional hardware control. Learn how to use a physical switch to toggle between "Perform" (Audio + Visual) and "Silent" (Visual only) modes, similar to a smartphone's silent switch.

### 2. Concepts Introduced
*   **Output Routing**: Directing a signal to different hardware components based on a state.
*   **Silent Mode**: Providing feedback through non-intrusive channels (Light) when Sound is inappropriate.
*   **Logical AND/OR**: Combining conditions to determine if a specific hardware action should occur.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Slide Switch or Toggle Switch
*   LED + Resistor
*   Buzzer
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Silent Switch** | GP13 | Toggle position |
| **Buzzer** | GP15 | Audio Pulse |
| **LED** | GP14 | Visual Pulse |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking the switch)
*   **from Smart IO, drag `pico_gpio_read`** (read Pin)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin control)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **sound_enabled**: Boolean state of the physical switch.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output Pins**:
    *   Set GP14 (LED) and GP15 (Buzzer) to LOW.

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Read the Switch**:
    *   From **Variables**, **Set** `sound_enabled` = **Smart IO** `pico_gpio_read` GP13.

**C. Conditional Pulse Phase**
4.  **Execute Beat**:
    *   **Always Pulse LED**: From **Smart IO**, **Set** GP14 -> HIGH.
    *   **Conditionally Pulse Buzzer**:
        *   From **Logic**, drag `controls_if`.
        *   **Condition**: If `sound_enabled` == True.
        *   **Action**: **Set** GP15 (Buzzer) -> HIGH.
5.  **Hold the Pulse**:
    *   From **Time**, **Wait** 0.05 seconds.
6.  **End the Pulse**:
    *   **Set** both GP14 and GP15 to LOW.

**D. Timing Phase**
7.  **Hold the Rhythm**:
    *   From **Time**, **Wait** 0.95 seconds (for 60 BPM).

### 8. Execution Flow
1.  **Check**: The Pico looks at the position of the slide switch.
2.  **Flash**: regardless of the switch, the LED flashes for Every beat.
3.  **Route**: If the switch is "ON", the Pico also sends power to the Buzzer.
4.  **Silence**: If the switch is "OFF", the Buzzer logic is skipped, and the metronome becomes silent but visual.
5.  **Result**: An adaptable metronome for practice in both choir rooms and quiet libraries.

### 9. Generated Code
```python
from machine import Pin
import time

sw = Pin(13, Pin.IN, Pin.PULL_DOWN)
bz = Pin(15, Pin.OUT)
led = Pin(14, Pin.OUT)

while True:
    silent_off = sw.value() # 1 = Sound ON, 0 = Sound OFF
    
    # Visual Beat (Always)
    led.value(1)
    
    # Audio Beat (Conditional)
    if silent_off:
        bz.value(1)
        
    time.sleep(0.05)
    
    # Stop Pulse
    led.value(0)
    bz.value(0)
    
    time.sleep(0.95)
```

### 10. Common Mistakes
*   **Switch Bounce**: If you read the switch inside the 0.05s pulse, it may flicker. Read it at the VERY start of each beat for a stable state.
*   **Wiring Inversion**: If the buzzer sounds when the switch is clicked "OFF", change your logic to `if not sound_enabled` or swap your VCC/GND wires on the switch.

### 11. Try This Next
*   **Dual Mode LED**: Use a Green LED for "Normal" mode and a Blue LED for "Silent" mode.
*   **Baton Animation**: If you have an LED strip, make the light "swing" like a conductor's baton in silent mode.

---

## Project 0197: Metronome Alarm System

### 1. Learning Objective
Explore system performance monitoring (Drift Detection). Learn how to measure the actual execution time of a loop and trigger an alarm (Red LED) if the timing becomes inaccurate due to processor lag or complex code.

### 2. Concepts Introduced
*   **Timing Drift**: The accumulation of small errors that cause a clock to lose or gain time.
*   **Performance Jitter**: Variations in how long it takes for a microcontroller to execute a task.
*   **Self-Diagnostic Logic**: A program that monitors its own health and warns the user of failure.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Red LED + Resistor
*   Buzzer
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Error LED** | GP14 | Lights up on timing drift |
| **Buzzer** | GP15 | Main rhythm beat |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_time_ms`** (get millisecond clock)
*   **from Logic, drag `controls_if`** (checking lag)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)

### 6. Variables
*   **start_tick**, **end_tick**: Time markers for calculating loop duration.
*   **actual_ms**: The measured time between beats.
*   **is_drifting**: Error flag.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Marker**:
    *   **Set** `start_tick` = **Time** `pico_time_ms`.

**B. Monitoring Phase (Loop)**
2.  **Start Beat Loop**: From **Loops**, drag `pico_forever`.
3.  **Perform Beat**:
    *   **Click** Buzzer (GP15). **Wait** 0.05s.
4.  **Target Timing**:
    *   **Wait** 1 second (Target: 60 BPM).

**C. Diagnostics Phase**
5.  **Calculate Lag**:
    *   **Set** `end_tick` = **Time** `pico_time_ms`.
    *   **Set** `actual_ms` = `end_tick` - `start_tick`.
    *   **Update Marker**: **Set** `start_tick` = `end_tick`.
6.  **Flag the Error**:
    *   From **Logic**, drag `controls_if` with **else**.
    *   **Condition**: If `actual_ms` > 1100. (The beat took 1.1s instead of 1.0s).
    *   **Action**: **Set** GP14 (Red LED) -> HIGH. **Print** "LAG DETECTED!".
    *   **Else**: **Set** GP14 (Red LED) -> LOW.

### 8. Execution Flow
1.  **Start**: The Pico notes the exact time (e.g. 1000ms).
2.  **Act**: The buzzer beeps. The Pico waits 1 second.
3.  **Check**: The Pico notes the time again (e.g. 2100ms).
4.  **Compare**: 2100 - 1000 = 1100ms. Since it matched the target, the LED stays OFF.
5.  **Detect**: If the Pico was busy doing something else and the end time was 2500ms, the Red LED would turn ON to tell the musician the beat is no longer trustworthy.

### 9. Generated Code
```python
from machine import Pin
import time

led_err = Pin(14, Pin.OUT)
bz = Pin(15, Pin.OUT)

last_tick = time.ticks_ms()

while True:
    # Perform Beat
    bz.value(1)
    time.sleep(0.05)
    bz.value(0)
    
    # Intentional heavy work or long sleep
    time.sleep(0.95)
    
    # Diagnostic
    now = time.ticks_ms()
    diff = time.ticks_diff(now, last_tick)
    last_tick = now
    
    # Check for 10% drift (Target 1000ms)
    if diff > 1100:
        print("ALERT: Timing Drift! Actual ms: " + str(diff))
        led_err.value(1)
    else:
        led_err.value(0)
```

### 10. Common Mistakes
*   **Strict Comparison**: Don't check for `diff > 1000`. Microcontrollers always have a few milliseconds of natural variation. Use a buffer (e.g. 1100).
*   **Marker Reset**: If you don't update `start_tick` at the end of the check, the drift will appear to grow every single loop.

### 11. Try This Next
*   **Auto-Correction**: If drift is detected, automatically shorten the NEXT wait block slightly to "catch up" to the real-time clock.
*   **Buzzer Siren**: Sound a different tone if the timing is too far off.

---

## Project 0198: The Metronome Game

### 1. Learning Objective
Explore internal rhythm validation. Learn how to implement a "Memory Challenge" where a machine sets a tempo, goes silent, and then evaluates the user's ability to maintain that exact tempo using a button.

### 2. Concepts Introduced
*   **Pattern Extrapolation**: Continuing a sequence based on a previously established rule.
*   **Error Offset (Rhythm)**: Calculating how many milliseconds a user's tap was away from the "Theoretical Perfect Beat".
*   **Blind Performance**: testing skills without visual or audio accompaniment.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   Button
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Game Button** | GP14 | Tap to keep the beat |
| **Buzzer** | GP15 | Guidance and Fail sounds |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Time, drag `pico_time_ms`** (timestamping)
*   **from Math, drag `math_arithmetic`** (subtraction)
*   **from Logic, drag `controls_if`** (evaluating result)

### 6. Variables
*   **ideal_beat**: The time when the beat *should* have happened.
*   **user_beat**: The time when the user *actually* tapped.
*   **score**: Accuracy percentage.

### 7. Step-by-Step Guide

**A. Training Phase**
1.  **Play Guidance**: 
    *   From **Loops**, Repeat 4 times:
        *   **Beep** GP15. **Wait** 1.0 second.
2.  **Silent Prep**:
    *   **Print** "YOUR TURN! 1... 2... 3... CLICK!".
    *   **Set** `ideal_beat` = **Time** `pico_time_ms` + 1000.

**B. Performance Phase**
3.  **Capture Guess**:
    *   Wait for **Button** GP14 to be Pressed.
    *   **Set** `user_beat` = **Time** `pico_time_ms`.

**C. Scoring Phase**
4.  **Calculate Error**:
    *   **Set** `offset` = Abstract(`user_beat` - `ideal_beat`).
5.  **Verdict**:
    *   If `offset` < 100: **Print** "PERFECT! (", `offset`, "ms error)".
    *   Else If `offset` < 300: **Print** "GOOD! (", `offset`, "ms error)".
    *   Else: **Print** "OUT OF TIME! (", `offset`, "ms error)".
6.  **Cooldown**: **Wait** 3 seconds before next round.

### 8. Execution Flow
1.  **Listen**: The Pico plays a steady 60 BPM beat 4 times for you to "internalize".
2.  **Silence**: The Pico goes quiet. You must count "FIVE" in your head.
3.  **Action**: You hit the button exactly where the 5th beat should be.
4.  **Math**: The Pico compares your tap to its internal master clock.
5.  **Result**: If you hit within 0.1s of the true beat, you win!

### 9. Generated Code
```python
from machine import Pin
import time

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)
bz = Pin(15, Pin.OUT)

def game_round():
    print("Listen to the rhythm...")
    for _ in range(4):
        bz.value(1); time.sleep(0.05); bz.value(0)
        time.sleep(0.95)
        
    print("NOW YOU! Tap on the NEXT beat!")
    perfect_time = time.ticks_ms() + 1000
    
    # Wait for player tap
    while btn.value() == 0:
        # Fail if they wait too long (>2s)
        if time.ticks_ms() > perfect_time + 1000:
            print("TOO LATE!")
            return
            
    user_time = time.ticks_ms()
    error = abs(time.ticks_diff(user_time, perfect_time))
    
    if error < 100:
        print("EXCELLENT! Error: " + str(error) + "ms")
    elif error < 250:
        print("NOT BAD. Error: " + str(error) + "ms")
    else:
        print("OFF BEAT. Error: " + str(error) + "ms")

while True:
    game_round()
    time.sleep(3)
```

### 10. Common Mistakes
*   **Double Trigger**: hitting the button once might count as two "rounds". Always put a 1-second delay after the result is shown.
*   **Calculation Direction**: ensure you use `abs()` (Absolute Value) so that being 100ms early and 100ms late are both scored the same.

### 11. Try This Next
*   **Increasing Difficulty**: make the training phase shorter (only 2 beats) or the tempo faster.
*   **High Score Table**: save the lowest (best) error and try to beat it.

---

## Project 0199: Automated Metronome

### 1. Learning Objective
Orchestrate programmatic tempo curves (Accelerando). Learn how to create a loop that automatically modifies its own duration variable over time, simulating a training exercise for musicians who need to build speed.

### 2. Concepts Introduced
*   **Accelerando**: A musical term meaning "to gradually get faster".
*   **Variable Decay/Promotion**: Gradually changing a value after a set number of cycles.
*   **Dynamic Intervals**: using logic to drive tempo instead of user input.

### 3. Hardware Required
*   Raspberry Pi Pico
*   Buzzer
*   1 LED (for visual speed indication)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Tempo Buzzer** | GP15 | Speed indicator |
| **Visual LED** | GP14 | Flashes faster over time |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (nested loops for bars)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (addition)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **current_bpm**: Starts at 60.
*   **beat_in_measure**: counter from 1 to 4.
*   **measure_count**: counter for when to speed up.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting Speed**:
    *   **Set** `current_bpm` = 60.

**B. Measurement Phase**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Perform a "Bar" (4 Beats)**:
    *   From **Loops**, drag `controls_repeat` (4 times).
    *   Inside:
        *   **Click** Buzzer. **Wait** 0.05s.
        *   **Delay**: **Wait** (60 / `current_bpm`) - 0.05.

**C. Automation Phase**
4.  **Increase Speed**:
    *   After the 4-beat loop finishes:
    *   **Set** `current_bpm` = `current_bpm` + 5.
    *   **Print** "Speeding up! New Tempo: ", `current_bpm`.
5.  **Upper Limit**:
    *   From **Logic**, if `current_bpm` > 200: **Set** `current_bpm` = 60 (Reset for next drill).

### 8. Execution Flow
1.  **Slow**: The metronome plays at 60 BPM for 4 beats.
2.  **Step**: The Pico adds 5 to the tempo. Now it is 65 BPM.
3.  **Smooth**: The next 4 beats are slightly faster.
4.  **Escalation**: Every few seconds, the rhythm gets more intense automatically.
5.  **Result**: An automated coach that pushes the musician to play faster and faster.

### 9. Generated Code
```python
from machine import Pin
import time

bz = Pin(15, Pin.OUT)
current_bpm = 60

while True:
    print("Tempo: " + str(current_bpm))
    
    # Play one Measure (4 beats)
    for _ in range(4):
        bz.value(1)
        time.sleep(0.05)
        bz.value(0)
        
        # Calculate current wait
        wait_time = (60 / current_bpm) - 0.05
        time.sleep(wait_time)
        
    # Accelerando: Increase speed by 5 BPM every measure
    current_bpm += 5
    
    # Reset if it gets too fast
    if current_bpm > 200:
        print("Max speed reached! Restarting Drill...")
        current_bpm = 60
        time.sleep(2)
```

### 10. Common Mistakes
*   **Continuous Increase**: If you add +5 BPM inside the 1-beat loop, it will speed up *every beat*, which sounds unnatural and jerky. Add it after a full measure of 4 beats.
*   **Floating Math**: ensure your wait time calculation doesn't produce negative numbers if the BPM gets too high.

### 11. Try This Next
*   **Ritardando**: create a "Slow Down" mode where the tempo decreases every measure.
*   **Interval Training**: Speed up for 4 bars, then slow down for 4 bars in a cycle.

---

## Project 0200: Mastering Metronome

### 1. Learning Objective
Explore mathematical least-common-multiple timing (Polyrhythms). Learn how to manage two independent rhythmic pulses (e.g., "3 against 2") simultaneously using a single master clock and division logic.

### 2. Concepts Introduced
*   **Polyrhythm**: The simultaneous use of two or more conflicting rhythms (e.g., 2 beats in one hand, 3 in the other).
*   **Master Clock Slicing**: using a very small time step (e.g. 0.01s) to track when multiple different beats should trigger.
*   **Concurrent Logic**: handling overlapping events without one blocking the other.

### 3. Hardware Required
*   Raspberry Pi Pico
*   2 LEDs (Red and Blue)
*   Buzzer (Optional: use different pitches for each rhythm)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED A (Rhythm 1)** | GP15 | Flashes 2 times per bar |
| **LED B (Rhythm 2)** | GP14 | Flashes 3 times per bar |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set variable)
*   **from Math, drag `math_arithmetic`** (modulo, division)
*   **from Logic, drag `controls_if`** (checking both rhythms)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **master_timer**: Counts from 0 up to 600 (The "Super-Measure").

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define the Grid**:
    *   We want a bar that is 600 "units" long.
    *   Rhythm A (2 beats) should trigger every 300 units (600 / 2).
    *   Rhythm B (3 beats) should trigger every 200 units (600 / 3).
2.  **Initialize**: **Set** `master_timer` = 0.

**B. Rhythmic Slicing Phase (Loop)**
3.  **Start Loop**: From **Loops**, drag `pico_forever`.
4.  **Handle Rhythm A (Every 300)**:
    *   If `master_timer` % 300 == 0:
        *   **Set** GP15 (LED A) -> HIGH. **Print** "Beat A".
5.  **Handle Rhythm B (Every 200)**:
    *   If `master_timer` % 200 == 0:
        *   **Set** GP14 (LED B) -> HIGH. **Print** "Beat B".

**C. Cleanup and Pace Phase**
6.  **Hold Flash**: **Wait** 0.05s.
7.  **Reset LEDs**: **Set** both GP15 and GP14 to LOW.
8.  **Advance Time**:
    *   **Set** `master_timer` = (`master_timer` + 10) % 600. (We increment by 10 per tick).
    *   **Wait** 0.01 seconds.

### 8. Execution Flow
1.  **Start**: Both LEDs flash together (Beat 0 % both = 0).
2.  **Tick**: At 200ms, only the 3-beat LED flashes.
3.  **Tick**: At 300ms, only the 2-beat LED flashes.
4.  **Tick**: At 400ms, the 3-beat LED flashes again.
5.  **Result**: The user sees the complex overlapping "cross-rhythm" of 3 against 2, perfectly synchronized by math.

### 9. Generated Code
```python
from machine import Pin
import time

led_a = Pin(15, Pin.OUT)
led_b = Pin(14, Pin.OUT)

# 2 vs 3 Polyrhythm
# Total bar = 600ms
# Rhythm A = every 300ms
# Rhythm B = every 200ms
timer = 0

while True:
    a_hit = (timer % 300 == 0)
    b_hit = (timer % 200 == 0)
    
    if a_hit: led_a.value(1)
    if b_hit: led_b.value(1)
    
    if a_hit or b_hit:
        # If there was any beat, hold the light
        time.sleep(0.05)
        led_a.value(0)
        led_b.value(0)
        timer += 50
    else:
        # Just advance the clock
        time.sleep(0.01)
        timer += 10
        
    # Reset measure
    if timer >= 600:
        timer = 0
        print("--- Next Measure ---")
```

### 10. Common Mistakes
*   **Blocking Beats**: If the flash pause is too long, it will interfere with the next beat's timing. Use very small slices (10ms) for high accuracy.
*   **Phase Shift**: If you don't use the Modulo (%) operator, the two rhythms will eventually drift apart.

### 11. Try This Next
*   **4 vs 3**: Change the math to 120 (LCM of 3 and 4) and try to visualize the 4-over-3 pattern.
*   **Beat Pitch**: Use a buzzer to play a high note for Rhythm A and a low note for Rhythm B.

---
