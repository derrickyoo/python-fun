'''
Author: Derrick Yoo
Date: Oct 2, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

HOMEWORK 3 -- Initial code for Homework 3, Part II.

ADD YOUR LIST OF BUG FIXES HERE:
1.) line 50 syntax error: missing ':'
2.) line 83 intendation error
3.) line 74 import turtle
4.) line 84 type casting 'm' to int
5.) line 23 spelling error 'someTurtle'

ADD YOUR LIST OF IMPROVEMENTS HERE:
1.) Used a for loop for each plus function
2.) renamed parameter for plus3 function
3.) created function that initates turtle speed, location, and pensize
4.) Replaced all plus function into one function

Description:
Makes some pluses picture
'''

import turtle

def initialize(a_turtle):
    '''
    The function will initialize the turtle speed, location and pensize.

    a_turtle (turtle) - Turtle that will be doing the drawing.
    '''

    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.backward(300)
    a_turtle.pendown()

    m = input('What pen size would you like? ')
    
    if (int(m) > 30):
        a_turtle.pensize(30)
    else:
        a_turtle.pensize(int(m))


def plus(a_turtle):
    '''
    The function will create a series of pluses.

    a_turtle (turtle) - Turtle that will be doing the drawing
    '''

    new_range = range(1,4)
    for i in new_range:
        for x in range(4):
            a_turtle.forward(50*i)
            a_turtle.backward(50*i)
            a_turtle.left(90)

        if i < 3:
            a_turtle.forward(150*i)

#===================================================================
def main():
    '''
    Make some pluses in a row
    '''
    yertle = turtle.Turtle()

    initialize(yertle)

    plus(yertle)

    input('Enter to end')

if __name__ == '__main__':
    main()
