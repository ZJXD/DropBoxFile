
'''
# for 循环
for a in [3,4.4,'life']:
    print (a)


for a in range(10):
    print(a**2)


# while 循环

i=0
while i<10:
    print (i)
    i=i+1
'''

# 中断循环
# 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
# break 停止执行整个循环

for i in range(10):
    if i==6:
        continue
    print (i)

for i in range(10):
    if i==6:
        break
    print (i)

    
