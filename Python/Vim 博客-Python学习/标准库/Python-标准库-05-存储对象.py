# 存储对象（pickle包，cPickle包）-----------------------------------------

# 计算机的内存中存储的是二进制的序列（当然，在Linux眼中，是文本流）
# 我们可以直接将某个对象所对应位置的数据抓取下来，转成文本流（serialize）
# 再将文本流存入文件
# 由于Python在创建对象时，要参考对象的类定义，所以当我们从文本中读取对象时，
# 必须要有该对象的类定义，才能懂得如何去重建这一对象。
# 从文件读取时，对应Python的内建（built-in）对象（比如说整数、词典、表等等）
# 由于其类定义已经载入内存，所以不需要我们再在程序中定义类。
# 但对于用户自定义的对象，就必须先定义类，然后才能从文件中载入对象


# 将内存中的对象转换成文本流--------------------

import pickle

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
'''
summer = Bird()
#picklestring = pickle.dumps(summer)    # 将对象转换成文本流

#print(picklestring)
fn = 'a.pkl'
with open(fn,'wb+') as f:
    pic = pickle.dump(summer,f)        # 将对象summer存储在文件a.pkl
'''
    
# 重建对象----------------------------------------
# 要重建对象，首先要从文本中读出文本，存储到字符串
# 然后使用 pickle.loads(str)，将字符串转成对象
# 要记住，此时我们的程序中必须已经有啦该对象的类定义

fn = 'a.pkl'
with open(fn,'rb') as f:
    summer = pickle.load(f)
print(summer)


# cPickle 包----------------

# 这个和上面的包几乎完全相同，这个是用C语言编写，速度是上面的1000倍

import cPickle as pickle

