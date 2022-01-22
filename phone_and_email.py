#! python
# Write a program that searches the contents of the 
# System clipboard for all phone numbers and email addresses
# and replaces the content of the clipboard with the 
# results of that search.

"""
The program steps:

1. Get the text off the clipboard.
    - Use the pyperclip module for clipboard management
2. Find all phone numbers and email addresses in the text.
    - write a regex to harvest phone numbers
    - write a regex to harvest emails
    - find all matches of both regexes
    - format the matched strings
3. Paste them onto the clipboard.
    - use pyperclip module to insert the harvested info into the
        system clipboard.
"""

import email
import pyperclip
import re       

text_to_search = str(pyperclip.paste())

phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

phone_numbers = phone_number_regex.findall(text_to_search)
emails = email_regex.findall(text_to_search)
# print(phone_numbers)
# print(emails)
matches = []
for index in range(len(phone_numbers)):
    matches.append(phone_numbers[index][0])

for index in range(len(emails)):
    matches.append(emails[index][0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Phone numbers and emails copied to system clipboard.")
else:
    print("No phone numbers or emails found.")