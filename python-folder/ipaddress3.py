# This script finds IP Address of Local Computer

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print(f"My Computer IP Address is: " + s.getsockname()[0])

s.close()

hostname = socket.gethostname()

IPAddr = socket.gethostbyname(hostname)

print("My Computer Name is: " + hostname)

print("My Computer Broadcast Address is: " + IPAddr)

