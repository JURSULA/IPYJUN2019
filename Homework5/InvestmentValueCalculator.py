from tkinter import *

class InvestmentValueCalculator:
    def __init__(self):
        window = Tk()
        window.geometry("500x500")
        window.title("Investment Value Calculator")
        '''Create Label - w = Label(root, text="Hello, world!")'''
        Label(window, text = "Investment Amount:").grid(row =1, column=1, sticky= W)
        Label(window, text = "Years:").grid(row =2, column=1, sticky= W)
        Label(window, text = "Annual Interest Rate:").grid(row =3, column=1, sticky= W)
        Label(window, text = "Future Value:").grid(row =4, column=1, sticky= W)
        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar, justify = RIGHT).grid(row = 1, column = 2)
        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar, justify = RIGHT).grid(row = 2, column = 2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 3, column = 2)
        self.futureValueVar = StringVar()
        Label(window, textvariable = self.futureValueVar).grid(row = 4, column = 2,sticky=E)
        Button(window, text = "Calculate", command = self.computeFutureValue).grid(row=5, column = 2, sticky = E)
        window.mainloop()

    def computeFutureValue(self):
        monthlyInterestRate = (float(self.annualInterestRateVar.get())/100)/12
        futureValue = float(self.investmentAmountVar.get()) * (1 + monthlyInterestRate)**(int(self.yearsVar.get())*12)
        self.futureValueVar.set(format(futureValue, "10.2f"))
