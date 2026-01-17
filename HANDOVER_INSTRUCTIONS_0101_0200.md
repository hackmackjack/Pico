# Handover Instructions: Projects 0101-0200 (Batches 11-20)

**To:** Incoming Audit Agent
**From:** Jules AI (Lead Auditor, Batches 1-10)
**Date:** 2026-05-20
**Status:** Batches 1-10 (0001-0100) Complete. Handing over for Batches 11-20 (0101-0200).

---

## 1. Mission Objectives
You are tasked with auditing, fixing, and validating **Projects 0101 through 0200**.
Target File: `Documentation/Docs_0101_0200.md`
Reference File: `Reference_Bible_Standards/PICO_2500_TITLES.md`

## 2. Golden Standard v4.0 (Strict Compliance)
Every project must meet these criteria before validation.

### A. Title Authority
*   **Source:** `PICO_2500_TITLES.md`.
*   **Format:** `## Project XXXX: [Title]`
*   **Action:** If `Docs` file has "1. Project 0101" or mismatched text, **overwrite** it with the Canonical Title.

### B. Section 6: Blocks Used
*   **Format:** `* **from [Category], drag `[block_name]`** (optional desc)`
*   **Critical:** "from" must be **lowercase**. Block name must be in **backticks**.
*   *Bad:* `* From Smart IO, drag pico_led`
*   *Good:* `* **from Smart IO, drag `pico_led`**`

### C. Section 8: Step-by-Step Guide
*   **Formatting:** Watch out for "Clumping" where headers merge with text.
    *   *Bad:* `...end of step. B. Main Loop Phase`
    *   *Good:* Ensure `B. Main Loop Phase` is on a new line with a blank line before it.
*   **Detail Level:** Instructions must be explicit.
    *   *Bad:* "Turn on the LED."
    *   *Good:* "From **Smart IO**, drag **`pico_gpio_write`**. Set Pin to **15** and State to **HIGH (1)**."

### D. Section 10: Generated Code
*   **Explicit Logic:** Never use implicit boolean checks.
    *   *Bad:* `if btn.value():`
    *   *Good:* `if btn.value() == 1:`
    *   *Bad:* `while not btn.value():`
    *   *Good:* `while btn.value() == 0:`
*   **Traceability:** Variable names in Code **must** match names in Section 7.

---

## 3. Toolkit (Re-Create These Tools)
I have cleaned the environment. You should re-create these Python scripts to automate your audit.

### Tool 1: `verify_compliance.py`
Use this to scan `Docs_0101_0200.md` for common errors before and after fixes.

```python
import re

def verify_compliance():
    filepath = "Documentation/Docs_0101_0200.md"
    try:
        with open(filepath, 'r') as f: content = f.read()
    except FileNotFoundError: return

    for i in range(101, 201):
        pid = f"{i:04d}"
        if f"## Project {pid}" not in content:
            print(f"[{pid}] Missing Header")

        # Check S6 Formatting
        p_start = content.find(f"## Project {pid}")
        next_p = content.find(f"## Project {i+1:04d}", p_start)
        block = content[p_start:next_p] if next_p != -1 else content[p_start:]

        if "* From" in block or "*   From" in block:
            print(f"[{pid}] S6 Formatting Error ('From' detected)")

        if "if btn.value():" in block:
            print(f"[{pid}] Implicit Boolean Error")

if __name__ == "__main__":
    verify_compliance()
```

### Tool 2: `fix_formatting.py`
Use this to fix the "From" casing and common clumping issues.

```python
import re

def fix_formatting():
    filepath = "Documentation/Docs_0101_0200.md"
    with open(filepath, 'r') as f: content = f.read()

    # Fix S6 'From'
    # Pattern: *   From **Cat**, drag **`Block`**
    # Target: * **from Cat, drag `Block`**

    # 1. Lowercase From
    content = content.replace("*   From", "* **from")
    content = content.replace("* From", "* **from")

    # 2. Fix Bold/Space around Category
    # This regex is complex, refer to previous 'bulk_fix_s6' logic if needed.
    # Simple search/replace is safer for bulk:
    content = re.sub(r"\* \*\*from \*\*(.*?)\*\*, drag \*\*`?(.*?)`?\*\*", r"* **from \1, drag `\2`**", content)

    # Fix S8 Clumping
    content = re.sub(r"([^\n])\s+(B\. Main Loop Phase)", r"\1\n\n\2", content)
    content = re.sub(r"([^\n])\s+(\d+\.\s+\*\*)", r"\1\n\2", content)

    with open(filepath, 'w') as f: f.write(content)
    print("Formatting Fixed.")

if __name__ == "__main__":
    fix_formatting()
```

---

## 4. Execution Workflow

1.  **Scan:** Run `verify_compliance.py` to assess the state of Batches 11-20.
2.  **Fix:** Run `fix_formatting.py` to clear low-hanging fruit.
3.  **Deep Audit:** Manually review `Docs_0101_0200.md` for logical discrepancies (e.g., Code says Pin 15, Wiring says Pin 14).
4.  **Validate:** Generate individual reports in `Validation_Reports/`.
    *   Template: `PROJECT_XXXX_VALIDATION_REPORT.md`
    *   Must list S1-S12 status explicitly.
5.  **Submit:** Commit fixes and reports.

**Good luck.**
