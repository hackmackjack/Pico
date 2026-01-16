## Project 0100: Mastering Morse Code (Translator)

### 2. Learning Objective
Translating complex data structures into hardware signals. Build a text-to-baudot engine that takes a message string (like "PICO") and automatically pulses a Buzzer with the correct Morse patterns using list-based lookup tables.

### 3. Concepts Introduced
*   **Data Mapping (Dictionaries)**: Using paired lists or maps to connect human letters ('A') to hardware patterns ('.-').
*   **String Iteration**: Processing a word character by character in a loop.
*   **Variable Pulse Width**: Changing the duration of a signal based on the value found in the data table.

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x Passive Buzzer**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | Audio Output (PWM) |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Loops**, drag **`controls_forEach`** (for each item i in list)
*   From **Lists**, drag **`lists_create_with`** (create list)
*   From **Lists**, drag **`lists_getIndex`** (get item #)
*   From **Text**, drag **`text`** ("CAB")
*   From **Smart IO**, drag **`pico_pwm_freq_duty`** (set PWM)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)

### 7. Variables
*   **buzzer**: PWM object on GP15.
*   **chars**: List of letters (A, B, C...).
*   **codes**: List of Morse patterns (.-, -..., -.-.).
*   **message**: The text you want to translate (e.g., "CAB").

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Data Tables**:
    *   Initialize **buzzer** on **GP15**.
    *   Set **chars** to a list: ["A", "B", "C"].
    *   Set **codes** to a list: [".-", "-...", "-.-."].
    *   Set **message** to "CAB".
    *   **Snap** into the **`start`** block.

**B. The Translator Phase**
2.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
3.  **Process Letters**:
    *   From **Loops**, drag a **`controls_forEach`** (for each `letter` in `message`).
4.  **Lookup Logic**:
    *   Find the **index** of `letter` in the **chars** list.
    *   Get the corresponding **code** from the **codes** list at that index.
    *   **pico_log** text "Translating: " + `letter`.
5.  **Pulsing the Code**:
    *   Inside the letter loop, drag another **`forEach`** (for each `symbol` in `code`).
    *   If **symbol** is ".": Pulse Buzzer ON (0.1s) -> OFF (0.1s).
    *   Else (symbol is "-"): Pulse Buzzer ON (0.3s) -> OFF (0.1s).
6.  **Inter-Letter Timing**:
    *   Wait **0.3** seconds after each letter finishes.

### 9. Execution Flow
1.  **Input**: The dictionary contains letters up to "C". Your message is "CAB".
2.  **Processing**: The Pico takes "C" -> finds "-.-." -> beeps long-short-long-short.
3.  **Iteration**: It moves to "A" -> ".-" -> beeps short-long.
4.  **Finalization**: It finishes with "B" -> "-..." -> long-short-short-short.
5.  **Cycle**: The word "CAB" repeats forever.

### 10. Generated Code
```python
from machine import Pin, PWM
import time

# Initialization
buzz = PWM(Pin(15))
chars = ["A", "B", "C"]
codes = [".-", "-...", "-.-."]
message = "CAB"

while True:
    for letter in message:
        # 1. Logic Lookup
        if letter in chars:
            idx = chars.index(letter)
            code = codes[idx]
            print("Speaking:", letter, "->", code)

            # 2. Pulse Translation
            for symbol in code:
                buzz.freq(1000)
                buzz.duty_u16(32768) # 50%
                if symbol == ".":
                    time.sleep(0.1)
                else:
                    time.sleep(0.3)
                buzz.duty_u16(0)
                time.sleep(0.1) # Symbol gap

            time.sleep(0.3) # Letter gap

    time.sleep(2.0) # Word gap
```

### 11. Common Mistakes
*   **Index Errors**: Trying to find a letter that isn't in your `chars` list. The code will crash unless you add an `if letter in chars` check.
*   **Gap Missing**: Not putting a `time.sleep` after the Dash/Dot. The sounds will blend together into one long beep.
*   **Dictionary Limits**: To keep the Blocky view clean, we only used A, B, and C. In Python, you should use a proper `morse_dict = {'A': '.-'}` for efficiency.

### 12. Try This Next
*   **Full Alphabet**: Complete the `chars` and `codes` lists with all 26 letters.
*   **User Input**: Use the `input` block to allow the user to type the message into the serial console.
*   **Visual Mirror**: Flash an LED simultaneously with the Buzzer pulses for a multi-sensory output.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Lists, Text, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log. Finalized Batch 9.
- Date Verified: 2026-01-13
---
---
