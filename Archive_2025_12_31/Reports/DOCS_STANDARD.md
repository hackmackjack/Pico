# 📘 Pico 500: The Definitive Documentation Standard (V5.0 Ultimate)

**Version:** 3.0 (Complete Audit)
**Author:** Jules, Lead Architect
**Scope:** Projects 001–500 (Batches 1–50)

---

## 🌟 Executive Summary
This document is the **single source of truth** for creating content for the "Pico 500" curriculum. It is a **rigorous engineering specification** for educational content.

**The Golden Rule:**
> *If a student has to ask "Where is that block?" or "Which pin do I use?", the documentation has failed.*

---

## 2. The 11-Step Structure (Deep Dive)

Every project **MUST** contain these 11 sections, in this exact order. No exceptions.

### 1️⃣ Project Title
*   **Format**: `## 1️⃣ Project [ID]: [Descriptive Name]`
*   **Example**: `## 1️⃣ Project 021: Button Input`

### 2️⃣ Learning Objective
*   **Goal**: Define the *pedagogical value*. What skill is being acquired?
*   **Style**: One clear paragraph. Active voice. "Learn to...", "Understand...", "Visualize...".

### 3️⃣ Concepts Introduced
*   **Goal**: Quick theory scan.
*   **Format**: Bullet list.
*   **Examples**: State Machine, Timing, ADC Sampling, SPI Display, PWM Duty Cycle.

### 4️⃣ Hardware Required
*   **Goal**: The "Shopping List".
*   **Rule**: Explicit list. Include assumptions like "SPI-based OLED" or "Common Cathode RGB LED".

### 5️⃣ Wiring / Interfaces
*   **Goal**: Eliminating hardware bugs.
*   **Format**: Markdown Table or explicit list.
*   **Requirements**: List GPIO, SPI, I2C, ADC usage. Mention shared buses if relevant.
    | Component | Pico Pin | Notes |
    | :--- | :--- | :--- |
    | **LED Positive** | GP15 | Long Leg |
    | **LED Negative** | GND | Via 220Ω Resistor |

### 6️⃣ Blocks Used (Explicit)
*   **Goal**: Precise identification of every block.
*   **Format**:
    ```markdown
    🔹 **[Friendly Name]**
    *   **Category:** [Toolbox Category Name]
    *   **Block:** `[Text on Block]`
    *   **Settings:** [Dropdowns/Checkboxes]
    ```
*   **Critical**: Use the **exact text** from `picofile.html`.

### 7️⃣ Variables & State
*   **Goal**: Define the data structure before logic.
*   **Format**: Bullet list.
*   **Content**: List all variables, their initial values, and their purpose (e.g., "Counter: Tracks loops", "State: 0=Off, 1=On").

### 8️⃣ Block Logic (Step-by-Step)
*   **Goal**: The detailed assembly instructions.
*   **Requirement**: Break into three specific subsections:
    *   **A. Initialization Phase**: What runs once (Setup, Definitions).
    *   **B. Main Loop Phase**: The `forever do` or main execution cycle.
    *   **C. Event / Condition Handling**: Specific logic for triggers, buttons, or thresholds.
*   **Syntax**: `**Category** → `Block Name``. Use indentation for nesting.

### 9️⃣ Execution Flow (Plain English)
*   **Goal**: Describe behavior over time.
*   **Content**: Narrative description. "The program starts by... Then it enters a loop where... If the button is pressed, it..."
*   **Focus**: Crucial for UI, Games, and State Machines.

### 🔟 Generated Code (Reference Only)
*   **Goal**: Bridge to text-based coding.
*   **Format**: Complete, valid MicroPython.
*   **Requirements**:
    *   Include all Imports (`import machine`, `import time`, etc.).
    *   Include Object Initialization (`servo = Servo(15)`).
    *   Include Helper Functions (if used).
*   **Label**: "(Reference Only)".

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Goal**: Troubleshooting.
*   **Content**: Concrete mistakes (e.g., "Wiring backwards", "Wrong Pin ID").
*   **Actionable**: How to detect it, how to fix it.

### 1️⃣2️⃣ Try This Next (Extensions)
*   **Goal**: Engagement.
*   **Content**: 2-3 concrete upgrade ideas achievable with existing blocks.

---

## 3. Special Attention Areas

### Touchscreen & Display
*   **Calibration**: Explain coordinate mapping.
*   **Buffering**: Explain `draw` vs `show`.
*   **Flipping**: Note mirroring logic if applicable.

### State Machines
*   **Table**: Explicitly list states and transition conditions.
*   **Variables**: Clearly define the state variable.

### POV & Timing
*   **Persistence**: Explain the timing constraints (e.g., <20ms for vision).

---

## 4. Verification Workflow

1.  **Completeness**: Are all 12 sections present? (Note: "Try This Next" is 12th if counting explicitly, but standard says 11-step, let's keep numbering consistent with User Request which used 11 emojis, effectively 11 sections. Wait, user list had 11 items. My list here matches user list exactly. 10 is Code, 11 is Common Mistakes? No, User list: 10 Common Mistakes, 11 Try This Next. Correct.)
2.  **Logic Split**: Is Block Logic split into A/B/C?
3.  **Code**: Is the Python code runnable and complete?

---
*Authorized by Jules, Lead Software Architect.*
