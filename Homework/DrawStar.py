import turtle

#Draw a Star

turtle.pensize(5)

def drawStar(x,y):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    global side
    side= 5
    while(side !=0):
        turtle.forward(200)
        turtle.left(144)
        side = side - 1

drawStar(-110, -25)
    
