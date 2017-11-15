# os.path 包---------------------

'''
import os.path

path = 'D:\Dropbox\Python\Vim 博客-Python学习\补充-01-序列的方法.py'

print(os.path.basename(path))        # 查询路径包含的文件
print(os.path.dirname(path))         # 查询路径包含的目录


info = os.path.split(path)           # 将路径分隔成文件名和目录两部分，同一个列表返回
path2 = os.path.join('D:','Dropbox','Dropbox 使用入门.pdf') # 构成路径
print(path2)
p_list = [path,path2]

print(os.path.commonprefix(p_list))  # 查询多个路径的共同部分

print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件
'''

# glob 包---------------------------------
# 最常用的包只有一个 glob.glob()，与 Linux中的ls相似

import glob

print(glob.glob('D:\Dropbox\Python\Vim 博客-Python学习\标准库\*'))
# 找出文件夹下的所有文件
