#-*- coding:utf-8-*-
from PIL import Image
import hashlib
import time
import math
import os
import tkinter as tk
import tkinter.filedialog as FD

global im2
im2 = None

# 向量空间
class VectorCompare:
    # 计算矢量大小
    def magnitude(self, concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的 cos 值
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

# 将图片转为矢量
def buildvector(img):
    d1 = {}
    count = 0 
    for i in img.getdata():
        d1[count] = i
        count += 1
    return d1

# 对图片做基本的处理
def pretreatmentPic(pic_name):
    global im2
    im = Image.open(pic_name)
    # 将突破转换为8位像素模式
    im.convert("P")

    # # 打印颜色直方图
    # # print(im.histogram())
    # his  = im.histogram()
    # values = {}

    # for i in range(256):
    #     values[i] = his[i]

    # # 输出颜色最多的10个颜色，其中220和227对应的红色和灰色是我们需要的
    # for j,k in sorted(values.items(), key = lambda x:x[1], reverse=True)[:10]:
    #     print(j,k)

    # 处理图片，得到黑白二值图（这里的数值要根据你的验证码颜色来进行设置，这里验证码图片中是红色和灰色，所以是220和227）
    im2 = Image.new("P", im.size, 255)

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pix = im.getpixel((x, y))
            # if pix == 220 or pix == 227:
            if pix == 220:
                im2.putpixel((x, y), 0)

    # im2.show()   # 可以输出看下得到的二值图


    # 提取单个字符图片，获取每个图片的起始位置（纵向切割）
    inletter = False
    foundletter = False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix = im2.getpixel((y, x))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y
        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter = False
    # print(letters)
    return letters

# 提取单个图片作为训练集合
def cropPic(pic_name):
    global im2
    letters = pretreatmentPic(pic_name)

    # 根据获得的字符坐标，切割图片并保存
    count = 0
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop(( letter[0], 0, letter[1], im2.size[1]))
        m.update(("%s%s"%(time.time(), count)).encode("utf-8"))
        im3.save("./test_pic/%s.gif"%(m.hexdigest()))
        count += 1

# 对验证码识别
def RecognitionPic(pic_name):
    global im2
    letters = pretreatmentPic(pic_name)

    v = VectorCompare()
    iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # 加载训练集
    imggeset = []
    for letter in iconset:
        for img in os.listdir('./iconset/%s/'%(letter)):
            temp = []
            if img != "Thumbs.db" and img != ".DS_Store":
                temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter, img))))
            imggeset.append({letter:temp})

    count = 0
    # 对验证图片进行切割
    out_str = ""
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

        guess = []

        # 将切割得到的图片和每个训练段进行比较
        for image in imggeset:
            for x,y in image.items():
                if len(y) != 0:
                    guess.append((v.relation(y[0], buildvector(im3)), x))

        guess.sort(reverse=True)
        out_str += guess[0][1]
        count += 1
    print(out_str)

# 用户输入处理
def get_user_action(keyboard):
    c = "N"
    while c not in actions_dict:
        c = keyboard.getch()
    return actions_dict[c]

if __name__ == '__main__':
    print("请选择验证码图片")
    root = tk.Tk()
    root.withdraw()
    fileName = FD.askopenfilename(title = "选择文件")
    action = input("对图片进行识别选择Y，对图片进行训练提取选择N，Y/N：")
    if(action.upper() == 'Y'):
        print("开始对文件%s进行识别..."%os.path.basename(fileName))
        RecognitionPic(fileName)
    elif(action.upper() == 'N'):
        print("开始进行提取图片%s中的字符..."%os.path.basename(fileName))
        cropPic(fileName)
