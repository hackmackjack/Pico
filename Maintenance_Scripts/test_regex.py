
import re

text = """*   From **Smart IO**, drag Setup PWM pin:[13] (Red)."""
# Regex matching more flexibly
new_text = re.sub(r'drag Setup PWM pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', text)
print(f"Result 1: {new_text}")

# Testing regex with characters around
new_text = re.sub(r'drag Setup PWM pin:\[(\d+)\]', r'drag `pico_pwm`. Set Pin to \1', "*   From **Smart IO**, drag Setup PWM pin:[13] (Red).")
print(f"Result 2: {new_text}")
