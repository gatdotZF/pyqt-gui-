#! /usr/bin/env python
#coding=GB18030
'''
1.目前使用库：
    pip install pyqt5
    pip install pyqt5-tools
    pip install fbs 将python源码转换成一个执行的PyQt程序
'''
'''
1.导入相关的QT相关库；
2.创建一个QApplication
    app=QtWidgets.QApplication([])
            每个GUI程序都必须有且只有一个QApplication的实例，如果没有这个实例，QT无法执行；
            创建这个对象时需传递一个list参数，如果GUI不需要什么参数，直接传递[]
3.再创建一个Label（标签）
    label=QtWidgets.QLabel('hello world!')
            传递的参数就是标签显示的内容，然后通过调用show()方法让它在屏幕上显示
4.运行qt，直到有人关闭
'''
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QMessageBox

app=QtWidgets.QApplication([])     #实例化
# label=QtWidgets.QLabel('hello word!')   #创建label
# label.show()                      #显示窗口
# sys.exit(app.exec_())             #执行qt

window=QtWidgets.QWidget()   #Qwidget容器，存放widget

'''
水平布局管理器：QHBoxLayout;
垂直布局管理器：QVBoxLayout;
网管布局管理器：QGridLayout;
窗体布局管理器：QFormLayout以两列的形式排列所添加的控件
'''
#自定义风格
app.setStyle('Windows')
palette=QtGui.QPalette()       
palette.setColor(palette.ButtonText, QtCore.Qt.black)    #设置颜色
app.setPalette(palette)
#面板风格
app.setStyleSheet("QPushButton { margin:30ex; }")     #设置样式表
layout=QtWidgets.QGridLayout()          #垂直布局
layout.addWidget(QPushButton('TOP'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()

#signals/slots
'''
1.QT通过signals（信号）机制来让我们对一些事情做响应，例如：点击一个按钮
2.button.clicked就是这个信号，.connect(……):指定与这个signal关联的slot(槽)
3.Signals在QT中是无处不在的，用户也可以定义自己的signal。
'''
button=QPushButton('Click')
def on_button_clicked():
    alert=QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()
button.clicked.connect(on_button_clicked)
button.show()

app.exec_()

