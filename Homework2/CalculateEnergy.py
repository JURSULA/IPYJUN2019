'''Calculate Energy by getting water amount in kilograms and initial and
final temperatures in Celsius from the user'''

M = eval(input("Enter the amount of the water in kilogram:"))

initialTemp = eval(input("Enter the initial temperature in Celsius:"))

finalTemp = eval(input("Enter the final temperature in Celsius:"))

Q = M * (finalTemp - initialTemp) * 4184

print("The energy needed is: {0} joulies".format(Q))


