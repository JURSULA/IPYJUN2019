from Stock import Stock

# Create a rectangle with width 4 and height 40 
stock = Stock("Intel", "INTC", 20.5, 20.35)
print("The price change is", stock.getChangePercent())
