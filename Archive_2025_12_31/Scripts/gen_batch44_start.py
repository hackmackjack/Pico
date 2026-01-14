# Remove placeholders and generate Batch 44 FULL Elite documentation

target_file = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'

# Read and remove placeholder content after Batch 43
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find where Batch 43 ends
batch43_end_marker = "✅ **BATCH 43 COMPLETE: Projects 0421-0430 (Sound & Music 3)**"

if batch43_end_marker in content:
    # Keep everything up to and including Batch 43 completion
    content = content.split(batch43_end_marker)[0] + batch43_end_marker + "\n\n---\n\n"
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Removed placeholder content")
    print("📋 Ready to generate Batch 44 with full Elite documentation")
else:
    print("⚠️  Batch 43 marker not found, proceeding anyway")

# Now generate Batch 44
batch44_content = r'''
# 🏁 Batch 44: Simple Motors 3

---

## 1️⃣ Project 0431: Introduction to Simple Motors

### 2️⃣ Learning Objective
Implement smooth motor deceleration instead of abrupt stopping. You will learn about ramped speed reduction and controlled braking.

### 3️⃣ Concepts Introduced
*   **Slow Stop**: Gradual speed reduction (100→0).
*   **Ramped Deceleration**: Decreasing PWM duty cycle incrementally.
*   **Controlled Braking**: Smooth stop for mechanical safety.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Motor**
*   **Motor Driver** (L293D or similar)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Motor Enable (PWM)** | GP15 | Speed control |
| **Motor IN1** | GP16 | Direction control |
| **Motor IN2** | GP17 | Direction control |

### 6️⃣ Blocks Used

🔹 **PWM Control**
*   **Category:** Pin Access

🔹 **For Loop**
*   **Category:** Loops

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **speed**: Current motor speed (0-100%).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[15] as PWM`.
        *   **Snap** into setup block.
    *   From **Pin Access**, drag `Setup Pin:[16,17] as OUTPUT`.
        *   **Snap** below.
    *   From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
        *   **Snap** below (set direction forward).
    *   From **Pin Access**, drag `digital write pin:[17] value:[LOW]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Start at Full Speed**:
        *   From **PWM**, drag `set PWM duty cycle pin:[15] to [100%]`.
            *   **Snap** into loop.
        *   From **Timing**, drag `sleep [3] seconds`.
            *   **Snap** below (run at full speed).
    *   **Ramp Down**:
        *   From **Loops**, drag `for [speed] from [100] to [0] step [-20]`.
            *   **Snap** below.
            *   Inside:
                *   From **PWM**, drag `set PWM duty cycle pin:[15] to [speed%]`.
                    *   **Snap** inside.
                *   From **Console**, drag `print [Speed: {speed}%]`.
                    *   **Snap** below.
                *   From **Timing**, drag `sleep [0.2] seconds`.
                    *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The motor starts at 100% speed for 3 seconds. Then it decelerates in steps: 100%→80%→60%→40%→20%→0%. Each step lasts 0.2 seconds, creating a smooth 1-second deceleration. This prevents sudden mechanical stress and extends motor lifetime.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

enable_pwm = machine.PWM(machine.Pin(15))
enable_pwm.freq(1000)
in1 = machine.Pin(16, machine.Pin.OUT)
in2 = machine.Pin(17, machine.Pin.OUT)

# Set direction (forward)
in1.on()
in2.off()

# Full speed
enable_pwm.duty_u16(65535)
time.sleep(3)

# Ramp down
for speed in range(100, -1, -20):
    duty = int((speed / 100) * 65535)
    enable_pwm.duty_u16(duty)
    print(f"Speed: {speed}%")
    time.sleep(0.2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Motor Doesn't Stop**: Ensure final PWM duty is 0, not just "low".
*   **Jerky Motion**: Decrease step size to -10 for smoother deceleration.

### 1️⃣2️⃣ Try This Next

*   **Exponential Decay**: Use `speed = 100 * e^(-t)` for natural deceleration curve.
*   **Acceleration**: Add ramp-up from 0→100% on startup.

---

## 1️⃣ Project 0432: Blinking Simple Motors

### 2️⃣ Learning Objective
Create haptic feedback patterns using vibration motor pulses. You will learn about tactile messaging and pulse-width encoding.

### 3️⃣ Concepts Introduced
*   **Haptic Pattern**: Tactile communication through vibration.
*   **Pulse Encoding**: 2 short buzzes vs 1 long buzz for different alerts.
*   **Tactile Messaging**: Non-audio notification method.

### 4️⃣ Hardware Required
*   **Pico**
*   **Vibration Motor** (coin or cylinder type)
*   **Transistor** (for switching)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Vibration Motor** | GP15 | Via transistor |

### 6️⃣ Blocks Used

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Repeat Loop**
*   **Category:** Loops

🔹 **Sleep**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **alertType**: "message" or "call".

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Pin Access**, drag `Setup Pin:[15] as OUTPUT`.
        *   **Snap** into setup block.

*   **B. Main Loop Phase**
    *   **Message Alert (2 short buzzes)**:
        *   From **Variables**, drag `set [alertType] to ["message"]`.
            *   **Snap** into loop.
        *   From **Logic**, drag `if [alertType] = ["message"] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Loops**, drag `repeat [2] times`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Pin Access**, drag `digital write pin:[15] value:[HIGH]`.
                            *   **Snap** inside.
                        *   From **Timing**, drag `sleep [0.2] seconds`.
                            *   **Snap** below.
                        *   From **Pin Access**, drag `digital write pin:[15] value:[LOW]`.
                            *   **Snap** below.
                        *   From **Timing**, drag `sleep [0.2] seconds`.
                            *   **Snap** below.
    *   **Call Alert (1 long buzz)**:
        *   From **Logic**, drag `else`.
            *   **Snap** below.
            *   Inside:
                *   From **Pin Access**, drag `digital write pin:[15] value:[HIGH]`.
                *   From **Timing**, drag `sleep [1] seconds`.
                *   From **Pin Access**, drag `digital write pin:[15] value:[LOW]`.

### 9️⃣ Execution Flow (Plain English)

For a message notification, the vibration motor pulses twice (0.2s on, 0.2s off, 0.2s on, 0.2s off). For a call, it vibrates once continuously for 1 second. Users can distinguish notification types by the haptic pattern without looking at the device.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

vibe_motor = machine.Pin(15, machine.Pin.OUT)

alert_type = "message"  # or "call"

if alert_type == "message":
    # 2 short buzzes
    for _ in range(2):
        vibe_motor.on()
        time.sleep(0.2)
        vibe_motor.off()
        time.sleep(0.2)
else:
    # 1 long buzz
    vibe_motor.on()
    time.sleep(1)
    vibe_motor.off()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Weak Vibration**: Ensure transistor can handle motor current (typically 50-100mA).
*   **Patterns Feel Same**: Increase difference (3 short vs 2 long, for example).

### 1️⃣2️⃣ Try This Next

*   **Morse Code Vibration**: Encode short messages in Morse via haptic pulses.
*   **Customizable Patterns**: Let user record their own vibration patterns.

---

(Continuing with remaining Batch 44 projects 0433-0440...)

✅ **BATCH 44 IN PROGRESS**

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch44_content)

print("✅ Generated Batch 44 start (Projects 0431-0432)")
print("📋 Continuing with remaining projects 0433-0440...")
