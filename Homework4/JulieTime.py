import time
import datetime
class Time:
    def __init__(self):
        self.__hour = datetime.datetime.now().hour
        self.__minute = datetime.datetime.now().minute
        self.__second = datetime.datetime.now().second
        
    def getHour(self):
        return self.__hour
       
    def getMinute(self):
        return self.__minute
       
    def getSecond(self):
        return self.__second
    
    def setTime(self, elapseTime):
        print("Current Time is {0}:{1}:{2}".format(self.getHour(), self.getMinute(), self.getSecond()))
        h = int(elapseTime/3600)
        m = int((elapseTime%3600)/60)
        s = elapseTime - (h*3600 + m*60)
        '''print("Hour", h)
        print("Minute", m)
        print("Second", s)'''

        self.__hour += datetime.timedelta(hours = h)
        
        print("The hour:minute:second for the elapsed time is ", end='')
        print("%d:%d:%d" % (self.getSecond(), self.getMinute(), self.getHour()))

          
   
