import os

def regenerate_batch_55_60():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # Batch 55: Smart Fan 3
    b55_head = "\n---\n# Batch 55: Smart Fan 3\n"
    p0541 = "## 1. Project 0541: Intro Smart Fan\n### 8. Step-by-Step\n**B. Loop**\n1. **Soft Start**: Loop `i` 0->65000. PWM `i`. Wait 0.01s (Ramp)."
    p0542 = "## 2. Project 0542: Blinking Fan\n### 8. Step-by-Step\n**B. Loop**\n1. **Gusts**: Random PWM spikes. `val = random(30k, 65k)`. Wait random."
    p0543 = "## 3. Project 0543: Manual Control\n### 8. Step-by-Step\n**B. Loop**\n1. **Knob**: `pwm = adc_read()`. Set Fan."
    p0544 = "## 4. Project 0544: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **Wave**: Sine wave speed. scale `sin(time)` to PWM."
    p0545 = "## 5. Project 0545: Interactive\n### 8. Step-by-Step\n**B. Loop**\n1. **Breath**: If Mic > Thresh: Impulse Spin. Then Coast."
    p0546 = "## 6. Project 0546: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Mode**: Sw1=Silent (Max 30%). Sw2=Turbo (Max 100%)."
    p0547 = "## 7. Project 0547: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Stall**: If Speed=High AND Current=Low (if sensing) OR Time check."
    p0548 = "## 8. Project 0548: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Levitate**: Adjust Fan to keep PingPong ball in zone. (PID Game)."
    p0549 = "## 9. Project 0549: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Humidity**: If `dht.humidity > 60`: Fan ON."
    p0550 = "## 10. Project 0550: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **Tach**: Count pulses from Hall sensor. `rpm = pulses * 60`."

    # Batch 56: Robotic Arm 3 (0551-0560)
    b56_head = "\n---\n# Batch 56: Robotic Arm Basics 3\n"
    p0551 = "## 1. Project 0551: Intro Arm\n### 8. Step-by-Step\n**B. Loop**\n1. **Sweep**: Servo 0->180. Wait. 180->0."
    p0552 = "## 2. Project 0552: Blinking Arm\n### 8. Step-by-Step\n**B. Loop**\n1. **Wave**: Rapid center-left-center-right waggle."
    p0553 = "## 3. Project 0553: Manual Arm\n### 8. Step-by-Step\n**B. Loop**\n1. **Direct**: `angle = map(pot, 0-65k, 0-180)`. Write Servo."
    p0554 = "## 4. Project 0554: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **PickPlace**: Move(0). Down(90). Grab(Close). Up(0). Move(180). Drop(Open)."
    p0555 = "## 5. Project 0555: Interactive Arm\n### 8. Step-by-Step\n**B. Loop**\n1. **Teach**: Record points when Btn pressed. Replay list."
    p0556 = "## 6. Project 0556: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Safety**: Stop if `dist_sensor < 10cm` (Emergency Stop)."
    p0557 = "## 7. Project 0557: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Torque**: If current spike (simulated): Detach."
    p0558 = "## 8. Project 0558: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Catapult**: Swing fast 0->90 to launch object."
    p0559 = "## 9. Project 0559: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Sorter**: If Color=Red: Bin A (Angle 45). If Color=Blue: Bin B (Angle 135)."
    p0560 = "## 10. Project 0560: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **IK**: 2-DOF Inverse Kinematics calculation `x,y -> theta1, theta2`."

    # Batch 57: OLED Shapes 3 (0561-0570)
    b57_head = "\n---\n# Batch 57: OLED Shapes 3\n"
    p0561 = "## 1. Project 0561: Intro Shapes\n### 8. Step-by-Step\n**B. Loop**\n1. **Boundaries**: Draw Rect at bounds. Bounce pixel inside."
    p0562 = "## 2. Project 0562: Blinking Shapes\n### 8. Step-by-Step\n**B. Loop**\n1. **Screensaver**: Random `pixel(x,y,1)` (Snow)."
    p0563 = "## 3. Project 0563: Manual Shapes\n### 8. Step-by-Step\n**B. Loop**\n1. **Size**: Knob controls Radius of circle."
    p0564 = "## 4. Project 0564: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **Tunnel**: Concentric rectangles expanding."
    p0565 = "## 5. Project 0565: Interactive\n### 8. Step-by-Step\n**B. Loop**\n1. **Traffic**: Draw Cars. If Btn: Stop Light Red."
    p0566 = "## 6. Project 0566: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Tilt**: Accel X maps to Ball X. Physics gravity."
    p0567 = "## 7. Project 0567: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Visual**: Flashing 'WARNING' Octagon."
    p0568 = "## 8. Project 0568: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Pong**: Paddle Y controlled by pot. Ball bounce."
    p0569 = "## 9. Project 0569: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Graph**: Plot rolling history of Temp sensor as Line Chart."
    p0570 = "## 10. Project 0570: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **3D**: Wireframe Cube projection (Matrix math)."

    # Batch 58: Stopwatch 3 (0571-0580)
    b58_head = "\n---\n# Batch 58: Stopwatch 3\n"
    p0571 = "## 1. Project 0571: Intro Steps\n### 8. Step-by-Step\n**B. Loop**\n1. **Uptime**: Print `time.ticks_ms() / 1000`."
    p0572 = "## 2. Project 0572: Blinking Step\n### 8. Step-by-Step\n**B. Loop**\n1. **Non-Block**: `if now - last > 1000`: Blink. (No sleep)."
    p0573 = "## 3. Project 0573: Manual Step\n### 8. Step-by-Step\n**B. Loop**\n1. **Lap**: Btn press prints `current - start`."
    p0574 = "## 4. Project 0574: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **Relay**: 4 stages of 5s. Beep sequence."
    p0575 = "## 5. Project 0575: Interactive\n### 8. Step-by-Step\n**B. Loop**\n1. **Reflex**: Random wait. Flash. Measure response time."
    p0576 = "## 6. Project 0576: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Timeout**: If no input for 10s: Enter Sleep."
    p0577 = "## 7. Project 0577: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Sched**: Alarm at specific `ticks` count."
    p0578 = "## 8. Project 0578: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Stop at 10**: User tries to press exactly at 10.00s."
    p0579 = "## 9. Project 0579: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Logger**: Log timestamp of events to file/list."
    p0580 = "## 10. Project 0580: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **Scheduler**: Cooperative multitasking (Task A, Task B) via ticks."

    # Batch 59: Kitchen Timer 3 (0581-0590)
    b59_head = "\n---\n# Batch 59: Kitchen Timer 3\n"
    p0581 = "## 1. Project 0581: Intro Timer\n### 8. Step-by-Step\n**B. Loop**\n1. **Format**: Convert seconds to MM:SS string."
    p0582 = "## 2. Project 0582: Blinking Timer\n### 8. Step-by-Step\n**B. Loop**\n1. **Urgency**: If < 10s: Blink Red Fast."
    p0583 = "## 3. Project 0583: Manual Timer\n### 8. Step-by-Step\n**B. Loop**\n1. **Dial**: Encoder/Pot sets duration."
    p0584 = "## 4. Project 0584: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **Pomodoro**: 25m Work. Alarm. 5m Rest. Alarm."
    p0585 = "## 5. Project 0585: Interactive\n### 8. Step-by-Step\n**B. Loop**\n1. **Egg**: Presets (Soft, Hard) via Buttons."
    p0586 = "## 6. Project 0586: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Cancel**: Long press to reset."
    p0587 = "## 7. Project 0587: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Melody**: Play specific tune on finish."
    p0588 = "## 8. Project 0588: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Bomb**: Defuse code before timer 0."
    p0589 = "## 9. Project 0589: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Tea**: Steep phases (Dip servo?)."
    p0590 = "## 10. Project 0590: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **RTC**: Use Real Time Clock for absolute alarm (7:00 AM)."

    # Batch 60: Metronome 3 (0591-0600)
    b60_head = "\n---\n# Batch 60: Metronome 3\n"
    p0591 = "## 1. Project 0591: Intro Beat\n### 8. Step-by-Step\n**B. Loop**\n1. **BPM**: `interval = 60/BPM`. Tick."
    p0592 = "## 2. Project 0592: Blinking Beat\n### 8. Step-by-Step\n**B. Loop**\n1. **Visual**: Flash LED on quarter notes."
    p0593 = "## 3. Project 0593: Manual Beat\n### 8. Step-by-Step\n**B. Loop**\n1. **Tap Tempo**: Avg time between 3 taps -> BPM."
    p0594 = "## 4. Project 0594: Sequences\n### 8. Step-by-Step\n**B. Loop**\n1. **Clave**: 3-2 Son beat pattern playback."
    p0595 = "## 5. Project 0595: Interactive\n### 8. Step-by-Step\n**B. Loop**\n1. **Accent**: First beat of measure High pitch, others Low."
    p0596 = "## 6. Project 0596: Smart Switch\n### 8. Step-by-Step\n**B. Loop**\n1. **Subdivide**: Toggle triplets/eighths."
    p0597 = "## 7. Project 0597: Alarm\n### 8. Step-by-Step\n**B. Loop**\n1. **Swing**: Add syncopated delay to even notes."
    p0598 = "## 8. Project 0598: Game\n### 8. Step-by-Step\n**B. Loop**\n1. **Rhythm Keeper**: User taps along. Score accuracy."
    p0599 = "## 9. Project 0599: Automated\n### 8. Step-by-Step\n**B. Loop**\n1. **Polyrhythm**: 3 against 4 loop."
    p0600 = "## 10. Project 0600: Mastering\n### 8. Step-by-Step\n**B. Loop**\n1. **MIDI**: Send serial MIDI clock byte (`0xF8`)."

    with open(target_file, 'a', encoding='utf-8') as f:
        # Append all
        f.write(b55_head + p0541 + p0542 + p0543 + p0544 + p0545 + p0546 + p0547 + p0548 + p0549 + p0550)
        f.write(b56_head + p0551 + p0552 + p0553 + p0554 + p0555 + p0556 + p0557 + p0558 + p0559 + p0560)
        f.write(b57_head + p0561 + p0562 + p0563 + p0564 + p0565 + p0566 + p0567 + p0568 + p0569 + p0570)
        f.write(b58_head + p0571 + p0572 + p0573 + p0574 + p0575 + p0576 + p0577 + p0578 + p0579 + p0580)
        f.write(b59_head + p0581 + p0582 + p0583 + p0584 + p0585 + p0586 + p0587 + p0588 + p0589 + p0590)
        f.write(b60_head + p0591 + p0592 + p0593 + p0594 + p0595 + p0596 + p0597 + p0598 + p0599 + p0600)

if __name__ == "__main__":
    regenerate_batch_55_60()
