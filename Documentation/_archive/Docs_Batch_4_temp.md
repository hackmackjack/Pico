
# 🏁 Batch 4: Simple Motors 1

## 1️⃣ Project 0031: Introduction to Simple Motors
### 2️⃣ Learning Objective
Learn to drive a high-current load. You will connect a DC Motor to the Pico using a driver (transistor/module), understanding why a microcontroller cannot drive a motor directly (current limits).

### 3️⃣ Concepts Introduced
*   **Current Handling**: GPIOs are weak (20mA). Motors are hungry (200mA+).
*   **Driver/Transistor**: An electronic switch.

### 4️⃣ Hardware Required
*   **Pico**
*   **DC Motor** (with Fan)
*   **Motor Driver** (L9110 or Transistor)
*   **External Power** (if motor is >5V, otherwise 5V VBUS)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Driver IN-A** | GP14 |
| **Driver VCC** | VBUS (5V) |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [14] to [HIGH]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Set Pin 14 HIGH (Spin).
    *   Wait 3s.
    *   Set Pin 14 LOW (Stop).
    *   Wait 3s.

### 9️⃣ Execution Flow (Plain English)
The Pico signals the Driver: "Turn on!". The Driver opens the floodgates from the battery to the motor. The fan spins. The Pico says "Stop!", and the Driver cuts the power.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

motor = machine.Pin(14, machine.Pin.OUT)

while True:
    motor.value(1) # Spin
    time.sleep(3)
    motor.value(0) # Stop
    time.sleep(3)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Direct Connection**: NEVER connect a motor directly to a Pico pin. It will burn out the pin or the whole chip. Always use a driver or transistor.

### 1️⃣2️⃣ Try This Next
*   **Kickstart**: Sometimes motors need a push. Try a short 0.1s burst if it sticks.

---

## 1️⃣ Project 0032: Blinking Simple Motors (Vibration)
### 2️⃣ Learning Objective
Pulse a motor effectively. You will turn a motor on and off rapidly to create haptic feedback (vibration), similar to a phone notification.

### 3️⃣ Concepts Introduced
*   **Haptics**: Communicating via touch.
*   **Inertia**: Motors don't stop instantly.

### 4️⃣ Hardware Required
*   **Pico**
*   **Vibration Motor** (or standard motor with offset weight)
*   **Driver**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Driver** | GP14 |

### 6️⃣ Blocks Used
🔹 **Wait**
*   **Category:** Timing
*   **Block:** `sleep [0.5] s`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Motor ON. Wait 0.5s.
    *   Motor OFF. Wait 0.5s.

### 9️⃣ Execution Flow (Plain English)
The motor spins up briefly, shaking the device, then spins down. Repeating this creates a "Bzzt... Bzzt..." feeling.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
motor = machine.Pin(14, machine.Pin.OUT)

while True:
    motor.value(1)
    time.sleep(0.5)
    motor.value(0)
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Flyback Diode**: If building raw circuits, remember a diode across the motor to protect the Pico from voltage spikes when the motor stops.

### 1️⃣2️⃣ Try This Next
*   **Pattern**: SOS vibration (... --- ...).

---

## 1️⃣ Project 0033: Manual Motor Control (Fan)
### 2️⃣ Learning Objective
User-controlled actuation. The fan runs only when the button is held.

