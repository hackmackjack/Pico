
import os
import re

DOC_PATH = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
BATCH_6_TEMP = r"d:\MFF\Pico\Documentation\Docs_Batch_6_temp.md"
BATCH_7_TEMP = r"d:\MFF\Pico\Documentation\Docs_Batch_7_temp.md"
BATCH_7_NEW = r"d:\MFF\Pico\Documentation\Docs_Batch_7_Real.md"
BATCH_8_NEW = r"d:\MFF\Pico\Documentation\Docs_Batch_8_Real.md"

def fix_sequence():
    # 1. Truncate Master File
    print("Truncating Master File...")
    with open(DOC_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the wrong batch start
    # "Batch 6: Doorbells 1"
    # Actually, the file header is "# 🏁 Batch 6: Doorbells 1"
    match = re.search(r'\n# 🏁 Batch 6: Doorbells 1', content)
    if match:
        cut_index = match.start()
        print(f"Cutting at index {cut_index}")
        new_content = content[:cut_index]
        with open(DOC_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print("Could not find invalid batch header. Checking if it's already fixed?")
        # Maybe I look for Project 61?
        if "Project 0061" in content:
            print("Project 0061 found but header mismatch. Please check manually.")
            # return
    
    # 2. Rename/Move Temp Files
    # Docs_Batch_6_temp (Doorbells) -> Docs_Batch_7_Real (Doorbells)
    if os.path.exists(BATCH_6_TEMP):
        print(f"Renaming {BATCH_6_TEMP} to {BATCH_7_NEW}")
        with open(BATCH_6_TEMP, 'r', encoding='utf-8') as f:
            data = f.read()
        # Fix Header
        data = data.replace("# 🏁 Batch 6: Doorbells 1", "# 🏁 Batch 7: Doorbells 1")
        with open(BATCH_7_NEW, 'w', encoding='utf-8') as f:
            f.write(data)
        # Don't delete original yet just in case
        
    # Docs_Batch_7_temp (Reaction) -> Docs_Batch_8_Real (Reaction)
    # Note: Header in file was "Batch 8: Reaction Game 1" (which was correct for Project 71, but file was named 7)
    if os.path.exists(BATCH_7_TEMP):
        print(f"Renaming {BATCH_7_TEMP} to {BATCH_8_NEW}")
        with open(BATCH_7_TEMP, 'r', encoding='utf-8') as f:
            data = f.read()
        # Header "Batch 8" is correct for Proj 71. So no text replace needed.
        with open(BATCH_8_NEW, 'w', encoding='utf-8') as f:
            f.write(data)

    print("Sequence files prepared. Master truncated. Ready for Generation of Real Batch 6.")

if __name__ == "__main__":
    fix_sequence()
