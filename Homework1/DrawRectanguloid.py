import turtle

#Draw Rectanguloid

turtle.pensize(5)

def drawRectanguloid(x,y,z):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    global side
    side = 2
    while(side !=0):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        side = side - 1

drawRectanguloid(0, 0, 0)
drawRectanguloid(100, 0, 0)
drawRectanguloid(100, 100, 0)
drawRectanguloid(0, 100, 0)
drawRectanguloid(0, 0, 100)
drawRectanguloid(100, 0, 100)
drawRectanguloid(100, 100, 100)
drawRectanguloid(0, 100, 100)
    
