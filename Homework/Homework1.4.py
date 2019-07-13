
import math

#Homework 1.4

''' Program that displays the following table:
    a    a^2    a^3
    1    1      1
    2    4      8
    3    9      27
    4    16     64 '''

#To take number input from the user

count = int(input("Enter the table count:"))

print("a        a^2     a^3")
for i in range(1, count+1):
    num = 1
    print(i, "\t", end = ' ')
    print(i**2, "\t", end = ' ')
    print(i**3, "\t")
    i +=1
    
