'''
# 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。
# (提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
# 这里面用到的是，能让结尾是 0 的那么就看有多少个 2*5，分解因子，以少的一个为准
L=[312,23,3,125]

a = 0
b = 0
for i in L:
    while(i%2==0):
        a += 1
        i = i//2
        # print (i)

# print (L)

for i in L:
    while(i%5==0):
        b += 1
        i = i//5
        # print (i)

if(a>b):
    print (b)
else:
    print (a)


# 给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。--------------------------------------
# 如果为奇数输出1,偶数则输出0.
L=[312,23,3,125]

a = 0
b = 0
for i in L:
    while(i%2==0):
        a += 1
        i = i//2

# print (L)

for i in L:
    while(i%5==0):
        b += 1
        i = i//5

if(a>b):
    print (0)
else:
    print (1)



# 给你一个整数a，数出a在二进制表示下1的个数，并输出。
a = 7
b = 0
while(a/2>0):
    if(a%2==1):
        b+=1
    a = a//2

print (b)


# python 之禅
import this



# str = "www.runoob.com"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写

a="aaaaaabbbDDDDD"

print (a.lower())


# 人民币金额打印--------------------------------------------------------------------
from enum import Enum

class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day = Weekday.Mon
print (day)
print (day.value)
for name,member in Weekday.__members__.items():
    print (name,'=>',member)

import re
def NumToChar(n):
    switcher = {
        0:'零',
        1:'壹',
        2:'贰',
        3:'叁',
        4:'肆',
        5:'伍',
        6:'陆',
        7:'柒',
        8:'捌',
        9:'玖',
        }
    return switcher.get(n,'')
def NumToChar2(n):
    switcher = {
        2:'拾',
        3:'佰',
        4:'仟',
        }
    return switcher.get(n,'')

a = -9956499
str_rmb = ''
if(a<0):
    str_rmb += '负'

a = abs(a)
a = str(a)
a = list(a)
#print (a)


rmb = []
def RMBToChar(x):
    n = len(a)
    p = 0
    #print (n)
    if(n > 4):
        m = n - 4
        p = m
        n = 4
        str_m = a[0:m]
        #print (str_m)
        for i in str_m:
            s = NumToChar(int(i))
            if(s != '零'):
                s += NumToChar2(int(m))
            if(s != '零'):
                rmb.append(s)
            elif(m != 1):
                rmb.append(s)
            m -= 1
        rmb.append('万')
    str_n = a[p:]
    for j in str_n:
        s = NumToChar(int(j))
        if(s != '零'):
            s += NumToChar2(int(n))
        if(s != '零'):
            rmb.append(s)
        elif(n != 1):
            rmb.append(s)
        n -= 1
        
RMBToChar(a)

str_rmb += ''.join(rmb)
str_rmb = str_rmb.replace('零零万','万').replace('零万','万')
replace_rge = re.compile(r'零$')
str_rmb = replace_rge.sub('',str_rmb)
str_rmb = replace_rge.sub('',str_rmb)
str_rmb = str_rmb.replace('零零','零') + '圆'

print (str_rmb)


# 两个数的公约数个数-------------------------------------------------------------
a = 24
b = 36

# 先求最大公约数
def GCD(a,b):
    if(a < b):
        d = a
        a = b
        b = d
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

# 对最大公约数进行分解因子
gcd = GCD(a,b)
print (gcd)
def YZ(x):
    total = 0
    for i in range(1,x + 1):
        if(x % i == 0):
            total += 1
    return total
print (YZ(gcd))


# 已知最大公约数和最小公倍数，求是哪两个数的----------------------------
# 有多组，和最小的

# 解题思路：最大公约数和最小公倍数的积也是这两个数的积

a = 3
b = 60
p = 0   # 输出是数
ab = a * b
print (ab)

L = {}
def func(x):
    i = 1
    while(i**2 < x):
        if(x%i == 0):
            L[i] = x//i
        i += 1
    if(i**2 == x):
        L[i] = i

func(ab)

s = ab
for key in L:
    if(key >= a):
        if(s > key + L[key]):
            s = key + L[key]
            p = key      


# 筛选数值  没有用到
def SX(x):
    if(x>=a and x<= b):
        return True
    else:
        return False
L = list(filter(SX,L))

SC = [p,L[p]]
print (' '.join(str(s) for s in SC))



# 单身情歌----------------------------------------------------------
# 给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE

a = "OurWorldIsFullOfLOVE"

a = a.lower()

if "love" in a:
    print ("LOVE")
else:
    print ("SINGLE")
'''


# 信息加密---------------------------------------------------------------
# 给你个小写英文字符串a和一个非负数b(0<=b<26),
# 将a中的每个小写字符替换成字母表中比它大b的字母。
# 这里将字母表的z和a相连，如果超过了z就回到了a。

a = "cagy"
b = 3

from enum import Enum

class ZMB(Enum):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7
    i = 8
    j = 9
    k = 10
    l = 11
    m = 12
    n = 13
    o = 14
    p = 15
    q = 16
    r = 17
    s = 18
    t = 19
    u = 20
    v = 21
    w = 22
    x = 23
    y = 24
    z = 25

def findZM(x):
    for name,member in ZMB.__members__.items():
        if(x == member.value):
            return name
s = ""
for i in a:
    z = ZMB[i].value
    z += b
    if(z >= 26):
        z -= 26
    s += findZM(z)

print (s)


