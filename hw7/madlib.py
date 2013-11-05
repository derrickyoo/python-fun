'''
Author: Derrick Yoo
Date: Oct 28, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
This program asks the user to supply each of the need words (Noun, Plural Noun,
Verb, Verb Past, Adjective) and write out the completed version of the story to
a new file. 

The program will also print a simple numerical analysis of the contents of the 
file.
'''

def print_report(filename):
    '''
    This function will print a simple analytics report of the file.

    filename (str) = name of the .txt file being read.
    ''' 

    file_in = open(filename, 'r')

    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    vowel_count = 0
    consonant_count = 0
    whitespace_count = 0
    punctuation_count = 0

    for line in file_in:
        for char in line.lower():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
            elif char.isspace():
                whitespace_count += 1
            else:
                punctuation_count += 1

    total_count = vowel_count + consonant_count + whitespace_count + punctuation_count

    file_in.close()

    percent_vowels = round(100 * (vowel_count/total_count), 1) 
    percent_consonants = round(100 * (consonant_count/total_count), 1)
    percent_spaces = round(100 * (whitespace_count/total_count), 1)
    percent_punctuation = round(100 * (punctuation_count/total_count), 1)

    title = '---------' + filename + '---------'
    title_length = len(title)
    

    # Calculations to properly output and format the numerical analytics report.

    vowel_space = title_length - len('Vowels:' + str(vowel_count))
    consonant_space = title_length - len('Consonants:' + str(consonant_count))
    whitespace_space = title_length - len('Whitespace:' + str(whitespace_count))
    punctuation_space = title_length - len('Punctuation:' + str(punctuation_count))
    total_space = title_length - len('Total:' + str(total_count))

    percent_vowels_space = title_length - len('Percent vowels:' + str(percent_vowels))
    percent_consonants_space = title_length - len('Percent consonants:' + str(percent_consonants))
    percent_spaces_space = title_length - len('Percent spaces:' + str(percent_spaces))
    percent_punctuation_space = title_length - len('Percent punctuation:' + str(percent_punctuation))

    # Prints out numerical analyitcs report.
    print(title)
    print('Vowels:' + (' ' * vowel_space) + str(vowel_count))
    print('Consonants:' + (' ' * consonant_space) + str(consonant_count))
    print('Whitespace:' + (' ' * whitespace_space) + str(whitespace_count))
    print('Punctuation:' + (' ' * punctuation_space) + str(punctuation_count))
    print('-' * title_length)
    print('Total:' + (' ' * total_space) + str(total_count) + '\n')
    print('Percent vowels:' + (' ' * percent_vowels_space) + str(percent_vowels))
    print('Percent consonants:' + (' ' * percent_consonants_space) + str(percent_consonants))
    print('Percent spaces:' + (' ' * percent_spaces_space) + str(percent_spaces))
    print('Percent punctuation:' + (' ' * percent_punctuation_space) + str(percent_punctuation))
    print('=' * title_length)

def replace_parts_of_speech(string, speech_label):
    '''
    This function takes a string containing parts of speech labels that need to
    be replaced by words and takes a string indicating which part of speech label
    to replace and returns a new string containg replaced speech labels given
    by the user inputs.

    Provides how many speech labels are in the part of speech,
    the index of all speech label instances,
    and user inputs for the each speech label instance to be replaced.

    string (str) - String containing parts of speech labels
    speech_label (str) - Speech label that to be replaced 
    '''
    
    speech_label_count = 0
    index = 0
    speech_label_indexes = []
    while index < len(string):
        index = string.find(speech_label, index)
        if index == -1: break
        speech_label_indexes.append(index)
        speech_label_count += 1
        index += len(speech_label)
    
    if speech_label_count == 0:
        return string
    else: 
        user_inputs = []
        str_list = []
        for i in range(speech_label_count):
            user_input = input('Enter ' + speech_label.lower() + ': ')
            user_inputs.append(user_input)

            str1 = string.replace(speech_label, '{0}', 1)
            string = str1.format(user_inputs[i])

        return string

def complete_mad_lib(filename):
    '''
    This function will read in a template file line by line and replace all parts
    of speech labels with words entered by the user and write the completed story
    out to a new file.

    template_file (str) - Name of the file being processed.
    '''
    new_filename = 'MAD_' + filename

    file_in = open(filename, 'r')
    file_out = open(new_filename, 'w')

    speech_label_list = ['PLURAL NOUN', 'VERB PAST', 'ADJECTIVE', 'NOUN', 'VERB']
    for line in file_in:
        for i in range(len(speech_label_list)):
            string = replace_parts_of_speech(line, speech_label_list[i])
            line = string
        file_out.write(string)
           
    file_in.close()
    file_out.close()

#==========================================================
def main():
    '''
    This function will ask the user to enter the name of the Mad-Lib template
    file. It will call the function to print the character report on that file.
    It will then call the function to have the user complete the Mad Lib story.
    '''

    user_input = input('Enter the name of a Mad-Lib template file: ')
    print_report(user_input)
    complete_mad_lib(user_input)

if __name__ == '__main__':
    main()
