import base64
import pyperclip
import time

CHUNK_SIZE = 40000
SLEEP_TIME = 1.2 # DO NOT GO LOWER THAN 1

def receive_file():
    global transfer_started
    buffer = []
    seen_index = -1
    print("Receiver started...")

    while True:
        clip = pyperclip.paste().strip()

        if clip == "EOF":
            print("EOF received")
            break

        if "|" not in clip:
            time.sleep(SLEEP_TIME)
            continue

        try:
            index_str, data = clip.split("|", 1)
            index = int(index_str)
            print(f"[DEBUG] Parsed index: {index} - {clip[0:32]}...")

            if index == seen_index:
                print(f"[DEBUG] Duplicate chunk {index}, waiting...")
                time.sleep(SLEEP_TIME)
                continue

            buffer.append(data)
            seen_index = index
            pyperclip.copy(f"ACK:{index}")
            print(f"ACK:{index} sent")


        except Exception as e:
            print(f"[ERROR] Exception: {e}")
            time.sleep(SLEEP_TIME)
            continue

    print("Reassembling...")
    full_data = "".join(buffer)
    raw = base64.b64decode(full_data)
    with open("reconstructed_file.zip", "wb") as f:
        f.write(raw)
    print("Saved to reconstructed_file.zip")

if __name__ == "__main__":
    pyperclip.copy("")
    receive_file()
