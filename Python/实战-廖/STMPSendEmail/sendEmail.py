# coding=utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

msg = MIMEText('hello,send by Python...','plain','utf-8')
# 构造MIMEText对象时，第一个参数是邮件正文，第二个是subtype，传入'plain'表示纯文本，最终的就是'text/plain'，utf-8保证多语言兼容性

from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')
smtp_server = input('SMTP server:')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)  # SMTP协议默认的是25端口号
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()