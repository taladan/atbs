#!/usr/bin/python3
# Automate the Boring Stuff with Python
# Chapter 4 exercise: CoinFlips
# Write a program to find out how often a streak of six heads or a streak of six tails 
# comes up in a randomly generated list of heads and tails. 
# Your program breaks up the experiment into two parts: the first part generates 
# a list of randomly selected 'heads' and 'tails' values, and the second part checks 
# if there is a streak in it. Put all of this code in a loop that repeats the 
# experiment 10,000 times so we can find out what percentage of the coin flips contains 
# a streak of six heads or tails in a row. 
# 
# Expanding upon this exercise, I decided to track all streaks from a streak of 2 to a streak of 6
# 
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% 
# of the time and a 1 value the other 50% of the time.
import random

# Beyond the initial scope of the ATBS example, let's track all streaks from a streak of 2 -> a streak of 6
numberOf6Streaks = 0 # Track a streak length of 6
numberOf5Streaks = 0 # Track a streak length of 5
numberOf4Streaks = 0 # Track a streak length of 4
numberOf3Streaks = 0 # Track a streak length of 3
numberOf2Streaks = 0 # Track a streak length of 2
tests = 10000 # How many tests should we perform?

for experimentNumber in range(tests):
    fliplist = [] # Initialize the current test's list of flips
    streak = 0 # Set number of streaks to 0
    for _ in range(100): # flip a coin
        fliplist.append(random.choice(["h","t"]))
    
    for i in range(len(fliplist)):
        if i == 0: # We don't compare the first item of the list
            pass
        elif fliplist[i] == fliplist[i-1]: # if the current item of the list is the same as the previous item, add 1 to the streak counter
            streak += 1
        else: # if the current item isn't equal to the previous item, reset the streak counter to 0
            streak = 0
        if streak == 6: # When the streak counter hits 6, increase the number of 6 streaks by 1.
            numberOf6Streaks += 1 
        elif streak == 5:# When the streak counter hits 5, increase the number of 5 streaks by 1.
            numberOf4Streaks += 1
        elif streak == 4:# When the streak counter hits 4, increase the number of 4 streaks by 1.
            numberOf5Streaks += 1
        elif streak == 3:# When the streak counter hits 3, increase the number of 3 streaks by 1.
            numberOf3Streaks += 1
        elif streak == 2:# When the streak counter hits 2, increase the number of 2 streaks by 1.
            numberOf2Streaks += 1

# In the ATBS example, the output was just divided by 100, but this doesn't actually signify a percentage for the number of 
# tests that are performed, as it only takes the entire streak set and pulls a percentage calculation for the full set.  One
# commentor suggests that the data should be divided by 100 * the total # of tests performed. I'm not sure of the math on this
# as it seems that when I follow the 2 flip streak, it seems to be a fairly low percentage rate.  Though this code performs as
# expected according to the instructions in ATBS, practically I wouldn't stake any actual research on this without some deeper 
# research. -- DJC

print("Raw Output:") # Output requested by ATBS exercise.
print("6 flip Streak: %s"%(numberOf6Streaks/100))
print("5 flip Streak: %s"%(numberOf5Streaks/100))
print("4 flip Streak: %s"%(numberOf4Streaks/100))
print("3 flip Streak: %s"%(numberOf3Streaks/100))
print("2 flip Streak: %s"%(numberOf2Streaks/100))

# Output suggested by a commenter that for an actual percentage, one has to calculate the number of tests performed in the experiment.
# Formatting of outputted number is rounded to 3 decimal places.
print('Chance of a 6 flip streak: {:.3f} %'.format(numberOf6Streaks / (100 * tests))) # We want a percentage of streaks, not the number of streaks themself
print('Chance of a 5 flip streak: {:.3f} %'.format(numberOf5Streaks / (100 * tests))) # We want a percentage of streaks, not the number of streaks themself
print('Chance of a 4 flip streak: {:.3f} %'.format(numberOf4Streaks / (100 * tests))) # We want a percentage of streaks, not the number of streaks themself
print('Chance of a 3 flip streak: {:.3f} %'.format(numberOf3Streaks / (100 * tests))) # We want a percentage of streaks, not the number of streaks themself
print('Chance of a 2 flip streak: {:.3f} %'.format(numberOf2Streaks / (100 * tests))) # We want a percentage of streaks, not the number of streaks themself