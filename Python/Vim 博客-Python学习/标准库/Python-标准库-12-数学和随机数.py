# math ----------------------------------------
# math 包主要处理数学相关运算，math包含两个常数
'''
math.e     # 自然常数e
math.pi    # 圆周率pi

# 运算函数
math.ceil(x)    # 对x向上取整，比如 x = 1.2，返回2
math.floor(x)   # 对x向下取整，比如 x = 1.2，返回1
math.pow(x,y)   # 指数运算，得到x的y次方
math.log(x)     # 对数，默认基地为e，可以使用 math.log(100,base=10)
math.sqrt(x)    # 平方根

# 三角函数，这些函数接收的是一个弧度（radian）为单位的参数
math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)

# 角度和弧度互换
math.degrees(x)
math.radians(x)

# 双曲函数
math.sinh(x)
math.cosh(x)
math.tanh(x)
math.asinh(x)
math.acosh(x)
math.atanh(x)

# 特殊函数
math.erf(x)
math.gamma(x)

# random包-------------------------------------

# 如果你已经了解伪随机数的原理，那么你可以使用如下：
random.seed(x)
# 来改变随机数生成器的种子seed

# 随机挑选和排序
random.choice(seq)    # 从序列的元素中随机挑选一个元素
random.sample(seq,k)  # 从序列中随机挑选k个元素
random.shuffle(seq)   # 将序列的所有元素随机排序

# 随机生成实数，生成的实数符合均匀分布，意味着某个范围内的每个数字出现概率相等
random.random()       # 随机生成下一个实数，在[0,1]范围内
random.uniform(a,b)   # 随机生成下一个实数，在[a,b]范围内

# 随机生成符合其他分布
random.gauss(mu,sigma)    # 随机生成符合高斯分布随机数，mu,sigma为高斯分布两个参数
random.expovariate(lambd) # 符合指数分布的随机数，lambd为指数分布参数
'''

# 随机排出场顺序---
import random
'''
all_per = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']

random.shuffle(all_per)

for i,name in enumerate(all_per):
    print(str(i) + ':' +name)
    '''

# 选出1-22中不重复的5数字
'''
l = random.sample(range(1,23),5)
l.sort()
print (l)
'''

# 随机产生8为数字，每位是1-6中的一个

l = []
for i in range(8):
    l.append(random.choice(range(1,7)))

print(l)

