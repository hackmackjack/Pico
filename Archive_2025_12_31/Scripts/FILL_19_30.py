import os

def fill_19_30():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    p0519_0520 = """## 1. Project 0519: Automated Animation

### 2. Learning Objective
DVD bounce effect screensaver.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
x,y,dx,dy = 10,10,2,2
while True:
    x+=dx; y+=dy
    if x<0 or x>110: dx*=-1
    if y<0 or y>55: dy*=-1
    oled.fill(0); oled.text("DVD",x,y); oled.show(); time.sleep(0.05)
```

---

## 1. Project 0520: Mastering Animation

### 2. Learning Objective
Complex sprite walking cycle with arm movement.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
f = 0
while True:
    oled.fill(0); oled.ellipse(64,32,10,15,1); oled.line(54,32,74,32,1)
    if f: oled.line(64,47,54,57,1); oled.line(64,47,74,57,1)
    else: oled.line(64,47,64,60,1)
    oled.show(); f = not f; time.sleep(0.2)
```

---
"""
    
    p0521_0530 = """## 1. Project 0521: Introduction to Binary Counters

### 2. Learning Objective
Display a 4-bit binary count on 4 LEDs.

### 10. Generated Code
```python
import machine, time
l = [machine.Pin(i, machine.Pin.OUT) for i in range(10,14)]
c = 0
while True:
    for i in range(4): l[i].value((c>>i)&1)
    c = (c+1)%16; time.sleep(1)
```

---

## 1. Project 0522: Binary LED Sequences

### 10. Generated Code
```python
import machine, time
l = [machine.Pin(i, machine.Pin.OUT) for i in range(10,14)]
v = 0
while True:
    g = v ^ (v >> 1)
    for i in range(4): l[i].value((g >> i) & 1)
    v = (v + 1) % 16; time.sleep(1)
```

---

## 1. Project 0523: Manual Binary Control

### 10. Generated Code
```python
import machine
sw = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(14,18)]
l = [machine.Pin(i, machine.Pin.OUT) for i in range(10,14)]
while True:
    for i in range(4): l[i].value(sw[i].value())
```

---

## 1. Project 0524: Binary Sequences

---

## 1. Project 0525: Interactive Binary

---

## 1. Project 0526: Advanced Binary

---

## 1. Project 0527: Binary Logic

---

## 1. Project 0528: Binary Math

---

## 1. Project 0529: Binary Conversion

---

## 1. Project 0530: Mastering Binary

---
"""

    content = content.replace("## 1. Project 0519: Automated Animation\n\n---\n\n## 1. Project 0520: Mastering Animation\n\n---", p0519_0520)
    content = content.replace("## 1. Project 0521: Introduction to Binary Counters\n\n---\n\n## 1. Project 0522: Binary LED Sequences\n\n---\n\n## 1. Project 0523: Manual Binary Control\n\n---", p0521_0530)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Projects 0519-0523 filled.")

if __name__ == "__main__":
    fill_19_30()
