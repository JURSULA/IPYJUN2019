#Find the number of years and days from user given time in minutes

minutes = eval(input("Enter the minutes:"))

#Constant

DAYS_PER_YEARS = 365
MINUTES_PER_DAY = 1440

#Calculate years and days from minutes

days = minutes/MINUTES_PER_DAY
years = days/365

#Convert to whole numbers

numberOfYears = int(years)
daysPerYear = years%1
numberOfDays = int(daysPerYear * 365)

print("{0} minutes is approximately {1} years and {2} days".format(minutes, numberOfYears, numberOfDays))

