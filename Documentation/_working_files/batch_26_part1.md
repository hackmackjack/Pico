
# BATCH 26: Night Light 2 (Projects 0251-0260)

## 1. Project 0251: Introduction to Night Light

### 2. Learning Objective
Explore battery conservation via duty cycle (Low Power Mode). Learn how to use Pulse Width Modulation (PWM) to intentionally limit the brightness of an LED, extending the lifespan of a portable light source while maintaining sufficient visibility.

### 3. Concepts Introduced
*   **Low Duty Cycle**: restricting power flow to only 10% of the maximum.
*   **Energy Efficiency**: reducing thermal waste and current draw in embedded systems.
*   **Static Dimming**: setting a permanent brightness level for background illumination.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Night Light LED** | GP15 | PWM output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Actuators, drag `pico_pwm_write`** (set Brightness)
*   **from Time, drag `pico_wait`** (sustenance)

### 7. Variables
*   **None**: this is a fixed-value power setting.

### 8. Step-by-Step Guide

**A. Configuration Phase**
1.  **Select Dimming Level**:
    *   From **Actuators**, drag `pico_pwm_write`.
    *   **Set** GP15 Brightness to **10%**.

**B. Maintenance Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Hold State**:
    *   Inside the loop, simply **Wait** 1.0 second.
    *   *Note: Since the PWM hardware has its own memory, the LED will stay dim even while the code is waiting.*

### 9. Execution Flow
1.  **Initialize**: The Pico configures the internal timer for GP15.
2.  **Output**: Electricity is sent to the LED in very short, fast bursts (10% of the time).
3.  **Result**: The LED glows with a soft, non-intrusive light suitable for a dark bedroom, using minimal battery.

### 10. Generated Code
```python
import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)

# 10% Duty (6553 approx)
led.duty_u16(6553)

print("Night Light: Low Power Mode Active")

while True:
    utime.sleep(1)
```

### 11. Common Mistakes
*   **High Power**: If you use `pico_gpio_write` (HIGH), the LED will be at 100% brightness, which might be too bright and drain the battery 10 times faster.

### 12. Try This Next
*   **Ultralow Mode**: Try setting it to 1% brightness. Is it still visible in a pitch-black room?
*   **Power Measure**: If you have a multimeter, measure the current at 10% vs 100% brightness.

---

## 1. Project 0252: Blinking Night Light

### 2. Learning Objective
Explore organic randomization (The Candle Flicker). Learn how to use a random number generator to vary PWM duty cycles rapidly, simulating the natural, unpredictable movement of a physical flame.

### 3. Concepts Introduced
*   **Stochastic Modulation**: changing a value based on random probability.
*   **Visual Texture**: using fast changes in light to create a "Living" atmosphere.
*   **Clamped Randomness**: keeping brightness within a "Flicker Range" (e.g., 30-80%) to avoid complete darkness.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Yellow or Orange LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Candle LED** | GP15 | Flicker Output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Math, drag `math_random_int`** (picking brightness)
*   **from Actuators, drag `pico_pwm_write`** (set Brightness)
*   **from Time, drag `pico_wait_ms`** (fast updates)

### 7. Variables
*   **flicker_val**: Number representing current flame intensity.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.

**B. Randomization Phase**
2.  **Choose Intensity**:
    *   From **Variables**, **Set** `flicker_val` = **Math** `random integer from 30 to 80`.
3.  **Update Light**:
    *   From **Actuators**, **Set** GP15 Brightness to `flicker_val`%.

**C. Pacing Phase**
4.  **Temporal Jitter**:
    *   From **Time**, **Wait** 0.05 seconds.
    *   *Note: This fast speed is what makes the light look like a real flame.*

### 9. Execution Flow
1.  **Draft**: The Pico enters the loop. It rolls a virtual 100-sided die.
2.  **Result**: It gets "42". It sets the LED to 42% brightness.
3.  **Next**: 50ms later, it gets "75". The LED jumps to 75% brightness.
4.  **Result**: To your eyes, the constant jumping looks like the chaotic movement of light reflecting off a candle wick.

### 10. Generated Code
```python
import machine
import utime
import urandom

led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    # Random brightness between 30% and 80%
    bright = urandom.randint(30, 80)
    
    # Map % (0-100) to duty (0-65535)
    duty = int(bright * 655.35)
    led.duty_u16(duty)
    
    # Fast timing for organic feel
    utime.sleep_ms(urandom.randint(50, 150))
```

### 11. Common Mistakes
*   **Full Range Random**: If you pick random between 0 and 100, the "flame" will turn off completely (0) very often, which looks like a loose wire, not a candle.
*   **Slow Timing**: If you wait 1 second between changes, it won't flicker; it will just look like a blinking light.

### 12. Try This Next
*   **Deep Pulse**: add a slow 2-second "Pulse" underneath the flicker to simulate a candle bowing in the wind.
*   **Dual Candle**: add a second LED on GP14 with its own separate random loop.

