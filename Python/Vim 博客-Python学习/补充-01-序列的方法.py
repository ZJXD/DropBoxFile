# 序列(sequence)，包含 元组(定值表)(tuple)，表(list)，字符串(string)是特殊的元组
# 表的元素可以修改，定值表一旦建立，元素不可更改

# 下面的内置函数（BIF）可用于序列--------------------------------------------
'''
s = [1,2,3,4,5]

print('s len:',len(s))          # 返回：序列中包含元素的个数
print('s min:',min(s))          # 返回：序列中最小的元素
print('s max:',max(s))          # 返回：序列中最大的元素
print('s all:',all(s))          # 返回：True，如果所有的元素都为True的话
print('s any:',any(s))          # 返回：Ture，如果任一元素为True的话

# 查询功能，不改变序列本身

print('s sum:',sum(s))          # 返回：序列中所有元素的和

# x为元素值
x = 3
print('x in s count:',s.count(x))          # 返回：x在s中出现的次数
print('x in s first:',s.index(x))          # 返回：x在s中第一次出现的下标
'''

# 由于定值表的元素不可变，下面方法只适用于表----------------------------------
'''
l = [2,3,4]
l2 = [6,8]
l.extend(l2)            # 在表l末尾添加表l2所有元素
print('l add l2:',l)
l.append(7)             # 在l的末尾附加7
print('l add 7',l)
l.sort()                # 对l中的元素排序
print('l sort',l)
l.reverse()             # 将l中的元素逆序
print('l reverse',l)
l.pop()                 # 返回最后一个元素，并删除
print('l remove last',l)
del l[2]                # 删除元素
print('from l delete 2',l)
'''

# 字符串的一些方法--------------------------------------------------------------
# 尽管字符串是特殊的定值表，但是有一些方法会改变字符串。
# 这些方法的本质不是对字符串的本身进行操作，而是删除原有的，建立新的，和定值表的特点不矛盾

str = 'adbde sads hbbs'
sub = 'ad'
s = ['a','b','e']
'''
print('sub in str count:',str.count(sub))       # 返回：sub在str中出现的次数
print('sub in str first index:',str.find(sub))  # 返回：sub在str中第一次出现的位置，不存在为-1
print('sub in str first index:',str.index(sub)) # 返回：sub在str中第一次出现位置，不存在举错
print('sub in str right index:',str.rfind(sub)) # 返回：sub在str右边第一次出现位置，不存在未-1
print('sub in str right index:',str.rindex(sub))# 返回：sub在str右边第一次出现位置，不存在举错

print('all is alnum:',str.isalnum())            # 返回：True，如果所有的字符都是字母或数字
print('all is alpha:',str.isalpha())            # 返回：True，如果所有的字符都是字母
print('all is digit:',str.isdigit())            # 返回：True，如果所有的都是数字
print('all is title:',str.istitle())            # 返回：True，如果所有的词首字母都是大写
print('all is space:',str.isspace())            # 返回：True，如果所有的字符都是空格
print('all is lower:',str.islower())            # 返回：True，如果所有的字符都是小写字母
print('all is upper:',str.isupper())            # 返回：True，如果所有的字符都是大写字母

print('str split:',str.split())                 # 没有参数按照空格分隔，返回表
print('str split by a:',str.split('a'))         # 按照给定的字符分隔
print('str split by a ,but max 2',str.split('a',1))  # 分隔最大次数

print(str.rsplit('a'))

print('join s by str:',str.join(s))             # 将s中的元素，以str为分隔符，合并为一个字符串
print('remove sub:',str.strip(sub))             # 为空去掉两头空格，有参数去掉两头sub
print('replace sub:',str.replace(sub,'sdgh'))   # 用新的字符串替换 sub
'''

print('first upper:',str.capitalize())          # 返回：将str第一个字母大写
print('all lower:',str.lower())                 # 返回：将str的全部字母改为小写
print('all upper:',str.upper())                 # 返回：将str所有字母改为大写
print('swith str:',str.swapcase())              # 返回：将str字母大小写转换
print('str title:',str.title())                 # 返回：将str每个词的首字母大写

print('str in center:',str.center(20))          # 返回：长度为 20 的字符，str在中心，不足补空格
print('str in left:',str.ljust(20))             # 返回：长度为 20 的字符，str左对齐，不足补空格
print('str in right:',str.rjust(20))            # 返回：长度为 20 的字符，str右对齐，不足补空格
