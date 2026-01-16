## Project 0090: Digital Digit (7-Segment Display)

### 2. Learning Objective
Lookup tables and multi-segment coordination. Understand how a group of independent LEDs (segments) can be combined using data arrays to display complex characters like numbers.

### 3. Concepts Introduced
*   **Lookup Tables (Arrays)**: Storing a list of predefined values that can be accessed by their index (e.g., getting the pattern for "5" by checking the 5th item in a list).
*   **Hexadecimal/Binary Mapping**: Understanding how a single number (like `0x3F`) represents an 8-bit pattern of On/Off states for segments A through G.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x 7-Segment Display (Common Cathode)**
*   **7x 220Ω Resistors**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Common (GND)** | GND | Display Ground |
| **Segment A** | GP10 | Top bar |
| **Segment B** | GP11 | Top Right |
| **...to...** | ... | (Requires 7-8 pins for full hardware control) |

### 6. Blocks Used
*   From **Loops**, drag **`controls_for`** (count with i from... to...)
*   From **Lists**, drag **`lists_create_with`** (create list with)
*   From **Lists**, drag **`lists_getIndex`** (in list _ get #)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Smart IO**, drag **`pico_log`** (log/print)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Text**, drag **`""`** (text string)
*   From **Text**, drag **`create text with`** (string concatenation)

### 7. Variables
*   **patterns**: A list containing the 10 patterns (Hex) for digits 0-9.
*   **num**: The loop counter (0 to 9).
*   **p**: The current hex pattern retrieved from the list.

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Pattern List**:
    *   Initialize **patterns** as a list with **10 items**.
    *   Fill the list with: `0x3F`, `0x06`, `0x5B`, `0x4F`, `0x66`, `0x6D`, `0x7D`, `0x07`, `0x7F`, `0x6F`.
    *   **Snap** into the **`start`** block.

**B. main Loop Phase**
2.  **Sequential Counter**:
    *   From **Loops**, drag a **`controls_for`** block to count from **0** to **9**.
3.  **The Lookup**:
    *   Inside the loop, set **p** to the value **in list patterns get # num**.
4.  **Reporting**:
    *   From **Smart IO**, drag a **`pico_log`**.
    *   Join: "Displaying Digit: " + **num** + " (Hex: " + **p** + ")".
5.  **Timing**:
    *   Wait **1.0** second so you can read the log.

### 9. Execution Flow
1.  **Start**: Pico creates the "translation" list (0x3F means 0, 0x06 means 1, etc.).
2.  **Lookup**: The code asks the list: "What the code for number 5?".
3.  **Result**: The list responds: "0x6D".
4.  **Display**: In a real circuit, the Pico would turn on segments to match the pattern. In this code, it logs the pattern to the console.
5.  **Cycle**: The count resets after reaching 9.

### 10. Generated Code
```python
import time

# Hex patterns for digits 0-9 (Common Cathode)
# Segments: dp G F E D C B A
patterns = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]

while True:
    for num in range(10):
        # Retrieve pattern from list using index
        p = patterns[num]

        print("Digit:", num, "Pattern (Hex):", hex(p))

        # Pause for readability
        time.sleep(1)
```

### 11. Common Mistakes
*   **Index Errors**: Lists are 0-indexed. If you try to get item #10 for the digit 9, the code will crash. Always ensure your count range matches your list length.
*   **Common Anode vs Cathode**: `0x3F` shows "0" on a Common Cathode display. If your display is Common Anode, all segments will be backwards! You would need to invert the code.
*   **Missing Resistors**: Connecting segments directly to the Pico can burn out the LEDs or the Pico pins. Always use 220-330Ω resistors.

### 12. Try This Next
*   **Countdown**: Make the loop count from 9 down to 0 using the `by -1` step.
*   **Random Digit**: Use a button to pick and display a random digit from 0 to 9.
*   **Alphabet**: (Advanced) Try adding patterns for letters A, B, C, D, E, F to show hexadecimal counting!

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Lists, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---



# Batch 10: Morse Code 1

## Project 0091: SOS Beacon (Morse Code Standard)
