import sys
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget, QHBoxLayout, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime
import random

global playerdata
playerdata= {
    "이준호": {"name": "이준호", "price": 0, "image_path1": "LAS\미미1.png", "image_path2": "LAS\미미2.JPG"},
    "김도현": {"name": "김도현", "price": 0, "image_path1": "LAS\엘첼1.png", "image_path2": "LAS\엘첼2.JPG"},
    "이제현": {"name": "이제현", "price": 0, "image_path1": "LAS\억까1.png", "image_path2": "LAS\억까2.JPG"},
    "황창환": {"name": "황창환", "price": 0, "image_path1": "LAS\잭잼1.png", "image_path2": "LAS\잭잼2.JPG"},
    "이유환": {"name": "이유환", "price": 0, "image_path1": "LAS\맵리1.png", "image_path2": "LAS\맵리2.JPG"},
    "지수환": {"name": "지수환", "price": 0, "image_path1": "LAS\솨니1.png", "image_path2": "LAS\솨니2.JPG"},
    "유지호": {"name": "유지호", "price": 0, "image_path1": "LAS\뭅친1.png", "image_path2": "LAS\뭅친2.JPG"},
    "정영근": {"name": "정영근", "price": 0, "image_path1": "LAS\컹드1.png", "image_path2": "LAS\컹드2.JPG"},
    "신주형": {"name": "신주형", "price": 0, "image_path1": "LAS\쥬쥬1.png", "image_path2": "LAS\쥬쥬2.JPG"},
    "박은석": {"name": "박은석", "price": 0, "image_path1": "LAS\선대1.png", "image_path2": "LAS\선대2.JPG"},
    "정주빈": {"name": "정주빈", "price": 0, "image_path1": "LAS\짧주1.png", "image_path2": "LAS\짧주2.JPG"},
    "도인탁": {"name": "도인탁", "price": 0, "image_path1": "LAS\골포1.png", "image_path2": "LAS\골포2.JPG"},
    "박해준": {"name": "박해준", "price": 0, "image_path1": "LAS\핫초1.png", "image_path2": "LAS\핫초2.JPG"},
    "조현준": {"name": "조현준", "price": 0, "image_path1": "LAS\레몬1.png", "image_path2": "LAS\레몬2.JPG"},
    "이한희": {"name": "이한희", "price": 0, "image_path1": "LAS\한신1.png", "image_path2": "LAS\한신2.JPG"},
    "조민서": {"name": "조민서", "price": 0, "image_path1": "LAS\큰소1.png", "image_path2": "LAS\큰소2.JPG"},
    "박성준": {"name": "박성준", "price": 0, "image_path1": "LAS\생세1.png", "image_path2": "LAS\생세2.JPG"},
    "방준형": {"name": "방준형", "price": 0, "image_path1": "LAS\샤크1.png", "image_path2": "LAS\샤크2.JPG"},
    "게스트1": {"name": "게스트1", "price": 0, "image_path1": "LAS\게스트1.png", "image_path2": "LAS\게스트12.JPG"},
    "게스트2": {"name": "게스트2", "price": 0, "image_path1": "LAS\게스트2.png", "image_path2": "LAS\게스트22.JPG"}
}



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # CONFIGURATION
        self.teamblue = ["정영근"]
        self.teamred = ["이유환"]
        self.playernames = ["신주형", "이한희", "박성준", "도인탁", "유지호", "김도현", "박은석", "게스트1"]
        self.timelimit = 15

        self.bidorder = random.sample(self.playernames, len(self.playernames))

        self.auction = False
        self.auctiontime = self.timelimit

        self.leftscore = 1000
        self.rightscore = 1000

        self.highpriceteam = 0

        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.candidateUI())
        self.main_layout.addLayout(self.middleUI())
        self.main_layout.addLayout(self.bidUI())
        self.main_layout.addLayout(self.priceUI())
        self.main_layout.addStretch(1)

        self.setLayout(self.main_layout)

        # Set window properties
        self.setWindowTitle('SASA LOL DRAFTER')
        self.resize(int(1280), 900)  # Set the window size to 1920x1080

        # Position the window at the center of the screen
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        self.setStyleSheet("background-color: black;")
        # Show the main window
        self.show()

    def candidateUI(self):
        player_layout = QHBoxLayout()
        player_layout.addStretch(1)
        txt_label = QLabel("남은 선수", self)
        txt_label.setStyleSheet("color: white;")
        player_layout.addWidget(txt_label)
        #playernames = ['LAS\골포1.png', 'LAS\레몬1.png', 'LAS\맵리1.png', 'LAS\뭅친1.png', 'LAS\미미1.png']
        self.playerwidgets = {}
        for player in self.playernames:
            image_label = QLabel(self)
            pixmap = QPixmap(playerdata[player]["image_path1"])
            percentage = 0.2
            new_width = int(pixmap.width() * percentage)
            new_height = int(pixmap.height() * percentage)
            pixmap = pixmap.scaled(new_width, new_height)
            image_label.setPixmap(pixmap)
            self.playerwidgets[player] = image_label
            player_layout.addWidget(image_label)
        player_layout.addStretch(1)

        # 유찰 선수
        self.pass_layout = QHBoxLayout()
        self.pass_layout.addStretch(1)
        txt_label = QLabel("유찰 선수", self)
        txt_label.setStyleSheet("color: white;")
        self.pass_layout.addWidget(txt_label)
        passnames = []
        for player in passnames:
            image_label = QLabel(self)
            pixmap = QPixmap(playerdata[player]["image_path1"])
            percentage = 0.2
            new_width = int(pixmap.width() * percentage)
            new_height = int(pixmap.height() * percentage)
            pixmap = pixmap.scaled(new_width, new_height)
            image_label.setPixmap(pixmap)
            self.pass_layout.addWidget(image_label)
        self.pass_layout.addStretch(1)

        self.candidate_layout = QVBoxLayout()
        self.candidate_layout.addLayout(player_layout)
        self.candidate_layout.addLayout(self.pass_layout)
        return self.candidate_layout

    def middleUI(self):
        ### 중단 GUI
        # TEAM 1 status
        self.teamleft_layout = QVBoxLayout()

        # TIME NAME
        txt_label = QLabel("TEAM BLUE", self)
        txt_label.setAlignment(QtCore.Qt.AlignRight)
        txt_label.setStyleSheet("color: white;")
        self.teamleft_layout.addWidget(txt_label)

        # LEFT SCORE
        self.leftscore_label = QLabel(f"남은 점수: {self.leftscore}", self)
        self.leftscore_label.setAlignment(QtCore.Qt.AlignRight)
        self.leftscore_label.setStyleSheet("color: white;")
        self.teamleft_layout.addWidget(self.leftscore_label)

        # SELECTED TEAM MATES
        # teamblue = ['LAS\골포1.png', 'LAS\레몬1.png', 'LAS\맵리1.png', 'LAS\게스트1.png', 'LAS\게스트1.png']
        for player in self.teamblue:
            image_label = QLabel(self)
            image_label.setAlignment(QtCore.Qt.AlignRight)
            pixmap = QPixmap(playerdata[player]["image_path1"])
            percentage = 0.2
            new_width = int(pixmap.width() * percentage)
            new_height = int(pixmap.height() * percentage)
            pixmap = pixmap.scaled(new_width, new_height)
            image_label.setPixmap(pixmap)
            self.teamleft_layout.addWidget(image_label)

        self.teamleft_layout.addStretch(1)

        # MAIN PICTURE
        self.playerinfo_image_label = QLabel(self)
        pixmap = QPixmap(playerdata[self.bidorder[0]]["image_path2"])
        percentage = 0.8
        new_width = int(pixmap.width() * percentage)
        new_height = int(pixmap.height() * percentage)
        pixmap = pixmap.scaled(new_width, new_height)
        self.playerinfo_image_label.setPixmap(pixmap)

        # TEAM 2 status
        self.teamright_layout = QVBoxLayout()

        # TIME NAME
        txt_label = QLabel("TEAM RED", self)
        txt_label.setAlignment(QtCore.Qt.AlignLeft)
        txt_label.setStyleSheet("color: white;")
        self.teamright_layout.addWidget(txt_label)

        # LEFT OVER SCORE
        self.rightscore_label = QLabel(f"남은 점수: {self.rightscore}", self)
        self.rightscore_label.setAlignment(QtCore.Qt.AlignLeft)
        self.rightscore_label.setStyleSheet("color: white;")
        self.teamright_layout.addWidget(self.rightscore_label)

        # SELECTED TEAM MATES
        #teamred = ['LAS\뭅친1.png', 'LAS\샤크1.png', 'LAS\게스트1.png', 'LAS\게스트1.png', 'LAS\게스트1.png']
        #teamred = []
        for player in self.teamred:
            image_label = QLabel(self)
            image_label.setAlignment(QtCore.Qt.AlignLeft)
            pixmap = QPixmap(playerdata[player]["image_path1"])
            percentage = 0.2
            new_width = int(pixmap.width() * percentage)
            new_height = int(pixmap.height() * percentage)
            pixmap = pixmap.scaled(new_width, new_height)
            image_label.setPixmap(pixmap)
            self.teamright_layout.addWidget(image_label)

        self.teamright_layout.addStretch(1)

        self.middle_layout = QHBoxLayout()
        # middle_layout.addStretch(1)
        self.middle_layout.addStretch(1)
        self.middle_layout.addLayout(self.teamleft_layout)
        self.middle_layout.addWidget(self.playerinfo_image_label)
        self.middle_layout.addLayout(self.teamright_layout)
        self.middle_layout.addStretch(1)
        return self.middle_layout

    def bidUI(self):
        self.bid_layout = QHBoxLayout()

        left_bid_button = QPushButton('입찰', self)
        left_bid_button.setStyleSheet("background-color: white;")
        left_bid_button.setFixedHeight(50)
        left_bid_button.clicked.connect(self.left_bid_click)
        self.bid_layout.addWidget(left_bid_button)

        left_giveup_button = QPushButton('포기', self)
        left_giveup_button.setStyleSheet("background-color: white;")
        left_giveup_button.setFixedHeight(50)
        self.bid_layout.addWidget(left_giveup_button)
        #bid_layout.addStretch(1)

        self.time_txt_label = QLabel("Timer", self)
        self.time_txt_label.setFixedSize(400, 50)
        self.time_txt_label.setStyleSheet("color: white; font-size: 30px")
        self.time_txt_label.setAlignment(QtCore.Qt.AlignCenter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_txt_label)
        self.timer.start(1000)
        self.update_timer_txt_label()

        self.bid_layout.addWidget(self.time_txt_label)
        #bid_layout.addStretch(1)


        right_giveup_button = QPushButton('포기', self)
        right_giveup_button.setStyleSheet("background-color: white;")
        right_giveup_button.setFixedHeight(50)
        self.bid_layout.addWidget(right_giveup_button)


        right_bid_button = QPushButton('입찰', self)
        right_bid_button.setStyleSheet("background-color: white;")
        right_bid_button.setFixedHeight(50)
        right_bid_button.clicked.connect(self.right_bid_click)
        self.bid_layout.addWidget(right_bid_button)

        return self.bid_layout



    def priceUI(self):
        self.price_layout = QHBoxLayout()

        _20_button = QPushButton('+20', self)
        _20_button.setStyleSheet("background-color: white;")
        _20_button.setFixedHeight(50)
        _20_button.clicked.connect(self._20_click)
        self.price_layout.addWidget(_20_button)

        _40_button = QPushButton('+40', self)
        _40_button.setStyleSheet("background-color: white;")
        _40_button.setFixedHeight(50)
        _40_button.clicked.connect(self._40_click)
        self.price_layout.addWidget(_40_button)

        self.price_input_box = QLineEdit(self)
        self.price_input_box.setText("0")
        validator = QIntValidator()
        self.price_input_box.setValidator(validator)
        self.price_input_box.setStyleSheet("background-color: white; font-size: 30px")
        self.price_input_box.setAlignment(QtCore.Qt.AlignCenter)
        self.price_input_box.setFixedSize(400, 50)
        self.price_input_box.textChanged.connect(self.price_changed)
        self.price_layout.addWidget(self.price_input_box)
        
        _100_button = QPushButton('+100', self)
        _100_button.setStyleSheet("background-color: white;")
        _100_button.setFixedHeight(50)
        _100_button.clicked.connect(self._100_click)
        self.price_layout.addWidget(_100_button)

        _200_button = QPushButton('+200', self)
        _200_button.setStyleSheet("background-color: white;")
        _200_button.setFixedHeight(50)
        _200_button.clicked.connect(self._200_click)
        self.price_layout.addWidget(_200_button)
        return self.price_layout


    def update_timer_txt_label(self):
        if self.auction:
            self.auctiontime -= 1
            self.time_txt_label.setText(str(self.auctiontime))
            if self.auctiontime == 0:
                self.auction = False
                price = int(self.price_input_box.text())
                if self.highpriceteam == "left":
                    self.leftscore -= price
                    self.leftscore_label.setText(str(self.leftscore))

                    image_label = QLabel(self)
                    image_label.setAlignment(QtCore.Qt.AlignRight)
                    pixmap = QPixmap(playerdata[self.bidorder[0]]["image_path1"])
                    percentage = 0.2
                    new_width = int(pixmap.width() * percentage)
                    new_height = int(pixmap.height() * percentage)
                    pixmap = pixmap.scaled(new_width, new_height)
                    image_label.setPixmap(pixmap)
                    self.teamleft_layout.addWidget(image_label)
                elif self.highpriceteam == "right":
                    self.rightscore -= price
                    self.rightscore_label.setText(str(self.rightscore))

                    image_label = QLabel(self)
                    image_label.setAlignment(QtCore.Qt.AlignLeft)
                    pixmap = QPixmap(playerdata[self.bidorder[0]]["image_path1"])
                    percentage = 0.2
                    new_width = int(pixmap.width() * percentage)
                    new_height = int(pixmap.height() * percentage)
                    pixmap = pixmap.scaled(new_width, new_height)
                    image_label.setPixmap(pixmap)
                    self.teamright_layout.addWidget(image_label)
                else:
                    image_label = QLabel(self)
                    image_label.setAlignment(QtCore.Qt.AlignLeft)
                    pixmap = QPixmap(playerdata[self.bidorder[0]]["image_path1"])
                    percentage = 0.2
                    new_width = int(pixmap.width() * percentage)
                    new_height = int(pixmap.height() * percentage)
                    pixmap = pixmap.scaled(new_width, new_height)
                    image_label.setPixmap(pixmap)
                    self.pass_layout.insertWidget(2,image_label)
                    self.bidorder.append(self.bidorder[0])

                self.highpriceteam = 0
                try:
                    self.playerwidgets[self.bidorder[0]].deleteLater()
                except:
                    pass
                self.bidorder.pop(0)
                self.price_input_box.setText("0")

                if len(self.bidorder)==0:
                    self.timer.stop()
                else:
                    pixmap = QPixmap(playerdata[self.bidorder[0]]["image_path2"])
                    percentage = 0.8
                    new_width = int(pixmap.width() * percentage)
                    new_height = int(pixmap.height() * percentage)
                    pixmap = pixmap.scaled(new_width, new_height)
                    self.playerinfo_image_label.setPixmap(pixmap)



        else:
            self.auction = True
            self.auctiontime = self.timelimit
            self.time_txt_label.setText(str(self.auctiontime))

    def _20_click(self):
        self.price_input_box.setText(str(int(self.price_input_box.text())+20))
        self.auction = False

    def _40_click(self):
        self.price_input_box.setText(str(int(self.price_input_box.text())+40))
        self.auction = False

    def _100_click(self):
        self.price_input_box.setText(str(int(self.price_input_box.text())+100))
        self.auction = False

    def _200_click(self):
        self.price_input_box.setText(str(int(self.price_input_box.text())+200))
        self.auction = False

    def price_changed(self, price):
        self.auction = False

    def left_bid_click(self):
        self.highpriceteam = "left"
        self.price_input_box.setStyleSheet("background-color: white; font-size: 30px; color: blue;")

    def right_bid_click(self):
        self.highpriceteam = "right"
        self.price_input_box.setStyleSheet("background-color: white; font-size: 30px; color: red;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
