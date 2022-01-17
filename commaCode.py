#!/usr/bin/python3
# Automate the Boring Stuff with Python
# Chapter 4 Practice Project
# Comma Code
# Write a function that takes a list value as an argument
# and returns a string with all the items separated by a comma
# and a space, with and insterted before the last item.
# For example, passing the list `spam = ['applies', 'bananas', 'tofu', 'cats']`
# returns 'apples, bananas, tofu, and cats'.  The function
# should be able to work with any list value passed to it.
# Also test the case where an empty list [] is passed to the function


def commaCode(myList):
    accumulate = ""
    if myList == []: # Empty list test
        return "The list is empty."
    if len(myList)==1: # Single item list test
        return myList[0]
    for i in range(len(myList)):
        if myList[i] == myList[0]: # Nothing is prepended to the first index accumulated
            accumulate = myList[i]
        elif myList[i] == myList[-1]: # If the current i is the last index in myList, add ', and' before concatenating the last index to the string
            accumulate = accumulate + ', and ' + myList[i]
        else:
            accumulate = accumulate + ', ' + myList[i] # add a comma and a space to indexes that aren't 0 or -1
    return accumulate # Return the accumulated string