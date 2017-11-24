# iter 是内置函数，我们可以将诸如表、字典等容器变为循环器
'''
for i in iter([2,4,5,6]):
    print (i)

# 标准库中的 itertools 包提供了更加灵活的生产循环器的工具
# 这些工具的输入大都是已有的循环器。另一方面，这些工具完全可以自行使用Python实现
# 该包只是提供了一种比较标准、高效的实现方式
# 这也符合Python “只有且最好只有解决方案”的理念


# 无穷循环器------
count(5.2)      # 从5开始的整数循环器，每次增加2
cycle('abc')    # 重复序列的元素，即a,b,c,a,b,c……
repeat(1.2)     # 重复1.2，构成无穷循环器，即1.2,1.2,……，也可以设置重复次数
'''

# 函数式工具----------------------

# 函数式编程是将函数本身作为处理对象的编程范式，在Python中，函数也是对象
# 因此可以轻松的进行一些函数式的处理，比如 map(),filter(),reduce
# itertools 包含类似的工具
'''
from itertools import *

rlt = map(pow,[1,2,3],[1,2,3])   # 让 pow 依次作用于后面的列表

for num in rlt:
    print(num)

sta = starmap(pow,[(1,2),(2,2),(3,3)])  # 让 pow 依次作用于表的每个tuple

for s in sta:
    print(s)
    '''

# 这些函数都可以在循环一节找到

# 组合工具-------------------

# chain([1,2,3],[4,5,6])      # 连接两个循环器成为一个
# product('abc',[1,2])        # 多个循环器集合的笛卡尔积，相当于嵌套循环
# permutations('abc',2)       # 从“abc”中挑选两个元素，返回所有，一个循环器
# combinations('abc',2)       # 通上面一个，上面一个不分顺序，这个ab，ba就返回一个
# combinations_with_replacement('abc',2) # 和上面类似，参数可以重复
'''
from itertools import *
for m,n in product('abc',[1,2]):
    print(m,n)

for a in permutations('abcd',2):
    print(a)

print('123')
for a in combinations('abcd',2):
    print(a)

print('222')
for a in combinations_with_replacement('abcd',2):
    print(a)
'''

# groupby()------------------------------
# 将key函数作用于原循环器的各个元素，根据key函数的结果，将拥有相同函数结果的元素
# 分到一个新的循环器，每个循环器一函数返回结果为标签。
# 这就好像一群人的身高作为循环器，我们可以使用这样一个key函数：
# 如果身高大于180，返回“tall”，如果身高低于160，返回“short”，其他返回“moddle”
# 这样就将所有的身高分成三个循环器

from itertools import *
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191,158,159,165,170,177,181,182,190]
#friends = sorted(friends,key = height_class)
#print(friends)
for m,n in groupby(friends,key = height_class):
    print(m)
    print(list(n))

# 注意，使用groupby的功能类似于UNIX中的uniq。
# 分组前需要使用 sorted() 对原有循环器的元素，对key函数进行排序，让同组元素在位置上靠拢
