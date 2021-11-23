'''Main file for chess game'''
import numpy as np
import pieces

board = [[' ', ' ', ' ', 'bk ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'wp', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'K', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
         ]

if __name__ == '__main__':
    sample = pieces.Piece('white', (4, 5))
    print(sample.location)
    print(sample.colour)
    print(sample.total_locat())
    sample_rook = pieces.Rook('black', (2, 3))
    print(np.array(sample_rook.possible_moves(board)))
    print('maybe')
