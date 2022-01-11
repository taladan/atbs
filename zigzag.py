import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
worm = '**********'
snake = '##########'
mover = worm
iteration = 0

try:
    while True: # Main program loop.
        print(' ' * indent, end = '')
        print(worm)
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:
            indent += 1
            if indent == 20 - len(worm):
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
