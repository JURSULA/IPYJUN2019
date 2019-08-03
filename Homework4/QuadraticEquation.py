class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getA(self):
        self.__a = a
    def getB(self):
        self.__b = b
    def getC(self):
        self.__c = c
        
    def getDiscriminant(self):
        result = ((self.__b)**2) - (4 * self.__a * self.__c)
        print("The Discriminant is:", result)
        if result > 0:
            print (quadraticequation.getRoot2())
        elif result == 0:
            print(quadraticequation.getRoot1())
        else:
            print("The equation has no roots")


    def getRoot1(self):
        return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)
        
    def getRoot2(self):
        return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)


