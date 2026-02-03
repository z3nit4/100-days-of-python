"""
PAUSE 1 - Heads or Tails
Create a coin flip program using what you have learnt about randomisation in Python.
It should randomly print "Heads" or "Tails" everytime it is run.
"""

import random

coin_flip = random.randint(1, 2)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")

# Yesterday's lesson on if-statements was of great help completing this task

# Solution was:

import random

print(random.choice(["Heads", "Tails"]))

# LOL

