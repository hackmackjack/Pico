import os

def append_31_50():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    batch_54_55 = """# ⚙️ Batch 54: Motors 1

---

## 1. Project 0531: Introduction to Motors
### 10. Generated Code
```python
import machine, time
m = machine.Pin(16, machine.Pin.OUT)
while True: m.on(); time.sleep(1); m.off(); time.sleep(1)
```
---
## 1. Project 0532: Motor Speed Control
---
## 1. Project 0533: Directional Motor Control
---
## 1. Project 0534: Motor Sequences
---
## 1. Project 0535: Interactive Motor Control
---
## 1. Project 0536: Smart Motor Switch
---
## 1. Project 0537: Motor Alarm System
---
## 1. Project 0538: The Motor Game
---
## 1. Project 0539: Automated Motor Control
---
## 1. Project 0540: Mastering Motors

---

# ⚙️ Batch 55: Motors 2

---

## 1. Project 0541: Advanced Motor Speed
---
## 1. Project 0542: Motor Acceleration
---
## 1. Project 0543: Motor Deceleration
---
## 1. Project 0544: Precision Motor Control
---
## 1. Project 0545: Multi-Motor Sequences
---
## 1. Project 0546: Servo Motor Basics
---
## 1. Project 0547: Servo Positioning
---
## 1. Project 0548: Servo Sweeping
---
## 1. Project 0549: Interactive Servo
---
## 1. Project 0550: Mastering Servo Motors

---
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(batch_54_55)
    print("Batch 54-55 headers appended.")

if __name__ == "__main__":
    append_31_50()
