""" 
This program will roll a pair of dice, then add the values of the roll.  Then the user will be asked to guess a number.  If the user guessed the correct number, they win. 
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Take a guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print (f"The maximum possible value is: {max_val}")
  guess = get_user_guess()
  if guess > max_val:
    print ("This guess is invalid, it's above the maximum value.")
  else:
    print ("Rolling...")
    sleep(2)
    print (f"The first roll is {first_roll}")
    sleep(1)
    print (f"The second roll is {second_roll}")
    sleep(1)
    total_roll = first_roll + second_roll
    print (f"The combined total is {total_roll}")
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("That's correct. You won!!")
    else:
      print ("I'm sorry, that's not right. You lost :(")


roll_dice(6)