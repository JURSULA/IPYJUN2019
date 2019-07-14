# Implement Square Root using Babylonian Algorithm

# Define the Square Root Function
def sqrt(n):
    if (n == 0):
        return 0;

    global lastGuess
    lastGuess = 1
    nextGuess = (lastGuess + (n/lastGuess))/2
    if (nextGuess - lastGuess <= 0.0001):
        return nextGuess
    while (lastGuess != nextGuess):
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n/lastGuess))/2
    return nextGuess

n = eval(input("Enter a number:"))
sqrt = sqrt(n)
print("The Square Root of {0} is = {1}".format(n, sqrt))
