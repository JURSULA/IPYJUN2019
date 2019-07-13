import turtle

#Draw Four Circles

turtle.pensize(5)

def drawCircle():
    turtle.circle(45)
    turtle.circle(-45)
    turtle.penup()
    turtle.goto(90, 0)
    turtle.pendown()

drawCircle()
drawCircle()



