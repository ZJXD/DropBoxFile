'''
# open() 就是循环对象
for line in open('text.txt','r'):
    print (line)


# 生成器 生成器的编写方法和函数定义类似，只是在return的地方改为yield。
# 生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。
# 当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。
# 生成器自身又构成一个循环器
def gen():
    a = 100
    yield a
    a = a*6
    yield a
    yield 1000

for i in gen():
    print (i)

def gen1():
    for i in range(4):
        yield i

'''
G = (x for x in range(4))    # 生成器表达式(Generator Expression)
print (G)

for i in G:
    print (i)

'''
# 表推导
L = []
for x in range(10):
    L.append(x**2)


M = [x**2 for x in range(10)]     # 表推导，和上面的生成器表达式类似，只不过用的是中括号

for (l,m) in zip(L,M):
    print (l,m)

xl = [1,3,5]
yl = [9,12,13]
H = [x**2 for (x,y) in zip(xl,yl) if y>10]
print (H)
'''
