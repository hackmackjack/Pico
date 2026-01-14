
import os

def generate_batch_68_part1():
    header = """
# 🏁 Batch 68: Reaction Game 4

---
"""
    projects = []

    # 0671: Intro Reaction
    projects.append({
        "id": "0671",
        "title": "Introduction to Reaction Game",
        "objective": "Simple reaction timer: Wait for LED to turn Green, then press the button as fast as possible. Print time.",
        "concepts": ["Reflex Measurement", "Random Delays", "Time Differentials", "Visual Cues"],
        "hardware": ["Pico", "R/Y/G LEDs", "Button"],
        "interface": "| **LEDs** | GP16-18 | Traffic |\n| **Button** | GP14 | Trigger |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Math, drag `random_integer`**"],
        "vars": ["**start**: Int", "**reaction**: Int"],
        "guide": """**A. Loop**:
1.  **Wait**:
  *   Turn Red On. Wait Random(2, 5)s.
2.  **Go**:
  *   Turn Red Off, Green On.
  *   `start` = `time`.
  *   Wait until Button Pressed.
  *   `reaction` = `time` - `start`.
3.  **Result**:
  *   Print `reaction` + "ms".
  *   If `reaction` < 200: Print "Superhuman!".
  *   Wait 2s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Standard drag race tree logic. The random delay prevents predicting the start.",
        "code": """import machine, time, random
red = machine.Pin(16, machine.Pin.OUT)
grn = machine.Pin(18, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    red.on(); grn.off()
    time.sleep(random.uniform(2, 5))
    
    red.off(); grn.on()
    start = time.ticks_ms()
    while not btn.value(): pass # Blocking wait
    
    reaction = time.ticks_diff(time.ticks_ms(), start)
    print(f"Time: {reaction}ms")
    
    if reaction < 200: print("FAST!")
    elif reaction > 1000: print("SLOW!")
    
    time.sleep(2)""",
        "mistakes": ["**Cheating**: Holding the button down before Green causes 0ms time.", "**Floating**: If pull-down missing, button reads random."],
        "next": ["**Anti-Cheat**: Check if button is pressed *during* Red phase.", "**Average**: Calc avg of 5 tries."]
    })

    # 0672: Scanning
    projects.append({
        "id": "0672",
        "title": "Blinking Reaction Game",
        "objective": "Catch the Light: 5 LEDs scan Left to Right. Press the button exactly when the middle LED (3rd) is lit.",
        "concepts": ["Spatial Timing", "Scanning Arrays", "Precision Input", "Arcade Physics"],
        "hardware": ["Pico", "5 LEDs", "Button"],
        "interface": "| **LEDs** | GP10-14 | Array |\n| **Button** | GP15 | Stop |",
        "blocks": ["*   **from Loops, drag `for_in_list`**", "*   **from Logic, drag `break_loop`**"],
        "vars": ["**current**: Int"],
        "guide": """**A. Init**: `pins` = [10,11,12,13,14].
**B. Loop**:
1.  **Scan**:
  *   Loop `i` 0 to 4:
      *   Turn Pin `pins[i]` On.
      *   Wait 0.1s.
      *   If Button:
           *   If `i` == 2: Win (Flash All).
           *   Else: Fail (Flash Red).
           *   Break Loop.
      *   Turn Pin `pins[i]` Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "Classic arcade ticket game logic. The speed determines difficulty.",
        "code": """import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(10, 15)]
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    for i in range(5):
        leds[i].on()
        start = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start) < 100:
            if btn.value():
                if i == 2:
                    print("WIN")
                    for _ in range(5): 
                        for l in leds: l.toggle()
                        time.sleep(0.1)
                else:
                    print("MISS")
                    leds[i].off()
                    time.sleep(1)
                while btn.value(): pass # Debounce
                break
        leds[i].off()""",
        "mistakes": ["**Blocking Wait**: Using `time.sleep` blocks the button check. Use `ticks_ms` loop for responsiveness.", "**Index**: Arrays are 0-indexed, so 3rd LED is index 2."],
        "next": ["**Bounce**: Scan L->R->L.", "**Speed Up**: Decrease delay every win."]
    })

    # 0673: Manual Control (False Start)
    projects.append({
        "id": "0673",
        "title": "Manual Reaction Game Control",
        "objective": "Implement False Start detection. If the user presses the button while the Red light is still on, Disqualify them.",
        "concepts": ["State Validation", "Premature Input", "Fairness Logic", "Error Conditions"],
        "hardware": ["Pico", "R/G LEDs", "Button"],
        "interface": "| **Red** | GP16 | Wait |\n| **Green** | GP17 | Go |\n| **Button** | GP14 | Trigger |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Loops, drag `break_loop`**"],
        "vars": ["**fault**: Bool"],
        "guide": """**A. Loop**:
1.  **Wait Phase**:
  *   Red On.
  *   Loop 100 times (Wait loop 2s):
      *   If Button:
           *   Print "FALSE START".
           *   Flash Red. Break Loop.
      *   Wait 0.02s.
2.  **Go Phase**:
  *   (Only if no fault)
  *   Red Off, Green On.
  *   Wait for Button -> Print Time.
  *   **Snap** into `pico_forever`.""",
        "flow": "Polling during the wait period is essential to catch cheaters.",
        "code": """import machine, time, random
red = machine.Pin(16, machine.Pin.OUT)
grn = machine.Pin(17, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    red.on(); grn.off()
    fault = False
    delay = random.randint(200, 500) # x10ms = 2-5s
    
    for _ in range(delay):
        if btn.value():
            print("FALSE START!")
            for _ in range(5): red.toggle(); time.sleep(0.1)
            fault = True
            break
        time.sleep(0.01)
        
    if not fault:
        red.off(); grn.on()
        start = time.ticks_ms()
        while not btn.value(): pass
        print(f"{time.ticks_diff(time.ticks_ms(), start)}ms")
        grn.off()
    
    while btn.value(): time.sleep(0.01)
    time.sleep(2)""",
        "mistakes": ["**Wait Loop**: `time.sleep(5)` checks nothing. Must loop small Sleeps.", "**Release**: Wait for button release at end of round."],
        "next": ["**Penalty**: Add +2s to time instead of DQ.", "**Random**: Vary the wait time."]
    })

    # 0674: Sequences
    projects.append({
        "id": "0674",
        "title": "Reaction Game Sequences",
        "objective": "Memory/Simon Says: Flash a sequence (e.g. Red-Green-Blue). User must press the corresponding buttons in order.",
        "concepts": ["Short Term Memory", "Sequence Arrays", "Multiple Inputs", "Verification Loop"],
        "hardware": ["Pico", "3 LEDs", "3 Buttons"],
        "interface": "| **LEDs** | GP16-18 | R/G/B |\n| **Btns** | GP13-15 | In |",
        "blocks": ["*   **from Variables, drag `list_append`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**moves**: List"],
        "guide": """**A. Init**: `moves`=[].
**B. Loop**:
1.  **Add**: Append Random(0,2) to `moves`.
2.  **Show**:
  *   Loop `m` in `moves`:
      *   Flash LED[`m`].
3.  **Input**:
  *   Loop `i` 0 to len(`moves`):
      *   Wait for *Any* Button.
      *   If Button != `moves[i]`: Fail. Beep.
  *   **Snap** into `pico_forever`.""",
        "flow": "Classic Simon game. Increases in difficulty indefinitely.",
        "code": """import machine, time, random
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 19)]
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(13, 16)]
seq = []

while True:
    seq.append(random.randint(0, 2))
    
    # Show
    for s in seq:
        leds[s].on(); time.sleep(0.5); leds[s].off(); time.sleep(0.2)
        
    # Read
    for s in seq:
        pressed = -1
        while pressed == -1:
            for i in range(3):
                if btns[i].value(): pressed = i
        
        leds[pressed].on() # Feedback
        while btns[pressed].value(): pass
        leds[pressed].off()
        
        if pressed != s:
            print("GAME OVER")
            seq = []
            time.sleep(2)
            break
    time.sleep(1)""",
        "mistakes": ["**Feedback**: User needs to see their own press (LED lights up).", "**Infinite Wait**: If user walks away, code hangs. Add timeout."],
        "next": ["**Sound**: Add tones to colors.", "**Speed**: Show faster as list grows."]
    })

    # 0675: Interactive (Vibration)
    projects.append({
        "id": "0675",
        "title": "Interactive Reaction Game",
        "objective": "Non-Visual Reaction: Wait for Vibration Motor to buzz. Press button ASAP. Measures tactile response time.",
        "concepts": ["Haptic Cues", "Reaction Time (Tactile vs Visual)", "Motor Control", "Human Performance"],
        "hardware": ["Pico", "Vibration Motor", "Button"],
        "interface": "| **Motor** | GP16 | Stimulus |\n| **Button** | GP14 | Response |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Wait**:
  *   Wait Random(2, 6)s.
2.  **Stimulus**:
  *   Motor On.
  *   `start` = `time`.
3.  **Response**:
  *   Wait for Button.
  *   Motor Off.
  *   Print `time` - `start`.
  *   **Snap** into `pico_forever`.""",
        "flow": "Tactile reaction time is often faster than visual (approx 150ms vs 250ms).",
        "code": """import machine, time, random
motor = machine.Pin(16, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print("WAIT...")
    time.sleep(random.uniform(2, 6))
    
    motor.value(1)
    start = time.ticks_ms()
    while not btn.value(): pass
    
    diff = time.ticks_diff(time.ticks_ms(), start)
    motor.value(0)
    print(f"Reaction: {diff}ms")
    
    while btn.value(): time.sleep(0.01)
    time.sleep(2)""",
        "mistakes": ["**Motor Latency**: Mechanical motors take ~20ms to spin up. ERMs (Eccentric Rotating Mass) are laggy.", "**Noise**: Motor sound might cue the user before the vibration does."],
        "next": ["**Comparison**: Run Visual vs Tactile test.", "**Distraction**: Play random sounds during wait."]
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
    generate_batch_68_part1()
