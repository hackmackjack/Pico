# 📘 Pico Documentation Standard (Single Source of Truth)

This document defines the strict quality and validation standards for all 12 sections of the Pico Project Documentation. Every project MUST adhere to these rules to be considered "Audit Pass".

---

## 1️⃣ Project Title
**Format:** `## 1️⃣ Project [ID]: [Title]`
*   **ID Format:** Must be 4 digits (e.g., `0001`, `0250`, `1099`).
*   **Validation Rule:** The ID and Title MUST match the entry in the corresponding `problem_Statements/Projects_XXXX_YYYY.md` file exactly.

## 2️⃣ Learning Objective
**Format:** `### 2️⃣ Learning Objective`
*   **Content:** A single, clear sentence starting with an action verb (e.g., "Build", "Create", "Program").
*   **Validation Rule:** Must describe the *pedagogical goal*, not just the hardware function. (e.g., "Understand H-Bridge logic" vs "Spin a motor").

## 3️⃣ Concepts Introduced
**Format:** `### 3️⃣ Concepts Introduced`
*   **Content:** A bulleted list of 3-5 distinct concepts.
*   **Validation Rule:**
    *   Must include at least one Hardware concept.
    *   Must include at least one Coding concept (e.g., Loops, Variables).
    *   No empty bullets.

## 4️⃣ Hardware Required
**Format:** `### 4 Hardware Required`
*   **Content:** A bulleted list of all physical components.
*   **Validation Rule:**
    *   Must match the components used in the **Wiring** and **Code** sections.
    *   Must include "Raspberry Pi Pico".
    *   Must specify quantities if >1 (e.g., "3x LEDs").

## 5️⃣ Wiring / Interfaces
**Format:** `### 5 Wiring / Interfaces`
*   **Content:** A Markdown Table.
*   **Table Header:** `| Component | Pico Pin |`
*   **Validation Rule:**
    *   Every interactive component (LED, Button, Sensor) in the Code MUST have a pin assignment here.
    *   StandardPins: LEDs (GP15, GP14...), Buttons (GP16, GP17...), I2C (GP0/GP1 or GP4/GP5).

## 6️⃣ Blocks Used
**Format:** `### 6 Blocks Used`
*   **Content:** A list of Blockly blocks corresponding to the code.
*   **Validation Rule:**
    *   Must mention specific functional blocks (e.g., `Pin(OUT)`, `time.sleep`).
    *   Do not list generic Python syntax like "Whitespace".

## 7️⃣ Variables
**Format:** `### 7️⃣ Variables`
*   **Content:** A list of key variables used in the script.
*   **Validation Rule:**
    *   Must list variable names exactly as they appear in the code (e.g., `count`, `p1_score`).
    *   Brief description of what each variable stores.

## 8️⃣ Step-by-Step Guide
**Format:** `### 8️⃣ Step-by-Step Guide`
*   **Content:** Numbered list of logical steps.
*   **Validation Rule:**
    *   **Style Rule:** Instructions must use explicit "From **[Category]**, drag **[Block]**" format.
    *   Must cover the entire flow from Initialization to Main Loop.

## 9️⃣ Execution Flow
**Format:** `### 9️⃣ Execution Flow`
*   **Content:** High-level lifecycle summary.
*   **Validation Rule:**
    *   Standard Phases: **Start** -> **Input/Check** -> **Process/Logic** -> **Output/Act** -> **Loop/End**.

## 10️⃣ Generated Code
**Format:** `### 10️⃣ Generated Code`
*   **Content:** A single executable Python code block (` ```python ... ``` `).
*   **Validation Rule:**
    *   **Syntax:** Must be valid MicroPython.
    *   **Completeness:** Must import all necessary libraries (`machine`, `time`, etc.).
    *   **Pin Matching:** Pin numbers in code MUST match Section 5 (Wiring).
    *   **Comments:** Vital sections should be commented.

## 11️⃣ Common Mistakes
**Format:** `### 11️⃣ Common Mistakes`
*   **Content:** Bulleted list of prospective errors.
*   **Validation Rule:**
    *   Must include at least 2 common pitfalls related to the specific hardware or logic of *this* project (e.g., "Forgetting current limiting resistor" or "Infinite loop blocking").

## 12️⃣ Try This Next
**Format:** `### 12 Try This Next`
*   **Content:** Suggestions for extension.
*   **Validation Rule:**
    *   Must offer 2 distinct ideas for expanding the project (e.g., "Add a second button" or "Change the speed").

---

# 🛑 Mandatory Cross-Checks
Before marking a file as "COMPLETE":
1.  **Code-Wiring Alignment:** Does `lead = Pin(15)` in code match `| LED | GP15 |` in Wiring?
2.  **Hardware Consistency:** Does the Problem Statement ask for a Button, but the Hardware section lists a Potentiometer? (FAIL).
3.  **Title Verification:** Does the Project Title match the ID number in the directory?
