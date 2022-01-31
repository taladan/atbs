#! python

# mapit.py

# Automate the boring stuff chapter 12 practice
# This project demonstrates the functionality of
# the webbrowser module.  The program will do the following:
#     1. Get a street address from the command line 
#         arguments OR the system clipboard
#     2. Open the default web browser to the Google Maps page for that address
#
#     To do this, the program needs to do the following:
#     1. Read the command line arguments from sys.argv.
#     2. Read the clipboard contents.
#     3. Call the webbrowser.open() function to open the webbrowser.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)