import re

def fix_final_real():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        "0578": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Target**:
  *   From **Variables**, set `target` to 1000ms.
  *   **Snap** into `start`.

**B. Play Phase**
1.  **Start**:
  *   From **Loops**, wait for Button -> Set `start` = `pico_milliseconds`.
  *   **Snap** into loop.
2.  **Stop**:
  *   From **Loops**, wait for Button -> Set `stop` = `pico_milliseconds`.
  *   **Snap** below start.
3.  **Result**:
  *   From **Variables**, set `diff` to `stop` - `start`.
  *   From **Variables**, set `error` to abs(`diff` - 1000).
  *   From **Display**, show `error`.
  *   **Snap** at bottom.""",

        "0583": """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Select**:
  *   From **Loops**, repeat Until Button Pressed:
      *   From **Variables**, set `m` to Map `pico_adc_read` to 1-60.
      *   From **Display**, show "SET: `m` MINS".
  *   **Snap** into `start`.
2.  **Run**:
  *   From **Variables**, set `s` to m * 60.
  *   From **Loops**, repeat while `s` > 0:
      *   From **Display**, show Time. Wait 1s.
      *   From **Variables**, change `s` by -1.
  *   **Snap** below selection loop."""
    }

    print("Applying Corrected Elite-Standard Guides for 0578 and 0583...")
    
    for pid, new_text in replacements.items():
        # Locate project
        idx_proj = content.find(f"Project {pid}")
        if idx_proj == -1:
            print(f"FAIL: {pid} not found (Trying 'Project {pid}:')")
            idx_proj = content.find(f"Project {pid}:")
            if idx_proj == -1: continue

        # Locate Guide
        idx_guide = content.find("### 8. Step-by-Step Guide", idx_proj)
        if idx_guide == -1: continue
             
        # Locate Exec
        idx_exec = content.find("### 9. Execution Flow", idx_guide)
        if idx_exec == -1: continue
             
        # Replace
        pre = content[:idx_guide]
        post = content[idx_exec:]
        content = pre + new_text + "\n\n" + post
        print(f"Fixed {pid}")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fix Complete.")

if __name__ == "__main__":
    fix_final_real()
