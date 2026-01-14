# 📘 Pico Documentation Standard
**Version:** v1.2.1
**Status:** LOCKED  
**Applies to:** Pico Projects 0001–9999

---

## 0️⃣ Definitions
*   **Project**: A single Pico-based learning artifact with a unique 4-digit ID.
*   **Interactive Component**: Any part read from or written to via GPIO (LEDs, Buttons, Sensors).
*   **Algorithm Style**: Step descriptions independent of syntax (Logic first).
*   **Audit Pass**: A project that meets all Mandatory Cross-Checks and Semantic Validations.
*   **Golden Project**: The reference implementation (`PICO_GOLDEN_PROJECT.md`) that serves as the visual and structural dispute resolver.

---

## Rule Zero (Non-Negotiable)
Every section must be derived from, consistent with, and traceable back to the **Problem Statement**.  
**Presence alone is meaningless. Correctness and alignment decide Audit Pass.**

❗ **No Duplication Rule:** No information may be defined in more than one section. If duplicated, one is wrong by definition. (e.g., Pin numbers defined in Wiring, referenced in Code).

---

## 🧭 Canonical Authority Order (MANDATORY)
When validating content, authority flows strictly in this order:

1.  **Problem Statement** (Questions + Expected Behavior) 👑
2.  **Learning Objective** (Intent)
3.  **Concepts Introduced** (Knowledge)
4.  **Hardware Required** (Physical Scope)
5.  **Wiring / Interfaces** (Electrical Truth)
6.  **Step-by-Step Guide** (Canonical Algorithm) 🧠
7.  **Blocks Used** (Capabilities)
8.  **Variables** (State)
9.  **Generated Code** (Implementation)
10. **Execution Flow** (Outcome)
11. **Common Mistakes** (Context)
12. **Try This Next** (Extension)

If a lower section contradicts a higher one → **FAIL**.

---

## 🔍 Section-by-Section Semantic Validation Rules

### 1️⃣ Project Title — Problem Alignment
**Format:** `## 1️⃣ Project [ID]: [Title]`
*   **Derived From:** Project ID & Title in `problem_Statements`.
*   **Semantic Rules:**
    *   Title must describe what the problem asks, not how it’s implemented.
    *   **FAIL Conditions:** Extra features not in problem, Mismatched intent.

### 2️⃣ Learning Objective — Intent Validation
**Format:** `### 2️⃣ Learning Objective`
*   **Derived From:** Problem Statement questions.
*   **Semantic Rules:**
    *   Must answer: *What should the learner understand?*
    *   Must abstract learning, not repeat "Expected Behavior".
    *   **FAIL Conditions:** New goals absent in problem.

### 3️⃣ Concepts Introduced — Knowledge Coverage
**Format:** `### 3️⃣ Concepts Introduced`
*   **Derived From:** Problem Statement + Learning Objective.
*   **Semantic Rules:**
    *   Every core idea implied in the problem must appear here.
    *   Must include ≥1 Hardware concept AND ≥1 Coding concept.
    *   **FAIL Conditions:** Missing implied concept, Extra unrelated concept.

### 4️⃣ Hardware Required — Physical Scope Lock
**Format:** `### 4️⃣ Hardware Required`
*   **Derived From:** Problem Statement + Code + Wiring.
*   **Semantic Rules:**
    *   **Lock Rule:** No component may appear in Wiring/Code unless listed here.
    *   Must not add hardware not asked for in the problem.
    *   **FAIL Conditions:** Orphan hardware (listed but unused), Missing hardware (used but unlisted).

### 5️⃣ Wiring / Interfaces — Electrical Truth
**Format:** `### 5️⃣ Wiring / Interfaces`
*   **Derived From:** Hardware Required + Code.
*   **Semantic Rules:**
    *   Every interactive component (LED, Button, etc.) must have a pin mapping.
    *   Every pin used in Code must appear here.
    *   **FAIL Conditions:** Pin in Code but not Wiring, Component wired but unused.

