
import os

def generate_batch_63_part2():
    projects = []

    # 0626: Doorbell
    projects.append({
        "id": "0626",
        "title": "Smart Sound & Music Switch",
        "objective": "Select between two distinct sound effects ('Ding Dong' vs 'Buzz') using a toggle switch, triggered by a pushbutton.",
        "concepts": ["Mode Selection", "Trigger Logic", "Sound Design", "User Configuration"],
        "hardware": ["Pico", "Switch", "Button", "Buzzer"],
        "interface": "| **Switch** | GP14 | Mode |\n| **Button** | GP15 | Trigger |\n| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Actuators, drag `pwm_tone`**"],
        "vars": ["**mode**: Boolean"],
        "guide": """**A. Loop**:
1.  **Wait**:
  *   Wait for Button Press.
2.  **Select**:
  *   If Switch is On:
      *   Tone 600Hz 0.2s.
      *   Tone 400Hz 0.4s (Ding Dong).
  *   Else:
      *   Tone 100Hz 0.1s.
      *   Tone 0Hz 0.1s.
      *   Tone 100Hz 0.1s (Buzz).
  *   Wait Release.
  *   **Snap** into `pico_forever`.""",
        "flow": "The switch sets the behavior (Personality). The button executes the behavior (Action).",
        "code": """import machine, time
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.PWM(machine.Pin(16))

while True:
    if btn.value():
        if sw.value():
            # Ding Dong
            buzzer.freq(600); buzzer.duty_u16(32768); time.sleep(0.2)
            buzzer.freq(400); time.sleep(0.4)
            buzzer.duty_u16(0)
        else:
            # Buzz
            buzzer.freq(100); buzzer.duty_u16(32768); time.sleep(0.1)
            buzzer.duty_u16(0); time.sleep(0.1)
            buzzer.duty_u16(32768); time.sleep(0.1)
            buzzer.duty_u16(0)
        while btn.value(): time.sleep(0.01)
    time.sleep(0.01)""",
        "mistakes": ["**Switch Bounce**: Not critical for mode selection strings.", "**Tone Duration**: Ensure `duty=0` is called after tones end."],
        "next": ["**Random**: Play random sound if switch is in middle (requires 3-way switch).", "**Jingle**: Play melody if button held > 2s."]
    })

    # 0627: Car Alarm
    projects.append({
        "id": "0627",
        "title": "Sound & Music Alarm System",
        "objective": "Simulate a car alarm that cycles through 3 distinct patterns (Wail, Yelp, Phaser) randomly every 5 seconds.",
        "concepts": ["Random Selection", "Modulation Patterns", "Non-Blocking loops", "Intimidation Audio"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | Audio |",
        "blocks": ["*   **from Math, drag `random_integer`**", "*   **from Loops, drag `repeat`**"],
        "vars": ["**mode**: Int (0-2)"],
        "guide": """**A. Loop**:
1.  **Pick Mode**:
  *   `mode` = Random(0, 2).
  *   `end` = `time` + 5000.
2.  **Play**:
  *   Loop while `time` < `end`:
      *   If `mode` == 0 (Wail): Sweep 500-1500Hz in 0.5s.
      *   If `mode` == 1 (Yelp): Sweep 500-1500Hz in 0.1s.
      *   If `mode` == 2 (Phaser): Tone 1000Hz 0.05s, 0Hz 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Alarms change patterns to prevent listener fatigue (habituation). This script reshuffles the sonic attack every 5s.",
        "code": """import machine, time, random
buzzer = machine.PWM(machine.Pin(15))

while True:
    mode = random.randint(0, 2)
    start = time.ticks_ms()
    print(f"MODE: {mode}")
    
    while time.ticks_diff(time.ticks_ms(), start) < 5000:
        if mode == 0: # Wail
            for f in range(500, 1500, 50):
                buzzer.freq(f); buzzer.duty_u16(32768); time.sleep(0.02)
        elif mode == 1: # Yelp
            for f in range(500, 1500, 200):
                buzzer.freq(f); buzzer.duty_u16(32768); time.sleep(0.02)
        else: # Phaser
            buzzer.freq(1000); buzzer.duty_u16(32768); time.sleep(0.05)
            buzzer.duty_u16(0); time.sleep(0.05)
    
    buzzer.duty_u16(0)
    time.sleep(0.5)""",
        "mistakes": ["**Loop Traps**: If inner loops (sweeps) take too long, the 5s timer isn't checked often enough.", "**Power**: Buzzers draw current; driving too hard can reset Pico."],
        "next": ["**Two-Tone**: Alternate between 800Hz and 1200Hz (European).", "**Motion Trigger**: Only alarm if acceleration detected."]
    })

    # 0628: Memory Tone
    projects.append({
        "id": "0628",
        "title": "The Sound & Music Game",
        "objective": "Audio Memory Game. Listen to 3 tones (Low, Mid, High). Reproduce the sequence using 3 buttons.",
        "concepts": ["Audio Recall", "Sequence Matching", "Game Logic", "Input Mapping"],
        "hardware": ["Pico", "Buzzer", "3 Buttons"],
        "interface": "| **Buzzer** | GP16 | Audio |\n| **Btns** | GP13-15 | L, M, H |",
        "blocks": ["*   **from Variables, drag `list_append`**", "*   **from Logic, drag `list_equals`**"],
        "vars": ["**seq**: List", "**user**: List"],
        "guide": """**A. Init**: `seq` = [].
**B. Play**:
1.  **Add**: Append Random(13,15) to `seq`.
2.  **Demonstrate**:
  *   Loop `pin` in `seq`:
       *   Play Tone (Pin-based freq).
       *   Wait.
3.  **Input**:
  *   Loop `len(seq)` times:
       *   Wait for any Btn.
       *   Play Tone.
       *   Append Input to `user`.
4.  **Check**:
  *   If `user` != `seq`: Game Over.
  *   **Snap** into `pico_forever`.""",
        "flow": "Classic Simon, but purely auditory. The brain maps spatial buttons to pitch.",
        "code": """import machine, time, random
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(13, 16)]
buzzer = machine.PWM(machine.Pin(16))
freqs = [200, 500, 800] # Map 13->200, 14->500, 15->800
seq = []

while True:
    # Grow
    seq.append(random.randint(0, 2))
    
    # Show
    print("LISTEN")
    for item in seq:
        buzzer.freq(freqs[item]); buzzer.duty_u16(32768); time.sleep(0.5); buzzer.duty_u16(0); time.sleep(0.2)
    
    # Input
    print("REPEAT")
    user = []
    for _ in range(len(seq)):
        pressed = -1
        while pressed == -1:
            for i in range(3):
                 if btns[i].value(): pressed = i; break
        # Feedback
        buzzer.freq(freqs[pressed]); buzzer.duty_u16(32768); time.sleep(0.2); buzzer.duty_u16(0)
        while btns[pressed].value(): pass
        user.append(pressed)
        
    if user != seq:
        print("FAIL"); buzzer.freq(100); buzzer.duty_u16(32768); time.sleep(1); break
    time.sleep(1)""",
        "mistakes": ["**Pitch Mapping**: Ensure button order matches pitch order (Left=Low, Right=High).", "**Speed**: If demonstration is too fast, memory fails."],
        "next": ["**Blind Mode**: No console output.", "**Tempo**: Speed up every round."]
    })

    # 0629: Automated Volume
    projects.append({
        "id": "0629",
        "title": "Automated Sound & Music",
        "objective": "Simulate 'Fade In' volume control by ramping the PWM duty cycle while keeping frequency constant.",
        "concepts": ["Volume Envelope", "Attack Ramp", "Duty Cycle vs Frequency", "Dynamics"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | Audio |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**vol**: Int (0-65535)"],
        "guide": """**A. Init**: Freq 440Hz.
**B. Loop**:
1.  **Ramp Up**:
  *   Loop `vol` 0 to 65000 step 1000:
      *   Set Duty `vol`.
      *   Wait 0.05s.
  *   **Snap** into `pico_forever`.
2.  **Hold**:
  *   Wait 1s.
3.  **Cut**:
  *   Set Duty 0.
  *   Wait 1s.
  *   **Snap** below ramp.""",
        "flow": "This creates a 'Swell' effect. Note: On piezo buzzers, volume control via PWM is limited and non-linear, but the concept stands.",
        "code": """import machine, time
buzzer = machine.PWM(machine.Pin(15))
buzzer.freq(440)

while True:
    for vol in range(0, 65535, 500):
        buzzer.duty_u16(vol)
        time.sleep(0.01)
    time.sleep(1)
    buzzer.duty_u16(0)
    time.sleep(1)""",
        "mistakes": ["**Active Buzzer**: Cannot change volume or frequency. Required Passive.", "**Clicking**: Large steps in duty cycle cause clicks."],
        "next": ["**Decay**: Fade out slowly.", "**ADSR**: Attack, Decay, Sustain, Release envelope."]
    })

    # 0630: Mario Theme
    projects.append({
        "id": "0630",
        "title": "Mastering Sound & Music",
        "objective": "Play a complex melody (Mario Theme) using a list of tuples `(Note, Duration)` to handle rhythm.",
        "concepts": ["Data Structures (Tuples)", "Rhythmic Notation", "Music Transcription", "Complex Sequencing"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP15 | Audio |",
        "blocks": ["*   **from Variables, drag `create_list`**", "*   **from Logic, drag `list_get_item`**"],
        "vars": ["**song**: List of (Freq, Time)"],
        "guide": """**A. Init**: 
  *   `song` = [(659, 0.1), (659, 0.1), (0, 0.1), (659, 0.1), (0, 0.1), (523, 0.1), (659, 0.1), (0, 0.1), (784, 0.2)...]
**B. Loop**:
1.  **Play**:
  *   Loop `note` in `song`:
      *   `freq` = `note[0]`.
      *   `dur` = `note[1]`.
      *   If `freq` > 0: Play Freq.
      *   Else: Silence.
      *   Wait `dur`.
      *   Silence. Wait 0.05s.
  *   **Snap** into `pico_forever`.""",
        "flow": "The first true 'Music Engine'. It decouples Note (Frequency) from Duration (Time), allowing complex rhythms (eighth notes, quarter notes, rests).",
        "code": """import machine, time
buzzer = machine.PWM(machine.Pin(15))
# E5, E5, Rest, E5, Rest, C5, E5, Rest, G5
song = [
    (659, 0.15), (659, 0.15), (0, 0.15), (659, 0.15), (0, 0.15), (523, 0.15), (659, 0.15), (0, 0.15), (784, 0.4)
]

while True:
    for note in song:
        freq = note[0]; dur = note[1]
        if freq > 0:
            buzzer.freq(freq)
            buzzer.duty_u16(32768)
        else:
            buzzer.duty_u16(0)
        time.sleep(dur)
        buzzer.duty_u16(0) # Artifact gap
        time.sleep(0.02)
    time.sleep(2)""",
        "mistakes": ["**Tuple Indexing**: `note[0]` vs `note[1]`. Python uses 0-based indexing.", "**Synchrony**: The gap (0.02) adds to total time. Reduce `time.sleep(dur)` by 0.02 to keep tempo strict."],
        "next": ["**Full Song**: Transcribe the whole theme.", "**Transpose**: Add variable `offset` to all frequencies."]
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
    generate_batch_63_part2()
