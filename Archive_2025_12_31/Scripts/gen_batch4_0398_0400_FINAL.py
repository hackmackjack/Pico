# BATCH 4 (FINAL): Generate Full Elite Documentation for Projects 0398-0400

target_file = r'd:\MFF\Pico\Documentation\Docs_0301_0400.md'

batch4_content = r'''
## 1️⃣ Project 0398: File System 2 - Password Log

### 2️⃣ Learning Objective
Create an encrypted-style log where characters are shifted before saving. You will learn about basic data obfuscation and simple encryption techniques.

### 3️⃣ Concepts Introduced
*   **Caesar Cipher**: Shifting letters by +N positions before writing them to a file to hide information from plain sight.
*   **Reversible Encoding**: Ensuring data can be decoded back to original form.
*   **Security Awareness**: Understanding this is obfuscation, NOT real encryption.

### 4️⃣ Hardware Required
*   **Pico**
*   **Button** (to trigger password save)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Button** | GP14 | PULL_DOWN |

### 6️⃣ Blocks Used

🔹 **String Manipulation**
*   **Category:** Text

🔹 **ASCII/Char Conversion**
*   **Category:** Text

🔹 **File Write**
*   **Category:** File System

### 7️⃣ Variables & State
*   **password**: Plain-text password (e.g., "hello").
*   **shiftKey**: Number of positions to shift (e.g., 3).
*   **encodedPassword**: Shifted result.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **Variables**, drag `set [shiftKey] to [3]`.
        *   **Snap** into setup block.
    *   From **Inputs**, drag `Setup Button pin:[14] as PULL_DOWN`.
        *   **Snap** below.

*   **B. Main Loop Phase**
    *   **Encode Password**:
        *   From **Logic**, drag `if [digital read pin 14] then`.
            *   **Snap** into loop.
            *   Inside:
                *   From **Variables**, drag `set [password] to ["secret123"]`.
                    *   **Snap** inside.
                *   From **Text**, drag `set [encodedPassword] to [""]`.
                *   From **Loops**, drag `for each [char] in [password]`.
                    *   **Snap** below.
                    *   Inside:
                        *   From **Text**, drag `set [asciiVal] to [ord(char)]`.
                            *   **Snap** inside.
                        *   From **Math**, drag `set [shiftedVal] to [asciiVal + shiftKey]`.
                            *   **Snap** below.
                        *   From **Text**, drag `set [shiftedChar] to [chr(shiftedVal)]`.
                            *   **Snap** below.
                        *   From **Text**, drag `append [shiftedChar] to [encodedPassword]`.
                            *   **Snap** below.
    *   **Save Encoded**:
        *   From **File System**, drag `write [encodedPassword] to "passwords.enc"`.
            *   **Snap** below.
        *   From **Console**, drag `print [Password encoded and saved]`.
            *   **Snap** below.
    *   **Decode Password** (for verification):
        *   From **File System**, drag `set [encodedPassword] to [read from "passwords.enc"]`.
        *   Use same loop with `chr(ord(char) - shiftKey)` to decode.

### 9️⃣ Execution Flow (Plain English)

When the button is pressed, the program takes a password string like "secret123". For each character, it finds the ASCII value (e.g., 's' = 115), adds the shift key (115 + 3 = 118), and converts back to a character ('v'). The result "vhfuhw456" is saved to "passwords.enc". To retrieve the original, subtract the shift key from each character. This provides basic obfuscation but is NOT secure against determined attackers.

### 🔟 Generated Code (Reference Only)

```python
import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
SHIFT_KEY = 3

def encode(text, shift):
    result = ""
    for char in text:
        result += chr(ord(char) + shift)
    return result

def decode(text, shift):
    result = ""
    for char in text:
        result += chr(ord(char) - shift)
    return result

while True:
    if button.value():
        password = "secret123"
        encoded = encode(password, SHIFT_KEY)
        
        with open('passwords.enc', 'w') as f:
            f.write(encoded)
        
        print(f'Password encoded: {encoded}')
        
        # Verify decoding
        with open('passwords.enc', 'r') as f:
            loaded = f.read()
        
        decoded = decode(loaded, SHIFT_KEY)
        print(f'Decoded: {decoded}')
        
        time.sleep(1)
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Non-Printable Characters**: If shifting produces ASCII values >127, characters may not display correctly. Use modulo 256 or restrict to alphanumeric characters.
*   **False Sense of Security**: Caesar cipher is trivially broken. For real security, use `hashlib` for password hashing.

### 1️⃣2️⃣ Try This Next

*   **Variable Shift**: Change the shift key based on the day of the week (e.g., Monday = 1, Tuesday = 2).
*   **Base64 Encoding**: Use Python's `binascii.b2a_base64()` for a more standard obfuscation method.

---

## 1️⃣ Project 0399: File System 2 - Web File Browser

### 2️⃣ Learning Objective
Combine networking and storage to serve file contents over Wi-Fi. You will learn about full-stack embedded development and remote file access.

### 3️⃣ Concepts Introduced
*   **File Streaming**: Reading a file's content line-by-line and sending it directly into a web request.
*   **Directory Listing**: Using `os.listdir()` to show available files.
*   **Download Links**: Creating hyperlinks that serve file contents.

### 4️⃣ Hardware Required
*   **Pico W**

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **Wi-Fi** | Built-in | Pico W |

### 6️⃣ Blocks Used

🔹 **Directory List**
*   **Category:** File System

🔹 **File Read**
*   **Category:** File System

🔹 **Socket Send**
*   **Category:** Networking

### 7️⃣ Variables & State
*   **fileList**: List of all files in storage.
*   **selectedFile**: File requested by the user.

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   Connect to Wi-Fi and start socket server.

*   **B. Main Loop Phase**
    *   **Accept Connection**:
        *   From **Networking**, drag `wait for client connection`.
            *   **Snap** into loop.
        *   From **Networking**, drag `set [request] to [receive 1024 bytes]`.
            *   **Snap** below.
    *   **Parse Request**:
        *   From **Logic**, drag `if [request] contains [/list] then`.
            *   **Snap** below.
            *   Inside:
                *   From **File System**, drag `set [fileList] to [os.listdir()]`.
                    *   **Snap** inside.
                *   From **Text**, drag `build HTML page with file links`.
                *   From **Networking**, drag `send [HTML page]`.
        *   From **Logic**, drag `if [request] contains [/file?name=] then`.
            *   **Snap** below.
            *   Inside:
                *   From **Text**, drag `extract filename from URL`.
                *   From **File System**, drag `read file [filename]`.
                *   From **Networking**, drag `send [HTTP/1.1 200 OK\n\n{file content}]`.

### 9️⃣ Execution Flow (Plain English)

When you navigate to `http://<pico_ip>/list`, the server lists all files stored on the Pico as clickable links. Clicking a link like `log.csv` navigates to `/file?name=log.csv`, which triggers the server to read that file's contents and send them back to the browser. This creates a simple file manager accessible from any device on the network.

### 🔟 Generated Code (Reference Only)

```python
import network
import socket
import os

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
while not wlan.isconnected(): pass

s = socket.socket()
s.bind(('', 80))
s.listen(1)

print(f"File browser running at {wlan.ifconfig()[0]}")

def build_file_list_html():
    files = os.listdir()
    html = "<html><body><h1>File Browser</h1><ul>"
    for file in files:
        html += f'<li><a href="/file?name={file}">{file}</a></li>'
    html += "</ul></body></html>"
    return html

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    if '/list' in request:
        html = build_file_list_html()
        conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n' + html)
    
    elif '/file?name=' in request:
        try:
            filename = request.split('/file?name=')[1].split(' ')[0]
            with open(filename, 'r') as f:
                content = f.read()
            conn.send('HTTP/1.1 200 OK\nContent-Type: text/plain\n\n' + content)
        except OSError:
            conn.send('HTTP/1.1 404 Not Found\n\nFile not found')
    
    else:
        conn.send('HTTP/1.1 200 OK\n\nGo to /list to see files')
    
    conn.close()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Binary Files**: Reading binary files (images, etc.) with `'r'` mode will fail. Use `'rb'` and send as bytes.
*   **Security Risk**: This allows anyone on the network to read ALL files. Add authentication (Project 0389) for production use.

### 1️⃣2️⃣ Try This Next

*   **File Upload**: Add a form that allows uploading new files to the Pico.
*   **Delete Function**: Add `/delete?name=X` endpoint to remove files remotely.

---

## 1️⃣ Project 0400: Mastering File System

### 2️⃣ Learning Objective
Perform a full "System Backup" simulation by copying contents between internal storage and an external SD card (if available) or virtual partition. You will learn about bulk data migration and file system management.

### 3️⃣ Concepts Introduced
*   **Disk-to-Disk Transfer**: The logic of reading a block from File A and writing it to File B.
*   **Backup Verification**: Comparing source and destination to ensure data integrity.
*   **Final Master Test**: Integrating all logging and storage skills into a robust, crash-proof system.

### 4️⃣ Hardware Required
*   **Pico**
*   **SD Card Module** (Optional)

### 5️⃣ Wiring / Interfaces

| Component | Pico Pin | Notes |
| :--- | :--- | :--- |
| **SD Card CS** | GP17 | Chip Select (if using SPI SD) |
| **SD Card MOSI** | GP19 | SPI Data Out |
| **SD Card MISO** | GP16 | SPI Data In |
| **SD Card SCK** | GP18 | SPI Clock |

### 6️⃣ Blocks Used

🔹 **Directory List**
*   **Category:** File System

🔹 **File Read/Write**
*   **Category:** File System

🔹 **String Join**
*   **Category:** Text

### 7️⃣ Variables & State
*   **fileList**: All files to backup.
*   **backupPath**: Destination folder (e.g., `/sd/backup/`).

### 8️⃣ Step-by-Step Guide

*   **A. Initialization Phase**
    *   From **File System**, drag `set [backupPath] to ["/sd/backup/"]`.
        *   **Snap** into setup block.
    *   From **File System**, drag `if NOT directory exists [backupPath] then`.
        *   **Snap** below.
        *   Inside: From **File System**, drag `create directory [backupPath]`.

*   **B. Main Loop (Backup Process)**
    *   **List Files**:
        *   From **File System**, drag `set [fileList] to [os.listdir("/")]`.
            *   **Snap** into main block.
    *   **Copy Each File**:
        *   From **Loops**, drag `for each [filename] in [fileList]`.
            *   **Snap** below.
            *   Inside:
                *   From **File System**, drag `set [sourceContent] to [read from filename]`.
                    *   **Snap** inside.
                *   From **Text**, drag `set [destPath] to [backupPath + filename]`.
                    *   **Snap** below.
                *   From **File System**, drag `write [sourceContent] to [destPath]`.
                    *   **Snap** below.
                *   From **Console**, drag `print [Backed up {filename}]`.
                    *   **Snap** below.
    *   **Verification**:
        *   From **Loops**, drag `for each [filename] in [fileList]`.
            *   **Snap** below.
            *   Inside:
                *   From **File System**, drag `compare [source] and [backup] files`.
                *   From **Logic**, drag `if files match then print [✓] else print [✗]`.

### 9️⃣ Execution Flow (Plain English)

The program scans the Pico's root directory and gets a list of all files. For each file, it reads the entire contents into memory, then writes an exact copy to a backup location (either an SD card or a designated folder). After all files are copied, it re-reads both the original and backup to verify the data matches byte-for-byte. This ensures no corruption occurred during the transfer. The entire file system is now safely duplicated.

### 🔟 Generated Code (Reference Only)

```python
import os

BACKUP_PATH = '/sd/backup/'

def backup_all_files():
    # Create backup directory if it doesn't exist
    try:
        os.mkdir(BACKUP_PATH)
    except OSError:
        pass  # Directory already exists
    
    # Get list of all files in root
    files = os.listdir('/')
    
    print(f'Backing up {len(files)} files...')
    
    for filename in files:
        try:
            # Skip directories
            if '.' not in filename:
                continue
            
            # Read source file
            with open(f'/{filename}', 'rb') as source:
                content = source.read()
            
            # Write to backup location
            backup_file = BACKUP_PATH + filename
            with open(backup_file, 'wb') as dest:
                dest.write(content)
            
            print(f'✓ Backed up: {filename}')
            
        except Exception as e:
            print(f'✗ Failed: {filename} - {e}')
    
    print('Backup complete!')

def verify_backup():
    files = os.listdir('/')
    errors = 0
    
    for filename in files:
        if '.' not in filename:
            continue
        
        try:
            with open(f'/{filename}', 'rb') as f1:
                original = f1.read()
            
            with open(BACKUP_PATH + filename, 'rb') as f2:
                backup = f2.read()
            
            if original == backup:
                print(f'✓ Verified: {filename}')
            else:
                print(f'✗ MISMATCH: {filename}')
                errors += 1
        except Exception as e:
            print(f'✗ Error verifying {filename}: {e}')
            errors += 1
    
    if errors == 0:
        print('All files verified successfully!')
    else:
        print(f'WARNING: {errors} files failed verification')

# Run backup and verification
backup_all_files()
verify_backup()
```

### 1️⃣1️⃣ Common Mistakes & Debug Tips

*   **Memory Overflow**: Reading large files entirely into RAM can crash the Pico. For files >100KB, use chunked reading (read 1KB at a time).
*   **No SD Card**: If no SD card is present, the backup will fail. Add error handling to detect this.

### 1️⃣2️⃣ Try This Next

*   **Incremental Backup**: Only copy files that have changed since the last backup (compare timestamps).
*   **Cloud Upload**: Combine with Wi-Fi to upload backups to a server instead of an SD card.
*   **Compression**: Use `gzip` to compress files before backing up to save space.

---

🎉 **CONGRATULATIONS!** You have completed all 100 projects (0301-0400) covering advanced embedded systems, networking, file systems, and real-world IoT applications! 🎉
'''

# Append to file
with open(target_file, 'a', encoding='utf-8') as f:
    f.write(batch4_content)

print("✅ BATCH 4 (FINAL) COMPLETE: Generated full 12-section Elite docs for Projects 0398-0400")
print("📊 Progress: 19/19 projects completed")
print("🎉 ALL PROJECTS 0301-0400 NOW 100% ELITE-COMPLIANT!")
