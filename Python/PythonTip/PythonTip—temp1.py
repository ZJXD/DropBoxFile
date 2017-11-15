
# 给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）-------------------------------
'''
a=a[0:len(a):2]
print (a)


# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。

a = []
def fanx():
    for i in range(1,101):

        #print ("计算",i)

        isSS = True
        for n in range(2,i):

            #print ("用",n,"除",i)

            if((i % n) == 0):
                isSS = False

        if(isSS == True):
            a.append(i)

fanx()

print (" ".join(str(s) for s in a))


# 给你一字典a ---------------------------------------------------------------
# 如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

# 例如：a={1:1,2:2,3:3}, 则输出：1,2,3
a = {3:3,1:1,2:2}
a = sorted(a.items(),key = lambda asd:asd[0], reverse=False)

print (",".join(str(s[0]) for s in a))


#已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开----------------------
a = 3
b = 8
s = a * b
l = (a + b)*2
n = [s,l]
print (" ".join(str(m) for m in n))


#给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）---------------
L=[0,1,2,3,4]

z = 0
def zws():
    a = 0
    for l in L:
        a = a + l
        print (a)

    n = len(L)
    z = a/n
    

zws()
print (z)


# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。------------
L = [0,1,2,3,4]
S = sum(L)
leng = len(L)

zws = 0
if(S%leng==0):
    zws = S//leng
else:
    zws = round(S/leng,1)

print (zws)


# 给你两个正整数a和b， 输出它们的最大公约数。----------------------------------
# 这个是用-辗转相除法求的最大公约数，也叫欧几里得算法

def GCD(a,b):
    if(a < b):
        d = a
        a = b
        b = d
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    print (b)

GCD(260,104)
'''


# 给你两个正整数a和b， 输出它们的最小公倍数。----------------------------------
# 由于两个数的乘积等于这两个数的最大公约数与最小公倍数的积。
# 即（a，b）×[a，b]=a×b。所以，求两个数的最小公倍数，
# 就可以先求出它们的最大公约数，然后用上述公式求出它们的最小公倍数

def GCD(a,b):
    if(a < b):
        d = a
        a = b
        b = d
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

def LCM(a,b):
    gcd = GCD(a,b)
    lcm = a*b//gcd
    print (lcm)

LCM(45,30)
