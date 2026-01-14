# 📋 Smart Block Planning Report (V5.0 Strategy)

## 1. What is a Smart Block?
A **Smart Block** is a high-level UI wrapper designed to declutter the toolbox.
*   **Behavior:** It presents a single block with a **Dropdown Menu** to select an operation (e.g., "Read", "Exists", "Size").
*   **Constraint 1 (Inputs):** All operations in the dropdown must share the **exact same input fields**. (e.g., You cannot merge "Connect (SSID, Pass)" with "Disconnect (None)").
*   **Constraint 2 (Output):** The block must have a consistent shape (Statement or Value).
*   **Implementation:** The generator calls a specific **Runtime Helper** function for each operation. No heavy logic resides in the block definition.
*   **Relationship:** Smart Blocks **do not replace** existing blocks. They sit alongside them as a cleaner alternative for 80% of use cases.

---

## 2. Existing Block Inventory (V4.8)
*Blocks considered for consolidation.*

| ID | Purpose | Inputs | Output | Generator Logic |
| :--- | :--- | :--- | :--- | :--- |
| **File System** | | | | |
| `pico_file` | Write/Append | Name, Data | Statement | Inline `with open...` |
| `pico_file_read` | Read Content | Name | Value (String) | Helper `read_file` |
| `pico_file_exists` | Check File | Name | Value (Bool) | Helper `file_exists` |
| `pico_file_delete` | Delete File | Name | Statement | Inline `os.remove` |
| `pico_file_list` | List Files | Path | Value (List/Str) | Inline `os.listdir` |
| `pico_file_space` | Free Space | Path | Value (Number) | Helper `free_space` |
| **Math / Filters** | | | | |
| `pico_median` | Median Filter | Value | Value (Number) | Helper `median_filter` |
| `pico_smooth` | Average | Value, Count | Value (Number) | Helper `moving_average` |
| `pico_math_stats` | Stats (Avg/Max) | List | Value (Number) | Helper `stats` |
| **WiFi / IoT** | | | | |
| `pico_wifi` | Connect | SSID, Pass | Statement | Inline `wlan.connect` |
| `pico_wifi_disconnect`| Disconnect | None | Statement | Inline `wlan.disconnect` |
| `pico_wifi_status` | Status | None | Value (String) | Helper `wifi_status` |
| `pico_wifi_scan` | Scan | None | Statement (Print) | Inline `wlan.scan` |

---

## 3. Logical Groupings

1.  **File Queries (Name -> Value):** Blocks that take a filename string and return information (`Read`, `Exists`).
2.  **File Actions (Name -> Statement):** Blocks that take a filename and perform an action (`Delete`, `Rotate` - *proposed*).
3.  **Data Filters (Value/List -> Value):** Math blocks that process sensor data (`Median`, `Stats`, `Smooth`).
4.  **WiFi Utils (Void -> Statement/Value):** Simple WiFi commands with no parameters (`Disconnect`, `Scan`, `Status`).

---

## 4. Proposed Smart Block Candidates

### Candidate A: `pico_smart_file_query`
*   **Purpose:** Unified block for checking file info.
*   **Dropdown Operations:**
    1.  `Read Content` (Returns String)
    2.  `Check Exists` (Returns Boolean)
    3.  `Get Size Bytes` (Returns Number - *New helper based on os.stat*)
*   **Inputs:** `NAME` (String)
*   **Output Type:** Value (Unchecked/Polymorphic).
*   **Runtime Helpers:** `file_manager.read(n)`, `file_manager.exists(n)`, `file_manager.size(n)`.
*   **Unifies:** `pico_file_read`, `pico_file_exists`.
*   **Why Valid:** All ops take exactly 1 string (Name) and return a value.

### Candidate B: `pico_smart_data_filter`
*   **Purpose:** Apply math filters to data.
*   **Dropdown Operations:**
    1.  `Median (Window 5)`
    2.  `Average (Window 10)`
    3.  `Max (List)`
    4.  `Min (List)`
