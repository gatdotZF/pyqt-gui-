#! /usr/bin/env python
#coding=GB18030
'''
1.Ŀǰʹ�ÿ⣺
    pip install pyqt5
    pip install pyqt5-tools
    pip install fbs ��pythonԴ��ת����һ��ִ�е�PyQt����
'''
'''
1.������ص�QT��ؿ⣻
2.����һ��QApplication
    app=QtWidgets.QApplication([])
            ÿ��GUI���򶼱�������ֻ��һ��QApplication��ʵ�������û�����ʵ����QT�޷�ִ�У�
            �����������ʱ�贫��һ��list���������GUI����Ҫʲô������ֱ�Ӵ���[]
3.�ٴ���һ��Label����ǩ��
    label=QtWidgets.QLabel('hello world!')
            ���ݵĲ������Ǳ�ǩ��ʾ�����ݣ�Ȼ��ͨ������show()������������Ļ����ʾ
4.����qt��ֱ�����˹ر�
'''
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QMessageBox

app=QtWidgets.QApplication([])     #ʵ����
# label=QtWidgets.QLabel('hello word!')   #����label
# label.show()                      #��ʾ����
# sys.exit(app.exec_())             #ִ��qt

window=QtWidgets.QWidget()   #Qwidget���������widget

'''
ˮƽ���ֹ�������QHBoxLayout;
��ֱ���ֹ�������QVBoxLayout;
���ܲ��ֹ�������QGridLayout;
���岼�ֹ�������QFormLayout�����е���ʽ��������ӵĿؼ�
'''
#�Զ�����
app.setStyle('Windows')
palette=QtGui.QPalette()       
palette.setColor(palette.ButtonText, QtCore.Qt.black)    #������ɫ
app.setPalette(palette)
#�����
app.setStyleSheet("QPushButton { margin:30ex; }")     #������ʽ��
layout=QtWidgets.QGridLayout()          #��ֱ����
layout.addWidget(QPushButton('TOP'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()

#signals/slots
'''
1.QTͨ��signals���źţ������������Ƕ�һЩ��������Ӧ�����磺���һ����ť
2.button.clicked��������źţ�.connect(����):ָ�������signal������slot(��)
3.Signals��QT�����޴����ڵģ��û�Ҳ���Զ����Լ���signal��
'''
button=QPushButton('Click')
def on_button_clicked():
    alert=QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()
button.clicked.connect(on_button_clicked)
button.show()

app.exec_()

