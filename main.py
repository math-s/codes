class Game:
    def __init__(self):
        self.gameM = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.player = 1
        self.size = 3
        self.end = False
        self.winner = 0
        self.playgoer = 0

    def __str__(self):
        return self.end()

    """ ------------------------------------ """

    def play(self):
        mov = int(input("Play! "))
        if mov == 1 and self.gameM[2][0] == 0:
            self.gameM[2][0] = self.player
            return True
        if mov == 2 and self.gameM[2][1] == 0:
            self.gameM[2][1] = self.player
            return True
        if mov == 3 and self.gameM[2][2] == 0:
            self.gameM[2][2] = self.player
            return True
        if mov == 4 and self.gameM[1][0] == 0:
            self.gameM[1][0] = self.player
            return True
        if mov == 5 and self.gameM[1][1] == 0:
            self.gameM[1][1] = self.player
            return True
        if mov == 6 and self.gameM[1][2] == 0:
            self.gameM[1][2] = self.player
            return True
        if mov == 7 and self.gameM[0][0] == 0:
            self.gameM[0][0] = self.player
            return True
        if mov == 8 and self.gameM[0][1] == 0:
            self.gameM[0][1] = self.player
            return True
        if mov == 9 and self.gameM[0][2] == 0:
            self.gameM[0][2] = self.player
            return True
        else:

            print("JOGADA INVÁLIDA")
            return False

    def match(self):
        self.drawBoard()
        if self.play():
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
        self.verifyWinner()
        self.finishGame()

    def verifyWinner(self):
        self.drawBoard()
        for i in range(0, 3):
            if self.gameM[i] == [1, 1, 1] or \
                self.gameM[0][i] == self.gameM[1][i] == self.gameM[2][i] == 1 or \
                self.gameM[0][0] == self.gameM[1][1] == self.gameM[2][2] == 1 or \
                self.gameM[0][2] == self.gameM[1][1] == self.gameM[2][0] == 1 or \
                self.gameM[i] == [2, 2, 2] or \
                self.gameM[0][i] == self.gameM[1][i] == self.gameM[2][i] == 2 or \
                self.gameM[0][0] == self.gameM[1][1] == self.gameM[2][2] == 2 or \
                self.gameM[0][2] == self.gameM[1][1] == self.gameM[2][0] == 2:
                self.end = True
                return True
            else:
                self.end = False
                return False

    def finishGame(self):
        if not self.end:
            self.playgoer = self.playgoer + 1
            if self.playgoer == 9:
                self.drawBoard()
                print("THE GAME IS OVER")
                print("NOBODY WON")
            else:
                return self.match()
        elif self.end:
            self.drawBoard()
            print("THE GAME IS OVER")
            print("PLAYER " + str(self.winner) + " WON")

    """ ------------------------------------ """

    def drawBoard(self):
        c = ""
        for x in range(0, self.size):
            c = c + self.drawLine() + '\n'
            c = c + self.drawColumns(x) + '\n'
        c = c + self.drawLine()
        print(c)

    def drawLine(self):
        c = ""
        for x in range(0, self.size):
            c = c + " ---"
        return c

    def drawColumns(self, line):
        c = ""
        for x in range(0, self.size):
            if self.gameM[line][x] == 0:
                c = c + "|   "
            elif self.gameM[line][x] == 1:
                c = c + "|▉▉▉"
            else:
                c = c + "|⫻⫻⫻"
        c = c + "|"
        return c


g = Game()
g.match()