*   **Inputs:** `DATA` (Number/List)
*   **Output Type:** Value (Number).
*   **Runtime Helpers:** `data_filter.median(v)`, `data_filter.avg(v)`, `data_filter.max(l)`.
*   **Unifies:** `pico_median`, `pico_smooth` (fixed window), `pico_math_stats`.
*   **Why Valid:** All take data input and return a number. Note: We will fix the "Window" for smoothing to keep inputs simple (or use a sensible default).

### Candidate C: `pico_smart_wifi_cmd`
*   **Purpose:** Simple WiFi commands.
*   **Dropdown Operations:**
    1.  `Disconnect`
    2.  `Print Scan Results`
*   **Inputs:** None.
*   **Output Type:** Statement.
*   **Runtime Helpers:** `wifi_helper.disconnect()`, `wifi_helper.scan_print()`.
*   **Unifies:** `pico_wifi_disconnect`, `pico_wifi_scan`.
*   **Why Valid:** Both are parameter-less actions.

---

## 5. Rejected Candidates (Invalid Merges)

*   ❌ **Smart MQTT (Setup + Publish):**
    *   *Reason:* `Setup` requires (ID, Broker). `Publish` requires (Topic, Msg). `Check` requires (None). Merging these would require a block with 4 inputs where 2 are hidden/unused half the time. This violates "Simple UI" rules.
*   ❌ **Smart WiFi (Connect + Status):**
    *   *Reason:* `Connect` is a Statement (Action). `Status` is a Value (String output). You cannot change a block's shape from puzzle-piece to connector-nub dynamically in a simple dropdown system.

---

## 6. UI Impact
*   **File Category:** Reduces clutter from 6 blocks to ~3 (Smart Query, Smart Action, Smart List).
*   **Math/Sensors:** Hides 3 separate filter blocks behind 1 clean "Filter" block.
*   **System:** Removes "Disconnect" and "Scan" clutter blocks.

---

## 7. Options Strategy

### Option A: Minimal (Files Only)
*   Implement `pico_smart_file_query`.
*   *Pros:* Zero risk, high value (files are confusing).
*   *Cons:* Leaves Math and WiFi clutter.

### Option B: Moderate (Files + Math)
*   Implement `pico_smart_file_query` and `pico_smart_data_filter`.
*   *Pros:* Cleans up two busiest categories.
*   *Cons:* Moderate effort to write Math helpers.

### Option C: Aggressive (Files + Math + WiFi)
*   Implement all 3 candidates.
*   *Pros:* Maximum cleanliness.
*   *Cons:* Higher testing load.

---

## 8. Recommendation
I recommend **Option B (Files + Math)**.
*   **Why:** File operations are the messiest part of the toolbox. Math filters are conceptually similar and benefit from grouping. WiFi blocks are distinct enough that they don't hurt much.
*   **Simplicity:** Students get one block for "Check File" and one block for "Filter Sensor".
*   **Safety:** Does not touch the complex Networking stack logic yet.

---

## 9. Risks & Constraints
1.  **Polymorphic Return (File Query):** The `File Query` block returns String (Read) or Bool (Exists). In Python, this is fine. In Blockly, we must set the output check to `null` (allow any) to prevent connection errors.
2.  **Helper Duplication:** `pico_median` already has a helper. The Smart Block should **reuse** the existing `DRIVERS['median']` logic or wrap it, rather than pasting duplicate code.
3.  **Blocking:** File operations are blocking. This remains true for Smart Blocks.

---

## 10. Rollout Plan
1.  **Phase 1: Runtime Helpers**
    *   Create `FileManager` class (wrapping os).
    *   Create `DataFilter` class (unifying median/stats).
2.  **Phase 2: Smart Block Implementation**
    *   Add JSON for `pico_smart_file_query` and `pico_smart_data_filter`.
    *   Write Generators that call `FileManager.*` and `DataFilter.*`.
3.  **Phase 3: Integration**
    *   Add to Toolbox.
    *   Move old blocks to "Advanced/Legacy" sub-category (or keep them at bottom).
4.  **Phase 4: Testing**
    *   Verify `Read` returns string.
    *   Verify `Exists` returns bool.
    *   Verify `Median` filters noise.
