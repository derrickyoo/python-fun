'''
Author: Derrick Yoo
Date: Sep 26, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
This will ask a user how many polygons to draw including: How many sides the 
polygon should have, what color to use, length of a side of the polygon, and 
will output each polygon specified by the user input.
'''

import turtle


def polygon(a_turtle, num_side, side_length):
    '''
    The function draws a regular ploygon with the given number of sides, each
    side of the given length.

    a_turtle (turtle) - The turtle that is drawing.
    num_side (int) - Number of sides of the polygon.
    side_lenth (int) - Length of each side of the the polygon.
    '''
    
    for i in range(num_side):
        a_turtle.forward(side_length)
        a_turtle.left(360/num_side)

#==========================================================	
def main():
    '''
    The function creates a new turtle and creates polygons given the proper
    parameters input by user and calling the polygon function.
    '''

    mertle = turtle.Turtle()
    mertle.speed(0)
    mertle.pensize(10)

    num_polygons = input('Enter the number of polygons you\'d like to see:   ')
    num_polygons = int(num_polygons)

    for i in range(num_polygons):
        num_side = input('Enter the number of sides:   ')
        num_side = int(num_side)

        color = input('Enter the color:   ')

        side_length = input('Enter the side length for your polygon:   ')
        side_length = int(side_length)

        print()

        mertle.pencolor(color)
        polygon(mertle, num_side, side_length)

    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
