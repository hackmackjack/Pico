import random

FILENAME = "PICO_2500_INDEX.md"

# --- THEMES & DOMAINS ---

ELEM_THEMES = [
    "LED Patterns", "Button Logic", "Sound & Music", "Simple Motors", "Traffic Lights", 
    "Night Light", "Doorball", "Reaction Game", "Counting Machine", "Morse Code",
    "Digital Art", "Animation", "Binary Counter", "Temperature Alarm", "Smart Fan",
    "Robotic Arm Basics", "OLED Shapes", "Stopwatch", "Kitchen Timer", "Metronome"
]

MIDDLE_THEMES = [
    "Ultrasonic Distance", "Servo Kinematics", "Light Sensing (LDR)", "Temp/Humidity (DHT)", 
    "Infrared Remote", "Keypad Security", "Joystick Control", "Motor Driver (L9110)", 
    "LCD Display (I2C)", "Data Logging", "Soil Moisture", "Reed Switch Alarm", 
    "Tilt Sensor", "Laser Tripwire", "Radar Screen", "Weather Station", "Digital Spirit Level"
]

HIGH_THEMES = [
    # Communication & IoT
    "WiFi (Connect)", "NTP Time Sync", "HTTP Server", "REST API Client", "MQTT IoT", 
    "Cloud Dashboard", "Bluetooth (BLE) Beacon", "BLE UART", "Pico-to-Pico Radio", 
    "Modbus Industrial Control", 
    
    # Advanced System Architecture
    "Multi-Core Threading", "Interrupts (IRQ)", "Direct Memory Access (DMA)", 
    "Watchdog Reliability", "Deep Sleep Power Saving", "File System (Data Logging)", 
    "CSV Data Rotation", "Non-Blocking Timers", "State Machine Architecture",
    
    # Advanced Algorithms
    "PID Speed Control", "PID Temp Control", "Motion Profiling (Ramp)", 
    "Sensor Fusion (IMU)", "Statistical Analysis (Edge)", "Data Compression (RLE)", 
    "Safety Interlocks", "Error Handling (Try/Except)", "Home Automation Logic", 
    "Telegram Bot API"
]

def get_batch_info(batch_id):
    # ELEMENTARY: Grades 3-5 (Batches 1-75)
    if batch_id <= 75:
        grade = "3-5 (Elementary)"
        level = "Remember/Understand" if batch_id < 30 else "Apply"
        theme = ELEM_THEMES[(batch_id - 1) % len(ELEM_THEMES)]
        # Add variation to reuse themes without exact duplicates
        variation = (batch_id - 1) // len(ELEM_THEMES) + 1
        title = f"{theme} {variation}"
        
    # MIDDLE: Grades 6-8 (Batches 76-150)
    elif batch_id <= 150:
        grade = "6-8 (Middle)"
        level = "Apply/Analyze"
        idx = batch_id - 76
        theme = MIDDLE_THEMES[idx % len(MIDDLE_THEMES)]
        variation = idx // len(MIDDLE_THEMES) + 1
        title = f"Advanced {theme} {variation}"

    # HIGH: Grades 9-12 (Batches 151-250)
    else:
        grade = "9-12 (High School)"
        level = "Evaluate/Create"
        idx = batch_id - 151
        theme = HIGH_THEMES[idx % len(HIGH_THEMES)]
        variation = idx // len(HIGH_THEMES) + 1
        title = f"Professional {theme} {variation}"
        
    return title, grade, level

def generate_index():
    content = "# 🗺️ Pico 2500: Master Curriculum Index\n\n"
    content += "This index defines the structure for all 250 Batches (2500 Projects).\n\n"
    content += "| Batch ID | Grade Band | Bloom's Level | Project Range | Theme / Focus |\n"
    content += "| :--- | :--- | :--- | :--- | :--- |\n"
    
    for b_id in range(1, 251):
        title, grade, level = get_batch_info(b_id)
        start_p = (b_id - 1) * 10 + 1
        end_p = b_id * 10
        p_range = f"{start_p:04d}-{end_p:04d}"
        
        content += f"| **{b_id}** | {grade} | {level} | `{p_range}` | {title} |\n"
        
    print(f"Generating {FILENAME}...")
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")

if __name__ == "__main__":
    generate_index()
