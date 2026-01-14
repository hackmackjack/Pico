
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

for filename in files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Very broad replacements
    content = content.replace('Setup PWM pin:[', '`pico_pwm` Pin:[')
    content = content.replace('PWM Write pin:[', '`pico_pwm` Pin:[')
    content = content.replace('sleep [', '`pico_wait` [')
    
    # Also fix the "drag" phrasing
    content = re.sub(r'drag `pico_pwm` Pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Broad update complete.")
