# 语言的内存管理是语言设计的一个重要方面，它决定语言性能的重要因素。
# 无论是C语言的手工处理，还是Java的垃圾回收，都成为语言的最重要特征
# 这里以Python语言为例子，说明一门动态类型的，面向对象的语言的内存管理方式


# 对象的内存使用---------------------------------------------------------------------------
# 赋值语句是语言最常见的功能了。但即使是最简单的赋值语句，也很有内涵
# Python 的赋值语句就很值得研究

# 整数 1 是一个对象，而 a 是一个引用。利用赋值语句，引用 a 指向对象 1.
# Python 是动态类型语言，对象与引用分离，Python像使用“筷子”那样，通过引用来接触和翻动真正的食物--对象
'''
a = 1
b = 1

print (id(a))
print (hex(id(a)))
print (id(b))

# 为了探索对象在内存的存储，我们可以求助于Python的内置函数 id()
# 上面返回的是对象的身份（identity），这里的身份就是对象的 内存地址

print (a is b)

a = "good"
b = "good"

print (a is b)

a = "very good morning"
b = "very good morning"
print (a is b)

a = []
b = []
print (a is b)

# 在Python中可以用 is 判断两个引用所指的对象是否相同
# 从上面的语句可以看到，这些有些是指向同一个引用的，有些则不是

# 在 Python 总，每个对象都有存指向该对象的引用的总数，即 引用计数（reference count）
# 可以使用 sys 包中的 getrefcount() ，来查看某个对象的引用计数。
# 需要注意的是，在使用某个引用作为参数传递给 getrefcount() 时，参数实际上创建了一个临时引用，所以结果多 1
from sys import getrefcount

a = [1,2,3]
print (getrefcount(a))

b = a
print (getrefcount(b))
'''

# 对象引用对象-------------------------------------------------------------------------------------
'''
class from_obj(object):
    def __init__(self,to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print (id(a.to_obj))
print (id(b))

# 对象引用对象，是Python最基本的构成方式。
# 当一个对象  A 被另个一个对象 B 引用时，A 的引用计数增加1

from sys import getrefcount

print (getrefcount(a.to_obj))
print (getrefcount(b))


# 容器对象的引用可能构成很复杂的拓扑结构，可以用 objgraph 包来绘制其引用关系

x = [1,2,3]
y = [x,dict(key1=x)]
z = [y,(x,y)]

import objgraph
objgraph.show_refs([z],filename='ref_topo.png')
'''

# 引用减少----------------------------------------------------------------------
# 某个对象的引用计数可能减少，比如，可以使用 del 关键字删除某个引用
'''
from sys import getrefcount

a = [1,2,3]

b = a

del a[0]
print (a,b)

print (getrefcount(b))

del a
print (getrefcount(b))

# 如果指向对象 A 的引用重新指向其它对象 B ，对象A的引用计数就减少

a = b
print (getrefcount(b))

b = 1
print (getrefcount(a))
print (a,b)
'''

# 垃圾回收--------------------------------------------------------------------

# 吃太多，总会变胖，Python也是这样，当Python中的对象越来越多，他们将占据越来越多内存
# 不过你不用担心，Python会在适当的时候“减肥”,启动垃圾回收（garbage collection）
# 许多语言都有垃圾回收机制，虽然最终的目的都是为了“减肥”，但是不同语言有差异

# 从原理上，当Python的某个对象的引用计数将为0时，说明没有任何引用指向该对象，该对象就要成为被回收的对象

# 某一个对象被删除后，已经没有任何引用指向该对象，用户就不能通过任何方式接触或动用这个对象
# 这个对象如果继续在内存中就成了不健康的脂肪。
# 当垃圾回收启动时，Python扫描到这个引用计数为0的对象，就将它所占据的内存清空

# 但是，减肥是个昂贵而费力的事情，垃圾回收时，Python做不了其他的任务。频繁垃圾回收降低效率
# 如果内存中的垃圾不多，就没有必要启动垃圾回收，所以Python只会在特定条件下，自动启动垃圾回收

# Python在运行时，会记录分配对象（object allocation）和取消分配对象（object deallocation）次数
# 当两者的差值高于某个“阈值”时，垃圾回收才会启动

import gc
print (gc.get_threshold())  # 查看阈值

gc.set_threshold(1000,10,10)   # 设置阈值

print (gc.get_threshold())

# 分代回收----------------------------------------------------------------------------

# Python 同时采用了分代(generation)回收的策略
# 这个策略的基本假设是，存活越久的对象，越不可能在后面的程序中变成垃圾
# 我们的程序往往会产生大量的对象，许多对象很快产生和消失，但也有一些对象长期被使用
# 出于信任和效率，对于这样的“长寿”对象，我们信任他们的用处，所以减少垃圾回收对它的扫描频率

# Python将所有的对象分为0,1,2三代。所有的新建对象都是0代对象，
# 当某一代对象经历过垃圾回收，没有被回收的对象被归入下一代对象
# 垃圾回收启动时，一定会扫描所有的0代对象。
# 如果0代对象经历过一定“次数”垃圾回收，那么就启动对0代和1代的扫描清理
# 当1代也经历了一定“次数”的垃圾回收，那么0,1,2都会被扫描

# 这里的两个“次数”就是上面的阈值的后面两个

# 孤立的环引用-------------------------------------------------------------------------

# 引用环的存在会给上面的垃圾回收带来很大的困难
# 这些引用环可能构成无法使用，但会有引用计数不为0的对象
