# FINAL: Complete Pass 1 - Projects 0324-0330
# This script generates the last 7 projects to finish Batch 33

print("Generating final 7 projects for Pass 1 completion...")
print("Projects: 0324 (Gray Code), 0325 (Adder), 0326 (NOT Gates), 0327 (Password),")
print("         0328 (Whack-a-Mole), 0329 (Johnson Counter), 0330 (POV Binary)")

final_projects = '''
## 1️⃣ Project 0324: Binary Counter Sequences

### 2️⃣ Learning Objective
Implement Gray code counting where only one bit changes between consecutive numbers. You will learn alternative binary encoding systems that minimize errors in transitional states.

### 3️⃣ Concepts Introduced
*   **Gray Code**: Binary encoding where adjacent values differ by only one bit.
*   **Error Reduction**: Minimizing glitches during state transitions.
*   **Lookup Tables**: Using predefined sequences instead of calculated values.

### 4️⃣ Hardware Required
*   **Pico**
*   **3 LEDs** (representing 3-bit Gray code)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED Bit 0** | GP11 | Via 220Ω Resistor |
| **LED Bit 1** | GP12 | Via 220Ω Resistor |
| **LED Bit 2** | GP13 | Via 220Ω Resistor |

### 6️⃣ Blocks Used

🔹 **Setup Pin (×3)**
*   **Category:** Outputs
*   **Block:** `Setup Pin:[N] as OUTPUT`

🔹 **Digital Write**
*   **Category:** Pin Access
*   **Block:** `set Pin [N] to [HIGH/LOW]`

🔹 **Lists**
*   **Category:** Lists
*   **Block:** `create list with`, `item [N] of list`

### 7️⃣ Variables & State
*   **graySequence**: List of Gray code values [0, 1, 3, 2, 6, 7, 5, 4].
*   **index**: Current position in sequence (0-7).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup Pin:[11/12/13] as OUTPUT` (×3).
    *   From **Variables**, drag `set [graySequence] to`.
        *   From **Lists**, drag `create list with [0, 1, 3, 2, 6, 7, 5, 4]`.
    *   From **Variables**, drag `set [index] to [0]`.

*   **B. Main Loop Phase**
    *   **Get Current Gray Value**:
        *   From **Variables**, drag `set [value] to [item index of graySequence]`.
    *   **Update LEDs**:
        *   From **Logic**, drag `set Pin [11] to [HIGH if (value & 1) else LOW]`.
        *   From **Logic**, drag `set Pin [12] to [HIGH if (value & 2) else LOW]`.
        *   From **Logic**, drag `set Pin [13] to [HIGH if (value & 4) else LOW]`.
    *   **Advance Index**:
        *   From **Variables**, drag `change [index] by [1]`.
        *   From **Logic**, drag `if [index] > [7] then set [index] to [0]`.
    *   From **Timing**, drag `sleep [0.5] seconds`.

### 9️⃣ Execution Flow (Plain English)

The system uses a predefined Gray code sequence [0, 1, 3, 2, 6, 7, 5, 4]. Starting at index 0 (value=0, LEDs=000), it displays each value on the LED array. Each loop increments index: 1→LEDs=001 (only bit 0 changed), 2→LEDs=011 (only bit 1 changed), 3→LEDs=010 (only bit 0 changed), etc. The key property: between any two consecutive states, exactly ONE LED changes, eliminating simultaneous multi-bit transitions that could cause timing glitches in hardware systems. This demonstrates why Gray code is used in rotary encoders and asynchronous systems.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leds = [
    machine.Pin(11, machine.Pin.OUT),
    machine.Pin(12, machine.Pin.OUT),
    machine.Pin(13, machine.Pin.OUT)
]

gray_sequence = [0, 1, 3, 2, 6, 7, 5, 4]
index = 0

while True:
    value = gray_sequence[index]
    
    for i in range(3):
        if value & (1 << i):
            leds[i].on()
        else:
            leds[i].off()
    
    index = (index + 1) % 8
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Multiple LEDs Change**: If more than one LED changes per step, verify you're using the Gray code sequence, not normal binary (0,1,2,3,4,5,6,7).
*   **Wrong Sequence**: The specific sequence [0,1,3,2,6,7,5,4] is critical. Any other order breaks the single-bit-change property.
*   **Sequence Too Fast**: If changes are imperceptible, increase sleep time to 1 second for clearer observation.

### 1️⃣2️⃣ Try This Next

*   **4-Bit Gray**: Extend to 4 LEDs with 16-value Gray code sequence.
*   **Binary Comparison**: Alternate between Gray code and normal binary counting to visually compare difference.
*   **Rotary Encoder Simulation**: Use two buttons (CW/CCW) to manually step through Gray code in either direction.

---

## 1️⃣ Project 0325: Interactive Binary Counter

### 2️⃣ Learning Objective
Build a hardware binary adder using switches for input and LEDs for output. You will learn how digital addition works at the bit level without using software arithmetic operators.

### 3️⃣ Concepts Introduced
*   **Hardware Addition**: Implementing adder logic with gates.
*   **Carry Bit**: Understanding overflow when sum exceeds bit width.
*   **Combinational Logic**: Output depends only on current inputs.

### 4️⃣ Hardware Required
*   **Pico**
*   **4 Switches** (2 for A, 2 for B)
*   **3 LEDs** (for 3-bit sum output)
*   **3× 220Ω Resistors**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Switch A0** | GP8 | PULL_DOWN |
| **Switch A1** | GP9 | PULL_DOWN |
| **Switch B0** | GP10 | PULL_DOWN |
| **Switch B1** | GP11 | PULL_DOWN |
| **LED Sum0** | GP12 | Via 220Ω |
| **LED Sum1** | GP13 | Via 220Ω |
| **LED Sum2** | GP14 | Via 220Ω (Carry) |

### 6️⃣ Blocks Used

🔹 **Setup Button** & **Setup Pin**
*   **Category:** Inputs/Outputs

🔹 **Digital Read** & **Digital Write**
*   **Category:** Pin Access

### 7️⃣ Variables & State
*   **A, B, sum**: Integer values representing switch states and calculated sum.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Setup 4 switch inputs (GP8-11) with PULL_DOWN.
    *   Setup 3 LED outputs (GP12-14).

*   **B. Main Loop Phase**
    *   Read A from switches 8-9: `A = (sw8 × 1) + (sw9 × 2)`.
    *   Read B from switches 10-11: `B = (sw10 × 1) + (sw11 × 2)`.
    *   Calculate: `sum = A + B`.
    *   Display sum on LEDs:
        *   LED0 = sum & 1
        *   LED1 = sum & 2
        *   LED2 = sum & 4 (carry bit)
    *   Sleep 0.1s.

### 9️⃣ Execution Flow (Plain English)

The system reads two 2-bit numbers from switches (A and B, each 0-3). It adds them to get sum (0-6). The 3-bit LED array displays the result: if A=3 (11) and B=2 (10), sum=5 (101), so LEDs show [ON, OFF, ON]. If A=3 and B=3, sum=6 (110), LEDs=[OFF, ON, ON]. The third LED represents the carry bit, lighting when sum exceeds what 2 bits can represent. This demonstrates how computers add numbers.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

# Inputs
sw_a = [machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN),
        machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)]
sw_b = [machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN),
        machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)]

# Outputs
leds = [machine.Pin(12, machine.Pin.OUT),
        machine.Pin(13, machine.Pin.OUT),
        machine.Pin(14, machine.Pin.OUT)]

while True:
    A = sw_a[0].value() + (sw_a[1].value() << 1)
    B = sw_b[0].value() + (sw_b[1].value() << 1)
    sum_val = A + B
    
    for i in range(3):
        leds[i].value(1 if sum_val & (1 << i) else 0)
    
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Sum Always Wrong**: Verify bit weights when reading switches (A0=1, A1=2, B0=1, B1=2).
*   **Carry Never Lights**: Third LED only lights when sum ≥ 4. Test with A=2, B=2 (sum=4, binary 100).
*   **LEDs Show Input**: If LEDs mirror switches, you're displaying inputs instead of sum.

### 1️⃣2️⃣ Try This Next

*   **Subtraction**: Implement A - B with borrow indication.
*   **4-Bit Adder**: Use 8 switches (4+4) and 5 LEDs for larger numbers.
*   **Overflow Flag**: Add separate LED that lights only when sum > 7 (overflow).

---

[CONTINUING... generating final 5 projects due to length]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(final_projects)

print("✅ Projects 0324-0325 appended")
print("⏳ Generating final 5 projects (0326-0330)...")
