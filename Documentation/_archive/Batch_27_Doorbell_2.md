# 📘 Pico 2500: Batch 27 - Doorbell 2 (Projects 0261-0270)

**Grade Level:** 3-5 (Elementary)  
**Bloom's Level:** Remember/Understand  
**Theme:** Advanced Audio and Access Control Systems

---

## 1️⃣ Project 0261: Polyphonic Doorbell Tunes

### 2️⃣ Learning Objective
Learn to generate multi-tone "chords" or rapid sequences to create pleasant doorbell chimes (Ding-Dong) instead of simple beeps.

### 3️⃣ Concepts Introduced
*   Tone Frequencies (Hz)
*   Musical Intervals
*   Duration Control
*   Decay/Sustain (Envelope basics)

### 4️⃣ Hardware Required
*   Raspberry Pi Pico
*   Passive Buzzer / Speaker
*   Pushbutton (Doorbell)
*   Breadboard & Wires

### 5️⃣ Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Buzzer (+) | GP15 | PWM Capable |
| **Buzzer (-) | GND | |
| **Button** | GP14 | Pull-down |

### 6️⃣ Blocks Used
🔹 **Play Tone**
*   **Category:** Smart IO / Audio
*   **Block:** `pico_play_tone(pin, freq, duration)`

### 8️⃣ Step-by-Step Guide
**A. Logic**
1. Wait for Button Press.
2. Play Note 1 (High E - 659Hz) for 0.5s.
3. Play Note 2 (Low C - 523Hz) for 1.0s.
4. Silence.

### 10️⃣ Generated Code
```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(15))
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Frequencies
E5 = 659
C5 = 523

def play(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(32768) # 50% volume
    time.sleep(duration)
    buzzer.duty_u16(0)     # Stop

print("Doorbell Ready")

while True:
    if btn.value():
        print("Ding-Dong!")
        play(E5, 0.6)
        play(C5, 1.0)
        time.sleep(0.5) # Debounce
```

---

## 1️⃣ Project 0262: Wireless Doorbell (IR)

### 2️⃣ Learning Objective
Eliminate the wire! Use an Infrared (IR) Remote to trigger the doorbell from "outside" (across the room).

### 3️⃣ Concepts Introduced
*   Wireless Communication
*   IR Receiver
*   Signal Decoding
*   Remote Triggers

### 4️⃣ Hardware
*   IR Receiver (VS1838B)
*   IR Remote
*   Buzzer

### 5️⃣ Wiring
| IR Receiver | Pico Pin |
| :--- | :--- |
| Signal | GP16 |

### 10️⃣ Generated Code
```python
ir_pin = Pin(16, Pin.IN)

# Simplified IR detect (Real logic uses library)
while True:
    if ir_pin.value() == 0: # Active LOW usually
        print("Signal Received")
        play(E5, 0.5)
        play(C5, 0.8)
        time.sleep(1)
```

---

## 1️⃣ Project 0263: Video Doorbell (Camera Trigger)

### 2️⃣ Learning Objective
Simulate a smart doorbell mechanism that sends a "Trigger Signal" to an external system (like a camera) when pressed.

### 3️⃣ Concepts Introduced
*   Output Triggers
*   System Integration
*   Handshaking signals
*   Simulated Latency

### 10️⃣ Generated Code
```python
camera_trigger = Pin(20, Pin.OUT)

while True:
    if btn.value():
        # 1. Ring Bell
        play(659, 0.5)
        
        # 2. Trigger Camera (Pulse)
        camera_trigger.value(1)
        time.sleep(0.1)
        camera_trigger.value(0)
        print("📸 Snapshot Taken")
        
        play(523, 1.0)
```

---

## 1️⃣ Project 0264: Visitor Counter

### 2️⃣ Learning Objective
Track how many times the doorbell has been rung using a variable, and store it for review.

### 3️⃣ Concepts Introduced
*   Variables (Counters)
*   Incrementing
*   Data Persistence (Concept)

### 10️⃣ Generated Code
```python
visitor_count = 0

while True:
    if btn.value():
        visitor_count += 1
        print(f"Visitor #{visitor_count}")
        play(E5, 0.5)
        
        # Wait for release so we don't count once per millisecond
        while btn.value():
            time.sleep(0.1)
```

---

## 1️⃣ Project 0265: Custom Tune Library

### 2️⃣ Learning Objective
Allow the user to select from different ringtones (Westminster, DingDong, Buzzer) using a selector switch.

