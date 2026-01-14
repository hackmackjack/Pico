import os

def regenerate_batch_56_60_real():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    def get_full_project(id, name, obj, concepts, hardware, wiring, blocks, variables, guide, flow, code, mistakes, next_step):
        return f"""
## {int(id[-1]) if id[-1]!='0' else 10}. Project {id}: {name}

### 2. Learning Objective
{obj}

### 3. Concepts Introduced
{concepts}

### 4. Hardware Required
{hardware}

### 5. Wiring / Interfaces
{wiring}

### 6. Blocks Used
{blocks}

### 7. Variables
{variables}

### 8. Step-by-Step Guide
{guide}

### 9. Execution Flow
{flow}

### 10. Generated Code
```python
{code}
```

### 11. Common Mistakes
{mistakes}

### 12. Try This Next
{next_step}

---
"""

    # --- BATCH 56: Robotic Arm (0551-0560) ---
    b = "#  Batch 56: Robotic Arm Basics 3\n\n"
    
    # 0551: Intro - Sweep
    b += get_full_project("0551", "Intro to Robotic Arm", "Sweep servo 0-180.", "* PWM\n* Duty Cycle", "* Pico\n* Servo", "| Servo | GP0 | - |", "* Move", "* Angle", "**B. Loop**\n1. 0->180 Wait.\n2. 180->0 Wait.", "1. Sweeps.", "import machine, time\ns=machine.PWM(machine.Pin(0))\ns.freq(50)\nwhile True:\n s.duty_u16(1000)\n time.sleep(1)\n s.duty_u16(9000)\n time.sleep(1)", "* Power", "* 2 Servos")
    
    # 0552: Blinking Arm -> Wave
    b += get_full_project("0552", "Robotic Wave", "Rapid small movements (Waving).", "* Oscillation", "* Pico\n* Servo", "| Servo | GP0 | - |", "* Move", "* T", "**B. Loop**\n1. 90->120.\n2. 120->90.", "1. Waves.", "while True: wave()", "* Jerky", "* Speed var")

    # 0553: Manual - Knob
    b += get_full_project("0553", "Manual Arm Control", "Potentiometer controls Angle.", "* Mapping", "* Pico\n* Servo\n* Pot", "| Pot | GP26 | - |", "* Map", "* Val", "**B. Loop**\n1. Read Pot.\n2. Map to 0-180.\n3. Write.", "1. Mimics knob.", "val = adc.read_u16()", "* Jitter", "* Smooth")

    # 0554: Sequences - Pick and Place
    b += get_full_project("0554", "Pick and Place", "Move->Down->Grab->Up->Move->Drop.", "* State Machine", "* Pico\n* 2 Servos", "| Base | GP0 |\n| Grip | GP1 |", "* Wait", "* Step", "**B. Loop**\n1. Base 0.\n2. Grip Open.\n3. Base 90.\n4. Grip Close.", "1. Automates task.", "sequence()", "* Timing", "* Sensor")

    # 0555: Interactive - Teach Mode
    b += get_full_project("0555", "Teach and Play", "Record button presses as waypoints.", "* Arrays", "* Pico\n* Servo\n* Btn", "| Btn | GP14 | - |", "* Append", "* List", "**B. Loop**\n1. If Btn: List.append(pot_val).\n2. If Play: Loop List.", "1. Memorizes.", "points = []", "* RAM limit", "* Save Flash")

    # 0556: Smart Switch - Safety
    b += get_full_project("0556", "Safety Stop", "Stop if Distance Sensor < 10cm.", "* Interlock", "* Pico\n* Ultrasonic", "| Trig | GP2 |", "* If", "* Dist", "**B. Loop**\n1. Read Dist.\n2. If <10: Stop.\n3. Else: Run.", "1. Prevents hit.", "if d < 10: stop()", "* Noise", "* IR")

    # 0557: Alarm - Torque/Current (Simulated)
    b += get_full_project("0557", "Stall Alarm", "Alarm if position not reached (Simulated).", "* Feedback", "* Pico", "| Led | GP25 |", "* Compare", "* Err", "**B. Loop**\n1. Move.\n2. Check feedback (Simulated).\n3. Alarm if fail.", "1. Detects jam.", "check_stall()", "* No feedback wire", "* Real current sense")

    # 0558: Game - Catapult
    b += get_full_project("0558", "Catapult Game", "Launch ball at target speed.", "* Physics", "* Pico\n* Servo", "| Arm | GP0 |", "* Speed", "* V", "**B. Loop**\n1. Slow back.\n2. Fast forward.", "1. Throws.", "launch()", "* Loose parts", "* Safety")

    # 0559: Automated - Sorter
    b += get_full_project("0559", "Color Sorter", "Sort Red to Left, Blue to Right.", "* Logic", "* Pico\n* Color Sensor", "| SDA | GP8 |", "* If", "* Col", "**B. Loop**\n1. Read Color.\n2. If R: Servo 45.\n3. If B: Servo 135.", "1. Sorts.", "sort()", "* Lighting", "* Calib")

    # 0560: Mastering - IK
    b += get_full_project("0560", "Inverse Kinematics", "Calculate angles to reach (X,Y).", "* Trig", "* Pico", "| S1 | GP0 |", "* ACos", "* Theta", "**B. Loop**\n1. Input X,Y.\n2. Theta1 = ...\n3. Move.", "1. Cartesian control.", "ik_solve()", "* Range error", "* 3D")

    # --- BATCH 57: OLED Shapes (0561-0570) ---
    b += "#  Batch 57: OLED Shapes 3\n\n"
    b += get_full_project("0561", "Intro Shapes", "Draw Rect at bounds.", "* Coords", "* Pico\n* OLED", "| SDA | GP8 |", "* Rect", "* -", "**B. Loop**\n1. Draw Frame.", "1. Shows border.", "oled.rect(0,0,128,64,1)", "* 128 vs 127", "* Fill")
    b += get_full_project("0562", "Blinking Shapes", "Screen Flash.", "* Invert", "* Pico", "| - | - |", "* Inv", "* -", "**B. Loop**\n1. Invert(1). Wait. Invert(0).", "1. Flashes.", "oled.invert(1)", "* Seizure", "* Contrast")
    b += get_full_project("0563", "Manual Shapes", "Pot controls Radius.", "* Dyn scale", "* Pico\n* Pot", "| Pot | GP26 |", "* Circ", "* R", "**B. Loop**\n1. R = Pot.\n2. Circle(64,32,R).", "1. Sizes.", "oled.circle(x,y,r,1)", "* Center", "* Oval")
    b += get_full_project("0564", "Shapes Sequences", "Tunnel Animation.", "* Loop", "* Pico", "| - | - |", "* For", "* I", "**B. Loop**\n1. Loop R 1->64.\n2. Draw Rect.", "1. Tunnel effect.", "for r in range(64): rect()", "* Clear", "* Speed")
    b += get_full_project("0565", "Interactive Shapes", "pong paddle.", "* Y-axis", "* Pico\n* Btn", "| Btn | 14 |", "* Line", "* Y", "**B. Loop**\n1. If Btn: Y++.\n2. Rect(10, Y, 2, 10).", "1. Moves paddle.", "paddle()", "* Bounds", "* Ball")
    b += get_full_project("0566", "Smart Switch", "Tilt Ball (Sim).", "* Physics", "* Pico", "| - | - |", "* Accel", "* X", "**B. Loop**\n1. X += Tilt.\n2. Pixel(X, 32).", "1. Rolls.", "roll()", "* Friction", "* Gravity")
    b += get_full_project("0567", "Visual Alarm", "Flashing Warning Octagon.", "* Poly", "* Pico", "| - | - |", "* Poly", "* -", "**B. Loop**\n1. Draw Octagon. Show. Wait.\n2. Clear. Show.", "1. Alerts.", "octagon()", "* Slow", "* Text")
    b += get_full_project("0568", "Snake Game", "Mini Snake.", "* Grid", "* Pico\n* Btns", "| L/R | - |", "* List", "* Segs", "**B. Loop**\n1. Update Head.\n2. Check Wall.\n3. Draw.", "1. Games.", "snake()", "* Tail", "* Apple")
    b += get_full_project("0569", "Analog Gauge", "Draw Dial Needle.", "* Vector", "* Pico\n* Pot", "| P | 26 |", "* Line", "* Ang", "**B. Loop**\n1. Ang = Pot.\n2. X = r*cos(Ang).\n3. Line(64,64, X,Y).", "1. V-Meter.", "gauge()", "* Rad to Deg", "* Len")
    b += get_full_project("0570", "3D Cube", "Wireframe Cube.", "* Matrices", "* Pico", "| - | - |", "* Line", "* Pts", "**B. Loop**\n1. Rotate Points.\n2. Project.\n3. Connect.", "1. 3D.", "cube()", "* Float speed", "* Z-sort")

    # --- BATCH 58: Stopwatch (0571-0580) ---
    b += "#  Batch 58: Stopwatch 3\n\n"
    b += get_full_project("0571", "Intro Stopwatch", "Print ticks_ms.", "* Ticks", "* Pico", "| - | - |", "* Print", "* T", "**B. Loop**\n1. Print time.", "1. Logs.", "print(ticks_ms())", "* Wrap", "* Float")
    b += get_full_project("0572", "Non-Blocking", "Blink without sleep.", "* Diff", "* Pico", "| L | 25 |", "* If", "* Last", "**B. Loop**\n1. If now-last > 500: Toggle.", "1. Blinks.", "if t-l > 500:", "* Reset", "* Overflow")
    b += get_full_project("0573", "Lap Timer", "Lap button.", "* Store", "* Pico", "| B | 14 |", "* Print", "* Lap", "**B. Loop**\n1. If Btn: Print(now-start).", "1. Splits.", "print(lap)", "* Debounce", "* Array")
    b += get_full_project("0574", "Relay Race", "2 Player Timer.", "* State", "* Pico", "| B1,B2 | - |", "* Var", "* P", "**B. Loop**\n1. P1 Start. Button.\n2. P2 Start. Button.", "1. Race.", "relay()", "* False start", "* Sum")
    b += get_full_project("0575", "Reflex Test", "Reaction Time.", "* Rand", "* Pico", "| L,B | - |", "* Sub", "* Res", "**B. Loop**\n1. Wait Rand. LED ON.\n2. Wait Btn. Calc Diff.", "1. Scores.", "reflex()", "* Cheat", "* Avg")
    b += get_full_project("0576", "Timeout", "Inactivity Watchdog.", "* Idle", "* Pico", "| - | - |", "* Reset", "* I", "**B. Loop**\n1. If Btn: I=0.\n2. Else: I++.\n3. If I>10: Reset.", "1. Saves power.", "check_idle()", "* Sleep", "* Wake")
    b += get_full_project("0577", "Time Limit", "Safety Cutoff.", "* Limit", "* Pico", "| - | - |", "* If", "* Dur", "**B. Loop**\n1. While Btn: T++.\n2. If T > 5s: Cut.", "1. Protects.", "cutoff()", "* Heat", "* Lock")
    b += get_full_project("0578", "Precision Game", "Stop at 10.00.", "* Target", "* Pico", "| B | - |", "* Abs", "* Err", "**B. Loop**\n1. Show Time.\n2. Btn: Stop. Show Delta.", "1. Skill.", "game()", "* Lag", "* Screen")
    b += get_full_project("0579", "Datalogger", "Record Temp/Time.", "* Log", "* Pico", "| T | 26 |", "* File", "* D", "**B. Loop**\n1. Log (Time, Temp).", "1. Graphs.", "log()", "* Storage", "* Format")
    b += get_full_project("0580", "Multitasking", "3 LEDs independent.", "* Sched", "* Pico", "| 3L | - |", "* List", "* Task", "**B. Loop**\n1. Check L1 time.\n2. Check L2 time.", "1. Parallel.", "sched()", "* Starve", "* IRQ")

    # --- BATCH 59: Kitchen Timer (0581-0590) ---
    b += "#  Batch 59: Kitchen Timer 3\n\n"
    b += get_full_project("0581", "Intro Timer", "Console Print MM:SS.", "* Format", "* Pico", "| - | - |", "* Div", "* S", "**B. Loop**\n1. Sleep 1.\n2. Print.", "1. Clocks.", "print(m,s)", "* %, //", "* Drift")
    b += get_full_project("0582", "Urgency Blink", "Red flash < 10s.", "* Thresh", "* Pico", "| L | - |", "* If", "* U", "**B. Loop**\n1. If T < 10: Blink Fast.", "1. Warns.", "check_urgency()", "* State", "* Sound")
    b += get_full_project("0583", "Rotary Set", "Pot sets time.", "* Input", "* Pico", "| P | 26 |", "* Map", "* T", "**B. Loop**\n1. T = Pot * 60.", "1. UI.", "set_t()", "* Jump", "* Lock")
    b += get_full_project("0584", "Pomodoro", "25 Work / 5 Break.", "* Cycle", "* Pico", "| - | - |", "* Loop", "* P", "**B. Loop**\n1. Timer(25). Alarm.\n2. Timer(5).", "1. Focus.", "pomodoro()", "* Pause", "* Skip")
    b += get_full_project("0585", "Egg Timer", "Presets.", "* Menu", "* Pico", "| B | - |", "* Case", "* M", "**B. Loop**\n1. If Btn A: T=3. If B: T=5.", "1. Easy.", "presets()", "* Overwrite", "* Cancel")
    b += get_full_project("0586", "Child Lock", "Lock buttons.", "* Inhibit", "* Pico", "| Sw | - |", "* And", "* L", "**B. Loop**\n1. If Lock: Ignore Btn.", "1. Safe.", "if not lock:", "* Stuck", "* LED")
    b += get_full_project("0587", "Escalation Alarm", "Louder if ignored.", "* Vol", "* Pico", "| Bz | - |", "* Inc", "* V", "**B. Loop**\n1. Alarm.\n2. If not Ack: Vol++.", "1. Nags.", "nag()", "* Ear", "* Reset")
    b += get_full_project("0588", "Bomb Defuse", "Cut wire.", "* Sense", "* Pico", "| W | - |", "* Pin", "* C", "**B. Loop**\n1. Down count.\n2. If Wire Open: Stop/Boom.", "1. Tens.", "defuse()", "* Short", "* Bounce")
    b += get_full_project("0589", "Smart Light", "PIR Motion Timer.", "* Retrig", "* Pico", "| PIR | 16 |", "* Or", "* M", "**B. Loop**\n1. If PIR: T=300.\n2. While T>0: Light On.", "1. Auto.", "pir_light()", "* Sens", "* Time")
    b += get_full_project("0590", "RTC Timer", "Alarm at 5PM.", "* Abs", "* Pico", "| - | - |", "* RTC", "* H", "**B. Loop**\n1. Read RTC.\n2. If 17:00: Alarm.", "1. Daily.", "rtc.datetime()", "* Set", "* Batt")

    # --- BATCH 60: Metronome (0591-0600) ---
    b += "#  Batch 60: Metronome 3\n\n"
    b += get_full_project("0591", "Intro Beat", "Screen Flash.", "* Sync", "* Pico", "| - | - |", "* Slp", "* -", "**B. Loop**\n1. Flash. Sleep(60/bpm).", "1. Pulse.", "flash()", "* Lag", "* Var")
    b += get_full_project("0592", "Leader", "Count-in 4.", "* Seq", "* Pico", "| - | - |", "* Rep", "* -", "**B. Loop**\n1. 4 Clicks.\n2. Start.", "1. Ready.", "count_in()", "* Off", "* On")
    b += get_full_project("0593", "Tap Tempo", "Avg taps.", "* Avg", "* Pico", "| B | - |", "* Diff", "* L", "**B. Loop**\n1. Btn times.\n2. BPM = 60/Avg.", "1. Sets.", "calc_bpm()", "* Miss", "* Reset")
    b += get_full_project("0594", "Clave", "Bo Diddley.", "* Pat", "* Pico", "| - | - |", "* Arr", "* P", "**B. Loop**\n1. Play Pattern [1,0,0,1,0].", "1. Fun.", "clave()", "* Array", "* Loop")
    b += get_full_project("0595", "Accents", "Hi-Lo-Lo-Lo.", "* Tone", "* Pico", "| - | - |", "* Mod", "* i", "**B. Loop**\n1. If i%4==0: Hi. Else: Lo.", "1. Feel.", "accent()", "* 3/4", "* 4/4")
    b += get_full_project("0596", "Silent Mode", "Haptic.", "* Motor", "* Pico", "| Vib | - |", "* Sw", "* M", "**B. Loop**\n1. If Silent: Vib. Else: Beep.", "1. Quiet.", "vib()", "* Current", "* Felt")
    b += get_full_project("0597", "Volume Warn", "Mic monitor.", "* ADC", "* Pico", "| Mic | 26 |", "* Avg", "* V", "**B. Loop**\n1. Read Mic.\n2. If > Max: Flash.", "1. Protects.", "level()", "* Clip", "* Ref")
    b += get_full_project("0598", "Polyrhythm", "3 vs 4.", "* Euclid", "* Pico", "| 2Bz | - |", "* LCM", "* T", "**B. Loop**\n1. Play 3.\n2. Play 4.", "1. Hard.", "poly()", "* Sync", "* Math")
    b += get_full_project("0599", "Speed Trainer", "Accel.", "* Inc", "* Pico", "| - | - |", "* +=", "* B", "**B. Loop**\n1. Play 4 bars.\n2. BPM += 5.", "1. Push.", "train()", "* Fast", "* Limit")
    b += get_full_project("0600", "MIDI Out", "Serial 0xF8.", "* UART", "* Pico", "| Tx | 0 |", "* Wr", "* -", "**B. Loop**\n1. UART.write(0xF8).", "1. Syncs.", "midi()", "* Baud", "* Cable")

    # Write to File
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(target_file, 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # We replace from Batch 56 onwards
    split = existing.find("#  Batch 56: Robotic Arm Basics 3")
    if split == -1: 
        # Fallback
        split = existing.find("# Batch 56")

    if split != -1:
        new_content = existing[:split] + b
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    regenerate_batch_56_60_real()
