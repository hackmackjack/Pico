import re

def fix_foolproof():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    replacements = {
        "0513": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
  *   From **Display**, drag `pico_oled_init`.
  *   From **Display**, drag `pico_oled_clear`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Read Constants**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, set `x` to `pico_adc_read(26)` / 512.
  *   **Snap** into loop.
  *   From **Variables**, set `y` to `pico_adc_read(27)` / 1024.
2.  **Draw**:
  *   From **Display**, drag `pico_oled_pixel`.
  *   Set X=`x`, Y=`y`, Color=1.
  *   From **Display**, drag `pico_oled_show`.
  *   **Snap** below pixel.""",

        "0514": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**:
  *   Set `x`=64, `y`=32.
  *   Set `dx`=2, `dy`=2.

**B. Main Loop Phase**
1.  **Bounce**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Display**, `pico_oled_clear`.
  *   From **Display**, `pico_oled_circle` (x,y,5).
  *   **Snap** into loop.
2.  **Update**:
  *   Change `x` by `dx`. Change `y` by `dy`.
  *   From **Logic**, if `x` < 0 OR `x` > 127: `dx` = `dx` * -1.
  *   From **Logic**, if `y` < 0 OR `y` > 63: `dy` = `dy` * -1.
  *   `pico_oled_show`. Wait 0.05s.""",

        "0515": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: Init OLED.

**B. Main Loop Phase**
1.  **Load Bar**:
  *   From **Loops**, count `i` from 0 to 128.
  *   **Snap** into loop.
  *   From **Display**, `pico_oled_rect`.
  *   Set X=0, Y=28, W=`i`, H=8.
  *   `pico_oled_show`. Wait 0.02s.""",

        "0516": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Switch**: GP14 In.

**B. Main Loop Phase**
1.  **Mode**:
  *   From **Loops**, drag `pico_forever`.
  *   If Switch On:
      *   From **Display**, draw Lines (Rain).
  *   Else:
      *   From **Display**, draw Pixels (Snow).
  *   **Snap** into loop.
  *   `pico_oled_show`.""",

        "0517": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Heart**: Setup.

**B. Main Loop Phase**
1.  **Beat**:
  *   From **Loops**, drag `pico_forever`.
  *   Draw Big Heart. `pico_oled_show`. Wait 0.5s.
  *   **Snap** into loop.
  *   Draw Small Heart. `pico_oled_show`. Wait 0.5s.""",

        "0518": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Vars**: `py`=50, `ox`=120.

**B. Main Loop Phase**
1.  **Run**:
  *   From **Loops**, drag `pico_forever`.
  *   If Button: `py` = 20 (Jump). Else: `py` = 50.
  *   Change `ox` by -5.
  *   **Snap** into loop.
  *   Draw Dino at (10, `py`).
  *   Draw Cactus at (`ox`, 50).
  *   `pico_oled_show`.""",

        "0519": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Sine**: `angle`=0.

**B. Main Loop Phase**
1.  **Wave**:
  *   From **Loops**, drag `pico_forever`.
  *   Calc `y` = 32 + sin(`angle`)*30.
  *   **Snap** into loop.
  *   Pixel (64, `y`).
  *   Show. Change `angle`.""",

        "0520": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Starfield**: List of STARS.

**B. Main Loop Phase**
1.  **Warp**:
  *   From **Loops**, drag `pico_forever`.
  *   For each Star:
      *   Move X back. Move Y out.
      *   If Offscreen: Reset to center.
      *   Pixel(X,Y).
  *   **Snap** into loop.
  *   Show.""",

        "0522": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**: GP16-GP19 Output.

**B. Main Loop Phase**
1.  **Count**:
  *   From **Loops**, count `i` from 0 to 15.
  *   **Snap** into `pico_forever`.
  *   Set GP16 = `i` bit 0.
  *   Set GP17 = `i` bit 1.
  *   Set GP18 = `i` bit 2.
  *   Set GP19 = `i` bit 3.
  *   Wait 0.5s.""",

        "0538": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**: Sets random temp.

**B. Main Loop Phase**
1.  **Guess**:
  *   From **Loops**, drag `pico_forever`.
  *   `current` = Read Temp.
  *   `diff` = abs(`target` - `current`).
  *   **Snap** into loop.
  *   If `diff` < 2: Green LED.
  *   Else: Red LED.""",

        "0550": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **PID**: Set Kp, Ki, Kd.

**B. Main Loop Phase**
1.  **Control**:
  *   From **Loops**, drag `pico_forever`.
  *   `error` = Target - Temp.
  *   `pwm` = PID(`error`).
  *   **Snap** into loop.
  *   Set Fan Speed `pwm`.""",

        "0599": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Tempo**: `gap` = 1.0s.

**B. Main Loop Phase**
1.  **Accelerate**:
  *   From **Loops**, drag `pico_forever`.
  *   Repeat 4 times (Bar):
      *   Click. Wait `gap`.
  *   Change `gap` by -5%.
  *   **Snap** into loop.""",

        "0573": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Zero**:
  *   Set `start_time` = `pico_milliseconds`.

**B. Main Loop Phase**
1.  **Lap**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Btn A (Lap) Pressed:
      *   Set `current` = `pico_milliseconds`.
      *   Set `lap_time` = `current` - `last_lap`.
      *   From **Text**, print `lap_time`.
      *   Set `last_lap` = `current`.""",

        "0575": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wait**:
  *   Wait Random (1-5s).

**B. Active Phase**
1.  **Signal**:
  *   From **Smart IO**, set LED HIGH.
  *   Set `start` = `pico_milliseconds`.
2.  **React**:
  *   From **Loops**, repeat until Button Pressed.
  *   Set `end` = `pico_milliseconds`.
3.  **Score**:
  *   From **Text**, print `end - start`.""",

        "0578": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**: 1000ms.

**B. Play Phase**
1.  **Start**:
  *   Wait for Button -> Set `start` = `pico_milliseconds`.
2.  **Stop**:
  *   Wait for Button -> Set `stop` = `pico_milliseconds`.
3.  **Result**:
  *   Set `diff` = `stop` - `start`.
  *   Set `error` = abs(`diff` - 1000).
  *   From **Display**, show `error`.""",

        "0579": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Lifetime**: `total_secs` = 0.

**B. Main Loop Phase**
1.  **Accumulate**:
  *   From **Loops**, drag `pico_forever`.
  *   If Switch On:
      *   If 1 second passed: Change `total_secs` by 1.
      *   From **Text**, print `total_secs`.""",

        "0581": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Start Print**:
  *   From **Text**, print "Timer Started...".

**B. Main Loop Phase**
1.  **Count Seconds**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Variables**, change `ticks` by 1.
2.  **Format**:
  *   From **Logic**, if (`ticks` % 10) == 0:
      *   From **Text**, print " [10s Marks]".
  *   Else:
      *   From **Text**, print ".".""",

        "0583": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Select**:
  *   From **Loops**, repeat Until Button Pressed:
      *   Set `m` = Map `pico_adc_read` to 1-60.
      *   From **Display**, show "SET: `m` MINS".
2.  **Run**:
  *   Set `s` = m * 60.
  *   Repeat while `s` > 0:
      *   Show Time. Wait 1s.
      *   Change `s` by -1.""",

        "0585": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mode**: `type` = 0.

**B. Select Phase**
1.  **Cycle**:
  *   From **Loops**, repeat Until Button Released.
  *   If Button Click: `type` = (`type` + 1) % 3.
  *   From **Logic**, if 0: Print "Small".
  *   If 1: Print "Medium".
  *   If 2: Print "Large"."""
    }
    
    # Also add the Batch 58/59 stragglers if needed, but let's test these first.
    # Actually, adding them is safe.
    
    keys = list(replacements.keys())
    
    for pid in keys:
        target_str = f"Project {pid}"
        idx_proj = content.find(target_str)
        if idx_proj == -1:
            print(f"FAIL: Could not find Project {pid}")
            continue
            
        # Find Guide Header
        idx_guide = content.find("### 8. Step-by-Step Guide", idx_proj)
        if idx_guide == -1:
            print(f"FAIL: Could not find Guide for {pid}")
            continue
            
        # Find Exec Header
        idx_exec = content.find("### 9. Execution Flow", idx_guide)
        if idx_exec == -1:
            print(f"FAIL: Could not find Exec Flow for {pid}")
            continue
            
        # We replace EXACTLY the chunk between these two indices
        old_block = content[idx_guide:idx_exec]
        new_block = replacements[pid] + "\n\n"
        
        # Perform replacement on the full string
        # Warning: If there are multiple occurrences of this specific block text elsewhere (unlikely)
        # But here we are using indices so we can construct a new string
        
        pre = content[:idx_guide]
        post = content[idx_exec:]
        content = pre + new_block + post
        
        print(f"Success: Fixed {pid}")
        
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Foolproof fix executed.")

if __name__ == "__main__":
    fix_foolproof()
