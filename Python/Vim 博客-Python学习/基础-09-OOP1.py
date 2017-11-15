class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print (self.laugh)

    def laugh_100h(self):
        for i in range(100):
            self.show_laugh()

    def __init__ (self,input_gender):
        self.gender = input_gender
    def printGender (self):
        print (self.gender)

li_lei = Human("malt")
li_lei.printGender()
li_lei.show_laugh()


'''
__init__()是一个特殊方法
特殊方法的特点是名字前后有两个下划线
如果你在类中定义了__init__()这个方法，
创建对象时，Python会自动调用这个方法。这个过程也叫初始化。
特殊方法只接受两个参数(包括self在内)

'''
