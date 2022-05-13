import sys
import os.path
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class CreateAccount(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Create an Account')
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(310, 200)

        login_groupbox = QGroupBox('Account Setting', self)
        login_groupbox.move(10,20)
        login_groupbox.resize(290,160)

        user_id = QLabel("Username", self)
        user_pw = QLabel("Password", self)
        user_id.move(20, 30)
        user_id.resize(100, 80)
        user_pw.move(20, 60)
        user_pw.resize(100, 80)

        self.id_lineEdit = QLineEdit(self)
        self.pw_lineEdit = QLineEdit(self)
        self.id_lineEdit.move(90, 55)
        self.id_lineEdit.resize(185, 30)
        self.pw_lineEdit.move(90, 90)
        self.pw_lineEdit.resize(185, 30)

        cancelBtn = QPushButton("Cancel", self)
        cancelBtn.move(60,130)
        cancelBtn.resize(80, 35)
        cancelBtn.clicked.connect(self.close)

        createBtn = QPushButton("Create",self)
        createBtn.move(180,130)
        createBtn.resize(80,35)
        createBtn.clicked.connect(self.confirm_create)

        # create버튼을 누르면 아이디 패스워드를 txt파일에 적어놓고 가입 안내 메세지 박스 띄우기
    def confirm_create(self):
        id = self.id_lineEdit.text()
        pw = self.pw_lineEdit.text()
        # ID 나 PW가 빈칸으로 입력되면 생성 시켜주면 안됨
        if id == '' or pw == '':
            QMessageBox.warning(self, "입력 오류", "양식에 맞지 않습니다.\n입력 하신 내용을 다시 확인 해주세요.")
            return
        # ID가 이미 존재하는 아이디인지 확인하고 안내메세지
        file = 'C:\\Users\\3DONS\\PycharmProjects\\routine\\account.txt'
        if os.path.isfile(file):
            with open('account.txt', 'r') as f:
                accountDict = {}
                for i in f:
                    key_value = i.strip().split(',')
                    accountDict[key_value[0]] = key_value[1]
                if id in accountDict:
                    QMessageBox.warning(self, "중복 아이디", "이미 존재하는 아이디입니다.\n아이디를 다시 설정 해주세요.")
                    self.id_lineEdit.setText('')
                    self.pw_lineEdit.setText('')
                    return
        # 아니면 고대로 account.txt에 입력해주고 account 생성
        with open('account.txt','a') as f:
            f.write(id + "," + pw + "\n")
            QMessageBox.about(self, "계정 생성", "계정이 등록되었습니다.")
            self.close()
            # 등록메세지가 뜨고 닫아줘야함


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = CreateAccount()
   sys.exit(app.exec())