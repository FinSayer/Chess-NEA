from pieces import *

class Board:
    def __init__(self):
        self.rows, self.cols = (8, 8)
        #creating a 2D array of size 8 by 8 filled with Empty classes
        self.grid = [[Empty(0, [j, i]) for i in range(self.cols)] for j in range(self.rows)]

    def start(self):
        self.grid[0][0] = Rook(-1, [0, 0])
        self.grid[0][1] = Knight(-1, [0, 1])
        self.grid[0][2] = Bishop(-1, [0, 2])
        self.grid[0][3] = Queen(-1, [0, 3])
        self.grid[0][4] = King(-1, [0, 4])
        self.grid[0][5] = Bishop(-1, [0, 5])
        self.grid[0][6] = Knight(-1, [0, 6])
        self.grid[0][7] = Rook(-1, [0, 7])

        for i in range(self.cols):
            self.grid[1][i] = Pawn(-1, [1, i])

        self.grid[7][0] = Rook(1, [7, 0])
        self.grid[7][1] = Knight(1, [7, 1])
        self.grid[7][2] = Bishop(1, [7, 2])
        self.grid[7][3] = Queen(1, [7, 3])
        self.grid[7][4] = King(1, [7, 4])
        self.grid[7][5] = Bishop(1, [7, 5])
        self.grid[7][6] = Knight(1, [7, 6])
        self.grid[7][7] = Rook(1, [7, 7])

        for i in range(self.cols):
            self.grid[6][i] = Pawn(1, [1, i])

    def __str__(self):
        for j in self.grid:
            for e, i in enumerate(j):
                if e == 7:
                    print(str(i), end="\n")
                else:
                    print(str(i), end=" │ ")
        return ""