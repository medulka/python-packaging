#!/user/bin/env python3
# pip install --upgrade pip build twine
# pip -m build

import random 
import numpy as np

def roll_dice(n_dice: int, n_sides: int):
   return [random.randint(n_sides, n_dice)]

def flip_coin():
   return random.choice(['heads', 'tails'])

