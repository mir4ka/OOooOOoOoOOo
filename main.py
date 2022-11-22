import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush


class Exs(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.vfvf.resize(800, 500)
        self.vfvf.move(0, 0)
        self.vfvf.clicked.connect(self.nf)
        self.do = False


    def nf(self):
        self.vfvf.hide()
        self.do = True

    def paintEvent(self, event):
        if self.do:
            a = random.randint(2, 15)
            for i in range(a):
                qp = QPainter()
                qp.begin(self)
                self.drawc(qp)
                qp.end()

    def drawc(self, qp):
        qp.setBrush(QColor(250, 250, 20))
        a = random.randint(3, 200)
        b = random.randint(50, 300)
        c = random.randint(50, 300)
        qp.drawEllipse(b, c, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exs()
    ex.show()

    sys.exit(app.exec_())

