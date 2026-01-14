
## 1. Project 0246: Smart Traffic Lights Switch

### 2. Learning Objective
Explore multi-profile scheduling (Rush Hour Mode). Learn how to use a physical switch to toggle between two completely different timing profiles (Quiet vs. Busy), adapting the system's behavior to meet changing real-world demands.

### 3. Concepts Introduced
*   **Profile Switching**: changing multiple variables (Green duration, Red duration) with a single input.
*   **Parameter Optimization**: Adjusting timings to prioritize a "Main Road" over a "Side Road".
*   **Static vs. Dynamic Timers**: demonstrating how fixed delays can be made flexible.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Slide Switch
*   Traffic Lights (2 Groups: Main Road and Side Road)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Schedule Switch** | GP14 | HIGH = Rush Hour |
| **Main Green** | GP15 | Higher priority |
| **Side Green** | GP13 | Lower priority |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking the switch)
*   **from Variables, drag `variables_set`** (setting durations)
*   **from Time, drag `pico_wait`** (interval control)

### 7. Variables
*   **main_duration**: length of green on primary road.
*   **side_duration**: length of green on secondary road.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Evaluate Schedule**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **Switch** GP14 is HIGH (1).

**B. Profile Selection**
3.  **Busy Mode (Rush Hour)**:
    *   Inside the **If** block:
    *   **Set** `main_duration` = 10.
    *   **Set** `side_duration` = 2.
    *   **Print** "Mode: RUSH HOUR (Priority Main Road)".
4.  **Quiet Mode (Normal)**:
    *   Inside the **Else** block:
    *   **Set** `main_duration` = 5.
    *   **Set** `side_duration` = 5.
    *   **Print** "Mode: NORMAL (Equal Priority)".

**C. Execution Phase**
5.  **Run Cycle**:
    *   **Set** Main Green HIGH. **Wait** `main_duration` seconds.
    *   **Set** Main Green LOW.
    *   **Set** Side Green HIGH. **Wait** `side_duration` seconds.
    *   **Set** Side Green LOW.

### 9. Execution Flow
1.  **Read**: The Pico checks the switch position at the start of every circle.
2.  **Schedule**: If you slide the switch "ON", the Main Road gets effectively 5 times more "Green Time" than the Side Road.
3.  **Efficiency**: This keeps the heavy traffic moving while only occasionally letting a side car through.
4.  **Switch**: You slide it "OFF". The Pico instantly resets both roads to an equal 5-second balance.
5.  **Result**: An adaptive traffic controller that a person can adjust based on the time of day.

### 10. Generated Code
```python
from machine import Pin
import time

sw = Pin(14, Pin.IN, Pin.PULL_DOWN)
main_g = Pin(15, Pin.OUT)
side_g = Pin(13, Pin.OUT)

while True:
    # 1. Choose profile
    if sw.value() == 1:
        main_t = 10
        side_t = 2
    else:
        main_t = 5
        side_t = 5
        
    # 2. Main Road Phase
    main_g.value(1); side_g.value(0)
    time.sleep(main_t)
    
    # 3. Side Road Phase
    main_g.value(0); side_g.value(1)
    time.sleep(side_t)
```

### 11. Common Mistakes
*   **Infinite Wait**: If you put the switch check *inside* a long `wait` block, you'll have to wait until the current car finishes before the mode changes. Putting it at the *start* of the loop is the correct way to handle simple profile switching.

### 12. Try This Next
*   **Third Mode**: add another switch to create a same-duration "Night Mode" where both lights are shorter (e.g. 2s) to save power.
*   **Blinking Transition**: when switching modes, make all lights flash for 1 second.

---

## 1. Project 0247: Traffic Lights Alarm System

### 2. Learning Objective
Explore self-diagnostic feedback loops (Bulb Failure Detection). Learn how to use a "Feedback Wire" to monitor the success of a command, detecting if a hardware output (LED) is actually drawing power when it is supposed to be active.

### 3. Concepts Introduced
*   **Diagnostic Loops**: using an input pin to monitor an output pin.
*   **Simulated Faults**: unplugging a wire to trigger a software response.
*   **Redundancy**: Having an "Alarm" state that separate from the primary logic.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + Resistor
*   1 Jumper Wire (The Feedback Link)
*   1 Buzzer (Alarm)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Signal Out** | GP15 | Controls the LED |
| **Signal In** | GP14 | Connects TO the LED leg (Monitor) |
| **Alarm Buzzer** | GP13 | Fail indicator |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating validity)
*   **from Smart IO, drag `pico_gpio_read`** (checking the bulb)
*   **from Smart IO, drag `pico_gpio_write`** (signaling error)

