# 上下文管理器，用于规定某个对象的使用范围
# 一旦进入或者离开该使用范围，会有特殊操作被调用（比如为对象分配或者释放内存）
# 它的语法形式是 with...as...

'''
f = open("data/new.txt","w")

print (f.closed)

f.write("Hello World!")
f.close()

print (f.closed)
'''
# 这两个效果一样，但是使用起来方便

with open("data/new.txt","a") as f:
    print (f.closed)
    f.write("Hello World!\n")
print (f.closed)


# 上下文管理器基于 f 对象的 __exit__() 特殊方法
# 使用上下文管理器，实际上要求 Python 在进入程序块之前调用对象 __enter__() ，结束调用 __exit__()


# 任何定义了 __enter__() 和 __exit__() 的都可以使用上下文管理器
