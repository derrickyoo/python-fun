'''
Author: Derrick Yoo
Date: Sep 16, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
The turtle object draws a rotated shape.
'''

import turtle

def shape(a_turtle, size):
    '''
    This function draws a shape of my choice.

    a_turtle (turtle) - The turtle that is drawing
    size (int) - Size of each side of the shape I am drawing
    '''
    for i in range(6):
        a_turtle.forward(size)
        a_turtle.left(50)
        a_turtle.forward(size)
        a_turtle.left(50)
        a_turtle.forward(size)
        a_turtle.left(150)
        a_turtle.forward(size)
        a_turtle.left(50)

def rotated_shapes(a_turtle, size, num, angle):
    '''
    Draws a set number of shapes rotated at a set angle and size.

    a_turtle (turtle) - The turtle that is drawing
    size (int) - Size of each side
    num (int) - Number of shapes to draw
    angle (int) - Angle between shapes
    '''
    
    for i in range(num):
        shape(a_turtle, size)
        a_turtle.left(angle)

def move(a_turtle, distance, color):
    '''
    This function moves the turle a set distance and changes the color.

    a_turtle (turtle) - The turtle the draws something
    distance (int) - Distance to move the turtle
    color (string) - Color of the turtle
    '''
    a_turtle.penup()
    a_turtle.backward(distance)
    a_turtle.pencolor(color)
    a_turtle.pendown()
    
def main():
    '''
    Draws rotated shapes in at least three different locations in three
    different colors
    '''
    yertle = turtle.Turtle()
    yertle.speed(0)
    yertle.penup()
    yertle.backward(100)
    yertle.left(90)
    yertle.forward(300)
    yertle.right(90)
    yertle.pendown()
    yertle.pencolor('dark slate grey')
    yertle.pensize(5)
    
    # Test for creating a shape
    #shape(yertle, 100)

    rotated_shapes(yertle, 50, 5, 5)
    move(yertle, 300, 'red')
    rotated_shapes(yertle, 20, 3, 60)

    yertle.penup()
    yertle.left(90)
    yertle.forward(300)
    yertle.pendown()

    move(yertle, 50, 'blue')
    rotated_shapes(yertle, 60, 4, 80)
    
    input('Enter to end')

if __name__ == '__main__':
    main()
