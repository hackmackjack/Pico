
## 1. Project 0256: Smart Night Light Switch

### 2. Learning Objective
Explore multi-point activation (The Hallway Switch). Learn how to implement Boolean "OR" logic, where any one of multiple triggers (Sensors or Buttons) can activate a single system, ensuring a light turns on regardless of which side a user enters from.

### 3. Concepts Introduced
*   **OR Logic**: Output is HIGH if Input A is HIGH, OR Input B is HIGH, or both.
*   **Distributed Control**: managing a single hardware output from multiple physical locations.
*   **Pass-through States**: ensuring the light stays on as long as the user is "detected" anywhere along the path.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 PIR Motion Sensors (or 2 Buttons to simulate)
*   1 LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **PIR Sensor 1** | GP14 | Entrance A |
| **PIR Sensor 2** | GP13 | Entrance B |
| **Hallway LED** | GP15 | Shared illumination |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (if/then/else)
*   **from Logic, drag `logic_operation`** (OR)
*   **from Smart IO, drag `pico_gpio_read`** (read sensors)
*   **from Smart IO, drag `pico_gpio_write`** (set light)

### 7. Variables
*   **None**: this is a stateless combinational logic project.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Evaluate Combined Input**:
    *   From **Logic**, drag `controls_if` with an **else** slot.
    *   **Condition**:
        *   From **Logic**, drag the `[ ] OR [ ]` block.
        *   Inside slot 1: **Smart IO** `pico_gpio_read` GP14.
        *   Inside slot 2: **Smart IO** `pico_gpio_read` GP13.

**B. Execution Phase**
3.  **Active State (Any detection)**:
    *   Inside the **If** block: **Set** GP15 -> HIGH.
    *   **Print** "Occupant detected - Light ON".
4.  **Idle State (No detection)**:
    *   Inside the **Else** block: **Set** GP15 -> LOW.

### 9. Execution Flow
1.  **Case 1 (Enter from door A)**: PIR 1 triggers. The OR logic says "One is True, therefore the result is True." The light turns ON.
2.  **Case 2 (Enter from door B)**: PIR 2 triggers. The OR logic says "The other is True, therefore True." The light turns ON.
3.  **Case 3 (Walking through middle)**: Both sensors might see you momentarily. True OR True is still True. The light stays ON.
4.  **Case 4 (Exit)**: Both sensors stop seeing motion. Logic says "False OR False is False." The light turns OFF.
5.  **Result**: Reliable hallway lighting that covers two entrances with one smart rule.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
sensor_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
sensor_b = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    # OR Logic: If A is high OR B is high
    if sensor_a.value() == 1 or sensor_b.value() == 1:
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.1) # Debounce/Fast Polling
```

### 11. Common Mistakes
*   **Using AND**: If you use AND logic, the light will only turn on if two people enter from opposite doors at the exact same second, which is useless for a normal hallway.
*   **Pull-up/Down**: Ensure your sensors have a consistent grounded state when not detecting motion.

### 12. Try This Next
*   **Auto-Stay-On**: combine this with a 5-second "Wait" block so the light doesn't flicker off the moment you stop moving.
*   **Main Override**: add a third button on GP12 that keeps the light ON perpetually until clicked again.

---

## 1. Project 0257: Night Light Alarm System

### 2. Learning Objective
Explore gentle waking sequences (The Sunrise Alarm). Learn how to implement a long-duration countdown combined with a "Fade-In" ramp, simulating a natural sunrise to wake a user up without the stress of a loud buzzer.

### 3. Concepts Introduced
*   **Wake-Up Scheduling**: Using `sleep` or timers for long-term delays.
*   **Linear Ramping (Up)**: Gradually increasing a PWM value from 0% to 100%.
*   **Physiological Lighting**: understanding how increasing light intensity signals the brain to wake up.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Bright White LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sunrise LED** | GP15 | Gradual pulse-up output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (climbing up)
*   **from Actuators, drag `pico_pwm_write`** (set brightness)
*   **from Time, drag `pico_wait`** (delay intervals)

### 7. Variables
*   **sunrise_level**: number tracking current brightness.

### 8. Step-by-Step Guide

**A. Sleep Phase**
1.  **Initialize**: **Set** GP15 -> 0% (OFF).
2.  **Long Wait**:
    *   **Print** "Goodnight. Countdown to sunrise (20 seconds)...".
    *   **Wait** 20 seconds. (In a real alarm, this would be 8 hours).

**B. Sunrise Phase**
3.  **Initiate Wakeup**:
    *   **Print** "Sunrise starting...".
    *   From **Loops**, `count with sunrise_level from 0 up to 100 by 1`.
        *   **Set** GP15 Brightness to `sunrise_level`%.
        *   **Wait** 0.2 seconds. (0.2s * 100 steps = 20 second sunrise fade).

**C. Active Phase**
4.  **Hold Morning Light**:
    *   **Maintain** 100% brightness until the Pico is reset.

### 9. Execution Flow
1.  **Start**: You go to bed. The light is dark.
2.  **Count**: The Pico spends 20 seconds doing nothing but watching the clock.
3.  **Transition**: The time reaches the threshold. The Pico starts sending tiny pulses of power to the LED.
4.  **Growth**: The LED moves from a faint ember to full noon-day brightness over the course of 20 seconds.
5.  **Result**: You wake up gradually as the room becomes brighter, feeling more rested than a sudden alarm.

### 10. Generated Code
```python
import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)

