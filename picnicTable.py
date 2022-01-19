#!/usr/bin/python3
# ATBS: CH 6 Picnic Table example
# The original function 'printPicnic' allows to printing of a user-defined sized table of picnic items.
# The additional function 'tablePrint' takes the methods introduced in this example and allows a bit more
# extended functionality:
# The caller can pass the table header, dictionary of items, left and right widths of the columns, along with the
# pad character of the header and the table, while setting defaults.

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


def tablePrint(tableHeader, itemsDict, leftWidth, rightWidth, headerPadCharacter='-', tablePadCharacter='.'):
    print(tableHeader.center(leftWidth + rightWidth, headerPadCharacter))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, tablePadCharacter) + str(v).rjust(rightWidth))




if __name__ == '__main__':
    
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 5000}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)

    testDict = {'Bob': 'Julianus 14, 1976', 'Alice': 'Julianus 23, 1974', 'Steve': 'Octarius 30, 2002', 'Mattius': 'Septanius 7, 2003', 'Brianne': 'Octarius 11, 2005', 'Rebhorn': 'Septanius 20, 2006'}
    tablePrint('Test Table of Values', testDict, 30, 60, '~', '.')
