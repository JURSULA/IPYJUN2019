class Rectangle:
    # Construct a rectangle object 
    def __init__(self, width = 1, height = 2):
        self.__width = width
        self.__height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

