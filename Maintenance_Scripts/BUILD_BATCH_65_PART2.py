
import os

def generate_batch_65_part2():
    projects = []

    # 0646: Police Override
    projects.append({
        "id": "0646",
        "title": "Smart Traffic Lights Switch",
        "objective": "Implement a Police Override Mode. When a switch is flipped, force all lights to Red immediately for safety.",
        "concepts": ["Priority Interrupts", "Safety Overrides", "System Modes", "Manual Preemption"],
        "hardware": ["Pico", "Switch", "Traffic LEDs"],
        "interface": "| **Switch** | GP14 | Override |\n| **Signals** | GP16-18 | Out |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check**:
  *   If Switch On:
      *   Turn Red On.
      *   Turn Y/G Off.
  *   Else:
      *   Run Normal Cycle (G->Y->R).
  *   **Snap** into `pico_forever`.""",
        "flow": "Safety systems often have a physical key switch that cuts power or forces a safe state regardless of the software logic.",
        "code": """import machine, time
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(16, machine.Pin.OUT)
yel = machine.Pin(17, machine.Pin.OUT)
grn = machine.Pin(18, machine.Pin.OUT)

while True:
    if sw.value():
        red.on(); yel.off(); grn.off()
        time.sleep(0.1)
    else:
        # Standard Cycle
        grn.on(); time.sleep(3); grn.off()
        if sw.value(): continue
        yel.on(); time.sleep(1); yel.off()
        if sw.value(): continue
        red.on(); time.sleep(3); red.off()""",
        "mistakes": ["**Latency**: Using `time.sleep(3)` means the override might take 3s to activate. Need continuous checking.", "**Release**: Returning to Green instantly after override might cause a crash. Should go to Red first."],
        "next": ["**Blink Code**: Flash Green to signal 'Returning to Normal'.", "**All Red**: Make it a 4-Way Flash."]
    })

    # 0647: Red Light Camera
    projects.append({
        "id": "0647",
        "title": "Traffic Lights Alarm System",
        "objective": "Simulate a Red Light Camera. If an object is detected (IR Sensor) while the Red Light is active, flash a White LED (Camera Flash).",
        "concepts": ["Violation Detection", "Conditional Triggers", "State Coupling", "Enforcement"],
        "hardware": ["Pico", "IR Sensor", "Red LED", "White LED"],
        "interface": "| **IR** | GP14 | Car Detector |\n| **Red** | GP16 | Signal |\n| **Camera** | GP17 | Flash |",
        "blocks": ["*   **from Logic, drag `and_operation`**", "*   **from Smart IO, drag `pico_gpio_read`**"],
        "vars": ["**isRed**: Bool"],
        "guide": """**A. Loop**:
1.  **Normal Op**:
  *   Red On. Set `isRed`=True.
  *   Wait 5s.
  *   Red Off. Set `isRed`=False.
  *   Wait 5s (Green/Yellow sim).
2.  **Monitor**:
  *   (In parallel thread or fast loop)
  *   If `isRed` AND IR Sensor:
      *   Flash Camera.
  *   **Snap** into `pico_forever`.""",
        "flow": "The enforcement logic depends on the state of the signal logic. This coupling is critical.",
        "code": """import machine, time
ir = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(16, machine.Pin.OUT)
cam = machine.Pin(17, machine.Pin.OUT)
is_red = False

# Simulation Loop
while True:
    # RED PHASE
    red.on(); is_red = True
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < 5000:
        if ir.value() and is_red:
             print("VIOLATION!")
             cam.on(); time.sleep(0.1); cam.off()
             while ir.value(): time.sleep(0.1)
        time.sleep(0.01)
        
    # GREEN PHASE
    red.off(); is_red = False
    time.sleep(5)""",
        "mistakes": ["**False Positives**: Sensor triggering just as light turns Red (Amber dilemma).", "**Blocking**: Main loop blocks the sensor check. The 'while ticks' loop solves this."],
        "next": ["**Log**: Save timestamp of violation to file.", "**Counter**: Count total violations."]
    })

    # 0648: Stop/Go Game
    projects.append({
        "id": "0648",
        "title": "The Traffic Lights Game",
        "objective": "Reaction Game: The light randomly turns Green or Red. Player must HOLD the button when Green and RELEASE when Red.",
        "concepts": ["Inhibition", "Reflex Test", "Random Intervals", "Game Loops"],
        "hardware": ["Pico", "R/G LEDs", "Button"],
        "interface": "| **Signals** | GP16/17 | R/G |\n| **Btn** | GP14 | Input |",
        "blocks": ["*   **from Math, drag `random_integer`**", "*   **from Time, drag `time_ticks_ms`**"],
        "vars": ["**safe**: Bool"],
        "guide": """**A. Loop**:
1.  **Change State**:
  *   If Random(0,1):
      *   Green On, Red Off. `safe`=True.
  *   Else:
      *   Green Off, Red On. `safe`=False.
2.  **Check**:
  *   Wait Random(1,3)s.
  *   If `safe` AND NOT Button: Fail.
  *   If NOT `safe` AND Button: Fail.
  *   **Snap** into `pico_forever`.""",
        "flow": "Simulates the 'Red Light, Green Light' childhood game. Tests ability to stop *and* go.",
        "code": """import machine, time, random
red = machine.Pin(16, machine.Pin.OUT)
grn = machine.Pin(17, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    safe = bool(random.getrandbits(1))
    if safe:
        grn.on(); red.off()
    else:
        grn.off(); red.on()
        
    duration = random.randint(1000, 3000)
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < duration:
        pressed = btn.value()
        if safe and not pressed:
            print("FAIL: Too Slow")
        elif not safe and pressed:
            print("FAIL: Moved on Red")
        time.sleep(0.01)""",
        "mistakes": ["**Bias**: Should be 50/50 chance.", "**Feedback**: Needs a buzzer to signal failure."],
        "next": ["**Scoring**: Add points for every 100ms held correctly.", "**Speed Up**: Make switching faster."]
    })

    # 0649: Cross Traffic
    projects.append({
        "id": "0649",
        "title": "Automated Traffic Lights",
        "objective": "Control a full intersection with two sets of lights (North-South and East-West). Ensure they never show Green simultaneously.",
        "concepts": ["Interlocking Logic", "State Machines", "Safety Critical Systems", "Timing Diagrams"],
        "hardware": ["Pico", "2x R/Y/G Sets"],
        "interface": "| **NS** | GP10-12 | |\n| **EW** | GP13-15 | |",
        "blocks": ["*   **from Functions, drag `define_function`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **State 1 (NS Green)**:
  *   NS Green, EW Red. Wait 5s.
2.  **State 2 (NS Yellow)**:
  *   NS Yellow, EW Red. Wait 2s.
3.  **State 3 (All Red)**:
  *   NS Red, EW Red. Wait 1s (Clearance).
4.  **State 4 (EW Green)**:
  *   NS Red, EW Green. Wait 5s.
5.  **State 5 (EW Yellow)**:
  *   NS Red, EW Yellow. Wait 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The 'All Red' clearance interval is vital to clear the intersection before cross traffic starts.",
        "code": """import machine, time
ns = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 13)] # R,Y,G
ew = [machine.Pin(i, machine.Pin.OUT) for i in range(13, 16)]

def set_light(light, color):
    # color: 0=Red, 1=Yel, 2=Grn
    light[0].value(1 if color==0 else 0)
    light[1].value(1 if color==1 else 0)
    light[2].value(1 if color==2 else 0)

while True:
    set_light(ns, 2); set_light(ew, 0) # NS Green
    time.sleep(5)
    set_light(ns, 1); set_light(ew, 0) # NS Yellow
    time.sleep(2)
    set_light(ns, 0); set_light(ew, 0) # All Red
    time.sleep(1)
    set_light(ew, 2); set_light(ns, 0) # EW Green
    time.sleep(5)
    set_light(ew, 1); set_light(ns, 0) # EW Yellow
    time.sleep(2)
    set_light(ns, 0); set_light(ew, 0) # All Red
    time.sleep(1)""",
        "mistakes": ["**Missing Clearance**: Jumping straight from Red to Green without an All-Red buffer.", "**Wiring**: Mixing up the pins is very common with 6 LEDs."],
        "next": ["**Turn Arrow**: Add a Left Turn phase.", "**Sensor**: Skip EW Green if no cars waiting."]
    })

    # 0650: Mastering OOP
    projects.append({
        "id": "0650",
        "title": "Mastering Traffic Lights",
        "objective": "Use Object-Oriented Programming to create a `TrafficLight` class. Instantiate two independent lights and control them.",
        "concepts": ["Classes & Objects", "Encapsulation", "Methods", "Reusable Code"],
        "hardware": ["Pico", "R/Y/G LEDs"],
        "interface": "| **LEDs** | GP16-18 | |",
        "blocks": ["*   **from Classes, drag `define_class`**", "*   **from Functions, drag `call_method`**"],
        "vars": ["**north**: TrafficLight"],
        "guide": """**A. Class**:
1.  **Define `TrafficLight`**:
  *   `__init__(pinR, pinY, pinG)`: Setup pins.
  *   `go()`: G=1, R/Y=0.
  *   `stop()`: R=1, G/Y=0.
  *   `caution()`: Y=1.
**B. Loop**:
1.  **Use**:
  *   `north = TrafficLight(10,11,12)`.
  *   `north.go()`. Wait.
  *   `north.stop()`. Wait.
  *   **Snap** into `pico_forever`.""",
        "flow": "OOP allows us to think in terms of 'Things' (Lights) and 'Actions' (Go/Stop) rather than pins and bits.",
        "code": """import machine, time

class TrafficLight:
    def __init__(self, r_pin, y_pin, g_pin):
        self.red = machine.Pin(r_pin, machine.Pin.OUT)
        self.yel = machine.Pin(y_pin, machine.Pin.OUT)
        self.grn = machine.Pin(g_pin, machine.Pin.OUT)
    
    def stop(self):
        self.red.on(); self.yel.off(); self.grn.off()
        
    def go(self):
        self.red.off(); self.yel.off(); self.grn.on()
        
    def caution(self):
        self.red.off(); self.yel.on(); self.grn.off()

north = TrafficLight(10, 11, 12)
east = TrafficLight(13, 14, 15)

while True:
    north.go(); east.stop()
    time.sleep(3)
    north.caution()
    time.sleep(1)
    north.stop(); east.go()
    time.sleep(3)
    east.caution()
    time.sleep(1)""",
        "mistakes": ["**Self**: Forgetting `self` in method definitions.", "**Scope**: Variables created in `__init__` must be accessed via `self.`."],
        "next": ["**Add Property**: `self.state` to track current color.", "**Inheritance**: Create `PedestrianLight` inheriting from `TrafficLight`."]
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
    generate_batch_65_part2()
