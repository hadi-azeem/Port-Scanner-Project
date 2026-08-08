# Port Scanner

This mini project is a multithreaded TCP port scanner built in Python using raw sockets.

## Features
- Concurrent scanning using Python threading
- Banner grabbing to identify services on open ports
- CLI arguments for flexible usage
- Optional JSON output

## Usage
```bash
python3 scanner.py <ip> --ports <start-end> --output <filename.json>
```

## Examples
```bash
python3 scanner.py 127.0.0.1
python3 scanner.py 127.0.0.1 --ports 1-9000
python3 scanner.py 127.0.0.1 --ports 1-9000 --output results.json
```

## What I learned
- How TCP connect scanning works (3-way handshake)
- Python socket programming
- Multithreading and thread-safe data structures (Lock)
- Service banner grabbing
- Building CLI tools with argparse

## Disclaimer!
Only use this tool on systems you own or have explicit permission to scan.