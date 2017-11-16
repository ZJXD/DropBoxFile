
'''
import jieba  
seg_list = jieba.cut("湖西路东侧，030125号灯杆旁中式快餐店前人行道石凳子上有乱堆物料")  
print ("Default Mode:", ' '.join(seg_list))


import matplotlib.pyplot as plt    
labels='frogs','hogs','dogs','logs'    
sizes=15,20,45,10    
colors='yellowgreen','gold','lightskyblue','lightcoral'    
explode=0,0,0.05,0  
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)    
plt.axis('equal')    
plt.show()


#matplotlib inline  
import numpy as np  
import matplotlib.pyplot as plt  
from pylab import *  
x = np.arange(-5.0, 5.0, 0.02)  
y1 = np.sin(x)  
plt.figure(1)  
plt.subplot(211)  
plt.plot(x, y1)  
plt.subplot(212)  
#设置x轴范围  
xlim(-2.5, 2.5)  
#设置y轴范围  
ylim(-1, 1)  
plt.plot(x, y1)
plt.show()


import numpy as np  
import matplotlib.pyplot as plt  
# evenly sampled time at 200ms intervals  
t = np.arange(0.0, 10.0, 0.5)  
# red dashes, blue squares and green triangles  
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')  
plt.show()


import matplotlib.pyplot as plt  
plt.figure(1) # 第一张图  
plt.subplot(211) # 第一张图中的第一张子图  
plt.plot([1,2,3])  
plt.subplot(212) # 第一张图中的第二张子图  
plt.plot([4,5,6])  
plt.figure(2) # 第二张图  
plt.plot([4,5,6]) # 默认创建子图subplot(111)  
plt.figure(1) # 切换到figure 1 ; 子图subplot(212)仍旧是当前图  
plt.subplot(211) # 令子图subplot(211)成为figure1的当前图  
plt.title('Easy as 1,2,3') # 添加subplot 211 的标题
plt.show()



import numpy as np  
import matplotlib.pyplot as plt  
mu, sigma = 100, 15  
x = mu + sigma * np.random.randn(10000)  
# 数据的直方图  
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)  
plt.xlabel('Smarts')  
plt.ylabel('Probability')  
#添加标题  
plt.title('Histogram of IQ')  
#添加文字  
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')  
plt.axis([40, 160, 0, 0.03])  
plt.grid(True) 
plt.show()  



n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                n=n+1
                print (i,j,k)

print ('共',n,'个不重复的数字')

'''

#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？ 
Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2
    print (n)

print ('Total of road is %f' % Sn)
print ('The tenth is %f meter' % Hn)