# 1. Darkness
led.duty_u16(0)
print("Sleeping for 20s...")
utime.sleep(20)

# 2. Sunrise Fade-In
print("Sunrise Initiated!")
for i in range(0, 101):
    duty = int(i * 655.35)
    led.duty_u16(duty)
    utime.sleep(0.2) # 20 second total fade

print("Good Morning!")
while True:
    utime.sleep(1)
```

### 11. Common Mistakes
*   **Frequency Whine**: If your PWM frequency is set too low (e.g. 50Hz), you might hear the LED "singing" as it fades. Always use 1000Hz or higher for smooth, silent fading.
*   **Immediate ON**: accidentally skipping the loop will make the light jump to 100% instantly, which is just a regular desk lamp.

### 12. Try This Next
*   **Audio Chime**: add a soft melody (Project 0224) that only plays once the light reaches 100%.
*   **Variable Duration**: use a dial (Project 0195) to set the sunrise length.

---

## 1. Project 0258: The Night Light Game

### 2. Learning Objective
Explore visual calibration and timing (The Color Match Challenge). Learn how to implement a game where an RGB LED cycles through different hues and the user must tap a button exactly when the light "Matches" a target color.

### 3. Concepts Introduced
*   **Hue Rotation**: cycling through R, G, and B values in a predictable pattern.
*   **Target Interval Logic**: checking if an input occurs during a specific part of a loop.
*   **Color Perception**: understanding how PWM mixes red and blue to create Purple.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 RGB LED (Common Cathode)
*   1 Button
*   3 Resistors

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pico (R)** | GP15 | Red leg |
| **Pico (G)** | GP14 | Green leg |
| **Pico (B)** | GP13 | Blue leg |
| **Target Btn** | GP12 | Click to "Catch" the color |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Variables, drag `variables_set`** (set color)
*   **from Logic, drag `controls_if`** (evaluating success)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin)

### 7. Variables
*   **current_color**: tracking the game state (Red, Blue, Green, or Purple).

### 8. Step-by-Step Guide

**A. Sequence Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Define Phase 1 (Red)**:
    *   **Set** GP15 HIGH, others LOW. **Set** `current_color` = "red". **Wait** 1s.
3.  **Define Phase 2 (Blue)**:
    *   **Set** GP13 HIGH, others LOW. **Set** `current_color` = "blue". **Wait** 1s.
4.  **Define Phase 3 (Purple)**:
    *   **Set** GP15 HIGH, GP13 HIGH, others LOW. **Set** `current_color` = "purple". **Wait** 1s.
    *   *Note: This is the target!*

**B. Detection Phase**
5.  **Check for Catch**:
    *   Add a separate listener or check inside each phase:
    *   If **Button** GP12 is Pressed:
        *   If `current_color` == "purple":
            *   **Print** "WINNER! PERFECT COLOR MATCH!". Flash LED White 5 times.
        *   Else:
            *   **Print** "MISS! TRY AGAIN.".

### 9. Execution Flow
1.  **Interaction**: The light turns Red... then Blue... then Purple.
2.  **Action**: You wait for the Purple phase and tap the button.
3.  **Verification**: The Pico checks its internal variable. Since it matches "purple", you win!
4.  **Challenge**: If you were too slow and pressed during the next phase, you'd get a "Miss" message.
5.  **Result**: An interactive reflex game that uses basic color mixing as the mechanic.

### 10. Generated Code
```python
import machine
import utime

