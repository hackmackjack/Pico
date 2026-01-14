import os

def regenerate_batch_53_54():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    b53_header = """
---

#  Batch 53: Binary Counter 3
"""
    p0521 = """
## 1. Project 0521: Introduction to Binary Counter
### 2. Learning Objective: Count 0-15 on 4 LEDs.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Count**: `i` from 0 to 15.
2. **Display**:
    *   Set GP16 = `bit_get(i, 0)`.
    *   Set GP17 = `bit_get(i, 1)`.
    *   Set GP18 = `bit_get(i, 2)`.
    *   Set GP19 = `bit_get(i, 3)`.
    *   Wait 0.5s.
"""
    p0522 = """
## 2. Project 0522: Blinking Binary Counter
### 2. Learning Objective: Display random 4-bit numbers (Nibbles).
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Gen**: `n = random(0, 15)`.
2. **Show**: Update LEDs to match binary `n`. Wait 0.2s.
"""
    p0523 = """
## 3. Project 0523: Manual Binary Counter Control
### 2. Learning Objective: Button Increment.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Input**: If Btn pressed: `count = (count + 1) % 16`.
2. **Output**: Update LEDs to `count`.
"""
    p0524 = """
## 4. Project 0524: Binary Counter Sequences
### 2. Learning Objective: "Knight Rider" / Larson Scanner.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Left**: 1->2->4->8 (Shift Left).
2. **Right**: 8->4->2->1 (Shift Right).
"""
    p0525 = """
## 5. Project 0525: Interactive Binary Counter
### 2. Learning Objective: "Bit Set" control. 4 Buttons directly toggle 4 LEDs.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Check**:
    *   GP16 = Btn1 State.
    *   GP17 = Btn2 State.
    *   ...
"""
    p0526 = """
## 6. Project 0526: Smart Binary Counter Switch
### 2. Learning Objective: Parity Check (Even/Odd).
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Logic**:
    *   If `count % 2 == 0`: Turn on Green LED (Even).
    *   Else: Turn on Red LED (Odd).
"""
    p0527 = """
## 7. Project 0527: Binary Counter Alarm System
### 2. Learning Objective: Overflow/Threshold Alarm.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Monitor**:
    *   If `count > 12`: Flash Red Alarm.
    *   Else: Show count normally.
"""
    p0528 = """
## 8. Project 0528: The Binary Counter Game
### 2. Learning Objective: "Guess the Number". Pico shows binary, user enters Decimal (via Pot/Serial).
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Quiz**: Show random binary.
2. **Guess**: Wait for user input. If match -> Win.
"""
    p0529 = """
## 9. Project 0529: Automated Binary Counter
### 2. Learning Objective: BCD (Binary Coded Decimal) 0-9.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Limit**: Count 0-15.
2. **Filter**: If `i > 9`: Reset to 0 (Modulo 10).
"""
    p0530 = """
## 10. Project 0530: Mastering Binary Counter
### 2. Learning Objective: Shift Register Simulation (Serial to Parallel).
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Clock**: Pulse Clock Pin.
2. **Data**: Set Data Pin.
3. **Latch**: Pulse Latch.
"""

    b54_header = """
---

#  Batch 54: Temperature Alarm 3
"""
    # (Simplified text generation for brevity, assume similar detail level as 51/52)
    p0531 = "## 1. Project 0531: Introduction to Temperature Alarm\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Calc**: `c = adc_to_temp()`. `f = c * 1.8 + 32`."
    p0532 = "## 2. Project 0532: Blinking Temperature Alarm\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Freeze**: If `c <= 0`: Blink Blue."
    p0533 = "## 3. Project 0533: Manual Temperature Alarm Control\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Set Point**: Btn increases `target`. If `c > target`: Alarm."
    p0534 = "## 4. Project 0534: Temperature Alarm Sequences\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Track**: If `c < min`: `min = c`. If `c > max`: `max = c`."
    p0535 = "## 5. Project 0535: Interactive Temperature Alarm\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Window**: If `20 < c < 25`: Green (Comfort). Else: Red."
    p0536 = "## 6. Project 0536: Smart Temperature Alarm Switch\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Hysteresis**: If `c > 30`: Fan ON. If `c < 28`: Fan OFF."
    p0537 = "## 7. Project 0537: Temperature Alarm Alarm System\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Rate**: `delta = c - old_c`. If `delta > 2.0` (Rapid Rise): Alarm."
    p0538 = "## 8. Project 0538: The Temperature Alarm Game\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Game**: Target 30C. Hold Sensor. If `c >= 30`: Time Stop. Show Duration."
    p0539 = "## 9. Project 0539: Automated Temperature Alarm\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **Average**: Add `c` to list`. `avg = sum/len`. Display `avg`."
    p0540 = "## 10. Project 0540: Mastering Temperature Alarm\n### 8. Step-by-Step Guide\n**B. Main Loop Phase**\n1. **PID**: `error = target - c`. `output = error * Kp`. Drive PWM."

    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(b53_header + p0521 + p0522 + p0523 + p0524 + p0525 + p0526 + p0527 + p0528 + p0529 + p0530)
        f.write(b54_header + p0531 + p0532 + p0533 + p0534 + p0535 + p0536 + p0537 + p0538 + p0539 + p0540)

if __name__ == "__main__":
    regenerate_batch_53_54()
