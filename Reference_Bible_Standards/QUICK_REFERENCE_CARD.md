# 🚀 Elite Auditor v3.0 – Quick Reference Card
**One-Page Guide for Documentation Validation**

---

## 🎯 Validation in 3 Steps

### 1️⃣ PREPARE
```
Load: Problem Statement (source of truth)
Load: Documentation (12 sections)
Load: 12-Step Checklist
```

### 2️⃣ EXECUTE
```
Run: 12-step validation (S1 → S12)
Verify: Cross-section links
Assign: Per-section verdicts
```

### 3️⃣ REPORT
```
Generate: Verdict table
Document: Improvements needed
Assign: Overall verdict
```

---

## 📋 The 12 Sections

| # | Section | Critical? | Key Check |
|:-:|:--------|:---------:|:----------|
| S1 | Project Title | | Matches problem ID & title |
| S2 | Learning Objective | | Action verb, describes learning |
| S3 | Concepts Introduced | | Only used concepts, no extras |
| S4 | Hardware Required | | Exact match with problem |
| S5 | Wiring Table | ⭐ | Table format, Notes column |
| S6 | Blocks Used | | Exact taxonomy, all in S8 |
| S7 | Variables | | 1:1 match with S10 code |
| S8 | Step-by-Step | ⭐⭐⭐ | CRITICAL - detailed, atomic steps |
| S9 | Execution Flow | | Mirrors S8, observable behavior |
| S10 | Code | ⭐⭐⭐ | CRITICAL - solves exact problem |
| S11 | Common Mistakes | | Project-specific, not generic |
| S12 | Extensions | | Builds on current, no new hw |

---

## 🔗 Cross-Section Links (MUST VERIFY)

```
S4 ↔ S5   Hardware ↔ Wiring
S5 ↔ S10  Wiring ↔ Code pins
S6 ↔ S8   Blocks ↔ Steps
S7 ↔ S10  Variables ↔ Code
S8 ↔ S10  Steps ↔ Code logic
S8 ↔ S9   Steps ↔ Flow
Problem ↔ S10  Truth ↔ Code
```

**If ANY link breaks → FAIL**

---

## 📊 Verdict System

### Severity Levels
| Symbol | Meaning | Action |
|:------:|:--------|:-------|
| ✅ | **PASS** | Fully compliant, no changes |
| ⚠️ | **WARN** | Works, but needs clarity |
| ❌ | **FAIL** | Violates Elite Standard |

### Overall Verdict
- All ✅ → **PASS**
- Any ⚠️, no ❌ → **WARN**
- Any ❌ → **FAIL**

---

## 📝 Verdict Table Template

```markdown
| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | OVERALL |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|:-------:|
| ✅ | ✅ | ⚠️ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌  | ✅  | ✅  | ❌ FAIL |
```

---

## ⚠️ Common FAIL Conditions

### S5 (Wiring)
- ❌ Bullet list instead of table
- ❌ Missing "Notes" column
- ❌ Pin in S5 not in S10 code

### S8 (Step-by-Step)
- ❌ Vague steps ("configure sensor")
- ❌ Missing block sources
- ❌ Missing parameter field names

### S10 (Code)
- ❌ Solves different problem
- ❌ Missing imports
- ❌ Pin mismatch with S5
- ❌ Variable mismatch with S7

---

## 🎯 Critical Validation Points

### S8 (Step-by-Step) - HIGHEST RISK
**7-Step Protocol:**
1. **Verify blocks in picofile.html** (search `"type": "block_name"`)
2. **Map problem → blocks** (document line numbers)
3. **Validate block-to-code** alignment
4. **Create missing blocks** if needed! 🚨
5. **Validate detail level** (student can follow without guessing)
6. **Verify execution order** (Init → Loop → Logic)
7. **Cross-reference S10** code

**Required Format:**
```
From **[Category]** category, drag **`block_name`** block.
In the **[Parameter]** field, set to **[value]**.
```

**Block Location Map (picofile.html):**
- Lines 182-280: IO & Basics
- Lines 282-593: Sensors  
- Lines 595-697: Actuators
- Lines 700-748: Robotics
- Lines 751-900: Display
- Lines 901+: Advanced

**IF Block Missing:**
- Document requirement
- Design JSON spec
- Add to picofile.html
- Create Python generator
- **FAIL validation** (block creation needed)

---

### S10 (Code) - HIGHEST IMPACT
**10-Step Protocol:**
1. **Read problem word-by-word** (100% alignment)
2. **Verify blocks in picofile.html**
3. **Check Python generators** exist
4. **Create generators** if missing! 🚨
5. **Syntax validation** (imports, indentation)
6. **Pin match** (S5 exact)
7. **Variable match** (S7 exact)
8. **Logic match** (S8 exact)
9. **Feature completeness** (ALL problem requirements)
10. **Cross-section validation** (7-way check)

**Critical Checks:**
- ✅ Problem: "DHT11" → Code: DHT11 (not DHT22!)
- ✅ Problem: "600s" → Code: 600 (not 10!)  
- ✅ Problem: "log_1.txt" → Code: log_1.txt (not log.bak!)
- ✅ All imports present
- ✅ All pins match S5
- ✅ All variables match S7

**IF Block Generator Missing:**
```javascript
Blockly.Python['block'] = function(block) {
  var code = 'python_code\n';
  return code;
};
```
- Add to picofile.html
- Test generation
- **FAIL validation** (generator creation needed)

---

## 🚫 Prohibited in Validation

- ❌ Skip sections
- ❌ Say "looks fine" without checking
- ❌ Batch multiple projects
- ❌ Make assumptions
- ❌ Vague improvement reports

---

## ✅ Required in Output

- ✅ Verdict table (S1-S12)
- ✅ Per-section verdicts
- ✅ Overall verdict
- ✅ Specific improvements (if WARN/FAIL)
- ✅ Section references in improvements
- ✅ Explanations of WHY

---

## 📚 File Locations

```
Validation Framework:
→ Reference_Bible_Standards/ELITE_AUDITOR_VALIDATION_FRAMEWORK.md

12-Step Checklist:
→ Reference_Bible_Standards/ELITE_AUDITOR_12_STEP_CHECKLIST.md

Problem Statements:
→ Problem_Statements/Projects_XXXX_YYYY.md

Documentation:
→ Documentation/Docs_XXXX_YYYY.md

Navigation:
→ Reference_Bible_Standards/MASTER_INDEX.md
```

---

## 🔄 Workflow Loop

```
┌─────────────────────────────┐
│  Read Problem Statement     │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Load Documentation         │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Run 12-Step Checklist      │
│  (S1 → S2 → ... → S12)      │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Cross-Validate Links       │
│  (7 mandatory links)        │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Generate Verdict Table     │
│  + Improvement Report       │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Move to Next Project       │
└─────────────────────────────┘
```

---

## 🎯 Quality Target

**Every project must achieve:**
- Problem alignment: 100%
- Cross-links: All verified
- Code correctness: Exact problem
- Traceability: Complete chain
- Format: Elite Standard

---

## 💡 Pro Tips

1. **Read problem first** - it's the source of truth
2. **S8 & S10 are critical** - spend extra time here
3. **Cross-check everything** - use the matrix
4. **Be specific** - vague reports don't help
5. **One project at a time** - don't batch
6. **Zero tolerance** - if in doubt, FAIL it

---

**Version:** 3.0 | **Status:** Production  
**Print this card for quick reference during validation!**
