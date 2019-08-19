import random
import os.path
class WriteReadFile:
    def __init__(self, filename):
        self.__filename = filename
    def sortIntegers(self):
        if os.path.exists(self.__filename):
            print("The file already exists")
        else:
            with open (self.__filename, "w") as work_data:
                for x in range(100):
                    work_data.write(str(random.randint(1,1000))+ " ")
            with open(self.__filename, "r") as work_data:
                words = work_data.read()
                words = words.strip()
                wordArray = words.split(" ")
                wordArray = [int(i) for i in wordArray]
                wordArray.sort()
                print(*wordArray, sep = " ")
                
                    
                
        
