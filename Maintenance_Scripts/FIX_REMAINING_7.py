import re

def fix_remaining_7():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The 7 failed IDs
    # 0573, 0575, 0578, 0579, 0581, 0583, 0585
    
    replacements = {
        "0573": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Zero**:
  *   From **Variables**, set `start_time` to **Time** `pico_milliseconds`.
  *   **Snap** into `start`.

**B. Main Loop Phase**
1.  **Lap**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Btn A (Lap) Pressed:
      *   From **Variables**, set `current` to `pico_milliseconds`.
      *   From **Variables**, set `lap_time` to `current` - `last_lap`.
      *   From **Text**, print `lap_time`.
      *   From **Variables**, set `last_lap` to `current`.
  *   **Snap** into loop.""",

        "0575": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Wait**:
  *   From **Time**, wait Random (1-5s).
  *   **Snap** into `start`.

**B. Active Phase**
1.  **Signal**:
  *   From **Smart IO**, set LED HIGH.
  *   From **Variables**, set `start` to `pico_milliseconds`.
2.  **React**:
  *   From **Loops**, repeat until Button Pressed.
  *   From **Variables**, set `end` to `pico_milliseconds`.
3.  **Score**:
  *   From **Text**, print `end - start`.""",

        "0578": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**:
  *   From **Variables**, set `target` to 1000ms.

**B. Play Phase**
1.  **Start**:
  *   From **Loops**, wait for Button -> Set `start` = `pico_milliseconds`.
2.  **Stop**:
  *   From **Loops**, wait for Button -> Set `stop` = `pico_milliseconds`.
3.  **Result**:
  *   From **Variables**, set `diff` to `stop` - `start`.
  *   From **Variables**, set `error` to abs(`diff` - 1000).
  *   From **Display**, show `error`.""",

        "0579": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Lifetime**:
  *   From **Variables**, set `total_secs` to 0.

**B. Main Loop Phase**
1.  **Accumulate**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Logic**, if Switch On:
      *   From **Logic**, if 1 second passed:
          *   From **Variables**, change `total_secs` by 1.
          *   From **Text**, print `total_secs`.
  *   **Snap** into loop.""",

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
      *   From **Text**, print ".".
  *   **Snap** into loop.""",

        "0583": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Select**:
  *   From **Loops**, repeat Until Button Pressed:
      *   From **Variables**, set `m` to Map `pico_adc_read` to 1-60.
      *   From **Display**, show "SET: `m` MINS".
2.  **Run**:
  *   From **Variables**, set `s` to m * 60.
  *   From **Loops**, repeat while `s` > 0:
      *   From **Display**, show Time. Wait 1s.
      *   From **Variables**, change `s` by -1.""",

        "0585": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Mode**:
  *   From **Variables**, set `type` to 0.

**B. Select Phase**
1.  **Cycle**:
  *   From **Loops**, repeat Until Button Released.
  *   From **Logic**, if Button Click:
      *   From **Variables**, set `type` to (`type` + 1) % 3.
  *   From **Logic**, if `type` == 0: Print "Small".
  *   From **Logic**, if `type` == 1: Print "Medium".
  *   From **Logic**, if `type` == 2: Print "Large".
  *   **Snap** into loop."""
    }

    print("Injecting correct Elite-Standard Guides for 7 failed projects...")
    
    for pid, new_text in replacements.items():
        # Locate project
        idx_proj = content.find(f"Project {pid}")
        if idx_proj == -1:
            print(f"FAIL: {pid} not found")
            continue
            
        # Locate Guide
        idx_guide = content.find("### 8. Step-by-Step Guide", idx_proj)
        if idx_guide == -1:
             print(f"FAIL: {pid} Guide not found")
             continue
             
        # Locate Exec
        idx_exec = content.find("### 9. Execution Flow", idx_guide)
        if idx_exec == -1:
             print(f"FAIL: {pid} Exec not found")
             continue
             
        # Replace
        old_block = content[idx_guide:idx_exec]
        # We replace with new text + double newline
        # Be careful to preserve Headers
        
        pre = content[:idx_guide]
        post = content[idx_exec:]
        
        content = pre + new_text + "\n\n" + post
        print(f"Fixed {pid}")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fix Complete.")

if __name__ == "__main__":
    fix_remaining_7()
