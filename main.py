import sys

from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_obj(qp)
            # Завершаем рисование
            qp.end()

    def draw_obj(self, qp):
        # Задаем кисть
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        # Рисуем прямоугольник заданной кистью
        r = randint(1, 100)
        qp.drawEllipse(100, 100, r, r)
        self.flag = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
