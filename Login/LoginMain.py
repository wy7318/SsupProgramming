import sys
import LoginGUI, WelcomeGUI, SignUpGUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

class Login(QDialog, LoginGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_singUp.clicked.connect(self.SignUp)
        self.pushButton_signIn.clicked.connect(self.SignIn)
        self.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)

    def SignUp(self):
        self.signupPage = SignUp()
        self.signupPage.show()

    def SignIn(self):
        id = self.lineEdit_id.text()
        pw = self.lineEdit_pw.text()

        if id != "":
            if pw != "":
                self.welcomePage = Welcome()
                self.welcomePage.show()
                self.welcomePage.label_welcome.setText("Welcome " + id)
            else:
                QMessageBox.about(self, "Warning", "Please Enter Password")
        else:
            QMessageBox.about(self, "Warning", "Please Enter ID")


class SignUp(QDialog, SignUpGUI.Ui_Dialog):
    def __init__(self):
        super(SignUp, self).__init__()
        self.setupUi(self)

        self.pushButton_create.clicked.connect(self.Register)
        self.pushButton_cancel.clicked.connect(self.close)
        self.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)

    def Register(self):
        First = self.lineEdit_first.text()
        Last = self.lineEdit_last.text()
        id = self.lineEdit_id.text()
        pw = self.lineEdit_pw.text()

        if First != "":
            if Last != "":
                if id != "":
                    if pw != "":
                        QMessageBox.about(self, "Complete", "Congrats! {} {}. You have successfully created the account".format(First, Last))
                    else:
                        QMessageBox.about(self, "Warning", "Please Enter your password")
                else:
                    QMessageBox.about(self, "Warning", "Please Enter your ID")
            else:
                QMessageBox.about(self, "Warning", "Please Enter your Last Name")
        else:
            QMessageBox.about(self, "Warning", "Please Enter your First Name")



class Welcome(QDialog, WelcomeGUI.Ui_Dialog):
    def __init__(self):
        super(Welcome, self).__init__()
        self.setupUi(self)

        self.pushButton_signOut.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec_()