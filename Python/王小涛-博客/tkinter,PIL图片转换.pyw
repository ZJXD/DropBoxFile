import os
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window():
    def __init__(self):
        self.root = root = tkinter.Tk()
        self.menu = tkinter.Menu(root)
        self.submenu = tkinter.Menu(self.menu, tearoff = 0)
        self.submenu.add_command(label='作者：朱海涛')
        root.config(menu = self.submenu)
        self.Image = tkinter.StringVar()
        self.Image.set('.bmp')
        self.mstatus = tkinter.IntVar()
        self.fstatus = tkinter.IntVar()
        self.mstatus.set(0)
        self.fstatus.set(0)
        self.status = tkinter.StringVar()
        self.label = tkinter.Label(root, text='输入百分比')
        self.label.place(x=5,y=5)
        self.entryNew = tkinter.Entry(root)
        self.entryNew.place(x=70,y=5)
        self.checkM = tkinter.Checkbutton(self.root, text='批量转换',command = self.OnCheckM, variable = self.mstatus, onvalue = 1,offvalue = 0)
        self.checkM.place(x=5,y=30)
        self.label = tkinter.Label(root, text='选择文件')
        self.label.place(x=5,y=55)
        self.entryFile = tkinter.Entry(root)
        self.entryFile.place(x=70,y=55)
        self.BrowserFileButton = tkinter.Button(root, text='浏览',command=self.BrowserFile)
        self.BrowserFileButton.place(x=220,y=55)
        self.label = tkinter.Label(root,text='选择目录')
        self.label.place(x=5,y=90)
        
        self.entryDir = tkinter.Entry(root, state=tkinter.DISABLED)  
        self.entryDir.place(x=70, y=90)  
        self.BrowserDirButton = tkinter.Button(root, text='浏览', command=self.BrowserDir, state=tkinter.DISABLED)  
        self.BrowserDirButton.place(x=220, y=90)  
  
        self.checkF = tkinter.Checkbutton(root, text='改变文件格式', onvalue=1, offvalue=0, variable=self.fstatus, command=self.OnCheckF)  
        self.checkF.place(x=5, y=120)  
  
  
        frame = tkinter.Frame(root, )  
        frame.place(x=10, y=150)  
        self.rBmp = tkinter.Radiobutton(frame, variable=self.Image, value='.bmp', text='BMP', state=tkinter.DISABLED)  
        self.rBmp.pack(anchor='w')  
        self.rJpg = tkinter.Radiobutton(frame, variable=self.Image, value='.jpg', text='JPG', state=tkinter.DISABLED)  
        self.rJpg.pack(anchor='w')  
        self.rPng = tkinter.Radiobutton(frame, variable=self.Image, value='.png', text='PNG', state=tkinter.DISABLED)  
        self.rPng.pack(anchor='w')  
        self.rGif = tkinter.Radiobutton(frame, variable=self.Image, value='.gif', text='GIF', state=tkinter.DISABLED)  
        self.rGif.pack(anchor='w')  
        self.ButtonCov = tkinter.Button(root, text='转换格式', command=self.Conv)  
        self.ButtonCov.place(x=120, y=180)  
        self.statusLabel = tkinter.Label(root, textvariable=self.status, fg='red')  
        self.statusLabel.place(x=80, y=220)

    def OnCheckM(self):
        if not self.mstatus.get():
            self.entryDir.config(state = tkinter.DISABLED)
            self.entryFile.config(state = tkinter.NORMAL)
            self.BrowserFileButton.config(state = tkinter.NORMAL)
            self.BrowserDirButton.config(state = tkinter.DISABLED)
        else:
            self.entryDir.config(state = tkinter.NORMAL)
            self.entryFile.config(state = tkinter.DISABLED)
            self.BrowserFileButton.config(state = tkinter.DISABLED)
            self.BrowserDirButton.config(state = tkinter.NORMAL)

    def OnCheckF(self):  
        if not self.fstatus.get():  
            self.rBmp.config(state=tkinter.DISABLED)  
            self.rPng.config(state=tkinter.DISABLED)  
            self.rJpg.config(state=tkinter.DISABLED)  
            self.rGif.config(state=tkinter.DISABLED)  
        else:  
            self.rBmp.config(state=tkinter.NORMAL)  
            self.rPng.config(state=tkinter.NORMAL)  
            self.rJpg.config(state=tkinter.NORMAL)  
            self.rGif.config(state=tkinter.NORMAL)

    def BrowserFile(self):
        file = tkinter.filedialog.askopenfilename(title='Python player',filetypes=[('JPG','*.jpg'),('BMP','*.bmp'),('GIF','*.gif'),('PNG','*.png')])
        if file:
            self.entryFile.delete(0,tkinter.END)
            self.entryFile.insert(tkinter.END,file)

    def BrowserDir(self):
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0,tkinter.END)
            self.entryDir.insert(tkinter.END,directory)

    def make(self,file,format = None):
        im = Image.open(file)
        mode = im.mode
        if mode not in('L','RGB'):
            im = im.convert('RGB')
        width, height = im.size
        s = self.entryNew.get()
        if s == '':
            tkinter.messagebox.showerror('出错啦！','请输入百分比')
            return
        else:
            n = int(s)
        nwidth = int(width*n/100)
        nheight = int(height*n/100)
        thumb = im.resize((nwidth,nheight),Image.ANTIALIAS)
        if format:
            thumb.save(file[:(len(file)-4)] + '_thumb' + format)
        else:
            thumb.save(file[:(len(file))-4] + '_thumb' + file[-4:])

    def Conv(self):
        n =  0
        if self.mstatus.get():
            path = self.entryDir.get()
            if path == '':
                tkinter.messagebox.showerror('出错了！','请选择路径')
                return
            filenames = os.listdir(path)
            if self.fstatus.get():
                f = self.Image.get()
                print (f)
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path + '/' + filename,f)
                        n += 1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path + '/' + filename)
                        n += 1
        else:
            file = self.entryFile.get()
            if file == '':
                tkinter.messagebox.showerror('出错啦','请选择文件')
                return
            if self.fstatus.get():
                f = self.Image.get()
                self.make(file,f)
                n += 1
            else:
                self.make(file)
                n += 1
        self.status.set('成功转换 %d 张图片' % n)



    def mainloop(self):
        self.root.minsize(380,370)
        self.root.maxsize(380,350)
        self.root.title('图片转换')
        self.root.mainloop()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
