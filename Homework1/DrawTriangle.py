import turtle
#Draw a triangle

turtle.pensize(5)

def drawTriangle(x,y):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    global side
    side = 3
    while(side !=0):
        turtle.forward(100)
        turtle.left(120)
        side = side - 1
  

drawTriangle(-110, -25)
