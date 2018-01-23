# 加这行不用使用plt.show(),就可以直接显示
# %matplotlib inline

# -*-coding=utf-8-*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# from matplotlib.font_manager import FontProperties 
# font_set = FontProperties(fname=r"C:\Windows\Fonts\simkai.ttc", size=12)

display_columns = ["title","read_num","like_num","comment_num","reward_num","p_date"]

# 读取数据
df = pd.read_csv("post.csv", encoding="utf-8")

# 重新设置序列顺序
df = df.reindex(columns = display_columns)
# 将p_date的数据类型从timestamp转换成datetime
df.p_date = pd.to_datetime(df['p_date'])
df.head()

# print(df)

# 数据的总体概览，各个指标的总和、均值、最小、最大等
# print(df.describe())
# 总数
# print(df.read_num.sum())

# 获取阅读量最高的10篇文章-------------------------------------------------
# 根据阅览数排序，ascending 表示降序
# top_read_num_10 = df.sort_values(by = ['read_num'], ascending = False)[:10]
# top_read_num_10 = top_read_num_10[display_columns]
# # 重置行索引，drop表示删除原来的行索引
# top_read_num_10.reset_index(drop = True)
# ax = top_read_num_10.plot(x = 'title', y = 'read_num', kind = 'barh', figsize = (9,6), fontsize = 15)
# ax.set_title("阅读量Top10", fontsize = 20)
# ax.set_ylabel("", fontsize = 16)
# ax.set_xlabel("阅读量", fontsize = 16)
# ax.legend().set_visible(False)
# plt.show()

# 文章阅读量随时间变化曲线--------------------------------------------------
# ax = df.plot(y = 'read_num', x = 'p_date', figsize = (9,6))
# ax.set_title("文章阅读量趋势", fontsize = 20)
# ax.set_ylabel("阅读量", fontsize = 16)
# ax.set_xlabel("时间", fontsize = 16)
# # 隐藏图例
# #ax.legend().set_visible(False)
# plt.show()

# 每年文章数量柱状图-----------------------------------------------------
# year_df = df.groupby(df.p_date.dt.year).size().reset_index(name = 'total')
# ax = year_df.plot(x = 'p_date', y = 'total', kind = 'bar', figsize = (9,6), fontsize = 15)
# ax.set_title("年发表文章数", fontsize = 20)
# ax.set_ylabel("文章数", fontsize = 16)
# ax.set_xlabel("", fontsize = 16)
# ax.legend().set_visible(False)
# # 柱状上面显示数字
# for p in ax.patches:
#     ax.annotate(str(p.get_height()), xy = (p.get_x() + 0.2, p.get_height() + 1))
# plt.show()

# 文章与赞赏---------------------------------------------------------
# 赞赏前10的 这里的 kind 用 “barh” 表示横向的条形图
# top_reward_num = df.sort_values(by = ['reward_num'], ascending = False)[:10]
# top_reward_num = top_reward_num[display_columns]
# top_reward_num.reset_index(drop = True)
# ax = top_reward_num.plot(x = 'title', y = 'reward_num', kind = 'barh', figsize = (9,6), fontsize = 14)
# ax.set_axes([0.2,0.11,0.7,0.77])
# ax.set_title("赞赏Top10", fontsize = 20)
# ax.set_ylabel("", fontsize = 16)
# ax.set_xlabel("赞赏数", fontsize = 16)
# ax.legend().set_visible(False)
# plt.show()

# 文章与点赞---------------------------------------------------------
# 散点图 这里的 kind 用 “scatter” 表示用散点图
ax = df.plot(kind = "scatter", y = 'like_num', x = 'read_num', s = 10, figsize = (9,6), fontsize  =14)
ax.set_title("阅读量与点赞数", fontsize = 20)
ax.set_xlabel("阅读量", fontsize = 16)
ax.set_ylabel("点赞数", fontsize = 16)

z = np.polyfit(df.read_num, df.like_num, 1)
p = np.poly1d(z)
plt.plot(df.read_num, p(df.read_num), "r--")
plt.show()
