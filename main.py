import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from calc import Ui_Form


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.t = ''
        self.sp = []
        self.btn0.clicked.connect(self.butt)
        self.btn1.clicked.connect(self.butt)
        self.btn2.clicked.connect(self.butt)
        self.btn3.clicked.connect(self.butt)
        self.btn4.clicked.connect(self.butt)
        self.btn5.clicked.connect(self.butt)
        self.btn6.clicked.connect(self.butt)
        self.btn7.clicked.connect(self.butt)
        self.btn8.clicked.connect(self.butt)
        self.btn9.clicked.connect(self.butt)
        self.btn_eq.clicked.connect(self.butt)
        self.btn_plus.clicked.connect(self.butt)
        self.btn_div.clicked.connect(self.butt)
        self.btn_dot.clicked.connect(self.butt)
        self.btn_minus.clicked.connect(self.butt)
        self.btn_mult.clicked.connect(self.butt)
        self.btn_pow.clicked.connect(self.butt)
        self.btn_sqrt.clicked.connect(self.butt)
        self.btn_fact.clicked.connect(self.butt)
        self.btn_clear.clicked.connect(self.butt)

    def butt(self):
        if str(self.sender().text()) == 'С':
            self.t = ''
            self.sp = []
            self.table.display('0')
        elif str(self.sender().text()) == '√':
            self.sqrt()
        elif str(self.sender().text()) == '!':
            self.sp.append(self.t[:-1])
            self.sp.append(self.t[-1])
            self.fact()
        else:
            if str(self.sender().text()) not in '=':
                if self.t == '0':
                    self.t = ''
                self.t += str(self.sender().text())
                self.table.display(self.t)
                if self.t[-1] not in '1234567890.':
                    self.sp.append(self.t[:-1])
                    self.sp.append(self.t[-1])
                    self.t = ''
                    self.table.display('0')
            elif str(self.sender().text()) == '=':
                self.run()

    def run(self):
        d = ''
        for t in self.sp:
            if t == '^':
                t = '**'
            d += t
        d = d + self.t
        if '/0' in d:
            self.table.display('error')
        else:
            self.table.display(eval(d))

    def sqrt(self):
        d = ''
        for t in self.t:
            d += t
        f = int(d)**0.5
        self.table.display(f)

    def fact(self):
        d = ''
        for t in self.sp:
            if t == '^':
                t = '**'
            d += t
        g = eval(d)
        r = 1
        for i in range(1, int(g) + 1):
            r *= i

        self.table.display(r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
