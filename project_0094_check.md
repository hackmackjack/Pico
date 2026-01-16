## Project 0094: Modular Morse (Function-Based Signaling)

### 2. Learning Objective
Code reusability and logic abstraction using functions. Build an SOS repeater that uses custom-defined subroutines for "Dot" and "Dash" signals, making the main execution loop cleaner and easier to manage.

### 3. Concepts Introduced
*   **Subroutines (Functions)**: Grouping a sequence of blocks (e.g., Turn ON -> Wait -> Turn OFF -> Wait) under a shared name so they can be triggered with a single "Call" block.
*   **Code Abstraction**: Hiding the timing details of individual signals so the programmer can focus on the "Message" level (e.g., Calling `dot()` three times).

### 4. Hardware Required
*   **Raspberry Pi Pico**
*   **1x LED**
*   **1x 220Ω Resistor**

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP15 | Visual Output |
| **Ground** | GND | Common reference |

### 6. Blocks Used
*   From **Smart IO**, drag **`pico_forever`** (forever do)
*   From **Functions**, drag **`procedures_defnoreturn`** (to [method name] do)
*   From **Functions**, drag **`procedures_callnoreturn`** (call [method name])
*   From **Smart IO**, drag **`pico_gpio_write`** (set Pin to ...)
*   From **Smart IO**, drag **`pico_wait`** (wait)
*   From **Variables**, drag **`set [variable] to`** (variable assignment)
*   From **Logic & Math**, drag **`[X] * [Y]`** (arithmetic)

### 7. Variables
*   **led**: Pin object for GP15.
*   **UNIT**: The base timing duration (0.2s).

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Constants**:
    *   Initialize **led** on **GP15**.
    *   Set **UNIT** to **0.2**.
    *   **Snap** into the **`start`** block.
2.  **Define the `dot` Function**:
    *   From **Functions**, drag a **definition** block and name it **`dot`**.
    *   **Action**: Turn **led** ON -> Wait **UNIT** -> Turn **led** OFF -> Wait **UNIT**.
3.  **Define the `dash` Function**:
    *   From **Functions**, drag a **definition** block and name it **`dash`**.
    *   **Action**: Turn **led** ON -> Wait **UNIT * 3** -> Turn **led** OFF -> Wait **UNIT**.

**B. Messaging Phase**
4.  **Start Loop**:
    *   From **Smart IO**, drag the **`pico_forever`** block.
5.  **Signal "S"**:
    *   Call **`dot`** three times.
    *   Wait **UNIT * 2** (Letter Space).
6.  **Signal "O"**:
    *   Call **`dash`** three times.
    *   Wait **UNIT * 2** (Letter Space).
7.  **Signal "S"**:
    *   Call **`dot`** three times.
8.  **Word Gap**:
    *   Wait **3.0** seconds before repeating.

### 9. Execution Flow
1.  **Initialization**: Define what a "dot" and "dash" are.
2.  **Organization**: The main loop is now very short—it just names the letters (S, O, S).
3.  **Performance**: The Pico reaches into the "definitions" area every time it encounters a call block, executes the instructions, and returns to exactly where it left off.

### 10. Generated Code
```python
from machine import Pin
import time

# Initialization
led = Pin(15, Pin.OUT)
UNIT = 0.2

# Define Subroutines
def dot():
    led.value(1)
    time.sleep(UNIT)
    led.value(0)
    time.sleep(UNIT)

def dash():
    led.value(1)
    time.sleep(UNIT * 3)
    led.value(0)
    time.sleep(UNIT)

while True:
    # SOS Sequence using modular calls
    dot(); dot(); dot()
    time.sleep(UNIT * 2) # Inter-letter space

    dash(); dash(); dash()
    time.sleep(UNIT * 2) # Inter-letter space

    dot(); dot(); dot()

    # Word gap
    time.sleep(3.0)
```

### 11. Common Mistakes
*   **Misplaced Blocks**: Snapping the `dot` and `dash` definitions *inside* the `pico_forever` loop. Definitions should be placed outside (usually to the side) the main flow.
*   **Gap Omission**: Forgetting the letter gap between calling `dot()` and `dash()`. The logic within the function only handles the gap *between* signals in a single character.
*   **Function Name Conflicts**: Giving two functions the same name. Each unique sequence must have a unique identifier.

### 12. Try This Next
*   **Complete Alphabet**: Add `dot` and `dash` combinations to define other letters like `A` (dot, dash) or `B` (dash, dot, dot, dot).
*   **Function Variables**: (Advanced) Try creating a function that takes a number as input to decide how many times to blink.
*   **Audio Subroutine**: Create a `beep()` function that controls both an LED and a Buzzer simultaneously.

---
###  Audit Metadata
- Standard Version: Elite v3.2
- Audit Result: ✅ PASS (after fixes)
- Auditor: Antigravity Elite Auditor v3.2
- Previous Result: ❌ FAIL (S6/S8 category mismatches)
- Date Fixed: 2026-01-13
- Issues Resolved: Fixed block categories to Smart IO, Functions, Loops, refined step-by-step for atomic block actions, updated title format, expanded sections to 3+ items, fixed code box syntax, replaced outdated print blocks with pico_log.
- Date Verified: 2026-01-13
---

### 11. Common Mistakes
*   **Tedious**: Writing out every letter is slow. Project 100 solves this.

### 12. Try This Next
*   **Name**: Spell your own name.
---

## Project 0095: Morse Rhythm Game (Pattern Recognition)
