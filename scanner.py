import socket
import threading

IP_ADDRESS = '127.0.0.1'
open_ports = []
lock = threading.Lock()

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        with lock:
            open_ports.append(port)
    
    s.close()

threads = []

for port in range(1, 9000):
    t = threading.Thread(target=scan_port, args=(IP_ADDRESS, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan complete")
print(f"Open ports: {sorted(open_ports)}")

