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

def test_is_leap_year():
    known_leap_years = (1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832,
        1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 
        1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 
        1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 
        1972, 1976, 1980, 1984, 1988, 1992, 1996, 2004, 2008, 2012, 2016, 
        2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 
        2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 
        2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 
        2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 
        2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232, 2236, 2240, 2244, 
        2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 
        2292, 2296, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 
        2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 
        2384, 2388, 2392, 2396,)
    test_years = range(1800,2400)
    leap_years = []
    for y in test_years:
        if is_leap_year(y):
            leap_years.append(y)
    return tuple(leap_years) == known_leap_years

def test_is_valid_date():
    dates = ('15/10/1990', '222/24/2990', '29/02/1996', '84/4/2021', '12/12/1924', '16/9/2020')
    for date in dates:
        print(f"Testing date: {date}: {is_valid_date(date)}")


if __name__ == '__main__':
    print(test_is_leap_year())
    test_is_valid_date()
