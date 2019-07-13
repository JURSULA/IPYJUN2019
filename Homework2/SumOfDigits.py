#Sum the digits in an user given number

number = eval(input("Enter a number between 0 and 1000:"))

#Intially assign sum of the digits in an integer to zero
sum = 0
#Sum of the digits in an integer
while(number):
    sum = sum + number %10
    number = number //10

print("The sum of the digits of the given interger {0} is: {1}".format(number, sum))
