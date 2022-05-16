import sys

from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import *

from globals import globalVar
from routineCountTime import RoutineCountTime


class RoutineSettingBasedOnCount(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting(횟수기반)', self)
        set_name_groupbox.move(10,20)
        set_name_groupbox.resize(290,160)

        routineName = QLabel("하루에", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineName_lineEdit = QLineEdit(self)
        self.routineName_lineEdit.setValidator(QIntValidator(1, 100, self))
        self.routineName_lineEdit.move(90, 55)
        self.routineName_lineEdit.resize(30, 30)

        routineCount = QLabel("회", self)
        routineCount.move(130, 30)
        routineCount.resize(100, 80)

        backBnt = QPushButton("back", self)
        backBnt.move(60,130)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next",self)
        nextBtn.move(180,130)
        nextBtn.resize(80,35)
        nextBtn.clicked.connect(self.next)

    # 넥스트를 눌렸을때 바로 넘어가는것이 아니고 빈칸이 있는지 확인하고 있으면 입력 양식이 맞지 않으니 다시 입력하라고 경고하고 돌려보내기
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    def next(self):
        globalVar.routineCount = self.routineName_lineEdit.text()
        if globalVar.routineCount == '':
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        elif globalVar.routineCount == '0':
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        else:
            #routineCount를 받아서 다음 화면에 넘겨줄때 알려줘야한다. 3회이면 시간을 3번 쓸수 있도록 유도
            rct = RoutineCountTime()
            rct.exec()
        print(globalVar.routineCount)

    def back(self):
        self.close()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RoutineSettingBasedOnCount()
   sys.exit(app.exec())