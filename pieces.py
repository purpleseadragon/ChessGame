"""File that contains piece classes"""
from helper_functions import rook_move_helper_column, rook_move_helper_row


class Piece:
    def __init__(self, colour, location, board):
        """Create a piece object with location information"""
        self.colour = colour
        self.location = location
        self.board = board
        self._has_moved = False
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
            self._has_moved = True
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
        check makes it so first piece of same colour is also considered"""
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

        possible = set(possible_vertical + possible_horizontal)
        # sample_board = board.copy()
        #
        # for coord in possible:
        #     sample_board[coord[0]][coord[1]] = 'x '
        # sample_board[row][column] = 'R '
        return possible

    def letter(self):
        return 'R'


class King(Piece):
    """King class"""
    def possible_moves(self, check=False):
        """Does not include moves that would put king in check,
        these will be covered in main loop"""
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


class Queen(Piece):
    def letter(self):
        return 'Q'


class Bishop(Piece):
    def letter(self):
        return 'B'


class Pawn(Piece):
    def letter(self):
        return ''


class Knight(Piece):
    def letter(self):
        return 'N'
