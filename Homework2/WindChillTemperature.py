#Calculate Wind-Chill temperature

import math

temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))

windChillIndex = 35.74 + (0.6215 * temp) - (35.75 * (windSpeed **0.16)) + (0.4275 * (temp * (windSpeed **0.16)))

print("The Wind Chill Index is:", windChillIndex)

