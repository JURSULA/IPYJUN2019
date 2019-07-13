import turtle

#Draw Red Line

turtle.pensize(5)

def drawLine(color, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto (x1 + 5, y1 + 5)
    X1 = str(x1)
    Y1 = str(y1)
    turtle.write("(" + X1 + "," + Y1 + ")", font = ("Arial", 16, "normal"))
    turtle.goto (x2 + 5, y2 + 5)
    X2 = str(x2)
    Y2 = str(y2)
    turtle.write("(" + X2 + "," + Y2 + ")", font = ("Arial", 16, "normal"))


drawLine("red", x1 = -39, y1 = 48, x2 = 50, y2 = -50)
