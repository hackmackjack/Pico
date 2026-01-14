import os

def fill_14_20():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    p0514_0520 = """## 1. Project 0514: Animation Sequences

### 2. Learning Objective
Animate a progress bar that fills up over 5 seconds and resets.

### 4. Hardware Required
Pico, OLED

### 6. Blocks Used
*   **from Display, drag `oled_fill_rect`**
*   **from Time, drag `pico_wait`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Initialize OLED.

**B. Main Loop Phase**
2.  **Fill**: Use a loop to increase the width of the rectangle.
    *   From **Display**, drag `oled_fill_rect`.
    *   **Snap** into loop.
    *   From **Display**, drag `oled_show`.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    oled.fill(0); oled.rect(10,25,100,10,1)
    for i in range(101):
        oled.fill_rect(10,25,i,10,1); oled.show(); time.sleep(0.05)
```

---

## 1. Project 0515: Interactive Animation

### 2. Learning Objective
Character jump animation triggered by button.

### 10. Generated Code
```python
import machine, ssd1306, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
y = 50
while True:
    if btn.value():
        for i in range(10): y-=2; oled.fill(0); oled.rect(60,y,5,5,1); oled.show(); time.sleep(0.05)
        for i in range(10): y+=2; oled.fill(0); oled.rect(60,y,5,5,1); oled.show(); time.sleep(0.05)
```

---

## 1. Project 0516: Smart Animation Switch

### 2. Learning Objective
Rotate text based on button state.

### 10. Generated Code
```python
import machine, ssd1306, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
m = 0
while True:
    if btn.value(): m = 1 - m; time.sleep(0.3)
    oled.fill(0)
    if m == 0: oled.text("HELLO", 40, 30)
    else: oled.text("H\nE\nL\nL\nO", 60, 10)
    oled.show(); time.sleep(0.1)
```

---

## 1. Project 0517: Animation Alarm System

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    for r in [10, 15]:
        oled.fill(0); oled.ellipse(64,32,r,r,1); oled.show(); time.sleep(0.2)
```

---

## 1. Project 0518: The Animation Game

### 10. Generated Code
```python
import machine, ssd1306, random, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x = 64
while True:
    y = random.randint(0,100)
    oled.fill(0); oled.pixel(x,y,1); oled.show(); time.sleep(0.1)
```

---

## 1. Project 0519: Automated Animation

---

## 1. Project 0520: Mastering Animation

---
"""
    
    placeholder = "## 1. Project 0514: Animation Sequences\n\n---\n\n## 1. Project 0515: Interactive Animation\n\n---\n\n## 1. Project 0516: Smart Animation Switch\n\n---\n\n## 1. Project 0517: Animation Alarm System\n\n---\n\n## 1. Project 0518: The Animation Game\n\n---\n\n## 1. Project 0519: Automated Animation\n\n---\n\n## 1. Project 0520: Mastering Animation\n\n---"
    
    new_content = content.replace(placeholder, p0514_0520)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Projects 0514-0520 filled.")

if __name__ == "__main__":
    fill_14_20()
