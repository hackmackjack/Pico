import re

def verify_compliance():
    filepath = "Documentation/Docs_0101_0200.md"
    try:
        with open(filepath, 'r') as f: content = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    for i in range(101, 201):
        pid = f"{i:04d}"
        if f"## Project {pid}" not in content:
            print(f"[{pid}] Missing Header")
            continue

        p_start = content.find(f"## Project {pid}")
        next_p = content.find(f"## Project {i+1:04d}", p_start)
        block = content[p_start:next_p] if next_p != -1 else content[p_start:]

        # Check S6 Specifically
        s6_start = block.find("### 6. Blocks Used")
        s7_start = block.find("### 7. Variables")

        if s6_start != -1 and s7_start != -1:
            s6_block = block[s6_start:s7_start]
            if "* From" in s6_block or "*   From" in s6_block:
                print(f"[{pid}] S6 Formatting Error ('From' detected)")
        else:
            # Fallback if structure is broken
            if "* From" in block: # Logic from original tool, mainly as backup
                 # Only report if it looks like it's in a list context that isn't S8?
                 # Actually, let's trust the section finding.
                 pass

        if "if btn.value():" in block:
            print(f"[{pid}] Implicit Boolean Error")

        if "### 9. Execution Flow" not in block:
            print(f"[{pid}] Missing S9")

        if "### 10. Generated Code" not in block:
            print(f"[{pid}] Missing S10")

if __name__ == "__main__":
    verify_compliance()
