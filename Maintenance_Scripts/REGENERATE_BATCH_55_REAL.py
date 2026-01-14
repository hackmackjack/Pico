import os

def regen_batch_55():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    def get_template(id, name, obj, concepts, hardware, wiring, blocks, variables, guide, flow, code, mistakes, next_step):
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

    b = "#  Batch 55: Smart Fan 3\n\n"
    b += get_template("0541", "Soft Start Fan", "Ramp up logic.", "* PWM Ramp", "* Pico\n* Fan", "| Fan | 15 |", "* Loop", "* i", "**B. Loop**\n1. For i 0..65000: PWM(i). Wait.", "1. Accel.", "ramp()", "* Jerk", "* Stop")
    b += get_template("0542", "Gust Mode", "Random speed.", "* Random", "* Pico", "| - | - |", "* Rand", "* -", "**B. Loop**\n1. Speed = Rand.\n2. Wait.", "1. Wind.", "gust()", "* Stall", "* Noise")
    b += get_template("0543", "Manual Fan", "Pot Speed.", "* ADC", "* Pico\n* Pot", "| P | 26 |", "* Map", "* -", "**B. Loop**\n1. Read Pot.\n2. Write PWM.", "1. Ctrl.", "pot()", "* Rev", "* Heat")
    b += get_template("0544", "Sine Wave", "Oscillation.", "* Math", "* Pico", "| - | - |", "* Sin", "* -", "**B. Loop**\n1. PWM = sin(t).", "1. Wave.", "sine()", "* Float", "* Cast")
    b += get_template("0545", "Breath Control", "Mic blow.", "* Sound", "* Mic", "| M | 26 |", "* If", "* v", "**B. Loop**\n1. If Mic > Threshold: Spin.", "1. Blow.", "mic()", "* Level", "* Clip")
    b += get_template("0546", "Fan Modes", "Quiet/Turbo.", "* Switch", "* Pico", "| S | - |", "* If", "* m", "**B. Loop**\n1. If Sw: Max.\n2. Else: 30%.", "1. Sel.", "modes()", "* State", "* LED")
    b += get_template("0547", "Stall Alarm", "Check Move.", "* Sense", "* Hall", "| H | 16 |", "* If", "* rpm", "**B. Loop**\n1. If On and RPM=0: Alarm.", "1. Safety.", "stall()", "* False", "* Delay")
    b += get_template("0548", "Levitation Game", "PID Float.", "* PID", "* Ball", "| - | - |", "* PID", "* err", "**B. Loop**\n1. Read H.\n2. Adj Spd.", "1. Hover.", "pid()", "* Tune", "* Tube")
    b += get_template("0549", "Auto Fan", "Temp/Hum.", "* OneWire", "* DHT", "| D | 16 |", "* If", "* t", "**B. Loop**\n1. Read T.\n2. If T>30: On.", "1. Cool.", "auto()", "* Rate", "* Err")
    b += get_template("0550", "Tachometer", "Read RPM.", "* IRQ", "* Fan", "| T | 16 |", "* Irq", "* cnt", "**B. Loop**\n1. Count pulses.\n2. RPM = cnt*30.", "1. Meas.", "tach()", "* Pull", "* Noise")

    # Read and Replace
    with open(target_file, 'r', encoding='utf-8') as f:
        existing = f.read()

    # Find Batch 55 and Batch 56
    start = existing.find("#  Batch 55: Smart Fan 3")
    end = existing.find("#  Batch 56: Robotic Arm Basics 3")

    if start != -1 and end != -1:
        new_content = existing[:start] + b + existing[end:]
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    regen_batch_55()
