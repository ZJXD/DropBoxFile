# 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好

# 取一个list 或者 tuple的部分元素是非常常见的操作

'''
L = ['M', 'S', 'T', 'B', 'J']

# 取取前三个
print([L[0],L[1],L[2]])  # 笨方法，取前N个的话，就没辙了

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)                 # 用循环的方法，但是这样经常取指定范围的操作，用循环十分繁琐

print(L[0:3])            # Python提供了切片(Slice)操作，能大大简化这种操作

# L[0:3] 表示，从索引0开始取，直到索引3为止，但不包括3
# 如果第一索引是 0 ，还可以简写

print(L[-2:],L[-2:-1])
# Python 支持取倒数第一个元素，那么同样支持倒数切片
'''

'''
def trim(s):
    while(s[:1]) == ' ':
        s = s[1:]
    while(s[-1:]) == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
