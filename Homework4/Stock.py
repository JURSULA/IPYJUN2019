class Stock:
    # Construct a stock object 
    def __init__(self, name, symbol, previousClosingPrice, currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPreviousClosingPrice(self):
        return self.previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setPreviousClosingPrice(self, previousClosingPrice):
        self.previousClosingPrice = previousClosingPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return format((self.__currentPrice - self.previousClosingPrice) * 100 / self.previousClosingPrice, "5.2f") + "%"

