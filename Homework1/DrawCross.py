import turtle

#Draw a cross

turtle.pensize(5)

def drawVerticalLine(x1 = 0, y1 = 0, x2 =-110, y2= 125):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

def drawHorizontalLine(x1 = -55, y1 = 65, x2 = 0, y2 = 0):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)



drawVerticalLine(x1 = -110, y1 = -25)
drawHorizontalLine(x2 = -165, y2 = 65)

