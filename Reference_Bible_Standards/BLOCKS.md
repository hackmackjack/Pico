# 📚 Pico Blockly Reference Guide

Welcome to the **Pico 500** block reference! This guide covers every block in the V5.0 Ultimate edition, organized exactly as they appear in your Toolbox.

---

## 🧩 **Logic**
*Decision making blocks.*

*   **If / Else:** `if [Condition] do [Action]`
    *   *What it does:* Checks a condition. If true, runs the code inside.
    *   *🐍 Code:* `if condition: ...`
*   **Comparison:** `[A] [= / < / >] [B]`
    *   *What it does:* Compares two values.

| Option | Python Code |
| :--- | :--- |
| **=** | `a == b` |
| **≠** | `a != b` |
| **<** | `a < b` |
| **≤** | `a <= b` |
| **>** | `a > b` |
| **≥** | `a >= b` |

*   **Operation:** `[A] [AND / OR] [B]`
    *   *What it does:* Combines logic checks.

| Option | Python Code |
| :--- | :--- |
| **AND** | `a and b` |
| **OR** | `a or b` |
*   **Boolean:** `True` / `False`
    *   *What it does:* Represents logic states.
    *   *🐍 Code:* `True`

---

## 🔄 **Loops**
*Repeating actions.*

*   **Repeat:** `repeat [10] times`
    *   *What it does:* Runs code a specific number of times.
    *   *🐍 Code:* `for count in range(10):`
*   **While:** `while [Condition]`
    *   *What it does:* Runs code as long as the condition is true.
    *   *🐍 Code:* `while condition:`

---

## ➕ **Math**
*Calculations and numbers.*

*   **Number:** `[0]`
    *   *What it does:* A plain number.
    *   *🐍 Code:* `0`
*   **Arithmetic:** `[A] [+ / - / * / /] [B]`
    *   *What it does:* Basic math operations.
    *   *🐍 Code:* `a + b`
*   **Random:** `random integer from [1] to [100]`
    *   *What it does:* Generates a random number.
    *   *🐍 Code:* `random.randint(1, 100)`
*   **List Stats:** `List Stats [Average] Data [List]`
    *   *What it does:* Calculates Average, Max, Min, or Variance of a list.
    *   *🐍 Code:* `stats(list, 'AVG')`

---

## 📝 **Text**
*Words and messages.*

*   **String:** `["Hello"]`
    *   *What it does:* A piece of text.
    *   *🐍 Code:* `"Hello"`
*   **Print:** `print [Text]`
    *   *What it does:* Prints text to the console.
    *   *🐍 Code:* `print("Text")`

---

## 📦 **Variables**
*   **Create Variable:** Use the button to create named placeholders for your data (e.g., `score`, `temp`).
*   **Set:** `set [item] to [0]`
*   **Change:** `change [item] by [1]`

---

## 📋 **Lists**
*storing multiple items.*

*   **Create Empty:** `create empty list`
    *   *🐍 Code:* `[]`
*   **Create With:** `create list with [item] [item]`
    *   *🐍 Code:* `[item1, item2]`
*   **Length:** `length of [list]`
    *   *🐍 Code:* `len(list)`
*   **Is Empty:** `is list [list] empty?`
    *   *🐍 Code:* `not len(list)`
*   **Find:** `in list [list] find first occurrence of [item]`
    *   *🐍 Code:* `list.index(item)`
*   **Get:** `in list [list] get # [1]`
    *   *🐍 Code:* `list[0]`
*   **Set:** `in list [list] set # [1] as [item]`
    *   *🐍 Code:* `list[0] = item`

---

## 🗂️ **Data**
*Key-Value Pairs (Dictionaries).*

*   **Create Dictionary:** `Create Dictionary (Empty)`
    *   *What it does:* Creates a new empty Key-Value structure.
    *   *🐍 Code:* `{}`
*   **Get Value:** `In Dict [d] Get Key [k]`
    *   *What it does:* Retrieves the value saved under the name `k`.
    *   *🐍 Code:* `d.get(k)`
*   **Set Value:** `In Dict [d] Set Key [k] to [v]`
    *   *What it does:* Saves value `v` under the name `k`.
    *   *🐍 Code:* `d[k] = v`

---

## 🛠️ **Smart IO**
*Timing, Logging, and Pins.*

