"""File that contains piece classes"""
from helper_functions import rook_move_helper_column, rook_move_helper_row


class Piece:
    def __init__(self, colour, location, board):
        """Create a piece object with location information"""
        self.colour = colour
        self.location = location
        self.board = board
        self.has_moved = False
        self._colour_letter = self.colour[0]
        self.name = f'{self._colour_letter}{self.letter()}'
        self.board[self.location[0]][self.location[1]] = self.name
        self.coord_dict_rows = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
        self.coord_dict_columns = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def move_piece(self, move):
        if move in self.possible_moves():
            self.board[self.location[0]][self.location[1]] = '  '
            self.location = move
            self.board[self.location[0]][self.location[1]] = f'{self._colour_letter}{self.letter()}'
        else:
            return 'Pick a valid move pls'

    def letter(self):
        """returns letter that represents that piece, eg N for knight"""
        return 'implement this'

    def print_board(self, colour):
        if colour == 'white':
            for row in self.board:
                print(row)
        reversed_board = self.board[::-1]
        # prints board other way for black
        if colour == 'black':
            for row in reversed_board:
                print(row[::-1])
        # print([self.coord_dict_rows[num]] + row)
        # print(list(self.coord_dict_columns.values()))

    def return_board(self):
        return self.board

    def possible_moves(self, check=False):
        return 'implement this'

    def possible_moves_notation(self, check=False):
        chess_notation_list = []
        for row, column in self.possible_moves(check):
            chess_notation_list.append(f'{self.coord_dict_columns[column]}{self.coord_dict_rows[row]}')
        chess_notation_list.sort()
        return chess_notation_list


class Rook(Piece):
    """Rook class"""
    def possible_moves(self, check=False):
        """returns list of possible moves for the given board state,
        check makes it so first piece of same colour is also considered,
        Rook can move along rows and columns"""
        # board always square
        # rook moves up-down, left-right
        # check possible moves not yet considering other pieces
        possible_horizontal = []
        possible_vertical = []
        row = self.location[0]
        column = self.location[1]

        # setup of possible vertical moves
        lower_vertical_range = list(range(row))
        lower_vertical_range.reverse()
        upper_vertical_range = list(range(len(self.board)-row-1))
        for x, num in enumerate(upper_vertical_range):
            upper_vertical_range[x] += row + 1

        possible_vertical += rook_move_helper_column(lower_vertical_range, self._colour_letter, self.board, column,
                                                     check)
        possible_vertical += rook_move_helper_column(upper_vertical_range, self._colour_letter, self.board, column,
                                                     check)

        # setup of possible horizontal moves
        lower_horizontal_range = list(range(column))
        lower_horizontal_range.reverse()
        upper_horizontal_range = list(range(len(self.board)-column-1))
        for x, num in enumerate(upper_horizontal_range):
            upper_horizontal_range[x] += column + 1

        possible_horizontal += rook_move_helper_row(lower_horizontal_range, self._colour_letter, self.board, row, check)
        possible_horizontal += rook_move_helper_row(upper_horizontal_range, self._colour_letter, self.board, row, check)

        possible = possible_vertical + possible_horizontal
        return possible

    def letter(self):
        return 'R'


class King(Piece):
    """King class"""
    def possible_moves(self, check=False):
        """Does not include moves that would put king in check,
        these will be covered in main loop, King can move one spot in any direction"""
        lower_horizontal = []
        lower_vertical = []
        upper_horizontal = []
        upper_vertical = []
        lower_left_diag = []
        lower_right_diag = []
        upper_left_diag = []
        upper_right_diag = []
        row = self.location[0]
        column = self.location[1]

        if row != 0:
            if self.board[row-1][column][0] != self._colour_letter or check:
                lower_vertical = [(row - 1, column)]
            if column != 0:
                if self.board[row - 1][column-1][0] != self._colour_letter or check:
                    upper_left_diag = [(row-1, column-1)]
            if column != 7:
                if self.board[row - 1][column + 1][0] != self._colour_letter or check:
                    upper_right_diag = [(row-1, column+1)]

        if row != 7:
            if self.board[row+1][column][0] != self._colour_letter or check:
                upper_vertical = [(row + 1, column)]
            if column != 0:
                if self.board[row+1][column-1][0] != self._colour_letter or check:
                    lower_left_diag = [(row+1, column-1)]
            if column != 7:
                if self.board[row+1][column+1][0] != self._colour_letter or check:
                    lower_right_diag = [(row+1, column+1)]

        if column != 0:
            if self.board[row][column-1][0] != self._colour_letter or check:
                lower_horizontal = [(row, column-1)]

        if column != 7:
            if self.board[row][column+1][0] != self._colour_letter or check:
                upper_horizontal = [(row, column+1)]

        possible = upper_vertical + upper_horizontal + lower_vertical + lower_horizontal + \
            lower_left_diag + lower_right_diag + upper_right_diag + upper_left_diag

        return possible

    def letter(self):
        return 'K'

    def castling_possible(self, side='kingside'):
        pass


