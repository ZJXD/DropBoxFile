# 使用静态文件或者CGI来回应请求
# CGIHTTPServer包中的CGIHTTPRequestHandler类继承自SimpleHTTPRequestHandleer类
# 所以可以用来代替上面的例子，来提供静态文件的服务。这个类还可以运行CGI脚本

# 什么是CGI(Common Gateway Interface),是服务器和应用脚本之间的一套接口标准
# 功能是让服务器程序运行脚本程序，将程序的输出作为response发送给客户
# 总体的效果，是允许服务器动态的生成回复内容，而不必局限于静态文件

# 支持CGI的服务器接收到客户的请求，根据请求中的URL，运行对应的脚本文件
# 服务器会将HTTP请求的信息和scoket信息传递给脚本文件并等待脚本的输出
# 脚本的输出封装成合法的HTTP回复，发送给客户
# CGI可以充分发挥服务器的可编程性，让服务器变的“更聪明”

# 服务器和CGI脚本之间的通信要符合CGI标准，CGI实现的方式很多
# 比如使用Apache服务器于Perl写的CGI脚本，或者Python服务器于shell写的CGI脚本

# 为了使用CGI，需要使用BaseHTTPServer包中的HTTPServer来构建服务器

# Written by ZHT
# A messy HTTP server based on TCP socket

from http import server

HOST = ''
PORT = 60000

# Create the server
ser = server.HTTPServer((HOST,PORT),server.CGIHTTPRequestHandler)

# Start the server
ser.serve_forever()
