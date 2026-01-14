# Batch 46: Night Light 3 (Projects 0451-0460) - Elite Standard v2.0

## Project 0451: Introduction to Night Light

### 2. Learning Objective
Implement automatic nightlight using LDR threshold detection.

### 3. Concepts
Light threshold, Auto-on in darkness, Energy-saving automation

### 4. Hardware
Pico, LDR, LED, 10kΩ resistor

### 5. Wiring
LDR: GP26 (ADC0) | LED: GP16

### 6. Blocks Used
*   **from Smart IO, drag `pico_analog_read`** (read light level)
*   **from Logic, drag `if_compare`** (threshold check)
*   **from Smart IO, drag `pico_gpio_write`** (control LED)

### 7. Variables
lightLevel: ADC value | threshold: 15000 (darkness limit)

### 8. Guide
Loop: Read LDR → if value < threshold (dark): LED on, else: LED off

### 10. Code
```python
import machine, time
ldr = machine.ADC(26)
led = machine.Pin(16, machine.Pin.OUT)
threshold = 15000

while True:
    led.value(1 if ldr.read_u16() < threshold else 0)
    time.sleep(1)
```

---

## Project 0452: Blinking Night Light

### 2. Objective
Pulsing LED fade effect for gentle night illumination.

### 6. Blocks
*   **from Smart IO, drag `pico_pwm_write`** (variable brightness)
*   **from Loops, drag `for_in_range`** (fade cycle)
*   **from Math, drag `sine_wave`** (smooth pulsing)

### 8. Guide
Loop brightness 0→100→0 using sine wave over 2 seconds for smooth breathing effect.

### 10. Code
```python
import machine, time, math
led = machine.PWM(machine.Pin(16)); led.freq(1000)

while True:
    for i in range(100):
        brightness = int((math.sin(i/100*math.pi)*32768) + 32768)
        led.duty_u16(brightness)
        time.sleep(0.02)
```

---

## Project 0453: Manual Night Light Control

### 2. Objective
Button toggles nightlight on/off with memory.

### 6. Blocks
*   **from Smart IO, drag `pico_gpio_read`** (button)
*   **from Variables, drag `set_variable`** (toggle state)
*   **from Smart IO, drag `pico_gpio_write`** (LED)

### 8. Guide
Edge detection: if button pressed (rising edge) → toggle isOn state → update LED

---

## Project 0454: Night Light Sequences

### 2. Objective
Multi-color LED sequence for nighttime ambiance.

### 6. Blocks
*   **from Smart IO, drag `pico_pwm_write`** (R/G/B channels)
*   **from Variables, drag `create_list`** (color patterns)
*   **from Loops, drag `for_in_list`** (cycle through colors)

### 8. Guide
Sequence: Red (2s) → Green (2s) → Blue (2s) → Purple (2s) → repeat

---

## Project 0455: Interactive Night Light

### 2. Objective
PIR sensor activates nightlight when motion detected.

### 6. Blocks
*   **from Sensors, drag `pir_read`** (motion detection)
*   **from Smart IO, drag `pico_gpio_write`** (LED control)
*   **from Time, drag `pico_wait`** (timeout timer)

### 8. Guide
If PIR detects motion → LED on for 30 seconds → if no more motion: LED off

---

## Project 0456: Smart Night Light Switch

### 2. Objective
Dual-mode: Auto (LDR) or Manual (button override).

### 6. Blocks
*   **from Smart IO, drag `pico_analog_read`** (LDR)
*   **from Smart IO, drag `pico_gpio_read`** (mode button)
*   **from Logic, drag `if_compare`** (mode selection)

### 8. Guide
Mode button toggles auto/manual. Auto: use LDR threshold. Manual: button controls LED.

---

## Project 0457: Night Light Alarm System

### 2. Objective
Bright flash alarm when LDR detects sudden brightness (intruder/light).

### 6. Blocks
*   **from Smart IO, drag `pico_analog_read`** (monitor light changes)
*   **from Math, drag `calculate_delta`** (sudden change detection)
*   **from Smart IO, drag `pico_gpio_write`** (flash LED alarm)

### 8. Guide
Track previous light level. If current - previous > 10000 (sudden bright): flash LED 10 times

---

## Project 0458: The Night Light Game

### 2. Objective
Reaction game: LED flashes randomly, press button to catch the light.

### 6. Blocks
*   **from Math, drag `random_int`** (random timing)
*   **from Smart IO, drag `pico_gpio_write`** (LED flash)
*   **from Smart IO, drag `pico_gpio_read`** (button press)
*   **from Time, drag `time_ticks_ms`** (reaction time measurement)

### 8. Guide
Random delay (1-5s) → LED flash → measure time until button press → display score

---

## Project 0459: Automated Night Light

### 2. Objective
Gradual fade-in at sunset based on time-of-day simulation.

### 6. Blocks
*   **from Time, drag `time_ticks_ms`** (track elapsed time)
*   **from Math, drag `map_range`** (time to brightness)
*   **from Smart IO, drag `pico_pwm_write`** (gradual brightness)

### 8. Guide
Simulate day cycle: 6am=off, fade in 6pm-7pm (0-100%), stay on night, fade out 6am-7am

---

## Project 0460: Mastering Night Light

### 2. Objective
Neopixel RGB strip with color temperature adjustment (warm→cool).

### 6. Blocks
*   **from Smart IO, drag `neopixel_write`** (RGB control)
*   **from Variables, drag `create_list`** (color temperature values)
*   **from Math, drag `interpolate`** (smooth color transition)

### 8. Guide
Pot controls color temp: Left=warm (255,100,0), Middle=neutral (200,200,200), Right=cool (150,150,255)

### 10. Code
```python
import machine, neopixel
pot = machine.ADC(26)
np = neopixel.NeoPixel(machine.Pin(16), 8)

while True:
    val = pot.read_u16() / 65535
    r = int(255 - val*105)
    g = int(100 + val*150) 
    b = int(val*255)
    for i in range(8):
        np[i] = (r, g, b)
    np.write()
    time.sleep(0.1)
```

---

✅ **Batch 46 Complete**: Night Light projects (0451-0460) - 10 projects generated
