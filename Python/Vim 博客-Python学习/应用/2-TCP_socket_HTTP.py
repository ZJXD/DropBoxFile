# 前面，已经使用TCP socket来为两台远程计算机建立连接
# 然而，socket传输自由度太高，从而带来很多安全和兼容的问题
# 我们往往利用一些应用层的协议来规定socket使用规则，以及所传输信息的格式

# HTTP 协议利用请求-回应的方式来使用TCP socket
# 客户端想服务器发送一段文本作为request，服务器端接收到request之后向客户端发送一段文本response
# 在完成这样一次request-response交易之后，TCP socket被废弃，下次的request将建立新的socket
# request和response本质上说是两个文本，只是http协议对这两个文本一定的格式要求

# Written by ZHT

import socket

# Address
HOST = ''
PORT = 60000

# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK
Content-Type:text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow,Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture,put into HTTP format
pic_content = '''
HTTP/1.x 200 OK
Content-Type:image/jpg

'''



# Configure socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

# infinite loop,server forever
while True:
    s.listen(3)
    conn,addr = s.accept()
    request = str(conn.recv(1024),encoding = 'utf-8')
    if(request != ''):
        method = request.split(' ')[0]
        src = request.split(' ')[1]

        # deal with GET method
        if method == 'GET':
            # ULR
            if '.jpg' in src:
                f = open(src[1:],'rb')
                pic_bytes = f.read()
                f.close()
                content = bytes(pic_content,encoding = 'utf-8') + pic_bytes
            else:
                content = bytes(text_content,encoding = 'utf-8')
            conn.sendall(content)
            #print('Response is:',content)
            print('Connected by ',addr)
            print('Request is:',request)

        conn.close()
    

