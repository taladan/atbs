#! python
# zombie_dice.py
# ATBS Chapter 6 Zombie Dice Bots exercise
"""
Zombie Dice is a quick, fun dice game from Steve Jackson Games.

The players are zombies trying to eat as many human brains as
possible without getting shot three times. There is a cup of 13 dice
with brains, footsteps, and shotgun icons on their faces.  The dice 
icons are colored, and each color has a different likelihood of each 
event occurring.  Every die has two sides with footsteps, but dice with 
green icons have more sides with brains, red-icon dice have more shotguns, 
and yellow-icon dice have an even split of brains and shotguns.  Do the following on 
each player's turn:

1. Place all 13 dice in the cup. The player randomly draws three dice 
from the cup and then rolls them.  Players always roll exactly three dice.
2. They set aside and count up any brains (humans whose brains were eaten) and 
shotguns (humans who fought back).  Accumulating three shotguns automatically ends 
a player's turn with zero points (regardless of how many brains they had).  If they 
have between zero and two shotguns, they may continue rolling if they want.  
They may also choose to end their turn and collect one point per brain.
3. If the player decides to keep rolling, they must reroll all dice with 
footsteps.  Remember that the player must always roll three dice; they
must draw more dice out of the cup if they have fewer than three footsteps 
to roll. A player may keep rolling dice until either they get three shotguns
-- losing everything -- or all 13 dice have been rolled.  A player may not 
reroll only one or two dice, and may not stop mid-reroll.
4.  When someone reaches 13 brains, the rest of the players finish out the
round.  The person with the most brains wins.  If there's a tie, the tied players
play one last tiebreaker round.

For this exercise, we are using Al Sweigart's pre-written zombiedice code - it handles
all the classes and underlying game play.  The point of the exercise is to write bots
that use some sort of logic to determine playstyle, then iterate through a number of
tournaments to determine win percentages.

Specifics asked for in this exercise:
* A bot that, after the first roll, randomly decides if it will continue or stop
* A bot that stops rolling after it has rolled two brains
* A bot that stops rolling after it has rolled two shotguns
* A bot that initially decides it'll roll the dice one to four times, but will stop early if it rolls two shotguns
* A bot that stops rolling after it has rolled more shotguns than brains
"""

from random import random, choice
import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        brains = 0
        if choice([0,1]) == 0:
            diceRollResults = zombiedice.roll()


class TwoBrainZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        brains = 0
        if brains < 2:
            diceRollResults = zombiedice.roll()

class TwoShotgunZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RollOneToFourUnlessTwoShotgunsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        number_of_rolls = choice(range(0,4))
        current_roll = 0
        
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2 and current_roll < number_of_rolls:
                diceRollResults = zombiedice.roll() # roll again
                current_roll += 1
            else:
                break
class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow, 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotguns = 0
        
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns <= brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    RandomZombie(name = 'Rando Zombie'),
    TwoBrainZombie(name = 'Two Brains'),
    TwoShotgunZombie(name = '2 Shotgun Willie'),
    RollOneToFourUnlessTwoShotgunsZombie(name = '1 - 4 Rolls unless 2 shotguns Pete'),
    MoreShotgunsThanBrainsZombie(name = 'Bird Shot Bill - More Shotgun than Brains'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
