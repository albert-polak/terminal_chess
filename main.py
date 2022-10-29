

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

        self.knight_move_matrix = [[0, 1, 0, 1, 0], 
                                    [1, 0, 0, 0, 1], 
                                    [0, 0, 0, 0, 0], 
                                    [1, 0, 0, 0, 1], 
                                    [0, 1, 0, 1, 0]]

    def draw_chessboard(self):
        print("  A   B   C   D   E   F   G   H")
        print('---------------------------------')
        for i in range(8):
            for j in range(8):
                print('|', end=' ')
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
            print('|', end=' ')
            print(8-i)
            print('---------------------------------')

    def move(self, start, end):
        start = start.upper()
        end = end.upper()
        if start[0] == 'A':
            start_x = 0
        elif start[0] == 'B':
            start_x = 1
        elif start[0] == 'C':
            start_x = 2
        elif start[0] == 'D':
            start_x = 3
        elif start[0] == 'E':
            start_x = 4
        elif start[0] == 'F':
            start_x = 5
        elif start[0] == 'G':
            start_x = 6
        elif start[0] == 'H':
            start_x = 7
        else:
            print('Impossible move!')

        if end[0] == 'A':
            end_x = 0
        elif end[0] == 'B':
            end_x = 1
        elif end[0] == 'C':
            end_x = 2
        elif end[0] == 'D':
            end_x = 3
        elif end[0] == 'E':
            end_x = 4
        elif end[0] == 'F':
            end_x = 5
        elif end[0] == 'G':
            end_x = 6
        elif end[0] == 'H':
            end_x = 7
        else:
            print('Impossible move!')
        try:
            start_y = 8 - int(start[1])
            end_y = 8 - int(end[1])

            start_tuple = (start_x, start_y)
            end_tuple = (end_x, end_y)

            if self.check_if_legal(start_tuple, end_tuple):
                self.board[end_y][end_x] = self.board[start_y][start_x]
                self.board[start_y][start_x] = 0 
            else:
                print('Impossible move!')
        except:
            print('Wrong move!')
            
    def check_if_legal(self, start, end):
        y_move = end[1]-start[1]
        x_move = end[0] - start[0]
        if 7 < start[0] < 0 or 7 < start[1] < 0 or 7 < end[0] < 0 or 7 < end[1] < 0:
            return False
        elif self.board[start[1]][start[0]] == 0:
            return False
        elif self.board[start[1]][start[0]] == 1:
            if start[0]-end[0] != 0 and start[1]-end[1] != 0:
                return False
            else:
                return True
        elif self.board[start[1]][start[0]] == 2:
            if self.knight_move_matrix[2+y_move][2+x_move] == 1:
                return True
            else:
                return False
        else:
            return True





if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.draw_chessboard()

    while True:
        start = input("Start: ")
        end = input("End: ")
        chessboard.move(start, end)
        chessboard.draw_chessboard()
