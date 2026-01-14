## Batch 250: Professional Direct Memory Access (DMA) 4 (9-12 (High School))

## 1. Project 2491: Professional Direct Memory Access (DMA) Driver Implementation

### 2. Learning Objective
Move a massive block of data (1KB) from one memory location to another in 5 microseconds, without the CPU lifting a finger.

### 3. Concepts Introduced
*   **DMA (Direct Memory Access)**: A specialized coprocessor dedicated to copying bytes.
*   **Registers**: Creating the command by writing to specific hardware addresses (`0x50000000`).
*   **Channels**: The RP2040 has 12 independent DMA channels.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Bitwise, drag `write_register`**
*   **from Lists, drag `create_list`**

### 7. Variables
*   **src_addr**, **dst_addr** (Numbers)

### 8. Step-by-Step Guide

**A. Setup Arrays**
1.  `src` = bytearray(1000). Fill with "A".
2.  `dst` = bytearray(1000). Fill with "B".

**B. Configure DMA (Channel 0)**
1.  **READ_ADDR**: Address of `src`.
2.  **WRITE_ADDR**: Address of `dst`.
3.  **TRANS_COUNT**: 1000.
4.  **CTRL_TRIG**: Enable, Incr Read, Incr Write, Data Size=8bit, Start!

**C. Verification**
1.  Wait.
2.  Check `dst[0]`. Should be "A".

### 9. Execution Flow
1.  **Command**: CPU writes 4 integers to the DMA Controller.
2.  **Action**: DMA Engine grabs the bus. Copies 1000 bytes.
3.  **CPU**: Can perform other tasks during this time.
4.  **Complete**: Copy finished.

### 10. Generated Code
```python
import uctypes, machine
import ustruct

# DMA Base
DMA_BASE = 0x50000000
CH0_READ_ADDR = DMA_BASE + 0x00
CH0_WRITE_ADDR = DMA_BASE + 0x04
CH0_TRANS_COUNT = DMA_BASE + 0x08
CH0_CTRL_TRIG = DMA_BASE + 0x0C

src = bytearray(b"Hello DMA World!")
dst = bytearray(len(src))

def start_dma():
    # Get physical addresses
    src_addr = uctypes.addressof(src)
    dst_addr = uctypes.addressof(dst)
    
    machine.mem32[CH0_READ_ADDR] = src_addr
    machine.mem32[CH0_WRITE_ADDR] = dst_addr
    machine.mem32[CH0_TRANS_COUNT] = len(src)
    
    # CTRL: Enable(1) + DATA_SIZE(0=Byte) + INCR_READ(1) + INCR_WRITE(1) + EN(1)
    # Bit 0=EN, 4=HIGH_PRIO, 11-20=Treq... simplistic 0x00... config
    ctrl = 0
    ctrl |= (1 << 0) # Enable
    ctrl |= (1 << 4) # Incr Write
    ctrl |= (1 << 5) # Incr Read
    
    machine.mem32[CH0_CTRL_TRIG] = ctrl

start_dma()
print(dst)
```

### 11. Common Mistakes
*   **Address Alignment**: Some DMA modes require addresses to be multiples of 4 (Word Aligned). Use `bytearray` which is usually safe.
*   **Cache Coherency**: The CPU cache might not know the RAM changed. MicroPython usually handles this, but in C++ it's a huge issue.

### 12. Try This Next
*   **Word Copy**: Copy 32-bit integers instead of bytes. 4x faster throughput.
*   **Chain**: Configuring Channel 0 to trigger Channel 1 when finished (Ping Pong).

---

## 1. Project 2492: Asynchronous Professional Direct Memory Access (DMA) Handler

### 2. Learning Objective
Start a long transfer (e.g., sending image to a display) and use `asyncio` to wait for completion.

### 3. Concepts Introduced
*   **Completion Interrupt**: The DMA fires an IRQ when `TRANS_COUNT` reaches 0.
*   **Event Loop Integration**: Setting an Async Flag from the DMA IRQ.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Async, drag `async_flag_wait`**
*   **from Bitwise, drag `set_bit`**

### 7. Variables
*   **dma_done** (Flag)

### 8. Step-by-Step Guide

**A. Configuration**
1.  **CTRL**: Enable IRQ (Bit 21 in `CTRL_TRIG`).
2.  **INTE0**: Enable DMA Channel 0 IRQ in the System Controller.

**B. Async Task**
1.  **Trigger**: Start DMA.
2.  **Await**: `dma_done.wait()`.
3.  **Finish**: Clean up or Start Next.

