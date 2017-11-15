'''
# 回文字符串------------------------------------------------------------------
# 回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".

a = "lkldjlljksombdo"
n = 4

# 字符串的逆序
def NX(x):
    b = x[len(x):0:-1]
    b = b + x[0]
    return b

def CalNX(s):
    if(n > len(s)):
        return "NO"
    for i in range(n,len(s)+1):
        s_t = s[i - n:i]
        if(s_t == NX(s_t)):
            return "YES"
    return "NO"

print (CalNX(a))



# 时间就是金钱：时间间隔的秒数--------------------------------------------------
st = "00:00:00"
et = "00:00:10"

import time
import datetime

a = time.strptime(st,'%H:%M:%S')
b = time.strptime(et,'%H:%M:%S')

d1 = datetime.datetime(*a[:6])
d2 = datetime.datetime(*b[:6])

print ((d2-d1).seconds)


# 润年-------------------------------------------------------------------------
# 润年是四年一润，百年不润，四百年再润
year = "2100"

year = int(year)

# 计算润年
def RN(n):
    if(n % 4 == 0):
        if(n % 100 == 0):
            if(n % 400 ==0):
                return 366
            return 365
        else:
            return 366
    else:
        return 365

print (RN(year))


# 一马当先
# 象棋中的马走日，给定一个N行M列的棋盘，最少多少步到右上角

# 解题分析：走的日，也就是走：一行两列（横向），两行一列（竖向）
# 分析知：行列数满足的条件是：一个不能是另一个的2倍以上，行列数是2倍的
# 行列数的和是 3 的倍数的可以
n = 11
m = 13

# 计算步数
def BS(a,b):
    if(a/b > 2 or b/a > 2):
        return -1
    elif((a + b) % 3 !=0):
        return -1
    else:
        return (a + b)//3


print (BS(n,m))


# 格式化时间--------------------------------------------------------------
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

import time

L = ['year','month','day','hour','minute','second']
L_t = []
for n in L:
    for (k,v) in t.items():
        if(n == k):
            L_t.append(v)
tim = "".join(str(s) for s in L_t)
d = time.strptime(tim,'%Y%m%d%H%M%S')

print (time.strftime('%Y-%m-%d %H:%M:%S',d))


# 序列判断------------------------------------------------------------------
# 给一个 list 看是升序还是降序
# sorted 升序，原数组不变，返回新的数组,a.sort():在原基础变化

L = [90,53,34,21,19,5]

L_s = sorted(L)
L_j = sorted(L,reverse = True)

def XL(x):
    if(x == L_s):
        return "UP"
    elif(x == L_j):
        return "DOWN"
    else:
        return "WRONG"
    
print (XL(L))


# 加油站------------------------------------------
# 加油站编号：0,1,2,3……n-1
# 加油上限：limit , limit[i]
# 到下一个加油站需要的油：cost[i]

n = 10
limit = [6,5,8,4,9,3,9,3,6,8]
cost = [5,7,2,9,7,5,3,7,9,10]

# x:加油站数量，y:加油量，z:用油量
def JYZ(x,y,z):
    for i in range(x):
        m = 0
        yl = 0  # 油量
        # print ("i :",i)
        while(m < n):
            yl = yl + y[(i + m) % n] - z[(i + m) % n]
            # print (yl)
            if(yl >= 0):
                m += 1
            else:
                break
        if(yl >= 0):
            return i
    return -1

print (JYZ(n,limit,cost))


# 相同是数字-------------------------------------------------------------------
# 给一个数组，是否存在相同的数字

L = [1,2,63,7,3]

def Con(x):
    for i in x:
        if(x.count(i)>1):
            return "YES"
    return "NO"

print (Con(L))
'''

# 判断三角形------------------------------------------------------------------
a = 3
b = 6
c = 5

def SJX(x,y,z):
    L = [x,y,z]
    for i in range(len(L)):
        if(L[(i-1)%3] + L[(i+1)%3] <= L[i] or L[(i-1)%3] - L[(i+1)%3] >= L[i]):
            return "NO"
    return "YES"

print (SJX(a,b,c))

print ("Happy")
