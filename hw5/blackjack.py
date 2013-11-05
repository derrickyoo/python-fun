'''
Author: Derrick Yoo
Date: Oct 7, 2013
Class: ISTA 130
Section Leader: Logan Chadderdon

Description:
This program is a water downed version of Black Jack (a simple card game) for 2 
people to play
'''

import random


def ask_user(prompt, response_one, response_two):
    '''
    This function will give a user a prompt for input, check to see if that user
    typed in matches one of the two options provided by the two response types,
    and will continue until the user enters a valid response.

    prompt (string) - A string that will prompt user for input.
    response_one (string) - A possible response from the user.
    response_two (string) - Another possible response from the user.
    '''

    while True:
        user_response = input(prompt + ' ')
        if (user_response == response_one) or (user_response == response_two):
            return user_response
            break
        
def print_card(name, num):
    '''
    This function will take two parameters and will print a statment.

    name (string) - A person's name.
    num (int) - A number between 1 and 13 (inclusive)
    '''

    if (num == 1):
        print(name + ' draws an Ace')
        return 'Ace'
    elif (num == 11):
        print(name + ' draws a Jack')
        return 'Jack'
    elif (num == 12):
        print(name + ' draws a Queen')
        return 'Queen'
    elif (num == 13):
        print(name + ' draws a King')
        return 'King'
    else:
        print(name + ' draws a ' + str(num))
        return num

def get_ace_value():
    '''
    This function will get ask the user if they would like to set 1 or 11 to an
    ace using the ask_user function.
    '''

    ace_value = ask_user('Should the Ace be 1 or 11? ', '1', '11')
    return int(ace_value)

def deal_card(name):
    '''
    This function will pick a random number between 1 and 13 (inclusive), will
    print out what the user drew, and return the point-value of the card.

    name (string) - Name of the user
    '''

    card_value = random.randrange(1, 14, 1)
    card = print_card(name, card_value)

    if (card == 'Ace'):
        ace_value = get_ace_value()
        return ace_value
    else:
        return card_value

def adjust_for_bust(num):
    '''
    This function takes a single integer parameter. If number is greater than
    21, print "Bust!" and return -1. Otherwise return the number passed in.
    
    num (int) - Number that is passed in
    '''
    
    if (num > 21):
        print('Bust!')
        return -1
    else:
        return num

def hit_or_stay(hand_value):
    '''
    This function will ask user if he or she would like to hit or stay. If the 
    user types something else, repeatedly ask the user the same question until
    the user types either 'hit' or 'stay'. Returns True if user chose hit, 
    otherwise returns False

    hand_value (int) - value of a player's card hand.
    '''

    user_response = ask_user('Hit or stay? ', 'hit', 'stay')
    if user_response == 'hit':
        return True
    else:
        return False


def play_turn(name):
    '''
    This function prints out that it's the players turn, deals the player a
    card, prints out the player's total score, asks if they want to hit, if they
    do, deal another card. Does not deal cards to the player if the player
    busts. Returns the total value of all cards the player drew unless busted.
    If the player busted return -1.

    name (string) - Represents a user's name
    '''

    print('==========[ Current player: ' + name + ' ]==========')
    
    total = 0
    while True:
        card_value = deal_card(name)
        total += card_value        
        print('Total: ' + str(total))

        num = adjust_for_bust(total)
        if num == -1:
            return num
            break
        else:
            user_response = hit_or_stay(total)
            if user_response == False:
                return total
                break

def determine_winner(name1, name2, score1, score2):
    '''
    This function prints out who won or if it is a tie.

    name1 (string) - Name of player one
    name2 (string) - Name of player two
    score1 (int) - score of player one
    score2 (int) - score of payer two
    '''

    if (score1 == score2):
        print(name1 + ' and ' + name2 + ' tie!')
    elif (score1 > score2):
        print(name1 + ' wins!')
    else:
        print(name2 + ' wins!')

#==========================================================
def main():
    '''
    This function will ask each player for their name, greet them, let the first
    player play a turn, let the second player play a turn, determine who won,
    ask the users if they want to play again, and play again if yes
    '''
    player1 = input('Player 1 name: ')
    player2 = input('Player 2 name: ')
    print('Welcome to BlackJack ' + player1 + ' and ' + player2)
    print()
    print()

    response = 'yes';    
    while response == 'yes':
        player1_hand = play_turn(player1)
        print()
        player2_hand = play_turn(player2)
        print()    

        determine_winner(player1, player2, player1_hand, player2_hand)    

        response = ask_user('Would you like to play again?', 'yes', 'no')
        print()
        print()

    input('Press enter to end.')

if __name__ == '__main__':
    main()
