import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Medicine Routine')
        self.resize(700, 700)

        grid = QGridLayout()
        self.setLayout(grid)


        grid.addWidget(QLabel('My Medicine Routine'),0,0,1,1, alignment=Qt.AlignHCenter)
        grid.addWidget(self.createLoginGroup(),1,0,2,1, alignment=Qt.AlignHCenter)
        grid.addWidget(QPushButton('Create an account'),3,0,1,1, alignment=Qt.AlignHCenter)
        self.show()

    def createLoginGroup(self):
        groupbox = QGroupBox('Login')

        id = QLabel("ID")
        pw = QLabel("PW")

        self.id_lineEdit = QLineEdit()
        self.pw_lineEdit = QLineEdit()

        login = QPushButton("Login")
        login.clicked.connect(self.loginMessage)

        createGrid = QGridLayout()
        createGrid.addWidget(id,0,0,1,1)
        createGrid.addWidget(pw,1,0,1,1)
        createGrid.addWidget(self.id_lineEdit,0,1,1,2)
        createGrid.addWidget(self.pw_lineEdit,1,1,1,2)
        createGrid.addWidget(login,0,4,2,6)
        groupbox.setLayout(createGrid)

        return groupbox

    def loginMessage(self):
        msgBox = QMessageBox()
        id = self.id_lineEdit.text()
        pw = self.pw_lineEdit.text()
        login_info = "ID:" + id +"\nPW:" + pw
        msgBox.setText(login_info)
        return msgBox.exec()






if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec())