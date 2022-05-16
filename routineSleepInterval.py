import sys
from PySide6.QtWidgets import *


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
        set_name_groupbox.resize(290, 170)

        morningTime = QLabel("기상 시간", self)
        morningTime.move(40, 25)
        morningTime.resize(100, 80)

        nightTime = QLabel("취침 시간", self)
        nightTime.move(40, 65)
        nightTime.resize(100, 80)

        morningTimeEdit = QTimeEdit(self)
        morningTimeEdit.move(140, 50)
        morningTimeEdit.resize(100, 30)

        nightTimeEdit = QTimeEdit(self)
        nightTimeEdit.move(140, 90)
        nightTimeEdit.resize(100, 30)

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
        buttonReply = QMessageBox.information(self, "입력 확인", "이대로 설정하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            pass
        elif buttonReply == QMessageBox.No:
            return

    def back(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineSleepInterval()
    sys.exit(app.exec())