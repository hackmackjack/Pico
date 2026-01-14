
import os

def generate_batch_63_part1():
    header = """
# 🏁 Batch 63: Sound & Music 4

---
"""
    projects = []

    # 0621: Rising Tone
    projects.append({
        "id": "0621",
        "title": "Introduction to Sound & Music",
        "objective": "Generate a rising 'Whoop' sound by looping frequency from 100Hz to 1000Hz.",
        "concepts": ["Frequency Sweep", "For Loops", "Audio Synthesis", "Ramping"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | PWM Output |",
        "blocks": ["*   **from Actuators, drag `pwm_freq`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**freq**: Integer"],
        "guide": """**A. Init**: Setup PWM GP15.
**B. Loop**:
1.  **Sweep**:
  *   From **Loops**, loop `freq` from 100 to 1000 by 10.
      *   Set PWM Freq to `freq`.
      *   Set Duty to 50%.
      *   Wait 0.01s.
      *   **Snap** into `pico_forever`.
2.  **Reset**:
  *   Set Duty to 0.
  *   Wait 0.5s.
  *   **Snap** below loop.""",
        "flow": "By changing the frequency rapidly in small steps, we create the illusion of a continuous slide (glissando).",
        "code": """import machine, time
buzzer = machine.PWM(machine.Pin(15))

while True:
    for freq in range(100, 1001, 10):
        buzzer.freq(freq)
        buzzer.duty_u16(32768)
        time.sleep(0.01)
    
    buzzer.duty_u16(0)
    time.sleep(0.5)""",
        "mistakes": ["**Duty Cycle**: If Duty is 0, you hear nothing regardless of Frequency.", "**Step Size**: Too large steps (e.g. 100Hz) sound like a staircase, not a slide."],
        "next": ["**Falling Tone**: 1000 down to 100.", "**Siren**: Up then Down continuously."]
    })

    # 0622: Metronome
    projects.append({
        "id": "0622",
        "title": "Blinking Sound & Music",
        "objective": "Create a precise metronome that beeps for 50ms every 1 second.",
        "concepts": ["Precision Timing", "Duty Cycle Modulation", "Short Durations", "Rhythm"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | Audio |",
        "blocks": ["*   **from Actuators, drag `pwm_tone`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Init**: Setup PWM.
**B. Loop**:
1.  **Tick**:
  *   Set Freq 1000Hz.
  *   Set Duty 50%.
  *   Wait 0.05s.
  *   Set Duty 0%.
  *   Wait 0.95s.
  *   **Snap** into loop.""",
        "flow": "Total cycle = 0.05 + 0.95 = 1.00s (60 BPM). The short 'On' time creates a sharp 'Click' or 'Tick' sound.",
        "code": """import machine, time
buzzer = machine.PWM(machine.Pin(15))
buzzer.freq(1000)

while True:
    buzzer.duty_u16(32768)
    time.sleep(0.05)
    buzzer.duty_u16(0)
    time.sleep(0.95)""",
        "mistakes": ["**Drift**: `sleep` isn't perfectly accurate. Over an hour, it might drift.", "**Blocking**: The code does nothing else while waiting."],
        "next": ["**Selectable BPM**: Use a variable `wait_time` based on (60/BPM).", "**Visual**: Flash LED with the beep."]
    })

    # 0623: 2-Key Piano
    projects.append({
        "id": "0623",
        "title": "Manual Sound & Music Control",
        "objective": "Simulate a keyboard: Button A plays 'C', Button B plays 'E'. Pressing both play 'G' (Chord Logic).",
        "concepts": ["Polyphony Simulation", "Input Combinations", "Frequency Mapping", "Priority Logic"],
        "hardware": ["Pico", "2 Buttons", "Buzzer"],
        "interface": "| **Btn A** | GP14 | Key C |\n| **Btn B** | GP15 | Key E |\n| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Actuators, drag `pwm_freq`**"],
        "vars": ["None"],
        "guide": """**A. Init**: Setup IOs.
**B. Loop**:
1.  **Check Chord**:
  *   If A AND B: Freq=392 (G). Duty=50%.
  *   Else If A: Freq=261 (C). Duty=50%.
  *   Else If B: Freq=329 (E). Duty=50%.
  *   Else: Duty=0.
  *   **Snap** into loop.""",
        "flow": "We check the most specific condition (A+B) first. If we checked A first, holding A+B would just play A. Order matters.",
        "code": """import machine, time
btnA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.PWM(machine.Pin(16))

while True:
    if btnA.value() and btnB.value():
        buzzer.freq(392)
        buzzer.duty_u16(32768)
    elif btnA.value():
        buzzer.freq(261)
        buzzer.duty_u16(32768)
    elif btnB.value():
        buzzer.freq(329)
        buzzer.duty_u16(32768)
    else:
        buzzer.duty_u16(0)
    time.sleep(0.01)""",
        "mistakes": ["**Priority**: Putting the single button checks before the double button check.", "**Stutter**: Re-setting frequency every 0.01s might cause audio artifacts."],
        "next": ["**Shift Octave**: Add a 3rd button to double the frequencies (High C/E).", "**Arpeggiator**: Play C-E-G rapidly if both held."]
    })

    # 0624: Melody Array
    projects.append({
        "id": "0624",
        "title": "Sound & Music Sequences",
        "objective": "Play a tune stored in a list: `[261, 293, 329, 349, 392]` (C-D-E-F-G).",
        "concepts": ["Arrays/Lists", "Data-Driven Logic", "Iteration", "Sequencing"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | Audio |",
        "blocks": ["*   **from Variables, drag `create_list`**", "*   **from Loops, drag `for_in_list`**"],
        "vars": ["**melody**: List of Ints"],
        "guide": """**A. Init**:
  *   `melody` = [261, 293, 329, 349, 392].
**B. Loop**:
1.  **Play**:
  *   Loop `note` in `melody`:
      *   Set Freq `note`. Duty 50%.
      *   Wait 0.5s.
      *   Set Duty 0.
      *   Wait 0.1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The data (notes) is separated from the logic (player). To change the song, you only change the list, not the code structure.",
        "code": """import machine, time
buzzer = machine.PWM(machine.Pin(15))
melody = [261, 293, 329, 349, 392]

while True:
    for note in melody:
        buzzer.freq(note)
        buzzer.duty_u16(32768)
        time.sleep(0.5)
        buzzer.duty_u16(0)
        time.sleep(0.1)
    time.sleep(1)""",
        "mistakes": ["**Legato**: Forgetting the silence/gap causes notes to bleed together.", "**Empty List**: Loops on empty lists do nothing."],
        "next": ["**Durations**: Use a second list for timing.", "**Reverse**: Play `reversed(melody)`."]
    })

    # 0625: Theremin
    projects.append({
        "id": "0625",
        "title": "Interactive Sound & Music",
        "objective": "Use an LDR to control pitch: Dark environment = Low Pitch, Bright environment = High Pitch.",
        "concepts": ["Analog Mapping", "Sensor Modulation", "Continuous Control", "Theremin Physics"],
        "hardware": ["Pico", "LDR", "Buzzer"],
        "interface": "| **LDR** | GP26 | Light Input |\n| **Buzzer** | GP16 | Audio Output |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Math, drag `map_range`**"],
        "vars": ["**light**: Int", "**pitch**: Int"],
        "guide": """**A. Loop**:
1.  **Read**:
  *   `light` = Read Analog(26).
2.  **Calc**:
  *   `pitch` = Map `light` (0-65535) to (200-2000).
3.  **Output**:
  *   Set PWM Freq `pitch`.
  *   Wait 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Direct translation of physical quantity (photons) to physical quantity (sound waves/hertz).",
        "code": """import machine, time
ldr = machine.ADC(26)
buzzer = machine.PWM(machine.Pin(16))
buzzer.duty_u16(32768)

while True:
    light = ldr.read_u16()
    pitch = int(200 + (light/65535 * 1800))
    buzzer.freq(pitch)
    time.sleep(0.05)""",
        "mistakes": ["**Zero Division**: Map function handles ranges, but manual math must allow for 0.", "**Sampling Rate**: Too slow (e.g. 0.5s) feels laggy."],
        "next": ["**Quantizer**: Snap pitch to nearest Musical Note (C, D, E).", "**Volume**: Use a Potentiometer for volume control."]
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
    generate_batch_63_part1()
