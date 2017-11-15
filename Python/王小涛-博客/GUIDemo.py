'''
# python GUI 例子

from tkinter import *

def hello():
    print ('hello')

def about():
    label = Label(root, text = '朱海涛\n QQ：1725819676',fg='red',bg='black')
    label.pack(expand=YES,fill=BOTH)
    
root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command( label='打开', command=hello)
filemenu.add_command(label='保存')
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件',menu=filemenu)
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label='关于作者',command=about)
menubar.add_cascade(label='关于',menu=helpmenu)
root.config(menu=menubar)
root.geometry('200x400')
root.mainloop()

'''
from tkinter import *

root = Tk(className = 'bitunion')

# root = tkinter.Tk()     # Tk() 是一个Tkinter 库之中的函数（就是构造函数，构造了一个对象）

label = Label(root)
label['text'] = 'be on your own'
label.pack()

root.geometry('400x200')
root.mainloop()         # mainloop() 主窗口的成员函数，表示让这个root工作起来

