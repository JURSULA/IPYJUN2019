from Account import Account

account1 = Account(1122, 20000, 4.5)
account1.withdraw(2500)
account1.deposit(3000)
print("Account ID:",account1.getAccountId())
print("Account Balance:$",account1.getAccountBalance())
print("Monthly Interest Rate: {0}%".format(account1.getMonthlyInterestRate()))
print("Monthly Interest:$",account1.getMonthlyInterest())
print(account1.getAnnualInterestRate())
