# BATCH 3: Generate Full Elite Documentation for Projects 0393-0397

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

batch3_content = r'''
## 1️⃣ Project 0393: File System 2 - Log Rotation

### 2️⃣ Learning Objective
Manage memory constraints by implementing automatic log deletion. You will learn about file size auditing, cleanup logic, and storage management.

### 3️⃣ Concepts Introduced
*   **File Size Check**: Monitoring how many bytes a file consumes using `os.stat()`.
*   **Log Rotation**: Deleting an old file when it gets too big (e.g., >10KB) to prevent the disk from filling up.
*   **Conditional Deletion**: Using threshold logic to trigger cleanup.

### 4️⃣ Hardware Required
*   **Pico**
*   **Sensor** (Optional, for data generation)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Sensor** | GP15 | Optional |

### 6️⃣ Blocks Used

🔹 **File Size**
*   **Category:** File System

🔹 **Delete File**
*   **Category:** File System

🔹 **Logic Comparison**
*   **Category:** Logic

### 7️⃣ Variables & State
*   **logSize**: Size of the log file in bytes.
*   **maxSize**: Threshold for rotation (e.g., 10240 bytes = 10KB).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [maxSize] to [10240]`.
        *   **Snap** into setup block (10KB limit).

*   **B. Main Loop Phase**
    *   **Check File Size**:
        *   From **File System**, drag `if file "log.csv" exists then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **File System**, drag `set [logSize] to [size of "log.csv"]`.
                    *   **Snap** inside.
                *   From **Logic**, drag `if [logSize] > [maxSize] then`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Console**, drag `print [Log file too large ({logSize} bytes), rotating...]`.
                            *   **Snap** inside.
                        *   From **File System**, drag `delete file "log.csv"`.
                            *   **Snap** below.
                        *   From **File System**, drag `create file "log.csv" with header`.
                            *   **Snap** below.
    *   **Append New Data**:
        *   From **File System**, drag `append [data] to "log.csv"`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [60] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

Every loop iteration, the program checks the size of "log.csv". If it exceeds 10KB, the file is deleted and a fresh one is created with just the header row. This prevents the log from consuming all available storage. Data logged after rotation starts building a new file from scratch.

### 🔟 Generated Code (Reference Only)

```python
import os
import time

MAX_SIZE = 10240  # 10KB

def rotate_log():
    if 'log.csv' in os.listdir():
        file_size = os.stat('log.csv')[6]  # Size in bytes
        
        if file_size > MAX_SIZE:
            print(f'Log file too large ({file_size} bytes), rotating...')
            os.remove('log.csv')
            with open('log.csv', 'w') as f:
                f.write('Time,Temperature,Humidity\n')

while True:
    rotate_log()
    
    # Append new data
    data = f'{time.time()},25.0,60.0\n'
    with open('log.csv', 'a') as f:
        f.write(data)
    
    time.sleep(60)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Data Loss**: Rotation deletes all old data. To preserve it, rename the old file to `log_backup.csv` before creating a new one.
*   **Wrong Size**: `os.stat()[6]` returns size in bytes. For MB, divide by 1,048,576.

### 1️⃣2️⃣ Try This Next

*   **Numbered Backups**: Instead of deleting, rename to `log_1.csv`, `log_2.csv`, etc., and keep the last 5 files.
*   **Compression**: Use `gzip` to compress old logs before archiving.

---

## 1️⃣ Project 0394: File System 2 - Multi-File Storage

### 2️⃣ Learning Objective
Organize data into multiple files based on category or time. You will learn about directory-like logic and dynamic filename generation.

### 3️⃣ Concepts Introduced
*   **Indexed Filenames**: Creating files like `log_1.txt`, `log_2.txt` based on a variable.
*   **Daily/Hourly Logs**: Generating filename from current date/time.
*   **File Organization**: Structuring data for easy retrieval.

### 4️⃣ Hardware Required
*   **Pico**

### 5️⃣ Wiring / Interfaces
None required.

### 6️⃣ Blocks Used

🔹 **String Formatting**
*   **Category:** Text

🔹 **File Write**
*   **Category:** File System

🔹 **Time Functions**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **currentHour**: Hour of the day (0-23).
*   **filename**: Dynamically generated filename.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   None required.

*   **B. Main Loop Phase**
    *   **Get Current Hour**:
        *   From **Timing**, drag `set [currentHour] to [hour of day]`.
            *   **Snap** into loop.
    *   **Generate Filename**:
        *   From **Text**, drag `set [filename] to [log_{currentHour}.csv]`.
            *   **Snap** below.
    *   **Write Data**:
        *   From **File System**, drag `append [data] to [filename]`.
            *   **Snap** below.
    *   From **Timing**, drag `sleep [60] seconds`.
        *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program generates a filename based on the current hour (e.g., `log_14.csv` for 2 PM). All data logged during that hour goes into that file. When the hour changes, a new file is automatically created. This organizes logs by time period without manual intervention.

### 🔟 Generated Code (Reference Only)

```python
import time

while True:
    # Get current hour (0-23)
    current_time = time.localtime()
    current_hour = current_time[3]
    
    # Generate filename
    filename = f'log_{current_hour}.csv'
    
    # Append data
    data = f'{time.time()},25.0,60.0\n'
    with open(filename, 'a') as f:
        f.write(data)
    
    print(f'Data logged to {filename}')
    time.sleep(60)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **24 Files Created**: If running for 24 hours, you'll have 24 separate files. Plan storage accordingly.
*   **No RTC**: If the Pico doesn't have a real-time clock, `localtime()` may return incorrect values. Use uptime-based naming instead.

### 1️⃣2️⃣ Try This Next

*   **YYYYMMDD Format**: Use `log_20250129.csv` for daily logs instead of hourly.
*   **Auto-Archive**: At midnight, move all the previous day's files to an `archive/` folder.

---

## 1️⃣ Project 0395: File System 2 - Structured JSON Storage

### 2️⃣ Learning Objective
Save complex data structures using JSON format. You will learn about key-value persistence and serialization.

### 3️⃣ Concepts Introduced
*   **JSON Objects**: Storing data like `{"temp": 25, "humidity": 60}` in a way that's easy for other computers to read.
*   **Serialization**: Converting Python dictionaries to JSON strings.
*   **Deserialization**: Converting JSON strings back to Python objects.

### 4️⃣ Hardware Required
*   **Pico**
*   **Sensor** (Optional)

### 5️⃣ Wiring / Interfaces
None required.

### 6️⃣ Blocks Used

🔹 **JSON Dumps**
*   **Category:** Text (JSON)

🔹 **JSON Loads**
*   **Category:** Text (JSON)

🔹 **File Write/Read**
*   **Category:** File System

### 7️⃣ Variables & State
*   **settings**: Dictionary containing multiple configuration values.
*   **jsonString**: Serialized JSON representation.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [settings] to [{"brightness": 80, "alarm": True, "tempThreshold": 30}]`.
        *   **Snap** into setup block.
    *   **Save to JSON**:
        *   From **JSON**, drag `set [jsonString] to [json.dumps(settings)]`.
            *   **Snap** below.
        *   From **File System**, drag `write [jsonString] to "config.json"`.
            *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Load from JSON**:
        *   From **File System**, drag `set [jsonString] to [read from "config.json"]`.
            *   **Snap** into loop.
        *   From **JSON**, drag `set [settings] to [json.loads(jsonString)]`.
            *   **Snap** below.
        *   From **Console**, drag `print [Brightness: {settings['brightness']}]`.
            *   **Snap** below.

### 9️⃣ Execution Flow (Plain English)

The program creates a dictionary with 3 settings: brightness (80), alarm (True), and temperature threshold (30). It converts this to a JSON string like `{"brightness":80,"alarm":true,"tempThreshold":30}` and writes it to "config.json". Later, it reads the file, converts back to a Python dictionary, and accesses individual values like `settings['brightness']`. JSON is ideal for storing complex configurations that need to be read by other devices or software.

### 🔟 Generated Code (Reference Only)

```python
import json

# Create settings dictionary
settings = {
    "brightness": 80,
    "alarm": True,
    "temp_threshold": 30
}

# Save to JSON
with open('config.json', 'w') as f:
    json.dump(settings, f)

print('Settings saved to config.json')

# Load from JSON
with open('config.json', 'r') as f:
    loaded_settings = json.load(f)

print(f"Brightness: {loaded_settings['brightness']}")
print(f"Alarm: {loaded_settings['alarm']}")
print(f"Threshold: {loaded_settings['temp_threshold']}")
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Quote Errors**: JSON requires double quotes (`"key"`), not single quotes (`'key'`).
*   **Type Preservation**: JSON converts `True` to `true`. When reading back, it becomes Python `True` again automatically.

### 1️⃣2️⃣ Try This Next

*   **Nested Structures**: Store lists and sub-dictionaries: `{"users": [{"name": "Alice", "age": 30}]}`.
*   **Validation**: Check if required keys exist before accessing to prevent KeyErrors.

---

## 1️⃣ Project 0396: File System 2 - System Health Monitor

### 2️⃣ Learning Objective
Log system uptime and error counts to a hidden diagnostic file. You will learn about background logging and system monitoring.

### 3️⃣ Concepts Introduced
*   **Diagnostic Logging**: Recording technical data that the user doesn't see unless there's a problem.
*   **Error Tracking**: Counting exceptions and failures.
*   **Hidden Files**: Using filenames like `.diagnostics.txt` to indicate internal use.

### 4️⃣ Hardware Required
*   **Pico**

### 5️⃣ Wiring / Interfaces
None required.

### 6️⃣ Blocks Used

🔹 **Try/Except**
*   **Category:** Logic

🔹 **File Append**
*   **Category:** File System

🔹 **Time Functions**
*   **Category:** Timing

### 7️⃣ Variables & State
*   **errorCount**: Number of exceptions caught.
*   **uptime**: Time since boot.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [errorCount] to [0]`.
        *   **Snap** into setup block.
    *   From **Variables**, drag `set [bootTime] to [time()]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Error Tracking**:
        *   From **Logic**, drag `try:`.
            *   **Snap** into loop.
            *   Inside: [Main program logic]
        *   From **Logic**, drag `except Exception as e:`.
            *   **Snap** below.
            *   Inside:
                *   From **Variables**, drag `change [errorCount] by [1]`.
                    *   **Snap** inside.
                *   From **File System**, drag `append [{time()}: Error #{errorCount} - {str(e)}\n] to ".diagnostics.txt"`.
                    *   **Snap** below.
    *   **Periodic Health Log**:
        *   From **Timing**, drag `if [time() % 3600] = [0] then`.
            *   **Snap** below (every hour).
            *   Inside:
                *   From **Variables**, drag `set [uptime] to [time() - bootTime]`.
                *   From **File System**, drag `append [Uptime: {uptime}s, Errors: {errorCount}\n] to ".diagnostics.txt"`.

### 9️⃣ Execution Flow (Plain English)

The program wraps the main logic in a try/except block. Any error that occurs is logged to ".diagnostics.txt" with a timestamp and error count. Additionally, every hour (3600 seconds), it logs the current uptime and total error count. This creates an invisible audit trail that can be reviewed if the device behaves unexpectedly.

### 🔟 Generated Code (Reference Only)

```python
import time

error_count = 0
boot_time = time.time()

def log_diagnostic(message):
    with open('.diagnostics.txt', 'a') as f:
        f.write(f'{time.time()}: {message}\n')

while True:
    try:
        # Main program logic (simulated error for demo)
        result = 10 / 0  # This will raise ZeroDivisionError
        
    except Exception as e:
        error_count += 1
        log_diagnostic(f'Error #{error_count} - {str(e)}')
    
    # Hourly health check
    uptime = time.time() - boot_time
    if int(uptime) % 3600 == 0:
        log_diagnostic(f'Health: Uptime={int(uptime)}s, Errors={error_count}')
    
    time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **File Gets Big**: Diagnostic logs can grow quickly. Implement rotation similar to Project 0393.
*   **Infinite Errors**: If an error occurs inside the logging code itself, it can create a crash loop. Always test logging separately.

### 1️⃣2️⃣ Try This Next

*   **Memory Usage**: Log `gc.mem_free()` to track available RAM over time.
*   **Remote Upload**: On Wi-Fi, automatically send the diagnostic file to a server when errors exceed 10.

---

## 1️⃣ Project 0397: File System 2 - High-Speed Logging

### 2️⃣ Learning Objective
Optimize write cycles to reduce flash wear. You will learn about RAM buffering before disk commits and performance optimization.

### 3️⃣ Concepts Introduced
*   **Flash Wear**: Understanding that memory has a limited number of writes (~10k-100k cycles).
*   **Write Buffering**: Collecting many data points in RAM and writing them all at once to minimize disk access.
*   **Flush Strategy**: Balancing between data safety (frequent writes) and wear reduction (batched writes).

### 4️⃣ Hardware Required
*   **Pico**
*   **High-Frequency Sensor** (e.g., accelerometer at 100Hz)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Accelerometer** | I2C | Optional |

### 6️⃣ Blocks Used

🔹 **List Append**
*   **Category:** Variables

🔹 **List Length**
*   **Category:** Variables

🔹 **File Write**
*   **Category:** File System

### 7️⃣ Variables & State
*   **buffer**: List holding data in RAM before writing.
*   **bufferSize**: Maximum number of entries before flushing (e.g., 100).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [buffer] to [[]]`.
        *   **Snap** into setup block (empty list).
    *   From **Variables**, drag `set [bufferSize] to [100]`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Collect Data**:
        *   From **Sensors**, drag `read sensor`.
            *   **Snap** into loop.
        *   From **Variables**, drag `append [sensorValue] to [buffer]`.
            *   **Snap** below.
    *   **Check Buffer**:
        *   From **Logic**, drag `if [length of buffer] >= [bufferSize] then`.
            *   **Snap** below.
            *   Inside:
                *   From **File System**, drag `append [join(buffer, "\n")] to "data.txt"`.
                    *   **Snap** inside.
                *   From **Variables**, drag `set [buffer] to [[]]`.
                    *   **Snap** below (clear buffer).
                *   From **Console**, drag `print [Flushed {bufferSize} entries to disk]`.
                    *   **Snap** below.
    *   From **Timing**, drag `sleep [0.01] seconds`.
        *   **Snap** below (100Hz sampling).

### 9️⃣ Execution Flow (Plain English)

The program reads sensor data at 100Hz (every 10ms) and stores each reading in a RAM list called `buffer`. Once the buffer contains 100 entries, all 100 are written to "data.txt" in a single file operation. This reduces writes from 100 individual operations to 1 batched operation, extending flash memory lifespan by 100x while capturing high-frequency data.

### 🔟 Generated Code (Reference Only)

```python
import time

buffer = []
BUFFER_SIZE = 100

def flush_buffer():
    global buffer
    if len(buffer) > 0:
        with open('data.txt', 'a') as f:
            f.write('\n'.join(map(str, buffer)) + '\n')
        count = len(buffer)
        buffer = []
        print(f'Flushed {count} entries to disk')

while True:
    # Simulate sensor reading
    sensor_value = time.ticks_ms()
    buffer.append(sensor_value)
    
    # Flush when buffer is full
    if len(buffer) >= BUFFER_SIZE:
        flush_buffer()
    
    time.sleep(0.01)  # 100Hz
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Data Loss on Crash**: If the Pico loses power before the buffer flushes, up to 99 readings are lost. For critical data, flush more frequently (e.g., every 10 entries).
*   **Memory Overflow**: Large buffers can consume too much RAM. Monitor with `gc.mem_free()`.

### 1️⃣2️⃣ Try This Next

*   **Time-Based Flush**: Flush every 5 seconds OR when buffer is full, whichever comes first.
*   **Compression**: Before writing, compress the buffer data to save even more space.

---
'''

# Append to file
with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch3_content)

print("✅ BATCH 3 COMPLETE: Generated full 12-section Elite docs for Projects 0393-0397")
print("📊 Progress: 16/19 projects completed")
print("📋 Remaining: 3 projects (0398-0400)")
