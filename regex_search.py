#! python
#
# regex_search.py
# Usage:
# regex_search.py /path/to/textfiles/ expression
#
#   If the user includes a path to search, we search that path, otherwise
#   we search the current working directory.  This only searches files
#   that end in .txt
#
# Automate the boring stuff with python, chapter 9 exercise:
# 
# Write a program that opens all .txt files in a folder
# and searches for any line that matches a user-supplied
# regular expression.  The results should be printed
# to the screen.

# Imports
import os
import re
import sys

try:
    from pathlib import Path
except ImportError:
    print('''This program requires pathlib to be installed:
                'pip install pathlib'
                ''')

try:
    import magic
except ImportError:
    print('''This program requires Python-magic to be installed:
                'pip install Python-magic'
                ''')

previous_directory = Path.cwd()                                     # Starting directory
mime = magic.Magic(mime=True)                                       # We will determine filetype with PythonMagic

# Handle cli arguments
numArgs = len(sys.argv)
enoughArgs = numArgs >= 2
helpRequested = enoughArgs and sys.argv[1].lower() in ['?', 'help', '--help', '-h', '-help', 'h']

if not enoughArgs or helpRequested:
    print('''
    Usage:
        regex_search.py [path] "expression"

        Path is optional. If no path is included, the current
        working directory is searched. Note: the regular expression 
        searched for must be surrounded by quotes to parse correctly.
    ''')
    sys.exit()

# Parse sys.argv for path and regex pattern
if len(sys.argv) == 3 and Path(sys.argv[1]).exists():               # Path included & is valid
    search_directory = Path(sys.argv[1])
    try:
        userRegex = re.compile(sys.argv[2])
    except re.error:
        print("Invalid regex pattern. Exiting.")
        sys.exit()
elif len(sys.argv) == 3 and not Path(sys.argv[1]).exists():         # Path included but not valid
    print("Invalid input: Directory does not exist.  Exiting.")
    sys.exit()
elif len(sys.argv) == 2:                                            # No path included
    try:
        userRegex = re.compile(sys.argv[1]) 
        search_directory = Path.cwd()
    except re.error:                                                # Invalid regex
        print("Invalid regex pattern.  Exiting.")
        sys.exit()
elif len(sys.argv) < 2:                                             # No path or regex included
    print(usage)
    sys.exit()

# Generator function to yield only files, not directories
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file

# let's work within the directory itself.
os.chdir(search_directory)

# Gather files to iterate through or error if there are no text files
text_files = [f for f in files(Path.cwd()) if mime.from_file(f) == "text/plain"]
if len(text_files) == 0:
    print(f"There are no text files to search in {search_directory}.  Exiting")
    sys.exit()

for f in text_files:
    filename = f
    f = search_directory/Path(f)
    with open(f, encoding='utf_8') as file:
        for line in enumerate(file.readlines()):
            match = userRegex.search(line[1])
            if match != None:
                print(f"Pattern matched in file '{filename}' on line [{line[0]+1}]:> '{match.group()}'")

# go back to the original directory
os.chdir(previous_directory)