# coding:utf-8
# 输出26个字母，每个字母占两个位子，每行输出5个

s = [chr(i) for i in range(97,123)]

n = 0
s_p = ''
for a in s:
    n += 1
    if n%5 ==0:
        s_p = s_p + ("%s\n" % a)
    else:
        s_p = s_p + ("%-2s" % a)

print(s_p)
print(s)
