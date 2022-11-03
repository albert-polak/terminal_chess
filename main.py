import copy

# Main class
class Chessboard:
    def __init__(self):
        # Filling chessboard with pieces
        self.board = [[(0, 0) for i in range(8)] for j in range(8)]
        # Tuple of (type_of_piece, color)
        self.board[0][0] = (1, 'B')
        self.board[0][1] = (2, 'B')
        self.board[0][2] = (3, 'B')
        self.board[0][3] = (4, 'B')
        self.board[0][4] = (5, 'B')
        self.board[0][5] = (3, 'B')
        self.board[0][6] = (2, 'B')
        self.board[0][7] = (1, 'B')

        self.board[1][0] = (6, 'B')
        self.board[1][1] = (6, 'B')
        self.board[1][2] = (6, 'B')
        self.board[1][3] = (6, 'B')
        self.board[1][4] = (6, 'B')
        self.board[1][5] = (6, 'B')
        self.board[1][6] = (6, 'B')
        self.board[1][7] = (6, 'B')

        self.board[7][0] = (1, 'W')
        self.board[7][1] = (2, 'W')
        self.board[7][2] = (3, 'W')
        self.board[7][3] = (4, 'W')
        self.board[7][4] = (5, 'W')
        self.board[7][5] = (3, 'W')
        self.board[7][6] = (2, 'W')
        self.board[7][7] = (1, 'W')

        self.board[6][0] = (6, 'W')
        self.board[6][1] = (6, 'W')
        self.board[6][2] = (6, 'W')
        self.board[6][3] = (6, 'W')
        self.board[6][4] = (6, 'W')
        self.board[6][5] = (6, 'W')
        self.board[6][6] = (6, 'W')
        self.board[6][7] = (6, 'W')

        # Available moves for knight matrix 
        self.knight_move_matrix = [[0, 1, 0, 1, 0],
                                   [1, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 1],
                                   [0, 1, 0, 1, 0]]

        self.previous_board = copy.deepcopy(self.board)

    # Drawing the chessboard in terminal
    def draw_chessboard(self):
        print("  A   B   C   D   E   F   G   H")
        print('---------------------------------')
        for i in range(8):
            for j in range(8):
                print('|', end=' ')
                if self.board[i][j][0] == 0:
                    print(' ', end=' ')
                elif self.board[i][j][0] == 1:
                    print('R', end=' ')
                elif self.board[i][j][0] == 2:
                    print('N', end=' ')
                elif self.board[i][j][0] == 3:
                    print('B', end=' ')
                elif self.board[i][j][0] == 4:
                    print('Q', end=' ')
                elif self.board[i][j][0] == 5:
                    print('K', end=' ')
                elif self.board[i][j][0] == 6:
                    print('P', end=' ')
            print('|', end=' ')
            print(8-i)
            print('---------------------------------')

    def move(self, start, end, color):
        start = start.upper()
        end = end.upper()
        try:
            # Preventing incorrect notation
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

            start_y = 8 - int(start[1])
            end_y = 8 - int(end[1])

            start_tuple = (start_x, start_y)
            end_tuple = (end_x, end_y)

            if self.check_if_legal(start_tuple, end_tuple, color):
                self.previous_board = copy.deepcopy(self.board)
                # Checking if the pawn is on the last row
                if self.board[start_tuple[1]][start_tuple[0]][0] == 6 and end_tuple[1] == 0:
                    self.board[end_tuple[1]][end_tuple[0]] = (4, color)
                elif self.board[start_tuple[1]][start_tuple[0]][0] == 6 and end_tuple[1] == 7:
                    self.board[end_tuple[1]][end_tuple[0]] = (4, color)
                else:
                    self.board[end_y][end_x] = self.board[start_y][start_x]
                self.board[start_y][start_x] = (0, 0)
            else:
                print('Impossible move!')
                return False
        except:
            print('Wrong move!')
            return False
        return True


    def check_if_blocked(self, start, end, color):
        # Checking if a piece is in the way
        y_move = end[1] - start[1]
        x_move = end[0] - start[0]
        if x_move == 0:
            if y_move > 0:
                for i in range(start[1]+1, end[1]+1):
                    if self.board[i][start[0]][0] != 0 and self.board[i][start[0]][1] == color:
                        return False
                    elif self.board[i][start[0]][0] != 0 and i != end[1]:
                        return False
                return True
            else:
                for i in range(start[1]-1, end[1]-1, -1):
                    if self.board[i][start[0]][0] != 0 and self.board[i][start[0]][1] == color:
                        return False
                    elif self.board[i][start[0]][0] != 0 and i != end[1]:
                        return False
                return True
        elif y_move == 0:
            if x_move > 0:
                for i in range(start[0]+1, end[0]+1):
                    if self.board[start[1]][i][0] != 0 and self.board[start[1]][i][1] == color:
                        return False
                    elif self.board[start[1]][i][0] != 0 and i != end[0]:
                        return False
                return True
            else:
                for i in range(start[0]-1, end[0]-1, -1):
                    if self.board[start[1]][i][0] != 0 and self.board[start[1]][i][1] == color:
                        return False
                    elif self.board[start[1]][i][0] != 0 and i != end[0]:
                        return False
                return True
        elif abs(x_move) == abs(y_move):
            if x_move > 0:
                if y_move > 0:
                    for i in range(1, x_move+1):
                        if self.board[start[1]+i][start[0]+i][0] != 0 and self.board[start[1]+i][start[0]+i][1] == color:
                            return False
                        elif self.board[start[1]+i][start[0]+i][0] != 0 and i != x_move:
                            return False
                    return True
                else:
                    for i in range(1, x_move+1):
                        if self.board[start[1]-i][start[0]+i][0] != 0 and self.board[start[1]-i][start[0]+i][1] == color:
                            return False
                        elif self.board[start[1]-i][start[0]+i][0] != 0 and i != x_move:
                            return False
                    return True
            else:
                if y_move > 0:
                    for i in range(1, abs(x_move)+1):
                        if self.board[start[1]+i][start[0]-i][0] != 0 and self.board[start[1]+i][start[0]-i][1] == color:
                            return False
                        elif self.board[start[1]+i][start[0]-i][0] != 0 and i != abs(x_move):
                            return False
                    return True
                else:
                    for i in range(1, abs(x_move)+1):
                        if self.board[start[1]-i][start[0]-i][0] != 0 and self.board[start[1]-i][start[0]-i][1] == color:
                            return False
                        elif self.board[start[1]-i][start[0]-i][0] != 0 and i != abs(x_move):
                            return False
                    return True
        else:
            return False


    # Checking if a move is legal for each piece
    def check_if_legal(self, start, end, color):
        y_move = end[1] - start[1]
        x_move = end[0] - start[0]



        # Checking boundaries
        if 7 < start[0] < 0 or 7 < start[1] < 0 or 7 < end[0] < 0 or 7 < end[1] < 0:
            return False
        # Checking if correct color is being moved
        elif self.board[start[1]][start[0]][1] != color:
            return False
        # Checking of starting position isn't empty
        elif self.board[start[1]][start[0]][0] == 0:
            return False
        # Checking if the move is right for a Rook
        elif self.board[start[1]][start[0]][0] == 1:
            if start[0]-end[0] != 0 and start[1]-end[1] != 0:
                return False
            elif self.check_if_blocked(start, end, color):
                return True
            else: return False
        # Cheking if the move is right for a Knight
        elif self.board[start[1]][start[0]][0] == 2:
            if self.knight_move_matrix[2+y_move][2+x_move] == 1:
                return True
            else:
                return False
        # Cheking if the move is right for a Bishop
        elif self.board[start[1]][start[0]][0] == 3:
            if abs(y_move) == abs(x_move) and x_move != 0:
                if self.check_if_blocked(start, end, color):
                    return True
                else:
                    return False
            else:
                return False
        # Cheking if the move is right for the Queen
        elif self.board[start[1]][start[0]][0] == 4:
            if (abs(y_move) == abs(x_move) and x_move != 0) or start[0]-end[0] == 0 or start[1]-end[1] == 0:
                if self.check_if_blocked(start, end, color):
                    return True
                else:
                    return False
            else:
                return False
        # Cheking if the move is right for the King
        elif self.board[start[1]][start[0]][0] == 5:
            if abs(x_move) <= 1 and abs(y_move) <= 1:
                return True
            else:
                return False
        # Cheking if the move is right for a Pawn
        elif self.board[start[1]][start[0]][0] == 6:
            if self.board[start[1]][start[0]][1] == 'W':
                if 8-start[1] == 2:
                    if x_move == 0:
                        if 0 < -y_move <= 2 and self.board[end[1]][end[0]][0] == 0:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == 1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False

                else:
                    if x_move == 0:
                        if 0 < -y_move <= 1 and self.board[end[1]][end[0]][0] == 0:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == 1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
            if self.board[start[1]][start[0]][1] == 'B':
                if 8-start[1] == 7:
                    if x_move == 0:
                        if 0 > -y_move >= -2 and self.board[end[1]][end[0]][0] == 0:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == -1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False

                else:
                    if x_move == 0:
                        if 0 > -y_move >= -1 and self.board[end[1]][end[0]][0] == 0:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == -1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
        else:
            return True

    def undo(self):
        self.board = self.previous_board


if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.draw_chessboard()

    while True:
        start = input("White start: ")
        if start == 'previous':
            chessboard.undo()
            chessboard.draw_chessboard()
            continue
        end = input("White end: ")

        while not chessboard.move(start, end, 'W'):
            start = input("White start: ")
            if start == 'previous':
                chessboard.undo()
                chessboard.draw_chessboard()
                continue
            end = input("White end: ")
        
        chessboard.draw_chessboard()

        start = input("Black start: ")
        if start == 'previous':
            chessboard.undo()
            chessboard.draw_chessboard()
            continue
        end = input("Black end: ")

        while not chessboard.move(start, end, 'B'):
            start = input("Black start: ")
            if start == 'previous':
                chessboard.undo()
                chessboard.draw_chessboard()
                continue
            end = input("Black end: ")
        
        chessboard.draw_chessboard()
