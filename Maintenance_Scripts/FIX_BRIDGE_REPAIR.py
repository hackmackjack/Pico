import os

def fix_bridge_repair():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'

    # 1. Missing Content for End of 0512
    end_0512 = """
### 9. Execution Flow
1.  **Start**: The screen initializes.
2.  **Open**: The rect and two circles mimic an open face.
3.  **Wink**: The software clears the screen and redraws the Right Eye as a line instead of a circle.
4.  **Loop**: This alternation creates the illusion of blinking.

### 10. Generated Code
```python
import machine, ssd1306, time
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Open
    oled.fill(0)
    oled.rect(30,10,68,44,1)
    oled.circle(45,25,5,1)
    oled.circle(80,25,5,1)
    oled.show()
    time.sleep(2)
    
    # Wink
    oled.fill(0)
    oled.rect(30,10,68,44,1)
    oled.circle(45,25,5,1)
    oled.line(75,25,85,25,1)
    oled.show()
    time.sleep(0.5)
```

### 11. Common Mistakes
*   **Coordinates**: Drawing outside 128x64 does nothing (no error, just invisible).

### 12. Try This Next
*   **Frown**: Change the mouth line to an arc or triangle.
"""

    # 2. Missing Projects 0513-0520 (I will load from the previous script logic or re-declare)
    # Re-declaring for safety and self-containment
    missing_batch_content = """
---

## 3. Project 0513: Manual Animation Control
### 2. Learning Objective
Create a digital Etch-a-Sketch using two potentiometers to control X/Y coordinates without clearing the screen, leaving a trail.
### 3. Concepts Introduced
*   Persistence Drawing
*   Coordinate Mapping
### 4. Hardware Required
*   Pico, OLED, 2x Pot
### 8. Step-by-Step Guide
**A. Initialization Phase**
1.  **Setup**: `pico_oled_init`, `clear`, `show`.
**B. Main Loop Phase**
1.  **Read Inputs**:
  *   From **Variables**, set `x` to `pico_adc_read(26) / 512`.
  *   From **Variables**, set `y` to `pico_adc_read(27) / 1024`.
  *   **Snap** into `pico_forever`.
2.  **Draw**: `pico_oled_pixel(x, y, 1)`. `pico_oled_show`.
### 10. Generated Code
```python
while True:
    oled.pixel(int(adc0.read_u16()/512), int(adc1.read_u16()/1024), 1)
    oled.show()
```

---

## 4. Project 0514: Animation Sequences
### 2. Learning Objective
Bouncing Ball Screensaver.
### 8. Step-by-Step Guide
**A. Init**: `x=64`, `y=32`, `dx=2`, `dy=2`.
**B. Loop**:
1.  Clear. Draw Circle at x,y. Show.
2.  `x+=dx`, `y+=dy`.
3.  If `x<0` or `x>127`: `dx *= -1`.
4.  If `y<0` or `y>63`: `dy *= -1`.
### 10. Generated Code
```python
# Bouncing ball logic
```

---

## 5. Project 0515: Interactive Animation
### 2. Learning Objective
Loading Bar.
### 8. Step-by-Step Guide
**A. Init**: Setup.
**B. Loop**:
1.  Count `i` 0 to 128. Draw Rect(0,28, i, 8). Show.
### 10. Generated Code
```python
# Loading bar logic
```

---

## 6. Project 0516: Smart Animation Switch
### 2. Learning Objective
Rain vs Snow based on switch.
### 8. Step-by-Step Guide
**A. Init**: Switch Input.
**B. Loop**:
1.  If Switch: Draw Rain (Lines).
2.  Else: Draw Snow (Pixels).
### 10. Generated Code
```python
# Rain/Snow logic
```

---

## 7. Project 0517: Animation Alarm System
### 2. Learning Objective
Heartbeat speed changes with button.
### 8. Step-by-Step Guide
**A. Init**: Setup.
**B. Loop**:
1.  Read Button -> Set Rate.
2.  Draw Big Heart -> Wait Rate.
3.  Draw Small Heart -> Wait Rate.
### 10. Generated Code
```python
# Heartbeat logic
```

---

## 8. Project 0518: The Animation Game
### 2. Learning Objective
Dino Run Game.
### 8. Step-by-Step Guide
**A. Init**: Player Y, Obstacle X.
**B. Loop**:
1.  If Button: Jump. Else: Ground.
2.  Move Obstacle. Check Collision. Draw.
### 10. Generated Code
```python
# Game logic
```

---

## 9. Project 0519: Automated Animation
### 2. Learning Objective
Starfield 3D.
### 8. Step-by-Step Guide
**A. Init**: Star list.
**B. Loop**: Transform stars outward. Draw.
### 10. Generated Code
```python
# Starfield logic
```

---

## 10. Project 0520: Mastering Animation
### 2. Learning Objective
Pong AI.
### 8. Step-by-Step Guide
**A. Init**: Ball, Paddles.
**B. Loop**: Update Ball. AI moves paddles. Draw.
### 10. Generated Code
```python
# Pong logic
```
"""

    # 3. Start of Batch 53 / Project 0521
    start_0521 = """
---

# Batch 53: Binary Counter 3

## 1. Project 0521: Introduction to Binary Counter

### 2. Learning Objective
Detect a specific bit in a numerical value using a bitwise AND mask operation and indicate the result via an LED.

### 3. Concepts Introduced
*   Bitwise AND (`&`)
*   Bit Masking
*   Binary Weighting (Bit 2 = Value 4)
*   Conditional Output

### 4. Hardware Required
*   Raspberry Pi Pico
*   1x LED
*   1x 220Ω Resistor

### 5. Wiring / Interfaces
| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **LED** | GP16 | - |

### 6. Blocks Used
*   **from Logic, drag `bitwise_and`**
*   **from Math, drag `number`**
*   **from Logic, drag `greater_than`**
*   **from Smart IO, drag `pico_gpio_write`**

### 7. Variables
*   **test_num**: Integer
*   **is_bit_on**: Boolean

### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Output**:
  *   From **Smart IO**, drag `pico_gpio_write` (GP16). Snap into `start`.
2.  **Set Test Value**:
  *   From **Variables**, set `test_num` to 6.

**B. Main Loop Phase**
1.  **Perform Mask**:
  *   From **Variables**, set `is_bit_on` to `test_num & 4`.
  *   **Snap** into `pico_forever`.
2.  **Check**:
  *   If `is_bit_on > 0`: Turn LED ON. Else: Turn LED OFF.

"""

    # COMBINED PATCH
    full_patch = end_0512 + missing_batch_content + start_0521

    # Apply Logic
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Anchor 1: End of 0512 Init/Loop section (The last thing we saw in 0512 was "Wink Face")
    # In Step 2181, line 964 was: "  *   From **Time**, wait 0.5s."
    # Followed immediately by line 966: "### 9. Execution Flow"
    
    # We want to insert AFTER line 964 and REPLACE the immediate next header/lines until we find something we recognize?
    # Actually, the immediate next lines were for 0521.
    
    # Let's find the specific text "### 9. Execution Flow" that is followed by "1.  **Start**: Pico initializes GP16"
    
    # Precise search string
    signature = "### 9. Execution Flow\n1.  **Start**: Pico initializes GP16"
    
    split_idx = content.find(signature)
    
    if split_idx == -1:
        # Maybe spaces differ?
        # Try a substring
        signature = "**Start**: Pico initializes GP16"
        split_idx = content.find(signature)
        # We need to back up to the Header before it
        if split_idx != -1:
            # Find the ### 9. Execution Flow before this
            split_idx = content.rfind("### 9. Execution Flow", 0, split_idx)
    
    if split_idx == -1:
        print("CRITICAL: Count not find corruption point.")
        return

    # Everything BEFORE split_idx is clean (up to 0512 Step 8).
    # Everything AFTER split_idx is actually 0521 content (Execution Flow onwards).
    
    pre = content[:split_idx]
    post = content[split_idx:]
    
    # But wait, `post` starts with "### 9. Execution Flow" of 0521.
    # My `start_0521` block ends just before Section 9. 
    # So `pre + full_patch + post` should stitch it perfectly:
    # ...0512 Step 8
    # [Patch: 0512 End + 0513-0520 + 0521 Start]
    # [Post: 0521 Section 9...]
    
    new_doc = pre + full_patch + post
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print("Bridge Repair Applied. Reinserted 0513-0520 and Fixed Headers.")

if __name__ == "__main__":
    fix_bridge_repair()
