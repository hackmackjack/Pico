import re
from pathlib import Path

def fix_categories(file_path):
    print(f"Fixing categories in {file_path.name}...")
    content = Path(file_path).read_text(encoding='utf-8')
    
    mapping = {
        # Catch **Category:** Displays and variants
        r'\*\*Category:\*\*\s*Displays': '**Category:** Smart Display',
        r'\*\*Category:\*\*\s*Display': '**Category:** Smart Display',
        r'\*\*Category:\*\*\s*Timing': '**Category:** Smart IO',
        r'\*\*Category:\*\*\s*Actuators': '**Category:** Motion & Motors',
        r'\*\*Category:\*\*\s*Sensors': '**Category:** Smart Sensors',
        r'\*\*Category:\*\*\s*Robotics': '**Category:** Motion & Motors',
        r'\*\*Category:\*\*\s*Pin Access': '**Category:** Smart IO',
        r'\*\*Category:\*\*\s*System': '**Category:** System & Storage',
        r'\*\*Category:\*\*\s*IoT': '**Category:** Network & IoT',
        
        # From **Bold** variants
        r'From \*\*Displays\*\*': 'From **Smart Display**',
        r'From \*\*Display\*\*': 'From **Smart Display**',
        r'From \*\*Timing\*\*': 'From **Smart IO**',
        r'From \*\*Actuators\*\*': 'From **Motion & Motors**',
        r'From \*\*Sensors\*\*': 'From **Smart Sensors**',
        r'From \*\*Robotics\*\*': 'From **Motion & Motors**',
        r'From \*\*Pin Access\*\*': 'From **Smart IO**',
        
        # (Category: XYZ) variants
        r'\(Category:\s*Displays\)': '(Category: Smart Display)',
        r'\(Category:\s*Display\)': '(Category: Smart Display)',
        r'\(Category:\s*Timing\)': '(Category: Smart IO)',
        r'\(Category:\s*Actuators\)': '(Category: Motion & Motors)',
        r'\(Category:\s*Sensors\)': '(Category: Smart Sensors)',
        r'\(Category:\s*Robotics\)': '(Category: Motion & Motors)',
        r'\(Category:\s*Pin Access\)': '(Category: Smart IO)',
        r'\(Category:\s*System\)': '(Category: System & Storage)',
        r'\(Category:\s*IoT\)': '(Category: Network & IoT)',
        
        # Plain bold category names
        r'\*\*Displays\*\*': '**Smart Display**',
        r'\*\*Display\*\*': '**Smart Display**',
        r'\*\*Timing\*\*': '**Smart IO**',
        r'\*\*Actuators\*\*': '**Motion & Motors**',
        r'\*\*Sensors\*\*': '**Smart Sensors**',
        r'\*\*Robotics\*\*': '**Motion & Motors**',
        r'\*\*Pin Access\*\*': '**Smart IO**',
        
        # Specific Block Category Fixes (TM1637 & LCD belong to Smart Display)
        r'From \*\*Smart IO\*\*, drag `pico_tm1637_init`': 'From **Smart Display**, drag `pico_tm1637_init`',
        r'From \*\*Smart IO\*\*, drag `pico_tm1637_show`': 'From **Smart Display**, drag `pico_tm1637_show`',
        r'From \*\*Smart IO\*\*, drag `pico_tm1637_colon`': 'From **Smart Display**, drag `pico_tm1637_colon`',
        r'From \*\*Smart IO\*\*, drag `pico_tm1637_brightness`': 'From **Smart Display**, drag `pico_tm1637_brightness`',
        r'From \*\*Smart IO\*\*, drag `pico_lcd_init`': 'From **Smart Display**, drag `pico_lcd_init`',
        r'From \*\*Smart IO\*\*, drag `pico_lcd_print`': 'From **Smart Display**, drag `pico_lcd_print`',
        
        # Also catch the "Timing" variants before they get converted or if they already were
        r'From \*\*Timing\*\*, drag `pico_tm1637_init`': 'From **Smart Display**, drag `pico_tm1637_init`',
        r'From \*\*Timing\*\*, drag `pico_tm1637_show`': 'From **Smart Display**, drag `pico_tm1637_show`',
        r'From \*\*Timing\*\*, drag `pico_tm1637_colon`': 'From **Smart Display**, drag `pico_tm1637_colon`',
        r'From \*\*Timing\*\*, drag `pico_tm1637_brightness`': 'From **Smart Display**, drag `pico_tm1637_brightness`',
        r'From \*\*Timing\*\*, drag `pico_lcd_init`': 'From **Smart Display**, drag `pico_lcd_init`',
        r'From \*\*Timing\*\*, drag `pico_lcd_print`': 'From **Smart Display**, drag `pico_lcd_print`',
    }
    
    changed = False
    for pattern, replacement in mapping.items():
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            print(f"  Applied: {pattern} -> {replacement}")
            changed = True
            
    if changed:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"  [OK] Saved changes to {file_path.name}")
    else:
        print("  No changes needed.")

if __name__ == "__main__":
    docs_dir = Path(r"d:\MFF\Pico\Documentation")
    files = ["Docs_0001_0100.md", "Docs_0101_0200_FINAL.md"]
    for f in files:
        full_path = docs_dir / f
        if full_path.exists():
            fix_categories(full_path)
