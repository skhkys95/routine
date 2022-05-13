import sys
from PySide6.QtWidgets import *

from routineSettingBasedOnCount import RoutineSettingBasedOnCount

class MethodToTake(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting', self)
        set_name_groupbox.move(10,20)
        set_name_groupbox.resize(290,160)

        routineName = QLabel("복용 방식", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineMethod = QComboBox(self)
        self.routineMethod.addItem('횟수 기반')
        self.routineMethod.addItem('수면 기반')
        self.routineMethod.addItem('식사 기반')

        self.routineMethod.move(90, 55)
        self.routineMethod.resize(185, 30)

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
        global routineMethodName
        routineMethodName = self.routineMethod.currentText()
        if routineMethodName == '횟수 기반':
            rsboc = RoutineSettingBasedOnCount()
            rsboc.exec()
        elif routineMethodName == '수면 기반':
            pass
            print(routineMethodName)


    def back(self):
        self.close()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MethodToTake()
   sys.exit(app.exec())