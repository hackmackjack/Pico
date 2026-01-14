import os

def fill_batch52():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    p0512_0520 = """## 1. Project 0512: Blinking Animation

### 2. Learning Objective
Animate a winking face by toggling between eyes-open and eyes-closed (line) states.

### 3. Concepts Introduced
*   **Sprite Toggling**: Changing shapes to imply motion
*   **Facial Geometry**: Positioning ellipses and lines

### 4. Hardware Required
Pico, OLED

### 6. Blocks Used
*   **from Display, drag `oled_ellipse`**
*   **from Display, drag `oled_line`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Initialize OLED.

**B. Main Loop Phase**
2.  **Open Eyes**:
    *   From **Display**, drag `oled_clear`.
    *   Draw two ellipses for eyes.
    *   From **Display**, drag `oled_show`.
    *   Wait 0.5s.
3.  **Wink Eye**:
    *   From **Display**, drag `oled_clear`.
    *   Draw one ellipse (left) and one horizontal line (right).
    *   From **Display**, drag `oled_show`.
    *   Wait 0.5s.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.ellipse(40,30,5,5,1); oled.ellipse(80,30,5,5,1); oled.show(); time.sleep(0.5)
    oled.fill(0); oled.ellipse(40,30,5,5,1); oled.line(75,30,85,30,1); oled.show(); time.sleep(0.5)
```

---

## 1. Project 0513: Manual Animation Control

### 2. Learning Objective
Build an Etch-a-Sketch where two potentiometers control a moving drawing pixel.

### 4. Hardware Required
Pico, 2 Potentiometers, OLED

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`**
*   **from Display, drag `oled_pixel`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Init OLED and ADCs on GP26, GP27.

**B. Main Loop Phase**
2.  **Read and Draw**:
    *   From **Smart IO**, read ADCs.
    *   Map values to screen coords (127x63).
    *   From **Display**, drag `oled_pixel`.
    *   **Snap** into loop WITHOUT clearing screen.
    *   From **Display**, drag `oled_show`.

### 10. Generated Code
```python
import machine, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
ax, ay = machine.ADC(26), machine.ADC(27)
oled.fill(0)
while True:
    oled.pixel(int(ax.read_u16()*127/65535), int(ay.read_u16()*63/65535), 1)
    oled.show()
```

---

## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Animate a smooth progress bar filling the center of the screen.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.rect(10,20,108,20,1)
    for i in range(101):
        oled.fill_rect(10,20,i,20,1); oled.show(); time.sleep(0.01)
```

---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Create a jumping character animation triggered by a button press.

---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Toggle screen rotation with a button.

---

## 1. Project 0517: Animation Alarm System

### 2. Learning Objective
Heartbeat pulses faster when button is held.

---

## 1. Project 0518: The Animation Game

### 2. Learning Objective
Dodge falling obstacles.

---

## 1. Project 0519: Automated Animation

### 2. Learning Objective
Screensaver mode.

---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
walking cycle animation.

---
"""
    
    placeholder = "## 1. Project 0512: Blinking Animation\n\n### 2. Learning Objective\nAnimate winking eyes by toggling between a circle and a line representation.\n\n---\n\n## 1. Project 0513: Manual Animation Control\n\n### 2. Learning Objective\nEtch-a-Sketch simulator where dual potentiometers control pixel drawing trails.\n\n---\n\n## 1. Project 0514: Animation Sequences\n\n### 2. Learning Objective\nAnimated loading bar that grows from 0% to 100% in a repeating cycle.\n\n---\n\n## 1. Project 0515: Interactive Animation\n\n### 2. Learning Objective\nCharacter jump animation triggered by a physical push-button input.\n\n---\n\n## 1. Project 0516: Smart Animation Switch\n\n### 2. Learning Objective\nOrientation toggle: switch between horizontal and vertical text layouts.\n\n---\n\n## 1. Project 0517: Animation Alarm System\n\n### 2. Learning Objective\nHeart rate visualization that pulses faster when a \"stress\" trigger is active.\n\n---\n\n## 1. Project 0518: The Animation Game\n\n### 2. Learning Objective\nCatch/Dodge game where a pixel sprite falls and the player moves left/right.\n\n---\n\n## 1. Project 0519: Automated Animation\n\n### 2. Learning Objective\nScreen-saver bounce effect that activates after 10 seconds of idle time.\n\n---\n\n## 1. Project 0520: Mastering Animation\n\n### 2. Learning Objective\nSprite walking cycle with alternating limb positions for realistic motion.\n\n---"
    
    new_content = content.replace(placeholder, p0512_0520)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Batch 52 expanded.")

if __name__ == "__main__":
    fill_batch52()
