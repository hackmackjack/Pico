## Project 0096: Optical Morse Link (Light Communication)

### 2. Learning Objective
Wireless data transmission using light (Optical Communication). Build a receiver system that uses an LDR to detect light pulses from a source and converts them into a digital log, demonstrating the core principles of fiber optics and Li-Fi.

### 3. Concepts Introduced
*   **Li-Fi Basics**: Communicating data via high-speed light pulses.
*   **Threshold Detection (ADC)**: Converting a varying analog light level into a "High" (Light) or "Low" (Dark) digital state for processing.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LDR (Light Dependent Resistor)**
*   **1x LED (To act as the Transmitter)**
*   **1x 10kΩ Resistor (Voltage Divider for LDR)**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LDR (ADC)** | GP26 | Analog light sensor |
| **LED** | GP15 | Light pulse transmitter |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Logic & Math**, drag **`controls_if`** (if / else)
*   From **Logic & Math**, drag **`[X] < [Y]`** (comparison)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Smart Sensors**, drag **`pico_sensor_read`** (read analog sensor)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)

### 7. Variables
*   **ldr**: ADC object for the light sensor.
*   **led**: Pin object for the blinker.
*   **val**: The raw light reading (0-65535).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Sensors**:
    *   Set **ldr** to **GP26**.
    *   Set **led** to **GP15**.
    *   **Snap** into the **`start`** block.

**B. Communication Phase (Receiver)**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Monitor the Link**:
    *   Set **val** to **pico_sensor_read** for **ldr**.
4.  **Bit Characterization**:
    *   From **Logic & Math**, drag a **`controls_if`** (else).
    *   **Condition**: If **val** < **30000** (Threshold: Darker means LED is hitting the sensor).
    *   **Action (On Light)**: Log the text **"1"**.
    *   **Action (Else Dark)**: Log the text **"_"**.
5.  **Synchronization**:
    *   Wait **0.1** seconds (Allows the system to "see" the pulse duration).

### 9. Execution Flow
1.  **Transmitter**: Another device (or another thread) flashes the LED.
2.  **Detection**: The LDR sees the light value drop (LDR resistance decreases, voltage drops).
3.  **Decoding**: The Pico sees `val` go under the threshold and prints "1".
4.  **Bitstream**: Moving your hand between the LED and LDR "cuts" the signal, resulting in "111_111_111" (Morse S).

### 10. Generated Code
```python
from machine import ADC, Pin
import time

# Initialization
ldr = ADC(Pin(26))
led = Pin(15, Pin.OUT)

# Simulating a pulse (In a real test,
# another Pico would do the transmitter part)
while True:
    # Read raw analog brightness
    val = ldr.read_u16()

    # 30,000 is a good threshold for direct LED light
    if val < 30000:
        print("1", end="")
    else:
        print("_", end="")

    # Check 10 times per second
    time.sleep(0.1)
```

### 11. Common Mistakes
*   **Ambient Light Interruption**: If the room lights are too bright, the LDR might never see the LED. Shield the LDR with a straw or a dark tube.
*   **Threshold Drift**: 30,000 works in the dark but not in the sun. Use a **pico_log(val)** block first to see what your "High" and "Low" values actually are.
*   **Missing `end=""`**: In Python, `print` adds a new line by default. Using `end=""` ensures the 1s and _s stay on the same line like a stream of data.

### 12. Try This Next
*   **Auto-Threshold**: Measure the light for 1 second at startup and set the threshold to `(measured_val / 2)`.
*   **Speed Test**: Reduce the sleep to `0.01` and see how fast you can reliably transmit data.
*   **Signal Booster**: Add a magnifying lens in front of the LDR to increase the range of the optical link.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Smart Sensors, Logic & Math, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log. Cleaned up redundant separators.
- Date Verified: 2026-01-13
---

## Project 0097: Silent Distress Signal (Covert Alarm)
