
import os

def generate_batch_64_part1():
    header = """
# 🏁 Batch 64: Simple Motors 4

---
"""
    projects = []

    # 0631: Intro Motors (Relay)
    projects.append({
        "id": "0631",
        "title": "Introduction to Simple Motors",
        "objective": "Control a DC Motor using a Relay Module. Turn the motor on for 3 seconds and off for 3 seconds.",
        "concepts": ["High-Power Switching", "Relay Control", "Isolation", "On/Off Logic"],
        "hardware": ["Pico", "Relay Module", "DC Motor"],
        "interface": "| **Relay** | GP16 | Digital |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Init**: Setup Pin 16 Output.
**B. Loop**:
1.  **Cycle**:
  *   Turn GP16 On. Wait 3s.
  *   Turn GP16 Off. Wait 3s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Digital outputs (3.3V) can control huge loads (120V/10A) via a relay. The logic is identical to blinking an LED.",
        "code": """import machine, time
relay = machine.Pin(16, machine.Pin.OUT)

while True:
    relay.on()
    time.sleep(3)
    relay.off()
    time.sleep(3)""",
        "mistakes": ["**Inductive Kickback**: Always use a flyback diode if not using a module.", "**Clicking**: Mechanical relays life cycle is limited (100k clicks). Don't switch too fast."],
        "next": ["**Transistor**: Use MOSFET for faster switching.", "**Interlock**: Prevent two relays expanding at once."]
    })

    # 0632: Pulse Move
    projects.append({
        "id": "0632",
        "title": "Blinking Simple Motors",
        "objective": "Create an 'Inching' movement: Turn the motor on for very short bursts (0.1s) followed by a stop (0.5s).",
        "concepts": ["Pulse Control", "Inching/Jogging", "Mechanical Inertia", "Open Loop Control"],
        "hardware": ["Pico", "Motor Driver", "DC Motor"],
        "interface": "| **Motor** | GP16 | Driver Input |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Jog**:
  *   Turn Motor On. Wait 0.1s.
  *   Turn Motor Off. Wait 0.5s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Instead of continuous rotation, we push the motor in small increments. This is useful for feeders or conveyor belt alignment.",
        "code": """import machine, time
motor = machine.Pin(16, machine.Pin.OUT)

while True:
    motor.value(1)
    time.sleep(0.1)
    motor.value(0)
    time.sleep(0.5)""",
        "mistakes": ["**Stall Current**: Motor draws max current at start. Rapid pulsing heats the driver.", "**Kick**: The motor might not move at all if 0.1s is too short to overcome friction."],
        "next": ["**Ramp**: Smooth start.", "**Encoder**: Move exactly 10 degrees."]
    })

    # 0633: Servo Knob
    projects.append({
        "id": "0633",
        "title": "Manual Simple Motors Control",
        "objective": "Control a Servo Motor's angle (0-180 degrees) using a Potentiometer.",
        "concepts": ["Angular Position", "Analog Mapping", "Servo Pulse Width", "Human Interface"],
        "hardware": ["Pico", "Servo", "Potentiometer"],
        "interface": "| **Pot** | GP26 | Analog Input |\n| **Servo** | GP16 | PWM Output |",
        "blocks": ["*   **from Actuators, drag `servo_write`**", "*   **from Math, drag `map_range`**"],
        "vars": ["**angle**: Int"],
        "guide": """**A. Loop**:
1.  **Read**:
  *   `val` = Read Pot(26).
2.  **Map**:
  *   `angle` = Map `val` (0-65535) to (0-180).
3.  **Drive**:
  *   Set Servo(16) to `angle`.
  *   Wait 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The user turns the knob, the math converts the voltage to degrees, and the servo mimics the action.",
        "code": """import machine, time
pot = machine.ADC(26)
servo = machine.PWM(machine.Pin(16))
servo.freq(50)

def set_angle(angle):
    # Map 0-180 to 2500-7500 duty (approx for SG90)
    duty = int(2500 + (angle/180)*5000) 
    servo.duty_u16(duty)

while True:
    val = pot.read_u16()
    angle = int(val / 65535 * 180)
    set_angle(angle)
    time.sleep(0.05)""",
        "mistakes": ["**Jitter**: Noisy power supply causes servo to shake. Add capacitors.", "**Range**: Some servos go 0-270. Check datasheet."],
        "next": ["**Smoothing**: Average the pot readings.", "**Inverse**: Turn knob left, servo goes right."]
    })

    # 0634: Wiper
    projects.append({
        "id": "0634",
        "title": "Simple Motors Sequences",
        "objective": "Simulate a windshield wiper: Sweep servo 0->180, wait, sweep 180->0, wait.",
        "concepts": ["Reciprocating Motion", "For Loops", "Mechanical Linkage", "Cyclic Tasks"],
        "hardware": ["Pico", "Servo"],
        "interface": "| **Servo** | GP16 | PWM |",
        "blocks": ["*   **from Loops, drag `for_in_range`**", "*   **from Actuators, drag `servo_write`**"],
        "vars": ["**angle**: Int"],
        "guide": """**A. Loop**:
1.  **Sweep Up**:
  *   Count `angle` 0 to 180:
      *   Set Servo to `angle`. Wait 0.01s.
      *   **Snap** into loop.
2.  **Sweep Down**:
  *   Count `angle` 180 to 0 step -1:
      *   Set Servo to `angle`. Wait 0.01s.
  *   Wait 1s.
  *   **Snap** below.""",
        "flow": "We control the *speed* of the servo by controlling the delay inside the loop. Smaller delay = faster wipe.",
        "code": """import machine, time
servo = machine.PWM(machine.Pin(16))
servo.freq(50)

def set_angle(angle):
    duty = int(2500 + (angle/180)*5000)
    servo.duty_u16(duty)

while True:
    for a in range(0, 181, 2):
        set_angle(a); time.sleep(0.01)
    time.sleep(0.5)
    for a in range(180, -1, -2):
        set_angle(a); time.sleep(0.01)
    time.sleep(1)""",
        "mistakes": ["**Logic Limit**: Servo logic runs faster than physical motor. A loop with 0 delay will just jump instantly.", "**Current**: Moving servos consume amps. Don't power via USB if large."],
        "next": ["**Intermittent**: Add variable delay between wipes.", "**Rain Sensor**: Trigger wipe only when wet."]
    })

    # 0635: Fan Speed
    projects.append({
        "id": "0635",
        "title": "Interactive Simple Motors",
        "objective": "Control the speed of a DC Motor using PWM and a Potentiometer.",
        "concepts": ["Variable Speed Drive", "PWM Duty Cycle", "Power Level", "Analog Control"],
        "hardware": ["Pico", "Motor Driver", "DC Motor", "Pot"],
        "interface": "| **Pot** | GP26 | Speed Input |\n| **Motor** | GP16 | Speed Output |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Smart IO, drag `pico_analog_read`**"],
        "vars": ["**speed**: Int"],
        "guide": """**A. Init**: Frequency 1000Hz.
**B. Loop**:
1.  **Read**: `val` = Read Pot.
2.  **Write**: Set PWM Duty to `val`.
3.  Wait 0.1s.
4.  **Snap** into `pico_forever`.""",
        "flow": "The ADC range (0-65535) exactly matches the PWM Duty range (0-65535). No math needed!",
        "code": """import machine, time
pot = machine.ADC(26)
motor = machine.PWM(machine.Pin(16))
motor.freq(1000)

while True:
    val = pot.read_u16()
    motor.duty_u16(val)
    time.sleep(0.1)""",
        "mistakes": ["**Dead Zone**: Motor won't spin below ~20% duty. Adding an offset helps.", "**Whine**: Low frequency PWM causes audible coil whine."],
        "next": ["**Soft Start**: Ramp speed up to target to protect gears.", "**Tachometer**: Measure actual speed."]
    })

    # OUTPUT
    final_md = header
    
    for p in projects:
        final_md += f"""
## {int(p['id']) - 600}. Project {p['id']}: {p['title']}

### 2. Learning Objective
{p['objective']}

### 3. Concepts Introduced
"""
        for c in p['concepts']:
            final_md += f"*   **{c}**\n"
            
        final_md += f"""
### 4. Hardware Required
"""
        for h in p['hardware']:
            final_md += f"*   **{h}**\n"

        final_md += f"""
### 5. Wiring / Interfaces
{p['interface']}

### 6. Blocks Used
"""
        for b in p['blocks']:
            final_md += f"{b}\n"

        final_md += f"""
### 7. Variables
"""
        for v in p['vars']:
            final_md += f"*   **{v}**\n"

        final_md += f"""
### 8. Step-by-Step Guide
{p['guide']}

### 9. Execution Flow
{p['flow']}

### 10. Generated Code
```python
{p['code']}
```

### 11. Common Mistakes
"""
        for m in p['mistakes']:
            final_md += f"*   {m}\n"

        final_md += f"""
### 12. Try This Next
"""
        for n in p['next']:
            final_md += f"*   {n}\n"
            
        final_md += "\n---\n"

    with open(r'd:\MFF\Pico\Documentation\Docs_0601_0700.md', 'a', encoding='utf-8') as f:
        f.write(final_md)

if __name__ == "__main__":
    generate_batch_64_part1()
