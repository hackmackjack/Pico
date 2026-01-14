
import os

def generate_batch_65_part1():
    header = """
# 🏁 Batch 65: Traffic Lights 4

---
"""
    projects = []

    # 0641: Intro (Yellow Flash)
    projects.append({
        "id": "0641",
        "title": "Introduction to Traffic Lights",
        "objective": "Simulate 'Maintenance Mode' by flashing a Yellow LED endlessly (1s On, 1s Off).",
        "concepts": ["State Indication", "Hazard Signaling", "Maintenance Loop", "Visual Warning"],
        "hardware": ["Pico", "Yellow LED"],
        "interface": "| **Yellow** | GP17 | Warning Light |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Loops, drag `pico_forever`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Flash**:
  *   Turn Yellow On. Wait 1s.
  *   Turn Yellow Off. Wait 1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "During power outages or sensor errors, traffic lights revert to a safe fallback state (flashing yellow/red).",
        "code": """import machine, time
yel = machine.Pin(17, machine.Pin.OUT)

while True:
    yel.toggle()
    time.sleep(1)""",
        "mistakes": ["**Wrong Pin**: Traffic lights usually use 16(R), 17(Y), 18(G).", "**Timing**: Too fast (0.1s) looks like panic/error. 1s is standard."],
        "next": ["**4-Way**: Flash Red instead (Stop Sign).", "**Alternating**: Flash Left/Right arrows."]
    })

    # 0642: Blinking (UK Sequence)
    projects.append({
        "id": "0642",
        "title": "Blinking Traffic Lights",
        "objective": "Implement the UK Traffic Light sequence: Red -> Red+Yellow -> Green -> Yellow -> Red.",
        "concepts": ["Standard Sequences", "Regional Variations", "Multi-State Outputs", "Transition Logic"],
        "hardware": ["Pico", "R/Y/G LEDs"],
        "interface": "| **Red** | GP16 | Stop |\n| **Yellow** | GP17 | Ready/Caution |\n| **Green** | GP18 | Go |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Red**: R=1, Y=0, G=0. Wait 3s.
2.  **Red+Yellow**: R=1, Y=1, G=0. Wait 1s.
3.  **Green**: R=0, Y=0, G=1. Wait 3s.
4.  **Yellow**: R=0, Y=1, G=0. Wait 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The 'Red+Yellow' phase warns drivers to get ready (engage clutch), reducing reaction time when Green appears.",
        "code": """import machine, time
red = machine.Pin(16, machine.Pin.OUT)
yel = machine.Pin(17, machine.Pin.OUT)
grn = machine.Pin(18, machine.Pin.OUT)

while True:
    # Red
    red.on(); yel.off(); grn.off()
    time.sleep(3)
    # Red+Yellow
    yel.on()
    time.sleep(1)
    # Green
    red.off(); yel.off(); grn.on()
    time.sleep(3)
    # Yellow
    grn.off(); yel.on()
    time.sleep(2)""",
        "mistakes": ["**Green+Yellow**: Never happens. Green -> Yellow.", "**Ghosting**: Forgetting to turn off Red when switching to Green."],
        "next": ["**US Logic**: Red -> Green -> Yellow -> Red (No R+Y).", "**Austria**: Green flashes before Yellow."]
    })

    # 0643: Manual (Call Button)
    projects.append({
        "id": "0643",
        "title": "Manual Traffic Lights Control",
        "objective": "Pedestrian Crossing: Light stays Green until Button pressed. Then: Wait 3s -> Yellow -> Red -> Walk -> Green.",
        "concepts": ["Demand Actuated", "Interrupt-like Flow", "Sequential Logic", "Pedestrian Safety"],
        "hardware": ["Pico", "R/Y/G LEDs", "Button"],
        "interface": "| **Button** | GP14 | Call |\n| **Signals** | GP16-18 | R/Y/G |",
        "blocks": ["*   **from Logic, drag `if_do`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Init**: Green On.
**B. Loop**:
1.  **Check**:
  *   If Button (GP14) Pressed:
      *   Wait 3s (Walk buffer).
      *   Yellow On, Green Off. Wait 2s.
      *   Red On, Yellow Off. Wait 5s (Walk).
      *   Green On, Red Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "The logic gives priority to cars (Green) unless interrupted by a human request.",
        "code": """import machine, time
red = machine.Pin(16, machine.Pin.OUT)
yel = machine.Pin(17, machine.Pin.OUT)
grn = machine.Pin(18, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Start Logic
grn.on()

while True:
    if btn.value():
        time.sleep(3) # Reaction delay
        grn.off(); yel.on(); time.sleep(2)
        yel.off(); red.on(); time.sleep(5) # Walk
        red.off(); grn.on()
    time.sleep(0.1)""",
        "mistakes": ["**Instant Change**: Turning Red immediately causes accidents. Always transition via Yellow.", "**Stuck**: If button broken (always high), traffic stops forever. Add minimum Green time."],
        "next": ["**Buzzer**: Add sound for blind pedestrians.", "**Cancel**: Press again to cancel (No, that's bad UX)."]
    })

    # 0644: Sequences (Drag Race)
    projects.append({
        "id": "0644",
        "title": "Traffic Lights Sequences",
        "objective": "Simulate a 'Christmas Tree' drag race starter: 3 Amber lights count down, then Green.",
        "concepts": ["Countdown Logic", "Visual Timing", "Race Theory", "Starting Gun"],
        "hardware": ["Pico", "3 Amber LEDs", "1 Green LED"],
        "interface": "| **Ambers** | GP15-17 | Pre-Stage/Stage/Go |\n| **Green** | GP18 | Launch |",
        "blocks": ["*   **from Loops, drag `for_in_list`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**lights**: List"],
        "guide": """**A. Init**: `lights`=[15, 16, 17].
**B. Loop**:
1.  **Wait**:
  *   Wait for Button.
2.  **Countdown**:
  *   Loop `pin` in `lights`:
       *   Turn Pin On. Wait 0.5s. Turn Off.
  *   Turn Green (18) On. Wait 2s. Turn Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "Precise .500s intervals are crucial in drag racing (Pro Tree).",
        "code": """import machine, time
ambers = [machine.Pin(i, machine.Pin.OUT) for i in range(15, 18)]
grn = machine.Pin(18, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value():
        for led in ambers:
            led.on(); time.sleep(0.5); led.off()
        grn.on(); time.sleep(2); grn.off()
    time.sleep(0.01)""",
        "mistakes": ["**Overlap**: In a real tree, lights sequence down. They don't just blink.", "**False Start**: Detecting button release before Green."],
        "next": ["**Reaction Timer**: Measure time between Green ON and Button Release.", "**Foul**: If button released while Amber is on, Red Light."]
    })

    # 0645: Interactive (Night Mode)
    projects.append({
        "id": "0645",
        "title": "Interactive Traffic Lights",
        "objective": "Switch traffic modes based on ambient light. Day = Normal Cycle. Night (Dark) = Flashing Red (Stop Sign).",
        "concepts": ["Mode Switching", "Environmental Sensing", "Conditional Loops", "Power Saving"],
        "hardware": ["Pico", "LDR", "R/Y/G LEDs"],
        "interface": "| **LDR** | GP26 | Light Sensor |\n| **Signals** | GP16-18 | Out |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Logic, drag `if_else`**"],
        "vars": ["**dark**: Bool"],
        "guide": """**A. Loop**:
1.  **Check**:
  *   If ADC(26) < 10000 (Dark):
      *   Toggle Red. Wait 0.8s. Matches Off.
  *   Else (Day):
      *   Run Normal Sequence (G-Y-R).
  *   **Snap** into `pico_forever`.""",
        "flow": "The main loop decides *which* sub-loop or sequence to run. This is a simple 'State' pattern.",
        "code": """import machine, time
ldr = machine.ADC(26)
red = machine.Pin(16, machine.Pin.OUT)
yel = machine.Pin(17, machine.Pin.OUT)
grn = machine.Pin(18, machine.Pin.OUT)

while True:
    if ldr.read_u16() < 10000:
        # Night
        yel.off(); grn.off()
        red.toggle(); time.sleep(0.8)
    else:
        # Day (One step per loop)
        red.off(); yel.off(); grn.on(); time.sleep(3)
        grn.off(); yel.on(); time.sleep(1)
        yel.off(); red.on(); time.sleep(3)""",
        "mistakes": ["**Blocking**: The 'Day' sequence blocks checking the LDR for ~7s. Use `ticks_ms` for better response.", "**Hysteresis**: Light flickering at dusk causes rapid mode switching."],
        "next": ["**Hysteresis**: Add buffer zone.", "**Clock**: Use Real Time Clock (RTC) instead of LDR."]
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
    generate_batch_65_part1()
