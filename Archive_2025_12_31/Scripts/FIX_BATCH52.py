#!/usr/bin/env python3
"""
FIX BATCH 52 - Regenerate with proper Elite Standard v2.0 format
"""

import re

# Read current doc
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where Batch 52 starts and ends
batch52_start = content.find('# 📺 Batch 52: Animation 3')
batch52_end = content.find('# ', batch52_start + 1)  # Next batch header

if batch52_start == -1:
    print("ERROR: Batch 52 not found")
    exit(1)

# Keep everything before Batch 52 and after (if any)
before_batch52 = content[:batch52_start]
after_batch52 = content[batch52_end:] if batch52_end != -1 else ""

print(f"Found Batch 52 at position {batch52_start}")
print("Regenerating with proper Elite Standard format...")
print()

# Create properly formatted Batch 52
batch52_proper = '''# 📺 Batch 52: Animation 3

---

## 1. Project 0511: Introduction to Animation

### 2. Learning Objective
Display countdown "3", "2", "1" on OLED filling entire screen with clear between numbers.

### 3. Concepts Introduced
*   **Full-Screen Display**: Large text rendering
*   **Sequential Animation**: Timed sequence
*   **Screen Clearing**: Between frames

### 4. Hardware Required
Pico, OLED Display (128x64, I2C)

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **OLED SDA** | GP0 | I2C Data |
| **OLED SCL** | GP1 | I2C Clock |
| **OLED VCC** | 3.3V | Power |
| **OLED GND** | GND | Ground |

### 6. Blocks Used
*   **from Display, drag `oled_init`** (initialize OLED)
*   **from Display, drag `oled_text`** (draw text)
*   **from Display, drag `oled_clear`** (clear screen)
*   **from Display, drag `oled_show`** (update display)
*   **from Time, drag `pico_wait`** (timing)
*   **from Loops, drag `pico_forever`** (continuous loop)

### 7. Variables
*   None (sequential display)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize I2C**:
    *   From **Display**, drag I2C configuration block.
        *   **Snap** into setup section.
        *   Set SDA=GP0, SCL=GP1.
2.  **Initialize OLED**:
    *   From **Display**, drag `oled_init` block.
        *   **Snap** below.
        *   Configure for 128x64 display.

**B. Main Loop Phase**
3.  **Display "3"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** into main loop.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
        *   Set text: "3", size: large, position: center.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.
4.  **Display "2"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
        *   Set text: "2", size: large, position: center.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.
5.  **Display "1"**:
    *   From **Display**, drag `oled_clear` block.
        *   **Snap** below.
    *   From **Display**, drag `oled_text` block.
        *   **Snap** below.
        *   Set text: "1", size: large, position: center.
    *   From **Display**, drag `oled_show` block.
        *   **Snap** below.
    *   From **Time**, drag `pico_wait` block.
        *   **Snap** below.
        *   Set 1 second.

### 9. Execution Flow
OLED initialized via I2C. Main loop displays "3" for 1s, clears, displays "2" for 1s, clears, displays "1" for 1s, then repeats. Full-screen countdown sequence.

### 10. Generated Code
```python
from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Display 3
    oled.fill(0)
    oled.text("  3", 40, 24, 1)
    oled.show()
    time.sleep(1)
    
    # Display 2
    oled.fill(0)
    oled.text("  2", 40, 24, 1)
    oled.show()
    time.sleep(1)
    
    # Display 1
    oled.fill(0)
    oled.text("  1", 40, 24, 1)
    oled.show()
    time.sleep(1)
```

### 11. Common Mistakes
*   Wrong I2C pins (verify wiring)
*   Not calling show() after drawing
*   Text too small (increase font size)
*   Wrong I2C address (usually 0x3C or 0x3D)

### 12. Try This Next
*   Add "GO!" after countdown
*   Animate with growing text size
*   Add buzzer sound effects
*   Reverse countdown (1→2→3)

---

'''

# Save
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(before_batch52 + batch52_proper + after_batch52)

print("✓ Project 0511 regenerated with proper Elite Standard format")
print("Next: Regenerating 0512-0520 with same quality...")
