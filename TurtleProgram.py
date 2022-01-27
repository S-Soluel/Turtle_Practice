# Name: Sam Solheim
# Date: 9/14/2020
# description: The Turtle program that I created includes
# functions for sunflowers, clouds, and the ground.
# If I work on this in the future, I might try to make edit some of my current functions
# to make them slightly less 'clunky.'

import turtle

def rectangle(t, length, color):
    """Draws a rectangle with a given length, of a given color

    Parameters:
        t = a turtle
        length = a number
        color = a color supported by Python
    Returns:
        Nothing
    Preconditions:
        length > 4
    """  
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.lt(90)
        t.forward(length/4)
        t.lt(90)
    t.end_fill()

def cloud(t, n, color):
    """Draws a single cloud component, of a given
        color, to be used in clouds function

    Parameters:
        t = a turtle
        n = an integer
        color = a color supported by Python
    Returns:
        Nothing
    Preconditions:
        n > 2
    """  
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for i in range(n):
        t.forward((n))
        t.lt(360/n)
    t.end_fill()

def clouds(t, n, color):
    """Draws a cloud formation, with a given (n)
        number of program repetitions, of a
        given color. Formula set to not have completely
        circular clouds

    Parameters:
        t = a turtle
        n = an integer
        color = a color supported by Python
    Returns:
        Nothing
    Preconditions:
        n > 2
    """  
    for i in range(n):
        cloud(t, 3*n, color)
        t.lt(360/n)
        cloud(t, n, color)
        t.rt(360/(40+n))
        cloud(t, 2*n, color)
        t.rt(20*n)
        t.forward(n/6)
        cloud(t, n*2, color)
        t.rt(140/n)

def flower(t, length, n, color):
    """Draws a sunflower of a given diameter (length),
        given number (n) of repetitions, and given color

    Parameters:
        t = a turtle
        length = a number
        n = an integer
        color = a color supported by Python
    Returns:
        Nothing
    Preconditions:
        length > 3
    """  
    t.fillcolor(color)
    t.begin_fill()
    t.speed(500)
    for i in range(n):
        t.forward(length/3)
        t.lt(240/2*n)
        t.forward(length*2)
        t.lt(120/n)
        t.forward(length/2)
        t.lt(120/n)
    t.end_fill()
    
def stem(t, length, color):
    """Draws a sunflower stem of given length and color

    Parameters:
        t = a turtle
        length = a number
        color = a color supported by Python
    Returns:
        Nothing
    Preconditions:
        length > 1
    """  
    t.fillcolor(color)
    t.begin_fill()
    t.speed(500)
    for i in range(2):
        t.forward(length)
        t.lt(90)
        t.forward(30)
        t.lt(90)
    t.end_fill()

turtle.bgcolor("sky blue")
susan=turtle.Turtle()
turtle.title("Sunflowers and Sky")
susan.speed(100000)
#Apparently I just have a lot of code so I tried
#speeding it up as much as possible and it decided
#not to go very fast

# Start of code relating to drawing design

#Ground
susan.penup()
susan.goto(-475,-400)
susan.pendown()
rectangle(susan, 950, "forest green")

#Clouds
#Draws three different clouds, two of which
#utilize the clouds function twice
susan.penup()
susan.goto(400, 300)
susan.pendown()
clouds(susan, 5, "white")

susan.penup()
susan.goto(-400, 250)
susan.pendown()
clouds(susan, 6, "white")
susan.penup()
susan.goto(-375, 300)
clouds(susan, 5, "white")

susan.penup()
susan.goto(20, 180)
susan.pendown()
clouds(susan, 5, "white")
susan.penup()
susan.goto(0, 240)
susan.pendown()
clouds(susan, 6, "white")

#Flowers
#Draws six flowers with their stems, petals, and
#seeds
susan.pencolor("black")
susan.penup()
susan.goto(-271,-75)
susan.pendown()
susan.lt(-196)
stem(susan, 300, "lime green")
susan.penup()
susan.lt(90)
susan.penup()
susan.goto(-200,0)
susan.pendown()
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(-223,-17)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(-71,-25)
susan.pendown()
susan.rt(90)
stem(susan, 300, "lime green")
susan.lt(90)
susan.penup()
susan.goto(0,50)
susan.pendown()
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(-23,50-17)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(129,100)
susan.pendown()
susan.rt(90)
stem(susan, 400, "lime green")
susan.penup()
susan.goto(200,175)
susan.pendown()
susan.lt(90)
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(200-23, 158)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(300, 75)
susan.pendown()
susan.rt(90)
stem(susan, 250, "lime green")
susan.penup()
susan.goto(371,150)
susan.pendown()
susan.lt(90)
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(348,133)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(300-100, 0)
susan.pendown()
susan.rt(90)
stem(susan, 250, "lime green")
susan.penup()
susan.goto(371-100,75)
susan.pendown()
susan.lt(90)
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(348-100,133-75)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(50, 0)
susan.pendown()
susan.rt(90)
stem(susan, 250, "lime green")
susan.penup()
susan.goto(371-250,150-75)
susan.pendown()
susan.lt(90)
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(348-250,133-75)
susan.pendown()
flower(susan, 29, 80, "black")

susan.penup()
susan.goto(-200, -50)
susan.pendown()
susan.rt(90)
stem(susan, 250, "lime green")
susan.penup()
susan.goto(371-500,25)
susan.pendown()
susan.lt(90)
flower(susan, 50, 80, "yellow")
susan.penup()
susan.goto(348-500,8)
susan.pendown()
flower(susan, 29, 80, "black")

turtle.mainloop()