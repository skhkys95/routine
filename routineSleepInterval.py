import sys
from PySide6.QtWidgets import *
import re
from globals import Global


class RoutineSleepInterval(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting(수면기반)', self)
        set_name_groupbox.move(10, 20)
        set_name_groupbox.resize(290, 160)

        routineName = QLabel("간격", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineInterval = QComboBox(self)
        self.routineInterval.addItem('0분')
        self.routineInterval.addItem('30분')
        self.routineInterval.addItem('1시간')
        self.routineInterval.addItem('2시간')

        self.routineInterval.move(90, 55)
        self.routineInterval.resize(185, 30)

        backBnt = QPushButton("back", self)
        backBnt.move(60, 130)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next", self)
        nextBtn.move(180, 130)
        nextBtn.resize(80, 35)
        nextBtn.clicked.connect(self.next)

    # 넥스트를 눌렸을때 바로 넘어가는것이 아니고 빈칸이 있는지 확인하고 있으면 입력 양식이 맞지 않으니 다시 입력하라고 경고하고 돌려보내기
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    # 그동안 저장된 사용자 입력값들을 계산해서 메인페이지에 양식에 맞게 표현
    # 메세지 박스 띄워서 설정대로 루틴을 등록하겠습니까? 물어보기

    def next(self):
        buttonReply = QMessageBox.information(self, "입력 확인", "설정대로 루틴을 등록하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            # 지금까지의 설정 정리 요약해서 main에 띄워줘야함
            Global.sleepInterval = self.routineInterval.currentText()
            Global.explainSleep1 = '기상'+ Global.sleepInterval + '후'
            Global.explainSleep2 = '취침'+ Global.sleepInterval + '전'
            Global.explainSleepList = [Global.explainSleep1, Global.explainSleep2]
            # 숫자만 나오게 뽑아주는 함수
            Global.sleepIntervalTime = re.sub(r'[^0-9]', '', Global.sleepInterval)
            # 기상, 취침시간 받고 간격을 받아서 기상시간에는 간격을 더하고, 취침시간에는 간격을 빼서 테이블에 표현되는 시간에 나타낸다
            if int(Global.sleepIntervalTime) == 30:
                h , m = map(int, Global.morningTime.split(':'))

                if m > 30:
                    if h == 23:
                        h = 0
                        m -= 30
                    else:
                        h += 1
                        m -= 30
                else:
                    m += 30

                print(Global.morningTime)

                H, M = map(int, Global.nightTime.split(':'))

                if M < 30:
                    if H == 0:
                        H = 23
                        M += 30
                    else:
                        H -= 1
                        M += 30
                else:
                    M -= 30

                print(Global.nightTime)
            elif int(Global.sleepIntervalTime) == 1:
                h, m = map(int, Global.morningTime.split(':'))
                if h == 23:
                    h=0
                else:
                    h += 1

                H, M = map(int, Global.nightTime.split(':'))
                if H == 0:
                    H = 23
                else:
                    H -= 1

            elif int(Global.sleepIntervalTime) == 2:
                h, m = map(int, Global.morningTime.split(':'))
                if h == 22:
                    h = 0
                elif h == 23:
                    h = 1
                else:
                    h += 2

                H, M = map(int, Global.nightTime.split(':'))
                if H == 0:
                    H = 22
                elif H == 1:
                    H = 23
                else:
                    H -= 2

            Global.morningTime = str(h) + ":" + str(m)
            Global.nightTime = str(H) + ":" + str(M)
            Global.sleepTimeList = [Global.morningTime, Global.nightTime]

            Global.mainDlg.identifyMethod()
            self.close()
        elif buttonReply == QMessageBox.No:
            return

    def back(self):
        from routineSetSleepTime import RoutineSetSleepTime
        rss = RoutineSetSleepTime()
        self.close()
        rss.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineSleepInterval()
    sys.exit(app.exec())