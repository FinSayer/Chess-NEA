import pygame
import sys

from board import *
from pieces import *

B = Board()
B.board_init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BLOCK_LENGTH = 75
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_piece(piece, ypos, xpos):
    # at the moment im just checking against the string value of the class but when I check B.grid[je][ie] == Bishop(-1, [je, ie]) it returns false.
    if piece == "B":
        return pygame.transform.scale(pygame.image.load('castle.png'), (BLOCK_LENGTH, BLOCK_LENGTH))

def draw_board(surface, grid):
    for je, j in enumerate(grid):
        for ie, i in enumerate(j):
            myrect = pygame.Rect(ie*BLOCK_LENGTH, je*BLOCK_LENGTH, BLOCK_LENGTH, BLOCK_LENGTH)
            if (je + ie) % 2 == 1:
                pygame.draw.rect(surface, BLACK, myrect)
            elif (je + ie) % 2 == 0:
                pygame.draw.rect(surface, WHITE, myrect)
            piece = str(B.grid[je][ie])
            if piece != " ":
                pygame.Surface.blit(surface, draw_piece(piece, je, ie), (ie*BLOCK_LENGTH, je*BLOCK_LENGTH))

def update(surface, grid):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        draw_board(surface, grid)
        pygame.display.update()
        x_position_start = int(input("x >"))
        y_position_start = int(input("y >"))
        piece = B.grid[y_position_start][x_position_start]
        x_position_end = int(input("x >"))
        y_position_end = int(input("y >"))
        if piece.checkMove(x_position_start, y_position_start, x_position_end, y_position_end) == True:
            B.grid[y_position_start][x_position_start] = Empty(0, [y_position_start, x_position_start])
            B.grid[y_position_end][x_position_end] = piece
        else:
            print("Invalid")

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
update(surface, B.grid)


while 1:
    print(B)
    x_position_start = int(input("x >"))
    y_position_start = int(input("y >"))
    piece = B.grid[y_position_start][x_position_start]
    x_position_end = int(input("x >"))
    y_position_end = int(input("y >"))
    if piece.checkMove(x_position_start, y_position_start, x_position_end, y_position_end) == True:
        B.grid[y_position_start][x_position_start] = Empty(0, [y_position_start, x_position_start])
        B.grid[y_position_end][x_position_end] = piece
    else:
        print("Invalid")


#https://www.geeksforgeeks.org/type-isinstance-python/