#Palindrome Integer

num = int(input("Enter a number to be reversed:"))

# Define function to reverse the given integer
def reverseInteger(num):
    global revNum
    revNum = 0
    while(num>0):
        reminder = num % 10
        revNum = (revNum * 10) + reminder
        num = num//10
    return revNum


if(reverseInteger(num) == num):
    print("The number is Palindrome")
else:
    print("The number is not a Palindrome")


