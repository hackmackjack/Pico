import re

def fix_0400_failures():
    target_path = r'd:\MFF\Pico\Documentation\Docs_0401_0500.md'
    
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # REPLACEMENT FOR 0423
    # Locate 0423 Guide
    # Current text (from view):
    # ### 8. Step-by-Step Guide
    # 
    # **A. Initialization Phase**
    # 1.  **Configure Pins**:
    #
    # New Text (Elite Standard):
    guide_0423 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Configure Pins**:
  *   From **Smart IO**, drag `pico_analog_setup` (GP26).
  *   **Snap** into setup block.
  *   From **Smart IO**, drag `pico_pwm_setup` (GP15).
  *   **Snap** below.

**B. Main Loop Phase**
1.  **Read and Map**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Smart IO**, drag `pico_analog_read` (GP26) -> `lightLevel`.
  *   From **Math**, drag `map_range` (`lightLevel`, 0, 65535, 200, 2000) -> `frequency`.
  *   **Snap** into loop.
2.  **Tone Output**:
  *   From **Smart IO**, drag `pico_pwm_write` (GP15, `frequency`).
  *   **Snap** below mapping.
  *   From **Time**, drag `pico_wait` (0.05s).
  *   **Snap** below."""

    # REPLACEMENT FOR 0424
    guide_0424 = """### 8. Step-by-Step Guide

**A. Initialization Phase**
1.  **Setup**:
  *   From **Smart IO**, drag `pico_pwm_setup` (GP15).
  *   **Snap** into setup block.
  *   From **Variables**, drag `create_list` (`notes` = [262, 330, 392]).
  *   **Snap** below.

**B. Main Loop Phase**
1.  **Arpeggio**:
  *   From **Loops**, drag `pico_forever`.
  *   From **Loops**, drag `for_in_list` (`note`, `notes`).
  *   **Snap** into loop.
  *   Inside:
      *   From **Smart IO**, drag `pico_pwm_write` (GP15, `note`, 50%).
      *   **Snap** inside.
      *   From **Time**, drag `pico_wait` (0.5s).
      *   **Snap** below.
  *   From **Smart IO**, drag `pico_pwm_write` (GP15, 0, 0%).
  *   **Snap** below loop (silence).
  *   From **Time**, drag `pico_wait` (0.5s).
  *   **Snap** below."""

    # Apply fixes
    # We use regex to find the block between "### 8. Step-by-Step Guide" and "### 9. Execution Flow"
    # for specific projects.
    
    # Project 0423
    pattern_0423 = r"(## 1\. Project 0423:.*?### 8\. Step-by-Step Guide)(.*?)(\n\n### 9\. Execution Flow)"
    # Note: DOTALL is needed.
    # We need to be careful not to match too much if regex is greedy.
    # So we find the project start, then the guide start.
    
    # Alternative: Use simple string find since we know the content somewhat.
    # Locate "Project 0423: Manual Sound"
    idx_423 = content.find("Project 0423: Manual Sound")
    if idx_423 != -1:
         idx_guide = content.find("### 8. Step-by-Step Guide", idx_423)
         idx_exec = content.find("### 9. Execution Flow", idx_guide)
         if idx_guide != -1 and idx_exec != -1:
             content = content[:idx_guide] + guide_0423 + content[idx_exec:]
             print("Fixed 0423.")

    # Project 0424
    idx_424 = content.find("Project 0424: Sound & Music")
    if idx_424 != -1:
         idx_guide = content.find("### 8. Step-by-Step Guide", idx_424)
         idx_exec = content.find("### 9. Execution Flow", idx_guide)
         if idx_guide != -1 and idx_exec != -1:
             content = content[:idx_guide] + guide_0424 + content[idx_exec:]
             print("Fixed 0424.")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Failure Fixes Complete.")

if __name__ == "__main__":
    fix_0400_failures()
