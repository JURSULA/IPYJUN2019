from Time import Time

time = Time()
print("Current Time is ", end='' )
time.printCurrentTime()

elapsedtime = int(input("Enter the elapsed time: "))
time.setNewTime(elapsedtime)
print("The hour:minute:second for the elapsed time is ", end='')
time.printCurrentTime()
