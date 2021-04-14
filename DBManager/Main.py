import mysql.connector
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import DBGUI

class MainClass(QDialog, DBGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_load.clicked.connect(self.loadDB)
        self.pushButton_add.clicked.connect(self.addData)
        self.pushButton_delete.clicked.connect(self.DeleteData)
        self.pushButton_update.clicked.connect(self.updateData)
        self.tableWidget.cellDoubleClicked.connect(self.selectedCell)

        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


    def loadDB(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        query = "SELECT ID, empF, empL, email FROM account"
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        cur.close()

    def addData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        ID = self.lineEdit_id.text()
        firstN = self.lineEdit_first.text()
        lastN = self.lineEdit_last.text()
        email = self.lineEdit_email.text()

        cur = connection.cursor()

        insertq = "INSERT INTO account (id, empF, empL, email) VALUES (%s, %s, %s, %s)"
        values = (ID, firstN, lastN, email,)

        try:
            cur.execute(insertq, values)
            connection.commit()
            print("Success")
        except:
            print("failed")

    def DeleteData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()
        email = self.lineEdit_email.text()
        deleteq = "DELETE FROM account WHERE email = %s"
        values = (email,)

        try:
            cur.execute(deleteq, values)
            connection.commit()
            print("success")
        except:
            print("failed")

    def updateData(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()
        firstN = self.lineEdit_first.text()
        lastN = self.lineEdit_last.text()
        email = self.lineEdit_email.text()
        updateq = "UPDATE account SET empF = %s, empL = %s WHERE email = %s"
        values = (firstN, lastN, email,)

        try:
            cur.execute(updateq, values)
            connection.commit()
            print("Success")
        except:
            print("failed")

    def selectedCell(self):
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Usopen97!",
            database="Employees"
        )

        cur = connection.cursor()

        self.index = self.tableWidget.selectedItems()

        query = "SELECT ID, empF, empL, email FROM account WHERE ID = %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.lineEdit_id.setText(row[0])
                self.lineEdit_first.setText(row[1])
                self.lineEdit_last.setText(row[2])
                self.lineEdit_email.setText(row[3])
        except:
            print("Fill Failed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ims = MainClass()
    ims.show()
    app.exec_()