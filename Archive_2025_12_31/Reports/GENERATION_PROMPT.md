# Elite Documentation Generation Prompt

## Mission
Generate documentation for Raspberry Pi Pico projects that strictly adheres to **Elite Documentation Standard v2.0** with zero drift from Problem Statements.

---

## 📋 Input Requirements

You will receive:
1. **Problem Statement** (from `Projects_0501_0600.md`)
2. **Reference Standard** (from `Docs_0001_0100.md` - Project 0001)
3. **Project Number** (e.g., 0501)

---

## 🎯 Output Requirements

Generate **exactly 12 sections** in this order:

### **Section 1: Project Title**
Format: `## 1. Project XXXX: [Name from Problem Statement]`

---

### **Section 2: Learning Objective**
**Rules**:
- Single sentence capturing the **exact task** from Problem Statement
- Include specific details (timing, colors, sequences)
- Action-oriented (starts with verb: Create, Build, Display, Control)
- NOT generic (❌ "Learn about LEDs")

**Template**:
```
Create [specific output] using [specific technique] ([specific parameters]).
```

**Example**:
- **Problem**: "Flash White (R+G+B) for 0.05s, Off for 0.1s"
- **Valid**: "Create an RGB strobe effect with precise timing control (flash ON for 50ms, OFF for 100ms)."

---

### **Section 3: Concepts Introduced**
**Rules**:
- List **only** concepts actually used in this project
- 3-5 bullet points maximum
- Each concept must appear in Section 8 or 10
- Format: `*   **Concept Name**: Brief description`

---

### **Section 6: Blocks Used**
**Rules**:
- MANDATORY format: `**from [Category], drag `block_name`**`
- Categories: "Smart IO", "Loops", "Time", "Logic", "Math", "Display", "Functions"

**Valid**:
```markdown
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
```

---

### **Section 8: Step-by-Step Guide**
**CRITICAL**: Must have phase headers:
1. **A. Initialization Phase**
2. **B. Main Loop Phase**
3. **C. Event/Condition Handling** (if sensors/buttons used)

**Template**:
```markdown
**A. Initialization Phase**
1.  **Configure Output**:
    *   From **Smart IO**, **Set** `pico_gpio_write` Pin GP16, GP17, GP18.

**B. Main Loop Phase**
2.  **Create Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Turn ON**:
    *   From **Smart IO**, drag `pico_gpio_write`.
        *   **Snap** into loop.
        *   Set R=HIGH, G=HIGH, B=HIGH.
```

---

## 🚨 CRITICAL RULES

1. **No Drift**: Only what Problem Statement specifies
2. **Exact Behavior**: Timing/colors/logic must match spec
3. **Structural Compliance**: 12 sections, A/B phases mandatory
4. **Traceability**: Concepts → Steps → Code (all connected)

---

## ✅ Quality Checklist

- [ ] All 12 sections in order
- [ ] Section 8 has A/B headers
- [ ] Section 6 uses "from X, drag Y"
- [ ] Code matches Problem Statement exactly
