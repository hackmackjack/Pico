
# 🏁 Batch 3: Sound & Music 1

## 1️⃣ Project 0021: Introduction to Sound & Music
### 2️⃣ Learning Objective
Generate audio output. You will control an Active Buzzer to make simple beep sounds, learning that "Sound" in electronics is just turning a voltage on and off.

### 3️⃣ Concepts Introduced
*   **Active vs Passive**: Active buzzers generate their own tone when powered.
*   **Auditory Feedback**: Information via ears.

### 4️⃣ Hardware Required
*   **Pico**
*   **Active Buzzer** (Sticker usually covering hole)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+)** | GP15 | Long Leg |
| **Buzzer (-)** | GND | Short Leg |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [15] to [HIGH]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Init**: Pin 15 Output.
*   **B. Loop**:
    *   Pin 15 HIGH (Beep).
    *   Wait 0.5s.
    *   Pin 15 LOW (Silence).
    *   Wait 0.5s.

### 9️⃣ Execution Flow (Plain English)
Identical to blinking an LED, but instead of light, the component vibrates air. High Voltage = Beep. Low Voltage = Silence.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

buzzer = machine.Pin(15, machine.Pin.OUT)

while True:
    buzzer.value(1) # Beep
    time.sleep(0.5)
    buzzer.value(0) # Silence
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Wrong Buzzer**: If applied voltage makes a "click" but no tone, you have a **Passive Buzzer**. You need PWM code (Project 0024) for that. Active buzzers usually have a black seal on top.
*   **Quiet**: Buzzers need current. Direct GPIO is barely enough. It works but may be quiet.

### 1️⃣2️⃣ Try This Next
*   **Morse Code**: Beep S-O-S (... --- ...). Simple timing challenge.

---

## 1️⃣ Project 0022: Blinking Sound (Sync)
### 2️⃣ Learning Objective
Synchronize multiple outputs. You will ensure an LED and a Buzzer fire at the exact same time, creating a cohesive "Alarm" effect.

### 3️⃣ Concepts Introduced
*   **Parallel Actuation**: Driving two pins in consecutive lines of code.

### 4️⃣ Hardware Required
*   **Pico**
*   **Active Buzzer**
*   **Red LED**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Buzzer** | GP15 |
| **LED** | GP14 |