---

## 1. Project 0253: Manual Night Light Control

### 2. Learning Objective
Explore incremental state adjustment (The Touch Dimmer). Learn how to use two momentary inputs to modify a single numerical variable (Brightness), ensuring the value stays within logical bounds (0-100%).

### 3. Concepts Introduced
*   **Stepwise Incrementation**: Adding or subtracting a fixed amount (e.g. +10%) per press.
*   **Min/Max Constraints**: preventing a variable from going so low it becomes negative or so high it breaks the PWM range.
*   **User Precision**: allowing the human to find their "Perfect" lighting level.

### 4. Hardware Required
*   Raspberry Pi Pico
*   2 Buttons (Up and Down)
*   1 LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Brighter (+)** | GP14 | Increments PWM |
| **Dimmer (-)** | GP13 | Decrements PWM |
| **Main Light** | GP15 | Adjusted illumination |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Logic, drag `controls_if`** (checking buttons)
*   **from Math, drag `math_arithmetic`** (+ and -)
*   **from Variables, drag `variables_set`** (storing level)
*   **from Actuators, drag `pico_pwm_write`** (set LED)

### 7. Variables
*   **level**: Number (0-100) tracking user choice.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Start Point**: From **Variables**, **Set** `level` = 50 (Half brightness).

**B. Monitoring Phase (Loop)**
2.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
3.  **Increase Logic**:
    *   If **Button** GP14 is Pressed:
        *   **Set** `level` = `level` + 10.
        *   **Wait** 0.2s.
4.  **Decrease Logic**:
    *   If **Button** GP13 is Pressed:
        *   **Set** `level` = `level` - 10.
        *   **Wait** 0.2s.

**C. Maintenance Phase (Bounds)**
5.  **Protect Range**:
    *   If `level` > 100: **Set** `level` = 100.
    *   If `level` < 0: **Set** `level` = 0.
6.  **Apply**:
    *   From **Actuators**, **Set** GP15 Brightness to `level`%.

### 9. Execution Flow
1.  **Interaction**: You press the "+" button three times.
2.  **Math**: The Pico moves the variable: 50 -> 60 -> 70 -> 80.
3.  **Output**: The LED gets visibly brighter with each click.
4.  **Safety**: You mash the button 20 times. The internal math hits 100 and stops. It never tries to go to 200%.
5.  **Result**: A responsive, custom dimmer switch.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

led = PWM(Pin(15))
btn_up = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_dn = Pin(13, Pin.IN, Pin.PULL_DOWN)

brightness = 50

while True:
    # Handle Up
    if btn_up.value() == 1:
        brightness += 10
        if brightness > 100: brightness = 100
        print("Level: " + str(brightness))
        time.sleep(0.2)
        
    # Handle Down
    if btn_dn.value() == 1:
        brightness -= 10
        if brightness < 0: brightness = 0
        print("Level: " + str(brightness))
        time.sleep(0.2)
        
    # Apply to LED
    duty = int(brightness * 655.35)
    led.duty_u16(duty)
    
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **No Clamping**: If you don't use the "If > 100" block, your code might eventually send a huge number to the PWM chip, which might cause an error or unwanted behavior.

### 12. Try This Next
*   **Fine Tuning**: change the step from 10 to 1 so you can adjust the light very gradually.
*   **Blink at Max**: make the LED flash once if the user tries to go above 100 or below 0.

---

## 1. Project 0254: Night Light Sequences

### 2. Learning Objective
Explore long-duration temporal ramps (The Sunset Sleep-Aid). Learn how to divide a large time interval (e.g. 10 seconds) into tiny mathematical steps to create a seamless fade-out effect that helps a user transition to sleep.

### 3. Concepts Introduced
*   **Linear Fading**: Reducing a value by small amounts over many cycles.
*   **Temporal Calibration**: adjusting wait times to match a real-world duration (Sunset).
*   **Auto-Deactivation**: turning the system completely OFF once the sequence reaches zero.

### 4. Hardware Required
*   Raspberry Pi Pico
*   Red or Warm White LED + Resistor
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sunset LED** | GP15 | Gradual fade output |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Loops, drag `controls_repeat_ext`** (climbing down)
*   **from Actuators, drag `pico_pwm_write`** (set brightness)
*   **from Time, drag `pico_wait_ms`** (step timing)

### 7. Variables
*   **fade_level**: index tracking the sunset.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Startup**: **Set** GP15 Brightness to 100%.

**B. Sequence Phase**
2.  **Start Fade Loop**:
    *   From **Loops**, drag `count with fade_level from 100 down to 0 by 1`.
    *   Inside:
        *   **Set** GP15 Brightness to `fade_level`%.
        *   **Set** Delay = 100ms. (100 steps * 100ms = 10 second sunset).

**C. Final Phase**
3.  **Cut Power**:
    *   After the loop finishes, **Set** GP15 -> LOW (0).
    *   **Print** "User is asleep. Light OFF.".

