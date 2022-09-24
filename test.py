import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from qt import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        a = ''
        d = '1234567890^*-+%/'
        for i in self.lineEdit.text():
            if i in d:
                if i == '^':
                    a += '**'
                else:
                    a += i
        self.widget.clear()
        self.widget.plot([i for i in range(int(self.lineEdit_2.text()), int(self.lineEdit_3.text()) + 1)],
                         [eval(str(i) + a) for i in range(int(self.lineEdit_2.text()),
                                                          int(self.lineEdit_3.text()) + 1)], pen='r')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

