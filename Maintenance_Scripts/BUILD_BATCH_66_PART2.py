
import os

def generate_batch_66_part2():
    projects = []

    # 0656: Party Mode
    projects.append({
        "id": "0656",
        "title": "Smart Night Light Switch",
        "objective": "Party Mode Switch: If slide switch is ON, flash RGB LEDs randomly (Disco). If OFF, pure White light.",
        "concepts": ["State Selection", "Random Color Generation", "Mode Toggle", "Epilepsy Warnings"],
        "hardware": ["Pico", "Switch", "RGB LED"],
        "interface": "| **Switch** | GP14 | Mode |\n| **RGB** | GP16-18 | Out |",
        "blocks": ["*   **from Math, drag `random_integer`**", "*   **from Logic, drag `if_else`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check**:
  *   If Switch On:
      *   R = Random(0, 65000).
      *   G = Random(0, 65000).
      *   B = Random(0, 65000).
      *   Wait 0.1s.
  *   Else:
      *   R=65000, G=65000, B=65000 (White).
  *   **Snap** into `pico_forever`.""",
        "flow": "Random values fed into PWM duties create chaotic color patterns.",
        "code": """import machine, time, random
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
leds = [machine.PWM(machine.Pin(i)) for i in range(16, 19)]
for l in leds: l.freq(1000)

while True:
    if sw.value():
        for l in leds: l.duty_u16(random.getrandbits(16))
        time.sleep(0.1)
    else:
        for l in leds: l.duty_u16(65535)
        time.sleep(0.1)""",
        "mistakes": ["**Power**: 3 channels at 100% (White) draws ~60mA. Limit duty if powering from weak source.", "**Seizures**: Flashing fast can be dangerous."],
        "next": ["**Strobe**: Flash White On/Off rapidly.", "**Fade**: Randomly pick target color and fade to it."]
    })

    # 0657: Sunrise Alarm
    projects.append({
        "id": "0657",
        "title": "Night Light Alarm System",
        "objective": "Wake-up Light: Wait for a button press (simulating alarm time). Then slowly fade from Red to White over 60 seconds.",
        "concepts": ["Bio-hacking", "Long Duration Fades", "Color Temperature", "Sleep Cycles"],
        "hardware": ["Pico", "Button", "RGB LED"],
        "interface": "| **Button** | GP14 | Test Alarm |\n| **RGB** | GP16-18 | Wake Light |",
        "blocks": ["*   **from Loops, drag `count_with`**", "*   **from Actuators, drag `pwm_duty`**"],
        "vars": ["**step**: Int"],
        "guide": """**A. Loop**:
1.  **Wait**: Wait for Button.
2.  **Sunrise**:
  *   Loop `step` 0 to 65000 by 100:
      *   Red = `step` (Starts immediately).
      *   Green = `step` - 20000 (Starts later).
      *   Blue = `step` - 40000 (Starts last).
      *   Clamp values to >0.
      *   Wait 0.1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Red comes up first (Dawn). Then Green mixes in (Orange/Yellow). Finally Blue (White daylight).",
        "code": """import machine, time
r = machine.PWM(machine.Pin(16)); r.freq(1000)
g = machine.PWM(machine.Pin(17)); g.freq(1000)
b = machine.PWM(machine.Pin(18)); b.freq(1000)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value():
        print("WAKE UP")
        for i in range(0, 65535, 100):
            r.duty_u16(i)
            # Delayed entry for G and B
            g.duty_u16(max(0, i - 20000)) 
            b.duty_u16(max(0, i - 40000))
            time.sleep(0.1) # Total ~65s
        time.sleep(5)
        r.duty_u16(0); g.duty_u16(0); b.duty_u16(0)
    time.sleep(0.1)""",
        "mistakes": ["**Negative Numbers**: `i - 20000` can be negative. PWM functions might crash or wrap around if not clamped.", "**Blue Hazard**: Too much blue light at night disturbs sleep."],
        "next": ["**Real Time**: Trigger at 7:00 AM.", "**Sunset**: Inverse for sleep aid."]
    })

    # 0658: Color Match
    projects.append({
        "id": "0658",
        "title": "The Night Light Game",
        "objective": "Reflex Game: The RGB LED cycles through colors. Press the button exactly when it turns BLUE.",
        "concepts": ["Pattern Recognition", "Reflex Timing", "State Matching", "Visual Cues"],
        "hardware": ["Pico", "RGB LED", "Button"],
        "interface": "| **RGB** | GP16-18 | Output |\n| **Button** | GP14 | Input |",
        "blocks": ["*   **from Variables, drag `create_list`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**color**: String"],
        "guide": """**A. Init**: `colors`=['Red', 'Green', 'Blue', 'Yellow'].
**B. Loop**:
1.  **Cycle**:
  *   Loop `c` in `colors`:
      *   Display `c` on RGB.
      *   Wait Random(0.5, 1.5)s.
      *   If Button Pressed AND `c` == 'Blue':
           *   Win (Flash White).
      *   If Button Pressed AND `c` != 'Blue':
           *   Fail (Flash Red).
      *   **Snap** into `pico_forever`.""",
        "flow": "Player must anticipate the color or react instantly.",
        "code": """import machine, time, random
leds = [machine.PWM(machine.Pin(i)) for i in range(16, 19)]
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
colors = [(65535,0,0), (0,65535,0), (0,0,65535), (65535,65535,0)] # R, G, B, Y

def set_color(c):
    for i in range(3): leds[i].duty_u16(c[i])

while True:
    idx = random.randint(0, 3)
    set_color(colors[idx])
    
    start = time.ticks_ms()
    duration = random.randint(500, 1500)
    
    while time.ticks_diff(time.ticks_ms(), start) < duration:
        if btn.value():
            if idx == 2: # Blue
                print("WIN!")
                set_color((65535,65535,65535)); time.sleep(1)
            else:
                print("FAIL!")
                set_color((65535,0,0)); time.sleep(0.1); set_color((0,0,0)); time.sleep(0.1)
                set_color((65535,0,0)); time.sleep(1)
            while btn.value(): pass
            break
        time.sleep(0.01)""",
        "mistakes": ["**Debounce**: Trying to press 'Blue' but catching the tail end of 'Green'.", "**Color Blindness**: Ensure colors are distinct brightnesses or positions possibly."],
        "next": ["**Speed**: Increase cycle speed.", "**Sequence**: Watch specific sequence R-G-B."]
    })

    # 0659: Dusk to Dawn
    projects.append({
        "id": "0659",
        "title": "Automated Night Light Sequences",
        "objective": "Dusk-to-Dawn Controller: Turns on at sunset (low light), stays on all night, turns off at sunrise. Includes Hysteresis to prevent flickering.",
        "concepts": ["Hysteresis", "Schmitt Trigger Logic", "Day/Night Cycle", "Automation"],
        "hardware": ["Pico", "LDR", "LED"],
        "interface": "| **LDR** | GP26 | |\n| **LED** | GP16 | |",
        "blocks": ["*   **from Logic, drag `if_elseif`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**state**: Bool"],
        "guide": """**A. Loop**:
1.  **Read**: `val`=ADC.
2.  **Schmitt Trigger**:
  *   If `val` < 10000 (Very Dark): State=On.
  *   If `val` > 15000 (Bright): State=Off.
  *   (Between 10k-15k, keep previous state).
3.  **Act**:
  *   Write LED `state`.
  *   **Snap** into `pico_forever`.""",
        "flow": "Hysteresis prevents the light from strobing when the light level is right on the edge (e.g., a passing cloud or car headlight).",
        "code": """import machine, time
ldr = machine.ADC(26)
led = machine.Pin(16, machine.Pin.OUT)
state = 0

while True:
    val = ldr.read_u16()
    
    if val < 10000:
        state = 1
    elif val > 15000:
        state = 0
    # Else keep state
    
    led.value(state)
    time.sleep(0.1)""",
        "mistakes": ["**Positive Feedback**: Light from LED shines on LDR -> Sensor says Bright -> Light Off -> Sensor Dark -> Light On. Loop.", "**Thresholds**: Needs manual tuning."],
        "next": ["**Timer Override**: Turn off after 4 hours even if still dark.", "**Dimmer**: PWM brightness proportional to darkness."]
    })

    # 0660: Mastering HSL
    projects.append({
        "id": "0660",
        "title": "Mastering Night Light",
        "objective": "Implement HSL (Hue, Saturation, Lightness) color Mixing. Cycle through the Hue wheel (Rainbow) while keeping Saturation and Lightness max.",
        "concepts": ["Color Spaces", "HSL to RGB Conversion", "Mathematical Modeling", "Rainbow Generation"],
        "hardware": ["Pico", "RGB LED"],
        "interface": "| **RGB** | GP16-18 | |",
        "blocks": ["*   **from Functions, drag `define_function`**", "*   **from Math, drag `arithmetic`**"],
        "vars": ["**h**: Int (0-360)"],
        "guide": """**A. Function**:
1.  **Def HSL_to_RGB(h, s, l)**:
  *   (Complex math to convert angle 0-360 to R,G,B 0-65535).
**B. Loop**:
  *   Loop `h` 0 to 360:
      *   Call `HSL_to_RGB(h, 1.0, 0.5)`.
      *   Wait 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "RGB is hard for humans to visualize ('What is mixed to make Orange?'). HSL is easier ('Orange is Hue 30'). The code translates Human -> Machine.",
        "code": """import machine, time, math
leds = [machine.PWM(machine.Pin(i)) for i in range(16, 19)]
for l in leds: l.freq(1000)

def set_hsl(h, s, l):
    # Simplest HSL to RGB algorithm for Hue cycling
    c = (1 - abs(2*l - 1)) * s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = l - c/2
    
    if 0 <= h < 60: r,g,b = c,x,0
    elif 60 <= h < 120: r,g,b = x,c,0
    elif 120 <= h < 180: r,g,b = 0,c,x
    elif 180 <= h < 240: r,g,b = 0,x,c
    elif 240 <= h < 300: r,g,b = x,0,c
    elif 300 <= h < 360: r,g,b = c,0,x
    else: r,g,b = 0,0,0
    
    leds[0].duty_u16(int((r+m)*65535))
    leds[1].duty_u16(int((g+m)*65535))
    leds[2].duty_u16(int((b+m)*65535))

while True:
    for h in range(360):
        set_hsl(h, 1.0, 0.5)
        time.sleep(0.05)""",
        "mistakes": ["**Float Math**: Python handles floats well on Pico, but they are slower than Ints. Not an issue for lights.", "**Gamma**: Colors might look 'washed out' without gamma correction."],
        "next": ["**Mood Light**: Use Pot to set Hue.", "**Pastels**: Reduce Saturation."]
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
    generate_batch_66_part2()
