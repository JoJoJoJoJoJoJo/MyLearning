#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import os
import shutil
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.nameInput2=Entry(self)
        self.nameInput2.pack()
        self.alertButton=Button(self,text='运行',command=self.cpy)
        self.alertButton.pack()
        self.quitButton=Button(self,text='退出',command=self.quit)
        self.quitButton.pack()

    def cpy(self):
        path1=self.nameInput.get()
        path2=self.nameInput2.get()

        try:
            Filelist=[x for x in os.listdir(path1)]
            for files in Filelist:
                realpath=os.path.join(path1,files)
                shutil.copy (realpath,path2)
                print "复制文件成功！"
        except IOError,e:
            print "文件路径错误或目标文件夹权限不足"
        except WindowsError,e:
            print '文件路径错误'
        finally:
            tkMessageBox.showinfo('Message','End')

app=Application()
app.master.title('复制文件')
app.mainloop()
