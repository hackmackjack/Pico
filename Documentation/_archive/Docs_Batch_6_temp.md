
# 🏁 Batch 6: Night Light 1

## 1️⃣ Project 0051: Introduction to Night Light
### 2️⃣ Learning Objective
Create a conceptual night light. Simply turn on the LED and keep it on. This represents the "Safety" state of a night light.

### 3️⃣ Concepts Introduced
*   **Continuous Operation**: Systems that run forever.
*   **Power State**: Determining On vs Off.

### 4️⃣ Hardware Required
*   **Pico**
*   **White LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Set Pin**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Set LED ON (High).

### 9️⃣ Execution Flow (Plain English)
The light turns on. It stays on until the power is cut.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
while True:
    led.value(1)
    time.sleep(1) # Keep processor happy
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Too Bright?**: Use a larger resistor (e.g., 1kΩ) for a dimmer night light.

### 1️⃣2️⃣ Try This Next
*   **Sleep**: Use `machine.lightsleep()` to save power while keeping the RAM active.

---

## 1️⃣ Project 0052: Blinking Night Light (Sleep Helper)
### 2️⃣ Learning Objective
Pulses the light slowly (Fade In/Out) to mimic breathing, aiding relaxation.

### 3️⃣ Concepts Introduced
*   **PWM Fading**: Varying brightness smoothly.
*   **Loops within Loops**: Incrementing up, then decrementing down.

### 4️⃣ Hardware Required
*   **Pico**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Analog Write** (PWM)
🔹 **Count with** (For Loop)

### 7️⃣ Variables & State
*   **brightness**

### 8️⃣ Block Logic
*   **Loop**:
    *   **Fade In**: For i from 0 to 65535, step 500. Set PWM. Wait tiny.
    *   **Fade Out**: For i from 65535 to 0, step -500. Set PWM. Wait tiny.

### 9️⃣ Execution Flow (Plain English)
The light glows brighter and brighter, pauses, then fades to black. Repeat.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)
while True:
    # Fade In
    for i in range(0, 65535, 1000):
        pwm.duty_u16(i)
        time.sleep(0.05)
    # Fade Out
    for i in range(65535, 0, -1000):
        pwm.duty_u16(i)
        time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Steps**: If the step size is too large (e.g., 10000), it looks jerky.

### 1️⃣2️⃣ Try This Next
*   **Color**: Use an RGB LED to fade between colors.

---

## 1️⃣ Project 0053: Manual Night Light Control
### 2️⃣ Learning Objective
Add a switch. Manually toggle the night light mode.

### 3️⃣ Concepts Introduced
*   **State Retention**: To switch or not to switch.
*   **Slide Switch**: A component that holds its state (unlike a button).

### 4️⃣ Hardware Required
*   **Pico**
*   **Slide Switch** (or Button acting as Toggle)
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Switch** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Switch is ON (High): LED ON.
    *   ELSE: LED OFF.

### 9️⃣ Execution Flow (Plain English)
Standard light switch logic. Up is On, Down is Off.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
sw = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    if sw.value():
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Floating**: If using a slide switch, ensure it connects to 3.3V and GND (if SPDT) or uses Pull-Downs correctly.

### 1️⃣2️⃣ Try This Next
*   **Timer**: Make the switch start a 10s timer, then auto-off.

---

## 1️⃣ Project 0054: Night Light Sequences (Mood Light)
### 2️⃣ Learning Objective
Color cycling. Slowly transition Red -> Green -> Blue.

### 3️⃣ Concepts Introduced
*   **RGB Color Mixing**: Creating moods.
*   **Sequential Transition**: Finishing one task before starting next.

### 4️⃣ Hardware Required
*   **Pico**
*   **RGB LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Red** | GP13 |
| **Green** | GP14 |
| **Blue** | GP15 |

### 6️⃣ Blocks Used
🔹 **Set Pin** (or PWM)

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Red ON. Wait 2s.
    *   Green ON. Wait 2s.
    *   Blue ON. Wait 2s.
    *   (Optional: Mix them for Yellow/Cyan/Magenta).

