import os

def fix_batch_56_code():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Updates for Batch 56 (Arm) to remove placeholders
    replacements = {
        "while True: wave()": "while True:\n    servo.duty_u16(4000) # Left\n    time.sleep(0.2)\n    servo.duty_u16(6000) # Right\n    time.sleep(0.2)",
        "val = adc.read_u16()": "while True:\n    val = adc.read_u16()\n    # Map 0-65535 to 1000-9000\n    duty = int(1000 + (val/65535)*8000)\n    servo.duty_u16(duty)\n    time.sleep(0.01)",
        "sequence()": "while True:\n    base.duty_u16(3000) # Move\n    time.sleep(1)\n    grip.duty_u16(8000) # Grab\n    time.sleep(1)\n    base.duty_u16(6000) # Move\n    time.sleep(1)\n    grip.duty_u16(2000) # Drop",
        "points = []": "points = []\nwhile True:\n    if btn.value():\n        points.append(pot.read_u16())\n        time.sleep(0.5)\n    if play_btn.value():\n        for p in points:\n            servo.duty_u16(p)\n            time.sleep(0.5)",
        "if d < 10: stop()": "while True:\n    dist = read_sonar()\n    if dist < 10:\n        servo.duty_u16(0) # Stop\n    else:\n        run_arm()",
        "check_stall()": "current_sense = machine.ADC(27)\nwhile True:\n    if current_sense.read_u16() > 50000:\n         print('STALL!')\n         servo.deinit()",
        "launch()": "servo.duty_u16(2000) # Load\ntime.sleep(1)\nservo.duty_u16(8000) # Fire!",
        "sort()": "while True:\n    if color_sensor.read() == 'RED':\n        servo.duty_u16(3000) # Left\n    else:\n        servo.duty_u16(7000) # Right"
    }

    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_batch_56_code()
