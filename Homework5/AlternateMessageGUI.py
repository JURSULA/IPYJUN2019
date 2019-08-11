from tkinter import *

class AlternateMessageGUI:
    def __init__(self):

        #create window and set its title
        window = Tk()
        window.title("Alternate Messages")

        #Define a boolean variable for alternate click
        self.__alternate = False

        #Create and add a canvas to window
        self.canvas = Canvas(window, width = 220, height = 100)
        self.canvas.pack()

        #Display initial message
        self.canvas.create_text(110, 50, text = "Programming is fun", tags = "text")

        #Bind Canvas with left mouse click
        self.canvas.bind('<Button-1>', self.change)

        window.mainloop()

    #Method to handle mouse click
    def change(self, event):

        #Delete the previous text
        self.canvas.delete("text")

        #Display message as per alternate variable
        if self.__alternate:
            self.canvas.create_text(110, 50, text = "Programming is fun", tags = "text")
        else:
            self.canvas.create_text(110, 50, text = "It is fun to program", tags = "text")

        #Change the current value to alternate variable
        self.__alternate = not self.__alternate
