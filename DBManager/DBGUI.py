# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bruce Ko\Desktop\DB GUI\DBGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(686, 484)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout.addWidget(self.lineEdit_id)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_first = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.horizontalLayout_2.addWidget(self.lineEdit_first)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_last = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_last.setObjectName("lineEdit_last")
        self.horizontalLayout_3.addWidget(self.lineEdit_last)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_email = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_4.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_5.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_5.addWidget(self.pushButton_delete)
        self.pushButton_update = QtWidgets.QPushButton(Dialog)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_5.addWidget(self.pushButton_update)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton_load = QtWidgets.QPushButton(Dialog)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout_2.addWidget(self.pushButton_load)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "First Name"))
        self.label_3.setText(_translate("Dialog", "Last Name"))
        self.label_4.setText(_translate("Dialog", "Email"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_delete.setText(_translate("Dialog", "Delete"))
        self.pushButton_update.setText(_translate("Dialog", "Update"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Last"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        self.pushButton_load.setText(_translate("Dialog", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