### 3️⃣ Concepts Introduced
*   **Deadman Switch**: Action only on hold.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Motor + Driver**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Driver** | GP14 |

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic
*   **Block:** `if [Button] then [Motor ON] else [Motor OFF]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button: Motor ON.
    *   ELSE: Motor OFF.

### 9️⃣ Execution Flow (Plain English)
Press button -> Wind blows. Release button -> Wind stops.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.Pin(14, machine.Pin.OUT)

while True:
    if btn.value():
        motor.value(1)
    else:
        motor.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Power**: If the fan slows down when button is held, your USB power might be weak.

### 1️⃣2️⃣ Try This Next
*   **Latch**: Click to turn on, Click again to turn off.

---

## 1️⃣ Project 0034: Simple Motors Sequences (Variable Speed)
### 2️⃣ Learning Objective
Control motor speed using Software. You will cycle through Low, Medium, and High speeds using PWM.

### 3️⃣ Concepts Introduced
*   **PWM (Pulse Width Modulation)**: Simulating lower voltage by pulsing fast.
*   **Duty Cycle**: % of time the power is ON.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Motor + Driver** (Must support PWM)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Driver** | GP14 |

### 6️⃣ Blocks Used
🔹 **Analog Write**
*   **Category:** Pin Access
*   **Block:** `analog write Pin [14] to [X]`

### 7️⃣ Variables & State
*   **speedLevel**: 0-3.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Clicked: `speedLevel` += 1. (Wrap if >3).
    *   **Apply**:
        *   Level 0: PWM 0 (Stop).
        *   Level 1: PWM 20000 (Low).
        *   Level 2: PWM 40000 (Med).
        *   Level 3: PWM 65535 (Max).

### 9️⃣ Execution Flow (Plain English)
The user clicks to cycle speeds. The Pico sends a signal that is "mostly off" for Low speed, "half on" for Medium, and "fully on" for High. The motor averages this out and spins at different rates.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.PWM(machine.Pin(14))
motor.freq(100) # 100Hz is good for DC motors
level = 0

while True:
    if btn.value():
        level += 1
        if level > 3: level = 0
        
        # Set Speed
        if level == 0: motor.duty_u16(0)
        if level == 1: motor.duty_u16(20000)
        if level == 2: motor.duty_u16(40000)
        if level == 3: motor.duty_u16(65535)
        
        time.sleep(0.3) # Debounce
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Stall**: At low PWM (e.g. 5000), the motor might hum but not spin. Increase the minimum value until it moves.

### 1️⃣2️⃣ Try This Next
*   **Ramp**: Hold button to smoothly accelerate.

---

## 1️⃣ Project 0035: Interactive Motors (Direction)
### 2️⃣ Learning Objective
Control direction. You will use an **H-Bridge** driver to spin basic motors Forward and Backward.

### 3️⃣ Concepts Introduced
*   **H-Bridge**: A circuit that can reverse polarity.
*   **Logic States**: A=High, B=Low (Fwd); A=Low, B=High (Rev).

### 4️⃣ Hardware Required
*   **Pico**
*   **H-Bridge Driver** (L9110s or L298N)
*   **DC Motor**
*   **2 Buttons**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Driver IA** | GP14 |
| **Driver IB** | GP15 |
| **Btn Fwd** | GP10 |
| **Btn Rev** | GP11 |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [14] to [High]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF BtnFwd: Pin 14 HIGH, Pin 15 LOW.
    *   ELSE IF BtnRev: Pin 14 LOW, Pin 15 HIGH.
    *   ELSE: Pin 14 LOW, Pin 15 LOW (Coast/Stop).

### 9️⃣ Execution Flow (Plain English)
To go forward, we push current from A to B. To go backward, we push from B to A. If we pull both to Ground, the motor stops.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

ia = machine.Pin(14, machine.Pin.OUT)
ib = machine.Pin(15, machine.Pin.OUT)
btnF = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnR = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btnF.value():
        ia.value(1)
        ib.value(0)
    elif btnR.value():
        ia.value(0)
        ib.value(1)
    else:
        ia.value(0)
        ib.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Short Circuit**: Never set BOTH High (IA=1, IB=1) if your driver doesn't support braking. It might short the supply on cheap drivers (Shoot-through).

### 1️⃣2️⃣ Try This Next
*   **Brake**: Set both High (if supported) to stop instantly instead of coasting.

---

## 1️⃣ Project 0036: Smart Motor Switch (Garage Door)
### 2️⃣ Learning Objective
Automate duration control. The motor runs for a fixed time then stops, simulating a garage door interacting with a limit (time-based limit).

### 3️⃣ Concepts Introduced
*   **Open Loop Control**: Assuming the door opens in X seconds without verifying position.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Motor**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Motor** | GP14 |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [14] to [High]`

### 7️⃣ Variables & State
*   **isOpening**: Boolean.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button and `not isOpening`:
        *   `isOpening` = True.
        *   Motor ON.
        *   Wait 5s.
        *   Motor OFF.
        *   `isOpening` = False.

### 9️⃣ Execution Flow (Plain English)
One click triggers the entire 5-second sequence. You don't need to hold the button. The system takes over until the task is done.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.Pin(14, machine.Pin.OUT)
isOpening = False

while True:
    if btn.value() and not isOpening:
        isOpening = True
        motor.value(1)
        time.sleep(5)
        motor.value(0)
        isOpening = False
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **No Stop**: If power fails mid-open, it stops. When power returns, it doesn't know where the door is (limitation of Open Loop).

### 1️⃣2️⃣ Try This Next
*   **Abort**: Allow button press to STOP the door mid-move.

---

## 1️⃣ Project 0037: Motor Alarm (Intruder Spray)
### 2️⃣ Learning Objective
Trigger mechanical action from sensors. Connect a PIR (Motion) sensor to a pump/fan.

### 3️⃣ Concepts Introduced
*   **Interfacing**: Connecting Input logic to Output power.
*   **Dwell Time**: Keeping the output on for a minimum time after trigger.

### 4️⃣ Hardware Required
*   **Pico**
*   **PIR Sensor**
*   **Motor/Pump**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **PIR** | GP16 |
| **Motor** | GP14 |

