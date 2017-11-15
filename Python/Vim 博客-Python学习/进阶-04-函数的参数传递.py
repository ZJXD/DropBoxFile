'''
def f(a,b,c):
    return a+b+c

print (f(6,1,4))

# 关键字传递
print (f(c=4,a=6,b=1))


# 参数默认值
def fm(a,b,c=10):
    return a+b+c

print (fm(1,4))
print (fm(1,4,9))
'''

# 包裹传递的关键在于定义函数时，在相应元组或字典前加*或**。
# 包裹传递-包裹位置传递
def func(*name):
    print (type(name))
    print (name)

func(1,4,6)
dict = {'a':1,'b':2,'c':3}
func(*dict)


# 包裹传递-包裹关键字传递
def func(**dict):
    print (type(dict))
    print (dict)

func(a=1,b=9)
func(**dict)
'''

# 解包裹，即在调用的时候使用 *或者**
def func(a,b,c):
    print (a,b,c)

args = (1,3,1)
func(*args)
dict = {'a':1,'b':2,'c':3}
func(**dict)
func(*dict)

list = [2,3,4]
func(*list)
'''

# 在定义或者调用参数时，参数的几种传递方式可以混合。
# 但在过程中要小心前后顺序。基本原则是，先位置，再关键字，再包裹位置，再包裹关键字，
# 并且根据上面所说的原理细细分辨。

 

# 注意：请注意定义时和调用时的区分。包裹和解包裹并不是相反操作，是两个相对独立的过程。
