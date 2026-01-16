## Project 0092: Manual Telegraph (Button Mirroring)

### 2. Learning Objective
Direct hardware mirroring and real-time logic response. Build a manual telegraph key where an LED mirrors the exact duration of a button press, allowing for human-controlled Morse code transmission.

### 3. Concepts Introduced
*   **Direct Keying**: Mapping a digital input state (High/Low) directly to an output state without complex intermediate processing.
*   **Latency vs. Scan Rate**: Understanding how the loop speed affects the "feel" and accuracy of a manual input device.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Push Button**
*   **1x LED**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP10 | Telegraph Key (Pull-Down) |
| **LED** | GP15 | Visual Signal |
| **Ground** | GND | Common Ground reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Smart IO**, drag **`pico_gpio_read`** (read Pin)
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)

### 7. Variables
*   **btn**: Pin object for the tap button.
*   **led**: Pin object for the signaling LED.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware Variables**:
    *   Initialize **btn** (GP10) and **led** (GP15).
    *   **Snap** into the **`start`** block.

**B. Mirroring Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **The Relay Logic**:
    *   From **Logic & Math**, drag a **`controls_if`** with an **else**.
    *   **Condition**: Check if **pico_gpio_read** for **btn** equals **1**.
    *   **Action (If Pressed)**: Turn **led** to **HIGH**.
    *   **Action (Else Released)**: Turn **led** to **LOW**.
4.  **Responsiveness**:
    *   Wait **0.01** seconds (Provides high-speed scanning for accurate keying).

### 9. Execution Flow
1.  **Idle**: Button is up. LED is Off.
2.  **Tap**: You press the button. The Pico immediately sets GP15 high.
3.  **Release**: You let go. The Pico immediately sets GP15 low.
4.  **Sequence**: By tapping in short and long bursts, you can transmit "HELLO" manually.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
btn = Pin(10, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

while True:
    # Direct hardware mirroring
    if btn.value() == 1:
        led.value(1)
    else:
        led.value(0)

    # High scan rate for manual "feel"
    time.sleep(0.01)
```

### 11. Common Mistakes
*   **The Wait Trap**: If you set the `pico_wait` block to 1.0 seconds, your telegraph will feel "broken" because it will only check the button once every second. Manual inputs require fast loops (0.01s to 0.05s).
*   **Pull-Down Missing**: If you forget the Pull-Down resistor (logic or physical), the LED might flicker or stay ON forever when you aren't touching the button.
*   **Logical Inversion**: Swapping the HIGH and LOW in the IF block will make the LED stay ON and turn OFF only when you press the key.

### 12. Try This Next
*   **Sound Keyer**: Add a Buzzer on GP14 and turn it ON/OFF alongside the LED.
*   **Toggle Mode**: Change the logic so that one tap turns the LED ON, and the next tap turns it OFF.
*   **Ghost Keyer**: Add a `pico_log` block to print "Key Down" and "Key Up" to the console for debugging your rhythm.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Logic & Math, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax.
- Date Verified: 2026-01-13
---
## Project 0093: Input Quantizer (Auto-Dot & Auto-Dash)