*   **Try / Except:** `Try { ... } On Error { ... }`
    *   *What it does:* Prevents crashes. If "Try" fails, "On Error" runs.
    *   *🐍 Code:* `try: ... except: ...`
*   **Run Delay:** `Run After [1] s (Non-Blocking) { ... }`
    *   *What it does:* Runs code later without pausing the program.
    *   *🐍 Code:* `Timer().init(mode=ONE_SHOT, ...)`
*   **Wait:** `wait [1] [seconds]`
    *   *What it does:* Pauses the program.
    *   *🐍 Code:* `time.sleep(1)`
*   **Stopwatch Ctrl:** `Stopwatch [Start]`
    *   *What it does:* Starts, Stops, or Resets the timer.
    *   *🐍 Code:* `stopwatch.start()`
*   **Stopwatch Get:** `Stopwatch Seconds`
    *   *What it does:* Returns elapsed time.
    *   *🐍 Code:* `stopwatch.time()`
*   **Log:** `log/print [Msg]`
    *   *What it does:* Prints to Serial.
    *   *🐍 Code:* `print(msg)`
*   **GPIO Write:** `set Pin [25] to [HIGH]`
    *   *What it does:* Turns a pin On (1) or Off (0).

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **HIGH (1)** | Turns the pin ON (3.3V). | `Pin(25, Pin.OUT).value(1)` |
| **LOW (0)** | Turns the pin OFF (0V). | `Pin(25, Pin.OUT).value(0)` |
| **TOGGLE** | Flips the state (On->Off, Off->On). | `Pin(25, Pin.OUT).toggle()` |

*   **GPIO Read:** `read [Digital] Pin [0]`
    *   *What it does:* Reads pin state (0/1) or voltage.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Digital (0/1)** | Checks if pin is High (1) or Low (0). | `Pin(0, Pin.IN).value()` |
| **Analog (u16)** | Reads voltage as number (0-65535). | `ADC(0).read_u16()` |
| **Voltage (0-3.3V)** | Reads voltage in Volts (float). | `adc * 3.3 / 65535` |

*   **PWM:** `PWM Pin [0] [Set Duty %] [50]`
    *   *What it does:* Sets LED brightness or Tone freq.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Set Freq (Hz)** | Sets how fast the pulse repeats. | `pwm.freq(int(val))` |
| **Set Duty (u16)** | Sets brightness bits (0-65535). | `pwm.duty_u16(int(val))` |
| **Set Duty (%)** | Sets brightness percentage (0-100). | `pwm.duty_u16(int(val/100*65535))` |
*   **Smooth:** `Smooth/Average [Val] Samples [10]`
    *   *What it does:* Averages the last 10 readings.
    *   *🐍 Code:* `moving_average(cache, val, 10)`
*   **Median:** `Median Filter [Val]`
    *   *What it does:* Removes noise spikes.
    *   *🐍 Code:* `median_filter(cache, val)`

---

## 🌍 **Smart Sensors**
*Environment and Inputs.*

*   **Button Debounce:** `Button (Debounced) Pin [15]`
    *   *What it does:* Checks button press safely (ignores noise).
    *   *🐍 Code:* `debounce(15)`
*   **Sensor Read:** `read sensor [DHT11 Temp] on Pin [15]`
    *   *What it does:* Reads data from various environment and input sensors.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **DHT11 Temp** | Temperature (C) from DHT11 sensor. | `read_DHT11(15, 't')` |
