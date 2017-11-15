import urllib.request as request  
import http.cookiejar as cookiejar  
import re  
import os  
import smtplib  
from email.mime.text import MIMEText  
import time  
user = '' #登陆邮箱  
pwd = ''#邮箱密码  
to = [''] #发送的邮箱  
with open('city.txt','r') as f:
   a = f.read()  
station = re.split(u'\w+:(.+?):(\w+):\d').findall(a)
dic1 = {}  
for b in range(0, len(station)):  
    dic1[station[b][0]] = station[b][1]  
def gethtml(geturl):  
    cj = cookiejar.LWPCookieJar()  
    cookiejarsupport = request.HTTPCookieProcessor(cj)  
    opener = request.build_opener(cookiejarsupport,request.HTTPHandler)  
    headers = {  
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36',  
        'Host':'www.12306.cn',  
        'Referer':'http://www.12306.cn/opn/lcxxcx/init'  
    }  
    request.install_opener(opener)  
    req = request.Request(url=geturl, headers=headers)  
    html = request.urlopen(req).read().decode()  
    return html  
def getstation(html):  
    fromstation = re.compile(r'from_station_name":"(.+?)","').findall(html)  
    tostation = re.compile(r'to_station_name":"(.+?)",').findall(html)  
    startime =  re.compile(r'"start_time":"(.+?)"').findall(html)  
    arrtime = re.compile(r'arrive_time":"(.+?)"').findall(html)  
    lishi =  re.compile(r'"lishi":"(.+?)",').findall(html)  
    webbuy = re.compile(r'"canWebBuy":"(.+?)').findall(html)  
    startstation = re.compile(r'start_station_name":"(.+?)"').findall(html)  
    endstation = re.compile(r'end_station_name":"(.+?)"').findall(html)  
    ruanwo = re.compile((r'"rw_num":"(.+?)",')).findall(html)  
    ruanzuo = re.compile((r'"rz_num":"(.+?)"')).findall(html)  
    yingwo = re.compile(r'"yw_num":"(.+?)"').findall(html)  
    ruanzuo = re.compile(r'"rz_num":"(.+?)"').findall(html)  
    yingzuo = re.compile(r'"yz_num":"(.+?)"').findall(html)  
    wuzuo = re.compile(r'"wz_num":"(.+?)"').findall(html)  
    checi = re.compile(r'station_train_code":"(.+?)"').findall(html)  
    datanum = re.compile((r'day_difference":"(.+?)"')).findall(html)  
    erdengzuo = re.compile(r'ze_num":"(.+?)",').findall(html)  
    num = range(0, len(yingwo))  
    for i in num:  
        try:  
            if int(yingzuo[i]) != 0 or int(erdengzuo[i]) != 0 or int(wuzuo[i] !=0):     #Z108  
                print(checi[i], '    二等座：  ', erdengzuo[i], '    硬座：   ', yingzuo[i],'   无座：  ',wuzuo[i])  
                if yingwo[i] != '--' or yingzuo[i] != '无':  
                    msg=MIMEText('火车： '+fromstation[i]+' ->'+tostation[i] +'（'+ checi[i]+ '）\n二等座：'+erdengzuo[i]+ '张;硬座：'+ yingzuo[i]+'张;无座：'+wuzuo[i]+ '张！快买去!\n网址： http://www.12306.cn/opn/lcxxcx/init')  
                    msg['Subject'] = '有票啦！'  
                    msg['From'] = user  
                    msg['To'] = ','.join(to)  
                    s = smtplib.SMTP('smtp.qq.com', timeout = 30) #连接SMTP端口 
                    s.login(user,pwd)#登陆服务器  
                    s.sendmail(user,to,msg.as_string())  
                    s.close()  
                    print('发送成功')  
                    print('------------------------------------------------------------')  
        except:  
            continue  
print(''''' 
    By:王小涛_同學 
-------------------------------------------------------------- 
    欢迎使用！ 
-------------------------------------------------------------- 
''')  
print ('请输入购票类型： （0为成人票   其他为学生票） ')  
leixing = input()  
print('请输入起点：')  
qidian = input()  
try:  
    if dic1[qidian]:  
        qidian = dic1[qidian]  
except:  
    print('起点输入有误！')  
print('请输入终点：')  
zhongdian = input()  
try:  
    if dic1[zhongdian]:  
        zhongdian = dic1[zhongdian]  
except:  
    print('终点输入有误！')  
print('请输入购票年份：')  
year = input()+'-'  
print('请输入购票月份:（2位）')  
month = input()+'-'  
print('请输入购票日期：(2位)')  
date = input()  
date = year + month + date  
  
  
if leixing == 0:  
   geturl = 'http://www.12306.cn/opn/lcxxcx/query?purpose_codes=ADULT&queryDate='+date+'&from_station='+qidian+'&to_station='+ zhongdian  
else:  
    geturl = 'http://www.12306.cn/opn/lcxxcx/query?purpose_codes=0X00&queryDate='+date+'&from_station='+qidian+'&to_station='+ zhongdian  
while 1:  
    getstation(gethtml(geturl))  
    print('火车票监测中...')
    time.sleep(300)  
