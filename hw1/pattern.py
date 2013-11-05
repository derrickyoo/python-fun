'''
Author: Derrick Yoo
Date: Sep 9, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
Part 1 of homework 1. A turtle object will be created to draw a figure defpicted in part 1 of homework 1 utilizing the notched_line fuction
'''

import turtle

#==========================================================
def notched_line(a_turtle):
    '''
    Takes a single parameter, turtle, and draws a notched line
    a_turtle (turtle) - The turtle that's drawing
    '''    
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(100)

def main():
    '''
    Creates a new turtle with speed set to 0 and pensize to 10 and draws multiple notched lines as shown in part 1 of homework 1
    '''
    snoopy = turtle.Turtle()
    snoopy.speed(0)
    snoopy.pensize(10)

    notched_line(snoopy)
    snoopy.left(120)
    notched_line(snoopy)
    snoopy.left(120)
    notched_line(snoopy)
    snoopy.left(30)
    notched_line(snoopy)
    snoopy.left(90)
    notched_line(snoopy)
    snoopy.left(30)
    notched_line(snoopy)
    snoopy.left(120)
    notched_line(snoopy)

    input('Press enter to end.')  # this is only needed if you're using turtle graphics

if __name__ == '__main__':
    main()
