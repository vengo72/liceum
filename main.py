import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt1 import Ui_Form
import os
d = '1234567890'


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if os.path.exists(self.lineEdit.text()):
            try:
                f = open(self.lineEdit.text(), mode="r").read().split()
                f = [int(item) for item in f]
                f1 = open("output.txt", mode="w")
                f1.write('Максимальное: ' + str(max(f)) + '\n')
                f1.write('Минимальное: ' + str(min(f)) + '\n')
                f1.write('Среднее: ' + str(sum(f) / len(f)) + '\n')
                self.spinBox.setValue(max(f))
                self.spinBox_2.setValue(min(f))
                self.doubleSpinBox.setValue(sum(f) / len(f))
            except Exception:
                self.label_5.setText(f'В файле {self.lineEdit.text()} содержатся некорректные данные')

        else:
            self.label_5.setText(f'Файл {self.lineEdit.text()} не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())




