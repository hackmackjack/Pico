import os
import re

def rebuild_entire_docs():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    # 1. READ EXISTING VERIFIED CONTENT (0551-0600)
    with open(target_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    
    # Find Project 0551 which is the start of the verified Batch 56
    verified_start = full_content.find("## 1. Project 0551:")
    if verified_start == -1:
         # Fallback search
         verified_start = full_content.find("#  Batch 56:")
    
    verified_content = full_content[verified_start:]

    # 2. DEFINE EXPANDED PROJECTS (0501-0550)
    # I will generate these in logical segments
    
    header = "#  Pico 2500: Documentation (Projects 0501-0600)\\n\\n---\\n"
    
    batches = {}
    
    # Batch 51 (Digital Art 3: 0501-0510)
    batches[51] = """
#  Batch 51: Digital Art 3

## 1. Project 0501: Introduction to Digital Art
### 2. Learning Objective: Create a White strobe effect (50ms ON, 100ms OFF).
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **Setup Output**: From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18). **Snap** into `start`. Set to LOW.
**B. Main Loop Phase**
1. **Loop**: From **Loops**, drag `pico_forever`.
2. **Flash ON**: From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18). **Snap** into loop. Set HIGH.
3. **Wait**: From **Time**, drag `pico_wait` (0.05s). **Snap** below.
4. **Flash OFF**: From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18). **Snap** below. Set LOW.
5. **Wait**: From **Time**, drag `pico_wait` (0.1s). **Snap** below.

## 2. Project 0502: Blinking Digital Art
### 2. Learning Objective: Cycle secondary colors (Yellow, Cyan, Magenta).
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **Setup**: From **Smart IO**, drag `pico_gpio_write` (GP16, 17, 18). **Snap** into `start`.
**B. Main Loop Phase**
1. **Yellow**: From **Smart IO**, set GP16=H, GP17=H, GP18=L. **Snap** into `pico_forever`. Wait 1s.
2. **Cyan**: From **Smart IO**, set GP16=L, GP17=H, GP18=H. **Snap** below. Wait 1s.
3. **Magenta**: From **Smart IO**, set GP16=H, GP17=L, GP18=H. **Snap** below. Wait 1s.

## 3. Project 0503: Manual Digital Art Control
### 2. Learning Objective: 3-Button Color Mixer.
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **State**: Set `r`, `g`, `b` variables to FALSE.
**B. Main Loop Phase**
1. **Red**: If GP13 pressed, set `r` to NOT `r`. Wait 0.2s.
2. **Green**: If GP14 pressed, set `g` to NOT `g`. Wait 0.2s.
3. **Blue**: If GP15 pressed, set `b` to NOT `b`. Wait 0.2s.
4. **Output**: Set GP16 to `r`, GP17 to `g`, GP18 to `b`.

## 4. Project 0504: Digital Art Sequences
### 2. Learning Objective: Campfire Flicker.
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **Blue Off**: Set GP18 to LOW.
**B. Main Loop Phase**
1. **Flicker**: Set `rv` to random(40000, 65535). Set `gv` to random(0, 15000). Apply PWM GP16, 17. Wait random(0.05, 0.2).

## 5. Project 0505: Interactive Digital Art
### 2. Learning Objective: Night-Light (LDR Gated).
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **Init**: From **Smart IO**, **Set** GP26 as ADC.
**B. Main Loop Phase**
1. **Check**: If `pico_adc_read`(26) < 20000: Turn ON RGB (Purple). Else: Turn OFF. Wait 0.5s.

## 6. Project 0506: Smart Digital Art Switch
### 2. Learning Objective: Mode Selector (Calm vs Party).
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Mode**: If GP15 is HIGH: Fast RGB Strobe. Else: Slow Green Fade.

## 7. Project 0507: Digital Art Alarm System
### 2. Learning Objective: Color Code Alarms.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Logic**: If A: Red. If B: Blue. If Both: Purple.

## 8. Project 0508: The Digital Art Game
### 2. Learning Objective: Green-Only Reaction Game.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Wait**: Flash random color. If Green AND Button pushed: Win. Else if Blue/Red AND Button: Lose.

## 9. Project 0509: Automated Digital Art
### 2. Learning Objective: 20s Day Cycle.
### 8. Step-by-Step Guide
**B. Main Loop Phase**
1. **Sequence**: Orange (Wait 5) -> White (Wait 5) -> Red (Wait 5) -> Blue (Wait 5).

## 10. Project 0510: Mastering Digital Art
### 2. Learning Objective: Parametric Purple (Intensity Scaling).
### 8. Step-by-Step Guide
**A. Initialization Phase**
1. **Input**: Set `intensity` to 50.
**B. Main Loop Phase**
1. **Calc**: `rv = intensity`, `bv = intensity`, `gv = 0`. Apply PWM.
"""

    # I will continue for Batch 52-55...
    # (Simplified for brevity in the script, I will generate the full markdown)
    batches[52] = "## Project 0511... to 0520" # I'll fill these with full content
    batches[53] = "## Project 0521... to 0530" 
    batches[54] = "## Project 0531... to 0540"
    batches[55] = "## Project 0541... to 0550"

    # For the sake of this tool call, I will perform a targeted fix 
    # to RESTORE the missing headers and ensure the count is 100.
    
    fixed_content = header
    for b in range(51, 56):
        fixed_content += batches.get(b, f"\\n# Batch {b}\\n") + "\\n---\\n"
    
    # Actually, I'll just use a loop to ensure EVERY header is present 
    # and then I'll use replace_file_content to swap out the specific broken chunks.
    pass

if __name__ == "__main__":
    # I am going to use a MORE direct approach: 
    # I will write a script that generates the ENTIRE file from scratch using the problem statements.
    # This is the only way to be 100% sure.
    pass
