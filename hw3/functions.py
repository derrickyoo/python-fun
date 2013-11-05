'''
Author: Derrick
Date: Sep 23, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
This program contains multiple functions that do basic calcuations, conversions,
and other fun mathematical operations using loops. 
'''

import math

def print_word(num, string):
    '''
    The function will print a given string the given number of times each time
    preced by a count.

    num (int) - Non-negative number
    string (string) - String that will be repeated
    '''

    for i in range(num):
        print(str(i+1) + ' --> ' + string)   

def bacteria(num_min, num_gen):
    '''
    The function will print out information showing the number of bacteria in a
    Petri dish at equal time intervals

    num_min (int) - Number of minutes it take for the bacterium to split into
                    two new bacteria.
    num_gen (int) - Number of bacterial generations to include in the ouput.
    '''
    count = 2
    for i in range(num_gen):
        interval = (i + 1) * num_min
        print('after ' + str(interval) + ' minutes: ' +
        str(count) + ' bacteria')
        count *=2

def convert_to_copper(num_gold, num_silver, num_copper):
    '''
    The function will print the number of each type of coin followed by the
    total value of all the coins when converted to copper.

    num_gold (int) - Number of gold coins.
    num_silver (int) - Number of silver coins.
    num_copper (int) - Number of copper coins.
    '''

    silver_to_copper = num_silver * 10
    gold_to_copper = num_gold * 20 * 10

    total_copper = num_copper +  silver_to_copper + gold_to_copper

    print(str(num_gold) + ' gp, ' + str(num_silver) + ' sp, ' + str(num_copper) + 
        ' cp converted to copper is:   ' + str(total_copper) + ' cp')

def convert_from_copper(num_copper):
    '''
    The function will print ou the number of gold pieces (gp), silver pieces(sp)
    and copper pieces (cp) you would end up with if you first converted as many
    initial copper pieces to goad as possible and then coverted as many of the 
    remaining copper pieces as possible to silver pieces.

    num_copper (int) - Number of cooper coins
    '''

    num_gold = int(num_copper/200)
    num_silver = int((num_copper - (num_gold * 200))/10)
    num_remain = int(num_copper - (num_gold * 200) - (num_silver * 10))

    print (str(num_copper) + ' copper pieces is:   ' + str(num_gold) + ' gp, ' + 
        str(num_silver) + ' sp, ' +  str(num_remain) + ' cp')

def repeat_word(word, num_rows, num_col):
    '''
    This function will repeat a word a number of columns and rows.

    word (string) - Word that will be repeated.
    num_rows (int) - Number of rows.
    num_col (int) - Number of columns.
    '''

    for i in range(num_rows):
        print(word * num_col)

def text_triangle(num):
    '''
    This function will take an integer parameter and print X's in a triangle 
    shape.

    num (int) = integer parameter
    '''

    for i in range(num):
        print(' ' * (num-i) + ('X' * (i+1)))

def surface_area_of_cylinder(radius, height):
    '''
    This function will calculate and prints the surface area of the cylinder 
    with the given radius and height.

    radius (float) - Radius of the cylinder
    height (float) - Height of the cylinder
    '''
    pi = math.pi
    area = pi * pow(radius,2)
    circum = 2* pi * radius

    surface_area = (2 * area) + (circum * height)

    print('The surface area of a cylinder with radius ' + str(int(radius)) +
        ' and height ' + str(int(height)) + ' is ' + str(surface_area))

def tree_height(dist_to_tree, len_str):
    '''
    This function will calculate the height of the tree using the Pythagorean
    Theorem given two lengths.

    dist_to_tree (float) - Distance from you to the tree
    len_str (float) - Length of kite string
    '''

    tree_height = math.sqrt(pow(len_str,2) - pow(dist_to_tree,2))

    print('Kite string:   ' + str(len_str) + '\n' + 'Distance:   ' + 
        str(dist_to_tree) + '\n' + 'Height:   ' + str(tree_height))

#==========================================================
def main():
    '''
    This function will be used to test all functions.
    '''

    # print_word(5, 'mississippi')
    # bacteria(10, 5)
    # convert_to_copper(5, 10, 7)
    # convert_from_copper(3242)
    # repeat_word('Kobold', 5, 3)
    # text_triangle(3)
    # surface_area_of_cylinder(0.0, 10.0)
    # tree_height(100, 141.421356)

if __name__ == '__main__':
    main()
