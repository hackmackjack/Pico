
import os

def generate_batch_67_part2():
    projects = []

    # 0666: Smart Knock
    projects.append({
        "id": "0666",
        "title": "Smart Doorbell Switch",
        "objective": "Implemented a 'Secret Knock' detector using a Piezo element. If 3 knocks are detected within 2 seconds, unlock the door (LED).",
        "concepts": ["Vibration Sensing", "Pattern Recognition", "Time Windows", "ADC Thresholding"],
        "hardware": ["Pico", "Piezo Sensor", "LED (Lock)"],
        "interface": "| **Piezo** | GP26 | Vibration |\n| **Lock** | GP16 | Actuator |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Time, drag `time_ticks_ms`**"],
        "vars": ["**knocks**: Int"],
        "guide": """**A. Loop**:
1.  **Detect**:
  *   Wait for Piezo > 10000.
  *   `knocks` += 1.
  *   Wait 0.2s (Debounce).
2.  **Timer**:
  *   If `knocks` == 1: Start Timer.
  *   If Timer > 2000: `knocks` = 0.
3.  **Unlock**:
  *   If `knocks` >= 3:
      *   Unlock (Green). Wait 3s. Relock. `knocks` = 0.
  *   **Snap** into `pico_forever`.""",
        "flow": "We need to reset the count if the user knocks too slowly. This is a basic 'Time Window' filter.",
        "code": """import machine, time
piezo = machine.ADC(26)
lock = machine.Pin(16, machine.Pin.OUT)
knocks = 0
start = 0

while True:
    val = piezo.read_u16()
    if val > 10000:
        print("KNOCK")
        if knocks == 0: start = time.ticks_ms()
        knocks += 1
        time.sleep(0.2)
        
    if knocks > 0:
        if time.ticks_diff(time.ticks_ms(), start) > 2000:
            print("TIMEOUT")
            knocks = 0
            
    if knocks >= 3:
        print("UNLOCK")
        lock.on(); time.sleep(3); lock.off()
        knocks = 0""",
        "mistakes": ["**Sensitivity**: Piezo disks are very sensitive. Might need a resistor (1M Ohm) in parallel to drain charge.", "**False Triggers**: Loud noises might trigger it."],
        "next": ["**Rhythm**: Detect 'Shave and a haircut' rhythm specifically.", "**Servo**: Actually move a bolt."]
    })

    # 0667: Alarm
    projects.append({
        "id": "0667",
        "title": "Doorbell Alarm System",
        "objective": "Tamper Detection: If the doorbell housing is opened (Limit Switch released), sound a continuous alarm.",
        "concepts": ["Tamper Loops", "Normally Closed Logic", "Security Systems", "Persistent Alarm"],
        "hardware": ["Pico", "Limit Switch", "Buzzer"],
        "interface": "| **Limit** | GP14 | Tamper Switch |\n| **Buzzer** | GP16 | Alarm |",
        "blocks": ["*   **from Layers, drag `repeat_until`**", "*   **from Smart IO, drag `pico_gpio_read`**"],
        "vars": ["None"],
        "guide": """**A. Init**: Check Switch.
**B. Loop**:
1.  **Monitor**:
  *   If Switch is OPEN (Low):
      *   Repeat Forever:
           *   Buzzer On. Wait 0.1s.
           *   Buzzer Off. Wait 0.1s.
  *   **Snap** into `pico_forever`.""",
        "flow": "Security loops are almost always 'Normally Closed'. If the wire is cut or the switch opens, the alarm triggers.",
        "code": """import machine, time
tamper = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buz = machine.PWM(machine.Pin(16))

while True:
    if tamper.value() == 1: # PULL_UP means Open = 1? No, Closed=0.
        # Actually with Pull Up: Connected to GND = 0. Open = 1.
        print("ALARM!")
        while True:
            buz.freq(1000); buz.duty_u16(32768); time.sleep(0.1)
            buz.freq(2000); time.sleep(0.1)
    time.sleep(0.1)""",
        "mistakes": ["**Logic**: Verify if the switch connects to GND or 3.3V. NC switches to GND need PULL_UP.", "**Reset**: No way to reset without rebooting. Good for security."],
        "next": ["**Siren**: Two-tone warble.", "**Silent**: Flash silent alarm to internal LED."]
    })

    # 0668: Game
    projects.append({
        "id": "0668",
        "title": "The Doorbell Game",
        "objective": "Guess Who? The doorbell randomly plays a Cat, Dog, or Bell sound. The user guesses which one by pressing 1, 2, or 3 (Simulated by console for now).",
        "concepts": ["Random Selection", "Audio Discrimination", "Game Loops", "User Input"],
        "hardware": ["Pico", "Button", "Buzzer"],
        "interface": "| **Button** | GP14 | Ring |\n| **Buzzer** | GP16 | Audio |",
        "blocks": ["*   **from Math, drag `random_integer`**", "*   **from Logic, drag `if_compare`**"],
        "vars": ["**animal**: Int"],
        "guide": """**A. Loop**:
1.  **Ring**:
  *   Wait for Press.
  *   `animal` = Random(1, 3).
2.  **Play**:
  *   If 1: Play "Meow" (High pitch slide).
  *   If 2: Play "Woof" (Low pitch burst).
  *   If 3: Play "Ding" (Mid tone).
3.  **Prompt**:
  *   Print "Guess?".
  *   **Snap** into `pico_forever`.""",
        "flow": "Simple logic to vary the feedback.",
        "code": """import machine, time, random
buz = machine.PWM(machine.Pin(16))
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btn.value():
        choice = random.randint(1, 3)
        if choice == 1: # Cat
             for f in range(1000, 2000, 50): buz.freq(f); buz.duty_u16(32768); time.sleep(0.01)
        elif choice == 2: # Dog
             buz.freq(200); buz.duty_u16(32768); time.sleep(0.1)
        else: # Bell
             buz.freq(600); buz.duty_u16(32768); time.sleep(0.5)
        
        buz.duty_u16(0)
        print(f"Played: {choice}")
        while btn.value(): pass
    time.sleep(0.1)""",
        "mistakes": ["**Audio Quality**: Square waves (PWM) make terrible animal sounds. It's symbolic.", "**Blocking**: Can't press again while playing."],
        "next": ["**MP3**: Use a DFPlayer Mini for real sounds.", "**Score**: Keep score of guesses."]
    })

    # 0669: Automated
    projects.append({
        "id": "0669",
        "title": "Automated Doorbell",
        "objective": "Data Logger: Count unique visitors. Increment the count every time the bell rings and print 'Visitor #X' to the console.",
        "concepts": ["Variables (Counters)", "Data Persistence", "Event Logging", "Incrementing"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Ring |",
        "blocks": ["*   **from Variables, drag `change_variable`**", "*   **from Text, drag `text_join`**"],
        "vars": ["**visits**: Int"],
        "guide": """**A. Init**: `visits` = 0.
**B. Loop**:
1.  **Wait**: Press.
2.  **Count**:
  *   `visits` += 1.
  *   Print "Visitor #" + `visits`.
3.  **Wait Release**:
  *   Wait until Button Released.
  *   **Snap** into `pico_forever`.""",
        "flow": "Without 'Wait Release', a single long press counts as hundreds of visitors.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
visits = 0

while True:
    if btn.value():
        visits += 1
        print(f"Visitor #{visits}")
        while btn.value(): time.sleep(0.01)
    time.sleep(0.01)""",
        "mistakes": ["**Power Loss**: Variables reset when unplugged. Need SD card or Flash memory to save.", "**Bounce**: Mechanical bounce might double count."],
        "next": ["**File Write**: Save to `log.txt`.", "**Timestamp**: Add time of day."]
    })

    # 0670: Mastering
    projects.append({
        "id": "0670",
        "title": "Mastering Doorbell",
        "objective": "IoT Simulator: Format doorbell events as MQTT JSON payloads ('home/doorbell', '{state: ON}'). Print to console.",
        "concepts": ["IoT Protocols", "JSON Formatting", "String Manipulation", "Home Automation"],
        "hardware": ["Pico", "Button"],
        "interface": "| **Button** | GP14 | Ring |",
        "blocks": ["*   **from Text, drag `text_join`**", "*   **from Functions, drag `define_function`**"],
        "vars": ["**topic**: String", "**payload**: String"],
        "guide": """**A. Loop**:
1.  **Wait**: Press.
2.  **Format**:
  *   `topic` = "home/doorbell".
  *   `payload` = '{"state": "ON", "ts": ' + time + '}'.
  *   Print `topic` + " -> " + `payload`.
3.  **Wait Release**:
  *   `payload` = '{"state": "OFF"}'.
  *   Print Payload.
  *   **Snap** into `pico_forever`.""",
        "flow": "MQTT is the standard for Home Assistant / Smart Home Hubs. Strings must be exact.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def publish(topic, payload):
    print(f"MQTT PUB: [{topic}] {payload}")

while True:
    if btn.value():
        publish("home/doorbell", '{"state": "ON"}')
        while btn.value(): time.sleep(0.01)
        publish("home/doorbell", '{"state": "OFF"}')
    time.sleep(0.01)""",
        "mistakes": ["**Quotes**: JSON requires double quotes. Python strings can use single quotes to wrap them.", "**Network**: This example simulates the data format, not the WiFi connection."],
        "next": ["**WiFi**: Use `network` library to actually send it.", "**Subscribe**: Listen for 'home/doorbell/mute'."]
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
    generate_batch_67_part2()
