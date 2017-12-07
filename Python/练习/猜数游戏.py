import random
x = random.randint(1,100)
print('你有最多十次的猜数机会，可以猜0-100之间的数字')
i=0
while i<10:
    y = int(input())
    if y > x:
        print ('您输入的数字比较大')
    elif y < x:
        print ('您输入的数字比较小')
    else:
        print ('恭喜你答对了,猜数游戏结束')
        break
    i+=1

print('小傻瓜！机会没有了-_-')
