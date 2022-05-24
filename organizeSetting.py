from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QMainWindow
import globals

class OrganizeSetting(QMainWindow):
    def __init__(self):
        super().__init__()
        self.identifyMethod()
        self.initUI()

    # rowNum = 설정 방식에 따른 setRowCount 값을 넣어두는 곳
    def identifyMethod(self):
        if globals.routineMethodName == '횟수 기반':
            self.rowNum = globals.routineCount
        elif globals.routineMethodName == '수면 기반':
            self.rowNum = globals.sleepCount
        elif globals.routineMethodName == '식사 기반':
            self.rowNum = len(globals.checked)

    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(160, 160)
        self.tableWidget.resize(370, 360)
        # row수는 사용자 설정에 따라 달라짐

        self.tableWidget.setRowCount(self.rowNum)
        self.tableWidget.setColumnCount(4)

        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        headerList = ["시간", "이름", "설명", "완료"]
        self.tableWidget.setHorizontalHeaderLabels(headerList)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.tableWidget.setItem(0, 0, QTableWidgetItem("14:26"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("소화제"))
        # self.tableWidget.setItem(0, 2, QTableWidgetItem("식후 30분"))
        # self.tableWidget.setItem(0, 3, QTableWidgetItem("체크박스"))

        # self.tableWidget.setItem(i,0,QTableWidgetItem("계산된 설정 시간")
        # 약 명칭 넣기
        self.checkBoxList = []
        for i in self.rowNum:
            self.checkBox = QCheckBox(self)
            self.tableWidget.setCellWidget(i, 3, self.checkBox)
            self.tableWidget.setItem((i, 1, QTableWidgetItem(globals.medicineName)))
            self.checkBox.stateChanged.connect(self.check_state_checkBox)
            self.checkBoxList.append(self.checkBox)


    # next_time = current_time + dt.timedelta(seconds=30) # 30초 더하기 minutes=10 hours=1
    # 입력받은 시간값과 간격에 따라 계산하고 table에 입력
    # 알고리즘은 맞지만 시간 연산하는 방법에 대해 고민 필요
    def calTime(self):
        if '전' in globals.mealInterval:
            globals.breakfastTime -= globals.mealIntervalTime
            globals.lunchTime -= globals.mealIntervalTime
            globals.dinnerTime -= globals.mealIntervalTime

        elif '후' in globals.mealInterval:
            globals.breakfastTime += globals.mealIntervalTime
            globals.lunchTime += globals.mealIntervalTime
            globals.dinnerTime += globals.mealIntervalTime

        globals.morningTime += globals.sleepIntervalTime
        globals.nightTime -= globals.sleepIntervalTime


    def identifyMethod(self):
        if globals.routineMethodName == '횟수 기반':
            for i in self.rowNum:
                self.tableWidget.setItem((i, 0, QTableWidgetItem(globals.countTimeList[i])))
                self.tableWidget.setItem((i, 2, QTableWidgetItem(i + 1 + "회차")))

        elif globals.routineMethodName == '수면 기반':
            pass

        elif globals.routineMethodName == '식사 기반':
            pass

