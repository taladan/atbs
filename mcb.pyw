#! python
# 
# mcb.pyw  
# -- Note: the .pyw extension precludes python from opening a terminal window when this is run

# Usage:    py mcb.pyw save <keyword>   - Saves clipboard to keyword.
#           py mcb.pyw <keyword>        - Loads keyword to clipboard. 
#           py mcb.pyw list             - Loads all keywords to clipboard


# Goal:
#   Rewrite the 'multi-clipboard' from ch. 6 so that it uses the shelve module.
#   The user will now be able to save new strings to load to the clipboard
#   without having to modify the source code.  The program will save each piece
#   of clipboard text under a keyword.  For example, when you run `py mcb.pyw save spam`, 
#   the current contents of the clipboard will be saved with the keyword `spam`.
#   This text can later be loaded to the clipboard again by running `py mcb.pyw spam`.
#   If the user forgets what keywords they have, the can run `py mcb.pyw list` to copy
#   a list of all keywords to the clipboard.

# What the program Does:
#   1. The command line arg for keyword is checked.
#   2. If arg is `save`, the clipboard contents are saved to the keyword
#   3. If arg is `list`, all keywords are copied to the clipboard.
#   4. Otherwise, text for chosen keyword is copied to the clipboard


# The Code needs to do the following:
#   1. Read the command line arguments from `sys.argv`.
#   2. Read and write to the clipboard using `pyperclip`
#   3. Save and load to a shelf file using `shelve`.

# Imports
import sys, pyperclip, shelve

# Open our shelf file
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Load content
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# Clost the shelf file
mcbShelf.close()