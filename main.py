import sys
import os.path

from PySide6.QtCore import QTimer, QTime, QDateTime
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from globals import Global
from login import Login
from routineSetting import RoutineSetting


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        Global.mainDlg = self
        self.rowNum = 0

        loginModal = Login()
        loginModal.exec()
        # 사실은 여기서 로그인을 성공하고 난 뒤 사용자가 setting이 있는지 없는지 판단해서 없으면 바로 setting으로 넘겨야됨
        self.initUI()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.alarm_box)
        self.timer.timeout.connect(self.statusBarShow)
        self.timer.timeout.connect(self.movePic)
        self.timer.start()
        self.setDistancePerTime = 102

    # settingZip.txt 파일이 존재하는지 안하는지 확인하고 있으면 패스, 없으면 바로 routineSetting.py로 연결
    def existRoutine(self):
        # ID가 이미 존재하는 아이디인지 확인하고 안내메세지
        file = 'C:\\Users\\3DONS\\PycharmProjects\\routine\\settingZip.txt'
        if os.path.isfile(file):
            with open('settingZip.txt', 'r') as f:
                return
                # accountDict = {}
                # for i in f:
                #     key_value = i.strip().split(',')
                #     accountDict[key_value[0]] = key_value[1]
                # if id in accountDict:
                #     QMessageBox.warning(self, "중복 아이디", "이미 존재하는 아이디입니다.\n아이디를 다시 설정 해주세요.")
                #     self.id_lineEdit.setText('')
                #     self.pw_lineEdit.setText('')
                #     return
        # 아니면 고대로 account.txt에 입력해주고 account 생성
        else:
            routineSet = RoutineSetting()
            routineSet.exec()


    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(700, 700)

        pic_sad = QLabel(self)
        pic_sad.move(500, 25)
        pic_sad.resize(80, 80)
        pic_sad.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\sad_pic.png")
        pic_sad.setPixmap(pixmap)

        pic_bottle = QLabel(self)
        pic_bottle.move(100, 25)
        pic_bottle.resize(80, 80)
        pic_bottle.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\bottle_pic.png")
        pic_bottle.setPixmap(pixmap)

        pic_line = QLabel(self)
        pic_line.move(180, 55)
        pic_line.resize(330, 25)
        pic_line.setScaledContents(200)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\line_pic.png")
        pic_line.setPixmap(pixmap)

        pic_target = QLabel(self)
        pic_target.move(310, 37)
        pic_target.resize(60, 60)
        pic_target.setScaledContents(100)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\target_pic.png")
        pic_target.setPixmap(pixmap)

        global pic_peel
        pic_peel = QLabel(self)
        pic_peel.move(250, 37)
        pic_peel.resize(65, 65)
        pic_peel.setScaledContents(100)
        pixmap = QPixmap("C:\\Users\\3DONS\\PycharmProjects\\routine\\peel_pic.png")
        pic_peel.setPixmap(pixmap)

        checkList = QGroupBox('Check List', self)
        checkList.move(150, 140)
        checkList.resize(390, 390)



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

        settingBnt = QPushButton('History', self)
        settingBnt.move(485, 640)
        settingBnt.resize(85, 40)

        statBnt = QPushButton('Stat', self)
        statBnt.move(580, 640)
        statBnt.resize(85, 40)
        self.existRoutine()

    # rowNum = 설정 방식에 따른 setRowCount 값을 넣어두는 곳
    def identifyMethod(self):
        if Global.routineMethodName == '횟수 기반':
            self.rowNum = Global.routineCount
            print("id1")
        elif Global.routineMethodName == '수면 기반':
            self.rowNum = Global.sleepCount
        elif Global.routineMethodName == '식사 기반':
            self.rowNum = len(Global.checked)
        else:
            return

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(160, 160)
        self.tableWidget.resize(370, 360)
        # row수는 사용자 설정에 따라 달라짐
        # self.identifyMethod()

        self.tableWidget.setRowCount(int(self.rowNum))
        self.tableWidget.setColumnCount(4)

        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        headerList = ["시간", "이름", "설명", "완료"]
        self.tableWidget.setHorizontalHeaderLabels(headerList)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # tableWidget.setItem(i,0,QTableWidgetItem("계산된 설정 시간")
        # tableWidget.setItem((i,1, QTableWidgetItem"설정된 이름"))
        self.checkBoxList = []

        for i in range(int(self.rowNum)):
            self.checkBox = QCheckBox(self)
            self.tableWidget.setCellWidget(i, 3, self.checkBox)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(Global.medicineName))
            self.checkBox.stateChanged.connect(self.check_state_checkBox)
            self.checkBoxList.append(self.checkBox)

        self.identifyMethod2()

    def identifyMethod2(self):
        if Global.routineMethodName == '횟수 기반':
            for i in range(int(self.rowNum)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(Global.countTimeList[i]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(i))
            print("id2")
        elif Global.routineMethodName == '수면 기반':
            pass
        elif Global.routineMethodName == '식사 기반':
            pass
        else:
            return


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
        pic_peel.move(self.setDistancePerTime, 37)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
