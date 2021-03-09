from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
import time
from threading import Timer
import ClockGUI

class MainClass(QDialog, ClockGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.showtime()

    def showtime(self):
        t = time.time()
        local = time.localtime(t)

        self.lcdNumber_year.display(local.tm_year)
        self.lcdNumber_month.display(local.tm_mon)
        self.lcdNumber_date.display(local.tm_mday)
        self.lcdNumber_hour.display(local.tm_hour)
        self.lcdNumber_min.display(local.tm_min)
        self.lcdNumber_sec.display(local.tm_sec)

        timer = Timer(1, self.showtime)
        timer.start()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    clockmain = MainClass()
    clockmain.show()
    app.exec_()