#Display first 100 Pentagonal Numbers

from math import *

#Define Pentagonal function

def getPentagonalNumbers(n):
    global answer
    answer = 0
    answer = int((n * ((3 * n) - 1))/2)
    
      

#Test the Pentagonal function

global n
n = 0
global count
count = 0
global num
num = 10
if (count <= 100):
    for row in range (num):
        for col in range (10):
            n +=1
            getPentagonalNumbers(n)
            print(answer, end=' ')
        print()
    count +=10
    num = count + 10
        
