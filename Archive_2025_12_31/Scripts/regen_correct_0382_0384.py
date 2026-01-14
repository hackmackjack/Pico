# CORRECT BATCH: Kitchen Timer 2 (Projects 0382-0390)

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

kitchen_timer_batch = r'''
## 1️⃣ Project 0382: Blinking Kitchen Timer

### 2️⃣ Learning Objective
Create a visual progress indicator using multiple LEDs to show remaining time. You will learn about proportional LED control and linear decay visualization.

### 3️⃣ Concepts Introduced
*   **Progress Bar LED**: Using multiple LEDs to represent percentage completion.
*   **Linear Visual Decay**: As time decreases, LEDs turn off sequentially.
*   **Threshold Mapping**: Dividing time into equal segments for each LED.

### 4️⃣ Hardware Required
*   **Pico**
*   **5× LEDs**
*   **5× Resistors** (220Ω)
*   **Buzzer** (for alarm)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED 1** | GP16 | 100% time |
| **LED 2** | GP17 | 80% time |
| **LED 3** | GP18 | 60% time |
| **LED 4** | GP19 | 40% time |
| **LED 5** | GP20 | 20% time |
| **Buzzer** | GP15 | Alarm |

### 6️⃣ Blocks Used

🔹 **Digital Write**
*   **Category:** Pin Access

🔹 **Logic Comparison**
*   **Category:** Logic

🔹 **Variables**
*   **Category:** Variables

### 7️⃣ Variables & State
*   **totalTime**: Initial timer duration (e.g., 100 seconds).
*   **remainingTime**: Current countdown value.
*   **percentage**: Calculated as `(remainingTime / totalTime) * 100`.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [totalTime] to [100]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [remainingTime] to [totalTime]`.
        *   **Snap** below.
    *   From **Pin Access**, drag `Setup Pin:[16-20] as OUTPUT`.
        *   **Snap** below (for all 5 LEDs).

*   **B. Main Loop Phase**
    *   **Calculate Percentage**:
        *   From **Math**, drag `set [percentage] to [([remainingTime] / [totalTime]) * 100]`.
            *   **Snap** into loop.
    *   **LED Control**:
        *   From **Logic**, drag `if [percentage] >= [80] then`.
            *   **Snap** below.
            *   Inside: From **Pin Access**, drag `digital write pin:[16] value:[HIGH]`.
        *   From **Logic**, drag `else`.
            *   Inside: From **Pin Access**, drag `digital write pin:[16] value:[LOW]`.
        *   (Repeat for pins 17, 18, 19, 20 with thresholds 60%, 40%, 20%, 0%).
    *   **Countdown**:
        *   From **Variables**, drag `change [remainingTime] by [-1]`.
            *   **Snap** below.
    *   **Alarm Check**:
        *   From **Logic**, drag `if [remainingTime] <= [0] then`.
            *   **Snap** below.
            *   Inside: From **Actuators**, drag `Buzzer [15] beep`.
    *   From **Timing**, drag `sleep [1] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The timer starts at 100 seconds with all 5 LEDs lit. Every second, it checks the remaining percentage. When it drops below 80%, LED 1 turns off. At 60%, LED 2 off. At 40%, LED 3 off. At 20%, LED 4 off. When the timer reaches 0, all LEDs are off and the buzzer sounds. This provides instant visual feedback on how much time is left without looking at numbers.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

leds = [machine.Pin(16 + i, machine.Pin.OUT) for i in range(5)]
buzzer = machine.Pin(15, machine.Pin.OUT)

total_time = 100
remaining_time = total_time

while remaining_time > 0:
    percentage = (remaining_time / total_time) * 100
    
    # Control LEDs based on percentage
    leds[0].value(1 if percentage >= 80 else 0)
    leds[1].value(1 if percentage >= 60 else 0)
    leds[2].value(1 if percentage >= 40 else 0)
    leds[3].value(1 if percentage >= 20 else 0)
    leds[4].value(1 if percentage > 0 else 0)
    
    remaining_time -= 1
    time.sleep(1)

# Alarm
buzzer.value(1)
time.sleep(2)
buzzer.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **All LEDs Off Too Soon**: Ensure LED 5 stays on until 0%, not 20%.
*   **Flickering**: If LEDs flicker, the percentage calculation might have floating-point precision issues. Use integer comparison.

### 1️⃣2️⃣ Try This Next

*   **10 LEDs**: Use all 10 LEDs for 10% increments.
*   **Color Code**: Use red LEDs for the last 20% as a visual warning.

---

## 1️⃣ Project 0383: Manual Kitchen Timer Control

### 2️⃣ Learning Objective
Implement a button-based interface to quickly add time increments. You will learn about accumulator patterns and multi-button input handling.

### 3️⃣ Concepts Introduced
*   **Quick Add Interface**: Buttons that add predefined time chunks.
*   **Accumulator Logic**: Building up a total from multiple small additions.
*   **Reset Functionality**: Clearing accumulated values.

### 4️⃣ Hardware Required
*   **Pico**
*   **3× Buttons** (Add 10s, Add 1m, Clear)
*   **OLED Display** (to show total time)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button A (+10s)** | GP12 | PULL_DOWN |
| **Button B (+1m)** | GP13 | PULL_DOWN |
| **Button C (Clear)** | GP14 | PULL_DOWN |
| **OLED SDA** | GP0 | I2C0 |
| **OLED SCL** | GP1 | I2C0 |

### 6️⃣ Blocks Used

🔹 **Digital Read**
*   **Category:** Pin Access

🔹 **Change Variable**
*   **Category:** Variables

🔹 **OLED Text**
*   **Category:** Displays

### 7️⃣ Variables & State
*   **totalSeconds**: Accumulated timer duration.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Communication**, drag `Setup I2C SDA:[0] SCL:[1]`.
        *   **Snap** into setup block.
    *   From **Displays**, drag `Setup OLED I2C:[0]`.
        *   **Snap** below.
    *   From **Inputs**, drag `Setup Button pin:[12,13,14] as PULL_DOWN`.
        *   **Snap** below.
    *   From **Variables**, drag `set [totalSeconds] to [0]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Button A (+10 seconds)**:
        *   From **Logic**, drag `if [digital read pin 12] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `change [totalSeconds] by [10]`.
                    *   **Snap** inside.
                *   From **Timing**, drag `sleep [0.3] seconds`.
                    *   **Snap** below (debounce).
    *   **Button B (+60 seconds)**:
        *   From **Logic**, drag `if [digital read pin 13] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [totalSeconds] by [60]`.
                *   From **Timing**, drag `sleep [0.3] seconds`.
    *   **Button C (Clear)**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `set [totalSeconds] to [0]`.
                *   From **Timing**, drag `sleep [0.3] seconds`.
    *   **Display Update**:
        *   From **Displays**, drag `OLED clear`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED text [Total: {totalSeconds}s]`.
            *   **Snap** below.
        *   From **Displays**, drag `OLED show`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The screen starts at "Total: 0s". Pressing Button A adds 10 seconds each time. Pressing Button B adds 60 seconds (1 minute). The total accumulates—pressing A five times and B once results in 110 seconds. Button C resets to zero. This provides a tactile, button-based interface for setting timer duration without typing or dials.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

btnA = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnC = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

total_seconds = 0

while True:
    if btnA.value():
        total_seconds += 10
        time.sleep(0.3)
    
    if btnB.value():
        total_seconds += 60
        time.sleep(0.3)
    
    if btnC.value():
        total_seconds = 0
        time.sleep(0.3)
    
    oled.fill(0)
    oled.text(f"Total: {total_seconds}s", 0, 0)
    oled.show()
    time.sleep(0.1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Double Counting**: Without debounce delay, one press registers multiple times.
*   **Overflow**: Consider capping `totalSeconds` at a maximum (e.g., 3600) to prevent unrealistic values.

### 1️⃣2️⃣ Try This Next

*   **Subtract Buttons**: Add buttons to decrease by 10s or 1m.
*   **Start Timer**: Add a 4th button that begins the countdown from the accumulated total.

---

## 1️⃣ Project 0384: Kitchen Timer Sequences

### 2️⃣ Learning Objective
Create a multi-stage timer for recipe sequences (e.g., tea brewing stages). You will learn about state machine programming and automatic phase transitions.

### 3️⃣ Concepts Introduced
*   **Multi-Stage Timer**: Different durations for each cooking phase.
*   **Recipe Sequencer**: Automating complex multi-step processes.
*   **Stage-Specific Alarms**: Different tones/patterns for each stage completion.

### 4️⃣ Hardware Required
*   **Pico**
*   **Buzzer**
*   **OLED Display** (optional)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer** | GP15 | PWM |

### 6️⃣ Blocks Used

🔹 **Variables (Stage)**
*   **Category:** Variables

🔹 **Buzzer Tone**
*   **Category:** Actuators

🔹 **If/Else If**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **stage**: Current stage number (1, 2, or 3).
*   **timeLeft**: Seconds remaining in current stage.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [stage] to [1]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [timeLeft] to [120]`.
        *   **Snap** below (Stage 1: Boil = 2 minutes).

*   **B. Main Loop Phase**
    *   **Countdown**:
        *   From **Variables**, drag `change [timeLeft] by [-1]`.
            *   **Snap** into loop.
        *   From **Console**, drag `print [Stage {stage}: {timeLeft}s remaining]`.
            *   **Snap** below.
        *   From **Timing**, drag `sleep [1] seconds`.
            *   **Snap** below.
    *   **Stage Transition**:
        *   From **Logic**, drag `if [timeLeft] <= [0] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Logic**, drag `if [stage] = [1] then`.
                    *   **Snap** inside.
                    *   Inside:
                        *   From **Actuators**, drag `Buzzer [15] tone [1000] for [500]ms`.
                            *   **Snap** inside.
                        *   From **Console**, drag `print [Boil Complete! Starting Steep...]`.
                            *   **Snap** below.
                        *   From **Variables**, drag `set [stage] to [2]`.
                            *   **Snap** below.
                        *   From **Variables**, drag `set [timeLeft] to [180]`.
                            *   **Snap** below (Stage 2: Steep = 3 minutes).
                *   From **Logic**, drag `else if [stage] = [2] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Actuators**, drag `Buzzer [15] tone [1500] for [500]ms`.
                        *   From **Console**, drag `print [Steep Complete! Starting Cool...]`.
                        *   From **Variables**, drag `set [stage] to [3]`.
                        *   From **Variables**, drag `set [timeLeft] to [60]`.
                            *   **Snap** below (Stage 3: Cool = 1 minute).
                *   From **Logic**, drag `else`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Actuators**, drag `Buzzer [15] tone [2000] for [1000]ms`.
                        *   From **Console**, drag `print [All Stages Complete! Tea Ready!]`.
                        *   `break` or `while True: pass`.

### 9️⃣ Execution Flow (Plain English)

The timer starts in Stage 1 (Boil) for 120 seconds. When it reaches 0, a medium-pitch beep sounds, and the timer automatically switches to Stage 2 (Steep) for 180 seconds. After Steep finishes, a higher-pitch beep plays, and it moves to Stage 3 (Cool) for 60 seconds. When all stages finish, a long, high-pitched alarm sounds to indicate the tea is ready to drink.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

buzzer = machine.PWM(machine.Pin(15))

stage = 1
time_left = 120  # Stage 1: Boil (2 minutes)

while stage <= 3:
    print(f"Stage {stage}: {time_left}s remaining")
    time.sleep(1)
    time_left -= 1
    
    if time_left <= 0:
        if stage == 1:
            buzzer.freq(1000)
            buzzer.duty_u16(32768)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            print("Boil Complete! Starting Steep...")
            stage = 2
            time_left = 180
        elif stage == 2:
            buzzer.freq(1500)
            buzzer.duty_u16(32768)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            print("Steep Complete! Starting Cool...")
            stage = 3
            time_left = 60
        else:
            buzzer.freq(2000)
            buzzer.duty_u16(32768)
            time.sleep(1)
            buzzer.duty_u16(0)
            print("All Stages Complete! Tea Ready!")
            break
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Stage Never Advances**: Ensure `stage` is incremented inside the `if timeLeft <= 0` block.
*   **Immediate Skip**: If you check `timeLeft <= 0` and set `stage` in the same loop iteration, it might skip stages. Use `elif` properly.

### 1️⃣2️⃣ Try This Next

*   **Variable Stages**: Load recipes from a list: `recipes = [(120, "Boil"), (180, "Steep"), (60, "Cool")]`.
*   **Pause/Resume**: Add a button to pause the timer at any stage.

---

(Due to token limits, I'll continue with remaining projects 0385-0390 in the next script file)
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(kitchen_timer_batch)

print("✅ Generated Projects 0382-0384 (Kitchen Timer 2)")
print("📋 Continuing with 0385-0390...")
