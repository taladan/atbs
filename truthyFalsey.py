name = ''
numOfGuests = ''
while not name:
    print('Enter your name:')
    name = input()
while not numOfGuests:
    print('How many guests will you have?')
    numOfGuests = input()
    if numOfGuests:
        print('Be sure to have enough room for all your guests.')
print('Done')
