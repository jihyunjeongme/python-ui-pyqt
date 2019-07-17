# Reference
# https://wikidocs.net/book/2165
# https://wikidocs.net/35492

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import time
import datetime
import random
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton("&Like", self)

        self.lbl1 = QLabel("ID", self)
        self.lbl1.move(40, 99)

        self.lbl2 = QLabel("PW", self)
        self.lbl2.move(40, 129)

        self.qle1 = QLineEdit(self)
        self.qle1.move(80, 100)

        self.qle2 = QLineEdit(self)
        self.qle2.setEchoMode(QLineEdit.Password)

        self.qle2.move(80, 130)

        self.setWindowTitle("Instagram Auto Program")
        # x, y, width, height
        self.setGeometry(800, 400, 300, 300)
        self.show()

        # 버튼에 기능을 할당하는 코드
        self.btn1.clicked.connect(self.printTextEdit)
        # self.initUI()

    def printTextEdit(self):
        print(self.qle1.text())
        print(self.qle2.text())

        self.instagramStart()

    def instagramStart(self):
        # ======== 1. Setting Options =======
        self.options = webdriver.ChromeOptions()

        # Chrome을 안 띄우고 수행하고 싶으면 아래 주석을 해제(리눅스 서버에서 작업시 headless 추천, 디버깅시는 headless 주석처리)
        # options.add_argument("headless")

        # Chrome 설정 : 진짜 유저가 작업하는 것처럼 보이도록 설정
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("disable-gpu")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        )
        self.options.add_argument("lang=ko_KR")

        # ======= 2. Setting id, password, hashtag ======

        id = self.qle1.text()
        password = self.qle2.text()

        timeline_like_count = 120

        # hash_tags : 좋아요할 전체 해시태그 리스트
        # important_hash_tags : 중요해서 더 많이 like할 해시태그 리스트

        important_hash_tags = ["수요일", "카페", "퇴근"]
        important_hash_tags_count = 200
        hash_tags = ["수요일", "카페", "퇴근"]
        hash_tags_count = 600

        # ======== 3. InstaJob Class ======
        print("browser loading..")
        global browser
        browser = webdriver.Chrome(
            "/Users/jihyun/Documents/GitHub/instagram-auto-like-with-Python/chromedriver_74",
            chrome_options=self.options,
        )

        browser.execute_script(
            "Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})"
        )
        browser.execute_script(
            "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})"
        )
        browser.execute_script(
            "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = \
            function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) \
            {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};"
        )

        browser.get("https://instagram.com/")

        # 로그인
        login_link = browser.find_element_by_css_selector(
            "p.izU2O"
        ).find_element_by_css_selector("a")
        login_link.click()
        time.sleep(3.5)

        username_input = browser.find_elements_by_css_selector("input._2hvTZ")[0]
        username_input.send_keys(id)
        time.sleep(2 + random.random() * 0.3)
        password_input = browser.find_elements_by_css_selector("input._2hvTZ")[1]
        password_input.send_keys(password)
        time.sleep(1)
        password_input.submit()
        time.sleep(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
