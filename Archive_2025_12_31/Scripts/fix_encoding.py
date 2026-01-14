
import os
import re

OUTPUT_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"
TEMP_FILES = [
    r"d:\MFF\Pico\Documentation\Docs_Batch_2_temp.md",
    r"d:\MFF\Pico\Documentation\Docs_Batch_3_temp.md",
    r"d:\MFF\Pico\Documentation\Docs_Batch_4_temp.md",
    r"d:\MFF\Pico\Documentation\Docs_Batch_5_temp.md"
]

def clean_rebuild():
    print("Starting clean rebuild of Docs_0001_0100.md... (Byte Level)")
    
    valid_bytes = b""
    try:
        with open(OUTPUT_FILE, 'rb') as f:
            raw_data = f.read()

        # Search for markers in BYTES
        # Marker 1: Clean UTF-8 "Project 0011"
        marker_clean = b"Project 0011"
        # Marker 2: Wide Char "P.r.o.j.e.c.t. .0.0.1.1" (Little Endian usually)
        marker_wide = b"P\x00r\x00o\x00j\x00e\x00c\x00t\x00 \x000\x000\x001\x001"
        
        idx1 = raw_data.find(marker_clean)
        idx2 = raw_data.find(marker_wide)
        
        cut_index = -1
        
        if idx1 != -1 and idx2 != -1:
            cut_index = min(idx1, idx2)
        elif idx1 != -1:
            cut_index = idx1
        elif idx2 != -1:
            # If we found ONLY the wide one, that's where we cut
            cut_index = idx2
        else:
            print("Could not find Project 11 start (neither clean nor wide).")
            # If we can't find Project 11, maybe we blindly trust the Batch 2 header?
            # Or maybe we rely on Batch 1 end?
            # Let's search for "Project 0010" and keep a bit after? 
            # Risk: We might lose Project 10's content if we cut too early.
            # Fallback: Check for "Batch 2" header?
            marker_batch2 = b"# \xf0\x9f\x8f\x81 Batch 2" # UTF-8 Emoji 🏁
            idx3 = raw_data.find(marker_batch2)
            if idx3 != -1:
                 cut_index = idx3
            else:
                 # Check for wide batch 2?
                 # Too complex. Let's assume if we found nothing, we keep all (risky) or keep nothing?
                 # If we return empty, we lose Batch 1.
                 # Let's assume the file is toast and we only have Batches 2-5.
                 # BUT we DO NOT want to lose Batch 1.
                 print("WARNING: keeping existing content as is (might be corrupted).")
                 valid_bytes = raw_data

        if cut_index != -1:
            print(f"Found cut point at index {cut_index}. Truncating...")
            valid_bytes = raw_data[:cut_index]
            
            # Now CLEAN the valid_bytes of any nulls (convert 'P\x00' to 'P')
            # This is a crude "ConvertToUTF8" from mixed noise
            # Only remove nulls if they look like inter-char padding?
            # Actually, simply removing ALL null bytes is usually safe for Text Markdown files 
            # (Null is not valid in markdown text).
            if b'\x00' in valid_bytes:
                print("Detected Null bytes in header. Stripping them...")
                valid_bytes = valid_bytes.replace(b'\x00', b'')

    except Exception as e:
        print(f"Error reading existing file: {e}")
        return

    # Write cleaned first part
    with open(OUTPUT_FILE, 'wb') as f_out:
        f_out.write(valid_bytes)
        if not valid_bytes.endswith(b'\n'):
            f_out.write(b'\n')
            
        # Append batches
        for tf in TEMP_FILES:
            if not os.path.exists(tf):
                 print(f"ERROR: Temp file missing: {tf}")
                 continue
                 
            print(f"Appending {tf}...")
            with open(tf, 'rb') as f_in: # Read as binary to be safe
                batch_content = f_in.read()
                f_out.write(batch_content)
                if not batch_content.endswith(b'\n'):
                    f_out.write(b'\n')
                    
    print("Rebuild complete.")

if __name__ == "__main__":
    clean_rebuild()
