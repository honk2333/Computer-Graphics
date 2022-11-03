import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,QPushButton)
from PyQt5.QtGui import QPainter, QColor, QPen
import matplotlib.pyplot as plt
from x_scaner import show
import sys
import numpy as np
import tt

def DDALine(x0, y0, x1, y1):
    x0 = 1

class MyWindow(QWidget):
    distance=0
    polygon=[]
    s=[]
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image=np.ones([150,150])
        #self.setMouseTracking(True)

    def initUI(self):
        self.bt1 = QPushButton("这是什么",self)
        self.bt1.clicked.connect(self.Action)
        self.bt1.setGeometry(0,40,200,20)
        self.setGeometry(200,200,1000,500)
        self.setWindowTitle('简单鼠标跟踪')
        self.label = QLabel(self)
        self.label.resize(500,40)
        self.pos=None        
        
        #self.show()
        
    def Action(self):
        s=[[x.x,x.y] for x in self.polygon]

        self.image = np.ones([1000,900])

        show(self.image,s)

    def mousePressEvent(self,event):
        distance=round(((event.y()-250)**2+(event.x()-500)**2)**0.5)
        self.label.setText('坐标：(x: %d, y: %d)'%(event.x(),event.y()))
        self.polygon.append([event.x(),event.y()])
        self.polygon=tt.solve(len(self.polygon),self.polygon)
        self.update()
 
    def paintEvent(self,event):
        qp=QPainter(self)
        qp.setPen(QPen(Qt.red,10))
        pre=None
        if len(self.polygon)>0:
            pre=self.polygon[-1]
        for i in self.polygon:
            qp.drawPoint(i.x,i.y)
            qp.drawLine(pre.x,pre.y,i.x,i.y)
            pre=i

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ec=MyWindow()
    sys.exit(app.exec_())