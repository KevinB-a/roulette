import random

import math

def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    username=""
    while username =="": #if value of user is empty the loop continue
        user=input("please enter your name or pseudo")
        return username
    print("welcome on casino game ",username," !")
#def user_choice():
    """the function allow the player to choose a number between 0 and 49 ,
    if enter his not a number or enter his str return to choice"""
#    number_choice=50 #for enter in a loop
#    while number_choice < 0 or number_choice > 49:
#        try:
#            number_choice=int(input("enter number between 0 and 49 :")) #ask user a number and convert it in integer
#        except ValueError: # if number_choice not a number
#            print("your enter is not a number") #display error message
#            number_choice = 50 #return in a loop
#        if number_choice < 0 or number_choice >49:
#            print("your enter is not included in range") #display error message  if number is out of range
#        return number_choice

#def computer_choice():
#    """this function makes it possible to randomly select values """
#    random_number= random.randrange(50) # choose a random number between 0 and 49
#    return random_number

#def user_bet():
#    bet=-1
#    while bet<0 :
#        try:
#            bet=int(input("enter your bet"))
#        except ValueError:
#            print("your enter is not a number")
#    return bet