### 3️⃣ Concepts Introduced
*   Arrays / Lists of Tunes
*   Selection Logic
*   Data Structures for Music

### 10️⃣ Generated Code
```python
# Tune 1: Westminster
tune1 = [(659, 0.5), (523, 0.5), (587, 0.5), (392, 1.0)] 
# Tune 2: Generic
tune2 = [(880, 0.2), (0, 0.1), (880, 0.2)]

selector = Pin(10, Pin.IN, Pin.PULL_UP) # Switch

def play_tune(tune):
    for note, dur in tune:
        if note == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(note)
            buzzer.duty_u16(32768)
        time.sleep(dur)
    buzzer.duty_u16(0)

while True:
    if btn.value():
        if selector.value() == 0:
            play_tune(tune1)
        else:
            play_tune(tune2)
```

---

## 1️⃣ Project 0266: Volume Control

### 2️⃣ Learning Objective
Use a potentiometer or button to adjust the loudness of the buzzer using PWM Duty Cycle.

### 3️⃣ Concepts Introduced
*   PWM Duty = Amplitude (Volume)
*   Mapping Input to Output
*   Dynamic Adjustment

### 10️⃣ Generated Code
```python
vol_pot = ADC(Pin(26))

def play_with_volume(freq):
    # Read Pot: 0-65535
    volume = vol_pot.read_u16() 
    # Max safe duty is 32768 (50% square wave)
    duty = int(volume / 2) 
    
    buzzer.freq(freq)
    buzzer.duty_u16(duty)

if btn.value():
    play_with_volume(659)
    time.sleep(0.5)
    buzzer.duty_u16(0)
```

---

## 1️⃣ Project 0267: Do-Not-Disturb Mode (Silent)

### 2️⃣ Learning Objective
Add a "Silent Switch". If active, the bell creates a visual flash (Light) instead of playing a sound.

### 3️⃣ Concepts Introduced
*   Mode Logic
*   Accessibility Features (Visual Alert)
*   Conditional Output Routing

### 10️⃣ Generated Code
```python
dnd_switch = Pin(11, Pin.IN) # Toggle switch
flash_led = Pin(16, Pin.OUT)

while True:
    if btn.value():
        if dnd_switch.value():
            # Silent Mode: Flash Light
            print("Silent Ring...")
            for i in range(5):
                flash_led.toggle()
                time.sleep(0.2)
        else:
            # Normal: Sound
            play(E5, 0.5)
```

---

## 1️⃣ Project 0268: Smart Lock Integration (Servo)

### 2️⃣ Learning Objective
Combine the doorbell with an "Unlock" button that moves a Servo motor to open the door remotely.

### 3️⃣ Concepts Introduced
*   Servo Motors
*   Mechanical Actuation
*   Remote Access Control

### 10️⃣ Generated Code
```python
servo = PWM(Pin(21))
servo.freq(50)

unlock_btn = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Simple servo move
def open_door():
    servo.duty_u16(4000) # Open position
    time.sleep(3)
    servo.duty_u16(8000) # Close position

if unlock_btn.value():
    print("Unlocking...")
    open_door()
```

---

## 1️⃣ Project 0269: Doorbell with Display

### 2️⃣ Learning Objective
Use an I2C LCD or OLED to display "Please Wait" or "Ringing..." to the visitor.

### 3️⃣ Concepts Introduced
*   User Feedback
*   Display States
*   I2C Communication

### 10️⃣ Generated Code
```python
# Assuming LCD library
from machine import I2C
# i2c = I2C(0, ...)
# lcd = LCD(i2c)

if btn.value():
    lcd.clear()
    lcd.putstr("Ringing...")
    play_tune()
    lcd.clear()
    lcd.putstr("Ready")
```

---

## 1️⃣ Project 0270: Smart Doorbell Hub

### 2️⃣ Learning Objective
The ultimate system combining: Camera Trigger, Silent Mode, Volume Control, LCD Display, and Servo Lock.

### 3️⃣ Features
1. **Inputs:** Door Button, Unlock Button, DND Switch, Volume Pot.
2. **Outputs:** Buzzer, Flash LED, Servo Lock, LCD.

### 10️⃣ Generated Code
```python
# Master Loop
while True:
    # 1. Check Doorbell
    if btn_door.value():
        lcd.print("Visitor!")
        if dnd.value():
            flash_light()
        else:
            play_sound(vol_pot.read())
            
    # 2. Check Unlock
    if btn_unlock.value():
        lcd.print("Unlocking")
        move_servo()
```

---

**Batch 27 Complete & Fixed.**
