## Project 0079: Ninja Reflex (Wave Detector)

### 2. Learning Objective
High-speed polling with non-contact sensors. Build a reaction game that measures physical "swiping" speed by detecting when a hand passes through an Ultrasonic sensor's field of view immediately after a visual cue.

### 3. Concepts Introduced
*   **Non-Contact Interaction**: Using distance thresholds as a "virtual button".
*   **Physical Range Gating**: Setting a specific distance (e.g., < 20cm) to ignore background movement and only capture intentional swipes.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Ultrasonic Sensor (HC-SR04)**
*   **1x LED**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Trig** | GP16 | Sensor Trigger |
| **Echo** | GP17 | Sensor Echo |
| **LED** | GP15 | Reaction Signal |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_whileUntil`** (while)
*   From **Logic & Math**, drag **`[X] > [Y]`** (logic_compare)
*   From **Logic & Math**, drag **`random integer from 1 to 100`** (math_random_int)
*   From **Smart Sensors**, drag **`get distance cm`** (pico_ultrasonic_dist)
*   From **Smart IO**, drag **`get current time (ms)`** (ticks_ms)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **led**: Pin object for output.
*   **trig, echo**: Pins for sensor (often handled by a single Ultrasonic block).
*   **start_time**: Number variable recording the moment the LED turns On.
*   **reaction_time**: Number variable calculating (Current Time - Start Time).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Create variables **`led`**, **`start_time`**, and **`reaction_time`**.
    *   Initialize **led** on **GP15**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **The Anticipation**:
    *   From **Smart IO**, set **led** to **LOW (0)**.
    *   From **Smart IO**, wait **`random 2000 to 5000`** milliseconds (2-5s random wait).
4.  **The Challenge**:
    *   From **Smart IO**, set **led** to **HIGH (1)**.
    *   From **Variables**, set **`start_time`** to **`get current time (ms)`**.
5.  **Monitoring for Motion**:
    *   From **Loops**, drag a **`controls_whileUntil`** (while).
    *   **Condition**: Check if **`get distance cm`** (Pins GP16/17) > **20**.
    *   **Action**: Wait **0.01** seconds (Wait until something moves closer than 20cm).
6.  **Calculate & Report**:
    *   From **Variables**, set **`reaction_time`** to (**`get current time (ms)`** - **`start_time`**).
    *   From **Smart IO**, **pico_log**: **"Time: "** + **`reaction_time`** + **" ms"**.
    *   Set **led** to **LOW (0)**.
7.  **Cooldown**:
    *   Wait **3.0** seconds before the next test.

### 9. Execution Flow
1.  **Idle**: The Pico waits silently.
2.  **Flash**: The LED snaps On.
3.  **Ninja Move**: You swipe your hand in front of the sensor.
4.  **Feedback**: The console reveals your reaction time in milliseconds.

### 10. Generated Code
```python
from machine import Pin
import time
import random
from pico_sensor import Ultrasonic

# Initialization
led = Pin(15, Pin.OUT)
ultrasonic = Ultrasonic(trig=Pin(16), echo=Pin(17))

while True:
    led.value(0)
    # Random wait to prevent pattern memorization
    time.sleep(random.uniform(2.0, 5.0))

    # 1. Signal GO
    led.value(1)
    start_time = time.ticks_ms()

    # 2. Poll for movement
    while ultrasonic.distance_cm() > 20:
        time.sleep(0.01)

    # 3. Calculate Speed
    reaction = time.ticks_diff(time.ticks_ms(), start_time)
    print("Ninja Swipe Speed:", reaction, "ms")

    led.value(0)
    time.sleep(3) # Take a breath
```

### 11. Common Mistakes
*   **Sensor Range**: If your "swipe" is too far away (>100cm), the sensor might miss it. Keep your hand within 20cm of the sensor face.
*   **False Trigger**: Ensure the sensor is pointing away from moving fans or people walking across the room, or they will finish the game for you!
*   **Timeout**: If no one swipes, the LED stays on forever. You could add a 10s timeout to auto-reset.

### 12. Try This Next
*   **Buzz the Speed**: Use a buzzer that plays a higher pitch for faster swipes.
*   **Multiplayer Duels**: Set up two sensors. See who can swipe through their sensor first.
*   **Calibration**: Automatically measure the average room distance for 2 seconds at startup to set a better threshold than "20cm".

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Smart Sensors, Logic & Math, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-08

### 11. Common Mistakes
*   **Loop Latency**: `get_dist` takes time (e.g. 20ms). This adds to your reaction time score. It's not perfectly precise but good for relative games.

### 12. Try This Next
*   **Cheater**: Check if distance < 20cm *before* the light turns on.
*   **Best of 3**: Average your score.

## Project 0080: Binary Brain (Cognitive Count)
