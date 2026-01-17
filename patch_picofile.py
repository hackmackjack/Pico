
import os

PICO_FILE = "picofile.html"

# 1. Definition for pico_ticks_ms
DEF_TICKS = """        {
          "type": "pico_ticks_ms",
          "message0": "Ticks (ms)",
          "output": "Number", "colour": 120
        },"""

# 2. Generator for pico_ticks_ms
GEN_TICKS = """      G["pico_ticks_ms"] = function (block) {
        return [`time.ticks_ms()`, Blockly.Python.ORDER_FUNCTION_CALL];
      };"""

# 3. Toolbox additions
# Math Modulo
TB_MODULO = '    <block type="math_modulo"></block>'
# Functions Category
TB_FUNCTIONS = '  <category name="Functions" custom="PROCEDURE" colour="290"></category>'
# Ticks block
TB_TICKS = '    <block type="pico_ticks_ms"></block>'

def patch_picofile():
    with open(PICO_FILE, 'r') as f: content = f.read()

    # Add Definition
    if '"type": "pico_ticks_ms"' not in content:
        # Insert before pico_system (System & IOT)
        target = '// --- SYSTEM & IOT ---'
        content = content.replace(target, DEF_TICKS + "\n\n        " + target)
        print("Added pico_ticks_ms definition.")

    # Add Generator
    if 'G["pico_ticks_ms"]' not in content:
        # Insert after pico_wait
        target = 'G["pico_wait"] = function (block) {'
        end_target = '};'
        # Find end of pico_wait
        idx = content.find(target)
        idx_end = content.find(end_target, idx) + 2
        content = content[:idx_end] + "\n" + GEN_TICKS + content[idx_end:]
        print("Added pico_ticks_ms generator.")

    # Update Toolbox
    if '<block type="math_modulo"></block>' not in content:
        # Insert in Math category
        target = '<category name="Math" colour="230">'
        content = content.replace(target, target + "\n" + TB_MODULO)
        print("Added math_modulo to Toolbox.")

    if '<category name="Functions"' not in content:
        # Insert before Variables
        target = '<category name="Variables" custom="VARIABLE" colour="330"></category>'
        content = content.replace(target, TB_FUNCTIONS + "\n  " + target)
        print("Added Functions category to Toolbox.")

    if '<block type="pico_ticks_ms"></block>' not in content:
        # Insert in Smart IO
        target = '<category name="Smart IO" colour="290">'
        content = content.replace(target, target + "\n" + TB_TICKS)
        print("Added pico_ticks_ms to Toolbox.")

    with open(PICO_FILE, 'w') as f: f.write(content)
    print("picofile.html patched successfully.")

if __name__ == "__main__":
    patch_picofile()
