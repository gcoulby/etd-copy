# ETD Copy — Encode Transfer Decode Utility

ETD Copy is a clipboard-based file transfer utility designed for secure, GUI-isolated environments such as virtual machines, sandboxed systems, or remote sessions where traditional file sharing is restricted. It uses base64 encoding, the system clipboard, and a two-script protocol to move zip archives safely and silently.

## Features

* No shared folders, no networking required — just clipboard access.
* Chunked transfer with acknowledgments and reassembly.
* Cross-platform Python-based scripts (host + guest).

## Project Structure

```
.
├── sender.py         # Host-side script that sends file via clipboard
├── receiver.py       # VM-side script that receives clipboard data
├── requirements.txt  # Python dependencies
├── README.md         # You're reading it
├── LICENSE           # License text
└── .gitignore        # Standard exclusions
```

## Usage

### Host (Sender)

```bash
python sender.py path/to/file.zip
```

This will:

1. Encode the file to base64.
2. Break the file into safe clipboard-sized chunks.
3. Wait for ACKs after each chunk.
4. Signal completion with an EOF message.

### VM (Receiver)

```bash
python receiver.py
```

This will:

1. Wait for file chunks via clipboard.
2. Reassemble and decode the file.
3. Save the result to disk.

## Requirements

* Python 3.6+
* `pyperclip` (cross-platform clipboard library)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Why ETD?

In some environments, dragging files into VMs or remote sessions is impossible, but the clipboard still works. ETD Copy leverages this to create a coordinated, low-friction file transfer mechanism that respects your isolation boundaries.

## Limitations & Tips

* Clipboard syncing can be slow or unreliable under 1-second polling.
* Large files may require patience — optimize chunk size if needed.
* Consider hashing the file after transfer to verify integrity.

## Future Ideas

* Automatic checksum validation (SHA-256)
* Optional compression
* GUI frontend for user-friendly transfers

## Name Origin

ETD stands for Encode → Transfer → Decode, the core process behind the tool. It’s ideal for constrained but clipboard-accessible environments.

> ETD Copy — A slow, useless-for-most-use-cases file transfer utility you don't really need... until you do. 

## License

MIT License


