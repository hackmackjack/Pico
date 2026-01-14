import os

def fill_batch51():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # We will replace the placeholder for 0509-0510
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    p0509_0510 = """## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Simulate a day/night color cycle (Sunrise → Noon → Sunset → Night) over 20 seconds.

### 3. Concepts Introduced
*   **Temporal Sequencing**: Mapping time to light color
*   **Color Atmosphere**: Using R, G, B to represent sunlight

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`**
*   **from Time, drag `pico_wait`**

### 7. Variables
*   None

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, drag PWM setup blocks for GP16, GP17, GP18.
        *   **Snap** into setup section.

**B. Main Loop Phase**
2.  **Sunrise (Orange)**:
    *   From **Smart IO**, drag `pico_pwm_write`.
        *   **Snap** into loop.
        *   R=65535, G=20000, B=0.
    *   Wait 5s.
3.  **Noon (White)**:
    *   Set R,G,B to 65535. Wait 5s.
4.  **Sunset (Red)**:
    *   Set R=65535, G=0, B=0. Wait 5s.
5.  **Night (Blue)**:
    *   Set R=0, G=0, B=40000. Wait 5s.

### 9. Execution Flow
The sequence cycles through four color phases every 20 seconds.

### 10. Generated Code
```python
import machine, time
r, g, b = [machine.PWM(machine.Pin(i)) for i in (16, 17, 18)]
for p in (r, g, b): p.freq(1000)
while True:
    # Sunrise
    r.duty_u16(65535); g.duty_u16(20000); b.duty_u16(0); time.sleep(5)
    # Noon
    r.duty_u16(65535); g.duty_u16(65535); b.duty_u16(65535); time.sleep(5)
    # Sunset
    r.duty_u16(65535); g.duty_u16(0); b.duty_u16(0); time.sleep(5)
    # Night
    r.duty_u16(0); g.duty_u16(0); b.duty_u16(40000); time.sleep(5)
```

---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Create a parametric shading function where purple intensity is controlled by a parameter (0-100).

### 3. Concepts Introduced
*   **Function Parameters**: Reusable color scaling
*   **Arithmetic Mapping**: Percent to PWM

### 4. Hardware Required
Pico, RGB LED

### 6. Blocks Used
*   **from Functions, drag `definition`**
*   **from Smart IO, drag `pico_pwm_write`**

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Define Function**:
    *   From **Functions**, drag `definition`.
        *   Name: `shade_purple`, Parameter: `intensity`.

**B. Main Loop Phase**
2.  **Call Function**:
    *   From **Loops**, drag `for_loop` (0 to 100).
    *   Inside loop, call `shade_purple` with current loop index.

### 10. Generated Code
```python
import machine, time
r, b = machine.PWM(machine.Pin(16)), machine.PWM(machine.Pin(18))
def shade_purple(p):
    val = int(p * 655.35)
    r.duty_u16(val); b.duty_u16(val)
while True:
    for i in range(101): shade_purple(i); time.sleep(0.02)
    for i in range(100, -1, -1): shade_purple(i); time.sleep(0.02)
```

---
"""
    
    placeholder = "## 1. Project 0509: Automated Digital Art\n\n### 2. Learning Objective\nTimed cycle simulating 24-hour patterns using colored LED lighting shifts.\n\n---\n\n## 1. Project 0510: Mastering Digital Art\n\n### 2. Learning Objective\nReusable function to define custom color blending ratios via numeric parameters.\n\n---"
    
    new_content = content.replace(placeholder, p0509_0510)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Batch 51 completed.")

if __name__ == "__main__":
    fill_batch51()
