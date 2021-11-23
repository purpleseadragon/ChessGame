'''Main file for chess game'''
import numpy as np
import pieces

board = [['  ', '  ', '  ', '  ', 'bp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'wp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', 'wp', 'wp', '  ', '  ', '  ', 'bp', 'wh'],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'bp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'wp', '  ', '  ', '  ']
         ]

if __name__ == '__main__':
    sample = pieces.Piece('white', (4, 5), board)
    print(sample.location)
    print(sample.colour)
    sample_rook = pieces.Rook('white', (3, 4), board)
    print(np.array(sample_rook.possible_moves()))
    print(sample_rook.move_piece((3, 6)))
    print(sample_rook.location)
    print(sample_rook.move_piece((6, 6)))
    print(sample_rook.location)
    print(sample_rook.print_board())