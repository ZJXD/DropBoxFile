
'''
# 定义函数

def square_sum(a,b):
    c=a**2 + b**2
    return c

print (square_sum(3,4))


# 我们将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化
a=1

def change_integer(a):
    a=a+1
    return a

print (change_integer(a))
print (a)


# 我们将一个表传递给函数，函数进行操作，原来的表b发生变化
b=[1,2,3]

def change_list(b):
    b[0]=b[0]+1
    return b

print (change_list(b))
print (b)


def isleap(year):
    if ((year%4==0) and (year%100!=0)) or year%400==0:
        return True
    else:
        return False

print (isleap(2016))
'''
