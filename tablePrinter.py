#! python
# tablePrinter.py
# ATBS: Ch 6 practice project
# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right justified.
# Assume that all the inner lists will contain the same number of strings.


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    """
    printTable():
        This function takes one argument that must be a list of lists, 
        with each internal list being of the same number of items.
        It then prints a table where each column is one of the lists, rjusted to the
        length of the longest item in that list.
    """
    number_of_columns = len(table)
    number_of_rows = len(table[0])
    max_column_widths = []

    # Get a list of integers equal to the max word length in each column
    for i in range(len(table)):
        l = len(max(table[i], key=len))
        max_column_widths.append(l)
  
    row = 0
    column = 0

    while column <= number_of_columns:
        while row  < number_of_rows - 1:
            width = max_column_widths[row]
            print(table[row][column].rjust(width) + " ", end = '')
            row += 1
        print('\n')
        column += 1
        row = 0

if __name__ == '__main__':
    printTable(tableData)
