#!/usr/bin/python3
# ATBS: Chapter 4 exercise
# Character Picture Grid
# 'Say you have a list of lists where each value in the inner lists
# is a one character string.  Think of grid[x][y] as being the character
# at the x- and y-coordinates of a "picture" drawn with text characters.
# The (0, 0) origin is in the upper-left corner, the x-coordinates increase
# going right, and the y-coordinates increase going down.
# Copy the previous grid value, and write code that uses it to 
# print the image.

testGrid = [['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

def arrayPrinter(grid):
    result = ""
    currentY = 0 # Loop Tracking.  CurrentY == Current row we're working on
    currentX = 0 # Loop Tracking.  CurrentX == Current column we're working on
    maxY = len(grid) # Maximum number of rows
    maxX = len(grid[0]) # Maximum number of columns

    while currentX <= maxX: # Loop through the columns
        if currentX == maxX: # Break if we're on the last column
            break
        else:
            while currentY <= maxY: # Loop through the rows
                if currentY == maxY: # Print a newline and break if we're on the last row
                    result = result + '\n'
                    currentY = 0
                    break
                else: # Print the current cell we're focused on and increment the row counter
                    result = result + grid[currentY][currentX]
                    currentY += 1
            currentX += 1 # Increment the column counter
    return result

if __name__ == '__main__':
    print(arrayPrinter(testGrid))