### 6️⃣ Blocks Used
🔹 **Set Pin**
*   **Category:** Pin Access
*   **Block:** `set Pin [14] to [HIGH]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Init**: Pins 14, 15 Output.
*   **B. Loop**:
    *   Pin 14 HIGH (LED), Pin 15 HIGH (Buzz).
    *   Wait 0.5s.
    *   Pin 14 LOW, Pin 15 LOW.
    *   Wait 0.5s.

### 9️⃣ Execution Flow (Plain English)
The Pico executes instructions so fast that even though "Turn LED On" happens *before* "Turn Buzzer On", humans perceive them as simultaneous. This creates a strong "Alert" sensation.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

led = machine.Pin(14, machine.Pin.OUT)
buzz = machine.Pin(15, machine.Pin.OUT)

while True:
    led.value(1)
    buzz.value(1)
    time.sleep(0.5)
    led.value(0)
    buzz.value(0)
    time.sleep(0.5)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Sequential vs Simultaneous**: If you put a `sleep` between turning the LED on and the Buzzer on, they will drift out of sync. Group commands together.

### 1️⃣2️⃣ Try This Next
*   **Alternating**: LED On when Buzzer Off. (Police Siren style visual).

---

## 1️⃣ Project 0023: Manual Sound Control (Doorbell)
### 2️⃣ Learning Objective
Create a user-interactive sound device. The buzzer sounds only while the button is pressed, behaving exactly like a basic doorbell.

### 3️⃣ Concepts Introduced
*   **Direct Feedback**: Input state = Output state.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Active Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else**
*   **Category:** Logic
*   **Block:** `if [Button] then [Buzz] else [Silence]`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Init**: Setup.
*   **B. Loop**:
    *   IF Button Pressed: Buzzer Pin HIGH.
    *   ELSE: Buzzer Pin LOW.

### 9️⃣ Execution Flow (Plain English)
The buzzer mirrors the button. Button Down -> Buzz. Button Up -> Silence.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)

while True:
    if btn.value():
        buzz.value(1)
    else:
        buzz.value(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Latching**: Students sometimes write code that turns the buzzer ON but forgets to turn it OFF when the button is released, leading to an endless screech.

### 1️⃣2️⃣ Try This Next
*   **Ding-Dong**: When pressed, play "High Tone", wait, then "Low Tone" (Requires Passive Buzzer).

---

## 1️⃣ Project 0024: Sound Sequences (Passive Melody)
### 2️⃣ Learning Objective
Generate specific frequencies. You will use a **Passive Buzzer** and Pulse Width Modulation (PWM) to sing specific musical notes (Do, Re, Mi) in a sequence.

### 3️⃣ Concepts Introduced
*   **Frequency**: Hertz (Hz). Vibrations per second.
*   **PWM Frequency**: Controlling pitch.
*   **Duty Cycle**: (usually 50% for sound).

### 4️⃣ Hardware Required
*   **Pico**
*   **Passive Buzzer** (No sticker, visible Circuit Board)

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Play Tone** (or PWM Block)
*   **Category:** Music/Audio
*   **Block:** `Play Frequency [262] Hz for [0.5] seconds`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **A. Init**: PWM on GP15.
*   **B. Loop**:
    *   Play 262Hz (C4) for 0.5s.
    *   Play 294Hz (D4) for 0.5s.
    *   Play 330Hz (E4) for 0.5s.
    *   Silence (0Hz) for 1s.

### 9️⃣ Execution Flow (Plain English)
The Pico vibrates the speaker membrane 262 times a second, then 294 times, then 330. Our brain interprets these vibration speeds as musical notes.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

buzz = machine.PWM(machine.Pin(15))

def play(freq, duration):
    buzz.freq(freq)
    buzz.duty_u16(32768) # 50% volume
    time.sleep(duration)
    buzz.duty_u16(0)     # Stop

while True:
    play(262, 0.5) # C
    play(294, 0.5) # D
    play(330, 0.5) # E
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Active Buzzer**: If used here, it will just make a weird "squeak" or constant tone, ignoring the frequency changes. You MUST use a Passive variant.
*   **Duty Cycle**: For sound, 50% duty is loudest. 100% duty is DC voltage (Silence/Heat).

### 1️⃣2️⃣ Try This Next
*   **Song**: Code "Twinkle Twinkle Little Star" (CC GGA AG...).

---

## 1️⃣ Project 0025: Interactive Sound (Piano)
### 2️⃣ Learning Objective
Map inputs to pitches. You will build a 2-key keyboard where Button A plays a low note and Button B plays a high note.

### 3️⃣ Concepts Introduced
*   **Input-Output Mapping**: Input A -> Output X.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button A, Button B**
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button A** | GP10 |
| **Button B** | GP11 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **If / Else If**
*   **Category:** Logic
*   **Block:** `if [BtnA] play [C4]...`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF BtnA: PWM Freq 262Hz, Duty 50%.
    *   ELSE IF BtnB: PWM Freq 392Hz (G), Duty 50%.
    *   ELSE: Duty 0% (Silence).

### 9️⃣ Execution Flow (Plain English)
The buzzer waits. Pressing a key sets the vibration speed immediately. Releasing it kills the vibration. You can play rhythmic tunes by tapping the buttons.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

buzz = machine.PWM(machine.Pin(15))
btnA = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
btnB = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if btnA.value():
        buzz.freq(262)
        buzz.duty_u16(32768)
    elif btnB.value():
        buzz.freq(392)
        buzz.duty_u16(32768)
    else:
        buzz.duty_u16(0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Clicking**: If the loop runs too slow, you might hear "clicking" instead of a tone.
*   **Polyphony**: Cannot play both at once (Pico has 1 buzzer). Priority logic decides which note wins if both pressed.

### 1️⃣2️⃣ Try This Next
*   **Octaves**: Use a 3rd button to shift everything up an Octave (Frequency * 2).

---

## 1️⃣ Project 0026: Smart Sound Switch (Mute)
### 2️⃣ Learning Objective
Control system settings with a persistent flag. You will make an alarm that runs continuously, but can be silenced (Muted) by toggling a switch.

### 3️⃣ Concepts Introduced
*   **Flags**: `isMuted`.
*   **Conditional Execution**: Run code only if `not Muted`.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button**
*   **Active Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Variable**
*   **Category:** Variables
*   **Block:** `isMuted`

### 7️⃣ Variables & State
*   **isMuted**: Boolean.

### 8️⃣ Block Logic
*   **Init**: `isMuted` = False.
*   **Loop**:
    *   (Logic to toggle `isMuted` on button press).
    *   **Action**:
        *   IF `not isMuted`: Beep (On/Off).
        *   ELSE: Wait 1s (Silent).

### 9️⃣ Execution Flow (Plain English)
The alarm logic runs constantly. However, before it plays a sound, it checks the "Mute" rule. If Mute is On, it skips the sound and just waits quietly. This demonstrates how software can override hardware behaviors.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)
muted = False

while True:
    if btn.value():
        muted = not muted
        while btn.value(): time.sleep(0.1) # Wait release
    
    if not muted:
        buzz.value(1)
        time.sleep(0.1)
        buzz.value(0)
        time.sleep(0.9)
    else:
        time.sleep(1.0)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Responsiveness**: If the beep is long (e.g., 2 seconds), pressing the Mute button might respond slowly because the code is stuck in `sleep`.

### 1️⃣2️⃣ Try This Next
*   **Visual Mute**: Light up a Red LED when Mute is active so the user knows why it's quiet.

---

## 1️⃣ Project 0027: Sound Alarm System (Reverse Truck)
### 2️⃣ Learning Objective
Modulate frequency based on danger. A "Reverse Alarm" beeps slowly normally. When a sensor (simulated by button) triggers, it beeps frantically.

### 3️⃣ Concepts Introduced
*   **Context Awareness**: Changing behavior based on context (Safe vs Danger).
*   **Variable Delay**: Using a variable for `time.sleep()`.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Simulates Obstacle Sensor)
*   **Active Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Button** | GP14 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Variable**
*   **Category:** Variables
*   **Block:** `delayTime`

### 7️⃣ Variables & State
*   **delayTime**: Seconds.

### 8️⃣ Block Logic
*   **Loop**:
    *   IF Button Pressed: `delayTime` = 0.1s.
    *   ELSE: `delayTime` = 1.0s.
    *   **Action**: Beep, Wait `delayTime`, Silence, Wait `delayTime`.

### 9️⃣ Execution Flow (Plain English)
The code sets the "Pace" of the loop based on the button. Then it executes the Beep-Wait sequence using that pace. This efficiently handles both fast and slow modes with one block of code.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzz = machine.Pin(15, machine.Pin.OUT)

while True:
    if btn.value():
        delay = 0.1
    else:
        delay = 1.0
        
    buzz.value(1)
    time.sleep(delay)
    buzz.value(0)
    time.sleep(delay)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Logic Separation**: Don't write two separate Beep logic blocks (one for fast, one for slow). Write one beep block and use a variable for the speed. It's cleaner code (DRY - Don't Repeat Yourself).

### 1️⃣2️⃣ Try This Next
*   **Ramp**: Make the beeps get faster and faster as long as the button is held (Approaching object).

---

## 1️⃣ Project 0028: The Sound Game (Simon Says)
### 2️⃣ Learning Objective
Memorize and repeat auditory patterns. The Pico plays a sequence (Low-Med-High). You must match it.

### 3️⃣ Concepts Introduced
*   **Lists/Arrays**: Storing a sequence `[262, 330, 392]`.
*   **Verification**: Checking input against memory.

### 4️⃣ Hardware Required
*   **Pico**
*   **3 Buttons**
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Btn Low/Med/High** | GP10, GP11, GP12 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **List**
*   **Category:** Lists
*   **Block:** `list [262, 330, 392]`

### 7️⃣ Variables & State
*   **sequence**: List of tones.

### 8️⃣ Block Logic
*   **Init**: Define Tones.
*   **Loop**:
    *   Play Tones 1, 2, 3.
    *   Wait for Button Press 1. IF correct, Good. ELSE fail.
    *   Wait for Button Press 2...
    *   Wait for Button Press 3...

### 9️⃣ Execution Flow (Plain English)
The Pico "Says" the pattern (plays tones). Then it listens. If you press the buttons in the matching pitch order, it plays a victory jingle.

### 🔟 Generated Code (Reference Only)
```python
# Simplified Logic 
import machine, time
buzz = machine.PWM(machine.Pin(15))
# Define play()...

