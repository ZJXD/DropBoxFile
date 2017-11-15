# 正则表达式（regular expression）主要功能是从字符串(string)中通过特定的模式(pattern)，搜索到想要的内容

# 语法------------------------------------------------------------------------------------------------

# 在之前，我们可与通过一些函数实现简单的搜索功能。比如说从字符串"I love you"中搜索是否有"you"这个字符串
# 但是有些时候我们只是模糊的知道我们想要找什么，而不能具体的说出我要找"you"。
# 比如我要从给定的字符串中找数字，那么这些数字可以是从0到9的任何一个。
# 这些模糊的目标可以作为信息写入正则表达式，传递给Python，从而让Python知道我们要想找什么

# 在Python中使用正则表达式需要一个标准库 re
'''
import re
m = re.search('[0-9]','dagnbl4c9r3')

print(m.group(0))
'''

# re.search 返回的是匹配到的第一个。没有的话返回None

# 正则表达式的函数--------------------------------------------------------------------------
'''
m = re.search(pattern,string)   # 搜索整个字符串，直到发现符合的子字符串
m = re.match(pattern,string)    # 从头开始检查字符串的是否符合，必须从第一个字符开始就相符

str = re.sub(pattern,replacement,string)
# 在string 中利用正则变换 pattern 进行搜索，对于搜索到的字符串，用 replacement 替换，返回替换后的字符串

re.split()    # 根据正则表达式分隔字符串，分割后的字符串放在一个 list 中返回
re.findall()  # 根据正则表达式搜索字符串，将所有符合的子字符串放在一个 list 中返回
'''

# 正则表达式语法--------------------------------------------------------------------------
'''
# 单个字符
.        任意的一个字符
a|b      字符a或字符b
[afg]    a或者f或者g的一个字符
[0-4]    0-4范围内的一个字符
[a-f]    a-f范围内的一个字符
[^m]     不是m的一个字符
\s       一个空格
\S       一个非空格
\d       [0-9]
\D       [^0-9]
\w       [0-9a-zA-Z]
\W       [^0-9a-zA-Z]

# 重复 紧跟在单个字符之后，表示多个这样类似的字符
*        重复 >= 0 次
+        重复 >= 1 次
?        重复 0 或 1 次
{m}      重复 m 次
[m,n]    重复 m 到 n 次

# 位置
^        字符串的起始位置
$        字符串的结尾位置

# 返回控制
# 我们有可能对搜索的结果进行进一步精简，如这个： output_(\d{4})
# 这样被()圈起来的正则表达式的一部分，称为群(group)
# 可以用 m.group(number)的方法来查询群。group(0)是整个正则表达式的搜索结果，group(1)是第一个群

import re
#m = re.search("output_(\d{4})","output_1986.txt")
m = re.search("output_(?P<year>\d{4})","output_1986.txt")    # (?P<name>...)  group命名
print(m.group("year"))
'''

#l 练习----------------------------------------------------------------------
# 有一个文件，文件名 output_2017.10.20.txt，使用Python：读取文件名中的日期信息，
# 找出这一天周几，将文件改为 output_YYYY-MM--DD-W.txt
import re
import os
from datetime import datetime,date

fileName = "output_2017.10.21.txt"
m = re.search("output_(\d{4}.\d{2}.\d{2}).txt",fileName)

date = m.group(1)
date1 = date.replace('.','-')
week = datetime.strptime(date1,"%Y-%m-%d").weekday()
fileName1 = fileName.replace(date,date1 + '-' + str(week + 1))
os.rename(fileName,fileName1)
print(fileName1)
