'''
Author: Derrick Yoo
Date: Sep 9, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
Part 2  of homework 1. 
'''

import turtle

#==========================================================
def triangle(a_turtle, side_length):
    '''
    Takes two parameters, turtle and length, and draws an equilateral triangle.

    a_turtle (turtle) - The turtle that's drawing
    side_length (int) - The length the turtle will draw
    '''
    a_turtle.forward(side_length)
    a_turtle.left(120)
    a_turtle.forward(side_length)
    a_turtle.left(120)
    a_turtle.forward(side_length)

def square(a_turtle, side_length):
    '''
    Takes two parameters, turtle and length, and draws a square.

    a_turtle (turtle) - The turtle that's drawing
    side_length (int) - The length the turtle will draw
    '''
    a_turtle.forward(side_length)
    a_turtle.left(90)
    a_turtle.forward(side_length)
    a_turtle.left(90)
    a_turtle.forward(side_length)
    a_turtle.left(90)
    a_turtle.forward(side_length)

def pentagon(a_turtle, side_length):
    '''
    Takes two parameters, turtle and length, and draws a pentagon.

    a_turtle (turtle) - The turtle that's drawing
    side_length (int) - The length the turtle will draw
    '''
    a_turtle.forward(side_length)
    a_turtle.left(72)
    a_turtle.forward(side_length)
    a_turtle.left(72)
    a_turtle.forward(side_length)
    a_turtle.left(72)
    a_turtle.forward(side_length)
    a_turtle.left(72)
    a_turtle.forward(side_length)

def hexagon(a_turtle, side_length):
    '''
    Takes two parameters, turtle and length, and draws a hexagon.

    a_turtle (turtle) - The turtle that's drawing
    side_length (int) - The length the turtle will draw
    '''
    a_turtle.forward(side_length)
    a_turtle.left(60)
    a_turtle.forward(side_length)
    a_turtle.left(60)
    a_turtle.forward(side_length)
    a_turtle.left(60)
    a_turtle.forward(side_length)
    a_turtle.left(60)
    a_turtle.forward(side_length)
    a_turtle.left(60)
    a_turtle.forward(side_length)


def main():
    '''
    Creates a new turtle with speed set to 0 and pensize to 10 and draws a figure shown in part 2 of homework 1.
    '''
    snoopy = turtle.Turtle()
    snoopy.pensize(10)
    snoopy.speed(0)

    square(snoopy, 200)

    snoopy.right(90)
    snoopy.penup()
    snoopy.forward(20)
    snoopy.right(90)
    snoopy.backward(50)

    snoopy.pendown()
    snoopy.right(45)
    square(snoopy, 50)

    snoopy.penup()
    snoopy.home()

    snoopy.penup()
    snoopy.forward(175)
    snoopy.right(180)

    snoopy.pendown()
    snoopy.pencolor('red')
    triangle(snoopy, 150)
    snoopy.penup()

    snoopy.home()

    snoopy.right(180)    
    snoopy.backward(150)
    snoopy.pendown()
    snoopy.pencolor('orange')
    triangle(snoopy, 100)

    snoopy.penup()
    snoopy.home()
    snoopy.forward(200)

    snoopy.pencolor('black')


    snoopy.right(90)
    snoopy.penup()
    snoopy.forward(20)
    snoopy.right(90)
    snoopy.backward(50)

    snoopy.pendown()
    snoopy.right(45)
    square(snoopy, 50)

    snoopy.penup()
    snoopy.home()

    snoopy.left(90)
    snoopy.forward(200)
    snoopy.right(90)
    snoopy.forward(25)

    snoopy.pendown()
    snoopy.pencolor('green')
    hexagon(snoopy, 150)
    snoopy.left(60)

    snoopy.penup()
    snoopy.forward(25)

    snoopy.pendown()
    snoopy.pencolor('blue')
    pentagon(snoopy, 100)
    snoopy.penup()

    snoopy.left(72)
    snoopy.forward(150)
    snoopy.right(180)
    snoopy.forward(25)

    snoopy.pendown()
    snoopy.color('magenta')
    triangle(snoopy, 50)

    snoopy.left(120)
    snoopy.forward(50)
    triangle(snoopy, 50)

    snoopy.left(120)
    snoopy.forward(50)
    triangle(snoopy, 50)








    input('Press enter to end.')  # this is only needed if you're using turtle graphics

if __name__ == '__main__':
    main()
