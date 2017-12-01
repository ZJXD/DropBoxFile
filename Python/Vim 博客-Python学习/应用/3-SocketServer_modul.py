# 建立一个 TCPServer 对象，建立的时候设置服务器的IP地址和端口
# 使用 server_forever 方法来让服务器不断工作（相当于前面的while循环）

# 我们定义的 MyTCPHandler 类，是来如何操作socket，这个类继承BaseRequestHandler
# 类中改写了 handle 方法。self.request 来查询通过socket进入服务器请求
# 对 socket 进行 recv 和 sendall，还是用self.address来引用socket的客户端地址

# Written by ZHT
# use TCPServer

import socketserver

HOST = ''
PORT = 60000

text_content = '''HTTP/1.x 200 OK
Content-Type:text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow,Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname">
<br><input type="submit" value="Submit">
</form>
</html>
'''

# Read picture,put into HTTP format
pic_content = '''
HTTP/1.x 200 OK
Content-Type:image/jpg

'''

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request = str(self.request.recv(1024),encoding = 'utf-8')
        
        if(request != ''):
            method = request.split(' ')[0]
            src = request.split(' ')[1]
            print('Connected by ',self.client_address[0])
            print('Request is:',request)

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
                self.request.sendall(content)
                #print('Response is:',content)

            if method == 'POST':
                form = request.split('\r\n')
                idx = form.index('')
                entry = form[idx:]

                value = entry[-1].split('=')[-1]
                self.request.sendall(bytes(text_content + '\n <p>' + value + '</p>',encoding = 'utf-8'))

# create the server
server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)

# start the server,and work forever
server.serve_forever()
