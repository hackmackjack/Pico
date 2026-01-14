import os

def append_51_100():
    target_file = r'd:\MFF\Pico\Documentation\Docs_0501_0600.md'
    
    batches = """# 🌡️ Batch 56: Sensors 1

---

## 1. Project 0551: Temperature Basics
---
## 1. Project 0552: Humidity Reading
---
## 1. Project 0553: Light Intensity
---
## 1. Project 0554: Sound Detection
---
## 1. Project 0555: Ultrasonic Distance
---
## 1. Project 0556: PIR Motion
---
## 1. Project 0557: Touch Sensing
---
## 1. Project 0558: Joystick Control
---
## 1. Project 0559: Potentiometer Dial
---
## 1. Project 0560: Mastering Sensors

---

# 🌡️ Batch 57: Sensors 2

---

## 1. Project 0561: Pressure Reading
---
## 1. Project 0562: Altitude Sensing
---
## 1. Project 0563: Accelerometer Basics
---
## 1. Project 0564: Gyroscope Motion
---
## 1. Project 0565: Compass Bearing
---
## 1. Project 0566: IR Remote Control
---
## 1. Project 0567: RFID Scanning
---
## 1. Project 0568: Heart Rate Sensing
---
## 1. Project 0569: Color Detection
---
## 1. Project 0570: Mastering Complex Sensors

---

# 🔗 Batch 58: I2C Devices

---

## 1. Project 0571: I2C LCD Basics
---
## 1. Project 0572: Custom Characters LCD
---
## 1. Project 0573: RTC Clock Setting
---
## 1. Project 0574: RTC Alarm
---
## 1. Project 0575: 7-Segment Display I2C
---
## 1. Project 0576: 8x8 Matrix I2C
---
## 1. Project 0577: Keypad Scanning
---
## 1. Project 0578: EEPROM Memory
---
## 1. Project 0579: Digital Potentiometer
---
## 1. Project 0580: I2C Mastery

---

# 📡 Batch 59: Communication

---

## 1. Project 0581: UART Basics
---
## 1. Project 0582: SPI Communication
---
## 1. Project 0583: Wireless NRF24
---
## 1. Project 0584: Bluetooth Low Energy
---
## 1. Project 0585: WebSocket Client
---
## 1. Project 0586: MQTT Messaging
---
## 1. Project 0587: Flash Memory Logging
---
## 1. Project 0588: Multi-Pico Link
---
## 1. Project 0589: HID Keyboard Emulation
---
## 1. Project 0590: Communication Mastery

---

# 🏆 Batch 60: Mastery & Beyond

---

## 1. Project 0591: Smart Home Hub
---
## 1. Project 0592: Weather Station
---
## 1. Project 0593: Handheld Console
---
## 1. Project 0594: Mini Robot Car
---
## 1. Project 0595: Security System
---
## 1. Project 0596: Greenhouse Controller
---
## 1. Project 0597: Digital Oscilloscope
---
## 1. Project 0598: Audio Player
---
## 1. Project 0599: AI Edge Vision
---
## 1. Project 0600: Final Capstone Project

---
"""
    
    with open(target_file, 'a', encoding='utf-8') as f:
        f.write(batches)
    print("All headers 0501-0600 established.")

if __name__ == "__main__":
    append_51_100()
