# Py 数-------------------------------------------------------------------
# 一个十进制的4位数，其对应的十六进制、十二进制的和一样
'''
n = 9999


def Py(x):
    s = 0
    for i in str(x):
        s += int(i)
    s_16 = 0
    a = x
    while(a>0):
        s_16 += a%16
        a = a//16

    if(s != s_16):
        return "No"

    s_12 = 0
    b = x
    while(b>0):
        s_12 += b%12
        b = b//12

    if(s != s_12):
        return "No"

    return "Yes"

print (Py(n))



# 分拆素数和------------------------------------------------------------------
# 分拆成两个不同的素数的和，有多个都输出



# 斐波那契数列----------------------------------------------------------------
# 数列从第三个数起是前两个的和

n = 6

a = 1
b = 0

for i in range(1,n+1):
    if(i == 1 or i ==2):
        a = 1
        b = 1
    else:
        c = a
        a = a + b
        b = c

print (a%20132013)



# 超级楼梯-------------------------------------------------------------------

n = 4
def a(x):
    if(x>2):
        return a(x-1)+a(x-2)
    else:
        return x

print (n)
'''

# 砝码问题------------------------------------------------------------------
# w 中砝码的重量， n 砝码的数量
from functools import reduce

w=[1,2]    # 每个重量
n=[2,1]    # 对应的数量

P = [[w[i]*k for k in range(n[i]+1)] for i in range(len(w))]

print(P)
def set_sum(a,b):
    return [m+n for m in a for n in b]
L = reduce(set_sum,P)
print(L)
print(len(set(L)))


'''
# 取石子，威佐夫博弈--------------------------------------------------------

a = 3
b = 1

if(a < b):
    a,b = b,a
k = a - b

a = (int)(k*(1+5.0**0.5)/2.0)

if(a == b):
    print ('Loose')
else:
    print ('Win')


# 杨辉三角-------------------------------------------------------------------
# 给一个正整数 n ，给出杨辉三角的前 n 层

n = 5
L_t = []
for i in range(1,n+1):
    L = L_t
    L_t = []
    if(i == 1):
        L_t.append(1)
    else:
        for m in range(1,i+1):
            if(m == 1):
                L_t.append(1)
            elif(m == i):
                L_t.append(1)
            else:
                L_t.append(L[m - 2] + L[m - 1])
    print (' '.join(str(a) for a in L_t))

'''
