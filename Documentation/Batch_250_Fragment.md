## 1. Project 2496: Optimized Professional Direct Memory Access (DMA) Algorithm

### 2. Learning Objective
Create an infinite "Ping-Pong" loop where DMA Channel 0 triggers Channel 1, and Channel 1 triggers Channel 0. Zero CPU usage.

### 3. Concepts Introduced
*   **Chaining**: Linking channels so one finishes and starts another.
*   **Double Buffer**: While Ch0 fills Buffer A, CPU processes Buffer B. Then swap.
*   **Automation**: The engine runs forever once started.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Bitwise, drag `set_mask`**
*   **from Variables, drag `global_array`**

### 7. Variables
*   **buf_a**, **buf_b** (Lists)

### 8. Step-by-Step Guide

**A. Config Ch0**
1.  **Dest**: Buffer A.
2.  **Chain To**: Ch1.

**B. Config Ch1**
1.  **Dest**: Buffer B.
2.  **Chain To**: Ch0.

**C. Start**
1.  **Trigger**: Ch0.
2.  **Result**: It never stops. Pumping data forever.

### 9. Execution Flow
1.  **T=0**: Ch0 Active. Ch1 Idle.
2.  **T=100**: Ch0 Done. Triggers Ch1. Ch0 Idle.
3.  **T=200**: Ch1 Done. Triggers Ch0.
4.  **CPU**: Sleeps deeply.

### 10. Generated Code
```python
# Pseudo-code for Chain setup
# CH0_CTRL: CHAIN_TO = 1
# CH1_CTRL: CHAIN_TO = 0
```

### 11. Common Mistakes
*   **Infinite Loop without Exit**: If you don't have a way to stop it (e.g. CPU intervention), it runs until power loss.
*   **Bus Contention**: If DMA is using 100% bandwidth, the CPU might stall waiting for RAM. Priority settings in `CTRL` helper here.

### 12. Try This Next
*   **LED PWM**: Use Ping-Pong DMA to feed a PIO State Machine for driving huge LED panels.
*   **DAC Waveform**: Generate a sine wave by feeding the PWM duty cycle register continuously.

---

## 1. Project 2497: Professional Direct Memory Access (DMA) Data Pipeline

### 2. Learning Objective
Implement "Scatter-Gather" (Control Blocks). The DMA reads its *own instructions* from RAM to reconfigure itself for complex tasks.

### 3. Concepts Introduced
*   **Control Block**: A struct `{ReadAddr, WriteAddr, Count, NextBlock}` stored in RAM.
*   **Self-Reprogramming**: The DMA engine copies the next block into its own registers.
*   **Complex Sequences**: Copy A->B, then C->D, then E->F, then Stop.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Lists, drag `create_list`**
*   **from Memory, drag `address_of`**

### 7. Variables
*   **control_blocks** (List)

### 8. Step-by-Step Guide

**A. Create Blocks**
1.  Block 1: Transfer "Hello" to UART. Chain to Block 2.
2.  Block 2: Transfer "World" to UART. Chain to Block 3.
3.  Block 3: Stop (Null Trigger).

**B. Config DMA**
1.  **Master**: Ch1 copies Block 1 to Ch0 Registers.
2.  **Worker**: Ch0 executes Block 1. Triggers Ch1 when done.

### 9. Execution Flow
1.  **Start**: Ch1 loads Block 1.
2.  **Run**: Ch0 prints "Hello".
3.  **Chain**: Ch0 triggers Ch1.
4.  **Reload**: Ch1 loads Block 2.
5.  **Run**: Ch0 prints "World".

### 10. Generated Code
```python
# Scatter Gather is advanced. One channel (Ch1) acts as the Manager.
# It copies [READ, WRITE, COUNT, CTRL] from RAM -> DMA_BASE of Ch0.
# Ch0 performs the actual data move.
```

### 11. Common Mistakes
*   **Infinite Recursion**: Pointing Block A to Block B, and Block B to Block A creates a loop. (Sometimes desired, but dangerous if unintentional).
*   **Memory alignment**: Control blocks must be aligned to 16 bytes for efficiency (Move all 4 registers in 4 cycles).

