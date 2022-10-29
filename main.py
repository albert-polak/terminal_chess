

class Chessboard:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.board[0][0] = 1
        self.board[0][1] = 2
        self.board[0][2] = 3
        self.board[0][3] = 4
        self.board[0][4] = 5
        self.board[0][5] = 3
        self.board[0][6] = 2
        self.board[0][7] = 1

        self.board[1][0] = 6
        self.board[1][1] = 6
        self.board[1][2] = 6
        self.board[1][3] = 6
        self.board[1][4] = 6
        self.board[1][5] = 6
        self.board[1][6] = 6
        self.board[1][7] = 6

        self.board[7][0] = 1
        self.board[7][1] = 2
        self.board[7][2] = 3
        self.board[7][3] = 4
        self.board[7][4] = 5
        self.board[7][5] = 3
        self.board[7][6] = 2
        self.board[7][7] = 1

        self.board[6][0] = 6
        self.board[6][1] = 6
        self.board[6][2] = 6
        self.board[6][3] = 6
        self.board[6][4] = 6
        self.board[6][5] = 6
        self.board[6][6] = 6
        self.board[6][7] = 6

    def draw_chessboard(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    print(' ', end=' ')
                elif self.board[i][j] == 1:
                    print('R', end=' ')
                elif self.board[i][j] == 2:
                    print('N', end=' ')
                elif self.board[i][j] == 3:
                    print('B', end=' ')
                elif self.board[i][j] == 4:
                    print('Q', end=' ')
                elif self.board[i][j] == 5:
                    print('K', end=' ')
                elif self.board[i][j] == 6:
                    print('P', end=' ')

            print()



if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.draw_chessboard()