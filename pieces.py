class Piece:
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def check_move(self, xpos_start, ypos_start, xpos_end, ypos_end):
        for i in self.move_vector:
            if (xpos_end - xpos_start == i[0]) and (ypos_end - ypos_start == i[1]):
                return True

class Empty(Piece):
    def __str__(self):
        return " "

class Pawn(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        self.move_vector = [[0, -1], [0, -2]]

    def __str__(self):
        return "P" if self.alliance == -1 else "p"

class Rook(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        pass

    def __str__(self):
        return "R" if self.alliance == -1 else "r"

class Knight(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        self.move_vector = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]

    def __str__(self):
        return "N" if self.alliance == -1 else "n"

class Bishop(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        self.move_vector = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

    def checkMove(self, xpos_start, ypos_start, xpos_end, ypos_end):
        if abs(xpos_end - xpos_start) == abs(ypos_end - ypos_start):
            return True

    def __str__(self):
        return "B" if self.alliance == -1 else "b"

class Queen(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        pass

    def __str__(self):
        return "Q" if self.alliance == -1 else "q"

class King(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        self.move_vector = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    def __str__(self):
        return "K" if self.alliance == -1 else "k"