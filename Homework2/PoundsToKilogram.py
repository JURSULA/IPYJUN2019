#Converts pounds into Kilogram by getting pounds value from user

pounds = eval(input("Enter a value in pounds:"))

#Constant

KILOGRAMS_PER_POUND = 0.454

#Convert pounds to kilogram

kilograms = pounds * KILOGRAMS_PER_POUND

print("{0} pounds is {1} kilograms.".format(pounds, kilograms))
