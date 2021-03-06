import sys

from PySide6.QtWidgets import *
# from PySide6.QtCore import *
# from routineCountTime import RoutineCountTime
from routineSetSleepTime import RoutineSetSleepTime
from globals import Global



class RoutineSettingBasedOnSleep(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting(수면기반)', self)
        set_name_groupbox.move(10,20)
        set_name_groupbox.resize(290,160)

        routineName = QLabel("복용 시기", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineSleepMorning = QCheckBox("기상 후", self)
        self.routineSleepMorning.move(130, 30)
        self.routineSleepMorning.resize(100, 80)
        # routineSleepMorning.setChecked(False)
        # self.routineSleepMorning.stateChanged.connect(self.checkbox_toggled)

        self.routineSleepNight = QCheckBox("취침 전", self)
        self.routineSleepNight.move(230, 30)
        self.routineSleepNight.resize(100, 80)
        # routineSleepNight.setChecked(False)
        # self.routineSleepNight.stateChanged.connect(self.checkbox_toggled)

        backBnt = QPushButton("back", self)
        backBnt.move(60,130)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next", self)
        nextBtn.move(180,130)
        nextBtn.resize(80,35)
        nextBtn.clicked.connect(self.next)


    # def checkbox_toggled(self):
    #     if self.routineSleepMorning.isChecked():
    #         print("Morning")
    #     if self.routineSleepNight.isChecked():
    #         print("Night")

    # 넥스트를 누르면 기상 후 / 취침 전 중 체크된 영역을 확인해서 정보를 넘겨준다.
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    # 경우의 수 3가지에 따라 다른 상태를 저장한 변수를 만들어서 다음 파일에서 확인해서 그에 맞는 상황 연출
    def next(self):
        global setTimeMorningOrNight
        if self.routineSleepMorning.isChecked() == False and self.routineSleepNight.isChecked() == False:
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        elif self.routineSleepMorning.isChecked() == True and self.routineSleepNight.isChecked() == False:
            Global.setTimeMorningOrNight = "morning"
            Global.sleepCount = 1
            rss = RoutineSetSleepTime()
            self.close()
            rss.exec()
        elif self.routineSleepMorning.isChecked() == False and self.routineSleepNight.isChecked() == True:
            Global.setTimeMorningOrNight = "night"
            Global.sleepCount = 1
            rss = RoutineSetSleepTime()
            self.close()
            rss.exec()
        else:
            Global.setTimeMorningOrNight = "both"
            Global.sleepCount = 2
            rss = RoutineSetSleepTime()
            self.close()
            rss.exec()

    def back(self):
        self.close()
        from methodToTake import MethodToTake
        mtt = MethodToTake()
        mtt.exec()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RoutineSettingBasedOnSleep()
   sys.exit(app.exec())