### 9. Execution Flow
1.  **Start**: You turn the light on. It is bright and useful.
2.  **Sequence**: The Pico begins counting down. 100... 99... 98...
3.  **Subtlety**: Every 1/10th of a second, the light gets 1% dimmer. It is so smooth you can barely see the change happening.
4.  **End**: After 10 seconds, the light reaches 0% and shuts off.
5.  **Result**: An automated sleep-aid that doesn't require you to get out of bed to turn the light off.

### 10. Generated Code
```python
import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)

print("Sunset sequence started...")

# Start at 100% and fade to 0%
for i in range(100, -1, -1):
    duty = int(i * 655.35)
    led.duty_u16(duty)
    
    # 0.1s delay * 100 steps = 10s total
    utime.sleep(0.1)

print("Sunset complete.")
led.duty_u16(0)
```

### 11. Common Mistakes
*   **Linear vs Logarithmic**: Human eyes are better at seeing changes in dark light than bright light. A "Perfect" sunset actually needs more steps at the end than at the beginning! For now, linear is a great start.

### 12. Try This Next
*   **Real-time Sunset**: change the `wait` to 3.0 seconds. Now the light will take 5 full minutes to fade out, just like a real sunset.
*   **Abort Button**: add a button that lets you jump back to 100% if you aren't tired yet.

---

## 1. Project 0255: Interactive Night Light

### 2. Learning Objective
Explore temporal accumulation (The Usage Timer). Learn how to use a software "Timer" to calculate exactly how many seconds a hardware component was active, allowing for battery-life estimation or usage monitoring.

### 3. Concepts Introduced
*   **Time Deltas**: `end_time - start_time`.
*   **Conditional Accumulation**: only counting time while a specific state (LED ON) is active.
*   **User Reports**: calculating a final number and presenting it to the console.

### 4. Hardware Required
*   Raspberry Pi Pico
*   1 Button (The Switch)
*   1 LED
*   Breadboard and jumper wires

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Pwr Button** | GP14 | Turns light on/off |
| **Main Light** | GP15 | Being monitored |

### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Time, drag `pico_time_ms`** (getting timestamps)
*   **from Variables, drag `variables_set`** (tracking state)
*   **from Logic, drag `controls_if`** (detecting transitions)

### 7. Variables
*   **is_on**: Boolean.
*   **start_time**: timestamp when light was turned on.
*   **total_seconds**: the calculated result.

### 8. Step-by-Step Guide

**A. Monitoring Phase (Loop)**
1.  **Start Main Loop**: From **Loops**, drag `pico_forever`.
2.  **Handle Turn-ON**:
    *   If **Button** GP14 is Pressed and `is_on` is False:
        *   **Set** `is_on` = True.
        *   **Set** `start_time` = **Time** `pico_time_ms`.
        *   **Set** LED (GP15) -> HIGH.

**B. Handle Turn-OFF**
3.  **Calculate Duration**:
    *   If **Button** GP14 is Pressed and `is_on` is True:
        *   **Set** `is_on` = False.
        *   **Set** `end_time` = **Time** `pico_time_ms`.
        *   **Set** `total_seconds` = (`end_time` - `start_time`) / 1000.
        *   **Print** "Usage: ", `total_seconds`, " seconds.".
        *   **Set** LED -> LOW.

**C. Wait for release**:
4.  **Debounce**: **Wait** 0.3s after any button press.

### 9. Execution Flow
1.  **Action**: You click the button. The light comes on. The Pico writes down "Start: 12:00:00".
2.  **Time Passes**: You leave the light on while you read.
3.  **Action**: You click the button again. The light goes off.
4.  **Math**: The Pico writes down "End: 12:05:00". It subtracts the two numbers to get "5 minutes".
5.  **Result**: The screen shows you exactly how much electricity you just used.

### 10. Generated Code
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

is_on = False
t_start = 0

while True:
    if btn.value() == 1:
        if not is_on:
            # TURN ON
            is_on = True
            t_start = time.ticks_ms()
            led.value(1)
            print("Light ON")
        else:
            # TURN OFF
            is_on = False
            t_diff = time.ticks_diff(time.ticks_ms(), t_start)
            secs = t_diff / 1000
            led.value(0)
            print("Light OFF. Used for: " + str(secs) + "s")
        
        time.sleep(0.3) # Debounce
        
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **Integer Division**: If you use only whole numbers, 5.5 seconds might show up as just "5". Always make sure your code uses "Floats" for accurate time.
*   **Missing State Check**: if you don't track `is_on`, the code won't know if this click is a "Start" or a "Stop".

### 12. Try This Next
*   **Battery Alert**: if the total usage exceeds 1 hour (3600 seconds), make an LED blink to remind you to change batteries.
*   **Cost Estimate**: multiply `total_seconds` by a small number to "estimate" the cost of the electricity.

---
