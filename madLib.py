#! python

# madLib.py

# Automate the Boring Stuff, Chapter 9: Practice
# Create a mad libs program that reads in text files
# and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

# Imports
from pathlib import Path
import os, sys, re
import pyinputplus as pyip

# Change your parent_dir to match your local file structure, and place the madlibs directory in it.
parent_dir = Path('/home/taladan/programs/mypy/atbs')
madlibs_dir = Path('madlibs')
full_path = parent_dir / madlibs_dir
madlibs_files = []

# Regex to search for CAPPED words in parenthesis including the characters ', -, 
# any digits 0-9 and preceeded by any number of _ characters and zero or more spaces.
replaceableRegex = re.compile('(_+ *\([A-Z \-\d\']*\))')

# If the madlibs directory doesn't exist, notify and gracefully exit.
if not full_path.exists():
    print("The madlibs directory cannot be found. Exiting.")
    sys.exit()
else:
    os.chdir(full_path)

# Gather current madlibs files
madlibs_files = [f for f in os.listdir(full_path) if f.endswith('mdlib')]

# If there aren't any madlibs files, notify and gracefully exit.
if len(madlibs_files) == 0:
    print("There are no current madlibs prompts available.  Exiting.")
    sys.exit()
else:           # Build a printable list of the madlibs filenames
    madlibs_filenames = [f.split('.')[0].title() for f in madlibs_files]

# Let the player choose which madlib to play
choice = pyip.inputMenu(madlibs_filenames, "Which madlib would you like to play?\n\n", numbered=True)

# Open the file and read the title and text in then close the file
with open(choice.lower() + '.mdlib', 'r') as madlib:
    madlib_title, madlib_text = madlib.readlines()

# Gather prompts from file and format for gathering user input
# TODO: Figure out why re.sub isn't working here for output.
prompts = replaceableRegex.findall(madlib_text)
for pattern in prompts:
    prompt = pattern.strip('_')
    prompt = re.sub("[\(\)]","", prompt).title()
    repl = pyip.inputStr(f"Pick a(n) {prompt}:\n")
    pattern = re.escape(pattern)
    madlib_text = re.sub(pattern, repl, madlib_text, count=1)

print(title)
print('\n\n')
print(madlib_text)