### 7. Variables
*   **bulb_is_okay**: Boolean tracking hardware health.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Status**: **Turn ON** GP15 (LED) and **Turn OFF** GP13 (Alarm).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Verify Hardware**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**: If **GPIO Read** GP14 is LOW (0).
    *   *Note: Since the LED is currently commanded ON (GP15=HIGH), GP14 SHOULD see power. If it is LOW, the bulb is dead or the wire is cut.*

**C. Response Phase**
4.  **Failure Detection**:
    *   Inside the **If** block: 
    *   **Set** GP13 -> HIGH (Sound Buzzer).
    *   **Print** "CRITICAL FAILURE: BULB OUT ON GP15".
5.  **Healthy Detection**:
    *   Inside the **Else** block:
    *   **Set** GP13 -> LOW.

### 9. Execution Flow
1.  **Idle**: The light is ON. The feedback wire sends electricity back to GP14. The Pico sees a "1" and is happy.
2.  **Pull the Plug**: You physically pull the LED out of the breadboard.
3.  **Detect**: Immediately, the Pico sees that although it is TRYING to send power to GP15, there is no signal coming back to GP14.
4.  **Reaction**: The buzzer starts screaming to let the repair crew know the light is broken.
5.  **Result**: A smart infrastructure system that monitors its own health.

### 10. Generated Code
```python
from machine import Pin
import time

# Output and Monitoring Pins
led_pin = Pin(15, Pin.OUT)
monitor_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)
alarm_buzzer = Pin(13, Pin.OUT)

# Turn light on initially
led_pin.value(1)

while True:
    # Check if the light is actually electrically active
    # (CMD is ON, so Monitor should be ON)
    if led_pin.value() == 1 and monitor_pin.value() == 0:
        # CMD is on but PIN is dead = Failure
        print("BULB FAILURE DETECTED!")
        alarm_buzzer.value(1)
    else:
        # All good or intentionally off
        alarm_buzzer.value(0)
        
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Wait Timing**: if you check the monitor pin *exactly* at the same millisecond you turn the LED on, you might get a "False Alarm" because electricity takes a tiny fraction of a second to travel. Always wait 0.1s after a command before checking health.

### 12. Try This Next
*   **Auto-Shutoff**: if the bulb fails, turn off the whole intersection for safety.
*   **External Service**: Print "Sending text to maintenance..." to the console.

---

## 1. Project 0248: The Traffic Lights Game

### 2. Learning Objective
Explore predictive timing (The Green Wave). Learn how to implement a game that tests the user's ability to synchronize a physical action with a changing light state, rewarding precision within a narrow temporal window.

### 3. Concepts Introduced
*   **Reaction Windows**: checking if a button press occurred during a specific "Success" state.
*   **Game Leveling**: Speeding up the light toggle as the user gets better.
*   **Score Accumulation**: tracking consecutive "Green Waves" caught.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button
*   2 LEDs (Red and Green)
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accelerator (Btn)** | GP14 | Press to "Drive" |
| **Signal (Green)** | GP15 | Go Trigger |
| **Signal (Red)** | GP13 | Stop Trigger |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (tracking score)
*   **from Logic, drag `controls_if`** (evaluating logic)
*   **from Smart IO, drag `pico_gpio_write`** (set Signal)

### 7. Variables
*   **current_color**: "RED" or "GREEN".
*   **score**: count of successful starts.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Prep Variables**: **Set** `score` = 0.

**B. Control Phase (Loop)**
2.  **Cycle the Light**:
    *   From **Loops**, `pico_forever`.
    *   **Set** Red HIGH. **Set** Green LOW. **Wait** a random (2-5s) duration.
    *   **Set** Red LOW. **Set** Green HIGH.

**C. Detection Phase (The Window)**
3.  **Catch the Wave**:
    *   **Wait** exactly 0.5s after the Green turns ON.
    *   If **Button** GP14 was Pressed during this 0.5s:
        *   **Print** "PERFECT START!".
        *   **Set** `score` = `score` + 1.
    *   Else if Button was Pressed while Red was ON:
        *   **Print** "FALSE START! Game Over.".
        *   **Set** `score` = 0.

### 9. Execution Flow
1.  **Interaction**: You sit with your finger on the button. The light is Red.
2.  **Anticipation**: The light turns Green.
3.  **Action**: You mash the button within half a second.
4.  **Reward**: The Pico plays a victory beep and adds to your score. 
5.  **Failure**: You get impatient and press during Red. The Pico resets you to zero.
6.  **Result**: An addictive reaction game that simulates a racing start or a green-wave navigator.

### 10. Generated Code
```python
import machine
import utime
import urandom