### 6️⃣ Blocks Used — Capability Declaration
**Format:** `### 6️⃣ Blocks Used`
*   **Derived From:** Step-by-Step Guide.
*   **Semantic Rules:**
    *   Every block must be necessary for at least one Step.
    *   Blocks must represent functionality (e.g., `Loop`, `Wait`), not UI labels.
    *   **FAIL Conditions:** Block without a step, Step without a block.

### 7️⃣ Variables — State Consistency
**Format:** `### 7️⃣ Variables`
*   **Derived From:** Code (Reference).
*   **Semantic Rules:**
    *   Every variable in Code must be listed.
    *   No variable may be listed unless used.
    *   **FAIL Conditions:** Ghost variable (listed not used), Unlisted variable (used not listed).

### 8️⃣ Step-by-Step Guide — Canonical Algorithm (CRITICAL)
**Format:** `### 8️⃣ Step-by-Step Guide`
*   **Derived From:** Problem Statement (Expected Behavior).
*   **Semantic Rules:**
    *   **Single Source of Logic Truth.**
    *   **Style Rule (MANDATORY):** Instructions must be explicit and visual.
        *   ❌ **Bad:** "Initialize loop."
        *   ✅ **Good:** "From **Loops**, drag a **Repeat Forever** block. Snap it below Setup."
    *   **Format:** "From **[Category]**, drag **[Block]**. Snap to [Location]."
    *   **FAIL Conditions:** Abstract logic without block sources, Missing "Snap" locations, Code-pasting.

### 9️⃣ Execution Flow — Outcome Explanation
**Format:** `### 9️⃣ Execution Flow`
*   **Derived From:** Step-by-Step Guide.
*   **Semantic Rules:**
    *   Must explain *what* happens, not *how* it's coded.
    *   Must fully explain all Expected Behaviors.
    *   **FAIL Conditions:** Behavior unexplained.

### 10️⃣ Generated Code (Reference Implementation)
**Format:** `### 10️⃣ Generated Code`
*   **Derived From:** Step-by-Step Guide + Blocks Used.
*   **Semantic Rules:**
    *   Code exists to **verify logic**, not to introduce new logic.
    *   Every logical code block must map to a Step.
    *   Pins/Variables must match Sections 5 & 7.
    *   **FAIL Conditions:** Orphan code, Step not implemented, New logic not in steps.

### 11️⃣ Common Mistakes — Contextual Relevance
**Format:** `### 11️⃣ Common Mistakes`
*   **Derived From:** Actual project logic & hardware context.
*   **Semantic Rules:**
    *   Must relate to: Hardware wiring OR Logic OR Execution behavior.
    *   **FAIL Conditions:** Generic/Copy-pasted tips.

### 12️⃣ Try This Next — Logical Extensions
**Format:** `### 12️⃣ Try This Next`
*   **Derived From:** Existing project scope.
*   **Semantic Rules:**
    *   Must extend current logic, not replace it.
    *   Must be buildable from current project foundation.
    *   **FAIL Conditions:** Concept jump (too hard), Unrelated idea.

---

## 🔁 Mandatory Cross-Section Match Rules (NON-OPTIONAL)
If any one of these links breaks, the project **FAILS**.

| Group | Must Match |
| :--- | :--- |
| **Hardware Required ↔ Wiring ↔ Code** | Components & pins |
| **Step-by-Step Guide ↔ Blocks Used** | Logic & capability |
| **Step-by-Step Guide ↔ Code** | Full algorithm |
| **Problem Statement ↔ Execution Flow** | Behavior & Outcome |
| **Variables ↔ Code** | State names & usage |

---

## 🛑 Final Audit Rule
A project is marked **COMPLETE** only if:
1.  Every section is **derived from the Problem Statement**.
2.  Every step is logically necessary and implemented.
3.  Blocks, Steps, Code, Wiring, and Hardware form a **closed loop**.
4.  No orphan content (unused pins, ghost variables, dead code) exists anywhere.

If something exists but cannot be traced — it is **WRONG**.

---

### ✅ Audit Metadata Template (Mandatory Footer)
(Must be present at the end of every project file)
```markdown
---
## ✅ Audit Metadata
- Standard Version: v1.2.1
- Audit Result: PASS / FAIL
- Failed Sections (if any): —
- Reviewer: Tarcin
- Date: [YYYY-MM-DD]
---
```
