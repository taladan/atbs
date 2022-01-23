#! python
# date_detection.py
# ATBS Chapter 7
# In this chapter we are working with regular expressions.
# This script is meant to determine if a date entered is a valid
# one in the format of DD/MM/YYYY.  It should detect if the day passed falls
# inside the actual month boundaries and will detect whether a year is a 
# leap year or not.

# Imports
import re

# regular expression definition
dateRegex = re.compile(r'''
    ^([0-3]?\d)/        # Day
    ([01]?\d)/          # Month
    (\d+)$''', re.VERBOSE)          # Year

months = [
    None,
    ('January',(31,)),
    ('February',(28,29)),
    ('March',(31,)),
    ('April',(30,)),
    ('May',(31,)),
    ('June',(30,)),
    ('July',(31,)),
    ('August',(31,)),
    ('September',(30,)),
    ('October',(31,)),
    ('November',(30,)),
    ('December',(31,))]

def is_valid_date(text):
    try:
        day, month, year = map(int,dateRegex.search(text).groups())
        return month <= 12 and day <= months[month][1][month == 2 and is_leap_year(year)]
    except (AttributeError, ValueError) as e:
        print(e)
        return False

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if __name__ == '__main__':
    test_dates = ('12/12/2020',
        '32/12/2020',
        '29/2/2004',
        '30/13/2004',
        '30/12/04',
        '12/12/1212')
    for d in test_dates:
        print(f"Date passed: {d}  Result returned: {is_valid_date(d)}")