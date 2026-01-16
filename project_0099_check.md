## Project 0099: Automated Morse Beacon (Low Power Signaling)

### 2. Learning Objective
Building periodic background tasks and message repetition. Build a beacon system that transmits a specific Morse digit (e.g., "1") every 10 seconds, focusing on timing logic and system idle states.

### 3. Concepts Introduced
*   **Low Power Design**: Keeping the system in a waiting state (idle) during long breaks between active tasks.
*   **Beacon Protocols**: Automatically re-broadcasting an ID signal to help other devices find or identify the station.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **1x 220Ω Resistor**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Beacon LED** | GP15 | Visual Signal |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_repeat_ext`** (repeat _ times)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Smart IO**, drag **`pico_log`** (log/print)

### 7. Variables
*   **led**: Pin object for GP15.
*   **UNIT**: The base timing duration (0.2s).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Constants**:
    *   Initialize **led** on **GP15**.
    *   Set **UNIT** to **0.2**.
    *   **Snap** into the **`start`** block.

**B. Transmission Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **The Identifier (Digit "1": .----)**:
    *   **Dot**: Turn **led** ON -> Wait **UNIT** -> OFF -> Wait **UNIT**.
    *   **4 Dashes**:
        *   From **Loops**, drag a **`controls_repeat_ext`** (repeat 4 times).
        *   Inside: Turn **led** ON -> Wait **UNIT * 3** -> OFF -> Wait **UNIT**.
4.  **The Idle Buffer**:
    *   **pico_log** text "Beacon cycle complete. Sleeping...".
    *   Wait **10.0** seconds before the next broadcast.

### 9. Execution Flow
1.  **Broadcast**: The LED pulses once, then stays on 3x longer for four pulses.
2.  **Quiet Phase**: The LED stays dark for exactly 10 seconds.
3.  **Repeat**: The Pico wakes up from the `pico_wait` block and restarts the Morse sequence.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
led = Pin(15, Pin.OUT)
UNIT = 0.2

while True:
    # 1 (.----)
    # Dot
    led.value(1)
    time.sleep(UNIT)
    led.value(0)
    time.sleep(UNIT)

    # 4 Dashes
    for _ in range(4):
        led.value(1)
        time.sleep(UNIT * 3)
        led.value(0)
        time.sleep(UNIT)

    print("Beacon cycle complete. Sleeping...")

    # Wait 10 seconds (Beacon Interval)
    time.sleep(10.0)
```

### 11. Common Mistakes
*   **Drift**: `time.sleep` isn't a precise clock. Over days, it will drift seconds. For real beacons, a dedicated RTC (Real Time Clock) should be used to trigger pulses.
*   **Duty Cycle**: If the beacon flashes too often (e.g., every 1 second), it may use too much battery. 10 seconds is a standard low-power interval.
*   **Signal Blur**: If `UNIT` is too fast (e.g., 0.05), the dashes may look like dots to a human observer from a distance.

### 12. Try This Next
*   **Light Sensor**: Only allow the beacon to activate at night (using an LDR).
*   **Identifier Rotation**: Change the digit every 5 cycles (Beacon 1... Beacon 2) to indicate station status.
*   **Buzzer Beacon**: Add a sound pulse to the beacon for non-line-of-sight tracking.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---

## Project 0100: Mastering Morse Code (Translator)