while True:
    # Simon Says
    play(262, 0.5); play(330, 0.5); play(392, 0.5)
    
    # Listen (Pseudocode)
    # wait_for_input()
    # verify_input()
    time.sleep(2)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Complexity**: Full Simon Says logic is complex for beginners. Start with a fixed sequence (always Low-Med-High) before randomizing it.

### 1️⃣2️⃣ Try This Next
*   **Expansion**: Add a 4th note.

---

## 1️⃣ Project 0029: Automated Sound (Theremin)
### 2️⃣ Learning Objective
Convert analog data to frequency. Use a Light Sensor to alter pitch continuously. Waving your hand creates spooky "Theremin" music.

### 3️⃣ Concepts Introduced
*   **Mapping**: Converting Range A (0-65535 Light) to Range B (100-2000 Hz).
*   **Real-time response**: Instant auditory feedback.

### 4️⃣ Hardware Required
*   **Pico**
*   **LDR** (Analog)
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **LDR** | GP26 |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Map Range**
*   **Category:** Math
*   **Block:** `map [value] from low [0] high [65535] to low [100] high [2000]`

### 7️⃣ Variables & State
*   **val**: Raw Light.
*   **pitch**: Mapped Hz.

### 8️⃣ Block Logic
*   **Loop**:
    *   `val` = Read Analog 26.
    *   `pitch` = Map `val` (0-65000) -> (100-2000).
    *   Set Buzzer Freq to `pitch`. Duty 50%.
    *   Wait 0.05s.

