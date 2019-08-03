#Create a class called Fan
class Fan:

#Initialize variables with values 1,2,3
    SLOW = 1
    MEDIUM = 2
    FAST = 3

#Call Constructor for initializing variables
    def __init__(self, speed = 1, radius = 5, color = 'blue', on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

#Define Accessor & Mutator for all properties
    def setSpeed(self, speed):
        if speed == self.SLOW:
            self.__speed=self.SLOW
        elif speed==self.MEDIUM:
            self.__speed=self.MEDIUM
        else:
            self.__speed=self.FAST
        
    def setRadius(self,radius):
        self.__radius=radius
        
    def setColor(self,color):
        self.__color=color
        
    def setOn(self,on):
        self.__on=on
        
    def getSpeed(self):
        return self.__speed
    
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color
    
    def getOn(self):
        return self.__on
    
    def __str__(self): #print the object contents
        result="Speed ="+str(self.getSpeed())+" Radius= "+str(self.getRadius())+" Color= "+self.getColor()+" Status= "+str(self.getOn())
        return result

        
    
