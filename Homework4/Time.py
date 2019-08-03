import datetime
now = 0
#Create Time Class
class Time:
    def __init__(self):
        global now
        now = datetime.datetime.now()
        self.__hour = now.hour
        self.__minute = now.minute
        self.__second = now.second

# Define Hour Property Accessor
    def getHour(self):
        return self.__hour

#Define Minute Property Accessor
    def getMinute(self):
        return self.__minute

#Define Second Property Accessor
    def getSecond(self):
        return self.__second

#Define the new time using the user inpute elpased time
    def setNewTime(self, elpasedTime):
        self.__hour = (elpasedTime//3600)%24
        elpasedTime = elpasedTime%3600
        self.__minute = elpasedTime//60
        elpasedTime = elpasedTime%60
        self.second = elpasedTime
        
#Define method to print the current time
    def printCurrentTime(self):
        print("%d:%d:%d" %(self.__hour,self.__minute,self.__second))
