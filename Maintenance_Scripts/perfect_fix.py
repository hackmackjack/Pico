
import os
import re

dir_path = r'd:\MFF\Pico\Documentation'
files = [f for f in os.listdir(dir_path) if f.startswith('Docs_') and f.endswith('.md')]

def perfect_fix(content):
    # 1. Fix double backticks
    content = content.replace('``', '`')
    
    # 2. Fix the "drag `pico_pwm` Pin:[13]" pattern to be "drag `pico_pwm`. Set Pin to 13."
    content = re.sub(r'drag `pico_pwm` Pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', content)
    content = re.sub(r'drag `pico_pwm` Pin:\[(\d+)\] freq:\[(\d+)\] duty:\[(\d+|[\w_]+)\]', r'drag `pico_pwm`. Set Pin to \1, Freq to \2, Duty to \3', content)
    content = re.sub(r'drag `pico_wait` \[([\d.]+)\] seconds', r'drag `pico_wait`. Set to \1 seconds', content)
    
    return content

for filename in files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = perfect_fix(content)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Perfect fix complete.")
