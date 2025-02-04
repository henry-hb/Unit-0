import random


"""
Name: Henry Hall-Brown
File: rps_minus_one.py
Description: IMplements the Rock Paper Scissors Minus One Game from Squid Gmae
"""

"""
Pseudocode
Have computer pick two random "hands" of rps
SET comp_score and player_score to 0
STORE values in comp_hand somehow (you choose) probably list or two separate vars
ASK user for their hands
STORE values in player_hand
ASK user which hand to keep
computer randomly chooses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and END game
    ELSE play again
"""

def gen_comp_hand():
    choices = ["rock", "paper", "scissors"]
    hand = ["",""]
    comp_choice1 = random.choice(choices)
    comp_choice2 = random.choice(choices)
    hand[0] = comp_choice1
    hand[1] = comp_choice2
    return hand

def gen_player_hand(player_hand):
    player_hand[0] = str(input("Do you want to choose rock, paper, or scissors for your first hand? ")) 
    player_hand[1] = str(input("Do you want to choose rock, paper, or scissors for your second hand? ")) 

def comp_keep(comp_hand):
    comp_keep_choice = random.randint(0,1)
    return comp_hand[comp_keep_choice]

def winner_evaluation(comp_final, player_final):
    

def main():
    # setup
    comp_hand = ["",""]
    player_hand = ["",""]
    comp_score = 0
    player_score = 0

    #generating hands
    comp_hand = gen_comp_hand()
    gen_player_hand(player_hand)

    #print hands
    print(f"Your hand is is {player_hand[0]} and {player_hand[1]}. Your opponent's hand is {comp_hand[0]} and {comp_hand[1]}")
    player_keep = int(input("Which hand would you like to keep, 1 or 2? "))
    player_final = player_hand[player_keep]
    comp_final = comp_keep(comp_hand)

if __name__ == "__main__":
    main()