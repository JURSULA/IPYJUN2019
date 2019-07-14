import turtle

#sets turtle characteristics
t = turtle.Turtle()
t.speed(0)

#draws and fills one Square
def square(size, alternte, color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.forward(size)

#Draw a row of square
def row(size, alternate, color1, color2):
    for i in range(4):
        if(alternate == True):
            square(size, alternate, color1)
            square(size, alternate, color2)
        else:
            square(size, alternate, color2)
            square(size, alternate, color1)

# Draw the whole chessboard outline
def chessboardOutline(size):
    t.penup()
    t.color("grey")
    t.pensize(5)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    
    

# Draw two chessboard
def chessboard(x, y, size, alternate, color1, color2):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    for i in range(8):
        row(size, alternate, color1, color2)
        t.backward(size*8)
        t.right(90)
        t.forward(size)
        t.left(90)
        if(alternate == True):
            alternate = False
        else:
            alternate = True
    t.goto(x, y = y + size)
    chessboardOutline((size*8))
    
    



chessboard(-350, 200, 35, True, "white", "black")
chessboard(-5, 200, 35,True,"white","black")



            
            
        





