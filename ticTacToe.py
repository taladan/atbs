#!/usr/bin/python3
# ATBS Chapter 5 Tic Tac Toe example
from clearScreen import clear

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    
# 1. Print the blank board
# 2. Ask player X to go
# 3. Print the board
# 4. Ask player 0 to go
# 5. Repeat steps 2-4 until there is either a straight line vertically, diagonally or horizontally, or there are no more spaces left
# 
def playerMove(turn)
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def checkBoard():
    # Vertical 
    leftVertical = ('top-L', 'mid-L', 'low-L')
    midVertical = ('top-M', 'mid-M', 'low-M')
    rightVertical = ('top-R', 'mid-R', 'low-R')

    # horizontal
    topHorizontal = ('top-L', 'top-M', 'top-R')
    midHorizontal = ('mid-L,' 'mid-M', 'mid-R')
    lowHorizontal = ('low-L', 'low-M', 'low-R')

    # diagonal
    descendingDiagonal = ('top-L', 'mid-M', 'low-R')
    ascendingDiagonal = ('low-L', 'mid-M', 'top-R')

def mainLoop():
    clear() 
    turn = 'X'
    printBoard(theBoard)

    # while True:
    #     playerMove(turn)

