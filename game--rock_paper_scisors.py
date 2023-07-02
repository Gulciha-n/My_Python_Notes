#Import the random library
import random
#Please create a list containing the three actions of the game.
actions = ["rock","paper","scissors"]
#Select a random action for each player
action_player1 = random.choice(actions)
action_player2 = random.choice(actions)
action_player3 = random.choice(actions)
#Use the print function to print the players choices
#print (action_player1,action_player2,action_player3)

#1 - Tie Condition
#Please write an if statement to check if the players chose the same action

if action_player1 == action_player2 and action_player1==action_player3:
    print("The players cohese same action.")

    