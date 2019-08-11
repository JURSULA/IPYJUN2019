from tkinter import *

class AddressBook:
    def __init__(self):

        #Create Window
        window = Tk()
        #window.geometry("500x500")
        window.title("Address Book")

        '''#Create Frame to the window
        frame = Frame(window)
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

        self.ZipVar = StringVar()
        Entry(window, textvariable = self.ZipVar, justify = RIGHT).grid(row = 3, column = 6)

        #Create Buttons to the window
        Button(window, text = "Add").grid(row=4, column = 2, sticky = W)
        Button(window, text = "First").grid(row=4, column = 2)
        Button(window, text = "Next").grid(row=4, column = 2, sticky = E)
        Button(window, text = "Previous").grid(row=4, column = 3, sticky = W)
        Button(window, text = "Last").grid(row=4, column = 4, sticky = W)

        window.mainloop()
    