class Queen(Piece):
    """Queen class"""
    def possible_moves(self, check=False):
        """Queen combines the movesets of the rook and bishop"""
        possible_horizontal = []
        possible_vertical = []
        row = self.location[0]
        column = self.location[1]

        # setup of possible vertical moves
        lower_vertical_range = list(range(row))
        lower_vertical_range.reverse()
        upper_vertical_range = list(range(len(self.board) - row - 1))
        for x, num in enumerate(upper_vertical_range):
            upper_vertical_range[x] += row + 1

        possible_vertical += rook_move_helper_column(lower_vertical_range, self._colour_letter, self.board, column,
                                                     check)
        possible_vertical += rook_move_helper_column(upper_vertical_range, self._colour_letter, self.board, column,
                                                     check)

        # setup of possible horizontal moves
        lower_horizontal_range = list(range(column))
        lower_horizontal_range.reverse()
        upper_horizontal_range = list(range(len(self.board) - column - 1))
        for x, num in enumerate(upper_horizontal_range):
            upper_horizontal_range[x] += column + 1

        possible_horizontal += rook_move_helper_row(lower_horizontal_range, self._colour_letter, self.board, row, check)
        possible_horizontal += rook_move_helper_row(upper_horizontal_range, self._colour_letter, self.board, row, check)

        possible_rook = possible_vertical + possible_horizontal

        # Bishop code
        valid_squares = [0, 1, 2, 3, 4, 5, 6, 7]
        squares_range = [1, 2, 3, 4, 5, 6, 7]
        possible_left_up = []
        possible_left_down = []
        possible_right_up = []
        possible_right_down = []

        # Bottom right diagonal
        for num in squares_range:
            if (row+num in valid_squares) and (column+num in valid_squares):
                if self.board[row+num][column+num] == '  ':
                    possible_right_down += [(row+num, column+num)]
                else:
                    if check:
                        possible_right_down += [(row+num, column+num)]
                        break
                    elif not check:
                        if self.board[row+num][column+num][0] != self._colour_letter:
                            possible_right_down += [(row+num, column+num)]
                            break
                        else:
                            break
            else:
                break

        # Bottom left diagonal
        for num in squares_range:
            if (row+num in valid_squares) and (column-num in valid_squares):
                if self.board[row+num][column-num] == '  ':
                    possible_left_down += [(row+num, column-num)]
                else:
                    if check:
                        possible_left_down += [(row+num, column-num)]
                        break
                    elif not check:
                        if self.board[row+num][column-num][0] != self._colour_letter:
                            possible_left_down += [(row+num, column-num)]
                            break
                        else:
                            break
            else:
                break

        # Top right diagonal
        for num in squares_range:
            if (row-num in valid_squares) and (column+num in valid_squares):
                if self.board[row-num][column+num] == '  ':
                    possible_right_up += [(row-num, column+num)]
                else:
                    if check:
                        possible_right_up += [(row-num, column+num)]
                        break
                    elif not check:
                        if self.board[row-num][column+num][0] != self._colour_letter:
                            possible_right_up += [(row-num, column+num)]
                            break
                        else:
                            break
            else:
                break

        # Top left diagonal
        for num in squares_range:
            if (row-num in valid_squares) and (column-num in valid_squares):
                if self.board[row-num][column-num] == '  ':
                    possible_left_up += [(row-num, column-num)]
                else:
                    if check:
                        possible_left_up += [(row-num, column-num)]
                        break
                    elif not check:
                        if self.board[row-num][column-num][0] != self._colour_letter:
                            possible_left_up += [(row-num, column-num)]
                            break
                        else:
                            break
            else:
                break
        possible_bishop = possible_right_up + possible_left_up + possible_left_down + possible_right_down
        possible = possible_rook + possible_bishop
        return possible

    def letter(self):
        return 'Q'


