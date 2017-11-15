'''
# 原因是在python 3.x中
# generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了
L = list(range(5))
print (L)
re = iter(range(5))

for i in range(100):
    print (re.__next__())

print ('HaHaHaHaHa')



# 对上面的进行修改，对可能出问题的地方进行 try
re = iter(range(5))

try:
    for i in range(100):
        print (re.__next__())
except StopIteration:
    print ('Here is end',i)

print ('HaHaHaHa')


# try 的层层比较
try:
    print (a**2)
except TypeError:
    print ("TypeError")
except:
    print ("Not Type Error & Error noted")


# 没有合适的 except，异常向上抛出
def test_func():
    try:
        m = 1/0
    except NameError:
        print ("Catch NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print ("Catch error in the main program")
'''

'''
try 流程如下，

try->异常->except->finally

try->无异常->else->finally

# 自己抛出异常
print ('LaLaLa')
raise StopIteration
print ('HaHaHa')

'''

def func(x):
    try:
        x = x+1
        return x
    finally:
        return x+1

print (func(11))
