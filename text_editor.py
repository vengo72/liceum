import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from text_editor_1 import Ui_Form


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.creat)
        self.pushButton_2.clicked.connect(self.read)
        self.pushButton_3.clicked.connect(self.save)

    def save(self):
        try:
            with open(self.lineEdit.text(), mode='w') as f:
                f.write(self.plainTextEdit.toPlainText())
            f.close()
        except Exception:
            pass

    def creat(self):
        self.plainTextEdit.clear()
        try:
            with open(self.lineEdit.text(), mode='w') as f:
                f.write(self.plainTextEdit.toPlainText())
            f.close()
        except Exception:
            pass

    def read(self):
        try:
            with open(self.lineEdit.text(), mode='r') as f:
                d = ''
                for i in f:
                    d += i
                self.plainTextEdit.setPlainText(d)
            f.close()
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

