class Piece:
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

class Empty(Piece):
    def __str__(self):
        return " "

class Pawn(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)

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
        pass

    def __str__(self):
        return "N" if self.alliance == -1 else "n"

class Bishop(Piece):
    def __init__(self, alliance, position):
        super().__init__(alliance, position)
        pass

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
        pass

    def __str__(self):
        return "K" if self.alliance == -1 else "k"