### 12. Try This Next
*   **Sprite Engine**: Use Scatter-Gather to copy 50 different small images (Sprites) to the Framebuffer for a game.
*   **Playlist**: DMA plays Song A, then Song B, then Song C automatically.

---

## 1. Project 2498: Secure Professional Direct Memory Access (DMA) Interface

### 2. Learning Objective
Use the DMA to "Scrub" (Secure Erase) a memory region faster than the CPU can. Protection against Cold Boot attacks.

### 3. Concepts Introduced
*   **Memory Bandwidth**: DMA saturates the bus (e.g., 4GB/s peak on some chips, ~500MB/s on Pico).
*   **Fixed Source**: Reading from a single "Zero" register and spraying it over a range.
*   **Sanitization**: Wiping buffers after use.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Bitwise, drag `write_register`**
*   **from Variables, drag `global_var`**

### 7. Variables
*   **secret_buffer** (List)

### 8. Step-by-Step Guide

**A. Setup**
1.  **Zero Var**: `z = 0`.
2.  **Target**: `secret_buffer` (10KB).

**B. DMA Config**
1.  **Read Addr**: Address of `z`. (No Increment).
2.  **Write Addr**: Address of `buffer`. (Increment).
3.  **Count**: 10240.
4.  **Data Size**: 32-bit (Write 4 zeros at once).

### 9. Execution Flow
1.  **Trigger**: Panic Button pressed.
2.  **DMA**: Blasts 10,000 zeros into RAM.
3.  **Speed**: Takes ~20 microseconds.
4.  **Result**: Data is gone before the attacker can say "Hack".

### 10. Generated Code
```python
zero_src = ustruct.pack("I", 0)

def fast_wipe(target_addr, length):
    # Setup DMA to copy 'zero_src' repeatedly to 'target_addr'
    machine.mem32[CH0_READ_ADDR] = uctypes.addressof(zero_src)
    machine.mem32[CH0_WRITE_ADDR] = target_addr
    machine.mem32[CH0_TRANS_COUNT] = length // 4
    
    # NO_INCR_READ, INCR_WRITE, SIZE_WORD
    ctrl = 0x00000000 | (1 << 4) | (2 << 2) | 1
    machine.mem32[CH0_CTRL_TRIG] = ctrl
```

### 11. Common Mistakes
*   **Wiping Code**: Be careful not to wipe the *instructions* currently running, or the CPU will crash instantly.
*   **Wiping Stack**: Don't wipe the stack pointer addresses while inside a function call.

### 12. Try This Next
*   **Pattern Fill**: Fill memory with `0xDEADBEEF` to detect buffer overflows later (Memory Debugging).
*   **Verified Wipe**: DMA Wipe, then DMA Compare (Sniffer) to prove it's zero.

---

## 1. Project 2499: Multi-Threaded Professional Direct Memory Access (DMA)

### 2. Learning Objective
Manage a shared DMA Channel between two CPU cores. Core 0 wants to move Audio, Core 1 wants to move Video. Who wins?

### 3. Concepts Introduced
*   **Resource Arbitration**: "Channel 0 is taken. Use Channel 1?"
*   **Dynamic Allocation**: Asking a driver "Give me *any* free channel".
*   **Mutex**: Locking the DMA Controller configuration registers.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Threading, drag `allocate_lock`**
*   **from Classes, drag `define_class`**

### 7. Variables
*   **dma_manager** (Object)

### 8. Step-by-Step Guide

**A. Manager Class**
1.  **State**: `in_use = [False, False, False...]`.
2.  **Method `alloc()`**:
    *   Lock. Find first `False`. Mark `True`. Unlock. Return ID.
3.  **Method `free(id)`**:
    *   Lock. Mark `False`. Unlock.

**B. Usage**
1.  **Core 0**: `ch = dma.alloc()`. Use it. `dma.free(ch)`.
2.  **Core 1**: `ch = dma.alloc()`. Use it. `dma.free(ch)`.

### 9. Execution Flow
1.  **Core 0**: Takes Ch0.
2.  **Core 1**: Requests Channel. Manager sees Ch0 busy. Gives Ch1.
3.  **Result**: No conflict. Both transfers run in parallel.

