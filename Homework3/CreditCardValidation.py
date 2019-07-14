#Financial: Credit Card NUmber Validation

#Define function to return sum of doubled digit number
def sumDigits(number):
    sumDigits = 0
    length = len(number)
    for i in range(length):
        sumDigits += int(number[i])
    return sumDigits

#Define function to Double Even place integer of a given number
def sumOfDoubleEvenPlace(number):
    length = len(number)
    evenSum = 0
    for i in range(length-2, -1, 2):
        number = number[i]
        intNumber = int(number)
        intNumber = intNumber * 2
        if(intNumber > 9):
            strNumber = str(intNumber)
            evenSumDigits = sumDigits(strNumber)
            evenSum +=evenSumDigits
        else:
            evenSum +=intNumber
    return evenSum
    



#Define function to Double odd place integer of a given number
def sumOfOddPlace(number):
    length = len(number)
    oddSum = 0
    for i in range(length-1, -1, 2):
        number = number[i]
        intNumber = int(number)
        intNumber = intNumber * 2
        if(intNumber > 9):
            strNumber = str(intNumber)
            oddSumDigits = sumDigits(strNumber)
            oddSum += oddSumDigits
        else:
            oddSum +=intNumber
    return oddSum
    

#Define function to validate the given integer
def isValid(number):
    evenTotal = sumOfDoubleEvenPlace(number)
    oddTotal = sumOfOddPlace(number)
    total = evenTotal + oddTotal
    if((total % 10) == 0):
        return print("The entered Credit Card Number:{0} is VALID".format(number))
    else:
        return print("The entered Credit Card Number:{0} is INVALID".format(number))




#Define function to check the lenght of the number
def getCreditCard(number):
    length = len(number)
    if((length >= 13 and length <= 16) and (number[0] == "4" or number[0] == "5" or number[0] == "6" or (number[0] == "3" and number[1] == "7"))):
        return isValid(number)
    else:
        return print("Enter a valid Credit Card Number")


stringNumber = input("Enter your credit card number:")
getCreditCard(stringNumber)
    

