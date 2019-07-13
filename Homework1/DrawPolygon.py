import turtle

#Draw a Polygon

turtle.pensize(5)

def drawPolygon(x, y):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    global side
    side = 6
    while(side !=0):
        turtle.forward(200)
        turtle.right(60)
        side = side-1

drawPolygon(-110, 100)