### 9️⃣ Execution Flow (Plain English)
The darker it is, the lower the tone. The brighter, the higher. Because the loop waits only 0.05s, the pitch slides smoothly as you move your hand over the sensor.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time

ldr = machine.ADC(26)
buzz = machine.PWM(machine.Pin(15))

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    val = ldr.read_u16()
    pitch = map_range(val, 0, 65535, 100, 2000)
    
    buzz.freq(pitch)
    buzz.duty_u16(32768)
    time.sleep(0.05)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Zero Error**: If `map` output is 0 or negative, `buzz.freq()` will crash. Ensure minimum is e.g. 50Hz.
*   **Range**: LDRs might not reach full 0 or full 65535. Adjust input range to matches your room (e.g., 20000 to 50000).

### 1️⃣2️⃣ Try This Next
*   **Discrete Notes**: Force the pitch to "snap" to the nearest musical note (Auto-tune).

---

## 1️⃣ Project 0030: Mastering Sound (Mario Coin)
### 2️⃣ Learning Objective
Recreate a specific sound effect using precise envelopes. A "Coin" sound is B5 (988Hz) for 0.1s followed by E6 (1319Hz) for 0.3s.

### 3️⃣ Concepts Introduced
*   **Envelope**: How a sound changes over time (Attack, Decay, Sustain, Release) - simplified here to Pitch change.
*   **Timbre**: (Limited control, but pulse width affects it).

### 4️⃣ Hardware Required
*   **Pico**
*   **Passive Buzzer**

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin |
| :--- | :--- |
| **Buzzer** | GP15 |

### 6️⃣ Blocks Used
🔹 **Play Tone**
*   **Category:** Music
*   **Block:** `Play [988] Hz`

### 7️⃣ Variables & State
*   None.

### 8️⃣ Block Logic
*   **Loop**:
    *   Play 988 Hz for 0.08s.
    *   Play 1319 Hz for 0.2s.
    *   Silence for 2s.

### 9️⃣ Execution Flow (Plain English)
The rapid jump from high frequency to higher frequency creates the iconic "Bling!" sound. The timings must be short; too long and it sounds like a siren, not a coin.

### 🔟 Generated Code (Reference Only)
```python
import machine
import time
buzz = machine.PWM(machine.Pin(15))

while True:
    # Note 1
    buzz.freq(988)
    buzz.duty_u16(32768)
    time.sleep(0.08)
    
    # Note 2
    buzz.freq(1319)
    buzz.duty_u16(32768)
    time.sleep(0.25)
    
    # Silence
    buzz.duty_u16(0)
    time.sleep(2)
    
    # It's-a-me, Pico!
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips
*   **Sluggishness**: Using delays > 0.1s ruins the effect. It must be snappy.

### 1️⃣2️⃣ Try This Next
*   **Jump Sound**: Implement the rising slide (sweep) of a character jumping. (Loop freq from 400 to 800).

---
