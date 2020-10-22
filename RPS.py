# print "Hello world!"
"""
The user will pick rock, paper, or scissors, then computer will randomly pick one, and then tell the user who won.
"""

from random import randint
from time import sleep

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "Yawn it's a tie!",
"won": "Yay you won!",
"lost" : "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print ("You picked %s") % user_choice
  sleep(2)
  print ("The computer picked %s") % computer_choice
  sleep(1)
  if user_choice == computer_choice:
    print (message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print (message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print (message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print (message["won"])
  else:
    print (message["lost"])

def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()