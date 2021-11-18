import random

from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

from PyQt5.QtGui import QPainter, QColor


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(800, 600)
        self.a = 0
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.go)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        if self.a == 1:
            self.qp.setBrush(QColor(255, 255, 0))
            for i in self.dim:
                self.qp.drawEllipse(i[1], i[2], i[0], i[0])
        self.update()  #1

    def go(self):
        self.a = 1
        self.dim = [[random.randint(10, 200)] for i in range(random.randint(3, 13))]
        for i in range(len(self.dim)):
            x = random.randint(30, 800 - 2 * self.dim[i][0])
            y = random.randint(30, 600 - 2 * self.dim[i][0])
            self.dim[i].append(x)
            self.dim[i].append(y)


app = QtWidgets.QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())