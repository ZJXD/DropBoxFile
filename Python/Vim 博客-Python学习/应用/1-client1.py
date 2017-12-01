import socket
import os

obj = socket.socket()

obj.connect(("192.168.1.237",50000))

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str)

size = os.stat("yan.jpg").st_size
obj.sendall(bytes(str(size),encoding="utf-8"))

obj.recv(1024)

with open("yan.jpg","rb") as f:
    for line in f:
        obj.sendall(line)
