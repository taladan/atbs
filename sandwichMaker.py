#! python

# sandwichMaker.py

# Automate the Boring Stuff: Chapter 8 Practice Projects
#
# Write a program that asks users for their sandwich preferences. 
# The program should use PyInputPlus to ensure that they enter valid
# input such as:
#     * Using inputMenu() for a bread type: wheat, white, or sourdough.
#     * Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
#     * Using inputYesNo() to ask if they want cheese.
#     * If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
#     * Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
#     * Using inputInt() to ask how many sandwices they want.  Make sure this number is 1 or more.
#
# Come up with prices for each of these options, and have your program display
# a total cost after the user enters their selection.

# Imports
import pyinputplus as pyip

# CONSTANTS
BREADS = ['white', 'whole wheat', '9 grain', 'flatbread (white)', 'flatbread (wheat)', 'honey wheat']
BREAD_COSTS = [.44, .60, .90, .30, .35, .64]
PROTEINS = ['chicken', 'turkey', 'ham', 'roast beef', 'fish', 'tofu']
PROTEIN_COSTS = [1.50, 1.00, 1.75, 2.00, 1.00, .75]
CHEESES = ['mild cheddar', 'sharp cheddar', 'swiss', 'mozzarella', 'provalone']
CHEESE_COSTS = [.50, .55, .75, .75, .75]
ADDITIONS = {'mayo': .10, 'mustard': .10, 'lettuce': .5, 'tomato':.25}

def sandwich_maker():
    # start the order
    print("Thank you for ordering a PythonSandwich!  Let's get your order started:\n")
    num_of_sandwiches = pyip.inputNum(prompt="How many sandwiches would you like to order today? ", min=1)
    sandwiches = {}
    total_cost = 0
    for sandwich in range(num_of_sandwiches):
        current_sandwich, cost=build_sandwich()
        sandwiches[current_sandwich] = cost
        total_cost += float(cost)
    return (sandwiches, total_cost)

def build_sandwich():

    # Set up some useful variables
    sandwich_type = ""
    total_cost = 0

    # pick your bread, add it to the cost, update the type of sandwich
    bread = pyip.inputMenu(BREADS, prompt="Please select the type of bread:\n", numbered=True)
    total_cost += BREAD_COSTS[BREADS.index(bread)]
    sandwich_type += f"on {bread}"

    # pick your protein, add it to the cost, update the type of sandwich
    protein = pyip.inputMenu(PROTEINS, prompt=f"Great! {bread.title()} is your bread type.  Please choose a protein:\n", numbered=True)
    total_cost += PROTEIN_COSTS[PROTEINS.index(protein)]
    sandwich_type = protein + ' ' + sandwich_type

    # You want cheese with that?
    wants_cheese = pyip.inputYesNo(prompt=f"Great, that's a {sandwich_type}.  Did you want cheese with that?\n")
    if wants_cheese == 'yes':
        cheese = pyip.inputMenu(CHEESES, prompt="Excellent choice, which type of cheese do you prefer?\n", numbered=True)
        total_cost += CHEESE_COSTS[CHEESES.index(cheese)]
        sandwich_type += f" with {cheese}"
    else: 
        print("Got it, no cheese!")
    
    for addon,cost in ADDITIONS.items():
        response = pyip.inputYesNo(f"Did you want to add {addon} to that? ")
        if response == 'yes':
            total_cost += cost
            sandwich_type = sandwich_type + f' add {addon}'
        else:
            sandwich_type = sandwich_type + f' hold the {addon}'

    return (sandwich_type.capitalize(),'%.2f'%total_cost)


if __name__ == '__main__':
    # sandwiches, cost= sandwich_maker()
    order = sandwich_maker()
    sandwiches = order[0]
    cost = order[1]
    print("Great!  Here's your order:\n")
    max_sandwich_column_width = max(len(x) for x in sandwiches) + 2
    max_cost_column_width = 10
    print_width = max_sandwich_column_width + max_cost_column_width + 1
    print('-' * print_width)
    print("Sandwich Type:".ljust(max_sandwich_column_width)+'|', end='')
    print("Cost:".rjust(max_cost_column_width))
    for k,v in sandwiches.items():
        print(k.ljust(max_sandwich_column_width) + '|' + v.rjust(max_cost_column_width) + '|')
    print()
    print('-' * print_width)
    print(f"Your order comes to: {cost}")
