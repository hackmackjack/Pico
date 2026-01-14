# Elite Documentation Generation Prompt v2.0

## Mission
Generate documentation for Raspberry Pi Pico projects that strictly adheres to **Elite Documentation Standard v2.0** with zero drift from Problem Statements.

---

## 📋 Input Requirements

You will receive:
1. **Problem Statement** (from `Projects_XXXX_XXXX.md`)
2. **Reference Standard** (from `Docs_0001_0100.md`)
3. **Project Number** (e.g., 0501)

---

## 🎯 Mandatory Output: All 12 Sections

Generate **exactly 12 sections** in this order. All sections are **mandatory**.

---

### **Section 1: Project Title**

**Format**: `## 1. Project XXXX: [Name from Problem Statement]`

**Example**:
```markdown
## 1. Project 0501: Introduction to Digital Art
```

---

### **Section 2: Learning Objective**

**Rules**:
- Single sentence capturing the **exact task** from Problem Statement
- Include specific details (timing, colors, sequences, thresholds)
- Action-oriented (starts with verb: Create, Build, Display, Control, Detect)
- **NOT generic** (❌ "Learn about LEDs")

**Template**:
```
Create [specific output] using [specific technique] ([specific parameters]).
```

**Examples**:

✅ **Valid**:
```markdown
### 2. Learning Objective
Create an RGB strobe effect with precise timing control (flash ON for 50ms, OFF for 100ms).
```

❌ **Invalid**:
```markdown
### 2. Learning Objective
Learn to control RGB LEDs.
```

---

### **Section 3: Concepts Introduced**

**Rules**:
- List **only** concepts actually used in this project
- 3-5 bullet points maximum
- Each concept must appear in Section 8 or 10
- Format: `*   **Concept Name**: Brief description`

**Traceability Rule**: Every concept listed must be used in the project.

**Example**:
```markdown
### 3. Concepts Introduced
*   Strobe Effect (Rapid switching)
*   RGB LED Control (Simultaneous channels)
*   Precise Timing (Milliseconds)
*   Infinite Loops (`while True`)
```

---

### **Section 4: Hardware Required**

**Rules**:
- Bullet list format
- **Always** start with "Raspberry Pi Pico"
- List components from Problem Statement
- Add **realistic necessities** (resistors, jumper wires, breadboard)
- Do not add components not needed for the project

**Template**:
```markdown
### 4. Hardware Required
*   Raspberry Pi Pico
*   [Component from Problem Statement]
*   [Component from Problem Statement]
*   [Realistic additions: resistors, wires, etc.]
```

**Example**:
```markdown
### 4. Hardware Required
*   Raspberry Pi Pico
*   RGB LED
*   3x 220Ω Resistors
*   Jumper Wires
*   Breadboard
```

---

### **Section 5: Wiring / Interfaces**

**Rules** (MANDATORY FORMAT):
- **Markdown table** with exactly **3 columns**
- Column headers: `Component | Pico Pin | Notes`
- **Left-aligned**: `| :--- | :--- | :--- |`
- Pin format: **GP##** (not just `##` or `Pin ##`)
- Component names: **Bold** (e.g., `**Red LED**`)
- Include interface type in Notes (I2C, SPI, Analog, etc.)

**Template**:
```markdown
### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **[Component]** | GP## | [Interface/Connection details] |
```

**Example**:
```markdown
### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Red LED** | GP16 | Connected via 220Ω resistor |
| **Green LED** | GP17 | Connected via 220Ω resistor |
| **Blue LED** | GP18 | Connected via 220Ω resistor |
```

---

### **Section 6: Blocks Used**

**Rules** (MANDATORY FORMAT):
- **Every block** must use format: `**from [Category], drag `block_name`**`
- Optional: Add brief description in parentheses
- Categories must match Blockly toolbox:
  - "Smart IO"
  - "Loops"
  - "Time"
  - "Logic"
  - "Math"
  - "Display"
  - "Functions"
  - "Variables"
  - "Text"

**Valid Examples**:
```markdown
### 6. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)
*   **from Logic, drag `if_else`** (conditional branching)
```

**Invalid** (missing "from X, drag Y"):
```markdown
❌ Use pico_forever block
❌ Set pin to HIGH
❌ `pico_gpio_write` for output
```

---

### **Section 7: Variables**

**Rules** (MANDATORY):
- List **all variables** used in Section 10 (code)
- Format: `*   **variable_name**: Type (purpose)`
- **If no variables**: `*   **None**: [reason why no variables needed]`
- **Traceability Rule**: Every variable in code MUST be listed here

**Example with variables**:
```markdown
### 7. Variables
*   **redState**: Boolean (Tracks Red LED on/off state)
*   **greenState**: Boolean (Tracks Green LED on/off state)
*   **blueState**: Boolean (Tracks Blue LED on/off state)
```

