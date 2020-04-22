from board import *
from pieces import *

B = Board()

B.start()

while 1:
    print(B)
    xpos_start = int(input("x >"))
    ypos_start = int(input("y >"))
    piece = B.grid[ypos_start][xpos_start]
    B.grid[ypos_start][xpos_start] = Empty(0, [ypos_start][xpos_start])
    xpos_end = int(input("x >"))
    ypos_end = int(input("y >"))
    B.grid[ypos_end][xpos_end] = piece