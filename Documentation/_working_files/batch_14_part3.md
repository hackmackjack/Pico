
## Project 0137: Temperature Alarm Alarm System

### 1. Learning Objective
Learn how to detect rapid environmental changes (Rate-of-Change). Understand how to track data over time and trigger emergency protocols if safety thresholds are violated.

### 2. Concepts Introduced
*   **Time-Series Comparison**: Comparing the current value to the value from exactly one second ago.
*   **Emergency Logic**: Immediate activation of multiple alarms (Audio/Visual) for safety.
*   **Buffer Tracking**: Storing previous values to calculate gradients/slopes.

### 3. Hardware Required
*   Raspberry Pi Pico
*   External Temp Sensor (DHT11 recommended for faster response)
*   Buzzer
*   Red LED
*   1x 220-330 Ohm resistor
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **DHT11 Data** | GP16 | Digital signal pin |
| **Buzzer (+)** | GP15 | Connect other side to GND |
| **Red LED** | GP14 | Through resistor |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_dht_read`** (read DHT sensor)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (if/then)
*   **from Math, drag `math_arithmetic`** (subtraction, comparison)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)
*   **from Time, drag `pico_wait`** (wait)

### 6. Variables
*   **last_temp**: Temperature from the previous cycle.
*   **current_temp**: Current live reading.
*   **increase**: The change in temperature (current - last).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Pins**:
    *   **Set** GP15 (Buzzer) and GP14 (LED) as OUTPUT -> LOW.
2.  **Initialize Buffer**:
    *   From **Variables**, **Set** `last_temp` = `pico_dht_read` (temp).

**B. Detection Phase**
3.  **Start Main Loop**:
    *   From **Loops**, drag `pico_forever`.
4.  **Sample Current Environment**:
    *   **Set** `current_temp` = `pico_dht_read` (temp).
5.  **Calculate Gradient**:
    *   From **Variables**, **Set** `increase` = (`current_temp` - `last_temp`).

**C. Emergency Phase**
6.  **Check for Rapid Rise**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `increase` >= 2.0.
    *   **Inside**:
        *   From **Text**, **Print** "FIRE ALARM DETECTED!".
        *   From **Smart IO**, **Set** GP15 (Buzzer) -> HIGH.
        *   From **Smart IO**, **Set** GP14 (LED) -> HIGH.
        *   From **Time**, **Wait** 1 second.
        *   **Set** GP15 -> LOW.

**D. Update Phase**
7.  **Shift Data**:
    *   From **Variables**, **Set** `last_temp` = `current_temp` (the current reading becomes the 'last reading' for the next loop).
8.  **Stabilize Sampling**:
    *   **Wait** 1 second.

### 8. Execution Flow
1.  **Loop**: The Pico checks the temp every second.
2.  **Compare**: It checks how much the temp rose since exactly 1 second ago.
3.  **Threshold**: If the room warms up by 2 degrees in just one second, fire is assumed.
4.  **Alarm**: The buzzer sounds and the Red LED glows to alert neighbors.
5.  **Reset**: After 1 second of alarm, it resets to check for further increases.

### 9. Generated Code
```python
import machine
import utime
import dht

# Hardware setup
sensor = dht.DHT11(machine.Pin(16))
buzzer = machine.Pin(15, machine.Pin.OUT)
led_red = machine.Pin(14, machine.Pin.OUT)

# Initialize buffer
sensor.measure()
last_temp = sensor.temperature()

while True:
    try:
        sensor.measure()
        current_temp = sensor.temperature()
        
        # Calculate rate of change
        increase = current_temp - last_temp
        
        if increase >= 2.0:
            print("FIRE ALARM DETECTED! Delta: " + str(increase))
            led_red.value(1)
            buzzer.value(1)
            utime.sleep(1)
            buzzer.value(0)
        else:
            led_red.value(0)
            
        # Update last_temp
        last_temp = current_temp
        
    except OSError:
        print("Sensor error")
        
    utime.sleep(1)
