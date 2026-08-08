import socket
import threading
import argparse
import json

parser = argparse.ArgumentParser(description="TCP Port Scanner")
parser.add_argument("ip", help="Target IP address")
parser.add_argument("--ports", help="Port range e.g. 1-1024", default="1-1024")
parser.add_argument("--output", help="Save results to a JSON file e.g. results.json")

args = parser.parse_args()

start_port, end_port = args.ports.split("-")
start_port = int(start_port)
end_port = int(end_port)

IP_ADDRESS = args.ip
open_ports = []
lock = threading.Lock()
port_banners = {}

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"

        with lock:
            open_ports.append(port)
            port_banners[port] = banner
    
    s.close()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(IP_ADDRESS, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan complete")
for port in sorted(open_ports):
    print(f"Port {port}: {port_banners[port]}")

if args.output:
    results = {
        "target": IP_ADDRESS,
        "open_ports": sorted(open_ports),
        "banners": {str(port): port_banners[port] for port in sorted(open_ports)}
    }
    with open(args.output, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {args.output}")

