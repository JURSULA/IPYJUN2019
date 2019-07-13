import turtle
import datetime
import time


# Display a clock to show the tie as 9:15:00

#def drawCLock(radius, hours, minutes, length):

def drawClock(hours, minutes, seconds):
      

    # Draw Clock
    
    turtle.pensize(7)
    turtle.color("black")
    turtle.penup()
    turtle.goto(0, 210)
    turtle.setheading(180)
    turtle.pendown()
    turtle.circle(210)

    # Draw the lines for the hours

    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)

    for hourHand in range (12):
        turtle.pensize(5)
        turtle.forward(190)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.goto(0,0)
        turtle.left(360/12)

    # Draw the hour hand
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    angle = (hours/12)*360
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(100)

    # Draw the minute hand
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    angle = (minutes/60)*360
    turtle.right(angle)
    turtle.pensize(3)
    turtle.pendown()
    turtle.forward(160)

    # Draw the Second hand
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    angle = (seconds/60)*360
    turtle.right(angle)
    turtle.pensize(1)
    turtle.pendown()
    turtle.forward(80)
    turtle.hideturtle()

    
    # Display time
    turtle.penup()
    turtle.goto(10, -260)
    style = ('Arial', 30, 'italic')
    h = str(hours)
    m = str(minutes)
    s = str(seconds)
    turtle.write(h + ":" + m + ":" + s , font=style, align='center')
    
    
        

drawClock(9, 15, 00)
