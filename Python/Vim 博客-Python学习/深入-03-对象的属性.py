# Python 一切皆对象（object），每个对象都可能有多个属性(attribute).
# python 的属性有一套统一的管理方案

# 属性的 __dict__ 系统-----------------------------------------------

# 对象的属性可能来自于其类定义，这一类叫做“类属性”(class attribute).
# 类属性可能来自类定义自身，也可能根据定义继承来的

# 对象的属性可能是该对象实例定义的，叫做对象属性(object attribute)

# 对象的属性存储在对象的 __dict__ 属性中， __dict__ 是一个词典，建为属性名，值为属性本身


# 下面的类和对象，chicken 类继承自 bird 类，summer 是 chicken 类的一个对象
'''
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self,age):
        self.age = age

summer = chicken(2)

print (bird.__dict__)
print (chicken.__dict__)
print (summer.__dict__)
'''

# 从上面打印出的各个类或者对象实例的属性，可以看出：Python 中的属性是分层定义的
# 比如这里分为 object/bired/chicken/summer 这四层。当我们需要调用某个属性的时候，
# Python 会一层层的向上遍历，直到找到那个属性（如果属性被不同的层重复定义，会取先遇到的那一个，就是比较底层的属性定义）
# __dict__ 分层存储，每一层只存储该层新增的属性，子类不需要重复存储父类中的属性


# 特性----------------------------------------------------------------

# 同一个对象的不同属性之间可能存在依赖关系。当某个属性被修改时，希望依赖于该属性的其他属性也发生变化
# 这时，我们就不能通过 __dict__ 的方式来静态存储属性。
# Python 提供了多种即时生成属性的方法，其中一种称为“特性”(property),其为特殊是属性
'''
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self,age):
        self.age = age
    def getAdult(self):
        if(self.age > 1.0):
            return True
        else:
            return False
    adult = property(getAdult)

summer = chicken(2)

print (summer.adult)

summer.age = 0.6
print (summer.adult)
'''

# 特性使用内置函数 property() 来创建。property() 最多可以加载四个参数。
# 前三个为函数，分别是处理查询特性、修改特性、删除特性，最后一个参数为特性文档，说明作用
'''
class num(object):
    def __init__(self,value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self,value):
        self.value = -value
    def delNeg(self):
        print ("value also deleted")
        del self.value
    neg = property(getNeg,setNeg,delNeg,"I'm negative")

x = num(1.1)

print (x.neg)

x.neg = -22

print (x.value)

print (num.neg.__doc__)

del x.neg
'''

# 使用特殊方法 __getattr__-------------------------------------------------
# 我们可以用 __getattr__(self,name) 来查询即时生成的属性
# 查询一个属性，通过 __dict__ 找不到的时候，Python 会调用对象 __getattr__ ,来查询即时生成的属性


class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self,age):
        self.age = age

    def __getattr__(self,name):
        if(name == 'adult'):
            if(self.age > 1.0):
                return True
            else:
                return False
        else:
            raise AttributeError(name)

summer = chicken(2)

print (summer.adult)
summer.age = 0.5
print (summer.adult)
print (summer.male)