| **DHT11 Hum** | Humidity (%) from DHT11 sensor. | `read_DHT11(15, 'h')` |
| **DHT22 Temp** | Temperature (C) from DHT22 sensor. | `read_DHT22(15, 't')` |
| **DHT22 Hum** | Humidity (%) from DHT22 sensor. | `read_DHT22(15, 'h')` |
| **DS18B20 Temp** | Waterproof temperature sensor. | `ds18x20.read_temp()` |
| **Gas Sensor** | Analog gas/smoke level. | `ADC(15).read_u16()` |
| **Flame (Analog)** | Fire proximity. | `ADC(15).read_u16()` |
| **Flame (Digital)** | Fire detected (True/False). | `Pin(15, Pin.IN).value()` |
| **Sound (Analog)** | Loudness envelope. | `ADC(15).read_u16()` |
| **Sound (Digital)** | Sound trigger/clap. | `Pin(15, Pin.IN).value()` |
| **Light (LDR)** | Brightness level. | `ADC(15).read_u16()` |
| **Thermistor** | Temperature (NTC) analog value. | `ADC(15).read_u16()` |
| **Soil Moisture** | Soil wetness level. | `ADC(15).read_u16()` |
| **Rain Level** | Water drop intensity. | `ADC(15).read_u16()` |
| **Water Level** | Depth level. | `ADC(15).read_u16()` |
| **Potentiometer** | Knob position. | `ADC(15).read_u16()` |
| **Joystick** | X or Y axis position. | `ADC(15).read_u16()` |
| **Flex/Bend** | Bending sensor value. | `ADC(15).read_u16()` |
| **Force (FSR)** | Pressure level. | `ADC(15).read_u16()` |
| **Vibration** | Shake detected. | `Pin(15, Pin.IN).value()` |
| **Tilt Switch** | Tilt detected. | `Pin(15, Pin.IN).value()` |
| **Reed Switch** | Door magnet detected (PullUp). | `Pin(15, Pin.IN, Pin.PULL_UP).value()` |
| **Touch Sensor** | Finger touch detected. | `Pin(15, Pin.IN).value()` |
| **Button (PullUp)** | Button press (0=Pressed). | `Pin(15, Pin.IN, Pin.PULL_UP).value()` |
| **Limit Switch** | Mechanical hit detected. | `Pin(15, Pin.IN, Pin.PULL_UP).value()` |
| **Beam Break** | Light beam broken. | `Pin(15, Pin.IN).value()` |
| **PIR Motion** | Body heat movement. | `Pin(15, Pin.IN).value()` |
| **IR Obstacle** | Object reflected nearby. | `Pin(15, Pin.IN).value()` |
| **Line Follower** | Black/White line detected. | `Pin(15, Pin.IN).value()` |
| **Hall Effect** | Magnet detected. | `Pin(15, Pin.IN).value()` |
*   **Peak Detector:** `Peak Detector [Max] Value [V] ID [0] ...`
    *   *What it does:* Remembers the highest/lowest value.

| Option | Description |
| :--- | :--- |
| **Max** | Tracks the highest value seen. |
| **Min** | Tracks the lowest value seen. |
*   **Color Match:** `Is Color [Red] ? R [r] G [g] B [b]`
    *   *What it does:* Checks if RGB matches a color.
    *   *🐍 Code:* `(r > g*1.5 ...)`
*   **I2C Sensor:** `read I2C [MPU6050] [Accel X] ...`
    *   *What it does:* Reads advanced I2C chips.
    *   *🐍 Code:* `mpu.vals()[0]`
*   **IMU Angle:** `IMU Angle [Pitch] SDA [0] SCL [1]`
    *   *What it does:* Calculates tilt angle using Sensor Fusion.
    *   *🐍 Code:* `mpu.get_angles()[0]`
*   **RTC Init:** `Setup RTC (DS3231) ...`
    *   *What it does:* Starts the Real Time Clock.
    *   *🐍 Code:* `rtc = DS3231(...)`
*   **RTC Get:** `Get RTC Time`
    *   *What it does:* Returns "HH:MM:SS".
    *   *🐍 Code:* `rtc.get()`
*   **RTC Set:** `Set RTC Time ...`
    *   *What it does:* Updates the clock.
    *   *🐍 Code:* `rtc.set(...)`
*   **Distance:** `Ultrasonic dist (cm) Trig [14] Echo [15]`
    *   *What it does:* Measures distance.
    *   *🐍 Code:* `hcsr04.dist_cm()`
*   **Rotary Read:** `Read Rotary (Delta) ...`
    *   *What it does:* Reads knob turns (+1/-1).
    *   *🐍 Code:* `rotary.read()`
*   **Rotary Button:** `Rotary Button Clicked?`
    *   *What it does:* Checks knob click.
    *   *🐍 Code:* `rotary.click()`
*   **IR Read:** `IR Remote Read Pin [16]`
    *   *What it does:* Reads IR remote codes.
    *   *🐍 Code:* `ir.read()`
*   **GPS:** `GPS Read [Lat] ...`
    *   *What it does:* Reads Latitude/Longitude.
    *   *🐍 Code:* `gps.read()[0]`
