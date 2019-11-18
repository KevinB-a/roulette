import random

import math

from functions import *
"""Rules of the game """
rules()
"""starting variable"""
continue_game=True
name_choice()
money=100
print("Hello you have {} € for start the game".format(money))
while continue_game==True or money==0:

    if money==0:
        continue_game=False
        print("you have no money")

    bet=-1 #create variable and assign -1 for enter in a loop
    while bet<0 :
        try: # try to convert str in int if it fall display error message
            bet=int(input("enter your bet :"))
        except ValueError:
            print("your enter is not a number")
            bet=-1
        if bet <= 0 :
            print("your enter is a negative number or 0")
            bet=-1
        else:
            print("your enter is biger than your money ")
            bet=-1

    user_number=user_choice()
    computer_number=computer_choice()
    if user_number==computer_number:
        money=money + 2*bet
        print("you win your money is ",money)
    elif (user_number %2==0 and computer_number %2==0) or (user_number %2==1 and computer_number %2==1):
        money=money-math.ceil((bet/2))
        print("you fall on the same color your money is",money)
    else :
        money=money-bet
        print("you loose you money is ",money)
    rematch=input("Do you want to play again ? enter yes for rematch or no for quit")
    if rematch =="yes":
        continue_game=True
    else :
        continue_game=False
