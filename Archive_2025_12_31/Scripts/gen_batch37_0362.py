# COMPLETE BATCH 37: Generate Projects 0362-0370
# OLED Shapes 2 - Eyes, Cursor, Explosion, Paint, Leveler, Alarm, Maze, Bouncing Ball, QR Code

print("Completing Batch 37 with Projects 0362-0370...")

batch37_complete = '''
## 1️⃣ Project 0362: Blinking OLED Shapes

### 2️⃣ Learning Objective
Create animated character eyes with moving pupils. You will learn sprite animation and position-based drawing.

### 3️⃣ Concepts Introduced
*   **Character Animation**: Creating expressive visual elements.
*   **Relative Positioning**: Drawing elements relative to base position.
*   **Frame-by-Frame Animation**: Updating positions over time.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (128x64, I2C)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C data |
| **OLED SCL** | GP1 | I2C clock |

### 6️⃣ Blocks Used

🔹 **OLED Circle & Filled Circle**
*   **Category:** Displays

🔹 **OLED Clear & Show**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **pupilX**: Horizontal offset for pupils (-5 for left, +5 for right).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Clear Screen**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** into loop.
    *   **Draw Left Eye (Outline)**:
        *   From **Displays**, drag `circle x:[40] y:[32] r:[15] color:[1]`.
            *   **Snap** below.
    *   **Draw Right Eye (Outline)**:
        *   From **Displays**, drag `circle x:[88] y:[32] r:[15] color:[1]`.
            *   **Snap** below.
    *   **Pupils Look Left**:
        *   From **Variables**, drag `set [pupilX] to [-5]`.
            *   **Snap** below.
        *   From **Displays**, drag `filled circle x:[40 + pupilX] y:[32] r:[5] color:[1]`.
            *   **Snap** below (left pupil).
        *   From **Displays**, drag `filled circle x:[88 + pupilX] y:[32] r:[5] color:[1]`.
            *   **Snap** below (right pupil).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.
    *   **Pupils Look Right**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   Draw eye outlines again (same as above).
        *   From **Variables**, drag `set [pupilX] to [5]`.
            *   **Snap** below.
        *   Draw pupils with +5 offset.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Two circular eyes (circles at x=40 and x=88, radius 15) are drawn with moving pupils (filled circles radius 5). Pupils shift left (offset -5) then right (offset +5) every second, creating a looking animation. The eyes appear to track something moving horizontally. This demonstrates character emoting and is foundational for interactive displays, robot faces, or animated characters.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Clear and draw eyes
    oled.fill(0)
    oled.circle(40, 32, 15, 1)  # Left eye
    oled.circle(88, 32, 15, 1)  # Right eye
    
    # Pupils look left
    oled.fill_circle(35, 32, 5, 1)  # Left pupil
    oled.fill_circle(83, 32, 5, 1)  # Right pupil
    oled.show()
    time.sleep(1)
    
    # Clear and redraw
    oled.fill(0)
    oled.circle(40, 32, 15, 1)
    oled.circle(88, 32, 15, 1)
    
    # Pupils look right
    oled.fill_circle(45, 32, 5, 1)
    oled.fill_circle(93, 32, 5, 1)  
    oled.show()
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Pupils Outside Eyes**: Ensure pupil offset doesn't exceed eye radius-pupil radius (max offset = 15-5 = 10).
*   **Flickering**: Always clear before redrawing to prevent ghosting of previous frames.
*   **Eyes Not Circular**: If using `ellipse()`, verify width=height for perfect circles.

### 1️⃣2️⃣ Try This Next

*   **Blinking**: Add closed eyes (horizontal line) state between looks.
*   **Vertical Movement**: Add up/down pupil positions for 4-way gaze.
*   **Emotion Expressi on**: Change eye shape (wide for surprise, narrowed for suspicion).

---

[Due to length constraints, I'll generate remaining projects 0363-0370 efficiently in next block]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch37_complete)

print("✅ Project 0362 appended")
print("⏳ Generating projects 0363-0370 to complete Batch 37...")
print(f"   Current: 62/100 projects")
