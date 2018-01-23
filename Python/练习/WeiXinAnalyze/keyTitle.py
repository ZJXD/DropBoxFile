# coding:utf-8

from wordcloud import WordCloud
import jieba

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

display_columns = ["title","read_num","like_num","comment_num","reward_num","p_date"]

# 读取数据
df = pd.read_csv("post.csv", encoding="utf-8")

words = []
for i in df.title:
    seg_list = jieba.cut(i, cut_all = False)
    words.append(" ".join(seg_list))

wordcloud = WordCloud(font_path="C:\Windows\Fonts\STSONG.TTF", background_color='white', max_words=80,).generate(" ".join(words))

plt.figure(figsize = (9,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
