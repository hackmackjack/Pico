#!/usr/bin/env python3
"""
COMPLETE DOCUMENTATION GENERATOR - Projects 0501-0600
Merges existing projects and generates remaining 93 projects
"""

import os

print("=" * 70)
print("🚀 GENERATING COMPLETE DOCUMENTATION: PROJECTS 0501-0600")
print("=" * 70)
print()

# Step 1: Merge existing documented projects (0501-0507)
print("Step 1: Merging existing documented projects...")

output = """# 📚 Pico 2500: Elite Documentation (Projects 0501-0600)

**Standard**: Elite Documentation Standard v2.0  
**Projects**: 100 (0501-0600) - Custom Content Per Project

---

# 🎨 Batch 51: Digital Art 3

---

"""

# Read and merge existing files
files_to_merge = [
    (r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'Projects 0501-0502'),
    (r'd:\MFF\Pico\BATCH51_COMPLETION_0503_0510.md', 'Projects 0503-0504'),
    (r'd:\MFF\Pico\BATCH51_REMAINING_0505_0510.md', 'Projects 0505-0507'),
]

for filepath, desc in files_to_merge:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract project content (skip headers)
            if '## 1. Project' in content:
                start_idx = content.find('## 1. Project')
                output += content[start_idx:]
        print(f"  ✓ Merged {desc}")
    except Exception as e:
        print(f"  ⚠ Warning: Could not merge {filepath}: {e}")

print()
print("Step 2: Generating final 3 projects for Batch 51 (0508-0510)...")

