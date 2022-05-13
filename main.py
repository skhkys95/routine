import sys

from PySide6.QtCore import QTimer, QTime, QDateTime
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap

from login import Login
from routineSetting import RoutineSetting


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loginModal = Login()
        loginModal.exec()

        self.initUI()
        self.show()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.alarm_box)
        self.timer.timeout.connect(self.statusBarShow)
        self.timer.timeout.connect(self.movePic)
        self.timer.start()
        self.setDistancePerTime = 102

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(700, 700)

        pic_sad = QLabel(self)
        pic_sad.move(500,25)
        pic_sad.resize(80,80)
        pic_sad.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\sad_pic.png")
        pic_sad.setPixmap(pixmap)

        pic_bottle = QLabel(self)
        pic_bottle.move(100,25)
        pic_bottle.resize(80,80)
        pic_bottle.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\bottle_pic.png")
        pic_bottle.setPixmap(pixmap)

        pic_line = QLabel(self)
        pic_line.move(180,55)
        pic_line.resize(330,25)
        pic_line.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\line_pic.png")
        pic_line.setPixmap(pixmap)

        pic_target = QLabel(self)
        pic_target.move(310,37)
        pic_target.resize(60,60)
        pic_target.setScaledContents(100)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\target_pic.png")
        pic_target.setPixmap(pixmap)

        global pic_peel
        pic_peel = QLabel(self)
        pic_peel.move(250,37)
        pic_peel.resize(65,65)
        pic_peel.setScaledContents(100)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\peel_pic.png")
        pic_peel.setPixmap(pixmap)

        checkList = QGroupBox('Check List', self)
        checkList.move(150, 140)
        checkList.resize(390, 390)

        tableWidget = QTableWidget(self)
        tableWidget.move(160, 160)
        tableWidget.resize(370, 360)
        # row수는 사용자 설정에 따라 달라짐
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)

        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        headerList = ["시간", "이름", "설명", "완료"]
        tableWidget.setHorizontalHeaderLabels(headerList)

        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        tableWidget.setItem(0, 0, QTableWidgetItem("14:26"))
        tableWidget.setItem(0, 1, QTableWidgetItem("소화제"))
        tableWidget.setItem(0, 2, QTableWidgetItem("식후 30분"))
        tableWidget.setItem(0, 3, QTableWidgetItem("체크박스"))

        # tableWidget.setItem(i,0,QTableWidgetItem("계산된 설정 시간")
        # tableWidget.setItem((i,1, QTableWidgetItem"설정된 이름"))

        checkBox = QCheckBox(self)
        tableWidget.setCellWidget(1, 3, checkBox)
        checkBox.stateChanged.connect(self.check_state_checkBox)
        # layout = QVBoxLayout()
        # layout.addWidget(tableWidget)
        # self.setLayout(layout)

        # progress bar 생성
        progressBar = QProgressBar(self)
        progressBar.setGeometry(180, 550, 370, 40)
        progressBar.setMinimum(0)
        # 최대값은 사용자의 설정에 따라 정해짐
        progressBar.setMaximum(5)

        # information 그룹박스
        information = QGroupBox('Information', self)
        information.move(380, 610)
        information.resize(300, 80)

        settingBnt = QPushButton('Setting', self)
        settingBnt.move(390, 640)
        settingBnt.resize(85, 40)
        settingBnt.clicked.connect(self.clicked_routineSetting)

        historyBnt = QPushButton('History', self)
        historyBnt.move(485, 640)
        historyBnt.resize(85, 40)

        statBnt = QPushButton('Stat', self)
        statBnt.move(580, 640)
        statBnt.resize(85, 40)

    def clicked_routineSetting(self):
        routineSet = RoutineSetting()
        routineSet.exec()

    # checkBox의 상태가 변할때에 나오는 함수로, 시간 값을 바꿔주는 역할 + range 밖에서 선택했을때는 makeup option으로 유도하는 역할 + progress bar 게이지 올려주는 역할
    def check_state_checkBox(self, state):
        pass

    def closeEvent(self, QCloseEvent):
        close = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if close == QMessageBox.Yes:
            QCloseEvent.accept()
            sys.exit()
        else:
            QCloseEvent.ignore()

    def statusBarShow(self):
        datetime = QDateTime.currentDateTime()
        setTime = datetime.toString('yy-MM-dd hh.mm.ss')
        self.statusBar().showMessage(setTime)
        self.statusBar().repaint()
        self.show()

    def alarm_box(self):
        alarm_box = QMessageBox()
        alarm_box.setWindowTitle("Alarm!")
        time = QTime.currentTime()
        setTime = time.toString('hh.mm.ss')
        if setTime == '17.00.00':
            alarm_box.setText("약먹을 시간이야!")
        else:
            return

    def movePic(self):
        self.setDistancePerTime += 0.05
        pic_peel.move(self.setDistancePerTime,37)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())