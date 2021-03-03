from mortgage import Loan
import locale

loan = Loan(principal=300000.16, interest=6/100, term=int(120/12))

print(loan.summarize)

print("Total principal payments: ", loan.total_principal)
print("APR : ", loan.apr)
print("APY :  ", loan.apy)
print("Monthly Payment: ", loan.monthly_payment)
print("Total interest payments: ",  loan.total_interest)
print("Total payments:  ",  loan.total_paid)
print("Interest to principal: ", loan.interest_to_principle)
print("Years to pay: ",  loan.years_to_pay)