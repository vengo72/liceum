import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from test import Ui_Form
from random import randint
import os


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('lines.txt', 'r') as f:
            lines = f.readlines()
            a = len(lines)
            if os.stat("lines.txt").st_size == 0:
                pass
            else:
                b = randint(0, a - 1)
                f.seek(0)
                for number, line in enumerate(f):
                    if b == number:
                        self.lineEdit.setText(line)
                        break
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())




