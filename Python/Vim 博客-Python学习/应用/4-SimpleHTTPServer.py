# 经过socketserver的改造后，代码还是不够简单。
# 我们上面的通信基于TCP协议，而不是HTTP协议，这样就必须手动解析HTTP协议
# 这里我们将建立基于HTTP协议的服务器

# HTTP 协议基于TCP协议，但增加了更多的规范
# 这些规范虽然限制了TCP协议的功能，但是大大提高了信息封装和提取的方便程度

#对于一个HTTP请求（request）来说，它们包含两个重要信息：请求方法和URL

# 根据请求方法和URL的不同，一个大型的HTTP服务器可以应付成千上万中的请求
# 在Python中，可以使用SimpleHTTPServer包和CGIHTTPServer包来规定针对不同的请求
# 其中SimpleHTTPServer可以用于处理GET方法和HEAD方法的请求
# 它读取request中的URL地址，找到对应的静态文件，分析文件类型，用HTTP协议发给客户端

# 在Python3.x中 BaseHTTPServer、SimpleHTTPServer、CGIHTTPServer整合到http.server
# SocketServer 改名为 socketserver

# Written by ZHT
# Simple HTTPsServer

import socketserver
from http import server

HOST = ''
PORT = 60000

ser = socketserver.TCPServer((HOST,PORT),server.SimpleHTTPRequestHandler)

ser.serve_forever()


# 这里的程序不能处理POST请求，这个在后面使用CGI来弥补这个缺陷
# 值得注意的是，现在的Python服务器程序变的非常简单。根据URL为客户端提供静态文件
# 这样在更新内容时，可以只修改静态文件，而不用停留整个Python服务器

# 这样的改进也付出代价。在原始程序中，request中的URL只具有指导意义，可以规定任意的操作
# 在这里，操作与URL的指向密切相关。用自由度，换来了更加简洁的程序
