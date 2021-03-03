import sys
import MortgageGUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from mortgage import Loan


class MainClass(QDialog, MortgageGUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # print("Total principal payments: ", loan.total_principal)
        # print("APR : ", loan.apr)
        # print("APY :  ", loan.apy)
        # print("Monthly Payment: ", loan.monthly_payment)
        # print("Total interest payments: ",  loan.total_interest)
        # print("Total payments:  ",  loan.total_paid)
        # print("Interest to principal: ", loan.interest_to_principle)
        # print("Years to pay: ",  loan.years_to_pay)
        self.pushButton_Calculate.clicked.connect(self.Calculate)

    def Calculate(self):
        TotalPrice = float(self.lineEdit_TotalPrice.text())
        DownPayment = float(self.lineEdit_DownPayment.text())
        InterestRate = float(self.lineEdit_IntRate.text())/100
        if self.comboBox_term.currentText() == "Months":
            Term = int(int(self.lineEdit_Term.text())/12)
        else:
            Term = int(self.lineEdit_Term.text())
        PrincipalBal = TotalPrice - DownPayment
        loan = Loan(principal=PrincipalBal, interest=InterestRate, term= Term)
        APR = loan.apr
        APY = loan.apy
        MonthlyPayment = loan.monthly_payment
        TotalPrincipalPay = PrincipalBal
        TotalIntPay = loan.total_interest
        TotalPay = loan.total_paid
        InttoPrincipal = loan.interest_to_principle
        self.lineEdit_PrincipalBal.setText(str("{:,.2f}".format(TotalPrincipalPay)))
        self.lineEdit_APR.setText(str(APR))
        self.lineEdit_APY.setText(str(APY))
        self.lineEdit_MonthPay.setText(str("{:,.2f}".format(MonthlyPayment)))
        self.lineEdit_TotalPrinPay.setText(str("{:,.2f}".format(TotalPrincipalPay)))
        self.lineEdit_TotalIntPay.setText(str("{:,.2f}".format(TotalIntPay)))
        self.lineEdit_TotalPay.setText(str("{:,.2f}".format(TotalPay)))
        self.lineEdit_InttoPrincipal.setText(str(InttoPrincipal))







if __name__=='__main__':
    app=QApplication(sys.argv)
    ims=MainClass()
    ims.show()
    app.exec_()


