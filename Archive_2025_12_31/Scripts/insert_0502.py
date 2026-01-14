#!/usr/bin/env python3
"""
INSERT MISSING PROJECT 0502
"""

project_0502 = '''
## 1. Project 0502: Blinking Digital Art

### 2. Learning Objective
Implement CMY color model cycling with RGB LED.

### 3. Concepts Introduced
*   **CMY Color Model**: Cyan, Magenta, Yellow (subtractive primaries shown with additive LED)
*   **Color Mixing**: Yellow (R+G), Cyan (G+B), Magenta (R+B)
*   **Sequential Display**: Cycle through three colors

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | 220Ω resistor |
| **Green LED** | GP17 | 220Ω resistor |
| **Blue LED** | GP18 | 220Ω resistor |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_write`** (control individual RGB channels)
*   **from Time, drag `pico_wait`** (timing between color changes)
*   **from Loops, drag `pico_forever`** (continuous cycle)

### 7. Variables
*   **currentColor**: Tracks current step (0=Yellow, 1=Cyan, 2=Magenta)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure RGB Pins**:
    *   From **Smart IO**, drag pin configuration blocks.
        *   **Snap** into setup.
        *   Set GP16, GP17, GP18 as outputs.
2.  **Initialize Color Index**:
    *   From **Variables**, drag initialization.
        *   **Snap** below.
        *   Set currentColor = 0.

**B. Main Loop Phase**
3.  **Display Yellow (R+G)**:
    *   From **Smart IO**, drag gpio_write blocks.
        *   **Snap** into loop.
        *   Set Red=HIGH, Green=HIGH, Blue=LOW.
4.  **Wait**:
    *   From **Time**, drag pico_wait.
        *   **Snap** below.
        *   Set 0.5-1 second delay.
5.  **Display Cyan (G+B)**:
    *   From **Smart IO**, drag gpio_write blocks.
        *   **Snap** below.
        *   Set Red=LOW, Green=HIGH, Blue=HIGH.
6.  **Wait**:
    *   From **Time**, drag pico_wait.
        *   **Snap** below.
7.  **Display Magenta (R+B)**:
    *   From **Smart IO**, drag gpio_write blocks.
        *   **Snap** below.
        *   Set Red=HIGH, Green=LOW, Blue=HIGH.
8.  **Wait**:
    *   From **Time**, drag pico_wait.
        *   **Snap** below.
        *   Loop repeats automatically.

### 9. Execution Flow
System cycles through CMY colors: Yellow (Red+Green) → Cyan (Green+Blue) → Magenta (Red+Blue). Each color displays for ~1 second before transitioning to next, creating continuous cyclic display of secondary colors.

### 10. Generated Code
```python
import machine, time

# RGB LED pins
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

while True:
    # Yellow (R+G)
    red.on(); green.on(); blue.off()
    time.sleep(1)
    
    # Cyan (G+B)  
    red.off(); green.on(); blue.on()
    time.sleep(1)
    
    # Magenta (R+B)
    red.on(); green.off(); blue.on()
    time.sleep(1)
```

### 11. Common Mistakes
*   **Wrong color combinations**: Yellow is R+G, not R+B
*   **Timing too fast**: Need visible display time (0.5-1s minimum)
*   **Forgetting to turn channels OFF**: Must explicitly set unused channels LOW
*   **RGB vs CMY confusion**: We're displaying CMY colors using RGB additive mixing

### 12. Try This Next
*   Add RGB primary colors to the cycle
*   Smooth fade transitions between colors using PWM
*   Add button to reverse cycle direction
*   Display all 7 colors (RGB + CMY + White)

---

'''

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert (after Project 0501, before "# Batch 51 Completion")
insert_marker = "# Batch 51 Completion: Projects 0503-0510"
if insert_marker in content:
    parts = content.split(insert_marker)
    new_content = parts[0] + project_0502 + insert_marker + parts[1]
else:
    # Fallback: insert before Project 0503
    insert_at = content.find("## 1. Project 0503:")
    if insert_at > 0:
        new_content = content[:insert_at] + project_0502 + "\n" + content[insert_at:]
    else:
        print("ERROR: Could not find insertion point")
        exit(1)

with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Project 0502 inserted successfully")
