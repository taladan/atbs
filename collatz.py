#!/usr/bin/python3
# Implement the Collatz Sequence - also known as 'The Simplest impossible math problem'
#   If the integer given is equal, floor divide by 2, 
#   if it's odd, multiply by three and add 1
#   Run the new result through the collatz sequence until you recieve the integer '1' 
#   as output.

# Get input
try:
    print("Enter an integer: ", end = '')
    choice = int(input()) # Make sure the input is an integer
except ValueError:
    print("Invalid input, please input an integer.")

# Collatz calculation, prints and returns results
def collatz(number):
    if number % 2==0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

# Seed our loop with the result of the initial choice
output = collatz(choice)
while True:
    if output == 1:
        break
    else:
        output = collatz(output) # Set the new output as the collatz of the previous output



