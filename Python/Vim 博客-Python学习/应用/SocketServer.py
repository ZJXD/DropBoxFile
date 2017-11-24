# Server side
import socket

# Address
HOST = ''
PORT = 5000

reply = "123"

# Configure socket,使用的是IPv4(AF_INET),和TCP协议(SOCK_STREAM)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

# passively wait,3:maximum number of connections in the queue
# 监听
s.listen(3)

while True:
    # accpet and establish connection，接受连接
    conn,addr = s.accept()
    conn.sendall(bytes("欢迎光临我爱我家",encoding="gb2312"))

    # receive message
    request = conn.recv(1024)

    print('request is:',str(request,encoding = "gb2312"))
    print('Connected by',addr)

    # send message
    conn.sendall(bytes("此次连接完成，拜拜",encoding="gb2312"))

    # close connection
    conn.close()
