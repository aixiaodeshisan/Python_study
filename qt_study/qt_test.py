#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :qt_test.py
@说明    :用于学习测试qt
@时间    :2019/12/22 15:30:52
@作者    :MrShiSan
@版本    :1.0
'''

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication,QLabel
from PyQt5.QtGui import QFont  
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUi()

    def initUi(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 8))
        
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        # self.setToolTip('This is a <b>QWidget</b> widget')
        
        # 创建一个PushButton并为他设置一个tooltip(悬停提示)
        btn = QPushButton('测试按钮', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        
        # 移动按钮在窗口的位置
        btn.move(400,400)    

        # 创建取消按钮，并且点击取消
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(500,400) 
        qbtn.setToolTip('这是退出按钮')
        
        # 设置窗口默认位置(300, 300)+窗口尺寸(640, 480)
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('UDP建议聊天器')   

        # 显示窗口 
        self.show()
        pass
    
    # 绝对定位
    # 调整窗口，控件的大小和位置不会改变
    # 各种平台上应用程序看起来会不一样
    # 改变字体，我们的应用程序的布局就会改变
    # 决定改变我们的布局，我们必须完全重做我们的布局
    def absoultUi(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)        
        
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Absolute绝对布局')    
        self.show()
        pass

def main():
    app = QApplication(sys.argv)

    ui = Example()
    ui.absoultUi();

    sys.exit(app.exec_())
    pass

def main2 ():
    # 创建应用程序
    app = QApplication(sys.argv)

    ex = Example()
    ex.initUi()

    sys.exit(app.exec_())
    pass

def main1():
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()
    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(640, 480)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('UDP聊天器')
    # 显示在屏幕上
    w.show()
    
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
    pass

if __name__ == "__main__":
    main()
    pass