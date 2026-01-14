# Generate Pass 2 Completion: Batches 35-36 (Projects 0341-0360)
# Following locked Elite template with comprehensive Snap instructions

print("🚀 Generating Pass 2 Completion: Batches 35-36")
print("Projects 0341-0360 (Smart Fan 2 + Robotic Arm 2)")
print("Note: 20 projects with full Elite compliance")

batch_35_36_content = '''

---

# 🏁 Batch 35: Smart Fan 2

## 1️⃣ Project 0341: Introduction to Smart Fan

### 2️⃣ Learning Objective
Control motor direction using H-Bridge to create bidirectional airflow. You will learn how to reverse DC motor polarity for forward/backward operation.

### 3️⃣ Concepts Introduced
*   **H-Bridge**: Circuit allowing motor direction reversal.
*   **Bidirectional Control**: Forward and reverse motor operation.
*   **Direction Pins**: Using logic signals to control motor polarity.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Fan Motor**
*   **H-Bridge** (L298N or similar)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **H-Bridge IN1** | GP14 | Direction control A |
| **H-Bridge IN2** | GP15 | Direction control B |
| **H-Bridge ENA** | GP13 | PWM Enable (speed) |

### 6️⃣ Blocks Used

🔹 **Setup PWM & Pin**
*   **Category:** Outputs

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   None (direct control).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Outputs**, drag `Setup PWM pin:[13]`.
        *   **Snap** into setup block.
        *   Set frequency to **1000** Hz.
    *   From **Outputs**, drag `Setup Pin:[14] as OUTPUT`.
        *   **Snap** into setup block.
    *   From **Outputs**, drag `Setup Pin:[15] as OUTPUT`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Forward (Push Air)**:
        *   From **Pin Access**, drag `set Pin [14] to [HIGH]`.
            *   **Snap** into loop.
        *   From **Pin Access**, drag `set Pin [15] to [LOW]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[65535]`.
            *   **Snap** below (full speed).
        *   From **Timing**, drag `sleep [2] seconds`.
            *   **Snap** below.
    *   **Reverse (Pull Air)**:
        *   From **Pin Access**, drag `set Pin [14] to [LOW]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `set Pin [15] to [HIGH]`.
            *   **Snap** below.
        *   From **Pin Access**, drag `PWM Write pin:[13] freq:[1000] duty:[65535]`.
            *   **Snap** below (full speed).
        *   From **Timing**, drag `sleep [2] seconds`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The Pico controls an H-Bridge to reverse fan direction. Setting IN1=HIGH and IN2=LOW makes the fan push air (forward). Setting IN1=LOW and IN2=HIGH reverses motor polarity, making the fan pull air (backward). The enable pin (ENA) controls speed via PWM. This 4-second cycle demonstrates bidirectional motor control essential for robotics and HVAC applications.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

ena = machine.PWM(machine.Pin(13))
in1 = machine.Pin(14, machine.Pin.OUT)
in2 = machine.Pin(15, machine.Pin.OUT)

ena.freq(1000)

while True:
    # Forward
    in1.high()
    in2.low()
    ena.duty_u16(65535)
    time.sleep(2)
    
    # Reverse
    in1.low()
    in2.high()
    ena.duty_u16(65535)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Motor Doesn't Reverse**: Verify H-Bridge connections. IN1/IN2 control direction, ENA controls speed.
*   **Weak Airflow**: Check power supply. Fans need adequate current (often >500mA). Pico supplies 3.3V logic, but motor needs external power (5-12V).
*   **Both Pins HIGH**: Never set both IN1 and IN2 HIGH simultaneously - this creates a short circuit in the H-Bridge.

### 1️⃣2️⃣ Try This Next

*   **Variable Speed**: Add potentiometer to control PWM duty cycle (fan speed).
*   **Brake Mode**: Set both IN1 and IN2 LOW to brake motor quickly.
*   **Automated Ventilation**: Reverse direction every 30 seconds for room air circulation.

---

[Continuing with Projects 0342-0360...]
'''

with open(r'd:\MFF\Pico\Documentation\Docs_0301_0400.md', 'a', encoding='utf-8') as f:
    f.write(batch_35_36_content)

print("✅ Project 0341 (Introduction to Smart Fan) appended")
print("⏳ Note: Remaining 19 projects (0342-0360) require ~7,500 lines")
print("   Estimated: 4-5 responses to complete Pass 2")
print("\\nStrategy: Generate in batches for quality control:")
print("  - Batch 35 remainder: 0342-0350 (9 projects)")
print("  - Batch 36: 0351-0360 (10 projects)")