### 9. Execution Flow
1.  **Start**: CPU kicks off 100MB transfer (Simulated).
2.  **Sleep**: Async task yields. Other tasks run (Webserver, Blink).
3.  **Interrupt**: Transfer Done.
4.  **Wake**: Task resumes.

### 10. Generated Code
```python
import uasyncio

dma_event = uasyncio.ThreadSafeFlag()

# Simplified pseudo-code for interrupt setup
def dma_irq_handler(p):
    # Clear Interrupt Hardware Flag
    machine.mem32[DMA_BASE + 0x44] = (1 << 0) 
    dma_event.set()

async def transfer_task():
    print("Starting Transfer...")
    start_dma_with_irq()
    
    await dma_event.wait()
    print("Transfer Complete!")

# Note: Attaching Python ISR to DMA IRQ requires 
# low-level 'machine.mem32' manipulation of NVIC, 
# which is complex. This is a conceptual implementation.
```

### 11. Common Mistakes
*   **Hanging**: If you enable IRQ in DMA CTRL but forget to Enable it in the NVIC (Interrupt Controller), the CPU never wakes up.
*   **Clearing Flag**: You MUST clear the interrupt status bit in the handler, or it will fire infinitely (ISR Storm).

### 12. Try This Next
*   **LED**: Turn LED on during transfer, off when done.
*   **Timeout**: `wait_for(dma_event.wait(), 1.0)` in case the DMA hangs.

---

## 1. Project 2493: Object-Oriented Professional Direct Memory Access (DMA) Class

### 2. Learning Objective
Wrap the complex register addresses into a clean Python Class `DMAChannel(id)`.

### 3. Concepts Introduced
*   **Abstraction**: Hiding `0x50000000 + (id * 0x40)` math behind a constructor.
*   **API Design**: `channel.transfer(src, dst, len)`.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Classes, drag `define_class`**
*   **from Math, drag `hex_const`**

### 7. Variables
*   **ch0**, **ch1** (Objects)

### 8. Step-by-Step Guide

**A. Class `DMA`**
1.  **Init(id)**: Calc base address.
2.  **Method `enable()`**: Set CTRL bit 0.
3.  **Method `busy()`**: Read CTRL bit 24 (Busy flag).

**B. Usage**
1.  `d = DMA(0)`.
2.  `d.config(src, dst)`.
3.  `d.start()`.
4.  `while d.busy(): pass`.

### 9. Execution Flow
1.  **User**: Uses high-level methods.
2.  **Class**: Manipulates silicon registers.
3.  **Outcome**: Readable, Reusable code.

### 10. Generated Code
```python
class DMA:
    def __init__(self, channel_id):
        self.base = 0x50000000 + (channel_id * 0x40)
        self.read_reg = self.base + 0x00
        self.write_reg = self.base + 0x04
        self.count_reg = self.base + 0x08
        self.ctrl_reg = self.base + 0x0C
        
    def transfer(self, src_obj, dst_obj):
        src_addr = uctypes.addressof(src_obj)
        dst_addr = uctypes.addressof(dst_obj)
        length = len(src_obj)
        
        machine.mem32[self.read_reg] = src_addr
        machine.mem32[self.write_reg] = dst_addr
        machine.mem32[self.count_reg] = length
        
        # Trigger (Simplified default config)
        machine.mem32[self.ctrl_reg] = 0x001f8001 

d0 = DMA(0)
d0.transfer(buf_a, buf_b)
```

### 11. Common Mistakes
*   **Pointer Safety**: If `src_obj` is a temporary Python object, the GC might delete it *while* DMA is copying! Always keep a reference to buffers (`global buf`).
*   **Channel Conflict**: Using Channel 0 for SPI and also for Memory Copy will cause corruption. Manage resources carefully.

### 12. Try This Next
*   **Wait Method**: `d.wait()` that sleeps while busy.
*   **Status**: `d.bytes_remaining()` reads the live COUNT register.

---

## 1. Project 2494: Robust Professional Direct Memory Access (DMA) Controller

### 2. Learning Objective
Stream data from the ADC (Microphone) directly to a Circular Buffer in RAM. The DMA resets itself automatically (Ring Buffer).

### 3. Concepts Introduced
*   **DREQ (Data Request)**: The ADC signals the DMA "I have a byte". DMA copies 1 byte.
*   **Ring Mode**: When DMA reaches end of buffer, it wraps address back to start.
*   **Zero CPU Load**: The Main loop just reads the buffer whenever it wants.

### 4. Hardware Required
*   **Raspberry Pi Pico W**
*   **Microphone** (ADC)