```

### 10. Common Mistakes
*   **Threshold Too Small**: Small fluctuations (0.1C) happen naturally; don't set the alarm to 0.1 or it will go off randomly.
*   **Sensor Response Time**: Internal Pico sensors are slow to change. A DHT11 or direct flame/heat source is needed to test a true 'rate' alarm.

### 11. Try This Next
*   **Latching Alarm**: Make the alarm stay ON until a "Secret Code" button is pressed.
*   **Data Array**: Track the last 5 readings instead of 2 for more accurate smoothing.

---

## Project 0138: The Temperature Alarm Game

### 1. Learning Objective
Learn how to implement a "Bust" logic game. Understand how to use precision sensor feedback to create a human-computer interaction challenge.

### 2. Concepts Introduced
*   **Target Logic**: Checking for proximity to a specific goal (30.0C).
*   **Game State Management**: Handling "Playing", "Winner", and "Bust" (Failure) states.
*   **Console UI**: Using the print console to guide the player's physical actions.

### 3. Hardware Required
*   Raspberry Pi Pico
*   External Temp Sensor (TMP36 or DHT11)
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sensor VCC** | 3.3V | Power |
| **Sensor OUT** | GP26 (ADC0) | Analog signal |
| **Sensor GND** | GND | Ground |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_analog_read`** (raw sensor input)
*   **from Math, drag `math_arithmetic`** (conversion and comparison)
*   **from Logic, drag `controls_if`** (nested IF blocks)
*   **from Text, drag `text_print`** (game dialogue)

### 6. Variables
*   **temp**: Live reading from player's touch.
*   **bust**: Boolean flag to stop the game if they go over.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Starting State**:
    *   From **Variables**, **Set** `bust` = False.
    *   From **Text**, **Print** "GAME START: Warm the sensor to EXACTLY 30.0C".

**B. Monitoring Phase**
2.  **Create Game Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Read and Convert**:
    *   Read GP26 and convert to Celsius. **Set** value to `temp`.

**C. Game Logic Phase**
4.  **Check Status**:
    *   From **Logic**, drag a nested IF structure (`controls_if`).
5.  **Bust Case (Over 30.0)**:
    *   If `temp` > 30.5 (allow small margin):
        *   **Print** "BUST! You went too far: ", `temp`.
        *   **Set** `bust` = True.
6.  **Win Case (Exactly 30.0)**:
    *   Else If `temp` >= 29.8 AND `temp` <= 30.2:
        *   **Print** "WINNER! YOU HIT THE TARGET!".
7.  **Ongoing Case**:
    *   Else (If not bust):
        *   **Print** "Current Temp: ", `temp`, "... Warm it more!".

**D. Timing Phase**
8.  **Refresh Rate**:
    *   **Wait** 0.5 seconds between updates.

### 8. Execution Flow
1.  **Objective**: Player holds the sensor, warming it with body heat.
2.  **Progress**: Console prints the rise (26... 27... 28...).
3.  **Tension**: Player must let go exactly as it hits 30.
4.  **End**: If physics/latency causes it to hit 30.6, the user loses.
5.  **Restart**: Reset the "Bust" flag and cool the sensor to play again.

### 9. Generated Code
```python
import machine
import utime

# Configure Analog Sensor (TMP36)
sensor = machine.ADC(26)

print("GAME START: Warm the sensor to EXACTLY 30.0C")
bust = False

while True:
    # Read and convert voltage to Celsius
    val = sensor.read_u16()
    voltage = (val / 65535) * 3.3
    temp = (voltage - 0.5) * 100
    
    if not bust:
        if temp > 30.5:
            print("BUST! Too hot: " + str(temp))
            bust = True
        elif temp >= 29.8 and temp <= 30.2:
            print("WINNER! Target Hit! " + str(temp))
        else:
            print("Current: " + str(temp) + " - Keep warming...")
            
    utime.sleep(0.5)
```

### 10. Common Mistakes
*   **Calibration**: If the sensor isn't calibrated, it might start at 29C, making the game last 1 second.
*   **Floating point**: Values like 29.9999 are hard for humans to hit. Use a small range (29.8 to 30.2).

