import sys
import os.path
from createAccount import CreateAccount
from main import Main
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        # 윈도우창 만들기
        self.setWindowTitle('Login')
        self.resize(700, 700)

        # 제목 라벨
        titleBox = QGroupBox(self)
        titleBox.move(160,100)
        titleBox.resize(370,60)
        title = QLabel('My Medicine Routine',self)
        title.setAlignment(Qt.AlignCenter)
        title.move(170,100)
        title.resize(350,50)
        title_font = title.font()
        title_font.setPointSize(25)
        title_font.setBold(True)
        title.setFont(title_font)

        # 로그인 파트 그룹박스로 만들기
        login_groupbox = QGroupBox('Login', self)
        login_groupbox.move(160,200)
        login_groupbox.resize(370,160)

        user_id = QLabel("ID",self)
        user_pw = QLabel("PW",self)
        user_id.move(190,220)
        user_id.resize(100,80)
        user_pw.move(182,270)
        user_pw.resize(100,80)

        self.id_lineEdit = QLineEdit(self)
        self.pw_lineEdit = QLineEdit(self)
        self.id_lineEdit.move(220,245)
        self.id_lineEdit.resize(200,30)
        self.pw_lineEdit.move(220,295)
        self.pw_lineEdit.resize(200,30)
        # 로그인 버튼
        login = QPushButton("Login",self)
        login.move(430,245)
        login.resize(80,80)
        login.clicked.connect(self.loginMessage)


        # 계정 만들기 버튼
        make_account_bnt = QPushButton('Create an account',self)
        make_account_bnt.resize(200,50)
        make_account_bnt.move(250,500)
        make_account_bnt.clicked.connect(self.clicked_createAccount)
        self.show()

    # 파일에 로그인 정보랑 일치 하는게 있는지 보고 있으면 통과, 없으면 불통
    def loginMessage(self):
        file = 'C:\\Users\\3DONS\\PycharmProjects\\routine\\account.txt'
        # 파일이 존재하는지 확인
        if os.path.isfile(file):
            # 파일이 존재하면 읽고 dict에 저장해둔다.
            # readline이런거 안썻는데 괜찮은지?
            with open('account.txt', 'r') as f:
                accountDict = {}
                for i in f:
                    key_value = i.strip().split(',')
                    print(key_value)
                    accountDict[key_value[0]] = key_value[1]
                print(accountDict)
            # self.f = open("account.txt", 'r')
            # input_id, input_pw = self.f.readlines().strip(',')
            # accountDict = {input_id: input_pw}

            id = self.id_lineEdit.text()
            pw = self.pw_lineEdit.text()
            # for문을 돌다가 딕셔너리 key랑 ID가 일치하는게 있으면 value가 password랑 일치하는게 있는지 확인
            # 아이디가 존재하는지 체크
            if id not in accountDict:
                loginFail_msgBox = QMessageBox.warning(self,"아이디 또는 비밀번호 오류","아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.")
                self.id_lineEdit.setText('')
                self.pw_lineEdit.setText('')
            # 아이디가 존재하면 pw와 일치하는지 체크
            # 로그인 성공하면 메인 페이지로 넘어야가함 연결 포인트!
            elif accountDict[id] == pw:
                print("로그인 성공")
                self.main()
            # 아이디가 존재하지만 pw와 일치하지 않는 경우
            else:
                loginFail_msgBox = QMessageBox.warning(self,"아이디 또는 비밀번호 오류","아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.")
                self.id_lineEdit.setText('')
                self.pw_lineEdit.setText('')

    def main(self):
        self.hide()
        self.second = Main(self)
        self.second.exec()
        self.show()

    # 아이디 비밀번호를 입력받아서 변수에 저장해놓고 파일에 써놔야함 파일로 연결
    # createAccount 버튼을 누르면 새로운 클래스로 연결하고 파일도 새로 만들어서 연결
    def clicked_createAccount(self):
        acc = CreateAccount(self)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Login()
   sys.exit(app.exec())