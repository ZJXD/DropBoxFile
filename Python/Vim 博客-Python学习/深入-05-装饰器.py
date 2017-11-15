# 装饰器(decorator)是一种高级Python语法。装饰器可以 对一个函数、方法或者类进行加工
# 在Python中我们有多种方法对函数和类进行加工，比如前面的闭包。
# 相对于其他方法，装饰器语法简单，代码可读性高，因此，装饰器在Python项目中有广泛的应用

# 装饰函数和方法-------------------------------------------------------------------------
'''
def decorator(F):
    def new_F(a,b):
        print ("input",a,b)
        return F(a,b)
    return new_F

# get square sum
@decorator
def square_sum(a,b):
    return a**2 + b**2
# get square diff
@decorator
def square_diff(a,b):
    return a**2 - b**2

print (square_sum(3,4))
print (square_diff(5,3))
'''
# 装饰器可以用 def 的形式定义，如上面代码中的 decorator
# 装饰器接收一个可调用对象作为输入参数，并返回一个新的可调用对象
# 装饰器新建了一个可调用对象，并通过调用传入的函数，来实现原有的功能

# 定义好装饰器后，就可以通过 @ 语法使用了
# 在 square_sum,square_diff 定义前调用 @decorator ，实际是将这两个函数传递给 decorator

# 在Python中变量名和对象是分离的，变量名可以指向任意一个对象
# 本质上，装饰器起到的作用就是重新指向变量名的作用，让同一个变量名指向一个新返回的可调用对象

# 如果我们有其他的类似函数，我们可以继续调用 decorator 来修饰函数，不用重复修改函数或者增加新的封装
# 这样，我们就提高了程序的可重复可利用性，并增加了程序的可读性


# 含参数的装饰器---------------------------------------------------------------------------

# 上面的装饰器默认它后面的函数是唯一参数。
# 装饰器的语法允许我们调用 decorator 时，提供其它参数，这样装饰器的编写和使用就有更大的灵活性
'''
def pre_str(pre=''):
    def decorator(F):
        def new_F(a,b):
            print (pre + "input",a,b)
            return F(a,b)
        return new_F
    return decorator

# get square sum
@pre_str('^_^')
def square_sum(a,b):
    return a**2 + b**2
# get square diff
@pre_str('T_T')
def square_diff(a,b):
    return a**2 - b**2

print (square_sum(3,4))
print (square_diff(5,3))
'''
# 上面的 pre_str 是允许参数的装饰器，它实际上是对原有的装饰器进行封装，并返回一个装饰器


# 装饰类------------------------------------------------------------------------------------------

def decorator(aClass):
    class newClass:
        def __init__(self,age):
            self.total_display = 0
            self.wrapped = aClass(age)
        def display(self):
            self.total_display += 1
            print ("total display",self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self,age):
        self.age = age
    def display(self):
        print ("My age is",self.age)

eagleLord = Bird(5)

for i in range(3):
    eagleLord.display()

# 装饰类，在上面装饰类传入的是 Bird 类，里面的 wrapped 是 Bird 的一个对象


# 装饰器的核心作用是 name binding ，这种语法是Python多编程范式的又一体现
# 大部分Python用户不怎么需要定义装饰器，但是可能会使用装饰器
