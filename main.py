import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from random_string import Ui_Form


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        a = ''
        b = ''
        with open('lines.txt', 'r') as f:
            d = 0
            for i in f:
                if d % 2 == 0:
                    a += i
                else:
                    b += i
                d += 1
            a += b
        f.close()
        self.textBrowser.setText(a)
        with open('lines.txt', 'w') as f:
            f.write(a)
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

