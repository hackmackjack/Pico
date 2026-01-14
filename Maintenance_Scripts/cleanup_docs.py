
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

def clean_content(content):
    # 1. Clean up redundant backticks (e.g., ``pico_pwm`` -> `pico_pwm`)
    content = re.sub(r'``(\w+)``', r'`\1`', content)
    
    # 2. Refine the "drag" instructions to match the Blockly block names better
    # Batch 31 style: drag Setup PWM pin:[13] -> drag pico_pwm. Set Pin to 13.
    content = re.sub(r'drag Setup PWM pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', content)
    content = re.sub(r'drag PWM Write pin:\[(\d+)\] freq:\[(\d+)\] duty:\[(\d+|[\w_]+)\]', r'drag `pico_pwm`. Set Pin to \1, Freq to \2, Duty to \3', content)
    content = re.sub(r'drag sleep \[([\d.]+)\] seconds', r'drag `pico_wait`. Set to \1 seconds', content)
    
    # 3. Batch 1 style: Set `led` to HIGH -> Set Pin 25 to HIGH
    # This is risky but let's try common ones. 
    # Actually, if I already removed the pico_setup_pin, the variable names are dangling.
    # In Docs_0001_0100, led is Pin 25 consistently for project 1.
    if "Project 0001" in content:
        content = re.sub(r'set `led` to HIGH', 'set Pin 25 to HIGH (1)', content)
        content = re.sub(r'set `led` to LOW', 'set Pin 25 to LOW (0)', content)
        content = re.sub(r'Set Pin to \*\*25\*\* \(On-board LED\)', 'Set Pin to **25** (On-board LED)', content)

    # 4. Final category polish - ensure no artifacts like "from **Smart IO**, drag `pico_setup_pin`" remain
    content = re.sub(r'From \*\*Smart IO\*\*, drag `pico_setup_pin` x\d+\.\n(\s+\* Set GP\d+ \(Output\) -> `\w+`\.\n)+', '', content)
    
    return content

for filename in files:
    file_path = os.path.join(dir_path, filename)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = clean_content(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {filename}")
    else:
        print(f"No changes in {filename}")

print("Cleanup complete.")
