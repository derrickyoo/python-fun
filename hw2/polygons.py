'''
Author: Derrick Yoo
Date: Sep 16, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
A function called polygon takes 3 parameters:
The turtle object.
A numeric value giving the number of sides.
A numeric value giving the length of the sides.
'''

import turtle

#==========================================================
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
	
def main():
    '''
    The function creates a new turtle and creates polygons given the proper
    parameters when calling the polygon function.
    '''
    # Blue triangles
    snoopy = turtle.Turtle()
    snoopy.speed(0)
    snoopy.pensize(5)
    snoopy.left(180)
   
    snoopy.pencolor('blue')
    for i in range(5):
        polygon(snoopy, 3, 100)
        snoopy.penup()
        snoopy.left(90)
        snoopy.forward(20)
        snoopy.right(90)
        snoopy.pendown()
    
    # Brown triangles
    snoopy_brown = turtle.Turtle()
    snoopy_brown.speed(0)
    snoopy_brown.pensize(5)
    snoopy_brown.pencolor('brown')
    snoopy_brown.penup()
    snoopy_brown.backward(100)
    snoopy_brown.left(60)
    snoopy_brown.pendown()
    for i in range(5):
        polygon(snoopy_brown, 3, 100)
        snoopy_brown.penup()
        snoopy_brown.left(90)
        snoopy_brown.forward(20)
        snoopy_brown.right(90)
        snoopy_brown.pendown()

    # Green triangles
    snoopy_green = turtle.Turtle()
    snoopy_green.speed(0)
    snoopy_green.pensize(5)
    snoopy_green.pencolor('green')
    snoopy_green.left(60)

    for i in range(5):
        polygon(snoopy_green, 3, 100)
        snoopy_green.penup()
        snoopy_green.forward(12)
        snoopy_green.right(60)
        snoopy_green.forward(12)
        snoopy_green.left(60)
        snoopy_green.pendown()
    
        
 

    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