class Bishop(Piece):
    """Bishop class"""
    def possible_moves(self, check=False):
        """Bishop can move diagonally in any direction"""
        row = self.location[0]
        column = self.location[1]
        valid_squares = [0, 1, 2, 3, 4, 5, 6, 7]
        squares_range = [1, 2, 3, 4, 5, 6, 7]
        possible_left_up = []
        possible_left_down = []
        possible_right_up = []
        possible_right_down = []

        # Bottom right diagonal
        for num in squares_range:
            if (row+num in valid_squares) and (column+num in valid_squares):
                if self.board[row+num][column+num] == '  ':
                    possible_right_down += [(row+num, column+num)]
                else:
                    if check:
                        possible_right_down += [(row+num, column+num)]
                        break
                    elif not check:
                        if self.board[row+num][column+num][0] != self._colour_letter:
                            possible_right_down += [(row+num, column+num)]
                            break
                        else:
                            break
            else:
                break

        # Bottom left diagonal
        for num in squares_range:
            if (row+num in valid_squares) and (column-num in valid_squares):
                if self.board[row+num][column-num] == '  ':
                    possible_left_down += [(row+num, column-num)]
                else:
                    if check:
                        possible_left_down += [(row+num, column-num)]
                        break
                    elif not check:
                        if self.board[row+num][column-num][0] != self._colour_letter:
                            possible_left_down += [(row+num, column-num)]
                            break
                        else:
                            break
            else:
                break

        # Top right diagonal
        for num in squares_range:
            if (row-num in valid_squares) and (column+num in valid_squares):
                if self.board[row-num][column+num] == '  ':
                    possible_right_up += [(row-num, column+num)]
                else:
                    if check:
                        possible_right_up += [(row-num, column+num)]
                        break
                    elif not check:
                        if self.board[row-num][column+num][0] != self._colour_letter:
                            possible_right_up += [(row-num, column+num)]
                            break
                        else:
                            break
            else:
                break

        # Top left diagonal
        for num in squares_range:
            if (row-num in valid_squares) and (column-num in valid_squares):
                if self.board[row-num][column-num] == '  ':
                    possible_left_up += [(row-num, column-num)]
                else:
                    if check:
                        possible_left_up += [(row-num, column-num)]
                        break
                    elif not check:
                        if self.board[row-num][column-num][0] != self._colour_letter:
                            possible_left_up += [(row-num, column-num)]
                            break
                        else:
                            break
            else:
                break
        possible = possible_right_up + possible_left_up + possible_left_down + possible_right_down
        return possible

    def letter(self):
        return 'B'


class Pawn(Piece):
    """Pawn class"""
    # not going to consider last row as piece promotion will be handled elsewhere
    def possible_moves(self, check=False):
        """Pawn can move one spot forward if there is no piece in front of, this is increased
        to two spots if it hasn't moved yet. Pawn can capture diagonally one spot ahead."""
        row = self.location[0]
        column = self.location[1]
        forward_moves = []
        left_capture_moves = []
        right_capture_moves = []
        # Forward moves
        if self.colour == 'white':
            if not self.has_moved:
                forward_move_range = [row-1, row-2]
                for num in forward_move_range:
                    if self.board[num][column] == '  ':
                        forward_moves += [(num, column)]
                    else:
                        break
            elif self.board[row-1][column] == '  ':
                forward_moves = [(row-1, column)]

        elif self.colour == 'black':
            if not self.has_moved:
                forward_move_range = [row+1, row+2]
                for num in forward_move_range:
                    if self.board[num][column] == '  ':
                        forward_moves += [(num, column)]
            elif self.board[row+1][column] == '  ':
                forward_moves = [(row+1, column)]

        # Capture moves
        if self.colour == 'white':
            if column != 0:
                if (self.board[row-1][column-1][0] == 'b') or (check and self.board[row-1][column-1][0] == 'w'):
                    left_capture_moves = [(row-1, column-1)]
            if column != 7:
                if (self.board[row-1][column+1][0] == 'b') or (check and self.board[row-1][column+1][0] == 'w'):
                    left_capture_moves = [(row-1, column+1)]

        if self.colour == 'black':
            if column != 0:
                if (self.board[row+1][column-1][0] == 'w') or (check and self.board[row+1][column-1][0] == 'b'):
                    left_capture_moves = [(row+1, column-1)]
            if column != 7:
                if (self.board[row+1][column+1][0] == 'w') or (check and self.board[row+1][column+1][0] == 'b'):
                    left_capture_moves = [(row+1, column+1)]

        possible = forward_moves + left_capture_moves + right_capture_moves
        return possible

    def letter(self):
        return 'P'


class Knight(Piece):
    """Knight class"""
    def possible_moves(self, check=False):
        """Knight moves in an L shape over other pieces,
        eg. (0,0) attacks (1, 2), (2, 1), +1, +2, -1, -2"""
        row = self.location[0]
        column = self.location[1]
        valid_squares = [0, 1, 2, 3, 4, 5, 6, 7]
        combos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        possible = []
        for x, y in combos:
            if (row + x in valid_squares) and (column + y in valid_squares):
                if self.board[row + x][column + y][0] != self._colour_letter or check:
                    possible += [(row + x, column + y)]
        return possible

    def letter(self):
        return 'N'
