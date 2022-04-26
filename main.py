import sys
from PySide6.QtWidgets import *


class Main(QDialog, QWidget):
    def __init__(self,parent):
        super(Main,self).__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("MAIN")
        self.resize(700, 700)

        # 체크리스트의 갯수만큼 크기가 달라져야한다.
        checkList = QGroupBox('Check List', self)
        checkList.move(160,160)
        checkList.resize(370,360)


        listNum1 = QLabel("1. 10:20 비타민 C 1회차",self)
        listNum2 = QLabel("2. 14:25 소화제   취침전",self)
        listNum1.move(190,220)
        listNum1.resize(250,80)
        listNum2.move(182,270)
        listNum2.resize(250,80)

        checkBox = QCheckBox(self)


        # progress bar 생성
        progressBar = QProgressBar(self)
        progressBar.setGeometry(180,550,370,40)
        progressBar.setMinimum(0)
        # 최대값은 사용자의 설정에 따라 정해짐
        progressBar.setMaximum(5)



        # information 그룹박스
        information = QGroupBox('Information', self)
        information.move(380,610)
        information.resize(300,80)

        settingBnt = QPushButton('Setting',self)
        settingBnt.move(390,640)
        settingBnt.resize(85,40)

        historyBnt = QPushButton('History',self)
        historyBnt.move(485,640)
        historyBnt.resize(85,40)

        statBnt = QPushButton('Stat',self)
        statBnt.move(580,640)
        statBnt.resize(85,40)

    def closeEvent(self, QCloseEvent):
        close = QMessageBox.question(self,"종료 확인","종료 하시겠습니까?", QMessageBox.Yes|QMessageBox.No)

        if close == QMessageBox.Yes:
            QCloseEvent.accept()
            sys
        else:
            QCloseEvent.ignore()

        #임시로 만든 로그인페이지로 돌아가는 버튼
        homeBnt = QPushButton("home", self)
        homeBnt.clicked.connect(self.Home)


    def Home(self):
        self.close()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Main()
   sys.exit(app.exec())