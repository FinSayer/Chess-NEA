import pygame
import sys
from constants import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, alliance, position, image):
        super(Piece, self).__init__()
        self.alliance = alliance
        self.position = position
        self.clicked = False
        self.image = pygame.transform.scale(pygame.image.load('sprites/' + image), (BLOCK_LENGTH, BLOCK_LENGTH))
        self.rect = self.image.get_rect()
        self.snap_piece()
        sprites.add(self)
        B.grid[self.position[0]][self.position[1]] = self

    def snap_piece(self):
        self.rect.topleft = [(self.position[1] * BLOCK_LENGTH), (self.position[0] * BLOCK_LENGTH)]

    def check_move(self, xpos_end, ypos_end):
        if self.alliance == T.get_turn():
            for vector in self.move_vector:
                for i in range(self.distance_limit):
                    try:
                        v0 = vector[0] * (i + 1)
                        v1 = vector[1] * (i + 1)
                        current_alliance = getattr(B.grid[self.position[0] + v1][self.position[1] + v0], "alliance", 0)
                        if current_alliance == 0:
                            if (ypos_end == self.position[0] + v1) and (xpos_end == self.position[1] + v0):
                                self.place_piece([ypos_end, xpos_end])
                                break
                        elif current_alliance == self.alliance * -1:
                            if (ypos_end == self.position[0] + v1) and (xpos_end == self.position[1] + v0):
                                self.take_piece([ypos_end, xpos_end])
                            break
                        else:
                            break
                    except IndexError:
                        continue
        self.snap_piece()

    def place_piece(self, new_position):
        B.grid[self.position[0]][self.position[1]] = None
        self.position = new_position
        B.grid[self.position[0]][self.position[1]] = self
        if isinstance(self, Pawn):
            self.set_distance_limit()
        T.set_turn()

    def take_piece(self, new_position):
        sprites.remove(B.grid[new_position[0]][new_position[1]])
        self.place_piece(new_position)


class Pawn(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.distance_limit = 2
        self.move_vector = [[0, -1]]
        self.take_vector = [[-1, -1], [1, -1]]
        if self.alliance == -1:
            self.move_vector = [[i * -1 for i in j] for j in self.move_vector]
            self.take_vector = [[i * -1 for i in j] for j in self.take_vector]

    def set_distance_limit(self):
        self.distance_limit = 1

    # def check_move(self, xpos_end, ypos_end):
    #     if self.alliance == T.get_turn():
    #         for vector in self.move_vector:
    #             for i in range(self.distance_limit):
    #                 try:
    #                     v0 = vector[0] * (i + 1)
    #                     v1 = vector[1] * (i + 1)
    #                     current_alliance = getattr(B.grid[self.position[0] + v1][self.position[1] + v0], "alliance", 0)
    #                     if current_alliance == 0:
    #                         if (ypos_end == self.position[0] + v1) and (xpos_end == self.position[1] + v0):
    #                             self.place_piece([ypos_end, xpos_end])
    #                             break
    #                     elif current_alliance == self.alliance * -1:
    #                         if (ypos_end == self.position[0] + v1) and (xpos_end == self.position[1] + v0):
    #                             self.take_piece([ypos_end, xpos_end])
    #                         break
    #                     else:
    #                         break
    #                 except IndexError:
    #                     continue
    #     self.snap_piece()


class Rook(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.move_vector = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        self.distance_limit = 8


class Knight(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.move_vector = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
        self.distance_limit = 1


class Bishop(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.move_vector = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
        self.distance_limit = 8


class Queen(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.move_vector = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        self.distance_limit = 8


class King(Piece):
    def __init__(self, alliance, position, image):
        super().__init__(alliance, position, image)
        self.move_vector = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        self.distance_limit = 1


class Board:
    def __init__(self):
        self.ROWS, self.COLUMNS = (8, 8)
        # creating a 2D array of size 8 by 8 filled with Empty classes
        self.grid = [[None for _ in range(self.ROWS)] for _ in range(self.COLUMNS)]


class Turn:
    def __init__(self):
        self.turn = 1

    def get_turn(self):
        return self.turn

    def set_turn(self):
        self.turn *= -1


def board_init():
    Rook(-1, [0, 0], 'b_rook.png')
    Knight(-1, [0, 1], 'b_knight.png')
    Bishop(-1, [0, 2], 'b_bishop.png')
    Queen(-1, [0, 3], 'b_queen.png')
    King(-1, [0, 4], 'b_king.png')
    Bishop(-1, [0, 5], 'b_bishop.png')
    Knight(-1, [0, 6], 'b_knight.png')
    Rook(-1, [0, 7], 'b_rook.png')
    for i in range(8):
        Pawn(-1, [1, i], 'b_pawn.png')
    Rook(1, [7, 0], 'w_rook.png')
    Knight(1, [7, 1], 'w_knight.png')
    Bishop(1, [7, 2], 'w_bishop.png')
    Queen(1, [7, 3], 'w_queen.png')
    King(1, [7, 4], 'w_king.png')
    Bishop(1, [7, 5], 'w_bishop.png')
    Knight(1, [7, 6], 'w_knight.png')
    Rook(1, [7, 7], 'w_rook.png')
    for i in range(8):
        Pawn(1, [6, i], 'w_pawn.png')


def minmax():
    pass


def zero_div(n, d):
    return n / d if d else 0


def draw_board(surface, grid):
    for je, j in enumerate(grid):
        for ie, i in enumerate(j):
            myrect = pygame.Rect(ie * BLOCK_LENGTH, je * BLOCK_LENGTH, BLOCK_LENGTH, BLOCK_LENGTH)
            if (je + ie) % 2 == 1:
                pygame.draw.rect(surface, BLACK, myrect)
            else:
                pygame.draw.rect(surface, WHITE, myrect)


def update(surface, grid):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    for sprite in sprites.sprites():
                        if sprite.rect.collidepoint(pos):
                            sprite.clicked = True
                            sprites.move_to_front(sprite)

            if event.type == pygame.MOUSEBUTTONUP:
                for sprite in sprites.sprites():
                    if sprite.clicked:
                        pos = pygame.mouse.get_pos()
                        xpos_end = int(pos[0] / BLOCK_LENGTH)
                        ypos_end = int(pos[1] / BLOCK_LENGTH)
                        sprite.check_move(xpos_end, ypos_end)
                        sprite.clicked = False

        for sprite in sprites.sprites():
            if sprite.clicked:
                pos = pygame.mouse.get_pos()
                sprite.rect.topleft = [pos[0] - (sprite.rect.width / 2), pos[1] - (sprite.rect.height / 2)]

        pygame.display.update()
        draw_board(surface, grid)
        sprites.draw(surface)
        clock.tick(FPS)


pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sprites = pygame.sprite.LayeredUpdates()
B = Board()
T = Turn()
board_init()
update(surface, B.grid)

# https://opengameart.org/content/chess-pieces-and-board-squares

