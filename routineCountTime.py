import sys
from PySide6.QtWidgets import *

class RoutineCountTime(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("My Medicine Routine")
        self.resize(310, 200)

        set_name_groupbox = QGroupBox('Routine Setting(횟수기반)', self)
        set_name_groupbox.move(10,20)
        set_name_groupbox.resize(290,170)

        tableWidget = QTableWidget(self)
        tableWidget.move(20, 35)
        tableWidget.resize(270, 110)
        # row수는 사용자 설정에 따라 달라짐
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(1)

        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        headerList = ["시간"]
        tableWidget.setHorizontalHeaderLabels(headerList)

        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        timeEdit = QTimeEdit(self)
        tableWidget.setCellWidget(0, 0, timeEdit)

        backBnt = QPushButton("back", self)
        backBnt.move(60,150)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next",self)
        nextBtn.move(180,150)
        nextBtn.resize(80,35)
        nextBtn.clicked.connect(self.next)

    # 넥스트를 눌렸을때 바로 넘어가는것이 아니고 빈칸이 있는지 확인하고 있으면 입력 양식이 맞지 않으니 다시 입력하라고 경고하고 돌려보내기
    # 양식에 이상이 없으면 사용자가 입력한 내용을 저장해서 보관
    def next(self):
        global medicineName
        medicineName = self.routineName_lineEdit.text()
        if medicineName == '':
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        print(medicineName)


    def back(self):
        self.close()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RoutineCountTime()
   sys.exit(app.exec())