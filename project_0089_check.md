## Project 0089: Magnitude Counter (Coin Sorter)

### 2. Learning Objective
Analog signal categorization and multi-level thresholding. Build a sorting device that distinguishes between "Small" and "Large" objects based on how much light they block when passing in front of a Light Dependent Resistor (LDR).

### 3. Concepts Introduced
*   **Magnitude Logic**: Processing analog values not just as "On/Off", but as ranges (Small Blockage vs Large Blockage).
*   **Signal Timing**: Using a small delay to allow a moving object to reach its "peak" blockage point before making a decision.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LDR (Photoresistor)**
*   **1x 10k Resistor**
*   **Light Source (Flashlight or Ambient Lamp)**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR** | GP26 | Analog Input (ADC0) |
| **Power** | 3V3 | LDR Excitation voltage |
| **Ground** | GND | Pull-down path |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] < [Y]`** (logic_compare)
*   From **Smart Sensors**, drag **`pico_sensor_read`** (read analog sensor)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Variables**, drag **`change [variable] by [value]`** (math_change)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **ldr**: Analog sensor object on GP26.
*   **small_count**: Tracker for minor blockages.
*   **big_count**: Tracker for major blockages.
*   **val**: The raw reading from the ADC (0-65535).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **ldr** on **GP26**.
    *   Set **small_count** and **big_count** to **0**.
    *   **Snap** into the **`start`** block.

**B. Main Loop Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Monitor Surface**:
    *   From **Variables**, set **val** to **pico_sensor_read** for **ldr**.
4.  **Detect Encroachment**:
    *   From **Logic & Math**, drag a **`controls_if`**.
    *   **Condition**: Check if **val** < **50000** (Something is blocking the light).
    *   **Action**:
        *   Wait **0.1** seconds (Allow the coin/object to fully cover the sensor).
        *   Set **val** to **pico_sensor_read** again (Get the peak blockage value).
        *   **Classification**: Add an `if/else` block.
            *   **IF val < 20000**: Change **big_count** by 1, log "Large Object Found!".
            *   **ELSE**: Change **small_count** by 1, log "Small Object Found!".
        *   Wait **0.5** seconds (Cooldown to prevent double-counting).
5.  **Scan Rate**:
    *   Wait **0.01** seconds.

### 9. Execution Flow
1.  **Ambient**: Light is bright. Sensor sees 60,000.
2.  **Shadow**: A small coin passes. Value drops to 40,000.
3.  **Process**: The Pico waits 0.1s, sees it's still around 40,000. It logs a "Small" coin.
4.  **Shadow 2**: A large coin passes. Value drops to 5,000.
5.  **Process**: The Pico sees the value is below 20,000. It logs a "Large" coin.

### 10. Generated Code
```python
from machine import ADC
import time

# Initialization
ldr = ADC(Pin(26))
small_count = 0
big_count = 0

while True:
    raw = ldr.read_u16()

    # 1. Look for a trigger (Drop in light)
    if raw < 50000:
        # Give object time to reach the center of the sensor
        time.sleep(0.1)
        peak_val = ldr.read_u16()

        # 2. Categorize based on darkness depth
        if peak_val < 20000:
            big_count += 1
            print("Coin Detected: LARGE. Total:", big_count)
        else:
            small_count += 1
            print("Coin Detected: SMALL. Total:", small_count)

        # 3. Prevent re-triggering while same coin is moving away
        time.sleep(0.5)

    time.sleep(0.01)
```

### 11. Common Mistakes
*   **The Shadow Problem**: If your hand moves over the machine, it will count as a "Giant Coin". Use a cardboard tube or box to shield the LDR from your hand.
*   **Floating Thresholds**: 50,000 is for a typical desk lamp. If you are in a dark room, the "Bright" value might only be 10,000. Print the raw values first to find your own thresholds!
*   **Wait Timing**: If your coins slide too fast, 0.1s might be too long and the coin will be gone. Reduce to 0.05s if needed.

### 12. Try This Next
*   **Auto-Calibration**: At startup, read the light for 2 seconds and set the threshold to `(average_value - 10000)`.
*   **Blink per Size**: Blink a Red LED for small, Blue for big.
*   **LCD Display**: Show the current totals ("S: 5, L: 2") on a screen.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-08
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math and Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code block syntax, replaced outdated print blocks with pico_log. Updated 0089 to use Smart Sensors category and clarified LDR usage.
- Date Verified: 2026-01-08
---

## Project 0090: Digital Digit (7-Segment Display)
