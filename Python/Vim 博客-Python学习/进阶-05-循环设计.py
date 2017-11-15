'''
# range 函数的使用
S = 'abcdefghijklmn'

for i in range(0,len(S),2):
    print (S[i])


# enumerate 函数的使用
# 实际上，enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)
S = 'abcdefghijklmn'
for (index,char) in enumerate(S):
    print (index)
    print (char)
'''


# zip 函数使用，等长的序列，每次循环从各个序列取出一个

ta = [1,2,3]
tb = [9,7,6]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print ({a,b,c})

zipped = zip(ta,tb)
print ((zipped))

na,nb = zip(*zipped)
print (na,nb)
