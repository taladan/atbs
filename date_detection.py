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
# dateRegex = re.compile(r'''
#                         ^([0-3]?[0-9])/              # Day
#                         ([0-3]?[0-9])/              # Month
#                         ([1-2][0-9][0-9][0-9])$      # Year
#                         ''',re.VERBOSE)

# We store months in a dictionary with the numerical value of the month key with the month 
# name and its maximum number of days as a tuple of tuple values (to account for February leap years.)

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

# months = {
#     '01':('January',(31,)),
#     '02':('February',(28,29)),
#     '03':('March',(31,)),
#     '04':('April',(30,)),
#     '05':('May',(31,)),
#     '06':('June',(30,)),
#     '07':('July',(31,)),
#     '08':('August',(31,)),
#     '09':('September',(30,)),
#     '10':('October',(31,)),
#     '11':('November',(30,)),
#     '12':('December',(31,))}

def is_valid_date(text):
    try:
        day, month, year = map(int,dateRegex.search(text).groups())
        return month <= 12 and day <= months[month][1][month == 2 and is_leap_year(year)]
    except (AttributeError, ValueError) as e:
        print(e)
        return False
    
# def _is_valid_day(day, month, year):
#     result = False # Set the initial value of the result
#     month_name = months[month][0] # Set the month name
    
#     # Get the total number of days in the given month
#     if month_name == "February" and is_leap_year(year):
#         month_length = months[month][1][1]
#     else:
#         month_length = months[month][1][0]

#     if month not in months: # Test for valid month
#         result = False
#     elif int(month_length) < int(day): # Test for valid day
#         result = False
#     else:
#         result = True
#     return result

def is_leap_year(year):
    # year = int(year)
    # result = False
    # if year%100 == 0:
    #     result = False
    # elif year%4 == 0:
    #     result = True
    # return result
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