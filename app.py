# Reference
# https://wikidocs.net/book/2165
# https://wikidocs.net/35492

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import time
import datetime
import random
from selenium import webdriver

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton("&Like", self)

        self.lbl1 = QLabel("ID", self)
        self.lbl1.move(40, 99)

        self.lbl2 = QLabel("PW", self)
        self.lbl2.move(40, 129)

        self.qle1 = QLineEdit(self)
        self.qle1.move(60, 100)

        self.qle2 = QLineEdit(self)
        self.qle2.setEchoMode(QLineEdit.Password)

        self.qle2.move(60, 130)

        self.setWindowTitle("Instagram Auto Program")
        # x, y, width, height
        self.setGeometry(300, 300, 300, 300)
        self.show()

        # 버튼에 기능을 할당하는 코드
        self.btn1.clicked.connect(self.printTextEdit)
        # self.initUI()

    def printTextEdit(self):
        print(self.qle1.text())
        print(self.qle2.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
