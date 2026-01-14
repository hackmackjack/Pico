# STEP-BY-STEP GUIDE FIX TEMPLATE

## ✅ GOLD STANDARD FORMAT

Every Step-by-Step Guide MUST follow this structure:

```markdown
### 8️⃣ Step-by-Step Guide
*   **1. [Action Name]**
    *   From **[Category]**, drag `[Block Name]`.
    *   **Snap** it [location].
    *   [Optional: Change/Configure instructions].
*   **2. [Next Action]**
    *   From **[Category]**, drag `[Block Name]`.
    *   **Snap** it [below/inside/into socket of] [previous block].
    *   Change `[field]` to `[value]`.
```

## 🔧 COMMON PATTERNS

### Pattern 1: Forever Loop + LED Control
```markdown
*   **1. Start Program**
    *   From **Loops**, drag `forever do`.
    *   **Snap** it into the workspace.
*   **2. Turn LED ON**
    *   From **Smart IO**, drag `Turn LED [GP15] [ON]`.
    *   **Snap** it inside the forever loop.
*   **3. Wait**
    *   From **Timing**, drag `sleep [1] seconds`.
    *   **Snap** it below the LED block.
    *   Change `[1]` to `[2]`.
*   **4. Turn LED OFF**
    *   From **Smart IO**, drag `Turn LED [GP15] [ON]`.
    *   **Snap** it below the wait block.
    *   Change `[ON]` to `[OFF]`.
```

### Pattern 2: Button + Conditional Logic
```markdown
*   **1. Start Program**
    *   From **Loops**, drag `forever do`.
   **Snap** it into the workspace.
*   **2. Check Button**
    *   From **Logic**, drag `if [condition] then`.
    *   **Snap** it inside the forever loop.
    *   From **Pin Access**, drag `digital read pin [10]`.
    *   **Snap** the read block into the `[condition]` socket.
    *   Change pin to `10`.
*   **3. Action When Pressed**
    *   From **Text**, drag `print [Hello]`.
    *   **Snap** it inside the "then" section.
    *   Click `[Hello]` and type `Button Pressed!`.
```

### Pattern 3: Variable Assignment
```markdown
*   **1. Create Variable**
    *   From **Variables**, drag `set [var] to`.
    *   From **Math**, drag `[0]`.
    *   **Snap** the number block into the socket.
    *   Change variable name to `counter`.
```

### Pattern 4: Sensor Reading
```markdown
*   **1. Read Sensor**
    *   From **Variables**, drag `set [temp] to`.
    *   From **Sensors**, drag `Read DHT11 Temperature`.
    *   **Snap** the sensor block into the socket of the set block.
    *   Change variable name to `temp`.
*   **2. Display Value**
    *   From **Displays**, drag `LCD Print [text]`.
    *   From **Variables**, drag `temp`.
    *   **Snap** the variable block into the `[text]` socket.
```

## ❌ BAD EXAMPLES (DO NOT USE)

### Bad: Abstract Logic
```markdown
*   **Loop**:
    *   IF Button: Buzzer ON.
    *   ELSE: Buzzer OFF.
```

### Bad: Assignment Notation
```markdown
*   `temp` = Read DHT11.
*   Print `temp`.
```

### Bad: Missing Snap Instructions
```markdown
*   From **Timing**, drag `sleep [1] seconds`.
*   Change to 2 seconds.
```
*(Missing: Where to snap it!)*

## 🚀 BATCH FIX STRATEGY

### For Projects 1-100:
1. Search for pattern: `*   **Loop**:` or `IF Button:` (abstract)
2. Replace with explicit drag/snap/configure
3. Verify each "drag" has a "**Snap**" within 2 lines

### For Projects 101-200:
1. Most already have "drag" - just need "**Snap**" added
2. Use regex: After line with `drag`, add snap instruction

## 📋 COMPLETION CHECKLIST

For each project, verify:
- [ ] Every action starts with "From **[Category]**, drag..."
- [ ] Every dragged block has a "**Snap** it..." instruction
- [ ] Field changes use "Change `[field]` to `[value]`" format
- [ ] No abstract logic (no "`var` = " notation)
- [ ] No assumptions (every physical action described)

## 🎯 PRIORITY PROJECTS TO FIX MANUALLY

1. **P0001-P0010**: Foundation projects (most viewed)
2. **P0011-P0020**: Button/Input fundamentals
3. **P0051-P0060**: Night Light (popular)
4. **P0061-P0070**: Doorbell (popular)
5. **P0101-P0110**: LCD (new batch, should be good but verify)
6. **P0171-P0180**: Neopixels (showcase project)

Remaining 160+ projects can be batch-fixed using templates.
