
import os

def generate_batch_66_part1():
    header = """
# 🏁 Batch 66: Night Light 4

---
"""
    projects = []

    # 0651: Intro (Reverse Logic)
    projects.append({
        "id": "0651",
        "title": "Introduction to Night Light",
        "objective": "Understand LDR reading direction (Low=Dark, High=Light) and implement a basic Night Light that turns ON when the reading is below 1000.",
        "concepts": ["Analogue to Digital (ADC)", "Reverse Logic", "Thresholding", "Calibration"],
        "hardware": ["Pico", "LDR", "LED"],
        "interface": "| **LDR** | GP26 | Light Level |\n| **LED** | GP16 | Illumination |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**level**: Int"],
        "guide": """**A. Loop**:
1.  **Read**:
  *   `level` = Read ADC(26).
  *   Print `level`.
2.  **Compare**:
  *   If `level` < 1000:
      *   Turn LED On.
  *   Else:
      *   Turn LED Off.
  *   Wait 0.1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Common novice mistake: thinking High voltage means Dark. Actually, Dark = High Resistance = Low Voltage (usually, depending on divider).",
        "code": """import machine, time
ldr = machine.ADC(26)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    level = ldr.read_u16()
    print(level)
    if level < 1000:
         led.on()
    else:
         led.off()
    time.sleep(0.1)""",
        "mistakes": ["**Divider config**: If LDR is connected to 3.3V, Dark=Low. If connected to GND, Dark=High.", "**Ambient Light**: LED light might shine on LDR, causing flickering (Feedback)."],
        "next": ["**Hysteresis**: Turn On at 1000, Turn Off at 1500.", "**Invert**: Make a Day Light (On when bright)."]
    })

    # 0652: Blinking (Lighthouse)
    projects.append({
        "id": "0652",
        "title": "Blinking Night Light",
        "objective": "Simulate a Lighthouse beacon: Fade In (1s), Fade Out (1s), Wait (2s).",
        "concepts": ["Navigational Aids", "PWM Fading", "Visual Patterns", "Long Period Loops"],
        "hardware": ["Pico", "LED"],
        "interface": "| **LED** | GP16 | Beacon |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**duty**: Int"],
        "guide": """**A. Loop**:
1.  **Fade In**: loop `duty` 0..65000. step 1000. Wait 0.015s.
2.  **Fade Out**: loop `duty` 65000..0. step -1000. Wait 0.015s.
3.  **Wait**: Delay 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "A beacon needs to be distinct from random lights. The specific timing signature identifies the lighthouse.",
        "code": """import machine, time
led = machine.PWM(machine.Pin(16))
led.freq(1000)

while True:
    # In
    for d in range(0, 65535, 1000):
        led.duty_u16(d); time.sleep(0.015)
    # Out
    for d in range(65535, 0, -1000):
        led.duty_u16(d); time.sleep(0.015)
    time.sleep(2)""",
        "mistakes": ["**Time Math**: 65 steps * 0.015s = ~1s.", "**Visibility**: Low PWM freq causes strobing."],
        "next": ["**Morse**: Flash coordinates via light.", "**Rotation**: Use 3 LEDs to simulate rotation."]
    })

    # 0653: Manual (RGB Mixer)
    projects.append({
        "id": "0653",
        "title": "Manual Night Light Control",
        "objective": "Use 3 Buttons (R, G, B) to toggle the red, green, and blue channels of an RGB LED, creating 7 possible colors.",
        "concepts": ["Color Mixing", "Additive Color Theory", "Digital RGB", "Input Arrays"],
        "hardware": ["Pico", "3 Buttons [13-15]", "RGB LED [16-18]"],
        "interface": "| **Btns** | GP13-15 | R/G/B In |\n| **RGB** | GP16-18 | R/G/B Out |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**r**: Bool", "**g**: Bool", "**b**: Bool"],
        "guide": """**A. Init**: r=0, g=0, b=0.
**B. Loop**:
1.  **Poll**:
  *   If BtnR: Toggle `r`. Wait Release.
  *   If BtnG: Toggle `g`. Wait Release.
  *   If BtnB: Toggle `b`. Wait Release.
2.  **Update**:
  *   Set Pin 16 `r`.
  *   Set Pin 17 `g`.
  *   Set Pin 18 `b`.
  *   **Snap** into `pico_forever`.""",
        "flow": "R+G=Yellow. R+B=Magenta. G+B=Cyan. R+G+B=White.",
        "code": """import machine, time
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(13, 16)]
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 19)]
state = [0, 0, 0]

while True:
    for i in range(3):
        if btns[i].value():
            state[i] = not state[i]
            leds[i].value(state[i])
            while btns[i].value(): time.sleep(0.01)
    time.sleep(0.01)""",
        "mistakes": ["**Common Anode**: If using Common Anode RGB, logic is inverted (0=On).", "**Resistors**: Red needs different resistor than Blue/Green."],
        "next": ["**Analog**: Use Pots to mix colors smoothly.", "**Save**: Save color to memory."]
    })

    # 0654: Sequences (Sunrise)
    projects.append({
        "id": "0654",
        "title": "Night Light Sequences",
        "objective": "Simulate a Sunrise: Start Blue (Night), fade to Purple, then Red, then Orange, then Yellow (Day).",
        "concepts": ["Color Gradients", "Transitions", "Atmospheric Simulation", "Multi-Channel PWM"],
        "hardware": ["Pico", "RGB LED"],
        "interface": "| **RGB** | GP16-18 | PWM |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**i**: Int"],
        "guide": """**A. Loop**:
1.  **Night to Dawn (Blue->Red)**:
  *   Loop `i` 0..65000:
      *   Blue = 65000 - `i`.
      *   Red = `i`.
      *   Wait.
2.  **Dawn to Day (Red->Green mix)**:
  *   Loop `i` 0..65000:
      *   Red = 65000.
      *   Green = `i`. (R+G=Yellow).
      *   Wait.
  *   **Snap** into `pico_forever`.""",
        "flow": "Instead of jumping colors, we cross-fade channels to create smooth spectral shifts.",
        "code": """import machine, time
r = machine.PWM(machine.Pin(16)); r.freq(1000)
g = machine.PWM(machine.Pin(17)); g.freq(1000)
b = machine.PWM(machine.Pin(18)); b.freq(1000)
delay = 0.005

while True:
    # Blue to Red (via Purple)
    for i in range(0, 65535, 500):
        b.duty_u16(65535 - i)
        r.duty_u16(i)
        time.sleep(delay)
    # Red to Yellow
    for i in range(0, 65535, 500):
        g.duty_u16(i)
        time.sleep(delay)
    time.sleep(1)
    # Reset
    r.duty_u16(0); g.duty_u16(0); b.duty_u16(0)
    time.sleep(1)""",
        "mistakes": ["**Blue Spike**: Real sunrise doesn't have much green until the sun is up.", "**Brightness**: RGB LEDs are very bright. Use diffusers."],
        "next": ["**Sunset**: Reverse the process.", "**Time Scale**: Stretch to 30 minutes."]
    })

    # 0655: Interactive (Smart Streetlight)
    projects.append({
        "id": "0655",
        "title": "Interactive Night Light",
        "objective": "Smart Streetlight: Only turns on if it is DARK (LDR) AND Motion is detected (PIR).",
        "concepts": ["Sensor Fusion", "Condition Stacking", "Energy Management", "AND Logic"],
        "hardware": ["Pico", "LDR", "PIR", "LED"],
        "interface": "| **LDR** | GP26 | Ambient |\n| **PIR** | GP15 | Motion |\n| **LED** | GP16 | Lamp |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Logic, drag `and_operation`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Read**:
  *   `isDark` = `ADC(26)` < 20000.
  *   `isMotion` = `GP15` == 1.
2.  **Logic**:
  *   If `isDark` AND `isMotion`:
       *   Turn LED On.
  *   Else:
       *   Turn LED Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "This saves energy by ignoring motion during the day, and ignoring darkness if no one is around.",
        "code": """import machine, time
ldr = machine.ADC(26)
pir = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    is_dark = ldr.read_u16() < 20000
    if is_dark and pir.value():
        led.on()
        time.sleep(5) # Stay on for 5s
    else:
        led.off()
    time.sleep(0.1)""",
        "mistakes": ["**Threshold**: Is 20000 too dark? Adjust for twilight.", "**False Trigger**: Wind moving trees might trigger PIR."],
        "next": ["**Dimming**: Run at 20% brightness at night, 100% when motion.", "**Network**: If one light triggers, wake up the next one."]
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
    generate_batch_66_part1()