**Example without variables**:
```markdown
### 7. Variables
*   **None**: This project controls output pins directly without state variables.
```

---

### **Section 8: Step-by-Step Guide**

**CRITICAL**: This section has **mandatory phase structure**.

#### **Phase Headers (Required)**:
1. **A. Initialization Phase** (always required)
2. **B. Main Loop Phase** (always required)
3. **C. Event/Condition Handling** (only if project uses sensors/buttons/conditionals)

#### **Step Format Rules**:
- Numbered list starting from 1 for each phase
- Bold action verbs: **Configure**, **Set**, **Check**, **Wait**, **Turn ON**, **Turn OFF**, **Create**, **Read**
- Each step must include:
  - Action description (bolded)
  - Block instruction: "From **[Category]**, drag `block_name`"
  - **Snap** instruction (where to place block)
  - Parameter details (what values to set)
- Use 4-space indentation for sub-steps

**Template**:
```markdown
### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_gpio_write` Pin GP16, GP17, GP18.

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Turn ON (White Flash)**:
    *   From **Smart IO**, drag `pico_gpio_write` blocks.
        *   **Snap** into loop.
        *   Set R=HIGH, G=HIGH, B=HIGH.
4.  **Wait**:
    *   From **Time**, drag `pico_wait`.
        *   **Snap** below.
        *   Set 0.05 seconds.
```

**Invalid** (vague, no block instructions):
```markdown
❌ 1. Set up the LED
❌ 2. Make it blink
❌ 3. Configure the pins
```

---

### **Section 9: Execution Flow**

**CRITICAL**: This is the **primary teaching artifact** - more important than code.

**Rules**:
- Numbered narrative (1., 2., 3., ...)
- Describe **runtime behavior** step-by-step in plain English
- Use bold keywords: **Start**, **Process**, **Output**, **Repeat**, **Check**, **Delay**, **Sense**, **Decide**
- Must match the logic in Section 10 (code) **exactly**
- Explain the "why" and "what happens", not just "what the code does"

**Template**:
```markdown
### 9. Execution Flow
1.  **Start**: The Pico powers up and [initialization description].
2.  **Process**: The code enters the main loop.
3.  **Output**: [What happens - user-visible behavior].
4.  **Delay**: The system waits [duration] ([reason]).
5.  **Repeat**: The process jumps back to Step X.
```

**Example**:
```markdown
### 9. Execution Flow
1.  **Start**: The Pico powers up and configures GP16, GP17, and GP18 as outputs.
2.  **Process**: The code enters the main loop.
3.  **Output**: All three LEDs turn HIGH simultaneously (creating white light).
4.  **Delay**: The system waits for 0.05 seconds (flash duration).
5.  **Output**: All three LEDs turn LOW (darkness).
6.  **Delay**: The system waits for 0.1 seconds (off duration).
7.  **Repeat**: The process jumps back to Step 3 instantly, creating a strobe effect.
```

**Validation**: Flow must trace exactly to code logic. This section teaches **what the learner will observe**.

---

### **Section 10: Generated Code**

**CRITICAL**: Code is **REFERENCE ONLY** - not the primary teaching artifact.

**Philosophy**:
- Code must match **Execution Flow first**, Problem Statement second
- **Teachable > Clever**: No premature abstractions, no over-optimization
- Code should match beginner understanding level
- **No functions** unless Problem Statement requires them (Difficulty 5)
- Comments for clarity, but not excessive

**Rules**:
- Valid MicroPython syntax
- Imports at the top (`from machine import Pin`, `import time`, etc.)
- Pin numbers match Section 5 wiring
- Variable names match Section 7
- Logic matches Problem Statement **exactly**
- Use code fence with `python` language tag

**Template**:
```markdown
### 10. Generated Code
\```python
from machine import Pin
import time

# Initialize [description]
[component] = Pin([pin], Pin.OUT)

while True:
    # [Step description]
    [code]
    time.sleep([duration])
\```
```

**Example (Teachable)**:
```python
from machine import Pin
import time

# Initialize RGB pins
red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)

while True:
    # Turn ON (White)
    red.on()
    green.on()
    blue.on()
    time.sleep(0.05)
    
    # Turn OFF
    red.off()
    green.off()
    blue.off()
    time.sleep(0.1)
```

**Invalid (Over-optimized)**:
```python
❌ Don't do this for beginners:
def set_rgb(r, g, b):
    pins = [Pin(i, Pin.OUT) for i in range(16, 19)]
    for i, val in enumerate([r, g, b]): pins[i].value(val)

while True:
    set_rgb(1, 1, 1); time.sleep(0.05)
    set_rgb(0, 0, 0); time.sleep(0.1)
```

**Validation**:
- Code must compile without errors
- Timing values must match Problem Statement
- Color logic must be correct (Yellow = R+G, Cyan = G+B, Magenta = R+B, White = R+G+B)

---

### **Section 11: Common Mistakes**