*   **Pulse In:** `Pulse In Pin [0] ...`
    *   *What it does:* Measures pulse length (us).
    *   *🐍 Code:* `time_pulse_us(...)`
*   **Map:** `Map [Val] from [0-100] to [0-255]`
    *   *What it does:* Scales a number.
    *   *🐍 Code:* `(val-0)*(255-0)/(100-0)+0`

---

## 🏎️ **Motion & Motors**
*Movement and Actuators.*

*   **Servo:** `Servo Pin [0] Angle [90]`
    *   *What it does:* Sets servo angle.
    *   *🐍 Code:* `servo.angle(90)`
*   **Servo Smooth:** `Servo Smooth Pin [0] to [180]° over [1000]ms`
    *   *What it does:* Moves servo gradually in the background. Does not stop the program!
    *   *🐍 Code:* `smart_servo.move(180, 1000)`
*   **Servo Sweep:** `Servo Sweep ...`
    *   *What it does:* Wags servo back and forth (Blocking).
    *   *🐍 Code:* `for i in range(...): ...`
*   **Servo Playlist:** `Servo Play List ...`
    *   *What it does:* Plays angles from a list.
    *   *🐍 Code:* `for a in list: servo.angle(a)`
*   **PWM Fade:** `PWM Fade ...`
    *   *What it does:* Fades LED brightness.
    *   *🐍 Code:* `for i in range(...): pwm.duty(...)`
*   **Motor:** `DC Motor ... Speed [100]%`
    *   *What it does:* Controls DC motor.

| Option | Description |
| :--- | :--- |
| **Forward** | Spins motor forward. |
| **Backward** | Spins motor backward. |
| **Stop** | Stops the motor. |
*   **Drive Dist:** `Drive Motor ... Dist [10] cm`
    *   *What it does:* Moves specific distance.
    *   *🐍 Code:* `while e.read() < target: ...`
*   **Stepper:** `Stepper ... Steps [100]`
    *   *What it does:* Moves stepper motor.
    *   *🐍 Code:* `stepper.step(100)`
*   **Stepper Ramp:** `Stepper Ramp ...`
    *   *What it does:* Smooth stepper move.
    *   *🐍 Code:* `stepper.ramp(...)`
*   **Encoder Init:** `Setup Encoder ID [0] ...`
    *   *What it does:* Starts encoder.
    *   *🐍 Code:* `e = Encoder(...)`
*   **Encoder Read:** `Read Encoder ID [0]`
    *   *What it does:* Gets count.
    *   *🐍 Code:* `e.read()`
*   **Encoder Reset:** `Reset Encoder ID [0]`
    *   *What it does:* Zeroes count.
    *   *🐍 Code:* `e.reset()`
*   **Music:** `Music/Tone Pin [0] ...`
    *   *What it does:* Beeps.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Play Tone (Hz)** | Plays a frequency. | `pwm.freq(val); pwm.duty_u16(32768)` |
| **Stop** | Stops the sound. | `pwm.duty_u16(0)` |
*   **Melody:** `Play Melody ... Notes [C4 D4]`
    *   *What it does:* Plays a song.
    *   *🐍 Code:* `melody.play("C4 D4", 120)`
*   **Synth Play:** `Play Tone [440] Hz Duration [500] ms ...`
    *   *What it does:* Plays a smooth synth tone.
    *   *🐍 Code:* `synth.play(440, 500)`

---

## 🖥️ **Smart Display**
*Visuals.*

*   **Init:** `Init OLED ...`
    *   *What it does:* Starts Screen.
    *   *🐍 Code:* `oled = SSD1306(...)`
*   **Op:** `OLED [Show/Clear/Fill]`
    *   *What it does:* Controls the display buffer.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Show** | Pushes buffer to screen. | `oled.show()` |
| **Clear** | Clears buffer (Black). | `oled.fill(0)` |
| **Fill** | Fills buffer (White). | `oled.fill(1)` |
*   **Text:** `OLED Print [Text] ...`
    *   *What it does:* Draws text.
    *   *🐍 Code:* `oled.text(...)`
*   **Draw:** `OLED Draw [Pixel/Line/Rect] ...`
    *   *What it does:* Draws shapes.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Pixel** | Draws a dot at X,Y. | `oled.pixel(x,y,c)` |
