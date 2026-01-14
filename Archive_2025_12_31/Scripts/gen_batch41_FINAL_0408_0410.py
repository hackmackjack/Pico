# Complete Batch 41: Projects 0408-0410 (Final 3 of LED Patterns 3)

target_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'

batch41_final = r'''
## 1️⃣ Project 0408: The LED Patterns Game

### 2️⃣ Learning Objective
Create an LED roulette game with decelerating spin animation. You will learn about probability simulation and deceleration curves.

### 3️⃣ Concepts Introduced
*   **Roulette Spin**: Rapidly cycling LED that slows down and stops.
*   **Deceleration Curve**: Gradually increasing delay between steps.
*   **Random Stopping**: Using randomness to select final position.

### 4️⃣ Hardware Required
*   **Pico**
*   **8× LEDs** (arranged in circle or row)
*   **Button** (Spin trigger)
*   **8× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LEDs 1-8** | GP16-GP23 | Circular arrangement |
| **Spin Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **Digital Write (×8)**
*   **Category:** Pin Access

🔹 **Random Number**
*   **Category:** Math

🔹 **Variable Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **currentLED**: Index of currently lit LED (0-7).
*   **spinSpeed**: Delay between LED changes (starts small, increases).
*   **spinsRemaining**: Countdown to stop.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16-23] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Wait for Spin**:
        *   From **Logic**, drag `wait until [digital read pin 14]`.
            *   **Snap** into loop.
        *   From **Console**, drag `print [SPINNING...]`.
            *   **Snap** below.
    *   **Determine Stop Point**:
        *   From **Math**, drag `set [spinsRemaining] to [random(20, 40)]`.
            *   **Snap** below.
        *   From **Variables**, drag `set [spinSpeed] to [0.05]`.
            *   **Snap** below.
    *   **Spin Animation**:
        *   From **Loops**, drag `repeat until [spinsRemaining] = [0]`.
            *   **Snap** below.
            *   Inside:
                *   From **Loops**, drag `for [pin] in [16-23]`.
                    *   **Snap** inside.
                    *   Inside: `digital write pin:[pin] value:[LOW]`.
                *   From **Pin Access**, drag `digital write pin:[16 + currentLED] value:[HIGH]`.
                    *   **Snap** below.
                *   From **Math**, drag `set [currentLED] to [(currentLED + 1) % 8]`.
                    *   **Snap** below.
                *   From **Variables**, drag `change [spinsRemaining] by [-1]`.
                    *   **Snap** below.
                *   From **Math**, drag `change [spinSpeed] by [0.01]`.
                    *   **Snap** below (deceleration).
                *   From **Timing**, drag `sleep [spinSpeed] seconds`.
                    *   **Snap** below.
    *   **Winner Announcement**:
        *   From **Console**, drag `print [STOPPED AT LED {currentLED + 1}!]`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

When the button is pressed, the program picks a random number of spins (20-40). The light starts moving fast (50ms per LED), gradually slowing down (60ms, 70ms, 80ms...). By the time it reaches the final spin, it's moving very slowly, building suspense. Finally, it stops on a random LED. This mimics a physical roulette wheel's deceleration.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
import random

leds = [machine.Pin(16 + i, machine.Pin.OUT) for i in range(8)]
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

current_led = 0

while True:
    if button.value():
        print("SPINNING...")
        spins_remaining = random.randint(20, 40)
        spin_speed = 0.05
        
        while spins_remaining > 0:
            # Turn off all LEDs
            for led in leds:
                led.off()
            
            # Light current LED
            leds[current_led].on()
            
            # Move to next LED
            current_led = (current_led + 1) % 8
            spins_remaining -= 1
            spin_speed += 0.01  # Decelerate
            
            time.sleep(spin_speed)
        
        print(f"STOPPED AT LED {current_led + 1}!")
        time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Stops Too Quickly**: If the deceleration is too aggressive (e.g., `+= 0.05`), reduce increment to 0.01.
*   **Predictable**: If it always stops at the same LED, ensure `random()` is inside the button press block, not outside.

### 1️⃣2️⃣ Try This Next

*   **Prize System**: Assign point values to each LED (LED 1 = 10 pts, LED 8 = 100 pts).
*   **Sound Effects**: Play click sounds during spin, celebration sound on stop.

---

## 1️⃣ Project 0409: Automated LED Patterns

### 2️⃣ Learning Objective
Create time-based event markers using periodic LED flashes. You will learn about chronometer logic and modulo-based scheduling.

### 3️⃣ Concepts Introduced
*   **Time Marker**: Periodic event signaling (every minute, every hour).
*   **Chronometer Logic**: Triggering actions at specific time intervals.
*   **Modulo Scheduling**: Using `time % interval` to detect events.

### 4️⃣ Hardware Required
*   **Pico**
*   **2× LEDs**
*   **2× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Minutes LED** | GP16 | Flashes every "minute" |
| **Hours LED** | GP17 | Flashes every "hour" |

### 6️⃣ Blocks Used

🔹 **Time Tracking**
*   **Category:** Timing

🔹 **Modulo Operator**
*   **Category:** Math

🔹 **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **elapsedSeconds**: Time since boot.
*   **lastMinuteFlash**: Timestamp of last minute marker.
*   **lastHourFlash**: Timestamp of last hour marker.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[16,17] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [startTime] to [time()]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Calculate Elapsed Time**:
        *   From **Timing**, drag `set [elapsedSeconds] to [time() - startTime]`.
            *   **Snap** into loop.
    *   **Minute Marker (every 60s)**:
        *   From **Logic**, drag `if [elapsedSeconds % 60] < [0.5] then`.
            *   **Snap** below (detects near-zero remainder).
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
                    *   **Snap** inside.
                *   From **Timing**, drag `sleep [0.2] seconds`.
                    *   **Snap** below.
                *   From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
                    *   **Snap** below.
    *   **Hour Marker (every 3600s)**:
        *   From **Logic**, drag `if [elapsedSeconds % 3600] < [0.5] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[17] value:[HIGH]`.
                *   From **Timing**, drag `sleep [0.5] seconds`.
                *   From **Pin Access**, drag `digital write pin:[17] value:[LOW]`.
    *   From **Timing**, drag `sleep [0.5] seconds`.
        *   **Snap** below (polling interval).

### 9️⃣ Execution Flow (Plain English)

The program tracks elapsed time since boot. Every 60 seconds, the "Minutes" LED flashes briefly (0.2s). Every 3600 seconds (1 hour), the "Hours" LED flashes longer (0.5s). For testing, simulate minutes as seconds (every 1 second = "minute" flash). This creates an ambient time awareness display.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

led_minutes = machine.Pin(16, machine.Pin.OUT)
led_hours = machine.Pin(17, machine.Pin.OUT)

start_time = time.time()

while True:
    elapsed = time.time() - start_time
    
    # Flash every "minute" (60s for real, 1s for testing)
    if int(elapsed) % 1 == 0:  # Use % 60 for real minutes
        led_minutes.on()
        time.sleep(0.2)
        led_minutes.off()
    
    # Flash every "hour" (3600s for real, 10s for testing)
    if int(elapsed) % 10 == 0:  # Use % 3600 for real hours
        led_hours.on()
        time.sleep(0.5)
        led_hours.off()
    
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Double Flash**: If using `==` instead of `<`, the same second might trigger twice. Use `< 0.5` to detect the window.
*   **Missed Events**: If sleep is too long, you might skip the exact moment. Keep polling interval small (0.5s).

### 1️⃣2️⃣ Try This Next

*   **7-Segment Display**: Instead of LEDs, show elapsed time on a 4-digit display.
*   **Alarm Clock**: Add button to set target time; flash red LED when time matches.

---

## 1️⃣ Project 0410: Mastering LED Patterns

### 2️⃣ Learning Objective
Implement Charlieplexing to control 6 LEDs with only 3 pins using tri-state logic. You will learn about advanced pin optimization and hardware multiplexing.

### 3️⃣ Concepts Introduced
*   **Charlieplexing**: Controlling N*(N-1) LEDs with N pins.
*   **Tri-State**: Using INPUT, OUTPUT HIGH, OUTPUT LOW pin modes.
*   **Pin Optimization**: Maximizing LED count with minimal GPIO.

### 4️⃣ Hardware Required
*   **Pico**
*   **6× LEDs**
*   **3× Resistors** (220Ω)

### 5️⃣ Wiring / Interfaces

| LED Pair | Anode | Cathode | Active When |
| :--- | :--- | :--- | :--- |
| **LED 1** | Pin A (GP16) | Pin B (GP17) | A=HIGH, B=LOW, C=INPUT |
| **LED 2** | Pin B (GP17) | Pin A (GP16) | B=HIGH, A=LOW, C=INPUT |
| **LED 3** | Pin A (GP16) | Pin C (GP18) | A=HIGH, C=LOW, B=INPUT |
| **LED 4** | Pin C (GP18) | Pin A (GP16) | C=HIGH, A=LOW, B=INPUT |
| **LED 5** | Pin B (GP17) | Pin C (GP18) | B=HIGH, C=LOW, A=INPUT |
| **LED 6** | Pin C (GP18) | Pin B (GP17) | C=HIGH, B=LOW, A=INPUT |

### 6️⃣ Blocks Used

🔹 **Pin Mode Control**
*   **Category:** Pin Access

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Sequential Logic**
*   **Category:** Loops

### 7️⃣ Variables & State
*   **currentLED**: Which LED to light (1-6).
*   **pinConfigs**: List of pin states for each LED.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   No fixed setup—pins dynamically reconfigure.

*   **B. Main Loop Phase**
    *   **Light LED 1 (A→B)**:
        *   From **Pin Access**, drag `set pin:[16] mode:[OUTPUT]`.
            *   **Snap** into loop.
        *   From **Pin Access**, drag `set pin:[17] mode:[OUTPUT]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `set pin:[18] mode:[INPUT]`.
            *   **Snap** below (unused pin as input).
        *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `digital write pin:[17] value:[LOW]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [0.3] seconds`.
            *   **Snap** below.
    *   **Light LED 2 (B→A)**:
        *   (Same structure, swap A/B roles)
    *   **Light LED 3 (A→C)**:
        *   Pin A=OUT, Pin C=OUT, Pin B=INPUT
        *   Pin A=HIGH, Pin C=LOW
    *   (Continue for LEDs 4, 5, 6...)

### 9️⃣ Execution Flow (Plain English)

Charlieplexing works by rapidly switching pin configurations. To light LED 1, Pin A is set HIGH and Pin B LOW (Pin C is input). To light LED 2, the roles reverse: Pin B HIGH, Pin A LOW. By cycling through all 6 configurations fast enough, all LEDs appear to be on simultaneously (persistence of vision). This uses only 3 pins instead of 6.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

pinA = machine.Pin(16)
pinB = machine.Pin(17)
pinC = machine.Pin(18)

def light_led(led_num):
    if led_num == 1:  # A→B
        pinA.init(machine.Pin.OUT); pinA.on()
        pinB.init(machine.Pin.OUT); pinB.off()
        pinC.init(machine.Pin.IN)
    elif led_num == 2:  # B→A
        pinB.init(machine.Pin.OUT); pinB.on()
        pinA.init(machine.Pin.OUT); pinA.off()
        pinC.init(machine.Pin.IN)
    elif led_num == 3:  # A→C
        pinA.init(machine.Pin.OUT); pinA.on()
        pinC.init(machine.Pin.OUT); pinC.off()
        pinB.init(machine.Pin.IN)
    elif led_num == 4:  # C→A
        pinC.init(machine.Pin.OUT); pinC.on()
        pinA.init(machine.Pin.OUT); pinA.off()
        pinB.init(machine.Pin.IN)
    elif led_num == 5:  # B→C
        pinB.init(machine.Pin.OUT); pinB.on()
        pinC.init(machine.Pin.OUT); pinC.off()
        pinA.init(machine.Pin.IN)
    elif led_num == 6:  # C→B
        pinC.init(machine.Pin.OUT); pinC.on()
        pinB.init(machine.Pin.OUT); pinB.off()
        pinA.init(machine.Pin.IN)

while True:
    for led in range(1, 7):
        light_led(led)
        time.sleep(0.3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Wrong LED Lights**: Double-check anode/cathode polarity. LEDs are directional.
*   **Multiple LEDs Dim**: If not setting unused pin to INPUT, current may leak through multiple paths.

### 1️⃣2️⃣ Try This Next

*   **4 Pins = 12 LEDs**: Expand to 4 pins for 12 LEDs using the formula N*(N-1).
*   **PWM Charlieplexing**: Vary on-time to dim specific LEDs while multiplexing.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch41_final)

print("✅ BATCH 41 COMPLETE: Projects 0401-0410 (LED Patterns 3)")
print("📊 Progress: 10/100 projects documented")
print("📋 Next: Batch 42 (Button Logic 3, Projects 0411-0420)...")
