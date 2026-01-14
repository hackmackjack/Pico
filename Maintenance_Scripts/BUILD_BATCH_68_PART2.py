
import os

def generate_batch_68_part2():
    projects = []

    # 0676: Smart Switch (2-Player)
    projects.append({
        "id": "0676",
        "title": "Smart Reaction Game Switch",
        "objective": "2-Player Arbiter: Both players wait for the LED. First to press their button wins. The system prevents ties by locking out the loser.",
        "concepts": ["Race Conditions", "Lockout Logic", "Fairness", "State Arbitration"],
        "hardware": ["Pico", "2 Buttons", "LED"],
        "interface": "| **Btn A** | GP14 | Player 1 |\n| **Btn B** | GP15 | Player 2 |\n| **LED** | GP16 | Cue |",
        "blocks": ["*   **from Logic, drag `if_elseif`**", "*   **from Loops, drag `break_loop`**"],
        "vars": ["None"],
        "guide": """**A. Loop**:
1.  **Wait**:
  *   LED Off. Random Delay.
  *   LED On.
2.  **Race**:
  *   Loop Forever:
      *   If Btn A: Print "P1 Wins". Break.
      *   If Btn B: Print "P2 Wins". Break.
  *   **Snap** into `pico_forever`.""",
        "flow": "Microcontrollers check inputs sequentially. If A is checked before B, A has a slight advantage (microseconds), but practically irrelevant for humans.",
        "code": """import machine, time, random
p1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
p2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    led.off()
    time.sleep(random.uniform(2, 5))
    led.on()
    
    while True:
        if p1.value():
            print("PLAYER 1 WINS!")
            break
        if p2.value():
            print("PLAYER 2 WINS!")
            break
            
    time.sleep(2)
    while p1.value() or p2.value(): pass""",
        "mistakes": ["**Tie**: Real ties are rare impossible. One check always happens first.", "**False Start**: Code doesn't check for early presses."],
        "next": ["**LEDs**: Light an LED for the winner.", "**Scoreboard**: Track wins."]
    })

    # 0677: Alarm
    projects.append({
        "id": "0677",
        "title": "Reaction Game Alarm System",
        "objective": "Performance Alarm: Sounds a 'Fail' buzzer if reaction time is too slow (> 1 second). Sounds 'Pass' (Ding) if fast.",
        "concepts": ["Thresholding", "Performance Metrics", "Audible Feedback", "Conditional Alerts"],
        "hardware": ["Pico", "Button", "Buzzer", "LED"],
        "interface": "| **Button** | GP14 | Trigger |\n| **Buzzer** | GP16 | Audio |\n| **LED** | GP17 | Cue |",
        "blocks": ["*   **from Logic, drag `if_else`**", "*   **from Actuators, drag `pwm_tone`**"],
        "vars": ["**diff**: Int"],
        "guide": """**A. Loop**:
1.  **Stimulus**:
  *   Wait Random. LED On.
  *   Start Timer. Wait Button.
  *   `diff` = Stop Timer.
2.  **Judge**:
  *   If `diff` > 1000:
      *   Buzzer 200Hz 1s (Fail).
  *   Else:
      *   Buzzer 1000Hz 0.1s (Pass).
  *   **Snap** into `pico_forever`.""",
        "flow": "Immediate feedback is key for training muscle memory.",
        "code": """import machine, time, random
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.PWM(machine.Pin(16))
led = machine.Pin(17, machine.Pin.OUT)

while True:
    led.off()
    time.sleep(random.uniform(2, 4))
    
    led.on()
    start = time.ticks_ms()
    while not btn.value(): pass
    diff = time.ticks_diff(time.ticks_ms(), start)
    led.off()
    
    if diff > 1000:
        print("FAIL")
        buz.freq(200); buz.duty_u16(32768); time.sleep(1)
    else:
        print("PASS")
        buz.freq(1000); buz.duty_u16(32768); time.sleep(0.1)
    buz.duty_u16(0)
    while btn.value(): time.sleep(0.01)
    time.sleep(1)""",
        "mistakes": ["**Unfair**: If random delay is too short (<1s), user isn't ready.", "**Physics**: Latency in the LED turning on (negligible)."],
        "next": ["**Level Up**: Decrease threshold to 800ms, then 600ms.", "**Lives**: 3 strikes and game over."]
    })

    # 0678: Game (Quick Draw)
    projects.append({
        "id": "0678",
        "title": "The Reaction Game Game",
        "objective": "Cowboy Quick Draw: Holster the gun (Tilt Sensor Down). When Buzzer sounds, Draw (Tilt Up) and Fire (Button) as fast as possible.",
        "concepts": ["Complex Sequences", "Motion Sensing", "Game Mechanics", "State Machines"],
        "hardware": ["Pico", "Tilt Sensor", "Button", "Buzzer"],
        "interface": "| **Tilt** | GP15 | Holster |\n| **Button** | GP14 | Trigger |\n| **Buz** | GP16 | Signal |",
        "blocks": ["*   **from Layers, drag `repeat_until`**", "*   **from Time, drag `time_ticks_ms`**"],
        "vars": ["**drawTime**: Int", "**fireTime**: Int"],
        "guide": """**A. Loop**:
1.  **Holster**:
  *   Wait until Tilt is LOW (Gun down).
  *   Wait Random Delay.
  *   Buzzer (Go!).
2.  **Action**:
  *   `t0` = `time`.
  *   Wait until Tilt HIGH (Draw).
  *   `t1` = `time`.
  *   Wait until Button HIGH (Fire).
  *   `t2` = `time`.
3.  **Result**:
  *   Print "Draw: " + (`t1`-`t0`).
  *   Print "Fire: " + (`t2`-`t1`).
  *   **Snap** into `pico_forever`.""",
        "flow": "Measures two distinct motor skills: Gross motor (arm lift) and Fine motor (finger press).",
        "code": """import machine, time, random
tilt = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buz = machine.PWM(machine.Pin(16))

while True:
    print("HOLSTER GUN!")
    while tilt.value() == 1: time.sleep(0.1) # Wait for Down (Assume 0=Down)
    # Note: Tilt sensors vary. Adjust 0/1 logic as needed.
    
    time.sleep(random.uniform(2, 5))
    buz.freq(2000); buz.duty_u16(32768); time.sleep(0.1); buz.duty_u16(0)
    
    start = time.ticks_ms()
    while tilt.value() == 0: pass # Wait Draw
    draw_time = time.ticks_ms()
    
    while not btn.value(): pass # Wait Fire
    fire_time = time.ticks_ms()
    
    print(f"Draw: {time.ticks_diff(draw_time, start)}ms")
    print(f"Aim: {time.ticks_diff(fire_time, draw_time)}ms")
    print(f"Total: {time.ticks_diff(fire_time, start)}ms")
    time.sleep(5)""",
        "mistakes": ["**Tilt Noise**: Ball bearings inside tilt sensors rattle. Needs debounce.", "**Cheating**: Holding the button *before* drawing."],
        "next": ["**Accuracy**: Point beam at LDR target.", "**Duel**: Two players."]
    })

    # 0679: Automated
    projects.append({
        "id": "0679",
        "title": "Automated Reaction Game",
        "objective": "Data Analytics: Run 5 reaction tests. Store results in a list. Calculate and print the Average Reaction Time.",
        "concepts": ["Data Aggregation", "Lists/Arrays", "For Loops", "Averaging"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Input |\n| **LED** | GP16 | Cue |",
        "blocks": ["*   **from Variables, drag `list_create`**", "*   **from Math, drag `list_average`**"],
        "vars": ["**times**: List", "**total**: Int"],
        "guide": """**A. Init**: `times`=[].
**B. Loop**:
1.  **Test 5x**:
  *   Loop 5 times:
      *   Run Reaction Test.
      *   Append result to `times`.
2.  **Calc**:
  *   `total` = 0.
  *   Loop `t` in `times`: `total` += `t`.
  *   `avg` = `total` / 5.
  *   Print `avg`.
  *   **Snap** into `pico_forever`.""",
        "flow": "Single data points are noisy. Averages reveal the truth.",
        "code": """import machine, time, random
led = machine.Pin(16, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    times = []
    print("STARTING SET OF 5")
    
    for i in range(5):
        time.sleep(random.uniform(1, 3))
        led.on()
        start = time.ticks_ms()
        while not btn.value(): pass
        res = time.ticks_diff(time.ticks_ms(), start)
        led.off()
        times.append(res)
        print(f"#{i+1}: {res}ms")
        while btn.value(): time.sleep(0.01)
        
    total = sum(times)
    print(f"AVERAGE: {int(total/5)}ms")
    times = []""",
        "mistakes": ["**Empty List**: Summing an empty list crashes.", "**Outliers**: One distraction (2000ms) ruins the average. Use Median?"],
        "next": ["**Median**: Sort list and pick middle value.", "**Best**: Print `min(times)`."]
    })

    # 0680: Mastering
    projects.append({
        "id": "0680",
        "title": "Mastering Reaction Game",
        "objective": "Psychophysics Experiment: Does the 'Wait Time' (Foreperiod) affect reaction time? Test different delays (1s vs 5s) and record results.",
        "concepts": ["Experimental Design", "Foreperiod Effect", "Data Correlation", "Hypothesis Testing"],
        "hardware": ["Pico", "Button", "LED"],
        "interface": "| **Button** | GP14 | Input |\n| **LED** | GP16 | Cue |",
        "blocks": ["*   **from Variables, drag `create_map`**", "*   **from Text, drag `print`**"],
        "vars": ["**delay**: Int"],
        "guide": """**A. Loop**:
1.  **Short Warning**:
  *   Delay 1000ms. Test. Print "Short: " + Time.
2.  **Long Warning**:
  *   Delay 5000ms. Test. Print "Long: " + Time.
  *   **Snap** into `pico_forever`.""",
        "flow": "Generally, there is a 'sweet spot' (2-3s). Too short = not ready. Too long = loss of focus.",
        "code": """import machine, time, random
led = machine.Pin(16, machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def run_test(delay_ms):
    time.sleep(delay_ms / 1000)
    led.on()
    start = time.ticks_ms()
    while not btn.value(): pass
    res = time.ticks_diff(time.ticks_ms(), start)
    led.off()
    while btn.value(): time.sleep(0.01)
    return res

while True:
    # Short
    r1 = run_test(1000)
    print(f"Delay 1s -> {r1}ms")
    
    # Long
    r2 = run_test(5000)
    print(f"Delay 5s -> {r2}ms")
    print("---")
    time.sleep(2)""",
        "mistakes": ["**Predictability**: Alternating 1s/5s becomes predictable. Randomize order.", "**Fatigue**: Users get tired/bored."],
        "next": ["**CSV**: Output as `delay,reaction` for Excel plotting.", "**Auditory**: Test sound delay vs visual delay."]
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
    generate_batch_68_part2()