r_led = machine.Pin(13, machine.Pin.OUT)
g_led = machine.Pin(15, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

score = 0

while True:
    # 1. Red Phase
    r_led.value(1); g_led.value(0)
    print("Wait for Green...")
    
    # Check for early press (Cheating)
    wait_time = urandom.randint(2, 5)
    start_wait = utime.ticks_ms()
    penalty = False
    
    while utime.ticks_diff(utime.ticks_ms(), start_wait) < (wait_time * 1000):
        if btn.value():
            print("FALSE START!")
            score = 0
            penalty = True
            break
        utime.sleep(0.01)
        
    if penalty:
        r_led.value(1); g_led.value(1); utime.sleep(1) # Flash both for error
        continue

    # 2. Green Phase (The Window)
    r_led.value(0); g_led.value(1)
    window_start = utime.ticks_ms()
    hit = False
    
    while utime.ticks_diff(utime.ticks_ms(), window_start) < 500: # 500ms window
        if btn.value():
            hit = True
            break
        utime.sleep(0.01)
            
    if hit:
        score += 1
        print("CATCH THE WAVE! Total Score: " + str(score))
        utime.sleep(1)
    else:
        print("TOO SLOW")
        score = 0
```

### 11. Common Mistakes
*   **Deterministic Timing**: if the light always turns Green after exactly 3 seconds, the user will just memorize the rhythm. Always use the `random` math block for the wait time.

### 12. Try This Next
*   **Leaderboard**: display the highest score on an LCD screen.
*   **Flashier Win**: blink the Green LED 10 times if they catch 5 in a row.

---

## 1. Project 0249: Automated Traffic Lights

### 2. Learning Objective
Explore deadlock resolution (Gridlock Prevention). Learn how to use multiple ultrasonic sensors to detect when both roads in an intersection are physically blocked (Full Capacity) and implement an "Empty-the-Intersection" safety sequence.

### 3. Concepts Introduced
*   **Gridlock Detection**: Using sensors to see if cars are not moving on either road.
*   **Logic Conflict Resolution**: prioritizing a "Clear" signal over a "Proceed" signal to fix congestion.
*   **Autonomous Efficiency**: the intersection fixes itself without human help.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Ultrasonic Sensors (North and East approaches)
*   Traffic Lights (Main and Side)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Main Sensor** | GP14 | Reads North cars |
| **Side Sensor** | GP13 | Reads East cars |
| **Main Light** | GP15 | Traffic Control |
| **Side Light** | GP12 | Traffic Control |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_ultrasonic_dist`** (read occupancy)
*   **from Logic, drag `logic_operation`** (AND)
*   **from Logic, drag `controls_if`** (gridlock check)
*   **from Smart IO, drag `pico_gpio_write`** (clearing roads)

### 7. Variables
*   **main_blocked**, **side_blocked**: Boolean status of roads.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Measure Congestion**:
    *   **Set** `main_dist` = **Sensors** `pico_ultrasonic_dist` GP14.
    *   **Set** `side_dist` = **Sensors** `pico_ultrasonic_dist` GP13.

**B. Brain Phase (The Check)**
3.  **Detect Deadlock**:
    *   If **Both** `main_dist` < 10cm **AND** `side_dist` < 10cm:
        *   **Print** "GRIDLOCK DETECTED! INITIATING RESET.".
        *   **Set** BOTH lights to RED.
        *   **Wait** 10 seconds (giving cars time to back up or reorganize).
    *   Else:
        *   Run standard traffic light rotation.

### 9. Execution Flow
1.  **Normal**: Cars are moving through smoothly. The sensors see "Clear" (High distance).
2.  **Jam**: Too many cars arrive at once and block the box. Both sensors see "Blocked" (Distance < 10cm).
3.  **Reaction**: The Pico sees both are blocked. It doesn't matter who was Green first; it turns EVERYTHING Red.
4.  **Clearing**: For 10 seconds, it holds the stop. This forces the drivers to stop moving into the "box".
5.  **Result**: The intersection clears itself and resumes normal operation once the sensors report "Clear".

### 10. Generated Code
```python
import machine
import utime

# Sensors and Lights
main_r = machine.Pin(15, machine.Pin.OUT)
side_r = machine.Pin(12, machine.Pin.OUT)

# Simplified dist function (reuse from previous projects)
def check_grid(p):
    # Mock check: return True if distance is low
    return False

while True:
    m_jam = check_grid(14)
    s_jam = check_grid(13)
    
    if m_jam and s_jam:
        print("GRIDLOCK! HOLDING ALL RED")
        main_r.value(1); side_r.value(1)
        utime.sleep(10)
    else:
        # Normal rotation
        main_r.value(0); side_r.value(1); utime.sleep(5)
        main_r.value(1); side_r.value(0); utime.sleep(5)
```

### 11. Common Mistakes
*   **Sensitivity**: if 10cm is too small, a single car might not trigger it. If it's too large, it might think it's gridlocked when cars are just waiting normally. Adjust the distance based on your toy car sizes!

### 12. Try This Next
*   **Blink Warning**: flash the Yellow lights for 3 seconds before the "Gridlock Red" starts to warn everyone.

---

## 1. Project 0250: Mastering Traffic Lights

### 2. Learning Objective
Explore peer-to-peer event handling (The 4-Way Stop). Learn how to implement logic for an unmanaged intersection where the system provides "Green Permission" based on arrival order (First in, First out), simulating a smart 4-way stop sign.

### 3. Concepts Introduced
*   **Event Priority**: granting access only when requested.
*   **First-In-First-Out (FIFO)**: simpler version: checking which button arrived first in a split second.
*   **Warning-State Consistency**: Maintaining a "Caution" state (Flashing Red) as the default mode.

### 4. Hardware Required
*   Raspberry Pi Pico
*   4 Buttons (Approaches A, B, C, D)
*   4 LEDs (Center Signal)

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A** | GP14 | Request North |
| **Button B** | GP13 | Request East |
| **Main Signal** | GP15 | The Go/No-Go light |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating requests)
*   **from Smart IO, drag `pico_gpio_write`** (signaling Go)
*   **from Time, drag `pico_wait`** (clearance duration)

