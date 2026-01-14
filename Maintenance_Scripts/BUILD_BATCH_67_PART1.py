
import os

def generate_batch_67_part1():
    header = """
# 🏁 Batch 67: Doorbell 4

---
"""
    projects = []

    # 0661: Simple Bell
    projects.append({
        "id": "0661",
        "title": "Introduction to Doorbell",
        "objective": "Simple Doorbell: Pressing the button turns the buzzer on. Releasing it turns the buzzer off (Momentary action).",
        "concepts": ["Momentary Switch", "Audible Signaling", "Direct Drive", "Basic Circuitry"],
        "hardware": ["Pico", "Button", "Buzzer"],
        "interface": "| **Button** | GP14 | Bell Push |\n| **Buzzer** | GP16 | Ringer |",
        "blocks": ["*   **from Smart IO, drag `pico_gpio_read`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Direct Map**:
  *   `state` = Read Button(14).
  *   Write Buzzer(16) `state`.
  *   **Snap** into `pico_forever`.""",
        "flow": "No logic needed. The software acts as a wire connecting input to output.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.Pin(16, machine.Pin.OUT)

while True:
    buz.value(btn.value())
    time.sleep(0.01)""",
        "mistakes": ["**Active vs Passive**: This code assumes an Active Buzzer (voltage = sound). If Passive, use PWM."],
        "next": ["**Latch**: One press rings for 2 seconds (Door chime type).", "**Light**: Add button LED."]
    })

    # 0662: Visual Bell
    projects.append({
        "id": "0662",
        "title": "Blinking Doorbell",
        "objective": "Visual Doorbell: For accessibility (deaf/hard of hearing), flash a bright LED for 5 seconds when the button is pressed.",
        "concepts": ["Accessibility Tech", "Visual Alerts", "Monostable Timer", "Strobe Effect"],
        "hardware": ["Pico", "Button", "High Power LED"],
        "interface": "| **Button** | GP14 | Trigger |\n| **LED** | GP16 | Strobe |",
        "blocks": ["*   **from Loops, drag `repeat`**", "*   **from Smart IO, drag `pico_gpio_toggle`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Check**:
  *   If Button Pressed:
      *   Repeat 20 times:
           *   Toggle LED. Wait 0.1s. (Strobe).
      *   Turn LED Off.
      *   Wait Until Release.
  *   **Snap** into `pico_forever`.""",
        "flow": "The buzzer is replaced by light. The '5 seconds' (simulated here as 2s strobe) ensures the signal is seen even if the glance is brief.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    if btn.value():
        # Flash for ~2s
        for i in range(20):
            led.toggle()
            time.sleep(0.1)
        led.off()
        while btn.value(): time.sleep(0.01)
    time.sleep(0.01)""",
        "mistakes": ["**Current**: High-power LEDs (1W+) need a MOSFET driver. Connecting directly burns the Pico.", "**Duration**: Too short might be missed."],
        "next": ["**Remote**: Send radio signal to remote strobe.", "**Pattern**: Flash 'Door' in Morse."]
    })

    # 0663: Manual (Privacy Switch)
    projects.append({
        "id": "0663",
        "title": "Manual Doorbell Control",
        "objective": "Implement a 'Do Not Disturb' (Privacy) switch. If the switch is ON, the doorbell button is ignored.",
        "concepts": ["Inhibition Logic", "Privacy Modes", "Conditional Execution", "Gatekeeping"],
        "hardware": ["Pico", "Button", "Switch", "Buzzer"],
        "interface": "| **Btn** | GP14 | Ring |\n| **Sw** | GP15 | DND Mode |\n| **Buz** | GP16 | Out |",
        "blocks": ["*   **from Logic, drag `and_operation`**", "*   **from Logic, drag `not_operator`**"],
        "vars": ["**dnd**: Bool"],
        "guide": """**A. Loop**:
1.  **Logic**:
  *   If Button AND (NOT Switch):
      *   Turn Buzzer On.
  *   Else:
      *   Turn Buzzer Off.
  *   **Snap** into `pico_forever`.""",
        "flow": "The switch acts as an 'Enable' signal. If Enable is Low (DND Active), the output is forced Low.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
sw = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.Pin(16, machine.Pin.OUT)

while True:
    if btn.value() and not sw.value():
        buz.on()
    else:
        buz.off() # Mute
    time.sleep(0.01)""",
        "mistakes": ["**UI Feedback**: The visitor doesn't know it's disabled. Maybe flash a Red light at the button.", "**Reverse**: DND usually means Switch Closed."],
        "next": ["**Schedule**: Auto DND between 10PM and 8AM (Automated).", "**Message**: Display 'Go Away' on OLED."]
    })

    # 0664: Sequences (Knock Knock)
    projects.append({
        "id": "0664",
        "title": "Doorbell Sequences",
        "objective": "Play the 'Shave and a Haircut' rhythm when the button is pressed.",
        "concepts": ["Rhythmic Phrases", "Cultural Signals", "Note Durations", "Melody"],
        "hardware": ["Pico", "Buzzer"],
        "interface": "| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Actuators, drag `pwm_tone`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Wait**: Press.
2.  **Play**:
  *   Tone C 0.2s (Shave)
  *   Tone G 0.1s (and)
  *   Tone G 0.1s (a)
  *   Tone A 0.2s (Hair)
  *   Tone G 0.2s (cut)
  *   Silence 0.2s
  *   Tone B 0.2s (Two)
  *   Tone C 0.2s (Bits)
  *   **Snap** into `pico_forever`.""",
        "flow": "Standard novelty doorbells use stored melodies.",
        "code": """import machine, time
buz = machine.PWM(machine.Pin(16))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# C5 G4 G4 A4 G4 (Rest) B4 C5
tune = [(523,0.3),(392,0.15),(392,0.15),(440,0.3),(392,0.3),(0,0.3),(493,0.3),(523,0.3)]

while True:
    if btn.value():
        for note in tune:
            if note[0]:
                buz.freq(note[0]); buz.duty_u16(32768)
            else:
                buz.duty_u16(0)
            time.sleep(note[1])
            buz.duty_u16(0); time.sleep(0.05)
        while btn.value(): pass
    time.sleep(0.01)""",
        "mistakes": ["**Tune**: Notes must be distinct.", "**Tempo**: Too slow sounds weird."],
        "next": ["**Random**: Play 1 of 5 random tunes.", "**Westminster**: The classic chime sequence."]
    })

    # 0665: Interactive (Video Sim)
    projects.append({
        "id": "0665",
        "title": "Interactive Doorbell",
        "objective": "Simulate a Video Doorbell UI: Show 'Connecting...' on OLED, wait delay, then show 'Visitor Detected'.",
        "concepts": ["UI Simulation", "State Feedback", "Latency Simulation", "Display Drivers"],
        "hardware": ["Pico", "OLED (I2C)", "Button"],
        "interface": "| **SDA/SCL** | GP0/1 | Display |\n| **Button** | GP14 | Ring |",
        "blocks": ["*   **from Displays, drag `olc_text`**", "*   **from Time, drag `pico_wait`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Wait**: Press.
2.  **State 1**:
  *   OLED Clear.
  *   Print "Connecting..." at (0,0).
  *   Show. Wait 2s.
3.  **State 2**:
  *   OLED Clear.
  *   Print "VISITOR" at (10, 20).
  *   Draw Rect (Face box).
  *   Show. Wait 3s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Mocking up the User Experience (UX) of a smart device using text and basic graphics.",
        "code": """import machine, time, ssd1306
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value():
        oled.fill(0)
        oled.text("Connecting...", 0, 0)
        oled.show(); time.sleep(2)
        
        oled.fill(0)
        oled.text("VISITOR", 30, 0)
        oled.rect(40, 20, 48, 40, 1) # Face box
        oled.show(); time.sleep(3)
        
        oled.fill(0); oled.show()
    time.sleep(0.1)""",
        "mistakes": ["**I2C Pullups**: OLEDs need pullup resistors on SDA/SCL (often built-in).", "**Burn-in**: Don't leave static text on OLED forever."],
        "next": ["**Camera**: Actually take a photo (requires ArduCAM).", "**Streaming**: Send data via UART."]
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
    generate_batch_67_part1()
