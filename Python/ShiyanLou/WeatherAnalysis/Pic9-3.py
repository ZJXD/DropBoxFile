# coding:utf-8
# 风向分析-风向频率玫瑰图

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

# plt.plot(df_ravenna['wind_deg'], df_ravenna['wind_speed'], 'ro')
# plt.show()

def showRoseWind(values,city_name,max_value):
    N = 8

    # 生成一个没四分之一pi 的列表
    theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
    radii = np.array(values)

    # 绘制极区图的坐标系
    plt.figure('WindRose')
    plt.axes([0.025, 0.025, 0.95, 0.95], polar = True)

    # 每个扇区的颜色rgb值，x越大，对应的color越接近蓝色
    colors = [(1 - x/max_value, 1 - x/max_value, 0.75) for x in radii]

    # 画出每个扇形区
    #plt.bar(theta, radii, width = (2*np.pi/N),left = 0.1, bottom = 0.1, right = 0.1, top = 0.1, color = colors)
    plt.bar(theta, radii, width = (2*np.pi/N), bottom = 0.0, color = colors)
    plt.title(city_name, x = 0.2, fontsize = 20)
    #plt.subplots_adjust(left = 0.3, bottom = 0.1, right = 0.95, top = 0.95)
    plt.show()

hist, bins = np.histogram(df_ravenna['wind_deg'], 8, [0,360])
showRoseWind(hist, 'Ravenna', max(hist))
# print(hist,bins)