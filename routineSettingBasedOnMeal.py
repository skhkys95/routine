import sys

from PySide6.QtWidgets import *
from routineSetMeal import RoutineSetMeal
import globals


class RoutineSettingBasedOnMeal(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting(식사기반)', self)
        set_name_groupbox.move(10, 20)
        set_name_groupbox.resize(290, 160)

        routineName = QLabel("복용 시기", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineMealBreakfast = QCheckBox("아침", self)
        self.routineMealBreakfast.move(100, 30)
        self.routineMealBreakfast.resize(100, 80)
        self.routineMealBreakfast.stateChanged.connect(self.checkbox_toggled)

        self.routineMealLunch = QCheckBox("점심", self)
        self.routineMealLunch.move(170, 30)
        self.routineMealLunch.resize(100, 80)
        self.routineMealLunch.stateChanged.connect(self.checkbox_toggled)

        self.routineMealDinner = QCheckBox("저녁", self)
        self.routineMealDinner.move(240, 30)
        self.routineMealDinner.resize(100, 80)
        self.routineMealDinner.stateChanged.connect(self.checkbox_toggled)

        backBnt = QPushButton("back", self)
        backBnt.move(60, 130)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next", self)
        nextBtn.move(180, 130)
        nextBtn.resize(80, 35)
        nextBtn.clicked.connect(self.next)

    def checkbox_toggled(self):
        if self.routineMealBreakfast.isChecked():
            print("Morning")
        if self.routineMealDinner.isChecked():
            print("Night")

    # 넥스트를 누르면 기상 후 / 취침 전 중 체크된 영역을 확인해서 정보를 넘겨준다.
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    # 경우의 수 3가지에 따라 다른 상태를 저장한 변수를 만들어서 다음 파일에서 확인해서 그에 맞는 상황 연출
    def next(self):
        globals.checked = []

        if self.routineMealBreakfast.isChecked():
            globals.checked.append("breakfast")
        if self.routineMealLunch.isChecked():
            globals.checked.append("lunch")
        if self.routineMealDinner.isChecked():
            globals.checked.append("dinner")
        print(globals.checked)
        if not globals.checked:
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        else:
            rsm = RoutineSetMeal()
            rsm.exec()

    def back(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineSettingBasedOnMeal()
    sys.exit(app.exec())
