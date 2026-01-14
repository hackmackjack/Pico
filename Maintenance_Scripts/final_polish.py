
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

def final_polish(content):
    # 1. Remove any remaining pico_setup_pin references gracefully
    content = re.sub(r'\*   From \*\*Smart IO\*\*, drag `pico_setup_pin`\..*\n?', '', content)
    
    # 2. Fix the "drag Setup PWM pin" and "drag PWM Write" to "drag `pico_pwm`"
    # Handling potential space and character variations
    content = re.sub(r'drag Setup PWM pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', content)
    content = re.sub(r'drag PWM Write pin:\[(\d+)\] freq:\[(\d+)\] duty:\[(\d+|[\w_]+)\]', r'drag `pico_pwm`. Set Pin to \1, Freq to \2, Duty to \3', content)
    content = re.sub(r'drag sleep \[([\d.]+)\] seconds', r'drag `pico_wait`. Set to \1 seconds', content)
    content = re.sub(r'drag sleep block', r'drag `pico_wait` block', content)

    # 3. Ensure categories are bolded consistently
    content = re.sub(r'From Smart IO', 'From **Smart IO**', content)
    content = re.sub(r'From Smart Sensors', 'From **Smart Sensors**', content)
    content = re.sub(r'From Motion & Motors', 'From **Motion & Motors**', content)
    
    return content

for filename in files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = final_polish(content)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Final polish complete.")
