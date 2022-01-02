class TicTacToe:
    def __init__(self):
        self._board = [[" _ ", " _ ", " _ "],
                       [" _ ", " _ ", " _ "],
                       [" _ ", " _ ", " _ "]]

    def showBoard(self):
        print()
        for line in self._board:
            print(f"{line[0]}|{line[1]}|{line[2]}")
        print()

    def pick(self, rad, kolonne, turn):
        assert (0 < rad <= 3)
        assert (0 < kolonne <= 3)
        assert (turn == "x" or turn == "o")
        x = 0
        while x == 0:
            if self._board[rad - 1][kolonne - 1] is not " _ ":
                print("Denne ruten er opptatt, velg en annen.")
                print()
                self.showBoard()
                rad = int(input("Velg rad: "))
                kolonne = int(input("Velg kolonne: "))
            else:
                self._board[rad - 1][kolonne - 1] = " " + turn + " "
                self.showBoard()
                x = 1

    def winCheck(self):
        board = self._board
        # Diagonal
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print("Win diagonal")
            return True
        elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            print("Win diagonal")
            return True
        # Horisontal
        for rad in self._board:
            if len(set(rad)) == 1:
                for var in rad:
                    if " x " == var or " o " == var:
                        print("Horisontal win.")
                        return True
        # Vertikal
        kolonne = []
        x = 0
        while x < 3:
            for gruppe in board:
                kolonne.append(gruppe[x])
            x += 1
            if len(set(kolonne)) == 1:
                print("win vertikal")
                return True
