
import os

def generate_batch_64_part2():
    projects = []

    # 0636: Endstop
    projects.append({
        "id": "0636",
        "title": "Smart Simple Motors Switch",
        "objective": "Implement an automatic homing sequence: The motor turns until a limit switch triggers, then stops immediately.",
        "concepts": ["Feedback Loop", "Calibration", "Limit Switch", "Homing"],
        "hardware": ["Pico", "Motor", "Limit Switch"],
        "interface": "| **Limit** | GP14 | Stop Input |\n| **Motor** | GP16 | Output |",
        "blocks": ["*   **from Layers, drag `repeat_until`**", "*   **from Smart IO, drag `pico_gpio_read`**"],
        "vars": ["None"],
        "guide": """**A. Sequence**:
1.  **Homing**:
  *   Turn Motor On.
  *   Loop until Limit Switch (GP14) is High.
  *   Turn Motor Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "This is how 3D printers find their 'Zero' position. They move blindly until they hit a known physical reference point.",
        "code": """import machine, time
limit = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.Pin(16, machine.Pin.OUT)

print("HOMING...")
motor.value(1)
while not limit.value():
    time.sleep(0.01)

motor.value(0)
print("HOME")
time.sleep(5)""",
        "mistakes": ["**Crash**: If the switch is broken or missed, the motor will grind gears forever. Add a timeout safety.", "**NC vs NO**: Limit switches are safer as Normally Closed (wire break = stop)."],
        "next": ["**Back Off**: After hitting switch, reverse for 1 second.", "**Center**: Home Left, Home Right, calc Center."]
    })

    # 0637: Vibrate Alert
    projects.append({
        "id": "0637",
        "title": "Simple Motors Alarm System",
        "objective": "Create a blind assist tool: If the Ultrasonic Sensor detects an object closer than 10cm, activate the Vibration Motor.",
        "concepts": ["Haptic Feedback", "Distance Sensing", "Assistive Tech", "Thresholds"],
        "hardware": ["Pico", "Ultrasonic (HC-SR04)", "Vibration Motor"],
        "interface": "| **Trig** | GP14 | Out |\n| **Echo** | GP15 | In |\n| **Motor** | GP16 | Vibrate |",
        "blocks": ["*   **from Sensors, drag `ultrasonic_read`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**dist**: Float"],
        "guide": """**A. Loop**:
1.  **Sense**:
  *   `dist` = Read Ultrasonic (Trig 14, Echo 15).
2.  **Act**:
  *   If `dist` < 10:
       *   Turn Motor On.
  *   Else:
       *   Turn Motor Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "Non-visual information transfer. The machine converts space (distance) into feel (vibration).",
        "code": """import machine, time, sr04
sonar = sr04.HCSR04(trigger_pin=14, echo_pin=15)
dev = machine.Pin(16, machine.Pin.OUT)

while True:
    dist = sonar.distance_cm()
    if dist < 10:
        dev.value(1)
    else:
        dev.value(0)
    time.sleep(0.1)""",
        "mistakes": ["**Vibro Power**: Vibration motors can be driven directly by Pico pins IF they are tiny coin types (<20mA). Bigger ones need a transistor.", "**Echo**: Wall absorption/angle affects reading."],
        "next": ["**Proximity**: Pulse faster as object gets closer (Parking Sensor).", "**PWM**: Vibrate intensity = 1/distance."]
    })

    # 0638: Pinball Flipper
    projects.append({
        "id": "0638",
        "title": "The Simple Motors Game",
        "objective": "Simulate a pinball flipper: Press button -> Servo snaps to 90° (Fast). Release -> Servo returns to 0° (Slow/Spring).",
        "concepts": ["Asymmetric Speed", "Servo Dynamics", "Game Physics", "Spring Simulation"],
        "hardware": ["Pico", "Button", "Servo"],
        "interface": "| **Btn** | GP14 | Trigger |\n| **Servo** | GP16 | Flipper |",
        "blocks": ["*   **from Actuators, drag `servo_write`**", "*   **from Smart IO, drag `pico_gpio_read`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check**:
  *   If Btn Pressed:
      *   Set Servo 90 (Power Stroke). Wait 0.1s.
      *   Loop until Btn Release.
  *   Else:
      *   Loop `ang` 90 to 0 step -5 (Return Stroke):
           *   Set Servo `ang`. Wait 0.01s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Real flippers are solenoids (instant). Servos are slower, so we jump max speed for the hit, but smooth the return to look like a spring.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
servo = machine.PWM(machine.Pin(16))
servo.freq(50)

def set_angle(angle):
    servo.duty_u16(int(2500 + (angle/180)*5000))

current_angle = 0
set_angle(0)

while True:
    if btn.value():
        set_angle(90) # Snap
        current_angle = 90
        while btn.value(): time.sleep(0.01)
    else:
        if current_angle > 0:
            current_angle -= 5 # Spring return speed
            if current_angle < 0: current_angle = 0
            set_angle(current_angle)
            time.sleep(0.01)""",
        "mistakes": ["**Power Supply**: Fast servo moves cause voltage dips. Pico might reboot. Use external 5V.", "**Torque**: Micro servos can't flip a real steel ball."],
        "next": ["**Double**: Two flippers (L/R) on L/R buttons.", "**Tilt**: Tilt sensor disables flippers."]
    })

    # 0639: Solar Tracker
    projects.append({
        "id": "0639",
        "title": "Automated Simple Motors",
        "objective": "Build a single-axis solar tracker. The servo moves towards the brighter LDR until both LDRs have equal light.",
        "concepts": ["Differential Sensing", "Closed Loop Control", "Phototropism", "Error Minimization"],
        "hardware": ["Pico", "Servo", "2 LDRs"],
        "interface": "| **LDR L** | GP26 | Left |\n| **LDR R** | GP27 | Right |\n| **Servo** | GP16 | Axis |",
        "blocks": ["*   **from Logic, drag `if_compare`**", "*   **from Variables, drag `change_variable`**"],
        "vars": ["**pos**: Int (90)", "**left**: Int", "**right**: Int"],
        "guide": """**A. Init**: `pos`=90.
**B. Loop**:
1.  **Read**: `left`=ADC0, `right`=ADC1.
2.  **Compare**:
  *   If `left` > `right` + 2000:
       *   Change `pos` by +1.
  *   Else If `right` > `left` + 2000:
       *   Change `pos` by -1.
3.  **Clamp**:
  *   If `pos` > 180 set 180. If `pos` < 0 set 0.
4.  **Act**:
  *   Set Servo `pos`. Wait 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The system seeks balance. If Left is brighter, turn Left. If Right Is brighter, turn Right. The 'Deadband' (2000) prevents jitter when equal.",
        "code": """import machine, time
ldrL = machine.ADC(26)
ldrR = machine.ADC(27)
servo = machine.PWM(machine.Pin(16))
servo.freq(50)
pos = 90

def set_angle(angle):
    servo.duty_u16(int(2500 + (angle/180)*5000))

while True:
    l = ldrL.read_u16()
    r = ldrR.read_u16()
    
    if l > r + 2000:
        pos += 1
    elif r > l + 2000:
        pos -= 1
        
    if pos > 180: pos = 180
    if pos < 0: pos = 0
    
    set_angle(pos)
    time.sleep(0.05)""",
        "mistakes": ["**Orientation**: If servo turns the wrong way, it will run away from the light. Swap +1/-1.", "**Shadows**: Sensors need a separator wall between them."],
        "next": ["**Dual Axis**: Up/Down + Left/Right (4 LDRs).", "**Efficiency**: Calculate total light gathered."]
    })

    # 0640: H-Bridge
    projects.append({
        "id": "0640",
        "title": "Mastering Simple Motors",
        "objective": "Control a DC Motor's direction using an H-Bridge driver logic. Implement Forward, Reverse, Brake, and Coast modes.",
        "concepts": ["H-Bridge Logic", "Direction Control", "Braking Modes", "Driver Abstraction"],
        "hardware": ["Pico", "L298N/L9110 Driver", "DC Motor"],
        "interface": "| **IN1** | GP16 | Leg A |\n| **IN2** | GP17 | Leg B |",
        "blocks": ["*   **from Functions, drag `define_function`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Functions**:
1.  **Def Forward**: Set IN1=1, IN2=0.
2.  **Def Reverse**: Set IN1=0, IN2=1.
3.  **Def Brake**: Set IN1=1, IN2=1 (Shorts motor).
4.  **Def Coast**: Set IN1=0, IN2=0 (Opens circuit).
**B. Loop**:
  *   Call Forward. Wait 1s.
  *   Call Brake. Wait 1s (Stop fast).
  *   Call Reverse. Wait 1s.
  *   Call Coast. Wait 1s (Stop slow).
  *   **Snap** into `pico_forever`.""",
        "flow": "An H-Bridge allows voltage to be applied across the motor in either polarity, or shorted (Brake), or disconnected (Coast).",
        "code": """import machine, time
in1 = machine.Pin(16, machine.Pin.OUT)
in2 = machine.Pin(17, machine.Pin.OUT)

def forward():
    in1.value(1); in2.value(0)

def reverse():
    in1.value(0); in2.value(1)

def brake():
    in1.value(1); in2.value(1)

def coast():
    in1.value(0); in2.value(0)

while True:
    forward(); time.sleep(1)
    brake(); time.sleep(1)
    reverse(); time.sleep(1)
    coast(); time.sleep(1)""",
        "mistakes": ["**Shoot-Through**: Switching too fast between Forward/Reverse can short the power supply in poorly designed bridges.", "**PWM**: Apply PWM to Enable pin or one of the inputs for speed control."],
        "next": ["**Speed+Dir**: Use PWM on inputs (Forward: IN1=PWM, IN2=0).", "**Tank Drive**: Two motors."]
    })

    # OUTPUT
    final_md = ""
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
    generate_batch_64_part2()
