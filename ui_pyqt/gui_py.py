#! /usr/bin/env python
#coding=GB18030

import tkinter

'''
1. tkinter.Tk()����������(root=tkinter.Tk())
    root.title('������')  �޸Ŀ�������֣�Ҳ���ڴ���ʱʹ��className������������
    root.resizable(0,0)  �����С�ɵ��ԣ��ֱ��ʾx,y����Ŀɱ���
    root.geometry('250x150')   ָ���������С,ע��������Сдx,����*
    roo.quit()                �˳�
    root.update_idletasks()
    root.update()              ˢ��ҳ��
'''
root=tkinter.Tk()            #����root������
label=tkinter.Label(root,text='�Զ������Թ���gui')    #���ɱ�ǩ
label.pack()            #����ǩ��ӵ�������
button1=tkinter.Button(root,text='Button1')   #����Button1
button1.pack(side=tkinter.LEFT)            #��Button1��ӵ�������
button2=tkinter.Button(root,text='Button2')   #����Button2
button2.pack(side=tkinter.RIGHT)   #��Button2��ӵ�������
root.geometry('300x300')
root.mainloop()