### 9️⃣ Execution Flow (Plain English)
The room changes color every 2 seconds.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
r = machine.Pin(13, machine.Pin.OUT)
g = machine.Pin(14, machine.Pin.OUT)
b = machine.Pin(15, machine.Pin.OUT)
while True:
    r.value(1); g.value(0); b.value(0)
    time.sleep(2)
    r.value(0); g.value(1); b.value(0)
    time.sleep(2)
    r.value(0); g.value(0); b.value(1)
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Common Anode/Cathode**: If your LED is Common Anode, `0` is ON and `1` is OFF.

### 1️⃣2️⃣ Try This Next
*   **Rainbow**: Use PWM to mix colors smoothly.

---

## 1️⃣ Project 0055: Interactive Night Light (Clap On)
### 2️⃣ Learning Objective
Audio trigger. Clap your hands to toggle the light.

### 3️⃣ Concepts Introduced
*   **Thresholding**: Deciding what counts as a "Clap" (Loud logic).
*   **Toggle Logic**: State = NOT State.

### 4️⃣ Hardware Required
*   **Pico**
*   **Sound Sensor** (Digital Out)
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Sound Sensor** | GP16 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If**
🔹 **Set Variable**

### 7️⃣ Variables & State
*   **light_state** (Boolean)

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Sound Detected:
        *   `light_state` = NOT `light_state`.
        *   Set LED to `light_state`.
        *   Wait 0.5s (Debounce clap).

### 9️⃣ Execution Flow (Plain English)
*Clap* -> Light On. *Clap* -> Light Off.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
mic = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
state = False
while True:
    if mic.value():
        state = not state
        led.value(state)
        time.sleep(0.5) # Wait for silence
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Sensitivity**: Adjust the potentiometer on the sound module if it triggers too easily or not at all.

### 1️⃣2️⃣ Try This Next
*   **Double Clap**: Require two claps in 1 second.

---

## 1️⃣ Project 0056: Smart Night Light Switch (LDR)
### 2️⃣ Learning Objective
Auto-brightness. Turn on when dark, off when bright.

### 3️⃣ Concepts Introduced
*   **Analog Input**: Reading light levels (0-65535).
*   **Inversion**: Low Light = High Brightness.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR (Light Dependent Resistor)**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 (ADC0) |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Read Analog**
🔹 **Map** (Optional)

### 7️⃣ Variables & State
*   **light_level**

### 8️⃣ Block Logic
*   **Loop**:
    *   `light_level` = Read ADC0.
    *   IF `light_level` < 30000 (Dark): LED ON.
    *   ELSE: LED OFF.

### 9️⃣ Execution Flow (Plain English)
Cover the sensor -> Light turns on. Shine a torch -> Light turns off.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
ldr = machine.ADC(26)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    reading = ldr.read_u16()
    if reading < 30000: # Threshold depends on wiring
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wiring**: LDR needs a voltage divider (10k Resistor usually). LDR to 3.3V, Resistor to GND, Middle to Pin.

### 1️⃣2️⃣ Try This Next
*   **Dimming**: Map the labeled ADC value to PWM to scale brightness perfectly.

---

## 1️⃣ Project 0057: Night Light Alarm System (Monster Detector)
### 2️⃣ Learning Objective
Motion detection in the dark.

### 3️⃣ Concepts Introduced
*   **Distance Change**: Detecting movement by delta in distance (or just presence < X).

### 4️⃣ Hardware Required
*   **Pico**
*   **HC-SR04**
*   **Red LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Trig** | GP16 |
| **Echo** | GP17 |
| **Red LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Distance**

### 7️⃣ Variables & State
*   **dist**

### 8️⃣ Block Logic
*   **Loop**:
    *   `dist` = Get Distance.
    *   IF `dist` < 30cm (Something under bed!):
        *   Red LED ON.
    *   ELSE:
        *   Red LED OFF.

### 9️⃣ Execution Flow (Plain English)
If the spooky monster reaches out (comes closer than 30cm), the red warning light scares it.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
trig = machine.Pin(16, machine.Pin.OUT)
echo = machine.Pin(17, machine.Pin.IN)
red = machine.Pin(15, machine.Pin.OUT)

