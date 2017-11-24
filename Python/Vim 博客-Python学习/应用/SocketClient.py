# Client side
import socket

# Address
HOST = '192.168.1.237'
PORT = 60000

request = 'can you hear me?'

s = socket.socket()
s.connect((HOST,PORT))

s.sendall(bytes("连接上啦，哈哈哈",encoding="gb2312"))

reply = s.recv(1024)

print('reply is:',str(reply,encoding = "utf-8"))

s.close()
