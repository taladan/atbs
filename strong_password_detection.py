#! python
# strong_password_detection.py
# Automate the Boring Stuff Chapter 7 Exercise
# The purpose of this module is to create a regex
# that validates whether a password meets a set of
# requirements such that the password contains at least
# one uppercase character, one lowercase character, one
# digit and is no less than 8 characters in length

# Module imports
import re

# Regex pattern

passwordRegex = re.compile(r'''
    (^                  # Line start anchor
    (?=.*[A-Z])         # Uppercase capture group - At least one or more UC characters
    (?=.*[a-z])         # Lowercase capture group - At least one or more LC characters
    (?=.*\d)            # Digit capture group - At least one or more Digit characters
    [A-Za-z\d]          # Match any string containing any uppercase, lowercase or digit characters
    {8,}                # Quantify to 8 or more charatcers
    $)''', re.VERBOSE)  # Line end anchor, and re.VERBOSE for readability

def is_strong_password(text: str) -> bool:
    try:
        return not passwordRegex.search(text) == None # If the password is None, return False, else True
    except AttributeError as e:
        print(e)
        return False


if __name__ == '__main__':
    pwds = ('foo', 
        'foobar', 
        'FooBar', 
        'FooBarBaz', 
        'FooBarBaz3', 
        'FOOBARBAZ3', 
        'foobarbaz3', 
        'BOOfarBAZ3')

    print("""
    Testing password strength.  Password must meet the following requirements:
    1.  Password must be at least 8 characters in length.
    2.  Password must contain at least 1 uppercase character.
    3.  Password must contain at least 1 lowercase character.
    4.  Password must contain at least 1 digit.
    """)
    for pwd in pwds:
        print(f"Testing {pwd=}. Results: {is_strong_password(pwd)}")

    print("Done")