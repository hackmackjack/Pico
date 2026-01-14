
import os

def generate_batch_61_part2():
    projects = []
    
    # 0605: Noise Meter
    projects.append({
        "id": "0605",
        "title": "Interactive LED Patterns",
        "objective": "Create a VU Meter that lights up 1, 2, or 3 LEDs based on microphone sound level.",
        "concepts": ["Analog Input", "Threshold Comparison", "Level Metering", "Conditionals"],
        "hardware": ["Pico", "Microphone Module (Analog)", "3 LEDs"],
        "interface": "| **Mic** | GP26 | Analog Input |\n| **LED 1** | GP16 | Low |\n| **LED 2** | GP17 | Med |\n| **LED 3** | GP18 | High |",
        "blocks": ["*   **from Smart IO, drag `pico_analog_read`**", "*   **from Logic, drag `if_elseif`**", "*   **from Smart IO, drag `pico_gpio_write`**"],
        "vars": ["**soundLevels**: Integer (ADC Value)"],
        "guide": """**A. Initialization Phase**
1.  **Setup**:
  *   From **Smart IO**, setup GP26 as ADC.
  *   From **Smart IO**, setup GP16-18 as Output.
  *   **Snap** into setup.

**B. Main Loop Phase**
1.  **Read**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Smart IO**, read GP26 -> `level`.
  *   **Snap** into loop.
2.  **Display**:
  *   From **Logic**, if `level` > 40000:
      *   Turn On GP16, 17, 18.
  *   Else If `level` > 20000:
      *   Turn On GP16, 17. Turn Off GP18.
  *   Else If `level` > 5000:
      *   Turn On GP16. Turn Off GP17, 18.
  *   Else:
      *   Turn Off All.
  *   **Snap** below read.""",
        "flow": "The Microphon converts sound pressure to voltage. The ADC converts voltage to a number (0-65535). The code works like a ladder: louder sounds climb higher up the `if/else` ladder, lighting more LEDs.",
        "code": """import machine, time
mic = machine.ADC(26)
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 19)]

while True:
    level = mic.read_u16()
    if level > 40000:
        for l in leds: l.value(1)
    elif level > 20000:
        leds[0].value(1); leds[1].value(1); leds[2].value(0)
    elif level > 5000:
        leds[0].value(1); leds[1].value(0); leds[2].value(0)
    else:
        for l in leds: l.value(0)
    time.sleep(0.05)""",
        "mistakes": ["**Sensitivity**: Every mic is different. Adjust the 5000/20000/40000 thresholds.", "**Noise**: Use a running average (mean) for smoother display."],
        "next": ["**Peak Hold**: Keep the highest LED on for 1 second.", "**Color**: Use RGB LED instead of 3 separate LEDs."]
    })

    # 0606: Timeout Light
    projects.append({
        "id": "0606",
        "title": "Smart LED Patterns Switch",
        "objective": "Implement an energy-saving light that turns on via button and stays on if motion is detected, otherwise turning off after 10s.",
        "concepts": ["Timer Reset", "Sensor Fusion", "State Maintenance", "Energy Efficiency"],
        "hardware": ["Pico", "Button", "PIR Sensor", "LED"],
        "interface": "| **Button** | GP14 | Trigger |\n| **PIR** | GP15 | Keep-Alive |\n| **LED** | GP16 | Output |",
        "blocks": ["*   **from Time, drag `time_ticks_ms`**", "*   **from Logic, drag `if_do`**", "*   **from Smart IO, drag `pico_gpio_read`**"],
        "vars": ["**expiryTime**: Time when light should turn off"],
        "guide": """**A. Initialization Phase**
1.  **Vars**:
  *   Set `expiryTime` to 0.

**B. Main Loop Phase**
1.  **Inputs**:
  *   From **Loops**, drag `pico_forever`.
  *   If Button (GP14) OR PIR (GP15):
      *   Set `expiryTime` to `current_time` + 10000.
  *   **Snap** into loop.
2.  **Logic**:
  *   If `current_time` < `expiryTime`:
      *   Turn LED On.
  *   Else:
      *   Turn LED Off.
  *   **Snap** below inputs.""",
        "flow": "Instead of `sleep(10)`, we use a deadline approach. Any activity 'pushes back' the deadline. If the deadlines passes (current time > expiry), the light turns off.",
        "code": """import machine, time
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)
expiry = 0

while True:
    if btn.value() or pir.value():
        expiry = time.ticks_add(time.ticks_ms(), 10000) # +10s
        
    if time.ticks_diff(expiry, time.ticks_ms()) > 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)""",
        "mistakes": ["**PIR Delay**: PIR sensors have a hardware delay (potentiometer). Keep it minimum.", "**Sleep**: Don't use `time.sleep(10)` or you can't detect motion during the wait."],
        "next": ["**Fade Out**: PWM fade out when timer expires.", "**Warning**: Blink briefly before turning off."]
    })

    # 0607: Code RED (Dual Button)
    projects.append({
        "id": "0607",
        "title": "LED Patterns Alarm System",
        "objective": "Simulate a nuclear launch key system where two buttons must be pressed simultaneously to trigger a 'Code Red' alarm.",
        "concepts": ["Dual Authentication", "Boolean AND", "Safety Interlock", "Rapid Flashing"],
        "hardware": ["Pico", "Button A", "Button B", "Red LED", "Green LED"],
        "interface": "| **Btn A** | GP14 | Key 1 |\n| **Btn B** | GP15 | Key 2 |\n| **Red** | GP16 | Alarm |\n| **Green** | GP17 | Safe |",
        "blocks": ["*   **from Logic, drag `and_operation`**", "*   **from Smart IO, drag `pico_gpio_write`**", "*   **from Loops, drag `pico_forever`**"],
        "vars": ["None"],
        "guide": """**A. Initialization Phase**
1.  **Setup**: IOs.

**B. Main Loop Phase**
1.  **Security Check**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Btn A AND Btn B:
      *   Turn Green Off.
      *   Turn Red High. Wait 0.1s.
      *   Turn Red Low. Wait 0.1s.
  *   Else:
      *   Turn Green On.
      *   Turn Red Off.
  *   **Snap** into loop.""",
        "flow": "The `AND` operator acts as the safety gate. Both electrical signals must be High simultaneously. If one is released, the alarm stops instantly.",
        "code": """import machine, time
btnA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
red = machine.Pin(16, machine.Pin.OUT)
green = machine.Pin(17, machine.Pin.OUT)

while True:
    if btnA.value() and btnB.value():
        green.off()
        # Strobe effect
        red.toggle()
        time.sleep(0.05)
    else:
        green.on()
        red.off()
        time.sleep(0.05)""",
        "mistakes": ["**One Button**: Pressing one then the other works? Logic is 'Is A held AND Is B held?'. Yes.", "**Flicker**: Ensure the 'Else' block keeps Green solid."],
        "next": ["**Latch**: Once triggered, keep alarm on until a 3rd 'Reset' button is pressed.", "**Siren**: Add sound."]
    })

    # 0608: Whac-A-LED
    projects.append({
        "id": "0608",
        "title": "The LED Patterns Game",
        "objective": "Create a reaction game where a random LED lights up and the player must press the corresponding button within 1 second.",
        "concepts": ["Random Numbers", "Input Mapping", "Timeouts", "Reaction Time"],
        "hardware": ["Pico", "3 LEDs", "3 Buttons"],
        "interface": "| **LEDs** | GP16-18 |\n| **Btns** | GP13-15 |",
        "blocks": ["*   **from Math, drag `random_integer`**", "*   **from Time, drag `time_ticks_ms`**", "*   **from Logic, drag `break_loop`**"],
        "vars": ["**score**: Integer", "**target**: 0-2"],
        "guide": """**A. Init**: `score`=0.
**B. Game**:
1.  **New Round**:
  *   Loop forever:
  *   Pick `target` = Random(0,2).
  *   Light LED[`target`].
2.  **Wait Input**:
  *   Reset `timer`.
  *   Loop while `timer` < 1000ms:
      *   If Btn[`target`] pressed:
           *   `score` += 1.
           *   Blink All (Win). Break inner loop.
      *   If Wrong Btn pressed:
           *   Game Over.
  *   If loop finished (Timeout):
       *   Game Over.
  *   Turn LED Off. Wait random time.""",
        "flow": "The Code picks a target, starts a stopwatch, and watches inputs. Success resets the cycle. Failure (Wrong/Slow) ends the game.",
        "code": """import machine, time, random
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 19)]
btns = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_DOWN) for i in range(13, 16)]
score = 0

print("START!")
while True:
    target = random.randint(0, 2)
    leds[target].on()
    start = time.ticks_ms()
    hit = False
    
    while time.ticks_diff(time.ticks_ms(), start) < 1000:
        if btns[target].value():
            score += 1
            print(f"HIT! Score: {score}")
            hit = True
            break
        # Check wrong buttons
        for i in range(3):
            if i != target and btns[i].value():
                 print("WRONG!"); hit = False; start = 0 # Force fail
    
    leds[target].off()
    
    if not hit:
        print("GAME OVER")
        break
        
    time.sleep(random.uniform(0.5, 1.5))""",
        "mistakes": ["**Wiring**: Button 0 must match LED 0 physically.", "**Holding**: Player holding all buttons wins? Add check that buttons must be released first."],
        "next": ["**Speed Up**: Reduce the 1000ms timeout by 50ms each round.", "**Lives**: Allow 3 misses."]
    })

    # 0609: Binary Count
    projects.append({
        "id": "0609",
        "title": "Automated LED Patterns",
        "objective": "Display numbers 0-7 in binary format on 3 LEDs (000, 001, 010...).",
        "concepts": ["Binary Notation", "Bitwise Operations", "Modulo", "Counting"],
        "hardware": ["Pico", "3 LEDs"],
        "interface": "| **LEDs** | GP16-18 | LSB=16, MSB=18 |",
        "blocks": ["*   **from Math, drag `remainder`**", "*   **from Logic, drag `bit_shift`**"],
        "vars": ["**count**: 0-7"],
        "guide": """**A. Loop**:
  *   From **Loops**, count `i` from 0 to 7:
      *   Set LED 0 to `i % 2`.
      *   Set LED 1 to `(i // 2) % 2`.
      *   Set LED 2 to `(i // 4) % 2`.
      *   Wait 1s.
      *   **Snap** into loop.""",
        "flow": "We strip bits from the integer 'i'. Bit 0 is `i%2`. Bit 1 is `(i/2)%2`. This math converts decimal to binary signals.",
        "code": """import machine, time
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(16, 19)]

while True:
    for i in range(8):
        leds[0].value(i & 1)
        leds[1].value((i >> 1) & 1)
        leds[2].value((i >> 2) & 1)
        time.sleep(1)""",
        "mistakes": ["**LSB/MSB**: Which LED represents 1? Usually right-most.", "**Index**: Range(8) goes 0..7."],
        "next": ["**8-Bit**: Add 5 more LEDs to count to 255.", "**Gray Code**: Count using Gray code pattern."]
    })

    # 0610: PWM Fading
    projects.append({
        "id": "0610",
        "title": "Mastering LED Patterns",
        "objective": "Implement a smooth 'Breathing' effect by fading an LED from 0% to 100% brightness and back using PWM.",
        "concepts": ["Pulse Width Modulation", "Duty Cycle", "For Loops", "Resolution"],
        "hardware": ["Pico", "LED"],
        "interface": "| **LED** | GP16 | PWM Output |",
        "blocks": ["*   **from Actuators, drag `pwm_duty`**", "*   **from Loops, drag `for_in_range`**"],
        "vars": ["**duty**: 0-65535"],
        "guide": """**A. Init**: Setup PWM on GP16.
**B. Loop**:
1.  **Fade In**:
  *   Loop `duty` from 0 to 65000 step 1000:
      *   Set PWM Duty to `duty`.
      *   Wait 0.005s.
      *   **Snap** into `pico_forever`.
2.  **Fade Out**:
  *   Loop `duty` from 65000 to 0 step -1000:
      *   Set PWM Duty to `duty`.
      *   Wait 0.005s.
      *   **Snap** below.""",
        "flow": "By rapidly changing the duty cycle (ratio of On vs Off time), the eye perceives dimming. Small steps make it smooth.",
        "code": """import machine, time
pwm = machine.PWM(machine.Pin(16))
pwm.freq(1000)

while True:
    # Fade In
    for duty in range(0, 65535, 1000):
        pwm.duty_u16(duty)
        time.sleep(0.005)
    # Fade Out
    for duty in range(65535, 0, -1000):
        pwm.duty_u16(duty)
        time.sleep(0.005)""",
        "mistakes": ["**Gamma**: LED brightness isn't linear. 50% duty looks 70% bright. Correcting this requires math.", "**Flicker**: Frequency too low (<100Hz)."],
        "next": ["**Sinewave**: Fade using sine function for organic breathing.", "**RGB Fade**: Fade colors (Rainbow)."]
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
    generate_batch_61_part2()
