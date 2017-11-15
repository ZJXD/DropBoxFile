print ('Hell World!')

#元组 tuple
s1=(2,1.3,'love',5.5,9,12,False)

#表 list
s2=[True,5,'smile']
#tuple和list的主要区别在于，
#一旦建立，tuple的各个元素不可再变更，而list的各个元素可以再变更。

print (s1,type(s1))
print (s2,type(s2))

#一个序列作为另一个序列的元素
s3=[1,[2,3,4,5]]

#空序列
s4=[]


print (s3,type(s3))
print (s4,type(s4))


#序列的引用
print (s1[0])
print (s3[1][2])

#list 的元素可变更，可以进行赋值
s2[1]=3.0
print (s2)


# 其他引用方式——范围引用： 基本样式[下限:上限:步长]
print (s1[:5])     # 从开始到下标4 （下标5的元素 不包括在内）

print (s1[2:])     # 从下标2到最后

print (s1[0:5:2])  # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）

print (s1[6:0:-2]) # 从后向前，步长就需要是 “-”


# 其他引用方式——尾部元素引用
print (s1[-1])     #序列最后一个元素

print (s1[-3])     #序列倒数第三个元素



#字符串可以看作元组
str='abcdefg'
print (str[2:4])
