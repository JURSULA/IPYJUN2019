from tkinter import *
import pymysql
from ReadConfig import read_db_config

class AddressBook:
    def __init__(self):
        self.__currentID = 1

        #Create Window
        window = Tk()
        window.geometry("500x150")
        window.title("Address Book")
        '''frame = Frame(window, borderwidth=1, relief="raised")
        frame.pack()'''

      #Create Lables and Textboxes to the window
        
        Label(window, text = "Name:").grid(row =1, column=1, sticky= W)

        self.nameVar = StringVar()
        Entry(window, textvariable = self.nameVar, justify = RIGHT).grid(row = 1, column = 2)

        Label(window, text = "Street:").grid(row =2, column=1, sticky= W)

        self.streetVar = StringVar()
        Entry(window, textvariable = self.streetVar, justify = RIGHT).grid(row = 2, column = 2)

        Label(window, text = "City:").grid(row =3, column=1, sticky= W)

        self.cityVar = StringVar()
        Entry(window, textvariable = self.cityVar, justify = RIGHT).grid(row = 3, column = 2)

        Label(window, text = "State:").grid(row =3, column=3, sticky= W)

        self.stateVar = StringVar()
        Entry(window, textvariable = self.stateVar, justify = RIGHT).grid(row = 3, column = 4)

        Label(window, text = "ZIP:").grid(row =3, column=5, sticky= E)

        self.zipVar = StringVar()
        Entry(window, textvariable = self.zipVar, justify = RIGHT).grid(row = 3, column = 6)

        self.messageVar = StringVar()
        Label(window, textvariable= self.messageVar).grid(row=6, column=1, columnspan = 4, sticky=W)
        self.messageVar.set("Message: No Error")

        #Create Buttons to the window
        Button(window, command = self.addAddress, text = "Add").grid(row=4, column = 2, sticky = W)
        Button(window, command = self.getFirst, text = "First").grid(row=4, column = 2)
        Button(window, command = self.getNext, text = "Next").grid(row=4, column = 2, sticky = E)
        Button(window, command = self.getPrevious, text = "Previous").grid(row=4, column = 3, sticky = W)
        Button(window, command = self.getLast, text = "Last").grid(row=4, column = 4, sticky = W)
        window.mainloop()

    def addAddress(self):
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        print("Name: {0}, Street: {1}, City: {2}, State: {3}, Zip: {4}".format(self.nameVar.get(), self.streetVar.get(),self.cityVar.get(), self.stateVar.get(), self.zipVar.get()))
        #cursor.execute('INSERT INTO addressBook (Name, Street, City, State, Zip) VALUES("Ria", "0001", "Redmond", "WA", "98007")')
        sql = "INSERT INTO addressBook (Name, Street, City, State, Zip) VALUES('%s', '%s', '%s', '%s', '%s')" % (self.nameVar.get(), self.streetVar.get(), self.cityVar.get(), self.stateVar.get(), self.zipVar.get())
        cursor.execute(sql)
        db.commit()
        cursor.execute('SELECT * FROM addressBook')
        data = cursor.fetchall()
        print(data)
        print("Sucessfuly created an address in address book")
        self.messageVar.set("Message: Sucessfuly created an address in address book")
        cursor.execute('SELECT * FROM employeedb.addressBook '
                       'ORDER BY Id DESC '
                       'LIMIT 1')
        data = cursor.fetchone()
        self.__currentID = data[0]
        db.close()

    def getFirst(self):
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        sql = 'SELECT * FROM employeedb.addressBook LIMIT 1'
        cursor.execute(sql)
        data = cursor.fetchone()
        self.__currentID = data[0]
        self.nameVar.set(data[1])
        self.streetVar.set(data[2])
        self.cityVar.set(data[3])
        self.stateVar.set(data[4])
        self.zipVar.set(data[5])
        print(data)
        print("Sucessfuly pulled first address from address book")
        self.messageVar.set("Message: Sucessfuly pulled first address from address book")
        db.close()

    def getLast(self):
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        sql = 'SELECT * FROM employeedb.addressBook ORDER BY Id DESC LIMIT 1'
        cursor.execute(sql)
        data = cursor.fetchone()
        self.__currentID = data[0]
        self.nameVar.set(data[1])
        self.streetVar.set(data[2])
        self.cityVar.set(data[3])
        self.stateVar.set(data[4])
        self.zipVar.set(data[5])
        print(data)
        print("Sucessfuly pulled last address from address book")
        self.messageVar.set("Message: Sucessfuly pulled last address from address book")
        db.close()

    def getNext(self):
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        sql = 'SELECT * FROM employeedb.addressBook WHERE Id = (%d)' % (self.__currentID + 1)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            self.__currentID = data[0]
            self.nameVar.set(data[1])
            self.streetVar.set(data[2])
            self.cityVar.set(data[3])
            self.stateVar.set(data[4])
            self.zipVar.set(data[5])
            print(data)
            self.messageVar.set("Message: Sucessfuly pulled next address from address book")
            #print("Sucessfuly pulled first address from address book")
        else:
            print("No Data")
            self.__currentID +=1
            self.messageVar.set("Message: No Data")

        db.close()

    def getPrevious(self):
        dbParam = read_db_config()
        db = pymysql.connect(**dbParam)
        cursor = db.cursor()
        sql = 'SELECT * FROM employeedb.addressBook WHERE Id = (%d)' % (self.__currentID - 1)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            self.__currentID = data[0]
            self.nameVar.set(data[1])
            self.streetVar.set(data[2])
            self.cityVar.set(data[3])
            self.stateVar.set(data[4])
            self.zipVar.set(data[5])
            print(data)
            self.messageVar.set("Message: Sucessfuly pulled previous address from address book")
            # print("Sucessfuly pulled first address from address book")
        else:
            print("No Data")
            self.__currentID -= 1
            self.messageVar.set("Message: No Data")
        db.close()




