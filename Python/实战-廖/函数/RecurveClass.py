# coding:utf-8
# 递归函数

# 如果一个函数在内部调用自身本身，这个函数就是递归函数
# 举阶乘的例子，用函 fact(n)，可以看出 fact(n) = fact(n-1)*n
# 在 n =1 的时候特殊处理下，得到如下的

'''
def fact(n):
    if n == 1:
        return 1
    return n*fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(50))
'''


# 递归函数的有点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
# 使用递归函数需要注意防止栈的益出。在计算机中，函数的调用是通过栈(stack)这种数据结构实现的，
# 每当进入一个函数调用，栈就增加一层栈帧，每当函数返回，栈就减少一层栈帧。
# 由于栈的大小不是无限的，所有递归调用的次数过多，会导致栈溢出

# print(fact(1000))  # 会报错

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以把循环看成是一种特殊的尾递归也是可以的
# 尾递归是指，在函数返回的时候，调用自身本身，并且，reture 语句不能包含表达式
# 这样编译器或者解释器就可以把尾递归做优化，使递归本身无论调多少次，都只占用一个栈帧，不会出现溢出的情况

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(1000))

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以上面的还是会报错
