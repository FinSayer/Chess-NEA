from pieces import *

class Board:
    def __init__(self):
        self.ROWS, self.COLUMNS = (8, 8)
        #creating a 2D array of size 8 by 8 filled with Empty classes
        self.grid = [[Empty(0, [j, i]) for i in range(self.COLUMNS)] for j in range(self.ROWS)]

    def board_init(self):
        # self.grid[0][0] = Rook(-1, [0, 0])
        # self.grid[0][1] = Knight(-1, [0, 1])
        self.grid[0][2] = Bishop(-1, [0, 2])
        self.grid[0][5] = Bishop(-1, [0, 5])


    def __str__(self):
        print(self.grid)
        for j in self.grid:
            for e, i in enumerate(j):
                if e == 7:
                    print(str(i), end="   {}\n".format(self.grid.index(j)))
                else:
                    print(str(i), end=" │ ")
        print("\n0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 ")
        return ""
    
