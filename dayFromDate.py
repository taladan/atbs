#! python

# dayFromDate.py

# Determine the day of the week from a given date.
# This currently only works with the gregorian calendar

# Formula: (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7

# Imports
from date_detection import is_leap_year
from datetime import datetime

# Constants
# Days of the week
DAYS_OF_WEEK = ('Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday')

# Gregorian Century Code
GCCODE = ((17,4), (18,2), (19,0), (20,6), (21,4), (22,2), (23,0),)
MONTHS_CODES = [None,0,3,3,6,1,4,6,2,5,0,3,5]

def find_day(date: datetime) -> str:
    # separate into individual variables and convert to integers
    # Doing it this way to be able to split the year apart before converting
    # individual variables to integers - There might be a better way.
    year, month, day = str(date).split('-')
    yy = int(year[-2:])                                                     # last two digits of YYYY
    cc = int(year[0:-2])                                                    # Up to the last two digits of YYYY
    year = int(year)                                                        # YYYY
    month = int(month)                                                      # MM
    day = int(day)                                                          # DD

<<<<<<< HEAD
    century_code = [code for code in GCCODE if code[0] == cc][0][1]         # Get Cen Code from GCCODE as tuple and 
                                                                            # set value of [0][1] as century code
                                                                            # found this solution from https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples
=======
    century_code = [code for code in GCCODE if code[0] == cc][0][1]
    # century_code_index = [code for code in GCCODE if code[0] == cc]
    # century_code = century_code_index[0][1]
    # for code in range(len(GCCODE)):                                         # find the right century code
    #     if GCCODE[code][0] == cc:
    #         century_code = GCCODE[code][1]
>>>>>>> 454b0746fa9a518d9baf89fbd4fdcf538025fb10

    year_code = (yy + (yy//4)) % 7                                          # Year Code formula
    leap_year_code = 1 if is_leap_year(year) and month in [1,2] else 0      # Leap year code is 0 unless it's a leap year and month is Jan or Feb
    month_code = MONTHS_CODES[month]                                        # month code

    return DAYS_OF_WEEK[(year_code + month_code + century_code + day - leap_year_code) % 7]

if __name__ == '__main__':

    import pyinputplus as pyip

    # If we're running this as a program, ask for a date
    PROMPT = "Please enter a date in the format: MM/DD/YYYY:> "
    response = find_day(pyip.inputDate(PROMPT))
    print(response)
