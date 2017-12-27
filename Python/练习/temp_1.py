# coding:utf-8
# 一年365天，工作值初始值1.0，工作一天工作值增加N，不工作不下降，一周连续工作4天
# 一年下来工作值

n = 365
N = 0.001

z = 1.0

w = n//7
d = n%7

for i in range(w*4):
    z = z * (1 + N)

print(z,z*(1+N))
#print(w,d)