### 10. Generated Code
```python
class DMAManager:
    def __init__(self):
        self.mask = 0
        self.lock = _thread.allocate_lock()
        
    def allocate(self):
        with self.lock:
            for i in range(12):
                if not ((self.mask >> i) & 1):
                    self.mask |= (1 << i)
                    return DMA(i)
            raise RuntimeError("Out of DMA")
            
    def free(self, dma_obj):
        with self.lock:
            # Clear bit
            self.mask &= ~(1 << dma_obj.id)
```

### 11. Common Mistakes
*   **Leak**: Forgetting to `free()` a channel. Eventually the system runs out and crashes.
*   **Hardcoded IDs**: "I'll just use Channel 0". If a Library (e.g. SPI) uses Channel 0 internally, you break the library. Always use dynamic allocation.

### 12. Try This Next
*   **Priority**: Reserve Ch0/1 for Core 0 (High Priority), Ch2-11 for Core 1 (Low Priority).
*   **Claiming**: Check `machine.mem32[DMA_BASE]` to see which channels are *actually enabled* by hardware, ensuring you don't overwrite a running transfer.

---

## 1. Project 2500: Industrial Professional Direct Memory Access (DMA) Soluton

### 2. Learning Objective
Build a **Logic Analyzer**. Capture the state of 8 GPIO pins at 100MHz (10ns resolution) directly into RAM. Debug protocols like SPI or I2C.

### 3. Concepts Introduced
*   **GPIO Input Register**: Address `0xD0000004` (GPIO_IN) holds the live state of all pins.
*   **Pacing Timer**: Using a DMA Timer (TREQ) to sample at exactly 1MHz, 10MHz, etc.
*   **Post-Processing**: CPU analyzes the captured buffer after the event.

### 4. Hardware Required
*   **Raspberry Pi Pico W**
*   **Jumper Wire** (Signal Source)

### 5. Wiring / Interfaces
*   **GP0-7** (Probes)

### 6. Blocks Used
*   **from Bitwise, drag `read_register`**
*   **from Storage, drag `file_save`**

### 7. Variables
*   **capture_buf** (List)

### 8. Step-by-Step Guide

**A. Config**
1.  **Source**: `GPIO_IN` Register. (No Incr).
2.  **Dest**: `capture_buf`. (Incr).
3.  **Transfer Count**: 10,000 samples.
4.  **Timer**: Paced at 1 microsecond.

**B. Arm**
1.  **Status**: Waiting for Trigger.

**C. Trigger**
1.  **Manual**: `dma.start()`.
2.  **Result**: 10ms of history captured instantly.
3.  **Analyze**: Print buffer. "0x00, 0x01, 0x01, 0x00...".

### 9. Execution Flow
1.  **Event**: Sub-microsecond glitch on GP0.
2.  **DMA**: Captures it in the stream.
3.  **CPU**: "I see a spike at Sample #4096!".
4.  **Application**: Professional Debugging Tool.

### 10. Generated Code
```python
GPIO_IN = 0xD0000004
buf = bytearray(10000)

d = DMA(0)
d.config_source(GPIO_IN, incr=False)
d.config_dest(buf, incr=True)
d.set_pace(TREQ_TIMER0) # Setup Timer0 for 1MHz

print("Capturing...")
d.start()
d.wait()

print("Analyzing...")
# Scan buffer for edges
last = 0
for i, val in enumerate(buf):
    if val != last:
        print(f"Edge at {i}us: {val:08b}")
        last = val
```

### 11. Common Mistakes
*   **Sampling Rate**: DMA can copy at system clock speed (125MHz). If the signal changes faster than that, you miss it (Nyquist limit).
*   **RAM Limits**: 264KB RAM = ~264,000 samples (bytes). At 1MHz, that's 0.26 seconds of data. Use compression or triggers for longer events.

### 12. Try This Next
*   **Trigger**: Use PIO to wait for a specific pattern (e.g. I2C Start Condition) then trigger DMA.
*   **Export**: Save `.csv` file to SD card and open in Excel or Sigrok/PulseView.

---