| **Line** | Draws line from X,Y to V1,V2. | `oled.line(x,y,v1,v2,c)` |
| **Rect** | Draws rectangle at X,Y with W,H. | `oled.rect(x,y,w,h,c)` |

*   **Icon:** `OLED Draw Icon [Heart] ...`
    *   *What it does:* Draws icon.

| Option | Code |
| :--- | :--- |
| **Heart, Smile, Sad, Arrow, Check, X** | `draw_icon(oled, 'NAME', x, y)` |
*   **Graph:** `OLED Graph Val [x] ...`
    *   *What it does:* Draws scrolling chart.
    *   *🐍 Code:* `graph.draw(x)`
*   **Progress:** `OLED Progress ... Val [50] %`
    *   *What it does:* Draws bar.
    *   *🐍 Code:* `oled.fill_rect(...)`
*   **Menu:** `Show Menu Options [List]`
    *   *What it does:* Interactive Menu.
    *   *🐍 Code:* `menu.select()`
*   **NeoPixel:** `NeoPixel ... Set # [0] ...`
    *   *What it does:* Sets LED color.
    *   *🐍 Code:* `np[0] = (r,g,b)`
*   **NP Show:** `NeoPixel Show`
    *   *What it does:* Updates strip.
    *   *🐍 Code:* `np.write()`
*   **NP Bright:** `NeoPixel Brightness [0.5]`
    *   *What it does:* Dims LEDs.
    *   *🐍 Code:* `np[i] = ...`
*   **NP Effect:** `NeoPixel Effect [Rainbow]`
    *   *What it does:* Plays animation.
    *   *🐍 Code:* `for i in range(255): ...`
*   **LCD Init:** `Init LCD ...`
    *   *What it does:* Starts LCD.
    *   *🐍 Code:* `lcd = I2cLcd(...)`
*   **LCD Print:** `LCD Print [Text] ...`
    *   *What it does:* Prints to LCD.
    *   *🐍 Code:* `lcd.put(...)`

---

## 🌐 **Network & IoT**
*WiFi and Cloud.*

*   **WiFi:** `WiFi Connect ...`
    *   *What it does:* Connects to internet.
    *   *🐍 Code:* `wlan.connect(...)`
*   **WiFi Scan:** `WiFi Scan ...`
    *   *What it does:* Lists networks.
    *   *🐍 Code:* `wlan.scan()`
*   **WiFi Status:** `WiFi Status`
    *   *What it does:* Checks IP/Signal.
    *   *🐍 Code:* `wlan.ifconfig()`
*   **WiFi Disconnect:** `WiFi Disconnect`
    *   *What it does:* Stops WiFi.
    *   *🐍 Code:* `wlan.disconnect()`
*   **NTP Sync:** `NTP Time Sync`
    *   *What it does:* Sets internet time.
    *   *🐍 Code:* `ntptime.settime()`
*   **Get Time:** `Get Current Time`
    *   *What it does:* Returns time string.
    *   *🐍 Code:* `time.localtime()`
*   **HTTP:** `HTTP [GET] ...`
    *   *What it does:* Sends HTTP requests.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **GET** | Gets raw text. | `urequests.get(url).text` |
| **POST (JSON)** | Sends JSON data. | `urequests.post(url, json=data).text` |
| **GET JSON** | Gets and decodes JSON. | `urequests.get(url).json()` |
| **POST JSON** | Sends and decodes JSON. | `urequests.post(url, json=data).json()` |
*   **Web Server:** `Start Web Server ...`
    *   *What it does:* Simple page.
    *   *🐍 Code:* `socket.accept()`
*   **Webhook:** `Trigger Webhook ...`
    *   *What it does:* Sends alert.
    *   *🐍 Code:* `urequests.post(...)`
*   **Download:** `Download File ...`
    *   *What it does:* Saves web file.
    *   *🐍 Code:* `f.write(req.text)`
*   **MQTT Setup:** `MQTT Setup ...`
    *   *What it does:* Connects Broker.
    *   *🐍 Code:* `mqtt = SmartMQTT(...)`
*   **MQTT Check:** `MQTT Check Messages`
    *   *What it does:* Receives data.
    *   *🐍 Code:* `mqtt.check()`
