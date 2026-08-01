import socket

IP_ADDRESS = '127.0.0.1'
PORT = 8000
ADDR = (IP_ADDRESS, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(1)

result = s.connect_ex((ADDR))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

s.close()