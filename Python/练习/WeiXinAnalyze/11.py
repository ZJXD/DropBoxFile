# import matplotlib
# print(matplotlib.matplotlib_fname()) #将会获得matplotlib包所在文件夹

import matplotlib.pyplot as plt

#from matplotlib.font_manager import FontProperties 
#font_set = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc", size=12)

plt.clf()
plt.plot((1,2,3),(4,3,-1))
#plt.xlabel(u'横坐标',fontproperties = font_set)
#plt.ylabel(u'纵坐标',fontproperties = font_set)
plt.xlabel(u'横坐标')
plt.ylabel(u'纵坐标')
plt.show()
