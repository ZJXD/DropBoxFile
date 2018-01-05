# coding:utf-8
# 每个城市的温度折线图

import numpy as np
import pandas as pd
import datetime

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

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

# 读取温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

# 把日期从 string 类型转化为标准的 datetime 类型
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
day_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

# 调用 subplots() 函数，重新定义 fig, ax 变量，fig 是图像对象，ax 是坐标轴对象
fig, ax = plt.subplots()
#plt.figure('Weather')
# 调整x轴坐标刻度，使其旋转70度，方便查看
plt.xticks(rotation=70)

# 设定时间格式
hours = mdates.DateFormatter('%H:%M')

# 设定X轴显示的格式
ax.xaxis.set_major_formatter(hours)
ax.set_title('Test')
ax.set_xlabel('Time')

#这里需要画出三根线，所以需要三组参数， 'g'代表'green'
ax.plot(day_ravenna,y1,'r',day_faenza,y2,'r',day_cesena,y3,'r')
ax.plot(day_milano,y4,'g',day_asti,y5,'g',day_torino,y6,'g')
plt.show('Weather')