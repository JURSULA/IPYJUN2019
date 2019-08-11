from tkinter import *

class TrafficLight:
    def __init__(self):
        #create window, set its title and size
        window = Tk()
        window.title("Traffic Lights")
        window.geometry("500x500")

        #create frame and add it to the window
        frame = Frame(window, borderwidth = 1, relief = "raised")
        frame.pack()

        #Create canvas and add it to the window
        self.canvas = Canvas(window, width = 500, height = 500)
        self.canvas.pack()

        #Variable for the at the moment current traffic light
        self.color = StringVar()
        self.color.set('B') #no light is ON
        

        #Add 3 circles for three traffic lights to the canvas
        self.cRed = self.canvas.create_oval(30,10,140,110)
        self.cYellow = self.canvas.create_oval(30,110,140,210)
        self.cGreen = self.canvas.create_oval(30,210,140,310)
        self.canvas.create_rectangle(30,10,140,310)

        #Add 3 radio buttons for traffic lights to the frame
        rRed = Radiobutton(frame, text = "Red", variable = self.color, value = 'R', command = self.processRadio).grid(row=10, column = 1)
        rYellow = Radiobutton(frame, text = "Yellow", variable = self.color, value = 'Y', command = self.processRadio).grid(row=10, column = 2)
        rGreen = Radiobutton(frame, text = "Green", variable = self.color, value = 'G', command = self.processRadio).grid(row=10, column = 3)

        #Create an event loop
        window.mainloop()

    def processRadio(self):
        #Get the currently clicked radio button
        color = self.color.get()

        #If red Radio button is clicked
        if color == 'R':
            self.canvas.itemconfig(self.cRed, fill = "red")
            self.canvas.itemconfig(self.cYellow, fill = "white")
            self.canvas.itemconfig(self.cGreen, fill = "white")

        #If Yellow Radio button is clicked
        elif color == 'Y':
            self.canvas.itemconfig(self.cRed, fill = "white")
            self.canvas.itemconfig(self.cYellow, fill = "yellow")
            self.canvas.itemconfig(self.cGreen, fill = "white")
        
        #If Green Radio button is clicked
        elif color == 'G':
            self.canvas.itemconfig(self.cRed, fill = "white")
            self.canvas.itemconfig(self.cYellow, fill = "white")
            self.canvas.itemconfig(self.cGreen, fill = "green")



    
    
   

    
   
   
    
    
    