# RGB Pins
r = machine.Pin(15, machine.Pin.OUT)
g = machine.Pin(14, machine.Pin.OUT)
b = machine.Pin(13, machine.Pin.OUT)
btn = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

colors = ["red", "blue", "purple", "green"]

while True:
    for c in colors:
        # Set hardware state
        if c == "red": r.value(1); g.value(0); b.value(0)
        if c == "blue": r.value(0); g.value(0); b.value(1)
        if c == "purple": r.value(1); g.value(0); b.value(1)
        if c == "green": r.value(0); g.value(1); b.value(0)
        
        # Check for button during this phase (1s window)
        start = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start) < 1000:
            if btn.value():
                if c == "purple":
                    print("MATCH FOUND!")
                    for _ in range(5):
                        r.value(1); g.value(1); b.value(1); utime.sleep(0.1)
                        r.value(0); g.value(0); b.value(0); utime.sleep(0.1)
                else:
                    print("WRONG COLOR - " + c)
                    utime.sleep(1)
                utime.sleep(1)
            utime.sleep(0.01)
```

### 11. Common Mistakes
*   **Wait in Loop**: If you use a simple `time.sleep(1)` for each color, your button will only work in the split second *between* sleeps. You must use a checking loop (like the one above) to catch the click at any point during the second.

### 12. Try This Next
*   **Faster Speed**: Reduce the phase time from 1s to 0.5s for a high-intensity challenge.
*   **Dynamic Target**: Draw a random target on the screen at the start of the game.

---

## 1. Project 0259: Automated Night Light

### 2. Learning Objective
Explore multi-tier thresholding (The Adaptive Efficiency Light). Learn how to use a Light Sensor (LDR) to categorize environmental brightness into three distinct zones—Day, Evening, and Night—and assign optimized power levels to each.

### 3. Concepts Introduced
*   **Zone Categorization**: Using "If / Else If" to create three distinct behavior modes.
*   **Threshold Buffering**: preventing the light from flickering when it's exactly on the line between two zones.
*   **Energy Optimization**: Using 10% for deep night and 50% for evening visibility.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Photoresistor (LDR)
*   1 LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Light Eye** | GP26 (ADC0) | Environment sensor |
| **Smart Light** | GP15 | Dynamic PWM output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (read ADC)
*   **from Logic, drag `controls_if`** (with `else if` and `else`)
*   **from Actuators, drag `pico_pwm_write`** (set output)

### 7. Variables
*   **lux**: measured ambient light value.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Measure Darkness**:
    *   **Set** `lux` = **Sensors** `pico_analog_read` GP26.

**B. Decision Phase (Zones)**
3.  **Zone 1 (Bright Day)**:
    *   If `lux` > 80% (Very bright):
        *   **Set** GP15 -> 0% (OFF). **Print** "Mode: DAY (Efficiency)".
4.  **Zone 2 (Evening/Dim)**:
    *   Else If `lux` > 30%:
        *   **Set** GP15 -> 50% (Comfort). **Print** "Mode: EVENING (Visibility)".
5.  **Zone 3 (Pitch Black)**:
    *   Else:
        *   **Set** GP15 -> 10% (Night). **Print** "Mode: NIGHT (Sleep)".

### 9. Execution Flow
1.  **Input**: The LDR reports "10000" (Dark).
2.  **Logic**: Since 10000 < 30% of max, the Pico enters Zone 3.
3.  **Output**: The LED glows at a soft 10% power to guide you through the dark without hurting your eyes.
4.  **Transition**: you turn on a nearby lamp. Lux jumps to 40000.
5.  **Reaction**: The Pico instantly shifts to Zone 2, bumping the LED to 50% so you can still see it clearly against the ambient light.
6.  **Result**: A fully autonomous light that always knows the correct amount of power to use.

### 10. Generated Code
```python
import machine
import utime