**Rules**:
- 2-3 bullet points
- Focus on **realistic student errors** (from teaching experience)
- Format: `*   **Category**: Description of mistake`
- Include consequences or how to fix

**Examples**:
```markdown
### 11. Common Mistakes
*   **Wrong Timing**: Using seconds instead of milliseconds (e.g., `time.sleep(50)` instead of `0.05`).
*   **Photosensitivity**: This project creates flashing lights—avoid if sensitive to strobes.
*   **Missing Resistors**: Connecting LEDs directly to 3.3V can burn them out.
```

---

### **Section 12: Try This Next**

**Rules**:
- 2-3 bullet points
- Suggest **simple extensions** of the current project (not entirely new projects)
- Format: `*   **Extension Name**: Description`
- Extensions should be achievable by modifying existing code

**Examples**:
```markdown
### 12. Try This Next
*   **Colored Strobe**: Change the code to flash only Red or Blue instead of white.
*   **Variable Speed**: Add a potentiometer to control the delay time dynamically.
```

---

## 🚨 CRITICAL VALIDATION RULES

### 1. **No Drift Rule**
- Every element must trace to Problem Statement
- ❌ No added features (e.g., score tracking unless in spec)
- ❌ No extra concepts (e.g., "Binary Logic" in RGB project)
- ❌ No extra variables (e.g., `timer` if not needed)

### 2. **Exact Behavior Rule**
- Timing must match exactly (0.05s in spec = `time.sleep(0.05)`)
- Color combinations must match (Yellow = R+G, NOT R+B)
- Logic must match (toggle vs turn ON, AND vs OR)

### 3. **Structural Compliance Rule**
- All 12 sections required, in exact order
- Section 8 must have A/B/C phase headers
- Section 6 must use "from X, drag Y" format
- Section 5 table must have 3 columns with correct alignment

### 4. **Traceability Rule**
- Section 3 (Concepts) → Used in Section 8 or 10
- Section 7 (Variables) → Appear in Section 10
- Section 9 (Flow) → Matches Section 10 logic exactly

### 5. **Pedagogy Over Code**
- Section 9 (Execution Flow) is more important than Section 10 (Code)
- Code is reference only, not primary teaching artifact
- Teachable code > Clever code

---

## ✅ Pre-Submission Checklist

Before submitting documentation, verify:

**Structure**
- [ ] All 12 sections present in exact order
- [ ] Section 8 has A/B phase headers (C if applicable)
- [ ] Section 5 table has 3 columns with `:---` alignment
- [ ] Section 6 uses "from [Category], drag `block`" format

**Content**
- [ ] Learning Objective captures exact task from Problem Statement
- [ ] All concepts listed are actually used
- [ ] All variables listed appear in code
- [ ] Code produces exact behavior from spec
- [ ] Execution Flow matches code logic

**Accuracy**
- [ ] Pin numbers consistent across Sections 5, 8, 10
- [ ] Timing values match Problem Statement
- [ ] Color combinations correct
- [ ] No features beyond spec

**Traceability**
- [ ] Every concept in Section 3 is used in Section 8 or 10
- [ ] Every variable in Section 7 appears in Section 10
- [ ] Every variable in Section 10 is declared in Section 7
- [ ] Section 9 (Flow) accurately describes Section 10 (Code)

---

## 🎓 Key Principles

1. **Structure is Law**: 12 sections, exact order, A/B/C phases mandatory
2. **Problem Statement = Source of Truth**: Every element traces back
3. **No Hallucinations**: Only what the spec requires
4. **Pedagogy Over Code**: Execution Flow is more important than code
5. **Traceability**: Concepts → Steps → Flow → Code (all connected)
6. **Exact Behavior**: Timing, colors, logic must match spec precisely
7. **Teachable Code**: Simple > Clever for beginner comprehension

---

## 📝 Self-Validation Questions

Before finalizing documentation, ask:

1. ✅ Does Section 2 (Learning Objective) match the Problem Statement task exactly?
2. ✅ Are all 12 sections present in the correct order?
3. ✅ Does Section 8 have A. Initialization and B. Main Loop headers?
4. ✅ Do all block instructions use "from [Category], drag `block`" format?
5. ✅ Are all concepts in Section 3 actually used in the project?
6. ✅ Do all variables in Section 7 appear in Section 10 code?
7. ✅ Does Section 9 (Execution Flow) accurately describe runtime behavior?
8. ✅ Does the code in Section 10 produce the exact behavior from the spec?
9. ✅ Are pin numbers consistent across Sections 5, 8, and 10?
10. ✅ Is the code teachable (not over-optimized for beginners)?

**If any answer is NO → Fix before proceeding.**

---

**Version**: 2.0  
**Date**: 2025-12-31  
**Status**: Production-Ready  
**Compliant With**: Elite Documentation Standard v2.0, Elite Validation Standard v1.0