### 7. Variables
*   **None**: this is a priority-polling project.

### 8. Step-by-Step Guide

**A. Idle Phase (Monitor)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Caution State**: 
    *   **Blink** the Red LED (GP15) every 0.5s.
    *   *Note: This is the default mode of a "Disabled" intersection.*

**B. Request Phase**
3.  **Check for Arrivals**:
    *   If **Button A** (North) is Pressed:
        *   **Stop** Blinking. **Set** LED to SOLID GREEN for 3 seconds.
        *   **Print** "North Proceeding...".
        *   **Return** to Blinking Red.
4.  **Check for others**:
    *   If **Button B** is Pressed: same sequence for East.

### 9. Execution Flow
1.  **Idle**: The light is constantly blinking Red. Every car must "Stop and Look".
2.  **Request**: You (as Driver A) press your button.
3.  **Grant**: The Pico sees your request. It pauses the blinking and gives you a Solid Green to tell you it's safe to go.
4.  **Finish**: After 3 seconds, it goes back to "Caution" mode.
5.  **Result**: An interactive stop sign that provides explicit safety confirmations.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    # Caution Mode
    led.value(1); time.sleep(0.3)
    led.value(0); time.sleep(0.3)
    
    # Priority Check (Simplified)
    if btn_a.value():
        print("North Given Green")
        led.value(1) # Solid Green logic (if using RGB)
        time.sleep(3)
        
    if btn_b.value():
        print("East Given Green")
        led.value(1)
        time.sleep(3)
```

### 11. Common Mistakes
*   **Ignoring Priority**: If two people press at once, the code will just do A then B. In a real system, you'd need a "Queue" to remember everyone's turn.

### 12. Try This Next
*   **The Queue**: Try to make a list of buttons pressed and play them back in order so nobody gets skiped!

---
