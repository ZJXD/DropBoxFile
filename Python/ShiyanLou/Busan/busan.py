#-*- coding:utf-8 -*-

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg


names = {}           # 姓名字典
relationships = {}   # 关系字典
lineNames = []

# 识别剧本中的人物，根据词性来判断
# 是人名存在 lineNames 中，之后出现的更新他们在 names 中的次数

jieba.load_userdict("dict.txt")
with codecs.open("busan.txt", "r", "utf-8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

# for item in lineNames:
#     print(lineNames)
# for name, times in names.items():
#     print (name, times)

# 对于 lineNames 中的每一行，我们为该行出现的人物两两相连
# 如果两人没有建立关系就新建关系，且权值为1，有的加1
for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

# 输出结果，以便可视化处理
# 输出过程中，可以过滤是冗余的边，这里设置共同出现次数少于3次的是冗余边
# 这里输出节点集合和边集合
with codecs.open("busan_node.csv", "w", "gbk") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("busan_edge.csv", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")
