#!/usr/bin/python3
# Simple implementation of conway's game of life from automate the boring stuff


import random, time, copy

from clearScreen import clear
WIDTH = 0
HEIGHT = 0
steps = 0
stepCheck = 0
previousCells = [0,0,0]
nextCells = [] # Needed for storing the cells of the board
run = 1
runs = []

# def clear():
#     # Windows
#     if name == 'nt':
#         _ = system('cls')
#     # Mac/*Nix
#     else:
#         _ = system('clear')

def defineParameters():
    while True:
        try:
            print("What size gameboard do you wish to play?")
            print("Input X (Width): ", end='')
            WIDTH = input()
            print("Input total Y (Height): ", end='')
            HEIGHT = input()
            if int(WIDTH) and int(HEIGHT):
                return (int(WIDTH), int(HEIGHT))
                break
        except ValueError:
            print("Invalid input.  Gameboard size must be entered as integers.")

# Create a list of lists for the cells:
def generateSeed():
    '''
    Creates a playing board initial state with random 'live' and 'dead' cells
    '''
    nextCells = [] # Clear the board
    currentCells = []
    for x in range(WIDTH):
        column = [] # Create a new column.
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#') # Add a living cell.
            else:
                column.append(' ') # Add a dead cell.
        nextCells.append(column) #nextCells is a list of column lists.
    return nextCells

def storeState(cells, step):
    previousCells[step-1] = cells


WIDTH, HEIGHT = defineParameters()
nextCells = generateSeed() # Create initial board setup

while True: # Main program loop.
    clear() # Clear the previous step from the screen
    if stepCheck == 3:
        stepCheck = 1
    else:
        stepCheck +=1
    storeState(copy.deepcopy(nextCells), stepCheck)
    currentCells = copy.deepcopy(nextCells)
    statecheck = copy.deepcopy(nextCells)
    print("Total runs of Conway's Game of Life: %s" % run)
    print("Current step: %s" % (steps))
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead:
                nextCells[x][y] = ' '
    if nextCells == previousCells[-2]: # Stability check - is the board flipping statically with no possibility of change in upcoming iterations?
        print("Stability reached in %s steps. Exiting simulation." % (steps))
        print("Continue with reseed? (y/n) ", end='')
        choice = input()
        while not choice.lower() in ['y', 'n']: # Ensure player chooses yes or no
            print("Invalid choice, please select 'y' or 'n'.")
            choice = input()

        if choice.lower() == "y": 
            print("Do you wish to change the board size?(y/n) ", end='')
            keepBoardParameters = input()
            while not keepBoardParameters.lower() in ['y', 'n']: 
                print("Invalid Choice, please select 'y' or 'n'.")
                keepBoardParameters = input()
            runs.append(steps)
            steps = 0 # Reset the step counter to 0
            nextCells = generateSeed() # Reinitialize the board
            run += 1

        elif choice.lower() == "n":
            print("Discontinuing simulation.")
            print("Total number of runs: %s" % run)
            print("Run statistics:")
            for i in range(len(runs)):
                print("{:10}| {:10}".format("Run Number", "# of Steps"))
                print("{:10d}| {:10d}".format(i, runs[i]))

            break
        if keepBoardParameters.lower() == "y":
            WIDTH, HEIGHT = defineParameters()
            nextCells = generateSeed()
    steps += 1
    time.sleep(.05)
