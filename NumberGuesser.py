"""
Number Guess
"""

from random import randint
from time import sleep

sides_input = int(input("How many sides should the dice have? "))

def get_guess():
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(sides):
  roll_1 = randint(1, sides)
  roll_2 = randint(1, sides)
  max_val = sides * 2
  print("The maximum possible value is " + str(max_val))
  guess = get_guess()
  if guess > max_val:
    print("You cannot guess higher than the maximum value!")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is " + str(roll_1))
    sleep(1)
    print("The second roll is " + str(roll_2))
    sleep(1)
    total_roll = roll_1 + roll_2
    print("The total roll is " + str(total_roll))
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You win!")
    else:
      print("You lost...")

roll_dice(sides_input)