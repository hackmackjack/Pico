
import os

MASTER_FILE = r"d:\MFF\Pico\Documentation\Docs_0001_0100.md"

def append_multiple():
    files_to_append = [
        r"d:\MFF\Pico\Documentation\Docs_Batch_9_temp.md",
        r"d:\MFF\Pico\Documentation\Docs_Batch_10_temp.md"
    ]
    
    for batch_file in files_to_append:
        print(f"Appending {batch_file} to {MASTER_FILE}...")
        if not os.path.exists(batch_file):
            print(f"Error: {batch_file} missing.")
            continue
            
        try:
            with open(batch_file, 'r', encoding='utf-8') as f_in:
                new_content = f_in.read()
            with open(MASTER_FILE, 'a', encoding='utf-8') as f_out:
                f_out.write('\n\n') 
                f_out.write(new_content)
            print("Success.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    append_multiple()
