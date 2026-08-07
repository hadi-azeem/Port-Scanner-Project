import socket
import threading

IP_ADDRESS = '127.0.0.1'
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

for port in range(1, 9000):
    t = threading.Thread(target=scan_port, args=(IP_ADDRESS, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan complete")
for port in sorted(open_ports):
    print(f"Port {port}: {port_banners[port]}")

