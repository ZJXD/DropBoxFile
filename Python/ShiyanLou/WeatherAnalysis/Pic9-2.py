# coding:utf-8
# 每个城市的最高温度

import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR

df_asti = pd.read_csv('./WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('./WeatherData/bologna_270615.csv')
df_cesena = pd.read_csv('./WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('./WeatherData/faenza_270615.csv')
df_ferrara = pd.read_csv('./WeatherData/ferrara_270615.csv')
df_mantova = pd.read_csv('./WeatherData/mantova_270615.csv')
df_milano = pd.read_csv('./WeatherData/milano_270615.csv')
df_piacenza = pd.read_csv('./WeatherData/piacenza_270615.csv')
df_ravenna = pd.read_csv('./WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('./WeatherData/torino_270615.csv')

# dist 是一个装城市距离海边距离的列表
dist = [df_ravenna['dist'][0],
    df_cesena['dist'][0],
    df_faenza['dist'][0],
    df_ferrara['dist'][0],
    df_bologna['dist'][0],
    df_mantova['dist'][0],
    df_piacenza['dist'][0],
    df_milano['dist'][0],
    df_asti['dist'][0],
    df_torino['dist'][0]
]

# temp_max 是一个存放每个城市最高温度的列表
temp_max = [df_ravenna['temp'].max(),
    df_cesena['temp'].max(),
    df_faenza['temp'].max(),
    df_ferrara['temp'].max(),
    df_bologna['temp'].max(),
    df_mantova['temp'].max(),
    df_piacenza['temp'].max(),
    df_milano['temp'].max(),
    df_asti['temp'].max(),
    df_torino['temp'].max()
]

# temp_min 是一个存放每个城市最低温度的列表
temp_min = [df_ravenna['temp'].min(),
    df_cesena['temp'].min(),
    df_faenza['temp'].min(),
    df_ferrara['temp'].min(),
    df_bologna['temp'].min(),
    df_mantova['temp'].min(),
    df_piacenza['temp'].min(),
    df_milano['temp'].min(),
    df_asti['temp'].min(),
    df_torino['temp'].min()
]

# dist1是靠近海的城市集合，dist2是远离海洋的城市集合
dist1 = dist[0:5]
dist2 = dist[5:10]
# 改变表的结构，现在是5个列表的集合
dist1 = [[x] for x in dist1]
dist2 = [[x] for x in dist2]
# dist对应的最高温度
temp_max1 = temp_max[0:5]
temp_max2 = temp_max[5:10]

# 调用 SVR函数，在参数中规定了使用线性的拟合函数
# 并把 C 设为1000来尽量里和数据
svr_lin1 = SVR(kernel='linear', C=1e3)
svr_lin2 = SVR(kernel='linear', C=1e3)
# 加入数据进行拟合（这一步会很久，大概10多分钟）
svr_lin1.fit(dist1, temp_max1)
svr_lin2.fit(dist2, temp_max2)
# 这里的效果和上面的改变结构一样
xp1 = np.arange(10,100,10).reshape((9,1))
xp2 = np.arange(50,400,50).reshape((7,1))
yp1 = svr_lin1.predict(xp1)
yp2 = svr_lin2.predict(xp2)

plt.figure("Temp-Dist")
plt.subplot(211)
plt.plot(dist, temp_max, 'ro')
plt.plot(xp1,yp1,c='b',label='Strong sea effect')
plt.plot(xp2,yp2,c='g',label='Light sea effect')

plt.subplot(212)
plt.plot(dist, temp_min, 'go')
plt.show()