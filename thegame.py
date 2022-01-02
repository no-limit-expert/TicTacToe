from tictactoe import TicTacToe


def playGame():
    game1 = TicTacToe()
    win = False
    turn = "x"
    print(f"{turn} sin tur.")
    game1.showBoard()
    game1.pick(int(input("Velg rad: ")), int(input("Velg kolonne: ")), turn)
    while not win:
        if turn == "x":
            turn = "o"
            print(f"{turn} sin tur.")
            print()
            game1.pick(int(input("Velg rad: ")), int(input("Velg kolonne: ")), turn)


        elif turn == "o":
            turn = "x"
            print(f"{turn} sin tur.")
            game1.pick(int(input("Velg rad: ")), int(input("Velg kolonne: ")), turn)

        win = game1.winCheck()
    print(f"{turn} vinner!")



playGame()
