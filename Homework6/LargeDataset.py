import random
class LargeDataset:
    def __init__(self):
        self.__rankTuple = ("assistant", "associate", "full")
        self.__salaryDict = {"assistant" : [50000.00, 80000.00],
                      "associate": [60000.00, 110000.00],
                      "full": [750000.00, 80000.00]
        }

    def createLargeDataset(self):
        with open("Salary.txt", "w") as work_file:
            for i in range (1, 1001):
                rank = self.__rankTuple[random.randrange(len(self.__rankTuple))]
                salaryArray = self.__salaryDict[rank]
                work_file.write("FirstName{0} LastName{1} {2} {3} \n".format(str(i), str(i), rank, str(
                    round(random.uniform(salaryArray[0], salaryArray[1]), 2))))

                '''if rank == "assistant":
                    work_file.write("FirstName{0} LastName{1} {2} {3} \n".format(str(i),str(i),rank, str(round(random.uniform(50000.00, 80000.00),2))))
                elif rank == "associate":
                    work_file.write("FirstName{0} LastName{1} {2} {3} \n".format(str(i),str(i),rank, str(round(random.uniform(60000.00, 110000.00),2))))
                else:
                    work_file.write("FirstName{0} LastName{1} {2} {3} \n".format(str(i), str(i), rank, str(round(random.uniform(75000.00, 130000.00), 2))))'''
            print("File created")