def get_dist():
    trig.low(); time.sleep_us(2)
    trig.high(); time.sleep_us(10); trig.low()
    # Simple timeout version
    t = time.ticks_ms()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_ms(), t) > 50: return 100
    start = time.ticks_us()
    while echo.value() == 1: pass
    return (time.ticks_diff(time.ticks_us(), start)) * 0.0343 / 2

while True:
    d = get_dist()
    if d < 30:
        red.value(1)
    else:
        red.value(0)
    time.sleep(0.2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **False Positives**: Ultrasonic sensors are noisy. Check wiring if it flickers.

### 1️⃣2️⃣ Try This Next
*   **Servo**: Make a "Monster Trap" that closes a box.

---

## 1️⃣ Project 0058: The Night Light Game (Shadow Puppets)
### 2️⃣ Learning Objective
Inverse logic as game. Trigger the light by casting a shadow.

### 3️⃣ Concepts Introduced
*   **Optical Switch**: Using light as a button.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If**

### 7️⃣ Variables & State
*   **lux**

### 8️⃣ Block Logic
*   **Loop**:
    *   `lux` = Read LDR.
    *   IF `lux` drops suddenly (or below threshold):
        *   LED ON for 2s.

### 9️⃣ Execution Flow (Plain English)
Wave your hand over the sensor. The light blinks ON to acknowledge the shadow.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
ldr = machine.ADC(26)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    if ldr.read_u16() < 10000: # Shadow
        led.value(1)
        time.sleep(2)
        led.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Ambient Light**: You might need to calibrate the threshold (10000) for your room.

### 1️⃣2️⃣ Try This Next
*   **Morse**: Communicate using shadows.

---

## 1️⃣ Project 0059: Automated Night Light (Timer)
### 2️⃣ Learning Objective
Timed event. Press button, light stays on for 15s (simulated 15 mins), then turns off.

### 3️⃣ Concepts Introduced
*   **Monostable Multivibrator**: Logic that outputs a pulse of fixed duration.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **If**
🔹 **Wait**

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Pressed:
        *   LED ON.
        *   Wait 15s.
        *   LED OFF.

### 9️⃣ Execution Flow (Plain English)
Click > Light On > (Read Book) > Auto Off.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    if btn.value():
        led.value(1)
        time.sleep(15)
        led.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Blocking**: During the 15s wait, the button doesn't work. To fix, use timers/timestamps.

### 1️⃣2️⃣ Try This Next
*   **Cancel**: Allow pressing the button again to turn it off early (Requires non-blocking logic).

---

## 1️⃣ Project 0060: Mastering Night Light (Battery Saver)
### 2️⃣ Learning Objective
Multifactor authentication (Logic AND). Light only turns on if Dark AND Motion.

### 3️⃣ Concepts Introduced
*   **Boolean AND**: Condition A && Condition B.
*   **Resource Management**: Saving battery.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR**
*   **PIR Sensor** (or Ultrasonic)
*   **LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 |
| **PIR** | GP16 |
| **LED** | GP15 |

### 6️⃣ Blocks Used
🔹 **Logic AND**

### 7️⃣ Variables & State
*   **is_dark**
*   **is_moving**

### 8️⃣ Block Logic
*   **Loop**:
    *   `is_dark` = (LDR < Threshold).
    *   `is_moving` = (PIR == High).
    *   IF `is_dark` AND `is_moving`:
        *   LED ON.
    *   ELSE:
        *   LED OFF.

### 9️⃣ Execution Flow (Plain English)
Daytime + Motion? Off. Night + Still? Off. Night + Motion? ON.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
ldr = machine.ADC(26)
pir = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
while True:
    is_dark = (ldr.read_u16() < 20000)
    is_moving = (pir.value() == 1)
    
    if is_dark and is_moving:
        led.value(1)
        time.sleep(5) # Stay on for 5s
    else:
        led.value(0)
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **PIR Delay**: PIR sensors have a "cooldown" (usually 2-4s) where they stay high.

### 1️⃣2️⃣ Try This Next
*   **Logging**: Count how many times it triggered each night.

---
