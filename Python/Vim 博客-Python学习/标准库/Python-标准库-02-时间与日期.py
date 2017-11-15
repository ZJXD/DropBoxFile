# 时间与日期
# Python 具有良好的时间和日期管理功能。实际上，计算机只会维护一个时间叫做：
# 挂钟时间（wall clock time），这个时间是从某个固定时间起点到现在的时间间隔
# 时间起点的选择与计算机相关，但是一台计算机，这一时间起点是固定的其他是从这个得到
# 此外，计算机和可以测量CPU实际上运行的时间，也就是处理时间（processor clock time）
# 用来测量计算机性能，当CPU处于闲置状态时，处理器时间会暂停


# time包-------------------------------------------------------------------------

# time 包基于C语言的库函数（library functions）Python的解释器通常是用C编写的

import time

# print(time.time())     # wall clock time,unit:second
# print(time.clock())    # processor clock time,unit:second

# print('start')
# time.sleep(10)         # sleep for 10 seconde
# print('wake up')

# time包还定义了struct_time对象，该对象时间上是将挂钟时间转换为年、月、日、时、分、秒
# 存储在该对象的各个属性中（tm_year,tm_mon,tm_mday...），下面是将挂钟时间转换为该对象
'''
st = time.gmtime()       # 返回struct_time格式的UTC时间
print(st)
st = time.localtime()    # 返回struct_time格式的当地时间
print(st)
s = time.mktime(st)      # 将struct_time格式转换成 wall clock time
print(s)
'''

# datetime包--------------------------------------------------------------------

# 简介------
# datetime包是基于time包的一个高级包
# datetime可以理解为date和time两个组成部分。date是指年月日构成的日期（相当于日历）
# time是指时分秒构成的一天24小时中的具体时间（相当于手表）
# 可以将这两个分开管理（datetime.date,datetime.time）也可以荷载一起用（datetime.datetime）

# 时间运算-----
'''
import datetime as dt

t = dt.datetime(2017,11,2,15,20)
t_next = dt.datetime(2017,11,2,16,20)
delta1 = dt.timedelta(seconds = 600)
delta2 = dt.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)
'''

# 给 datetime.timedelta传参数，还可以是days,hours,milliseconde,microseconds

# 两个 datetime 对象可以进行比较
# print (t>t_next)


# datetime对象与字符串转换--------

from datetime import datetime as dt
format = "output-%Y-%m-%d-%H%M%S.txt"
str = "output-1997-12-23-030000.txt"
t = dt.strptime(str,format)
print(t)
t = dt(2017,11,2,15,20)
print(t.strftime(format))