*   **MQTT:** `MQTT [Publish] ...`
    *   *What it does:* MQTT Messaging.

| Option | Description | Python Code Pattern |
| :--- | :--- | :--- |
| **Publish** | Sends a message to a topic. | `mqtt.pub(topic, msg)` |
| **Subscribe** | Listens for messages on a topic. | `mqtt.sub(topic)` |
*   **BLE Start:** `BLE Start Name [Robot1]`
    *   *What it does:* Turns the Pico into a Bluetooth device you can connect to with your phone.
    *   *🐍 Code:* `ble = BLE_UART("Robot1")`
*   **BLE Send:** `BLE Send [Msg]`
    *   *What it does:* Sends text to the connected phone.
    *   *🐍 Code:* `ble.send(msg)`
*   **BLE Read:** `BLE Read (String)`
    *   *What it does:* Gets text sent from the phone.
    *   *🐍 Code:* `ble.read()`
*   **Radio Init:** `Radio Init Mode [Host] ...`
    *   *What it does:* Starts Pico-to-Pico WiFi.
    *   *🐍 Code:* `radio = Radio(...)`
*   **Radio Send:** `Radio Send [Msg]`
    *   *What it does:* Broadcasts message.
    *   *🐍 Code:* `radio.send(msg)`
*   **Radio Receive:** `Radio Receive`
    *   *What it does:* Gets last message.
    *   *🐍 Code:* `radio.recv()`

---

## 💽 **System & Storage**
*Files and Power.*

*   **System:** `System [Reset/GC]`
    *   *What it does:* Reboots or cleans RAM.
    *   *🐍 Code:* `machine.reset()`
*   **Power:** `Power [Sleep]`
    *   *What it does:* Saves battery.
    *   *🐍 Code:* `machine.lightsleep()`
*   **Watchdog:** `Watchdog [Start]`
    *   *What it does:* Auto-restart on freeze.
    *   *🐍 Code:* `wdt = WDT(...)`
*   **Thread:** `Run on Core 1 { ... }`
    *   *What it does:* Multitasking.
    *   *🐍 Code:* `_thread.start_new_thread(...)`
*   **File:** `File [Write] ...`
    *   *What it does:* Saves file.
    *   *🐍 Code:* `f.write(...)`
*   **File Read:** `File Read ...`
    *   *What it does:* Reads file.
    *   *🐍 Code:* `f.read()`
*   **File List:** `File List ...`
    *   *What it does:* Lists files.
    *   *🐍 Code:* `os.listdir()`
*   **File Delete:** `File Delete ...`
    *   *What it does:* Deletes file.
    *   *🐍 Code:* `os.remove()`
*   **File Exists:** `File Exists ...`
    *   *What it does:* Checks file.
    *   *🐍 Code:* `os.stat()`
*   **File Space:** `Free Storage ...`
    *   *What it does:* Checks space.
    *   *🐍 Code:* `os.statvfs()`
*   **NVM Set:** `Save Setting Key [K] Value [V]`
    *   *What it does:* Saves data permanently.
    *   *🐍 Code:* `nvm.set(k, v)`
*   **NVM Get:** `Get Setting Key [K] ...`
    *   *What it does:* Loads data.
    *   *🐍 Code:* `nvm.get(k)`
*   **EEPROM Write:** `EEPROM Write ...`
    *   *What it does:* External storage write.
    *   *🐍 Code:* `eeprom.w(...)`
*   **EEPROM Read:** `EEPROM Read ...`
    *   *What it does:* External storage read.
    *   *🐍 Code:* `eeprom.r(...)`
*   **SD Init:** `Init SD Card ...`
    *   *What it does:* Mounts SD.
    *   *🐍 Code:* `os.mount(sd)`
*   **SD Unmount:** `Unmount SD Card`
    *   *What it does:* Ejects SD.
    *   *🐍 Code:* `os.umount()`
*   **Data Log:** `Log to CSV ...`
    *   *What it does:* Appends data.
    *   *🐍 Code:* `f.write(...)`
*   **Log Rotate:** `Log to CSV (Safe) ...`
    *   *What it does:* Logs with rotation.
    *   *🐍 Code:* `os.rename(...)`
