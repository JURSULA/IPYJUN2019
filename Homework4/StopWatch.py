import time
import datetime
class StopWatch:
    def __init__(self):
        self.__startTime = datetime.datetime.now().time()
        #self.__startTime = time.time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__endTime = time.time()
    def getElapsedTime(self):
        return int(1000*(self.__endTime - self.__startTime))
    
        
        
        
