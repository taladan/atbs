#! python
# regex_strip.py
# Automate the Boring Stuff Chapter 7 Exercise
# Create a function that takes a string and performs
# the same functionality as the strip() string method.
# If no other arguments are passed other than the string
# to strip, then whitespace characters will be removed from
# the beginning and end of the string.  Otherwise, the characters
# specified in the second argument to the function will be removed
# from the string.

# Module imports
import re


def regex_strip(text: str, remove: str='\s') -> str:
    '''
    After trying for a while to figure out how to embed a variable in a regex, I found
    https://github.com/zspatter/automate-the-boring-stuff/blob/master/regex_strip/regex_strip.py

    Yeah, I cheated, but I refined my cheat to simplify the initial find.  Turns
    out F-Strings works within regex.
    '''
    return re.compile(f'^({remove})*|({remove})*$').sub('', text)

if __name__ == '__main__':

    print(regex_strip('  ffffff  '))
    print(regex_strip('FOOBARbazFOOBAR','FOOBAR'))  