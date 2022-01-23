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
                        ^([0-3]?[0-9])/              # Day
                        ([0-3]?[0-9])/              # Month
                        ([1-2][0-9][0-9][0-9])$      # Year
                        ''',re.VERBOSE)

# We store months in a dictionary with the numerical value of the month key with the month 
# name and its maximum number of days as a tuple of tuple values (to account for February leap years.)

months = {
    '01':('January',(31,)),
    '02':('February',(28,29)),
    '03':('March',(31,)),
    '04':('April',(30,)),
    '05':('May',(31,)),
    '06':('June',(30,)),
    '07':('July',(31,)),
    '08':('August',(31,)),
    '09':('September',(30,)),
    '10':('October',(31,)),
    '11':('November',(30,)),
    '12':('December',(31,))
}

def is_valid_date(text):
    result = False
    try:
        day, month, year = dateRegex.search(text).groups()
        if len(day) < 2:
            day = '0' + day # Day format must be 01-31
        if len(month) < 2:
            month = '0' + month # Month format must be 01-12
        if _is_valid_day(day, month, year):
            result = True
    except AttributeError:
        result = False
    return result
    
def _is_valid_day(day, month, year):
    result = False # Set the initial value of the result
    month_name = months[month][0] # Set the month name
    
    # Get the total number of days in the given month
    if month_name == "February" and is_leap_year(year):
        month_length = months[month][1][1]
    else:
        month_length = months[month][1][0]

    if month not in months: # Test for valid month
        result = False
    elif int(month_length) < int(day): # Test for valid day
        result = False
    else:
        result = True
    return result

def is_leap_year(year):
    year = int(year)
    result = False
    if year%100 == 0:
        result = False
    elif year%4 == 0:
        result = True
    return result