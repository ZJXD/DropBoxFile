'''
# 山峰的个数-----------------------------------------------------------------
# 根据记录的高程，判断山峰的个数 (序列两端不算山峰)
h=[0.9,1.2,1.22,1.1,1.0,1.6,0.99]

def SF(s):
    sf = 0
    for i in range(1,len(s)-1):
        if(s[i] > s[i - 1] and s[i] > s[i + 1] ):
            sf += 1
    return sf
print (SF(h))


# 三角形形状
# 根据三边长，判断形状

a = 3
b = 5
c = 9

def SJX(x,y,z):
    S = [x,y,z]
    S.sort()
    if(S[2] >= S[1] + S[0]):
        return "W"
    elif(S[2]**2 > S[1]**2 + S[0]**2):
        return "D"
    elif(S[2]**2 == S[1]**2 + S[0]**2):
        return "Z"
    elif(S[2]**2 < S[1]**2 + S[0]**2):
        return "R"

print (SJX(a,b,c))


# 大幂次运算------------------------------------------------------------------
# a 底数， n 指数,最后一个取模的值
a = 66666
n = 55443300

x = pow(a,n,20132013)

print (x)


# 密码生成
# 两个正整数a和b, 利用a / b我们会到的一个长度无限的小数
# 将该小数点后第x位到第y位的数字当做密码
a = 1
b = 2
x = 1
y = 4

s = str(float(a)/b)
s = s.split('.')[1]

if(len(s) < y):
    while(len(s) < y):
        s += "0"

m = s[x-1:y]

print (m)


# 最大连续子序列----------------------------------------------------------------
# 还有问题（继续）

L=[2,-3,3,-4,50,-30,21,9,-6]

def MaxL(S):
    maxT = 0
    thisT = 0
    maxS = []
    thisS = []
    for i in S:
        thisT += i
        thisS.append(i)
        if(thisT < 0):
            thisT = 0
            thisS = []
        elif(thisT >= maxT):
            maxT = thisT
            maxS = thisS[:]

    return maxT

print (MaxL(L))


# 最大非连续子序列------------------------------------------------------------
# 未作出来
L=[2,-3,3,-4,50,-30,9,21,-6]

def MaxFL(S):
    maxT = 0
    b = True
    for i in S:
        if(i > 0 ):
            if(b):
                maxT += i
                b = not b
            else:
                b = not b
        else:
            b = not b
    return maxT

print (MaxFL(L))


# 勾股定理------------------------------------------------------------------

a = 3
b = 4

import math
c = math.sqrt(a**2 + b**2)

print ("%.3f"%(c))
'''


# 简单字符连接

L=['abc','d','efg']

print ("".join(str(s) for s in L))

print (" ".join(str(s) for s in L))
