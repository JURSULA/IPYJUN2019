import turtle

#Draw Four Squares at the center of the page

turtle.pensize(5)

def drawSquare(x, y):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    global side
    side = 4
    while(side !=0):
        turtle.forward(100)
        turtle.right(90)
        side = side - 1
  

drawSquare(-110, -25)
drawSquare(-110, -125)
drawSquare(-10, -25)
drawSquare(-10, -125)
    


