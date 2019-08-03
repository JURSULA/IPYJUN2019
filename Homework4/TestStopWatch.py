from JulieStopWatch import StopWatch

sw = StopWatch()
print(sw.getStartTime())
#declare a sum varialble
sum = 0
sw.start()
for i in range (1, 1000000):
    sum +=i
sw.stop()
print("Time taken in milliseconds: ",sw.getElapsedTime())
