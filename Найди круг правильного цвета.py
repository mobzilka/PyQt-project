import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt, QPoint, QRect, QSize


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 700, 700)
        self.setWindowTitle('Find a right color')
        self.objectstatustext = QLabel('', self)
        self.objectstatustext.setFont(QFont("Calibri", 12))
        self.objectstatustext.move(119, 23)
        self.objecttext = QLabel('', self)
        self.objecttext.setFont(QFont("Calibri", 12))
        self.objecttext.move(120, 7)
        self.button = QPushButton('start', self)
        self.button.setFont(QFont("Calibri", 14))
        self.button.setGeometry(10, 10, 100, 30)
        self.button.clicked.connect(lambda: self.button_clicked())
        self.rectR = QRect()
        self.rectG = QRect()
        self.rectB = QRect()
        self.show()

    def button_clicked(self):
        self.objectstatustext.setText('Состояние задания: не выполнено')
        self.objectstatustext.setFont(QFont("Calibri", 12))
        self.objectstatustext.resize(500, 18)
        self.button.setText("restart")
        self.shape()

    def shape(self):
        self.right_color = randint(1, 3)
        if self.right_color == 1:
            self.objecttext.setText('Задание: Найди красный круг')
        elif self.right_color == 2:
            self.objecttext.setText('Задание: Найди зеленый круг')
        else:
            self.objecttext.setText('Задание: Найди синий круг')
        self.objecttext.resize(500, 20)
        self.objecttext.move(120, 6)
        self.rectR = QRect(QPoint(randint(10, 590), randint(50, 590)), QSize(100, 100))
        self.rectG = QRect(QPoint(randint(10, 590), randint(50, 590)), QSize(100, 100))
        self.rectB = QRect(QPoint(randint(10, 590), randint(50, 590)), QSize(100, 100))
        self.update()

    def paintEvent(self, event):
        if not self.rectR.isNull():
            painterR = QPainter(self)
            painterR.setPen(QPen(Qt.red, 5))
            painterR.drawEllipse(self.rectR)
            painterG = QPainter(self)
            painterG.setPen(QPen(Qt.green, 5))
            painterG.drawEllipse(self.rectG)
            painterB = QPainter(self)
            painterB.setPen(QPen(Qt.blue, 5))
            painterB.drawEllipse(self.rectB)

    def mousePressEvent(self, event):
        if self.right_color == 1:
            if (
                    2 * QtGui.QVector2D(event.pos() - self.rectR.center()).length()
                    < self.rectR.width()
            ):
                self.objectstatustext.setText('Состояние задания: выполнено')
                self.objectstatustext.resize(500, 19)
        elif self.right_color == 2:
            if (
                    2 * QtGui.QVector2D(event.pos() - self.rectG.center()).length()
                    < self.rectG.width()
            ):
                self.objectstatustext.setText('Состояние задания: выполнено')
                self.objectstatustext.resize(500, 19)
        else:
            if (
                    2 * QtGui.QVector2D(event.pos() - self.rectB.center()).length()
                    < self.rectB.width()
            ):
                self.objectstatustext.setText('Состояние задания: выполнено')
                self.objectstatustext.resize(500, 19)


App = QApplication(sys.argv)
window = Game()
sys.exit(App.exec())