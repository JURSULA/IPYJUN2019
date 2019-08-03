class Account():
    def __init__(self, accountId =0, accountBalance=100, annualInterestRate = 0):
        self.__accountId = accountId
        self.__accountBalance = accountBalance
        self.__annualInterestRate = annualInterestRate
    def getAccountId(self):
        return self.__accountId
    def setAccountId(self, accountId):
        self.__accountId = int(accountId)
    def getAccountBalance(self):
        return self.__accountBalance
    def setAccountBalance(self, accountBalance):
        self.__accountBalance = float(accountBalance)
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = float(annualInterestRate)
    def getMonthlyInterestRate(self):
        return float(self.__annualInterestRate)/12
    def getMonthlyInterest(self):
        return self.__accountBalance * self.getMonthlyInterestRate()/100
    def withdraw(self, withdraw):
        self.__accountBalance -= withdraw
    def deposit(self, deposit):
        self.__accountBalance += deposit
    
