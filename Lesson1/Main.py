import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import MessageSenderGUI

class Mainclass(QDialog, MessageSenderGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.SendMessage)
        self.pushButton_2.clicked.connect(self.ClearText)

    def SendMessage(self):
        message = self.lineEdit_send.text()
        self.plainTextEdit_receive.appendPlainText(message)

    def ClearText(self):
        self.plainTextEdit_receive.clear()




if __name__=='__main__':
    app = QApplication(sys.argv)
    msg = Mainclass()
    msg.show()
    app.exec_()