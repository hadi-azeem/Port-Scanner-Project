import socket

IP_ADDRESS = '127.0.0.1'
open_count = 0
closed_count = 0
open_ports = []

for port in range(1, 1025):
    ADDR = (IP_ADDRESS, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ADDR))

    if result == 0:
        open_count += 1
        open_ports.append(port)
    else:
        closed_count += 1

    s.close()

print("Scan complete")
print(f"No. of ports open: {open_count}")
print(f"No. of ports closed: {closed_count}")
print(f"Open ports: {open_ports}")