### 11. Try This Next
*   **Hard Mode**: Shrink the target range to 29.95 - 30.05.
*   **Cold Mode**: Start with a warm sensor and blow on it to hit 20.0C.

---

## Project 0139: Automated Temperature Alarm

### 1. Learning Objective
Learn how to implement Statistical Tracking. Understand how to compare streaming data to historical maximums and minimums stored in memory.

### 2. Concepts Introduced
*   **Min/Max Tracking**: Using logic to store the highest and lowest values encountered.
*   **Persistence**: Maintaining records as long as the code is running.
*   **Comparison Loops**: "If current > record, update record".

### 3. Hardware Required
*   Raspberry Pi Pico
*   (Internal or External sensor)

### 4. Wiring / Interfaces
*   Uses internal sensor (GP26/ADC4).

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Variables, drag `variables_set`** (set variable to)
*   **from Logic, drag `controls_if`** (sequential if blocks)
*   **from Text, drag `text_print`** (summary output)

### 6. Variables
*   **current**: Current sample.
*   **highest**: Maximum temp seen so far.
*   **lowest**: Minimum temp seen so far.

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Set Initial Records**:
    *   From **Variables**, **Set** `val` = `pico_read_temp`.
    *   **Set** `highest` = `val`.
    *   **Set** `lowest` = `val`.

**B. Monitoring Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Daily Reading**:
    *   **Set** `current` = `pico_read_temp`.

**C. Statistical Update Phase**
4.  **Update Highest**:
    *   From **Logic**, drag `controls_if`.
    *   **Condition**: If `current` > `highest`.
    *   **Inside**: **Set** `highest` = `current`.
5.  **Update Lowest**:
    *   From **Logic**, drag a second `controls_if`.
    *   **Condition**: If `current` < `lowest`.
    *   **Inside**: **Set** `lowest` = `current`.

**D. Output Phase**
6.  **Print Record Report**:
    *   From **Text**, **Print** "LIVE: ", `current`.
    *   **Print** "MAX: ", `highest`, " | MIN: ", `lowest`.
7.  **Refresh Interval**:
    *   **Wait** 2 seconds.

### 8. Execution Flow
1.  **First Run**: The very first reading is recorded as both the highest and lowest.
2.  **Check**: Every 2 seconds, a new reading is compared.
3.  **Update**: If a new peak or valley is found, the variables `highest` or `lowest` are overwritten.
4.  **Result**: The user can see the temperature history (e.g. how high it got at noon and how low at night).

### 9. Generated Code
```python
import machine
import utime

# Internal temp sensor setup
sensor = machine.ADC(4)
c_factor = 3.3 / 65535

def get_temp():
    raw = sensor.read_u16() * c_factor
    return 27 - (raw - 0.706) / 0.001721

# Initial stats
init = get_temp()
highest = init
lowest = init

while True:
    current = get_temp()
    
    # Update max/min
    if current > highest:
        highest = current
    if current < lowest:
        lowest = current
        
    print(f"LIVE: {current:.2f} C | MAX: {highest:.2f} | MIN: {lowest:.2f}")
    utime.sleep(2)
```

### 10. Common Mistakes
*   **Initial Zero**: If you initialize `lowest` to 0, and your room is 25C, `lowest` will never update. Always initialize to the first reading.
*   **Formatting**: Without decimals, small changes might be missed. Use `.2f` in Python for better precision.

### 11. Try This Next
*   **Reset Records**: Add a button to wipe the max/min records and start over.
*   **LED Peak**: Flash a light every time a new "Record High" is set.

---

## Project 0140: Mastering Temperature Alarm

### 1. Learning Objective
Learn Linear Mapping (Scaling). Understand how to translate a numerical range (Temperature) into a physical display range (Bar of LEDs).

### 2. Concepts Introduced
*   **Mapping**: Converting a value from one range (20-30) to another (0-8).
*   **Clamping**: Preventing values from going outside the valid display range.
*   **Loop-Based LED Control**: Using a loop to turn on a specific number of LEDs.

