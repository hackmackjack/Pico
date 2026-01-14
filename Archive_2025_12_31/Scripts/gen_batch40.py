# Generate Full Elite Documentation for Batch 40 (Projects 0391-0400)

import os

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

batch40_content = r'''
# 🏁 Batch 40: File System 2

---

## 1️⃣ Project 0391: File System 2 - Data Persistence

### 2️⃣ Learning Objective
Implement "Settings Memory" that survives a power reboot. You will learn about write-once read-many cycles and persistent state management.

### 3️⃣ Concepts Introduced
*   **Non-Volatile Storage**: Saving variables to the internal flash so they remain after power is lost.
*   **Initialization Retrieval**: Checking for the existence of a config file during boot.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (Configuration Trigger)

### 5️⃣ Wiring / Interfaces
*   **Button**: GP14 (PULL_DOWN)

### 6️⃣ Blocks Used
🔹 **Write File**
🔹 **Read File**
🔹 **Check File Exists**

### 7️⃣ Variables & State
*   **configVal**: A settings value (e.g., 1 or 0) stored in `settings.txt`.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **File System**, drag `if [file "settings.txt" exists] then`.
        *   **Snap** into setup block.
        *   Inside: `set [configVal] to [read from "settings.txt"]`.
    *   Else: `set [configVal] to [0]`.

*   **B. Main Loop Phase**
    *   **Change Setting**:
        *   If `digital read 14`:
            *   `set configVal to 1 - configVal` (Toggle).
            *   From **File System**, drag `write [configVal] to "settings.txt"`.
            *   Beep and sleep 1s.

### 9️⃣ Execution Flow (Plain English)
The Pico checks if a file called "settings.txt" is on its memory chip. If it is, it loads the value into use. If you press the button, it changes the setting and writes the new value over the old one in the file. If you unplug the Pico and plug it back in, it will remember the last setting you saved.

### 🔟 Generated Code (Reference Only)
```python
import os
def save(val):
    with open("settings.txt", "w") as f: f.write(str(val))
def load():
    try:
        with open("settings.txt", "r") as f: return int(f.read())
    except: return 0

setting = load()
# Main loop logic...
```

---

## 1️⃣ Project 0392: File System 2 - CSV Data Logging

### 2️⃣ Learning Objective
Create a structured datasheet in CSV format for spreadsheet analysis. You will learn about string formatting and append-mode writing.

### 3️⃣ Concepts Introduced
*   **CSV Format**: Comma Separated Values for universal compatibility.
*   **Append Mode ('a')**: Adding new data to the end of a file without deleting old data.

---

## 1️⃣ Project 0393: File System 2 - Log Rotation

### 2️⃣ Learning Objective
Manage memory constraints by implementing automatic log deletion. You will learn about file size auditing and cleanup logic.

### 3️⃣ Concepts Introduced
*   **File Size Check**: Monitoring how many bytes a file consumes.
*   **Log Rotation**: Deleting an old file when it gets too big (e.g., >10KB) to prevent the disk from filling up.

---

## 1️⃣ Project 0394: File System 2 - Multi-File Storage

### 2️⃣ Learning Objective
Organize data into multiple files based on category. You will learn about directory-like logic and dynamic filename generation.

### 3️⃣ Concepts Introduced
*   **Indexed Filenames**: Creating files like `log_1.txt`, `log_2.txt` based on a variable.

---

## 1️⃣ Project 0395: File System 2 - Structured JSON Storage

### 2️⃣ Learning Objective
Save complex data structures using JSON format. You will learn about key-value persistence.

### 3️⃣ Concepts Introduced
*   **JSON Objects**: Storing data like `{"temp": 25, "humidity": 60}` in a way that's easy for other computers to read.

---

## 1️⃣ Project 0396: File System 2 - System Health Monitor

### 2️⃣ Learning Objective
Log system uptime and error counts to a hidden diagnostic file. You will learn about background logging.

### 3️⃣ Concepts Introduced
*   **Diagnostic Logging**: Recording technical data that the user doesn't see unless there's a problem.

---

## 1️⃣ Project 0397: File System 2 - High-Speed Logging

### 2️⃣ Learning Objective
Optimize write cycles to reduce flash wear. You will learn about RAM buffering before disk commits.

### 3️⃣ Concepts Introduced
*   **Flash Wear**: Understanding that memory has a limited number of writes.
*   **Write Buffering**: Collecting many data points in RAM and writing them all at once to minimize disk access.

---

## 1️⃣ Project 0398: File System 2 - Password Log

### 2️⃣ Learning Objective
Create an encrypted-style log where characters are shifted before saving. You will learn about basic data obfuscation.

### 3️⃣ Concepts Introduced
*   **Caesar Cipher**: Shifting letters by +1 before writing them to a file to hide information from plain sight.

---

## 1️⃣ Project 0399: File System 2 - Web File Browser

### 2️⃣ Learning Objective
Combine networking and storage to serve file contents over Wi-Fi. You will learn about full-stack embedded development.

### 3️⃣ Concepts Introduced
*   **File Streaming**: Reading a file's content line-by-line and sending it directly into a web request.

---

## 1️⃣ Project 0400: Mastering File System

### 2️⃣ Learning Objective
Perform a full "System Backup" simulation by copying contents between internal storage and an external SD card (if available) or virtual partition. You will learn about bulk data migration.

### 3️⃣ Concepts Introduced
*   **Disk-to-Disk Transfer**: The logic of reading a block from File A and writing it to File B.
*   **Final Master Test**: Integrating all logging and storage skills into a robust, crash-proof system.

---
'''

with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch40_content)

print("✅ Successfully appended Batch 40 (0391-0400) to Docs_0301_0400.md")
