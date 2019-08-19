class CountFileData:
    def __init__(self, filename):
        self.__filename = filename

    def countdata(self):
        with open(self.__filename, "r") as work_file:
            data = work_file.read()
            print("{0} characters".format(len(data)))
            print("{0} words".format(len(data.split())))
            print("{0} lines".format(data.count("\n")))

