import base64
import pyperclip
import time
import sys

CHUNK_SIZE = 40000
SLEEP_TIME = 1.2 # DO NOT GO LOWER THAN 1

def send_file(filepath):
    with open(filepath, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")

    chunks = [encoded[i:i + CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)]
    total = len(chunks)
    
    print(f"Sending {total} chunks...")

    for i, chunk in enumerate(chunks):
        payload = f"{i}|{chunk}"
        pyperclip.copy(payload)
        print(f"Sent chunk {i + 1}/{total}")

        while True:
            response = pyperclip.paste().strip()
            print(f"[HOST DEBUG] Clipboard: {response[0:32]}...")
            if response == f"ACK:{i}":
                break
            time.sleep(SLEEP_TIME)
            

    pyperclip.copy("EOF")
    print("Transfer complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sender.py <file.zip>")
    else:
        send_file(sys.argv[1])
