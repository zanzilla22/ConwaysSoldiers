import numpy as np
import time, os

# with numpy, y is first then x; origin stops in top left

board = np.zeros((8, 9))
board[4:, :] = 1

# Set the print options to display as a matrix
np.set_printoptions(formatter={'all': lambda x: '{:.0f}'.format(x)})

def reprint():
    os.system('clear')
    print("    ", end="")
    for i in range(board.shape[1]):
        print(f" {i} ", end="")
    print("\n")
    for i, row in enumerate(board):
        print(f"{i} |", end=" ")
        for val in row:
            if val == 0:
                print("   ", end="")
            elif val == 1:
                print(" X ", end="")
            elif val == 2:
                print(" O ", end="")
        print(" |")

def move(y, x, dir):
    if(dir == 'up'):
        if(y-2 >= 0):
            if(board[y-1, x] == 1 and board[y-2, x] == 0):
                print("can move")
                board[y, x] = 0
                board[y-1, x] = 0
                board[y-2, x] = 1

    if(dir == 'down'):
        if(y+2 <= board.shape[0]-1):
            if(board[y+1, x] == 1 and board[y+2, x] == 0):
                print("can move")
                board[y, x] = 0
                board[y+1, x] = 0
                board[y+2, x] = 1

    if(dir == 'left'):
        if(x-2 >= 0):
            if(board[y, x-1] == 1 and board[y, x-2] == 0):
                print("can move")
                board[y, x] = 0
                board[y, x-1] = 0
                board[y, x-2] = 1

    if(dir == 'right'):
        if(x+2 <= board.shape[1]-1):
            if(board[y, x+1] == 1 and board[y, x+2] == 0):
                print("can move")
                board[y, x] = 0
                board[y, x+1] = 0
                board[y, x+2] = 1

reprint()
time.sleep(2)
move(5, 5, 'up')
reprint()
time.sleep(2)
move(4, 3, 'right')
reprint()
time.sleep(2)
move(4, 5, 'up')
reprint()
time.sleep(2)
