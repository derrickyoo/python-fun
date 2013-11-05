'''
Author: Derrick Yoo
Date: Sep 9, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
Part 3  of homework 1. 
'''

import turtle

#==========================================================
def shape(a_turtle, side_length):
    '''
    Takes two parameters, turtle and length, and draws a particular shape.

    a_turtle (turtle) - The turtle that's drawing
    side_length (int) - The length the turtle will draw
    '''

    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)

    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)

    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)

    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)
    a_turtle.left(150)
    a_turtle.forward(side_length)
    a_turtle.left(50)
    a_turtle.forward(side_length)

def main():
    '''
    Creates a turtle that will draw 3 shapes with speed set to 0 with varying pen and general size in 3 different locations.
    '''
    snoopy = turtle.Turtle()
    snoopy.speed(0)

    snoopy.penup()
    snoopy.backward(300)
    snoopy.right(90)
    snoopy.forward(50)
    snoopy.pendown()

    shape(snoopy, 50)

    snoopy.pencolor('red')
    snoopy.pensize(10)
    snoopy.penup()
    snoopy.goto(50, 300)
    snoopy.pendown()

    shape(snoopy, 100)

    snoopy.pencolor('green')
    snoopy.pensize(20)
    snoopy.penup()
    snoopy.goto(-100, -200)
    snoopy.pendown()

    shape(snoopy, 30)


    input('Press enter to end.')  # this is only needed if you're using turtle graphics

if __name__ == '__main__':
    main()
