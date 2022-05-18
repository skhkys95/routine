import sys
from PySide6.QtWidgets import *
import globals


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

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 35)
        self.tableWidget.resize(270, 110)
        # row수는 사용자 설정에 따라 달라짐
        self.tableWidget.setRowCount(int(globals.routineCount))
        self.tableWidget.setColumnCount(1)

        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        headerList = ["시간"]
        self.tableWidget.setHorizontalHeaderLabels(headerList)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # 시간을 적어야하는 횟수를 앞에서 받아와서 for 문으로 옵션 for문으로 구현해서 각 셀에 타임에디트 들어가도록!
        # arr에 넣어서 설정할때 첫번째 값보다 두번째 시간이 빠를때 설정 실패 하도록
        # timeEdit = QTimeEdit(self)
        # tableWidget.setCellWidget(0, 0, timeEdit)
        # self.timeList = []
        for i in range(int(globals.routineCount)):
            self.timeEdit = QTimeEdit(self)
            self.timeEdit.setDisplayFormat('hh:mm')
            self.tableWidget.setCellWidget(i, 0, self.timeEdit)
            # self.timeList.append(self.timeEdit.text())


        backBnt = QPushButton("back", self)
        backBnt.move(60,150)
        backBnt.resize(80, 35)
        backBnt.clicked.connect(self.back)

        nextBtn = QPushButton("Next",self)
        nextBtn.move(180,150)
        nextBtn.resize(80,35)
        nextBtn.clicked.connect(self.next)

    # 넥스트를 눌렸을때 바로 넘어가는것이 아니고 시간 순서대로 설정이 되었는지 확인하고 넘어가야함
    # sort한 리스트와 그냥 리스트를 비교해서 같으면 통과 다르면 설정 오류가 있다고 알려주는 알고리즘  @@@@@@@@@질문...처음 타임에디트를 만들면서 리스트에 넣어놓고 ui에서 그것을 수정하면 그것을 다시 next함수에서 수정된 시간을 받아 넣고싶은데 도저히 안됨..
    # 그동안 저장된 사용자 입력값들을 계산해서 메인페이지에 양식에 맞게 표현
    # 메세지 박스 띄워서 설정대로 루틴을 등록하겠습니까? 물어보기

    def next(self):
        self.timeEdit.toString(self.timeEdit)
        # self.inputList = []
        # for i in range(int(globalVar.routineCount)):
        #     print(self.tableWidget.item(i, 0))
        print(self.timeEdit)
            # self.timeEdit.setText()
            # self.timeList.append(i.setText())

        # print(self.timeList)
        # if self.arr[2].time()>self.arr[3].time():
        #     QMessageBox.warning(self, "입력 오류", "시간 순서대로 입력해야 합니다.\n입력 하신 내용을 다시 확인 해주세요.")
        if self.timeList != sorted(self.timeList):
            QMessageBox.warning(self, "입력 오류", "시간 순서대로 입력해야 합니다.\n입력 하신 내용을 다시 확인 해주세요.")

    def back(self):
        self.close()
        from routineSettingBasedOnCount import RoutineSettingBasedOnCount
        rsboc = RoutineSettingBasedOnCount()
        rsboc.exec()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RoutineCountTime()
   sys.exit(app.exec())