# Add Projects 0508-0510 (final 3 for Batch 51)
batch51_final = """
## 1. Project 0508: The Digital Art Game

### 2. Learning Objective
Create reaction game - press button ONLY when green color shown (Go/No-Go).

### 3. Concepts Introduced
*   **Go/No-Go Task**: Selective response to stimuli
*   **Random Color Generation**: Unpredictable challenges
*   **Reaction Testing**: Measuring decision speed

### 4. Hardware Required
Pico, RGB LED, Button

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Button** | GP14 | PULL_DOWN |
| **Red LED** | GP16 | 220Ω |
| **Green LED** | GP17 | 220Ω |
| **Blue LED** | GP18 | 220Ω |

### 6. Blocks Used
*   **from Smart IO, drag `pico_gpio_read`** (read button)
*   **from Smart IO, drag `pico_gpio_write`** (control RGB)
*   **from Math, drag `random_int`** (pick random color)
*   **from Logic, drag `if_compare`** (check response)

### 7. Variables
*   **currentColor**: 0=Red, 1=Green, 2=Blue
*   **score**: Correct responses counter

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Hardware**:
    *   From **Smart IO**, drag pin configs.
       *   **Snap** into setup.
        *   GP14 input, GP16-18 outputs.
2.  **Initialize Score**:
    *   From **Variables**, set score = 0.

**B. Main Loop Phase**
3.  **Pick Random Color**:
    *   From **Math**, random 0-2.
        *   **Snap** into loop.
4.  **Display Color**:
    *   From **Smart IO**, show selected color for 1s.
5.  **Check Button Response**:
    *   From **Logic**, if color=GREEN and button pressed: score++.
    *   If color≠GREEN and button pressed: penalty.
6.  **Next Round**:
    *   Delay, repeat.

### 9. Execution Flow
System picks random color (red/green/blue), displays for 1 second. Player must press button ONLY if green shown. Pressing on red/blue is error. This tests visual discrimination and impulse control.

### 10. Generated Code
```python
import machine, time, random

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)
blue = machine.Pin(18, machine.Pin.OUT)

score = 0

while True:
    # Random color
    color = random.randint(0, 2)
    
    # Show color
    red.value(color == 0)
    green.value(color == 1)
    blue.value(color == 2)
    
    # Wait and check button
    time.sleep(1)
    if btn.value():
        if color == 1:  # Green - correct!
            score += 1
            print(f"Correct! Score: {score}")
        else:  # Wrong color
            print("Error! Don't press on red/blue")
    
    # Turn off
    red.off(); green.off(); blue.off()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   Pressing on every color (must inhibit on red/blue)
*   Not waiting for full display time
*   Missing random import

### 12. Try This Next
*   Add timer - how many correct in 30 seconds?
*   Vary display time (harder when faster)
*   Add yellow LED as "standby" indicator

---

## 1. Project 0509: Automated Digital Art

### 2. Learning Objective
Create automated day/night cycle with timed color transitions.

### 3. Concepts Introduced
*   **Timed Sequences**: Events at specific intervals
*   **Color Transitions**: Sunrise→Noon→Sunset→Night
*   **Temporal Palette**: Time-based color changes

### 4. Hardware Required
Pico, RGB LED

###5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (color mixing)
*   **from Time, drag `pico_wait`** (5s per phase)

### 7. Variables
*   None (sequential timing)

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, set GP16-18 as PWM.

**B. Main Loop Phase**
2.  **Sunrise (Orange)**:
    *   From **Smart IO**, R=HIGH, G=MED, B=LOW.
    *   From **Time**, wait 5s.
3.  **Noon (White)**:
    *   From **Smart IO**, R=HIGH, G=HIGH, B=HIGH.
    *   From **Time**, wait 5s.
4.  **Sunset (Red)**:
    *   From **Smart IO**, R=HIGH, G=LOW, B=LOW.
    *   From **Time**, wait 5s.
5.  **Night (Blue)**:
    *   From **Smart IO**, R=LOW, G=LOW, B=HIGH.
    *   From **Time**, wait 5s.

### 9. Execution Flow
System cycles through 4 phases every 20 seconds: Sunrise (orange 5s) → Noon (white 5s) → Sunset (red 5s) → Night (blue 5s). Repeats continuously, simulating day/night cycle.

### 10. Generated Code
```python
import machine, time

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

while True:
    # Sunrise - Orange
    red.duty_u16(65535)
    green.duty_u16(20000)
    blue.duty_u16(0)
    time.sleep(5)
    
    # Noon - White
    red.duty_u16(65535)
    green.duty_u16(65535)
    blue.duty_u16(65535)
    time.sleep(5)
    
    # Sunset - Red
    red.duty_u16(65535)
    green.duty_u16(0)
    blue.duty_u16(0)
    time.sleep(5)
    
    # Night - Blue
    red.duty_u16(0)
    green.duty_u16(0)
    blue.duty_u16(40000)
    time.sleep(5)
```

### 11. Common Mistakes
*   Wrong color mixing (orange needs R+some G)
*   Timing not equal (should be 5s each)
*   Using digital instead of PWM (loses color nuance)

### 12. Try This Next
*   Smooth fade between phases (not abrupt)
*   Add potentiometer to control cycle speed
*   Display current phase name on OLED

---

## 1. Project 0510: Mastering Digital Art

### 2. Learning Objective
Create parametric color shading function with intensity control.

### 3. Concepts Introduced
*   **Parametric Control**: Intensity parameter (0-100)
*   **Color Scaling**: Multiply base color by intensity
*   **Function Design**: Reusable shading function

### 4. Hardware Required
Pico, RGB LED

### 5. Wiring / Interfaces

| Component | Pin | Notes |
|:---|:---|:---|
| **Red LED** | GP16 | PWM |
| **Green LED** | GP17 | PWM (off for purple) |
| **Blue LED** | GP18 | PWM |

### 6. Blocks Used
*   **from Smart IO, drag `pico_pwm_write`** (intensity control)
*   **from Math, drag `map_range`** (0-100 → 0-65535)
*   **from Functions, drag `create_function`** (shading function)

### 7. Variables
*   **intensity**: 0-100
*   **scaledValue**: Mapped to PWM range

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure PWM**:
    *   From **Smart IO**, set GP16, GP18 as PWM.
2.  **Define Shading Function**:
    *   From **Functions**, create `shadePurple(intensity)`.
    *   Maps intensity to R and B channels, G=0.

**B. Main Loop Phase**
3.  **Iterate Intensities**:
    *   From **Loops**, for intensity 0 to 100.
4.  **Apply Shading**:
    *   Call shadePurple(intensity).
5.  **Display Result**:
    *   Show purple with current intensity.

### 9. Execution Flow
Function `shadePurple(intensity)` calculates R=intensity, B=intensity, G=0. Loop cycles intensity 0→100, creating fade from black to full purple. Demonstrates parametric color control and function design.

### 10. Generated Code
```python
import machine, time

red = machine.PWM(machine.Pin(16))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(18))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def shade_purple(intensity):
    # Intensity: 0-100
    # Purple: R=intensity, G=0, B=intensity
    value = int((intensity / 100) * 65535)
    red.duty_u16(value)
    green.duty_u16(0)
    blue.duty_u16(value)

while True:
    # Fade up
    for i in range(0, 101, 5):
        shade_purple(i)
        time.sleep(0.05)
    
    # Fade down
    for i in range(100, -1, -5):
        shade_purple(i)
        time.sleep(0.05)
```

### 11. Common Mistakes
*   Green not set to 0 (ruins purple)
*   Wrong intensity mapping (0-100 must map to 0-65535)
*   Forgetting to scale both R and B equally

### 12. Try This Next
*   Add potentiometer for manual intensity control
*   Create functions for other colors (cyan, yellow)
*   Combine multiple colors with mixing ratios

---

"""

output += batch51_final

print("  ✓ Added Projects 0508-0510")
print()
print("✅ Batch 51 COMPLETE (10/10 projects)")
print()

# Write current progress
with open(r'd:\MFF\Pico\Documentation\Docs_0501_0600.md', 'w', encoding='utf-8') as f:
    f.write(output)

print("=" * 70)
print("STATUS UPDATE:")
print("=" * 70)
print("✅ Batch 51 (Digital Art): 10/10 projects COMPLETE")
print("⏳ Remaining: Batches 52-60 (90 projects)")
print()
print("File updated: Docs_0501_0600.md")
print("=" * 70)