ldr = machine.ADC(machine.Pin(26))
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    val = ldr.read_u16()
    
    if val > 50000: # Very Bright (Day)
        led.duty_u16(0)
    elif val > 20000: # Dim (Evening)
        led.duty_u16(32768) # 50%
    else: # Dark (Night)
        led.duty_u16(6553) # 10%
        
    utime.sleep(0.5)
```

### 11. Common Mistakes
*   **Flicker**: if you stand in a shadow, the light might jump between zones rapidly. Adding a `wait 1s` block at the end of the loop helps stabilize the behavior.

### 12. Try This Next
*   **Negative Feedback**: try to make the light exactly inverse to the sun (as the sun goes down 1%, the LED goes up exactly 1%).

---

## 1. Project 0260: Mastering Night Light

### 2. Learning Objective
Explore acoustic-to-multimodal response (The Nursery Monitor). Learn how to combine sound detection with timed light fading and music generation, creating a complex device that comforts "Crying" detected through the sound sensor.

### 3. Concepts Introduced
*   **Acoustic Triggering**: identifying a sound event and performing a multi-step reaction.
*   **Compound Sequences**: running a fade-in followed by a melody.
*   **State Reset**: ensuring the device is ready to listen again after the lullaby finishes.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Sound Sensor Module
*   1 LED + Resistor
*   1 Passive Buzzer
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Microphone** | GP14 | Detects "Crying" |
| **Comfort Light** | GP15 | Soft warm glow |
| **Lullaby Speaker**| GP13 | Plays melody |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (evaluating noise)
*   **from Actuators, drag `pico_pwm_write`** (set output)
*   **from Actuators, drag `pico_buzzer_pitch`** (play notes)
*   **from Time, drag `pico_wait`** (timing the lullaby)

### 7. Variables
*   **None**: this is a sequence-based reaction.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Listen**:
    *   If **Sound Sensor** GP14 is HIGH:
        *   **Print** "Baby is Crying. Initiating Comfort Sequence.".

**B. Comfort Light Phase**
3.  **Slow Fade-In**: 
    *   Loop 0 to 80% brightness over 2 seconds. (Soft glow).

**C. Musical Phase**
4.  **Play Lullaby**:
    *   **Call** `pico_buzzer_pitch` for GP13: [330Hz, 349Hz, 392Hz, 330Hz].
    *   **Wait** 0.5s per note.

**D. Reset Phase**
5.  **Cleanup**:
    *   **Wait** 10 seconds (letting them fall back asleep).
    *   **Fade OUT** the light gradually.
    *   **Continue** listening.

### 9. Execution Flow
1.  **Idle**: The nursery is quiet and dark.
2.  **Sound**: A baby cries or a loud noise occurs.
3.  **Light**: The warm LED slowly wakes up, providing immediate visual reassurance.
4.  **Music**: The buzzer plays a soft, repetitive major-chord melody (The Lullaby).
5.  **Result**: A smart, automated caregiver tool that reacts instantly to environmental distress.

### 10. Generated Code
```python
import machine
import utime

# Pins
mic = machine.Pin(14, machine.Pin.IN)
led = machine.PWM(machine.Pin(15))
bz = machine.PWM(machine.Pin(13))
led.freq(1000)

def comfort():
    # 1. Fade Light In
    print("Fading in...")
    for i in range(0, 81, 2):
        led.duty_u16(int(i * 655.35))
        utime.sleep(0.05)
        
    # 2. Play Lullaby
    notes = [330, 392, 349, 262]
    for n in notes:
        bz.freq(n); bz.duty_u16(10000); utime.sleep(1)
        bz.duty_u16(0); utime.sleep(0.1)
        
    # 3. Hold and Fade out
    utime.sleep(5)
    for i in range(80, -1, -2):
        led.duty_u16(int(i * 655.35))
        utime.sleep(0.1)

while True:
    if mic.value() == 1:
        comfort()
    utime.sleep(0.1)
```

### 11. Common Mistakes
*   **False Triggers**: a door slamming or a cough might trigger the melody. You can fix this by requiring the mic to be HIGH for at least 1 full second before starting the song.

### 12. Try This Next
*   **Multiple Songs**: randomly pick a different song every time the baby cries (Project 0229).
*   **Recording**: Print the "Time of Event" to the console every time it triggers so parents can check in the morning.

---
