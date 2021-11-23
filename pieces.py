"""File that contains piece classes"""
import numpy as np

class Piece:
    def __init__(self, colour, location, board):
        """Create a piece object with location information"""
        self.colour = colour
        self.location = location
        self.board = board
        self._has_moved = False
        self._colour_letter = self.colour[0]


    def move_piece(self, board, move):
        pass

    def letter(self):
        """returns letter that represents that piece, i.e N for knight"""
        return 'yo no lo'

    def print_board(self):
        return np.array(self.board)


class Rook(Piece):
    def possible_moves(self):
        """returns list of possible moves for the given board state"""
        # board always square
        # rook moves up-down, left-right
        # check possible moves not yet considering other pieces
        # self.location[0][1] is vertical coord 0 horizontal 1 ??????
        possible_horizontal = []
        possible_vertical = []
        row = self.location[0]
        column = self.location[1]


        lower_vertical_range = list(range(row))
        lower_vertical_range.reverse()
        upper_vertical_range = list(range(len(self.board)-row-1))
        for x, num in enumerate(upper_vertical_range):
            upper_vertical_range[x] += row + 1

        possible_vertical += rook_move_helper_column(lower_vertical_range, self._colour_letter, self.board, column)
        possible_vertical += rook_move_helper_column(upper_vertical_range, self._colour_letter, self.board, column)

        lower_horizontal_range = list(range(column))
        lower_horizontal_range.reverse()
        upper_horizontal_range = list(range(len(self.board)-column-1))
        for x, num in enumerate(upper_horizontal_range):
            upper_horizontal_range[x] += column + 1

        possible_horizontal += rook_move_helper_row(lower_horizontal_range, self._colour_letter, self.board, row)
        possible_horizontal += rook_move_helper_row(upper_horizontal_range, self._colour_letter, self.board, row)

        possible = set(possible_vertical + possible_horizontal)
        # sample_board = board.copy()
        #
        # for coord in possible:
        #     sample_board[coord[0]][coord[1]] = 'x '
        # sample_board[row][column] = 'R '
        return possible

    def move_piece(self, move):
        if move in self.possible_moves():
            self.board[self.location[0]][self.location[1]] = '  '
            self.location = move
            self.board[self.location[0]][self.location[1]] = 'gp'  # gp is placeholder name
        else:
            return 'Pick a valid move pls'


def rook_move_helper_column(moves_range, colour_letter, board, column):
    # helps with creating possible moves
    possible_moves_list = []
    for num in moves_range:
        if board[num][column] == '  ':
            possible_moves_list.append((num, column))
        elif board[num][column][0] != colour_letter:
            possible_moves_list.append((num, column))
            break
        else:
            break
    return possible_moves_list


def rook_move_helper_row(moves_range, colour_letter, board, row):
    # helps with creating possible moves
    possible_moves_list = []
    for num in moves_range:
        if board[row][num] == '  ':
            possible_moves_list.append((row, num))
        elif board[row][num][0] != colour_letter:
            possible_moves_list.append((row, num))
            break
        else:
            break
    return possible_moves_list
