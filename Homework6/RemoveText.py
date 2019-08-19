class RemoveText:
    def __init__(self, fileName, word):
        self.__fileName = fileName
        self.__word = word
    def removeText(self):
        data = ""
        with open("test.txt", "r") as work_file:
            data = work_file.read()
            #print(data)
            data = data.replace(self.__word,"")
            #print(data)
        with open("test.txt", "w") as work_file:
            work_file.write(data)
        

        
        