### 5. Wiring / Interfaces
*   **Mic** -> ADC0

### 6. Blocks Used
*   **from Bitwise, drag `set_mask`**
*   **from Variables, drag `global_array`**

### 7. Variables
*   **audio_buf** (List)

### 8. Step-by-Step Guide

**A. ADC Config**
1.  **FIFO Enable**: Tell ADC to put results in its HW FIFO.
2.  **DREQ Enable**: Tell ADC to shout when FIFO has data.

**B. DMA Config**
1.  **Source**: `ADC_FIFO_ADDR`. (Fixed Address - No Incr).
2.  **Dest**: `audio_buf`. (Incr).
3.  **Ring**: Wrap Dest on 1024-byte boundary.

### 9. Execution Flow
1.  **Start**: ADC Sampling at 44kHz.
2.  **Autopilot**: DMA moves every sample to RAM.
3.  **Wrap**: At byte 1023, DMA writes next to byte 0.
4.  **CPU**: Can analyze "Last 1024 samples" at any time for FFT/Spectrogram.

### 10. Generated Code
```python
# Conceptual Config for ADC DREQ
ADC_BASE = 0x4004c000
ADC_FIFO = ADC_BASE + 0x08

# CTRL setup for DREQ=ADC (Treq 36 on RP2040)
# This requires precise bitmasking
# CTRL |= (36 << 15)
# Ring Buffer Size 1KB (1 << 10)
```

### 11. Common Mistakes
*   **Buffer Alignment**: Ring Buffers MUST be aligned in memory (Address starts at `...000`). Python `bytearray` doesn't guarantee this. You need a specialized allocator or allocate a larger buffer and manually find the aligned slice.
*   **Overwriting**: If CPU reads slower than ADC writes, you read old/mixed data.

### 12. Try This Next
*   **Double Buffer**: Have DMA trigger an interrupt at 50% mark and 100% mark.
*   **Output**: DMA from RAM to PWM (DAC) to play audio.

---

## 1. Project 2495: Professional Direct Memory Access (DMA) with Error Handling

### 2. Learning Objective
Detect and recover from DMA Bus Errors. What happens if you try to copy to Read-Only Memory (ROM)?

### 3. Concepts Introduced
*   **Bus Error**: Examples: Writing to Flash (XIP) via DMA, or accessing a non-existent peripheral.
*   **Error Flag**: The channel aborts and sets an Error Bit.
*   **Abort**: Manually stopping a runaway transfer.

### 4. Hardware Required
*   **Raspberry Pi Pico W**

### 5. Wiring / Interfaces
*   (Internal)

### 6. Blocks Used
*   **from Bitwise, drag `check_bit`**
*   **from Control, drag `reset_dma`**

### 7. Variables
*   **error_code** (Number)

### 8. Step-by-Step Guide

**A. Provoke Error**
1.  **Source**: RAM.
2.  **Dest**: `0x00000000` (Boot ROM - Read Only).
3.  **Start**: Trigger DMA.

**B. Handler**
1.  **Check**: `CTRL` Register bit 31 (AHB_ERROR).
2.  **If Set**:
    *   Print "Bus Error!".
    *   Command **ABORT** (Register `0x50000444`).
    *   Reset Channel.

### 9. Execution Flow
1.  **User**: Accidentally sets destination to wrong pointer.
2.  **DMA**: Tries to write. Bus Faults. Stops.
3.  **Code**: Detects the stall. Clears the error.
4.  **Recovery**: System continues (instead of hanging forever waiting for completion).

### 10. Generated Code
```python
def check_error(chan):
    # READ CTRL
    ctrl_val = machine.mem32[chan.ctrl_reg]
    
    # Bit 31 is AHB_ERROR
    if (ctrl_val >> 31) & 1:
        print(f"DMA Error on Channel {chan.id}")
        machine.mem32[0x50000444] = (1 << chan.id) # ABORT
        return True
    return False

d = DMA(0)
d.config(src, 0x0) # Invalid Write
d.start()
utime.sleep(0.1)
check_error(d)
```

### 11. Common Mistakes
*   **Silent Data Corruption**: Writing to a Reserved Address might not error, but might toggle random pins or reset unrelated peripherals.
*   **Hard Fault**: The CPU accessing a bad address crashes. DMA accessing a bad address just sets a flag (safer).

### 12. Try This Next
*   **Watchdog**: If DMA not done in 100ms, Abort and Retry.
*   **Checksum**: Use DMA Sniffer (RP2040 feature) to calculate CRC32 of the data *while* it copies.

---

