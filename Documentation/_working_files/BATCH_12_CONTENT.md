# BATCH 12: Animation 1 (Projects 0111-0120)

## Project 0111: Introduction to Animation

### 1. Learning Objective
Display simple text frames on an OLED screen. Learn the fundamental concept of animation as sequential image display.

### 2. Concepts Introduced
*   **OLED Display**: Small monochrome screen using I2C or SPI communication
*   **Frame**: Single still image in an animation sequence
*   **Clear and Redraw**: Animation technique of erasing then drawing next frame

### 3. Hardware Required
*   Raspberry Pi Pico
*   SSD1306 OLED Display (128x64 pixels, I2C)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **OLED VCC** | 3.3V | Power supply |
| **OLED GND** | GND | Ground |
| **OLED SCL** | GP1 | I2C Clock |
| **OLED SDA** | GP0 | I2C Data |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Smart Display, drag `pico_oled_init`** (initialize OLED)
*   **from Smart Display, drag `pico_oled_text`** (display text)
*   **from Smart Display, drag `pico_oled_clear`** (clear screen)
*   **from Smart Display, drag `pico_oled_show`** (update display)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **None**: Simple sequential display without state tracking.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Initialize OLED Display**:
    *   From **Smart Display**, drag `pico_oled_init`.
    *   **Set** Width -> 128, Height -> 64.
    *   **Set** I2C pins -> SDA=GP0, SCL=GP1.
    *   **Snap** at
