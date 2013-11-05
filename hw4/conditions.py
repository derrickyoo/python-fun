'''
Author: Derrick Yoo
Date: Sept 30, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
This program contains multiple functions that use conditional statements.
'''

def word_length(word, num):
	'''
	The function first prints a message about the relationship between the length of the
	length of the word and the integer.
	
	word (string) - Word that will be passed in. 
	num (int) - Integer that will be passed in
	'''
	
	if len(word) > num:
	    print('Longer than ' + str(num) + ' characters:   ' + word)
	elif len(word) == num:
		print('Exactly ' + str(num) + ' characters:   ' + word)
	else:
		print('Shorter than ' + str(num) + ' characters:   ' + word)

def stop_light(color, seconds):
    '''
	This function determines the color that a stop light should change to.
	
	color (string) - Will either be 'green', 'yellow', or 'red'.
	seconds (int) - Seconds this color has been showing.
	'''
	
    if (color == 'green') and (seconds > 60):
        print('yellow')	
    elif (color == 'yellow') and (seconds > 5):
        print('red')	
    elif (color == 'red') and (seconds > 55):
        print('green')
    else:
        print(color)
		
def is_normal_blood_pressure(systolic_bp, diastolic_bp):
    '''
	The function should return True if systolic is less than 120 AND diastolic is less than
	80. Otherwise it returns False.
	
	systolic_bp (int) - Systolic blood pressure.
	diastolic_bp (int) - Diastolic blood pressure.
	'''
		
    if (systolic_bp < 120) and (diastolic_bp < 80):
        return True
    else:
        return False

def doctor():
    '''
	The function takes no parameters and prints either 'Your blood pressure is normal.' or 
	'Your blood pressure is high.' depending on the values entered.
	'''
	
    systolic_bp = int(input('Enter your systolic reading: '))
    diastolic_bp = int(input('Enter your diastolic reading: '))
	
    if (is_normal_blood_pressure(systolic_bp, diastolic_bp) == True):
        print('Your blood pressure is normal.')
    else:
        print('Your blood pressure is high.')

def pants_size(waist_size):
    '''
	The function returns a string 'small', 'medium', or 'large' depeding on the parameter value
	
	waist_size (int) - Represents a person's waist size in inches.
	'''
    
    if (waist_size >= 34):
        return 'large'
    elif (waist_size >= 30):
        return 'medium'
    else:
        return 'small'

def pants_fitter():
    '''
	This function takes no parameters and will print out the number of pairs, the size, the type,
    and the total cost.
	'''
    name = input('Enter your name:   ')
    print('Greetings ' + name + ' welcome to Pants-R-Us')
    waist_size = int(input('Enter your waist size in inches:   '))
    pairs = int(input('How many pairs of pants would you like?   '))
    type = input('Would you like regular or fancy pants?    ')
    
    if (type == 'regular'):
        total_cost = 40 * pairs
        print(str(pairs) + ' pairs of ' + str(pants_size(waist_size)) + ' regular pants:   $ ' + str(total_cost))
    elif (type == 'fancy'):
        total_cost = 100 * pairs
        print(str(pairs) + ' pairs of ' + str(pants_size(waist_size)) + ' fancy pants:   $ ' + str(total_cost))

def digdug(number):
    '''
	This function will print 'dig' if the integer is evenly divisible by 3, will print 'dug'
	if the integer is divisible by 5, and will print 'digdug' if divisible by both 3 and 5.
	Otherwise it will not print anything.
	
    number (int) - Assume number will always be a positive integer.
    '''
    all_num = range(1, number+1)
    for i in all_num:
        if (i % 3 == 0) and (i % 5 == 0):
            print(str(i) + ' :   ' + 'digdug')
        elif (i % 3 == 0) and (i % 5 != 0):
            print(str(i) + ' :   ' + 'dig')
        elif (i % 3 != 0) and (i % 5 == 0):
            print(str(i) + ' :   ' + 'dug')
        else:
            pass


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    
    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