### 6️⃣ Blocks Used
🔹 **If**
*   **Category:** Logic
*   **Block:** `if [PIR High]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF PIR Detected:
        *   Motor ON.
        *   Wait 2s (Spray duration).
        *   Motor OFF.

### 9️⃣ Execution Flow (Plain English)
The PIR detects body heat. It sends a signal. The Pico receives it and activates the "Trap" (Motor) for 2 seconds, then resets to waiting mode.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

pir = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.Pin(14, machine.Pin.OUT)

while True:
    if pir.value():
        motor.value(1)
        time.sleep(2)
        motor.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **False Triggers**: PIR sensors need 30-60s to stabilize after power on. They might fire randomly at startup.

### 1️⃣2️⃣ Try This Next
*   **Cooldwon**: Don't spray again for 10 seconds.

---

## 1️⃣ Project 0038: The Motor Game (Spin the Wheel)
### 2️⃣ Learning Objective
Random actuation. Spin a wheel for a random duration to select a winner.

### 3️⃣ Concepts Introduced
*   **Random Duration**: `sleep(random)`.
*   **Deceleration**: (Advanced) simulated friction.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Motor** with Pointer/Wheel

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP10 |
| **Motor** | GP14 |

### 6️⃣ Blocks Used
🔹 **Random**
*   **Category:** Math
*   **Block:** `random value`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button:
        *   Calc `spinTime` = Random(1.0, 4.0).
        *   Motor ON.
        *   Wait `spinTime`.
        *   Motor OFF.

### 9️⃣ Execution Flow (Plain English)
You press the button. The wheel spins. It stops after a random time, pointing to a random slice of the pie.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
import random

btn = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.Pin(14, machine.Pin.OUT)

while True:
    if btn.value():
        spinTime = random.uniform(1.0, 4.0)
        motor.value(1)
        time.sleep(spinTime)
        motor.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Friction**: DC motors stop quickly due to friction, but not instantly. The wheel will coast a bit.

### 1️⃣2️⃣ Try This Next
*   **Ease-Out**: Reduce PWM speed gradually at the end for a realistic "click-click-click... stop" effect.

---

## 1️⃣ Project 0039: Automated Motor (Smart Cooling)
### 2️⃣ Learning Objective
Closed-loop control (Bang-Bang). Turn a fan on if temperature exceeds a limit.

### 3️⃣ Concepts Introduced
*   **Thermostat Logic**: Basic feedback loop.
*   **Hysteresis**: Preventing rapid on/off cycling.

### 4️⃣ Hardware Required
*   **Pico**
*   **Internal Temp Sensor** (or DHT11)
*   **Motor/Fan**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Motor** | GP14 |

### 6️⃣ Blocks Used
🔹 **Internal Temp**
*   **Category:** Sensors
*   **Block:** `read Temperature`

### 7️⃣ Variables & State
*   **temp**: Celsius.

### 8️⃣ Block Logic
*   **Loop**:
    *   Read Temp.
    *   IF Temp > 25: Fan ON.
    *   IF Temp < 24: Fan OFF.

### 9️⃣ Execution Flow (Plain English)
If it's hot (25+), fan runs. It stays running until it cools down to 24. This 1-degree gap prevents the fan from flickering on/off rapidly at 25.0 degrees.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

sensor = machine.ADC(4)
motor = machine.Pin(14, machine.Pin.OUT)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706)/0.001721
    
    if temp > 25:
        motor.value(1)
    elif temp < 24:
        motor.value(0)
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Calculation**: The internal temp sensor math is tricky. Ensure you use the formula for RP2040.

### 1️⃣2️⃣ Try This Next
*   **Proportional**: The hotter it is, the faster the fan spins (PWM).

---

## 1️⃣ Project 0040: Mastering Motors (Soft Start)
### 2️⃣ Learning Objective
Protect mechanical parts from stress. Ramp up speed slowly instead of jumping to 100%.

### 3️⃣ Concepts Introduced
*   **Ramping**: Changing value linearly over time.
*   **For Loops**: Iteration.

### 4️⃣ Hardware Required
*   **Pico**
*   **Motor + PWM Driver**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Motor** | GP14 |

### 6️⃣ Blocks Used
🔹 **For Loop**
*   **Category:** Loops
*   **Block:** `for i from 0 to 65000`

### 7️⃣ Variables & State
*   **i**: Duty Cycle.

### 8️⃣ Block Logic
*   **Init**: Motor Stop.
*   **Loop**:
    *   Wait 2s.
    *   **Ramp Up**: For i = 0 to 65535 (Step 1000):
        *   Set PWM = i.
        *   Wait 0.05s.
    *   Wait 2s at full speed.
    *   Stop.

### 9️⃣ Execution Flow (Plain English)
The motor whines, then slowly starts rotating, picking up speed over 3 seconds until it hits max RPM. This mimics how elevators and trains start smoothly.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

motor = machine.PWM(machine.Pin(14))
motor.freq(100)

while True:
    time.sleep(2)
    # Ramp Up
    for i in range(0, 65535, 1000):
        motor.duty_u16(i)
        time.sleep(0.05)
    
    time.sleep(2)
    motor.duty_u16(0) # Hard Stop
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Step Size**: If step is too large, it jumps. If too small, it takes forever.

### 1️⃣2️⃣ Try This Next
*   **Soft Stop**: Ramp down as well.

---
