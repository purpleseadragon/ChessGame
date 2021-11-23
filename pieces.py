"""File that contains piece classes"""

class Piece:
    def __init__(self, colour, location):
        """Create a piece object with location information"""
        self.colour = colour
        self.location = location
        self._has_moved = False
        self._colour_letter = self.colour[0]

    def total_locat(self):
        """Test method"""
        return self.location[0] * self.location[1]

    def move(self, board):
        pass

    def letter(self):
        """returns letter that represents that piece, i.e N for knight"""
        return 'yo no lo'


class Rook(Piece):
    def possible_moves(self, board):
        """returns list of possible moves for the given board state"""
        # board always square
        # rook moves up-down, left-right
        # check possible moves not yet considering other pieces
        # self.location[0][1] is vertical coord 0 horizontal 1 ??????
        possible_horizontal = []
        possible_vertical = []
        row = self.location[0]
        column = self.location[1]
        # for num in range(len(board)):
        #     if num != column:
        #         possible_horizontal.append((row, num))
        #     if num != row:
        #         possible_vertical.append((num, column))
        lower_vertical_list = list(range(row))
        lower_vertical_list.reverse()

        for num in lower_vertical_list:
            if board[num][column] == ' ':
                possible_vertical.append((num, column))
            elif board[num][column][0] != self._colour_letter:
                possible_vertical.append((num, column))
                break
            else:
                break

        sample_board = board.copy()

        possible = possible_vertical + possible_horizontal
        for coord in possible:
            sample_board[coord[0]][coord[1]] = 'x'
        sample_board[row][column] = 'R'

        # check if any piece in the way

        return sample_board
    


