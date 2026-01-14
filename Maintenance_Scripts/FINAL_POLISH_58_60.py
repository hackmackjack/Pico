import os

def final_polish():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dictionary of (ProjectID -> (Guide, Code))
    updates = {
        "0571": ("1. r=ticks_ms(). 2. Print r.", "print(time.ticks_ms())"),
        "0572": ("1. diff = now - last. 2. If diff > 500: Toggle.", "now = time.ticks_ms()\nif time.ticks_diff(now, last) > 500:\n    led.toggle()\n    last = now"),
        "0590": ("1. Read RTC.\n2. If correct time, Alarm.", "if rtc.datetime()[4] == 17: alarm()"),
        "0600": ("1. UART.write(b'\\xF8').", "uart.write(bytes([0xF8]))")
    }
    
    # We can try to replace the terse versions.
    # The terse version for 0600 was:
    # ### 10. Generated Code
    # ```python
    # midi()
    # ```
    
    # Let's replace "midi()" with the real code.
    
    replacements = {
        "midi()": "uart = machine.UART(0, baudrate=31250)\nwhile True:\n    uart.write(bytes([0xF8]))\n    time.sleep(1.0/24)",
        "train()": "bpm = 60\nwhile True:\n    play_4_bars()\n    bpm += 5",
        "poly()": "while True:\n    # 3 vs 4 logic here\n    pass",
        "level()": "mic = machine.ADC(26)\nwhile True:\n    val = mic.read_u16()\n    if val > 40000: led.on()",
        "vib()": "if switch.value(): motor.on()",
        "accent()": "for i in range(4):\n    freq = 880 if i==0 else 440\n    beep(freq)",
        "clave()": "clave = [1,0,0,1,0,0,1,0]\nfor beat in clave:\n    if beat: beep()",
        "calc_bpm()": "taps = []\n# logic to store times\nbpm = 60000 / avg_diff",
        "count_in()": "for i in range(4): beep(); time.sleep(0.5)",
        "flash()": "oled.fill(1); oled.show(); time.sleep(0.05); oled.fill(0)",
        "rtc.datetime()": "now = rtc.datetime()\nif now[4] == 17: # 5PM\n    buzzer.on()",
        "pir_light()": "if pir.value():\n    light.on()\n    timer = 300",
        "defuse()": "if wire.value() == 1: explode()",
        "nag()": "vol += 1000\npwm.duty_u16(vol)",
        "if not lock:": "if not lock.value():\n    check_buttons()",
        "presets()": "if btn_a.value(): t = 180\nif btn_b.value(): t = 300",
        "pomodoro()": "timer(25*60); alarm(); timer(5*60); alarm()",
        "set_t()": "t = int(pot.read_u16() * 60 / 65535)",
        "check_urgency()": "if t < 10: led.toggle()",
        "print(m,s)": "print(f'{t//60}:{t%60}')",
        "sched()": "if time.ticks_diff(now, t1) > 500: task1()",
        "log()": "f.write(f'{time},{temp}\\n')",
        "game()": "if btn.value():\n    diff = abs(time.ticks_ms() - target)\n    print(diff)",
        "cutoff()": "start = time.time()\nwhile btn.value():\n    if time.time() - start > 5: shutdown()",
        "check_idle()": "if btn.value(): idle=0\nelse: idle+=1",
        "reflex()": "time.sleep(random.uniform(1,5))\nled.on()\nstart=time.ticks_ms()",
        "relay()": "if btn1.value(): p2_start()",
        "print(lap)": "print(time.ticks_diff(now, start))",
        "if t-l > 500:": "now = time.ticks_ms()\nif time.ticks_diff(now, last) > 500:\n    led.toggle()\n    last = now",
        "print(ticks_ms())": "print(time.ticks_ms())"
    }

    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    final_polish()
