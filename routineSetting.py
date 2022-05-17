import sys
from PySide6.QtWidgets import *
from methodToTake import MethodToTake
import globals

class RoutineSetting(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting', self)
        set_name_groupbox.move(10, 20)
        set_name_groupbox.resize(290, 160)

        routineName = QLabel("약 명칭", self)
        routineName.move(20, 30)
        routineName.resize(100, 80)

        self.routineName_lineEdit = QLineEdit(self)
        self.routineName_lineEdit.move(90, 55)
        self.routineName_lineEdit.resize(185, 30)

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
    def next(self):
        globals.medicineName = self.routineName_lineEdit.text()
        if globals.medicineName == '':
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        mtt = MethodToTake()
        mtt.exec()


    def back(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineSetting()
    sys.exit(app.exec())
