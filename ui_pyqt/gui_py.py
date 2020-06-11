#! /usr/bin/env python
#coding=GB18030

import tkinter

'''
1. tkinter.Tk()生成主窗口(root=tkinter.Tk())
    root.title('标题名')  修改框体的名字，也可在创建时使用className参数来命名；
    root.resizable(0,0)  框体大小可调性，分别表示x,y方向的可变性
    root.geometry('250x150')   指定主框体大小,注意这里是小写x,不是*
    roo.quit()                退出
    root.update_idletasks()
    root.update()              刷新页面
'''
root=tkinter.Tk()            #生成root主窗口
label=tkinter.Label(root,text='自动化测试工具gui')    #生成标签
label.pack()            #将标签添加到主窗口
button1=tkinter.Button(root,text='Button1')   #生成Button1
button1.pack(side=tkinter.LEFT)            #将Button1添加到主窗口
button2=tkinter.Button(root,text='Button2')   #生成Button2
button2.pack(side=tkinter.RIGHT)   #将Button2添加到主窗口
root.geometry('300x300')
root.mainloop()