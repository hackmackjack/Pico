# Missing Blocks Report

### Summary
*   **Total Blocks Analyzed:** 293
*   **Implemented Blocks:** 151
*   **Unmatched Items:** 264

> **Note:** The majority of "missing" items are specific parameter strings in the documentation (e.g., `sleep [4] seconds` vs `sleep [1] seconds`) which are covered by a single implemented block (`pico_wait`). There are no critical missing functionalities.

### Unmatched Items List

| Block Name / Description | Projects Occurring In | Count |
|---|---|---|
| `if [Button Pressed] then` | 0017, 0019, 0020 | 3 |
| `print` | 0181, 0187, 0188 | 3 |
| `wait until [not Button Pressed]` | 0006, 0026 | 2 |
| `wait until [Button Pressed]` | 0014, 0048 | 2 |
| `set Pin [14] to [High]` | 0035, 0036 | 2 |
| `for [i] from [0] to [65535] by [1000]` | 0040, 0052 | 2 |
| `set Pin [25] to [LOW]` | 0001 | 1 |
| `set Pin [15] to [lightsOn]` | 0006 | 1 |
| `random number from [2] to [5]` | 0008 | 1 |
| `[Value] < [Threshold]` | 0009 | 1 |
| `[lightLevel] < [30000]` | 0009 | 1 |
| `for i from 0 to 4` | 0010 | 1 |
| `for [i] from [0] to [4]` | 0010 | 1 |
| `for [i] from [3] to [1]` | 0010 | 1 |
| `if [Read Pin 14] then` | 0011 | 1 |
| `print [Click!]` | 0011 | 1 |
| `if [Button] then... else...` | 0012 | 1 |
| `if [Button Pressed] then... else...` | 0012 | 1 |
| `if [Button] then [Safe] else [Alarm]` | 0013 | 1 |
| `if [condition] then... else...` | 0013 | 1 |
| `set Pin [16] to [LOW]` | 0013 | 1 |
| `if [not] [Button Pressed]` | 0013 | 1 |
| `set Pin [16] to [HIGH]` | 0013 | 1 |
| `create text "Cats:" + [cats]` | 0015 | 1 |
| `change [cats] by [1]` | 0015 | 1 |
| `print [create text "Cats:" + [cats]]` | 0015 | 1 |
| `print [create text "Dogs:" + [dogs]]` | 0015 | 1 |
| `get time (ms)` | 0017 | 1 |
| `if [time (ms) - start] > [3000]` | 0017 | 1 |
| `sleep [0.1]s` | 0017 | 1 |
| `pico_gpio_write or pico_gpio_read` | 0018 | 1 |
| `sleep [random 2 to 5] seconds` | 0018 | 1 |
| `sleep [4] seconds` | 0018 | 1 |
| `if [timeLeft] > [0] then` | 0019 | 1 |
| `sleep [0.05] s` | 0020 | 1 |
| `if [Button Still Pressed] then` | 0020 | 1 |
| `print [create text "Click " + [count]]` | 0020 | 1 |
| `if [Button] then [Buzz] else [Silence]` | 0023 | 1 |
| `if [BtnA] play [C4]...` | 0025 | 1 |
| `isMuted` | 0026 | 1 |
| `if [not muted] then` | 0026 | 1 |
| `delayTime` | 0027 | 1 |
| `list [262, 330, 392]` | 0028 | 1 |
| `Create list [sequence]` | 0028 | 1 |
| `Create empty list` | 0028 | 1 |
| `call play(262, 0.5)` | 0028 | 1 |
| `call play(330, 0.5)` | 0028 | 1 |
| `call play(392, 0.5)` | 0028 | 1 |
| `map [value] from low [0] high [65535] to low [100] high [2000]` | 0029 | 1 |
| `set [val] to` | 0029 | 1 |
| `set [pitch] to` | 0029 | 1 |
| `map [val] from [0]-[65535] to [100]-[2000]` | 0029 | 1 |
| `Set Pin [14] to [HIGH]` | 0031 | 1 |
| `Set Pin [14] to [LOW]` | 0031 | 1 |
| `sleep [0.5] s` | 0032 | 1 |
| `if [Button] then [Motor ON] else [Motor OFF]` | 0033 | 1 |
| `set [speedLevel] to [0]` | 0034 | 1 |
| `change [speedLevel] by [1]` | 0034 | 1 |
| `if [speedLevel > 3] then` | 0034 | 1 |
| `if [speedLevel = 0] then` | 0034 | 1 |
| `if [speedLevel = 1] then` | 0034 | 1 |
| `if [speedLevel = 2] then` | 0034 | 1 |
| `if [speedLevel = 3] then` | 0034 | 1 |
| `set [isOpening] to [false]` | 0036 | 1 |
| `AND` | 0036 | 1 |
| `NOT` | 0036 | 1 |
| `set [isOpening] to [true]` | 0036 | 1 |
| `if [PIR High]` | 0037 | 1 |
| `random value` | 0038 | 1 |
| `set [spinTime] to` | 0038 | 1 |
| `random from [1.0] to [4.0]` | 0038 | 1 |
| `set [temp] to [0]` | 0039 | 1 |
| `set [temp] to` | 0039 | 1 |
| `if [temp > 25] then` | 0039 | 1 |
| `for i from 0 to 65000` | 0040 | 1 |
| `set Pin [13] to [High]` | 0041 | 1 |
| `call set_lights(1, 0, 0)` | 0043 | 1 |
| `wait until [Button]` | 0045 | 1 |
| `set [light] to [0]` | 0046 | 1 |
| `set [NIGHT_THRESHOLD] to [20000]` | 0046 | 1 |
| `set [light] to` | 0046 | 1 |
| `if [light > NIGHT_THRESHOLD] then` | 0046 | 1 |
| `[Button] AND [isRed]` | 0047 | 1 |
| `set [isRed] to [false]` | 0047 | 1 |
| `if [car sensor pressed] then` | 0047 | 1 |
| `set [isRed] to [true]` | 0047 | 1 |
| `repeat [50] times` | 0047 | 1 |
| `call check_violation()` | 0047 | 1 |
| `set [reactionTime] to [0]` | 0048 | 1 |
| `sleep [random 2-5] seconds` | 0048 | 1 |
| `set [dist] to` | 0049 | 1 |
| `call measure_distance()` | 0049 | 1 |
| `if [dist < 10] then` | 0049 | 1 |
| `setNorth[Green]` | 0050 | 1 |
| `set [brightness] to [0]` | 0052 | 1 |
| `for [i] from [65535] to [0] by [-1000]` | 0052 | 1 |
| `IF Sound Detected:` | 0055 | 1 |
| `Set LED to ` | 0055 | 1 |
| `set Pin [15] to [High]` | 0061 | 1 |
| `else if [Button B value]` | 0063 | 1 |
| `IF Button:` | 0065 | 1 |
| `Check ` | 0069 | 1 |
| `Wait Until Button Pressed` | 0071 | 1 |
| `IF Button Pressed: YOU WIN (Solid On)` | 0072 | 1 |
| `set [sequence] to` | 0078 | 1 |
| `create list with` | 0078 | 1 |
| `Random Integer from [0] to [100]` | 0078 | 1 |
| `set [i] to` | 0078 | 1 |
| `repeat [10] times` | 0078 | 1 |
| `length of` | 0078 | 1 |
| `in list [sequence] get #` | 0078 | 1 |
| `wait [0.5] seconds` | 0078 | 1 |
| `wait [0.2] seconds` | 0078 | 1 |
| `Wait for Button [GP10] Press` | 0078 | 1 |
| `if [true] do` | 0078 | 1 |
| `[0] ≠ [0]` | 0078 | 1 |
| `wait [1] seconds` | 0078 | 1 |
| `IF Button: ` | 0087 | 1 |
| `IF No Press for 3s: Break` | 0087 | 1 |
| `if [val] < [50000]` | 0089 | 1 |
| `change [big] by [1]` | 0089 | 1 |
| `print ["Big"]` | 0089 | 1 |
| `change [small] by [1]` | 0089 | 1 |
| `print ["Small"]` | 0089 | 1 |
| `create list with items` | 0090 | 1 |
| `count with [num] from [0] to [9]` | 0090 | 1 |
| `get item [num] from [patterns]` | 0090 | 1 |
| `print [text]` | 0090 | 1 |
| `repeat [3] times` | 0091 | 1 |
| `sleep [UNIT] seconds` | 0091 | 1 |
| `sleep [UNIT*2] seconds` | 0091 | 1 |
| `sleep [UNIT*3] seconds` | 0091 | 1 |
| `Print "Dot"` | 0098 | 1 |
| `Check if user tapped short` | 0098 | 1 |
| `Print "Dash"` | 0098 | 1 |
| `Check if user tapped long` | 0098 | 1 |
| `Repeat the "Dash" sequence 3 more times` | 0099 | 1 |
| `sleep [10] seconds` | 0099 | 1 |
| `for each item [char] in list [message]` | 0100 | 1 |
| `for each item [dotdash] in text [code]` | 0100 | 1 |
| `if [dotdash] = [ "." ]` | 0100 | 1 |
| `Wait 0.1s (Gap between parts)` | 0100 | 1 |
| `wait [0.3] seconds` | 0100 | 1 |
| `Print "Breaking News: Pico is Awesome." at X:16 Y:0 (Off screen to the right)` | 0103 | 1 |
| `pico_lcd_scroll_left` | 0103 | 1 |
| `pico_lcd_custom_char` | 0104 | 1 |
| `pico_lcd_show_char` | 0104 | 1 |
| `change [clicks] by [1]` | 0105 | 1 |
| `Repeat ` | 0106 | 1 |
| `if [menu_item] = [1]` | 0107 | 1 |
| `pico_lcd_clear + pico_lcd_print` | 0109 | 1 |
| `print [message]` | 0111 | 1 |
| `Print "Voltage:" at Line 0` | 0113 | 1 |
| `set [r] to read analog [26]` | 0116 | 1 |
| `set [g] to read analog [27]` | 0116 | 1 |
| `set [b] to read analog [28]` | 0116 | 1 |
| `Print "="` | 0117 | 1 |
| `if [vol] > [ 10000 ]` | 0118 | 1 |
| `if [vol] > [ 30000 ]` | 0118 | 1 |
| `if [vol] > [ 50000 ]` | 0118 | 1 |
| `Print [temp_val]` | 0121 | 1 |
| `sleep**:` | 0121 | 1 |
| `create text with` | 0122 | 1 |
| `if [h] > [70]` | 0124 | 1 |
| `else if [h] < [30]` | 0124 | 1 |
| `if [t] > [28]` | 0125 | 1 |
| `Print "Dew Point: " + ` | 0126 | 1 |
| `if [curr_t] > [max_t]` | 0127 | 1 |
| `if [curr_t] < [min_t]` | 0127 | 1 |
| `Print "Max: " + ` | 0127 | 1 |
| `if [t] > [30] AND [h] > [60]` | 0128 | 1 |
| `if Button is Pressed` | 0130 | 1 |
| `if (Time Now - last_read_time) > 2000` | 0130 | 1 |
| `print [light_level]` | 0131 | 1 |
| `if [lux] < [10000]` | 0132 | 1 |
| `if [beam_val] < [50000]` | 0133 | 1 |
| `if [left] > [right + 1000]` | 0135 | 1 |
| `IF (Time Now - ` | 0136 | 1 |
| `print "Swipe Right! ->"` | 0136 | 1 |
| `sleep for LDR < 10000 (Beam Broken by fan blade)` | 0137 | 1 |
| `sleep for LDR > 10000 (Beam Clear)` | 0137 | 1 |
| `IF 1 Second Passed:` | 0137 | 1 |
| `sleep for Light (Signal Start)` | 0139 | 1 |
| `sleep for Dark (Signal End)` | 0139 | 1 |
| `if [pulse_len] < [400]` | 0139 | 1 |
| `Wait 1s (Stabilize)` | 0140 | 1 |
| `Print "Calibrated. Baseline:" + ` | 0140 | 1 |
| `if [current] < [trigger_level]` | 0140 | 1 |
| `count with [angle] from [0] to [180] by [1]` | 0143 | 1 |
| `count with [angle] from [180] to [0] by [-1]` | 0143 | 1 |
| `if Button [15] is pressed` | 0145 | 1 |
| `count with [pos] from [0] to [120] by [2]` | 0148 | 1 |
| `count with [pos] from [120] to [0] by [-2]` | 0148 | 1 |
| `pico_keypad_init` | 0151 | 1 |
| `if [key] != [null]` | 0151 | 1 |
| `print [key]` | 0151 | 1 |
| `if [key] = ["#"]` | 0152 | 1 |
| `print ` | 0153 | 1 |
| `if [key] = ["1"]` | 0154 | 1 |
| `Print "Option " + ` | 0155 | 1 |
| `print Letter` | 0156 | 1 |
| `IF '6' (Right): ` | 0158 | 1 |
| `IF '4' (Left): ` | 0158 | 1 |
| `IF '2' (Up): ` | 0158 | 1 |
| `IF '8' (Down): ` | 0158 | 1 |
| `print "O"` | 0158 | 1 |
| `sleep for Key (Letter A-D). Save to ` | 0159 | 1 |
| `sleep for Key (Number 1-4). Save to ` | 0159 | 1 |
| `Print "Dispensing Cola"` | 0159 | 1 |
| `Print "Dispensing Chips"` | 0159 | 1 |
| `Print "Invalid Slot"` | 0159 | 1 |
| `Set Pin GP2 (Row 1) High. All other Rows Low` | 0160 | 1 |
| `Print [dist]` | 0161 | 1 |
| `if [dist] < [50]` | 0162 | 1 |
| `sleep. 50cm = 0.5s From **Smart IO**, drag ` | 0162 | 1 |
| `Print "Calibrated: " + ` | 0164 | 1 |
| `if [current] < [baseline - 20]` | 0164 | 1 |
| `if [dist] < [15]` | 0165 | 1 |
| `if [dist] < [20]` | 0167 | 1 |
| `Print "STOP"` | 0167 | 1 |
| `Print "Reverse"` | 0167 | 1 |
| `Print "Turn Left"` | 0167 | 1 |
| `Print "Drive Forward"` | 0167 | 1 |
| `sleep for Entry**:` | 0168 | 1 |
| `Wait until [Read Distance] < [50]` | 0168 | 1 |
| `Print "Welcome! Count: " + ` | 0168 | 1 |
| `sleep for Exit**:` | 0168 | 1 |
| `Wait until [Read Distance] > [50]` | 0168 | 1 |
| `Print "Tank Level: " + ` | 0169 | 1 |
| `Repeat 5 times:` | 0170 | 1 |
| `Change Count to ` | 0171 | 1 |
| `count with [i] from [0] to [7] by [1]` | 0172 | 1 |
| `Change the ` | 0172 | 1 |
| `count with [pos] from [0] to [7] by [1]` | 0173 | 1 |
| `count with [brightness] from [0] to [255] by [5]` | 0174 | 1 |
| `count with [brightness] from [255] to [0] by [-5]` | 0174 | 1 |
| `set [r] to` | 0175 | 1 |
| `count with [i] from [0] to [level] by [1]` | 0176 | 1 |
| `count with [i] from [0] to [7]` | 0178 | 1 |
| `if ([number] AND 2^[i]) > 0` | 0178 | 1 |
| `set [flicker] to random (100-255)` | 0179 | 1 |
| `set [x] to` | 0181 | 1 |
| `set [y] to` | 0181 | 1 |
| `join` | 0181 | 1 |
| `if [x] > [33000]` | 0182 | 1 |
| `else if [x] < [32000]` | 0182 | 1 |
| `Print "Cursor at:" + ` | 0183 | 1 |
| `IF Down: ` | 0185 | 1 |
| `65535 - [y]` | 0186 | 1 |
| `Print "Pitch:" + value` | 0186 | 1 |
| `Print "Wiggle Stick!"` | 0190 | 1 |
| `Repeat 30 times:` | 0190 | 1 |
| `IF X < ` | 0190 | 1 |
| `IF X > ` | 0190 | 1 |
| `Print "Calibrated!"` | 0190 | 1 |
| `Change the number to ` | 0191 | 1 |
| `get current hours` | 0194 | 1 |
| `get current minutes` | 0194 | 1 |
| `if [Button B value]` | 0195 | 1 |
| `count with [pos] from [0] to [length of message - 4]` | 0197 | 1 |
| `sleep for Button Press` | 0198 | 1 |
| `Print "Final: " + ` | 0198 | 1 |
| `IF Green Pressed: ` | 0199 | 1 |
| `IF Red Pressed: Show "BOOM". Alarm` | 0199 | 1 |