*   **Timer:** `Every [1000] ms Do { ... }`
    *   *What it does:* Background timer.
    *   *🐍 Code:* `Timer().init(...)`

---

## 🔗 **Protocols**
*Advanced Communication.*

*   **I2C Scan:** `I2C Scan ...`
    *   *What it does:* Prints connected I2C addresses.
    *   *🐍 Code:* `print(i2c.scan())`
*   **I2C Read Reg:** `I2C Read Reg ...`
    *   *What it does:* Low-level I2C read.
    *   *🐍 Code:* `i2c.readfrom_mem(...)`
*   **I2C Write Reg:** `I2C Write Reg ...`
    *   *What it does:* Low-level I2C write.
    *   *🐍 Code:* `i2c.writeto_mem(...)`
*   **UART Init:** `Init UART ...`
    *   *What it does:* Starts Serial port.
    *   *🐍 Code:* `uart = UART(...)`
*   **UART Write:** `UART Write ...`
    *   *What it does:* Sends text via Serial.
    *   *🐍 Code:* `uart.write(...)`
*   **UART Read:** `UART Read Line`
    *   *What it does:* Reads text from Serial.
    *   *🐍 Code:* `uart.readline()`
*   **RFID:** `RFID (SPI0) Read UID`
    *   *What it does:* Reads tag ID.
    *   *🐍 Code:* `rfid.uid()`
*   **Modbus Init:** `Modbus Setup UART [0] ...`
    *   *What it does:* Starts Modbus Master.
    *   *🐍 Code:* `modbus = Modbus(uart)`
*   **Modbus Read:** `Modbus Read Addr [1] Reg [0]`
    *   *What it does:* Reads register.
    *   *🐍 Code:* `modbus.rw(1, 3, 0)`
*   **Modbus Write:** `Modbus Write Addr [1] Reg [0] Val [100]`
    *   *What it does:* Writes register.
    *   *🐍 Code:* `modbus.rw(1, 6, 0, 100)`

---

## 🧠 **Artificial Intelligence**
*Machine Learning.*

*   **AI Init:** `AI Init (KNN) Neighbors [3]`
    *   *What it does:* Starts AI.
    *   *🐍 Code:* `knn = KNN(3)`
*   **AI Add:** `AI Train Label [A] Data [List]`
    *   *What it does:* Teaches the AI.
    *   *🐍 Code:* `knn.add(list, "A")`
*   **AI Predict:** `AI Predict Class Data [List]`
    *   *What it does:* Guesses the class.
    *   *🐍 Code:* `knn.predict(list)`
*   **Get Gesture:** `Get Gesture Data (Accel)`
    *   *What it does:* Captures motion data.
    *   *🐍 Code:* `[ax, ay, az]`
*   **Get Color:** `Get Color Data (RGB)`
    *   *What it does:* Captures color data.
    *   *🐍 Code:* `[r, g, b]`

---

## 🎮 **Game**
*Sprite Engine.*

*   **Create Sprite:** `Create Sprite ID [0] ...`
    *   *What it does:* Spawns a character.
    *   *🐍 Code:* `s = Sprite(...)`
*   **Move:** `Update Sprite ID [0] (Move)`
    *   *What it does:* Applies speed to position.
    *   *🐍 Code:* `s.move()`
*   **Set Vel:** `Set Velocity ID [0] DX [1] DY [0]`
    *   *What it does:* Sets speed.
    *   *🐍 Code:* `s.set_vel(1, 0)`
*   **Bounce:** `Bounce Sprite ID [0]`
    *   *What it does:* Bounces off walls.
    *   *🐍 Code:* `s.bounce()`
*   **Check Col:** `Sprite [0] Touching [1] ?`
    *   *What it does:* Checks collision.
    *   *🐍 Code:* `s.touch(s2)`
*   **Draw:** `Draw Sprite ID [0]`
    *   *What it does:* Shows sprite on OLED.
    *   *🐍 Code:* `s.draw(oled)`

---

## 🚀 **Ultimate Pack**
*Advanced Control.*

*   **PID:** `PID Compute ...`
    *   *What it does:* Smooth control loop.
    *   *🐍 Code:* `pid.compute(...)`
*   **Keypad:** `Keypad 4x4 Read ...`
    *   *What it does:* Scans keypad.
    *   *🐍 Code:* `keypad.scan()`
