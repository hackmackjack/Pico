# START PASS 3: Generate Batch 37 (OLED Shapes 2)
# Projects 0361-0370

print("🚀 STARTING PASS 3 - Batch 37: OLED Shapes 2")
print("Generating Projects 0361-0370...")

batch_37_start = '''

---

# 🎯 PASS 3: Projects 0361-0400

---

# 🏁 Batch 37: OLED Shapes 2

## 1️⃣ Project 0361: Introduction to OLED Shapes

### 2️⃣ Learning Objective
Master full-frame OLED operations with filled rectangles. You will learn frame buffer manipulation and screen refresh techniques.

### 3️⃣ Concepts Introduced
*   **Full Frame Buffer**: Manipulating entire display memory.
*   **Fill Operations**: Setting all pixels to specific value.
*   **Screen Inversion**: Toggling between white and black backgrounds.

### 4️⃣ Hardware Required
*   **Pico**
*   **OLED Display** (128x64, I2C - SSD1306)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED SDA** | GP0 | I2C data |
| **OLED SCL** | GP1 | I2C clock |

### 6️⃣ Blocks Used

🔹 **Setup I2C & OLED**
*   **Category:** Communication/Displays

🔹 **OLED Rectangle**
*   **Category:** Displays
*   **Block:** `fill rectangle x:[0] y:[0] w:[128] h:[64] color:[1]`

🔹 **OLED Clear & Show**
*   **Category:** Displays

### 7️⃣ Variables & State
*   None (alternating full-screen states).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Fill White (All Pixels ON)**:
        *   From **Displays**, drag `fill rectangle x:[0] y:[0] w:[128] h:[64] color:[1]`.
            *   **Snap** into loop (white = color 1).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below (update display).
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.
    *   **Clear to Black (All Pixels OFF)**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below (clears to black).
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The display alternates between completely white (all pixels ON) and completely black (all pixels OFF) every second. This demonstrates full frame buffer control - the filled rectangle at position (0,0) with dimensions 128×64 covers the entire screen. The OLED show command transfers the frame buffer to the display hardware. Useful for screen blanking, flash effects, or display testing.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Fill white
    oled.fill_rect(0, 0, 128, 64, 1)
    oled.show()
    time.sleep(1)
    
    # Clear to black
    oled.fill(0)
    oled.show()
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **OLED Not Responding**: Verify I2C address (usually 0x3C). Use I2C scan: `i2c.scan()` to confirm device presence.
*   **Ghosting/Burn-in**: Prolonged white screen can cause temporary image retention. Vary patterns or reduce brightness.
*   **Forgot `show()`**: If screen doesn't update, ensure `oled.show()` is called after drawing operations.

### 1️⃣2️⃣ Try This Next

*   **Checkerboard**: Alternate filled and empty rectangles in grid pattern.
*   **Fade Effect**: Use grayscale (if supported) or rapid flashing to simulate fade in/out.
*   **Screen Saver**: Random rectangles filling screen over time to prevent burn-in.

---

[Continuing with Projects 0362-0370...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_37_start)

print("✅ Project 0361 appended - PASS 3 STARTED!")
print("⏳ Continuing with remaining Batch 37 projects...")