### 3. Hardware Required
*   Raspberry Pi Pico
*   8 LEDs
*   8x 220-330 Ohm resistors
*   Breadboard and jumper wires

### 4. Wiring / Interfaces
| Component | Pico Pins | Notes |
| :--- | :--- | :--- |
| **LEDs 1-8** | GP2-GP9 | Sequential pins for the bar graph |

### 5. Blocks Used
*   **from Loops, drag `pico_forever`** (forever do)
*   **from Sensors, drag `pico_read_temp`** (read temperature)
*   **from Math, drag `math_map`** (map value from ... to ...)
*   **from Loops, drag `controls_repeat_ext`** (count from 1 to 8)
*   **from Smart IO, drag `pico_gpio_write`** (set Pin to ...)

### 6. Variables
*   **t**: Celsius reading.
*   **bar_height**: Calculated number of LEDs to turn on (0 to 8).

### 7. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure LED Pins**:
    *   **Set** GP2 through GP9 as OUTPUT -> LOW.

**B. Monitoring Phase**
2.  **Create Forever Loop**:
    *   From **Loops**, drag `pico_forever`.
3.  **Read Temp**:
    *   **Set** `t` = `pico_read_temp`.

**C. Scaling Phase**
4.  **Map Temp to LEDs**:
    *   From **Math**, drag `math_map`.
    *   **Set** value = `t`.
    *   **Set** Input Range = [20.0 to 30.0].
    *   **Set** Output Range = [0 to 8].
    *   **Set** variable `bar_height` to this result.
5.  **Apply Logic Clamp**:
    *   Ensure if `t` < 20, `bar_height` = 0.
    *   Ensure if `t` > 30, `bar_height` = 8.

**D. Display Phase**
6.  **Refresh LED Bar**:
    *   From **Loops**, drag `controls_for` (count with i from 0 to 7).
    *   **Inside Loop**:
        *   From **Logic**, drag `controls_if` with **else**.
        *   If `i` < `bar_height`:
            *   **Set** Pin (2 + i) -> HIGH.
        *   Else:
            *   **Set** Pin (2 + i) -> LOW.

**E. Timing Phase**
7.  **Delay**:
    *   **Wait** 0.2 seconds for a responsive meter.

### 8. Execution Flow
1.  **Sample**: Program gets temperature.
2.  **Calculate**: It determines how many LEDs should be on (e.g. 25C = halfway = 4 LEDs).
3.  **Drive**: It loops through all 8 pins and turns on only the ones up to the `bar_height`.
4.  **Visual**: The bar graph grows as it gets hotter and shrinks as it cools.

### 9. Generated Code
```python
import machine
import utime

# Configure 8 LEDs
led_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(2, 10)]
sensor = machine.ADC(4)
conv = 3.3 / 65535

while True:
    # Read Temp
    reading = sensor.read_u16() * conv
    temp = 27 - (reading - 0.706) / 0.001721
    
    # Map 20C-30C to 0-8 LEDs
    # (temp - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    height = int((temp - 20) * (8 - 0) / (30 - 20) + 0)
    
    # Clamp
    if height < 0: height = 0
    if height > 8: height = 8
    
    # Update Bar
    for i in range(8):
        if i < height:
            led_pins[i].value(1)
        else:
            led_pins[i].value(0)
            
    print(f"Temp: {temp:.1f}C | Bar Height: {height}")
    utime.sleep(0.2)
```

### 10. Common Mistakes
*   **Float to Int**: The LED loop needs an integer (whole number) for the height. Don't forget to 'int' your mapping result.
*   **Off-by-one**: Ensure your LED array and loop ranges (0 to 7 vs 1 to 8) match properly.

### 11. Try This Next
*   **Different Range**: Change the code to map 15C to 25C if your room is cooler.
*   **Color Bar**: If using different colored LEDs, make the 'Red' ones at the top flash when the bar is full.

---
