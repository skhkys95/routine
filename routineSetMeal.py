import sys
from PySide6.QtWidgets import *

from globals import Global
from routineMealInterval import RoutineMealInterval


class RoutineSetMeal(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMorningOrNight()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 220)

        set_name_groupbox = QGroupBox('Routine Setting(식사기반)', self)
        set_name_groupbox.move(10, 20)
        set_name_groupbox.resize(290, 190)

        breakfastTime = QLabel("아침", self)
        breakfastTime.move(40, 25)
        breakfastTime.resize(100, 80)

        lunchTime = QLabel("점심", self)
        lunchTime.move(40, 65)
        lunchTime.resize(100, 80)

        dinnerTime = QLabel("저녁", self)
        dinnerTime.move(40, 105)
        dinnerTime.resize(100, 80)

        self.breakfastTimeEdit = QTimeEdit(self)
        self.breakfastTimeEdit.setDisplayFormat('hh:mm')
        self.breakfastTimeEdit.move(140, 50)
        self.breakfastTimeEdit.resize(100, 30)

        self.lunchTimeEdit = QTimeEdit(self)
        self.lunchTimeEdit.setDisplayFormat('hh:mm')
        self.lunchTimeEdit.move(140, 90)
        self.lunchTimeEdit.resize(100, 30)

        self.dinnerTimeEdit = QTimeEdit(self)
        self.dinnerTimeEdit.setDisplayFormat('hh:mm')
        self.dinnerTimeEdit.move(140, 130)
        self.dinnerTimeEdit.resize(100, 30)

        backBnt = QPushButton("back", self)
        backBnt.move(60, 170)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next", self)
        nextBtn.move(180, 170)
        nextBtn.resize(80, 35)
        nextBtn.clicked.connect(self.next)

    # 이전 설정에서 받아온 변수에 따라 시간 옵션 받기
    def setMorningOrNight(self):
        if 'breakfast' not in Global.checked:
            self.breakfastTimeEdit.setEnabled(False)
        if 'lunch' not in Global.checked:
            self.lunchTimeEdit.setEnabled(False)
        if 'dinner' not in Global.checked:
            self.dinnerTimeEdit.setEnabled(False)

    # 넥스트를 눌렸을때 바로 넘어가는것이 아니고 빈칸이 있는지 확인하고 있으면 입력 양식이 맞지 않으니 다시 입력하라고 경고하고 돌려보내기
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    # 그동안 저장된 사용자 입력값들을 계산해서 메인페이지에 양식에 맞게 표현
    # 메세지 박스 띄워서 설정대로 루틴을 등록하겠습니까? 물어보기

    def next(self):
        Global.breakfastTime = self.breakfastTimeEdit.text()
        Global.lunchTime = self.lunchTimeEdit.text()
        Global.dinnerTime = self.dinnerTimeEdit.text()
        self.close()
        rsi = RoutineMealInterval()
        rsi.exec()

    def back(self):
        from routineSettingBasedOnMeal import RoutineSettingBasedOnMeal
        rsbom = RoutineSettingBasedOnMeal()
        self.close()
        rsbom.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineSetMeal()
    sys.exit(app.exec())
