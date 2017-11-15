'''
# lambda 函数 可以利用lambda函数的语法，定义函数。
func = lambda x,y:x+y

print (func(3,4))

# 函数作为参数传递
def test(f,a,b):
    print ('test')
    print (f(a,b))

test(func,3,5)
test((lambda x,y:x**2+y),3,5)


# map() 函数 Python的内置函数，它的第一个参数是一个函数
# 在Python 3.X中，map()的返回值是一个循环对象。可以利用list()函数，将该循环对象转换成表。

re = map((lambda x:x+3),[1,3,5,7])

re1 = map((lambda x,y:x+y),[1,2,3],[6,7,8])

print (list(re),list(re1))



# filter() 函数，它的第一个参数也是一个函数对象
# 它也是将作为参数的函数对象作用于多个元素。如果函数对象返回的是True，则该次的元素被储存于返回的表中。
# filter通过读入的函数来筛选数据。
# 同样，在Python 3.X中，filter返回的不是表，而是循环对象。
def func(a):
    if a > 100:
        return True
    else:
        return False

print (list(filter(func,[10,56,101,500])))
'''


# reduce函数的第一个参数也是函数
# 但有一个要求，就是这个函数自身能接收两个参数。
# reduce可以累进地将函数作用于各个参数
import functools as fc
print (fc.reduce((lambda x,y:x+y),[1,2,5,7,9]))

# 对于 reduce 函数，还有一个可选的传递参数用于作为初始化值，
# 如果调用 reduce 函数时候没有传递这个初始值，将把序列的第一个元素作为初始化值。


print (fc.reduce((lambda x, y: x - y), (1, 2, 3, 4), 100))

print (fc.reduce((lambda x, y: x - y), (1, 2, 3, 4)))
